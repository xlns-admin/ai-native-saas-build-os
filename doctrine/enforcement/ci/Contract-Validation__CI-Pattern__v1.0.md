# Contract-Validation__CI-Pattern__v1.0.md

## Purpose

This document defines the canonical CI pattern for validating **architecture contracts** in product repositories.

The goal is to make contract compliance:
- automatic,
- repeatable,
- enforced at merge time.

## CI Gate Behaviour

The gate must:
- run on every pull request,
- fail the build on any **BLOCKER** or **ERROR** rule violation,
- surface **WARN** findings in logs.

The gate must not:
- depend on developer judgement to “remember to validate,”
- silently pass if the validator cannot run.

## Canonical File Locations

### In the Build OS Repository
- Validator rules:
  - `enforcement/validators/Technical-Architecture-Contract__Validator-Rules__v1.0.yaml`
- Validator spec:
  - `enforcement/validators/Technical-Architecture-Contract__Validator-Spec__v1.0.md`
- CI pattern (this document):
  - `enforcement/ci/Contract-Validation__CI-Pattern__v1.0.md`

### In a Product Repository
Recommended:
- Contract:
  - `governance/architecture/<DATE>__Technical-Architecture-Contract__vX.Y.yaml`
or
  - `architecture/<DATE>__Technical-Architecture-Contract__vX.Y.yaml`

Pin the OS version used in the contract (mandatory).

## Integration Pattern

This CI pattern assumes one of two approaches:

### Pattern A: Vendored Validator (Recommended for determinism)
- Copy the validator runtime and rules into the product repo.
- Pin versions explicitly.
- Run locally and in CI with identical results.

Pros:
- Fully deterministic.
- No external dependency.
- Easy audit.

Cons:
- Requires manual update when OS evolves.

### Pattern B: Remote Import (Acceptable for internal repos)
- Fetch validator rules from a pinned OS commit or tag.
- Execute validator runtime in the product repo.

Pros:
- Central control.
- Faster updates.

Cons:
- Requires strong pinning discipline to avoid drift.

## Required CI Steps

A compliant pipeline must do the following:

1. Identify the contract file path(s).
2. Load validator rules YAML (pinned).
3. Run validator runtime against contract(s).
4. Fail on any BLOCKER or ERROR.
5. Emit a clear failure report.

## Required Failure Modes

CI must fail if:
- contract file is missing,
- contract file is malformed YAML,
- validator rules cannot be loaded,
- validator runtime exits non-zero,
- any BLOCKER or ERROR is found.

CI must not pass on “tooling failure.”

## Developer Workflow

Recommended developer workflow:

- Update the contract YAML as part of architectural change.
- Run validator locally before opening a PR.
- Include ADR references for deviations.

This makes architecture changes:
- explicit,
- reviewable,
- audit-friendly.

## PR Review Guidance

PR reviewers should verify:
- contract version increments when meaning changes,
- deviations are justified and time-bounded,
- production constraints are not weakened without explicit risk acceptance.

## Notes on Extensibility

This pattern is designed to support:
- additional contract types (schema contracts, security posture contracts),
- multiple environments (test, staging, production),
- progressive escalation (Tier 1 to Tier 3 governance).

Keep the runtime generic.
Keep the rules declarative.
Keep the gates strict.
