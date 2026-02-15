# Build-OS-Governance-Charter__v1.1

AI-Native SaaS Build OS  
Governance Doctrine  

---

**Document:** Build-OS-Governance-Charter__v1.1  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.1  
**Review Cycle:** Annual  
**Classification:** Governance  
**Supersedes:** Build-OS-Governance-Charter__v1.0  
**Applies to:** All repositories governed by the AI-Native SaaS Build OS  

---

## Build OS Governance Charter

**Version:** v1.1  
**Status:** Active  

---

## 1. Purpose

This Charter defines the authority, structure, versioning discipline, execution model, and inheritance rules governing the AI-Native SaaS Build Operating System (“Build OS”).

The Build OS is canonical doctrine.  
It is not project documentation.  
It is the system that governs how projects are built.

This Charter exists to:

- Prevent governance drift  
- Preserve architectural consistency  
- Enable auditability at scale  
- Ensure forward compatibility  
- Ensure AI execution remains bounded, deterministic, and reviewable  

---

## 2. Repository Structure Authority

The Build ecosystem is structured into four distinct repository domains.

### 2.1 Canonical Doctrine

**Repository:** `ai-native-saas-build-os`

This repository is the single source of truth for:

- Lifecycle stages  
- Artefact definitions  
- Enforcement logic  
- Security and compliance frameworks  
- Governance doctrine  
- Prompt execution discipline  

No product-specific artefacts are permitted here.

This repository defines the rules.  
It does not execute them.

---

### 2.2 Product Repositories

**Pattern:** `product-name-platform`

Product repositories contain:

- Application code  
- Schema  
- Infrastructure configuration  
- Product-specific documentation  
- Work items (Epics / Stories / Prompts)  

Products inherit from the Build OS.  
They do not redefine it.

---

### 2.3 Product Governance Repositories

**Pattern:** `product-name-governance`

These repositories contain:

- Product-specific policies  
- Customer-facing compliance documentation  
- Audit exports  
- Incident records  
- Operational metrics  

This repository implements doctrine defined in the Build OS.

---

### 2.4 Platform Repositories

Platform repositories contain:

- Runtime implementation  
- Infrastructure as Code  
- Deployment configuration  
- Integration logic  

Platform repositories must remain traceable to the Build OS lifecycle stages.

---

## 3. Naming Convention Standard

File naming follows:

Artefact-Name__vX.Y.ext

Rules:

- No redundant product prefixes inside structured repositories  
- Artefact name describes its function, not its location  
- Version is mandatory  
- Date prefix is not required (Git history provides chronology)  

**Example:**

Threat-Model__v1.0.md

Folder structure provides context.  
Filenames provide identity and version.

---

## 4. Versioning Policy

Build OS artefacts follow semantic versioning.

### 4.1 Major Version (X.0)

Triggered by:

- Structural lifecycle change  
- Governance model redesign  
- Breaking enforcement logic  
- Artefact contract restructuring  

Major versions may require product migration planning.

---

### 4.2 Minor Version (X.Y)

Triggered by:

- New artefact introduction  
- New section added  
- Expanded enforcement rules  
- Additional compliance mapping  

Minor versions must remain backward compatible.

---

### 4.3 Patch Version (X.Y.Z)

Triggered by:

- Wording clarification  
- Typographical corrections  
- Non-structural adjustments  

No behavioural change permitted.

---

## 5. OS Change Control

All changes to the Build OS must:

- Be submitted via Pull Request  
- Receive peer review  
- Increment version number  
- Include changelog entry  
- Include backward compatibility note  

No direct commits to the main branch are permitted.

Changelog entries must state:

- What changed  
- Why it changed  
- Impact on inheriting products  
- Required migration steps, if any  

---

## 6. Work Item and AI Execution Governance

The Build OS formalises the mapping between human planning and AI execution.

### 6.1 Human Planning Units

- **Epic** — Outcome-sized initiative (weeks)  
- **Story** — Shippable slice (days)  
- **Task** — Implementation detail (hours)  

Epics and Stories define intent.  
They do not directly instruct AI execution.

---

### 6.2 AI Execution Units

Lovable operates only via bounded execution prompts.

Approved execution units:

- **Execution Prompt** — Story → Diff  
- **Refactor Prompt** — Debt item → Diff (no behaviour change)  
- **Upgrade Prompt** — Dependency change → Diff + fixes  

AI must not be prompted at Epic level.

If a prompt feels like a project, it must be split.

---

### 6.3 Prompt Identification and Traceability

Prompt IDs enable auditability and replay.

Recommended identifiers:

- `E-###` for Epics  
- `S-###` for Stories  
- `D-###` for Diff Prompts  

**Example:**

- E-012 Billing Foundations  
- S-045 Add invoice list endpoint  
- D-045-01 Implement API endpoint + tests  

Each Story must reference:

- Parent Epic ID  
- Relevant ADRs  
- Relevant Contracts  
- Diff Prompt IDs used for implementation  

Traceability is mandatory.

---

### 6.4 Diff Prompt Structure (Non-Negotiable)

Every Diff Prompt must contain:

1. **Inputs**
   - Contract references  
   - ADR references  
   - Schema constraints  

2. **Objective**
   - One-sentence outcome  

3. **Scope Boundaries**
   - Explicit non-goals  

4. **Acceptance Criteria**

5. **Output Format Requirement**
   - Files changed  
   - Tests added  
   - Manual test script (if required)  
   - Risk notes  

Prompts must produce one reviewable change set.

---

## 7. Architecture Authority

Architecture decisions must not live inside prompts.

Order of authority:

1. Architecture Contract  
2. ADR  
3. Governance Artefacts  
4. Story Definition  
5. Prompt  

If AI proposes architectural change:

- Stop execution  
- Raise ADR  
- Obtain approval  
- Then implement  

AI is an execution unit.  
It is not an architect.

---

## 8. Product Inheritance Rule

Products must:

1. Declare Build OS version in use  
2. Reference that version in governance documentation  
3. Record deviations via ADR  
4. Not modify canonical OS artefacts locally  
5. Not fork OS without formal version declaration  

Undocumented deviation is governance failure.

---

## 9. Machine-Readable Future

The Build OS shall evolve toward machine-validatable governance.

Machine-readable artefacts may include:

- Lifecycle Contract (YAML)  
- Architecture Contract (YAML)  
- Enforcement Policy Contract (YAML)  
- Compliance State Contract (YAML)  

These must:

- Be deterministic  
- Be versioned  
- Be enforceable by CI  
- Be compatible with the Lifecycle Enforcer  

Machine-readable artefacts strengthen human governance.  
They do not replace it.

---

## 10. Drift Prevention Principle

If a product requires altering the Build OS:

1. Formal proposal  
2. Version increment  
3. Migration note  
4. Changelog update  

Silent mutation of doctrine is governance failure.

---

## 11. Longevity Clause

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

## 12. Effective Date

This Charter is effective as of:

**2026-02-13**

---

**Status:** Active  
**Version:** v1.1  


⸻
