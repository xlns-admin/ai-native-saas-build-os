# Build-OS-Governance-Charter__v1.4

AI-Native SaaS Build OS  
Governance Doctrine  

---

**Document:** Build-OS-Governance-Charter__v1.4  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.4  
**Review Cycle:** Annual  
**Classification:** Governance  
**Supersedes:** Build-OS-Governance-Charter__v1.3  
**Applies to:** All repositories governed by the AI-Native SaaS Build OS  


---


## Canonical Entry Point

The repository root README.md and Master-Documentation-Index__vX.Y.md constitute the sole authoritative navigation entry point.

All governance artefacts must be referenced within the Master Documentation Index.

Unindexed artefacts are considered non-canonical.

---

## 1. Purpose

This Charter defines the authority, structure, taxonomy, versioning discipline, execution model, and inheritance rules governing the AI-Native SaaS Build Operating System (“Build OS”).

The Build OS is canonical doctrine.  
It is not project documentation.  
It is the system that governs how projects are built.

This Charter exists to:

- Prevent governance drift  
- Preserve architectural consistency  
- Enforce structural discipline  
- Enable auditability at scale  
- Ensure forward compatibility  
- Ensure AI execution remains bounded, deterministic, and reviewable  
- Prevent repository entropy  

The Build OS governs systems.  
It must therefore govern itself.

---

## Governance Spine

The following artefacts form the governance spine of the AI-Native SaaS Build OS:

- Build-OS-Governance-Charter
- Lifecycle Enforcer
- Lifecycle Execution Table
- Lifecycle-Artefact-Matrix
- Governance-and-Control-Register

These artefacts define structural authority, lifecycle enforcement, artefact discipline, and control ownership.  
All other artefacts inherit from or operate within this spine.

---

## 2. Repository Authority & Domain Model

The Build ecosystem is structured into clearly separated repository domains.

Structural clarity is a governance control.

### 2.1 Canonical Doctrine Repository

Repository: `ai-native-saas-build-os`

This repository is the single source of truth for:

- Lifecycle stages  
- Artefact definitions  
- Enforcement logic  
- Security and compliance frameworks  
- Governance doctrine  
- Prompt execution discipline  
- Structural taxonomy  

No product-specific artefacts are permitted here.

This repository defines rules.  
It does not execute product logic.

### 2.2 Product Repositories

Pattern: `product-name-platform`

Contain:

- Application code  
- Schema  
- Infrastructure configuration  
- Product-specific documentation  
- Work items (Epics / Stories / Prompts)  

Products inherit from the Build OS.  
They do not redefine it.

### 2.3 Product Governance Repositories

Pattern: `product-name-governance`

Contain:

- Product-specific policies  
- Customer-facing compliance documentation  
- Audit exports  
- Incident records  
- Operational metrics  

This repository implements doctrine defined in the Build OS.

### 2.4 Platform Repositories

Contain:

- Runtime implementation  
- Infrastructure as Code  
- Deployment configuration  
- Integration logic  

Platform repositories must remain traceable to Build OS lifecycle stages.

---

## 3. Canonical Repository Taxonomy Rule

The Build OS repository must adhere to a deterministic folder taxonomy.

Structure is policy.

### 3.1 Approved Top-Level Domains

All artefacts must reside within one of the following domains:

- `.github/`
- `architecture/`
- `contracts/`
- `doctrine/`
- `enforcement/`
- `governance/`
- `operations/`
- `security/`
- `tenancy/`
- `validators/`
- `runtime/`
- `templates/`
- `lifecycle/`
- `policies/`
- `examples/`
- `changelog/`

No new top-level folder may be introduced without formal approval.

### 3.2 Domain Separation Rules

- Governance artefacts must not reside in `security/`
- Security policies must not reside in `governance/`
- Runbooks must reside in `operations/`
- Machine-readable rules must reside in `validators/`
- Executable validation utilities must reside in `runtime/`
- Multi-tenant artefacts must reside in `tenancy/`

Ambiguous placement is governance drift.

### 3.3 Folder Drift Prevention

The following are prohibited:

- Duplicate semantic domains  
- Temporary or ad-hoc folders  
- Root-level artefact dumping  
- Silent folder introduction  
- Cross-domain duplication  

All structural changes must:

1. Follow Change Management Protocol  
2. Include rationale  
3. Update Master Documentation Index  
4. Be approved by Architecture Lead  

