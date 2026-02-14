# CI-Quality-Gate-Policy__v1.0.md
AI-Native SaaS Build OS

Document: CI-Quality-Gate-Policy__v1.0  
Owner: Build OS Maintainer  
Status: Canonical  
Version: v1.0  
Review Cycle: Annual  
Classification: Internal Doctrine  
Applies to: All governed product repositories.

---

## 1. Purpose

This policy ensures every governed product repository establishes CI enforcement at the start of the build.

CI gates are not a “later hardening task”.
They are a prerequisite for safe AI-assisted implementation.

---

## 2. Policy Statement

All governed product repositories MUST implement a CI Quality Gate.

The required CI level MUST be declared in the product’s Build OS declaration and/or product contract.

CI gates MUST be installed no later than Stage 0–1.
If CI gates are missing, the build is non-compliant.

---

## 3. CI Compliance Levels

### Level 1 — Disciplined Builder (Minimum)
Required checks on Pull Requests to main:
- TypeScript typecheck (tsc --noEmit)
- Lint (eslint)
- Tests (if present)
- Build (production build)

### Level 2 — Governed System
All Level 1 checks plus:
- Test coverage threshold (declared per product)
- Dependency audit
- Formatting check (if formatter is used)
- Required status checks enforced on main

### Level 3 — Enterprise Gate
All Level 2 checks plus:
- SAST (e.g., CodeQL)
- Secret scanning / push protection (where available)
- Dependency review (licence and vulnerability checks)
- SBOM generation (where applicable)
- Branch protection + CODEOWNERS enforcement
- Explicit release readiness checks for production deployments

---

## 4. Template Usage

Workflow templates are provided in:
- /templates/ci/

Products MUST instantiate the appropriate workflow template into:
- .github/workflows/

Products MUST NOT modify OS templates locally.
Deviations must be documented via ADR.

---

## 5. Enforcement

A product is BLOCKED if:
- No CI workflow exists for the declared CI level
- CI workflows do not run on Pull Requests to main
- Required package scripts are missing (lint/test/build/typecheck)
- Branch protections required by level are not enabled (L2/L3)

---

## 6. Audit Evidence

Products must be able to provide:
- Workflow file(s) in .github/workflows/
- Recent successful workflow run(s)
- Branch protection settings aligned to required level

---
