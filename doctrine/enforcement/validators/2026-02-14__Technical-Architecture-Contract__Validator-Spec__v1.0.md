# 2026-02-14__Technical-Architecture-Contract__Validator-Spec__v1.0.md

## Purpose

This document defines the validator behaviour for the **Technical Architecture Contract** (TAC) in YAML form.

The validator enforces:
- presence of mandatory fields,
- allowed values and formats,
- cross-field consistency rules,
- lifecycle discipline for architecture decisions,
- explicit declaration of deviations.

This is an enforcement artefact. It is not guidance prose.

## Scope

This validator applies to:
- Product repositories that inherit the Build OS.
- Any repository declaring a Technical Architecture Contract YAML.

Out of scope:
- Runtime security testing.
- Infrastructure provisioning.
- Application correctness.

## Inputs

### Contract File
- A single YAML file conforming to the **Technical Architecture Contract** template.

### Validator Rules
- Machine-readable rules file:
  - `enforcement/validators/2026-02-14__Technical-Architecture-Contract__Validator-Rules__v1.0.yaml`

## Output

The validator must produce a deterministic result:

- **PASS**: Contract is valid, consistent, and complete.
- **FAIL**: Contract violates one or more rules.

On FAIL, output must include:
- Rule ID
- Severity
- Human readable failure reason
- Field path(s) involved
- Remediation instruction (what to change)

## Enforcement Levels

Rules are evaluated with explicit severities:

- **BLOCKER**: Must fail CI. Merge is prohibited.
- **ERROR**: Must fail CI unless explicitly overridden.
- **WARN**: Does not fail CI, but must be surfaced.

Override policy:
- Overrides are permitted only for **ERROR** and **WARN**.
- Overrides are prohibited for **BLOCKER**.
- Overrides must be declared in the contract file and reference an ADR.

## Rule Categories

The validator rules are grouped into categories for traceability:

1. **Schema validity**
   - YAML parses correctly.
   - Required top-level keys exist.

2. **Identity and versioning**
   - Contract has stable IDs.
   - Version fields are valid (semver style).
   - OS version pin exists when required.

3. **Provider and environment declarations**
   - Cloud provider and region are explicit.
   - Environment separation rules are honoured.
   - Production constraints are stricter than test.

4. **Security posture**
   - Minimum security settings are declared.
   - Required controls are present (e.g., RLS enabled if relevant).
   - Logging and retention declarations exist.

5. **Data and tenancy**
   - Tenant model is declared.
   - Isolation mechanisms are stated.
   - Shared service boundaries are explicit.

6. **Operational resilience**
   - Backups and recovery posture are declared.
   - Incident ownership and monitoring posture are declared.

7. **MCP and mobile declarations**
   - If MCP is enabled, MCP fields must be complete.
   - If mobile clients exist, mobile security fields must be complete.

8. **Consistency and cross-field invariants**
   - Conflicting settings are rejected.
   - “Future work” placeholders are rejected where disallowed.

## Contract Override Mechanism

If the contract needs to diverge from the template or validator expectations:

- The contract must include an explicit `deviations` section.
- Each deviation must include:
  - affected rule ID(s),
  - justification,
  - associated ADR reference,
  - expiry review date.

Example structure (illustrative):
- deviations:
  - rule_id: TAC-RULE-012
    justification: "Legacy constraint, migration scheduled"
    adr_ref: "ADR-014"
    review_by: "2026-06-30"

## Non-goals

The validator does not:
- infer architecture from code,
- assess correctness of implementation,
- replace human architectural review.

Its role is to prevent silent drift and undocumented risk.

## Change Control

Changes to validator behaviour require:
- PR review,
- version increment of the rules file,
- changelog entry,
- backward compatibility note.

This is mandatory because validator changes impact product repo gates.
