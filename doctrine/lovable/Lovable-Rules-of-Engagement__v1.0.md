---
Document ID: Lovable-Rules-of-Engagement__v1.0
Owner: Build OS Maintainer
Status: Approved
Version: v1.0
Review Cycle: Annual
Classification: Internal Doctrine
Supersedes: None
Applies To: Any change implemented via Lovable in any governed product repository
---

# Lovable Rules of Engagement

AI-Native SaaS Build OS  
Lovable Implementation Discipline

---

## 1. Purpose

This document defines the mandatory rules for using Lovable as an implementation agent within governed product repositories.

It exists to prevent:

- Technical debt accumulation through uncontrolled “quick fixes”
- Schema drift and undocumented architectural change
- Inconsistent UI patterns and fragmented UX behaviour
- Untested changes that regress silently
- Documentation lagging behind product reality

Lovable operates as a deterministic implementation agent under human authority.  
It does not own architectural decisions.

---

## 1.1 Non-Goals

This document does not:

- Replace architectural review processes
- Define feature requirements
- Replace CI enforcement
- Override product contracts
- Permit autonomous architectural evolution

It governs execution discipline only.

---

## 2. Authority and Precedence

When prompting Lovable, the following authority order applies:

1. Product contracts in `/contracts/`
2. OS doctrine explicitly referenced
3. Product ADRs in `/adr/`
4. Product requirements and build manuals
5. Lovable output

If Lovable proposes changes conflicting with higher authority artefacts, the change must be rejected or escalated via ADR.

---

## 3. Non-Negotiable Build Constraints

Lovable must comply with the following constraints on every change:

- TypeScript strict mode enabled
- No `any` in production code
- No architectural decisions without ADR reference
- No schema change without migration artefact and contract update
- No security boundary modification without updating relevant policies
- No release-impacting change without tests and rollback checklist

If compliance is impossible, Lovable must halt and request missing inputs.

---

## 4. Code Quality and Anti-Debt Standard

### 4.1 TypeScript Discipline

- `strict: true` must remain enabled
- `any` is prohibited
- Use `unknown` and narrow explicitly
- Prefer discriminated unions for conditional flows
- Enforce typed DTOs at system boundaries

Type weakening to “make it compile” is forbidden.

---

### 4.2 React Discipline

- Functional components only
- Hooks only
- Components must remain single-responsibility
- Business logic must not reside inside UI components
- Effects must be thin, predictable, and dependency-safe
- Avoid unnecessary prop drilling; define explicit state boundaries

---

### 4.3 Separation of Concerns

Mandatory structure:

- UI Layer — rendering and interaction only
- Domain Layer — pure deterministic functions
- Data Layer — adapters and integration calls
- State Orchestration — explicit state transitions and error handling

Rule:

If logic can be unit tested without a browser, it must not live inside UI components.

---

### 4.4 Dependency Discipline

- Prefer stable, widely adopted libraries
- Avoid adding dependencies for trivial utility
- Every new dependency must include:
  - Rationale
  - Maintenance risk
  - Removal strategy

Lovable must not introduce packages without explicit approval.

---

## 5. Documentation and Comment Policy

Comments are permitted only when they add survivable knowledge.

Allowed:

- Decision comments referencing ADRs
- Invariants that must remain true
- Security boundary notes
- Non-obvious edge-case behaviour

Not allowed:

- Comments that repeat obvious code
- “Temporary” comments without tracked issue
- Speculative commentary

Public interfaces and shared utilities require docstrings.

---

## 6. UI Guidance and Tooltip Governance

Tooltips and guides are produced only when triggered.

Trigger conditions:

- New user workflow introduced
- Existing workflow materially changed
- New recurring concept introduced

When triggered, Lovable must generate:

- Tooltip copy
- Help text snippet
- Updated UI microcopy where applicable

Storage rule:

- Tooltip copy must live in a central UI copy file
- Help content must live in canonical documentation path

No tooltip may exist without defined user purpose.

