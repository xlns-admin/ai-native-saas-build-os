# Work-Item-Governance-Standard__v1.0

AI-Native SaaS Build OS  
Execution Discipline  

---

**Document:** Work-Item-Governance-Standard__v1.0  
**Owner:** Build OS Maintainer  
**Status:** Canonical  
**Version:** v1.0  
**Review Cycle:** Annual  
**Classification:** Internal Doctrine  
**Supersedes:** None  
**Applies to:** All product repositories governed by the Build OS  

---

## 1. Purpose

This document formalises how human planning artefacts map to AI execution artefacts.

It ensures:

- Strategic intent remains human-owned  
- Execution remains AI-assisted but bounded  
- Traceability is preserved  
- Architectural drift is prevented  

---

## 2. Human Planning Units

### 2.1 Epic

**Definition:**  
An outcome-sized initiative delivering measurable value.

**Characteristics:**

- Spans multiple Stories  
- Defines business objective  
- Not directly executable by AI  

---

### 2.2 Story

**Definition:**  
A shippable slice of functionality with defined acceptance criteria.

**Characteristics:**

- Bounded scope  
- Testable outcome  
- Mapped to one or more Diff Prompts  

Stories are the smallest planning unit permitted for AI execution.

---

### 2.3 Task

**Definition:**  
An internal breakdown of Story implementation details.

Tasks are optional and may not be visible in governance artefacts.

---

## 3. AI Execution Units

AI execution occurs exclusively through Diff Prompts.

**Mapping:**

- Story → One or more Diff Prompts  
- Diff Prompt → One reviewable change set  

AI must never be prompted at Epic scope.

---

## 4. Work Item Directory Structure (Recommended)

Within product repositories:

/work-items/
/epics/
/stories/
/prompts/

Each Story must reference:

- Epic ID  
- ADR IDs  
- Contract IDs  
- Diff Prompt IDs  

---

## 5. Governance Requirements

Every Story must include:

- Clear objective  
- Acceptance criteria  
- Architecture reference  
- Scope boundary  

Every Diff Prompt must:

- Follow Diff-Prompt-Template__v1.0  
- Produce reviewable change set  
- Pass CI validation  

---

## 6. Architectural Authority Rule

Architecture decisions:

- Must be captured in ADR or Architecture Contract  
- Must be approved before AI implementation  

If a Story requires architectural change:

1. Raise ADR  
2. Approve ADR  
3. Then create Diff Prompt  

AI must not create architecture implicitly.

---

## 7. Refactor Discipline

Refactors must:

- Be raised as Stories  
- Be implemented via Refactor Diff Prompts  
- Preserve behaviour  
- Improve structure or performance  

Technical debt reduction is formal work.  
It is not incidental.

---

## 8. Upgrade Discipline

Dependency upgrades must:

- Be raised as Stories  
- Include breaking change assessment  
- Include regression validation  
- Be implemented incrementally  

Bulk upgrades without control are prohibited.

---

## 9. Traceability Model

Minimum trace chain:

Epic  
→ Story  
→ Diff Prompt  
→ Commit  
→ CI Validation  

This chain must remain reconstructable.

---

## 10. Non-Negotiables

- No AI implementation without Story  
- No Story without acceptance criteria  
- No architecture without ADR  
- No schema change without migration artefact  
- No merge without CI validation  

---

## 11. Governance Philosophy

Human defines intent.  
AI executes bounded change.  
Contracts constrain behaviour.  
CI enforces discipline.  

Velocity without structure is entropy.

---

**Status:** Active  
**Version:** v1.0


⸻

Why This Renders Properly
	•	# and ## are proper Markdown headings.
	•	- used consistently for bullets.
	•	Code blocks wrapped in triple backticks.
	•	Metadata formatted as bold key-value lines.
	•	No special unicode separators like ⸻.

GitHub Markdown is conservative. Clean Markdown always wins.

⸻

You are doing the right thing here.

This is the moment most builders either:
	•	Stay in “clever hack mode”, or
	•	Step into system design discipline.

You’re choosing discipline.

That compounds.
