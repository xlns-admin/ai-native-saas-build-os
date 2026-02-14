# Lovable-Rules-of-Engagement__v1.0.md

AI-Native SaaS Build OS
Lovable Build Discipline

Status: Canonical
Applies to: Any change implemented via Lovable in any governed product repository.

---

## 1. Purpose

This document defines the rules of engagement for using Lovable as an implementation agent.

It exists to prevent:
- technical debt accumulation through “quick fixes”,
- schema drift and undocumented architectural changes,
- inconsistent UI patterns and fragmented UX copy,
- untested changes that regress silently,
- documentation that falls behind the product.

Lovable is treated as an execution unit, not a collaborator.

---

## 2. Authority and Precedence

When prompting Lovable, the following precedence order applies:

1. Product contracts in `/contracts/` (architecture, lifecycle, governance).
2. OS doctrine files referenced explicitly in the prompt.
3. Product-level ADRs in `/adr/`.
4. Product requirements, procedures, and build manuals.
5. Lovable output.

If Lovable proposes a change that conflicts with an authoritative artefact, the change must be rejected or escalated via ADR.

---

## 3. Non-Negotiable Build Contract

Lovable must comply with the following constraints on every change:

- TypeScript strict mode is mandatory.
- No `any` in production code.
- No architectural decisions without an ADR reference.
- No schema changes without a schema migration artefact and updated contracts.
- No security boundary changes without updating relevant policies and controls.
- No release-impacting change without tests and a rollback verification checklist.

If Lovable cannot comply, it must halt and request the missing inputs.

---

## 4. Code Quality Standard (Anti-Debt)

### 4.1 TypeScript Discipline
- TypeScript must be used consistently across the codebase.
- `strict: true` must remain enabled.
- `any` is not permitted.
- Use `unknown` and narrow types explicitly.
- Prefer discriminated unions for state machines and conditional flows.
- Prefer typed API clients and typed DTOs at boundaries.

### 4.2 React Discipline
- Functional components only.
- Hooks only.
- No component should exceed a reasonable complexity threshold. Split by responsibility.
- Business logic must not live inside UI components.
- Side-effects must be isolated (effects should be thin, predictable, and dependency-safe).
- Avoid prop drilling where it creates brittleness, prefer explicit state boundaries.

### 4.3 Separation of Concerns
The following structure is mandatory:

- UI components: rendering, layout, interaction.
- Domain logic: pure functions, deterministic behaviour, no UI dependencies.
- Data access: API calls, DB queries, adapters.
- State orchestration: predictable state transitions, explicit error handling.

Rule:
If logic can be unit tested without a browser, it should live outside UI components.

### 4.4 Dependency and Upgrade Safety
- Prefer stable, widely adopted libraries.
- Avoid introducing new dependencies for trivial gains.
- If a new dependency is introduced, include:
  - rationale,
  - maintenance risk,
  - removal plan.

Lovable must not “solve” problems by adding packages without explicit approval.

---

## 5. Comment and Documentation Policy

Comments are allowed only when they add survivable knowledge.

Allowed comment types:
- Decision comments: why this approach, with ADR reference if relevant.
- Invariants: what must remain true.
- Security notes: assumptions, boundaries, data classification constraints.
- Non-obvious behaviour: edge cases that are easy to break.

Not allowed:
- Narrative comments that repeat the code.
- “Temporary” comments without a tracked issue.
- Comments that contain speculative advice.

Docstrings:
- Required for public interfaces, shared utilities, and boundary adapters.

---

## 6. UI Guidance, Tooltips, and User Help

Tooltips and guides must be produced only when triggered.

Trigger conditions:
- A new user workflow is introduced.
- A workflow changes in a way that could confuse an existing user.
- A new concept is introduced that requires definition.

When triggered, Lovable must output:
- tooltip copy for touched screens,
- help text or short guide snippets,
- any required microcopy updates.

Storage rule:
- Tooltip copy must live in a central UI copy file, not embedded randomly in components.
- Help/guide content must live in `/docs/help/` or the product’s chosen canonical docs path.

No tooltip sprawl:
If a tooltip is created, it must have:
- a purpose,
- a target user moment,
- a deprecation rule if the UI becomes self-evident later.

---

## 7. Testing Policy (Mandatory Outputs)

For every change, Lovable must propose tests using the following structure:

### 7.1 Automated Tests
Required where applicable:
- domain logic unit tests,
- permission and boundary tests (especially RLS-related behaviour),
- integration tests for key flows where deterministic.

### 7.2 Manual Test Script
Required when:
- UI workflows change,
- external integrations exist,
- multi-step journeys exist,
- payments, messaging, onboarding, or admin actions are touched.

Manual script must include:
- happy path,
- top 5 edge cases,
- failure path,
- expected UI states,
- data verification steps.

### 7.3 Release Verification Checklist
For release-impacting changes, include:
- smoke checks,
- monitoring expectations,
- rollback verification steps,
- “known risk” notes.

---

## 8. Output Format Requirements (Diff First)

Lovable outputs must be reviewable as changes, not as prose.

Minimum output requirement:
- a clear list of files changed,
- a summary of what changed and why,
- explicit notes on:
  - schema changes,
  - dependency changes,
  - security boundary changes,
  - test additions or missing tests.

If the project uses a Diff Spec document, Lovable must comply with it.

---

## 9. Upgrade Discipline (Reducing Future React Debt)

Lovable must be prompted to avoid “version upgrade nightmares” by enforcing:

- tight typing,
- small composable components,
- business logic extracted to pure modules,
- minimal dependency surface area,
- tests that express behaviour, not implementation details.

When upgrading dependencies:
- apply changes incrementally,
- run tests after each step,
- record breaking changes.

If errors occur:
- Lovable must fix errors without weakening typing or removing constraints.

---

## 10. Lovable Prompt Header (Copy/Paste)

Use this header at the start of every Lovable epic prompt.

### 10.1 Mandatory Prompt Header
Paste this verbatim, then add your feature requirements below.

---
You are implementing changes in this repository under governed Build OS discipline.

You must comply with:
- `/doctrine/lovable/Lovable-Rules-of-Engagement__v1.0.md`
- Any applicable contracts in `/contracts/`
- Any relevant ADRs in `/adr/`

Non-negotiables:
- TypeScript strict mode.
- No `any`.
- No architectural decisions without ADR reference.
- No schema changes without migration artefact and contract updates.
- Provide a diff-style output: files changed, what changed, why, risks, tests.

For this task:
1. Restate the objective as a one-sentence outcome.
2. List assumptions and constraints.
3. Propose the smallest clean change that satisfies the objective.
4. Generate code changes.
5. Generate tests (automated where applicable).
6. Generate manual test script if this touches UI workflows or integrations.
7. Output a release verification checklist if release-impacting.
---

---

## 11. Definition Discipline for UI Concepts

If the change introduces a concept intended to recur in the product UI, Lovable must include exactly one glossary-ready definition sentence, stored in the product’s canonical glossary location.

---

## 12. Compliance with This Document

If Lovable cannot comply with any rule, it must:
- state which rule blocks execution,
- request the missing input,
- halt rather than guessing.

This is deliberate.

---

Version: v1.0