---

## 7. Testing Policy

Testing artefacts are mandatory outputs.

### 7.1 Automated Tests

Required where applicable:

- Domain logic unit tests
- Permission and boundary tests
- Deterministic integration tests

---

### 7.2 Manual Test Script

Required when:

- UI workflows change
- External integrations exist
- Multi-step journeys exist
- Payments, messaging, onboarding, or admin flows are modified

Manual script must include:

- Happy path
- Top 5 edge cases
- Failure path
- Expected UI states
- Data validation checks

---

### 7.3 Release Verification Checklist

For release-impacting changes include:

- Smoke checks
- Monitoring expectations
- Rollback verification steps
- Known risk summary

---

## 8. Output Requirements (Diff-First Discipline)

Lovable outputs must be reviewable as changes, not prose.

Minimum output:

- Files changed
- What changed
- Why changed
- Risk notes
- Schema impact statement
- Dependency impact statement
- Security boundary impact statement
- Test coverage summary

If a Diff Spec exists, it must be followed.

---

## 9. Upgrade Discipline

To prevent future React or dependency debt:

- Keep components small and composable
- Extract business logic to pure modules
- Minimise dependency surface area
- Write behavioural tests, not implementation tests

During upgrades:

- Apply changes incrementally
- Run tests after each change
- Record breaking changes
- Never weaken typing to satisfy compiler

---

## 10. Mandatory Lovable Prompt Header

The following header must precede every Lovable epic or implementation prompt.

Failure to include this header constitutes a governance breach.

---

### 10.1 Required Prompt Header (Copy Verbatim)

You are implementing changes in this repository under governed Build OS discipline.

You must comply with:
- /doctrine/lovable/Lovable-Rules-of-Engagement__v1.0.md
- Applicable contracts in /contracts/
- Relevant ADRs in /adr/

Non-negotiables:
- TypeScript strict mode enabled
- No `any`
- No architectural decisions without ADR reference
- No schema changes without migration artefact and contract update
- Provide diff-style output (files changed, what changed, why, risks, tests)

Execution Requirements:
1. Restate objective as a one-sentence outcome.
2. List assumptions and constraints.
3. Propose the smallest clean change that satisfies the objective.
4. Generate code changes.
5. Generate automated tests where applicable.
6. Generate manual test script if UI workflows or integrations are affected.
7. Provide a release verification checklist if the change is release-impacting.
8. Also apply Section 3 (Build Contract) and Sections 4–8 (Quality, Docs, UI help, Testing, Output).

---

### 10.2 Enforcement Note

Prompts that omit required constraints may result in:
- Type weakening
- Undocumented schema changes
- Architectural drift
- Incomplete test coverage

The header exists to prevent silent degradation of code quality and governance integrity.

It is mandatory.

---

### 10.3 Mandatory Build Constraints (Include When Applicable)

Include the following constraints in the prompt when relevant to the change:

Code quality constraints:
- TypeScript strict only. No `any`.
- Keep UI components thin. Extract domain logic into pure functions in `/src/domain` or `/src/utils`.
- No new dependencies without explicit approval. If proposing one, include rationale, risk, and removal plan.
- Add tests. At minimum, unit tests for domain logic. If a UI flow changes, include a manual test script.
- If permissions are touched, include explicit RLS/policy verification steps.
- Output changes as a diff summary: files changed, what changed, why, risks, tests added.
---

## 11. Enforcement

Compliance is mandatory.

Violations include:

- Direct architectural modification without ADR
- Schema mutation without contract update
- Type weakening
- Missing required test artefacts
- Unapproved dependency introduction

Violations result in:

- PR rejection
- Reversion of change
- Escalation under Escalation Matrix

Lovable must halt when blocked rather than guess.

---

## 12. Summary

Lovable is an execution unit.

Architecture is human-owned.
Contracts are authoritative.
Tests are mandatory.
Documentation is first-class.
Velocity follows discipline.

---

Version: v1.0
