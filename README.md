# AI-Native SaaS Build OS

Canonical doctrine and enforcement framework for AI-assisted SaaS product builds.

This repository defines the mandatory lifecycle, governance artefacts, architectural contracts, and validation logic required for building compliant, auditable, and enterprise-grade AI-native systems.

---

## Authority Model

This repository is the **source of truth** for:

- Lifecycle stages and enforcement rules
- Canonical artefact templates
- Technical architecture contract schema
- Validation and CI enforcement logic
- Enterprise hardening controls

Product repositories inherit from this OS.
They do not redefine it.

---

## Repository Structure

| Folder | Purpose |
|--------|---------|
| `/templates/` | Canonical artefact templates used by products |
| `/contracts/` | Binding contract specifications |
| `/enforcement/` | Validator rules, runtime, CI integration |
| `/doctrine/` | Governance doctrine and lifecycle definitions |
| `/changelog/` | Version history of the Build OS |

---

## Product Inheritance Rules

All product repositories must:

- Declare the Build OS version used
- Instantiate contracts from `/templates/`
- Store instantiated contracts locally
- Pass validation using OS enforcement rules
- Declare deviations via ADR
- Never modify OS templates directly

The OS is extended via versioned change control, not local mutation.

---

## Versioning Policy

- **Major** → Structural lifecycle or contract change
- **Minor** → New artefact or enforcement addition
- **Patch** → Clarifications or non-breaking refinements

Every change requires:
- Pull Request review
- Version increment
- Changelog entry
- Backward compatibility note

---

## Enforcement Model

All Technical Architecture Contracts must:

- Conform to validator rule schema
- Pass runtime validation
- Pass CI enforcement gate

Failure blocks merge.

---

## Scope

This OS governs:
- Lifecycle discipline
- Architecture contracts
- Security controls
- Compliance mapping
- AI usage boundaries

It does not contain product code.

---

## Ownership

Build OS Owner: `<NAMED_AUTHORITY>`
Change approval requires documented review.

---
