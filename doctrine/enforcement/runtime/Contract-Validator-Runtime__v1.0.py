#!/usr/bin/env python3
"""
Contract-Validator-Runtime__v1.0.py

Deterministic YAML contract validator.

Inputs:
  --contract <path/to/contract.yaml>
  --rules    <path/to/validator-rules.yaml>

Exit codes:
  0 = PASS (no BLOCKER/ERROR findings)
  1 = FAIL (any BLOCKER/ERROR findings, or runtime failure)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml  # type: ignore
except Exception:
    print("FAIL: Missing dependency 'pyyaml'. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


SEVERITY_ORDER = {"BLOCKER": 3, "ERROR": 2, "WARN": 1, "INFO": 0}


@dataclass
class Finding:
    rule_id: str
    severity: str
    message: str
    paths: List[str]
    remediation: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "message": self.message,
            "paths": self.paths,
            "remediation": self.remediation,
        }


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    content = path.read_text(encoding="utf-8")
    return yaml.safe_load(content)


def get_path_value(doc: Any, path: str) -> Tuple[bool, Any]:
    """
    Simple dotted path resolver with list indices:
      a.b.c
      agents[0].id
    Returns: (exists, value)
    """
    cur = doc
    parts = []
    for seg in path.split("."):
        if "[" in seg and seg.endswith("]"):
            key, idx_str = seg[:-1].split("[", 1)
            parts.append(key)
            parts.append(int(idx_str))
        else:
            parts.append(seg)

    try:
        for p in parts:
            if isinstance(p, int):
                if not isinstance(cur, list) or p < 0 or p >= len(cur):
                    return False, None
                cur = cur[p]
            else:
                if not isinstance(cur, dict) or p not in cur:
                    return False, None
                cur = cur[p]
        return True, cur
    except Exception:
        return False, None


def set_contains(haystack: Any, needle: Any) -> bool:
    if isinstance(haystack, list):
        return needle in haystack
    if isinstance(haystack, set):
        return needle in haystack
    return False


def is_non_empty_string(v: Any) -> bool:
    return isinstance(v, str) and v.strip() != ""


def is_semver_like(v: Any) -> bool:
    if not isinstance(v, str):
        return False
    return bool(re.fullmatch(r"\d+\.\d+(\.\d+)?", v.strip()))


def normalize_severity(s: str) -> str:
    s = (s or "").strip().upper()
    return s if s in SEVERITY_ORDER else "ERROR"


def format_findings(findings: List[Finding], output: str) -> str:
    if output == "json":
        return json.dumps(
            {
                "status": "FAIL" if any(SEVERITY_ORDER[f.severity] >= SEVERITY_ORDER["ERROR"] for f in findings) else "PASS",
                "findings": [f.to_dict() for f in findings],
            },
            indent=2,
        )
    # text
    lines = []
    status = "FAIL" if any(SEVERITY_ORDER[f.severity] >= SEVERITY_ORDER["ERROR"] for f in findings) else "PASS"
    lines.append(f"STATUS: {status}")
    if not findings:
        return "\n".join(lines)

    # Sort by severity desc, then rule_id
    findings_sorted = sorted(findings, key=lambda f: (-SEVERITY_ORDER[f.severity], f.rule_id))
    for f in findings_sorted:
        lines.append("")
        lines.append(f"[{f.severity}] {f.rule_id}")
        lines.append(f"Message: {f.message}")
        if f.paths:
            lines.append("Paths:")
            for p in f.paths:
                lines.append(f"  - {p}")
        lines.append(f"Remediation: {f.remediation}")
    return "\n".join(lines)


def apply_required_field_rules(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []

    for rule in rules.get("required_fields", []) or []:
        rule_id = rule.get("id", "TAC-REQ-UNKNOWN")
        severity = normalize_severity(rule.get("severity", "BLOCKER"))
        paths = rule.get("paths", []) or []
        message = rule.get("message", "Missing required field(s).")
        remediation = rule.get("remediation", "Add the missing field(s) to the contract.")

        missing = []
        for p in paths:
            exists, val = get_path_value(contract, p)
            if not exists or val is None or (isinstance(val, str) and val.strip() == ""):
                missing.append(p)

        if missing:
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=severity,
                    message=message,
                    paths=missing,
                    remediation=remediation,
                )
            )
    return findings


def apply_enum_rules(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []
    for rule in rules.get("enums", []) or []:
        rule_id = rule.get("id", "TAC-ENUM-UNKNOWN")
        severity = normalize_severity(rule.get("severity", "ERROR"))
        path = rule.get("path")
        allowed = rule.get("allowed", []) or []
        message = rule.get("message", "Value is not in the allowed set.")
        remediation = rule.get("remediation", f"Set {path} to one of: {allowed}")

        if not path:
            continue
        exists, val = get_path_value(contract, path)
        if not exists:
            continue  # missing handled by required_fields
        if val not in allowed:
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=severity,
                    message=f"{message} Got: {val!r}",
                    paths=[path],
                    remediation=remediation,
                )
            )
    return findings


def apply_regex_rules(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []
    for rule in rules.get("regex", []) or []:
        rule_id = rule.get("id", "TAC-REGEX-UNKNOWN")
        severity = normalize_severity(rule.get("severity", "ERROR"))
        path = rule.get("path")
        pattern = rule.get("pattern")
        message = rule.get("message", "Value does not match required format.")
        remediation = rule.get("remediation", "Update the field to match the expected format.")

        if not path or not pattern:
            continue
        exists, val = get_path_value(contract, path)
        if not exists:
            continue
        if not isinstance(val, str) or not re.fullmatch(pattern, val.strip()):
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=severity,
                    message=f"{message} Got: {val!r}",
                    paths=[path],
                    remediation=remediation,
                )
            )
    return findings


def apply_semver_rules(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []
    for rule in rules.get("semver", []) or []:
        rule_id = rule.get("id", "TAC-SEMVER-UNKNOWN")
        severity = normalize_severity(rule.get("severity", "ERROR"))
        path = rule.get("path")
        message = rule.get("message", "Version is not semver-like.")
        remediation = rule.get("remediation", "Use a version string like 1.0 or 1.2.3.")

        if not path:
            continue
        exists, val = get_path_value(contract, path)
        if not exists:
            continue
        if not is_semver_like(val):
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=severity,
                    message=f"{message} Got: {val!r}",
                    paths=[path],
                    remediation=remediation,
                )
            )
    return findings


def apply_cross_field_rules(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    """
    Cross-field rules are expressed as simple invariants to keep the runtime deterministic.
    Rules format:
      - id
        severity
        when:
          path: <path>
          equals: <value> | exists: true
        then:
          require:
            - <path>
          forbid:
            - <path>
          equals:
            - path: <path>
              value: <value>
    """
    findings: List[Finding] = []
    for rule in rules.get("cross_field", []) or []:
        rule_id = rule.get("id", "TAC-XFIELD-UNKNOWN")
        severity = normalize_severity(rule.get("severity", "ERROR"))
        when = rule.get("when", {}) or {}
        then = rule.get("then", {}) or {}
        message = rule.get("message", "Cross-field invariant violated.")
        remediation = rule.get("remediation", "Update the contract to satisfy this invariant.")

        # Evaluate when-clause
        when_path = when.get("path")
        if not when_path:
            continue

        exists, val = get_path_value(contract, when_path)
        when_matches = False
        if "exists" in when:
            when_matches = bool(exists) == bool(when.get("exists"))
        elif "equals" in when:
            when_matches = exists and val == when.get("equals")
        else:
            # default: require the field exists and is truthy
            when_matches = exists and bool(val)

        if not when_matches:
            continue

        violated_paths: List[str] = []

        # require paths
        for p in then.get("require", []) or []:
            ex, v = get_path_value(contract, p)
            if not ex or v is None or (isinstance(v, str) and v.strip() == ""):
                violated_paths.append(p)

        # forbid paths
        for p in then.get("forbid", []) or []:
            ex, _v = get_path_value(contract, p)
            if ex:
                violated_paths.append(p)

        # equals rules
        for eq in then.get("equals", []) or []:
            p = eq.get("path")
            expected = eq.get("value")
            if not p:
                continue
            ex, v = get_path_value(contract, p)
            if not ex or v != expected:
                violated_paths.append(p)

        if violated_paths:
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=severity,
                    message=message,
                    paths=violated_paths,
                    remediation=remediation,
                )
            )
    return findings


def apply_deviation_policy(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    """
    Enforces deviation rules:
    - BLOCKER rules cannot be overridden.
    - Overrides must reference ADR and review_by date.
    Rules format:
      deviations:
        allowed: true/false
        require_fields: [ ... ]
    """
    findings: List[Finding] = []
    policy = rules.get("deviations", {}) or {}
    allowed = bool(policy.get("allowed", True))

    exists, dev = get_path_value(contract, "deviations")
    if not exists:
        return findings

    if not allowed:
        findings.append(
            Finding(
                rule_id="TAC-DEV-001",
                severity="ERROR",
                message="Deviations are not permitted for this contract type.",
                paths=["deviations"],
                remediation="Remove the deviations section.",
            )
        )
        return findings

    if not isinstance(dev, list):
        findings.append(
            Finding(
                rule_id="TAC-DEV-002",
                severity="ERROR",
                message="Deviations must be a list.",
                paths=["deviations"],
                remediation="Set deviations to a list of deviation objects.",
            )
        )
        return findings

    require_fields = policy.get("require_fields", ["rule_id", "justification", "adr_ref", "review_by"])
    for i, item in enumerate(dev):
        if not isinstance(item, dict):
            findings.append(
                Finding(
                    rule_id="TAC-DEV-003",
                    severity="ERROR",
                    message="Each deviation entry must be an object.",
                    paths=[f"deviations[{i}]"],
                    remediation="Replace this entry with an object containing the required fields.",
                )
            )
            continue
        missing = []
        for f in require_fields:
            if f not in item or (isinstance(item.get(f), str) and item.get(f).strip() == ""):
                missing.append(f"deviations[{i}].{f}")
        if missing:
            findings.append(
                Finding(
                    rule_id="TAC-DEV-004",
                    severity="ERROR",
                    message="Deviation entry is missing required fields.",
                    paths=missing,
                    remediation="Populate the missing deviation fields, including ADR reference and review date.",
                )
            )
    return findings


def run_validator(contract: Any, rules: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []

    findings += apply_required_field_rules(contract, rules)
    findings += apply_semver_rules(contract, rules)
    findings += apply_enum_rules(contract, rules)
    findings += apply_regex_rules(contract, rules)
    findings += apply_cross_field_rules(contract, rules)
    findings += apply_deviation_policy(contract, rules)

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Technical Architecture Contract (YAML) against validator rules.")
    parser.add_argument("--contract", required=True, help="Path to the contract YAML file.")
    parser.add_argument("--rules", required=True, help="Path to the validator rules YAML file.")
    parser.add_argument("--output", choices=["text", "json"], default="text", help="Output format.")
    args = parser.parse_args()

    contract_path = Path(args.contract)
    rules_path = Path(args.rules)

    try:
        contract = load_yaml(contract_path)
        rules = load_yaml(rules_path)
    except Exception as e:
        print(f"STATUS: FAIL\n\n[BLOCKER] TAC-RUNTIME-LOAD\nMessage: Failed to load YAML. {e}\nPaths:\n  - {contract_path}\n  - {rules_path}\nRemediation: Ensure both files exist and are valid YAML.", file=sys.stderr)
        return 1

    if not isinstance(contract, dict):
        print("STATUS: FAIL\n\n[BLOCKER] TAC-RUNTIME-001\nMessage: Contract must be a YAML mapping/object.\nPaths:\n  - <root>\nRemediation: Ensure the contract YAML top level is a mapping.", file=sys.stderr)
        return 1

    if not isinstance(rules, dict):
        print("STATUS: FAIL\n\n[BLOCKER] TAC-RUNTIME-002\nMessage: Rules must be a YAML mapping/object.\nPaths:\n  - <rules-root>\nRemediation: Ensure the rules YAML top level is a mapping.", file=sys.stderr)
        return 1

    findings = run_validator(contract, rules)
    report = format_findings(findings, args.output)
    print(report)

    # FAIL if any ERROR or BLOCKER
    should_fail = any(SEVERITY_ORDER[f.severity] >= SEVERITY_ORDER["ERROR"] for f in findings)
    return 1 if should_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