### 3.4 Deterministic Placement Rule

Every artefact must have:

- One canonical location  
- One declared owner  
- One review cadence  
- One maturity tier  

Duplication without declared intent is governance debt.

---

## 4. Naming Convention Standard

All artefacts must follow:

Artefact-Name__vX.Y.ext

Rules:

- Title Case  
- Hyphen-separated words  
- Double underscore before version  
- Explicit version required  
- No “final”, “latest”, or ambiguous markers  
- No redundant product prefixes within structured domains  

Folder context provides scope.  
Filename provides identity.

---

## 5. Versioning Policy

Build OS artefacts follow semantic versioning.

### 5.1 Major Version (X.0)

Triggered by:

- Structural lifecycle change  
- Governance model redesign  
- Breaking enforcement logic  
- Artefact contract restructuring  

Requires migration note.

### 5.2 Minor Version (X.Y)

Triggered by:

- New artefact introduction  
- New section  
- Expanded enforcement rule  
- Additional compliance mapping  

Must remain backward compatible.

### 5.3 Patch Version (X.Y.Z)

Triggered by:

- Clarification  
- Non-structural refinement  
- Typographical correction  

No behavioural impact permitted.

---

## 6. OS Change Control

All Build OS changes must:

- Be submitted via Pull Request  
- Receive peer review  
- Increment version  
- Include changelog entry  
- Include compatibility statement  

Direct commits to main are prohibited.

---

## 7. Work Item & AI Execution Governance

### 7.1 Human Planning Units

- Epic  
- Story  
- Task  

Epics and Stories define intent.  
They do not directly instruct AI.

### 7.2 AI Execution Units

Approved units:

- Execution Prompt  
- Refactor Prompt  
- Upgrade Prompt  

AI must not be prompted at Epic level.

If a prompt feels like a project, it must be split.

### 7.3 Prompt Traceability

Identifiers:

- E-###  
- S-###  
- D-###  

Each Story must reference:

- Parent Epic  
- Relevant ADRs  
- Relevant Contracts  
- Diff Prompts used  

Traceability is mandatory.

## 7.4 AI-Assisted Execution Workflow Authority

All AI-assisted execution must conform to the AI-Assisted Execution Workflow artefact.

This workflow defines:
- Canonical data models (Epic, Story, Diff Prompt, Run, Evidence Bundle, Manual Test Record)
- Execution gating
- Human approval boundaries
- Evidence capture requirements

No AI-generated code may bypass this workflow.

Deviation requires formal ADR.

---

## 8. Architecture Authority

Authority order:

1. Architecture Contract  
2. ADR  
3. Governance Artefacts  
4. Story  
5. Prompt  

AI is an execution unit.  
It is not an architect.

---

## 9. Lifecycle Sequencing Authority

The Build OS enforces structured lifecycle progression.

The Lifecycle-Artefact-Matrix defines:

- Which artefacts are mandatory at each stage
- The sequencing order of governance maturity
- The gating criteria for progression
- The minimum compliance baseline per lifecycle tier

No product may progress to a subsequent lifecycle stage without:

- Mandatory artefacts present
- Ownership declared
- Version status active
- Required approvals complete

Stage progression is not discretionary.

Undeclared lifecycle skipping constitutes governance drift.

---

## 10. Product Inheritance Rule

Products must:

- Declare Build OS version in use  
- Reference that version in governance docs  
- Record deviations via ADR  
- Not fork OS without version declaration  
- Not silently override doctrine  

Undocumented deviation is governance failure.

---

## 11. Machine-Readable Governance Evolution

Build OS evolves toward deterministic validation.

Machine-readable artefacts must be:

- Versioned  
- Deterministic  
- CI-enforced  
- Backward compatible  

Automation strengthens governance.  
It does not replace accountability.

---

## 12. Drift Prevention Principle

If a product requires altering the Build OS:

1. Formal proposal  
2. Version increment  
3. Migration note  
4. Changelog update  

Silent mutation of doctrine is governance failure.

---

## 13. Longevity Clause

This Charter assumes:

- People leave  
- Context is lost  
- AI evolves  
- Systems scale  

The Build OS must remain:

- Deterministic  
- Versioned  
- Reviewable  
- Auditable  
- Machine-verifiable  

It must survive personnel change.

---

## 14. Effective Date

Effective as of:

2026-02-16

---

Status: Active  
Version: v1.4
