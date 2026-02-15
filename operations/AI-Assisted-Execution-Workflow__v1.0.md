# AI-Assisted-Execution-Workflow__v1.0

**Classification:** Governance / Operational Procedure  
**Owner:** Build OS Maintainer  
**Applies to:** Rich Media SuperAdmin Execution Console  
**Status:** Draft  
**Review Cycle:** Quarterly  

---

## 1. Purpose

This document defines the structured workflow for AI-assisted software execution using:

- Epics  
- Stories  
- Diff Prompts  
- Batch Runs  
- Evidence Bundles  
- Manual Test Records  

Its purpose is to:

- Ensure deterministic AI execution  
- Prevent undocumented architectural drift  
- Provide audit-grade traceability  
- Preserve separation between planning, execution, and approval  
- Enforce lifecycle gating discipline  

This workflow applies to all AI-generated code submitted via the SuperAdmin execution console.

---

## 2. Definitions

### Epic

Outcome-sized initiative spanning multiple Stories.

- Scope: Weeks  
- Granularity: Strategic  
- Authority: Human-defined only  

Epics define **why**.

---

### Story

Shippable functional slice derived from an Epic.

- Scope: Days  
- Granularity: Deliverable  
- Authority: Human-defined  

Stories define **what**.

A Story may contain multiple Diff Prompts.

---

### Diff Prompt

Atomic AI execution instruction producing one reviewable change set.

- Scope: Hours  
- Granularity: Single PR or logical diff  
- Authority: Executed by AI  

Diff Prompts define **how**, within strict boundaries.

---

### Run (Batch Execution)

A structured submission event that may contain:

- One or more Diff Prompts  
- Ordered execution  
- Shared context  
- Stop-on-failure or independent mode  

Runs define **when and how grouped execution occurs**.

---

### Evidence Bundle

Immutable record of:

- Prompt submitted  
- AI response  
- Files changed  
- PR link  
- CI results  
- Validation status  
- Hash of prompt and output  

Evidence defines **proof**.

---

### Manual Test Record

Human validation artefact required when:

- UI or UX changes exist  
- Behavioural logic cannot be fully validated by automated tests  
- Risk level exceeds automated confidence  

Manual tests define **human verification**.

---

## 3. Workflow Stages

### Stage 1 — Planning

**Owner:** Product / Architect  

**Inputs:**

- Epic defined  
- ADR references identified  
- Acceptance criteria drafted  

**Output:**

- Stories created  
- Stories linked to Epic  

**Risks:**

- Vague scope  
- Missing architectural references  

**Gate:**

- Story must reference parent Epic  
- Story must reference relevant ADR or contract  

---

### Stage 2 — Diff Prompt Authoring

**Owner:** Planner  

Each Diff Prompt must contain:

1. Inputs (contracts, ADRs, schema)  
2. Objective (single sentence)  
3. Scope boundaries (explicit non-goals)  
4. Acceptance criteria  
5. Output requirements  

**Risks:**

- Architectural mutation  
- Hidden side effects  
- Over-broad execution  

**Gate:**

- Prompt cannot modify governance artefacts  
- Prompt must not introduce new architecture without ADR  

---

### Stage 3 — Run Submission

**Owner:** Executor  

A Run includes:

- Run ID  
- Ordered Diff Prompts  
- Execution mode (stop_on_failure or independent)  

On submission:

- Prompt stored immutably  
- Timestamp recorded  
- Hash generated  

**Risks:**

- Dependency drift in stacked prompts  
- Hidden assumptions between prompts  

**Gate:**

- Dependencies declared  
- Cross-reference validation performed  

---

### Stage 4 — AI Execution (Lovable)

Lovable performs diff generation.

System must capture:

- Raw AI output  
- File diffs  
- Commit or PR link  
- Execution duration  

No manual edits allowed before evidence capture.

**Risks:**

- Silent mutation  
- Partial execution  
- Undocumented behaviour  

**Gate:**

- All output captured before merge  

---

### Stage 5 — Automated Validation

System validates:

- CI status  
- Validator rule compliance  
- Forbidden path protection  
- Test coverage (if required)  

If failed:

- Run marked FAILED  
- Story remains in Executing state  

**Risks:**

- CI not wired  
- Validator not enforced  

**Gate:**

- No Story advances without CI success  

---

### Stage 6 — Manual Test (Conditional)

Required when:

- UI or UX modified  
- Non-deterministic behaviour introduced  
- Risk category is High or Critical  

Manual Test Record must include:

- Test script  
- Environment  
- Tester  
- Result  
- Approval signature  
- Timestamp  

**Risks:**

- Rubber stamping  
- Unstructured testing  

**Gate:**

- Story cannot complete without approved Manual Test Record (if required)  

---

### Stage 7 — Story Completion

Story marked **Complete** only when:

- All Diff Prompts succeeded  
- Evidence Bundles exist for each  
- CI green  
- Manual Test approved (if required)  

Epic completion requires all Stories complete.

---

## 4. Canonical Data Model

---

### Epic Model

```yaml
epic_id: string
title: string
description: string
owner: string
created_at: datetime
status: [draft, active, complete, archived]
linked_adrs: array
linked_stories: array
risk_level: [low, medium, high, critical]
```
---

### Story Model
```yaml
story_id: string
epic_id: string
title: string
description: string
acceptance_criteria: array
owner: string
status: [draft, ready, executing, blocked, manual_test, complete]
linked_adrs: array
diff_prompts: array
requires_manual_test: boolean
risk_level: [low, medium, high, critical]
```
---

### Diff Prompt Model

```yaml
diff_prompt_id: string
story_id: string
objective: string
inputs: array
non_goals: array
acceptance_criteria: array
dependencies: array
execution_status: [draft, queued, submitted, succeeded, failed]
run_id: string
evidence_bundle_id: string
```
---

### Run Model

```yaml
run_id: string
submitted_by: string
submitted_at: datetime
execution_mode: [stop_on_failure, independent]
diff_prompts: array
overall_status: [running, failed, succeeded]
```
---

### Evidence Bundle Model

```yaml
evidence_bundle_id: string
diff_prompt_id: string
prompt_hash: string
raw_prompt: string
raw_response: string
files_changed: array
pr_url: string
commit_sha: string
ci_status: [pass, fail]
validator_status: [pass, fail]
timestamp: datetime
```
---

### Manual Test Record Model

```yaml
manual_test_id: string
story_id: string
environment: string
tester: string
test_steps: array
result: [pass, fail]
notes: string
approved_by: string
approval_timestamp: datetime
```
---

## 5. Risk Model

Primary risks mitigated:

- Architectural drift  
- AI hallucinated behaviour  
- Hidden dependency stacking  
- Unverified UI regressions  
- Governance bypass  
- Evidence gaps in audit  

---

## 6. Ownership and Authority

**Planner:**
- Defines Epics, Stories, Prompts  

**Executor:**
- Submits Runs  

**System:**
- Captures evidence  
- Enforces gates  

**Approver:**
- Conducts manual tests  

**Architect:**
- Approves ADR-required changes  

**AI:**
- Executes bounded Diff Prompts only  

AI has no approval authority.

---

## 7. Final Principle

AI-assisted execution is permitted only within:

- Explicit scope  
- Explicit acceptance criteria  
- Explicit validation gates  
- Explicit human accountability  

If a change cannot be traced,  
it did not happen.
