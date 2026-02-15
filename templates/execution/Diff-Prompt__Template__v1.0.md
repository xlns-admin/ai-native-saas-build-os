# Diff-Prompt-Template__v1.0

AI-Native SaaS Build OS  
Execution Discipline  

---

**Document:** Diff-Prompt-Template__v1.0  
**Owner:** Build OS Maintainer  
**Status:** Canonical  
**Version:** v1.0  
**Review Cycle:** Annual  
**Classification:** Internal Doctrine  
**Supersedes:** None  
**Applies to:** All AI-generated implementation changes in governed product repositories  

---

## 1. Purpose

This template defines the mandatory structure for any AI execution prompt that results in code changes.

A Diff Prompt is the only permitted mechanism for AI-driven implementation.

It exists to ensure:

- Traceability  
- Bounded scope  
- Architectural compliance  
- Reviewable change sets  
- Deterministic execution  

A Diff Prompt must produce **one reviewable change set**.

---

## 2. Prompt Identification

Every Diff Prompt must include a unique identifier.

### Format

D--

**Example:**

D-045-01

Each Diff Prompt must reference:

- Parent Story ID  
- Parent Epic ID  
- Relevant ADR IDs  
- Relevant Contract IDs  

---

## 3. Mandatory Prompt Structure

All Diff Prompts must contain the following sections.

---

### 3.1 Prompt Header (Non-Negotiable)

Include the Lovable Rules-of-Engagement header.

Reference:

- `/doctrine/lovable/Lovable-Rules-of-Engagement__v1.0.md`  
- Applicable contracts in `/contracts/`  
- Relevant ADRs in `/adr/`  

Failure to include this header constitutes a governance breach.

---

### 3.2 Objective (Single Sentence)

Define the outcome clearly.

**Example:**

> Implement a paginated invoice list endpoint with role-based access control.

---

### 3.3 Authority References

List the authoritative artefacts governing the change.

**Example:**

- `Technical-Architecture-Contract__v1.2`  
- `ADR-007 Billing Domain Boundary`  
- `Access-Control-Matrix__v1.0`  

If no architecture reference exists, execution must halt.

---

### 3.4 Scope Boundaries

Explicitly state non-goals.

**Example:**

- No schema change  
- No UI redesign  
- No dependency additions  

This prevents prompt sprawl.

---

### 3.5 Acceptance Criteria

Define behaviourally testable outcomes.

**Example:**

- Endpoint returns invoices for authenticated user  
- Pagination defaults to 20 items  
- 403 returned for unauthorized access  

Acceptance criteria must be deterministic.

---

### 3.6 Required Output Format

AI output must include:

- Files changed  
- Summary of change  
- Risks introduced  
- Automated tests added  
- Manual test script (if UI/integration change)  
- Schema impact note  
- Security impact note  

Prose-only responses are not permitted.

---

## 4. Diff Prompt Types

### 4.1 Execution Prompt

Implements new functionality.

Must include:

- Automated tests  
- Validation checklist  

---

### 4.2 Refactor Prompt

Improves structure without behaviour change.

Must explicitly state:

> No behavioural change.

Tests must confirm parity.

---

### 4.3 Upgrade Prompt

Dependency or runtime change.

Must include:

- Upgrade rationale  
- Breaking change analysis  
- Migration notes  
- Regression validation steps  

---

## 5. Enforcement Rule

If a Diff Prompt:

- Exceeds one change domain  
- Introduces architecture without ADR  
- Modifies schema without migration artefact  
- Weakens typing or test discipline  

Execution must halt.

AI is not permitted to resolve governance gaps autonomously.

---

## 6. Traceability Requirement

Each Story must record:

- Diff Prompt IDs used  
- Commit references  
- CI validation outcome  

This ensures replayability and audit readiness.

---

**Status:** Active  
**Version:** v1.0


⸻
