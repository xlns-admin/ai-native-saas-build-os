# Prompt-Governance-Addendum__v1.0

AI-Native SaaS Build OS  
Enforcement Policy

---

**Document:** Prompt-Governance-Addendum__v1.0  
**Owner:** Build OS Maintainer  
**Status:** Canonical  
**Version:** v1.0  
**Review Cycle:** Annual  
**Classification:** Enforcement Policy  
**Supersedes:** None  
**Applies to:** All AI-assisted execution in governed product repositories  

---

## 1. Purpose

This addendum formalises how prompts are permitted to interact with governed repositories.

Its objectives are to:

- Prevent unstructured AI execution  
- Enforce template discipline  
- Maintain traceability between planning artefacts and code  
- Eliminate undocumented architectural drift  
- Preserve auditability  

AI execution without artefact reference is prohibited.

---

## 2. Core Rule

No AI prompt may generate or modify production code unless it references:

- A Story ID  
- Any relevant ADR ID  
- The active Technical Architecture Contract version  

If these references are missing, execution must be blocked.

---

## 3. Prompt Classification

Every prompt must declare its type:

- ADR Creation Prompt  
- Epic Creation Prompt  
- Story Creation Prompt  
- Diff Prompt (Implementation)  
- Refactor Prompt  
- Documentation Prompt  
- Audit Prompt  

Prompts that do not declare type are non-compliant.

---

## 4. Mandatory Prompt Header

All execution prompts must include the following header:

Prompt Type:
Story ID:
ADR References:
Contract Version:
OS Version:

Scope Boundary:
Explicitly state what this prompt must NOT change.

Absence of any field constitutes a governance violation.

---

## 5. Template Enforcement

The following artefacts are mandatory depending on prompt type:

| Prompt Type        | Required Template              |
|--------------------|-------------------------------|
| ADR Creation       | ADR Template                  |
| Epic Creation      | Epic Template                 |
| Story Creation     | Story Template                |
| Diff Prompt        | Diff-Prompt Template          |
| Refactor Prompt    | Refactor Template             |

Deviation from template structure must be rejected.

---

## 6. Traceability Chain Requirement

Every implementation must be traceable through:

Vision  
→ Epic  
→ Story  
→ ADR (if architecture impacted)  
→ Diff Prompt  
→ Code  
→ Tests  

If any link is missing, execution is incomplete.

---

## 7. Scope Control

Diff Prompts must explicitly declare:

- What files may be changed  
- What files must not be changed  
- Whether schema may be touched  
- Whether dependencies may be touched  

AI may not expand scope silently.

If scope expansion is required:

1. Stop execution.  
2. Request Story update.  
3. Possibly create a new Story.  

---

## 8. Architectural Protection Rule

AI must not:

- Modify system boundaries  
- Alter authentication model  
- Change RLS or permission logic  
- Introduce new infrastructure  
- Add dependencies  

Unless:

- An ADR exists  
- The ADR is referenced in the prompt  
- The ADR status is **Accepted**  

---

## 9. Schema Protection Rule

Any prompt that changes schema must:

- Include a migration artefact  
- Update the architecture contract  
- Declare backward compatibility impact  
- Include rollback instructions  

Schema drift without a migration artefact is a critical violation.

---

## 10. Testing Enforcement

Every Diff Prompt must include:

- Unit tests for domain logic  
- Manual test script if UI changes  
- Permission verification steps if security is affected  
- Release verification checklist if deployment-impacting  

Test omission must block execution.

---

## 11. Dependency Governance

New dependencies require:

- Explicit justification  
- Maintenance risk assessment  
- Removal plan  
- Security consideration  

AI may not introduce packages implicitly.

---

## 12. AI Boundary Enforcement

AI is an execution agent.

AI must not:

- Make product strategy decisions  
- Redefine scope  
- Override governance artefacts  
- Modify contracts  
- Modify OS doctrine  

If governance artefacts require modification:

1. Create ADR  
2. Create OS Pull Request  
3. Do not patch locally  

---

## 13. Failure Mode

If a prompt violates governance:

AI must respond with:

- Rule violated  
- Artefact missing  
- Required corrective action  

Execution must halt.

---

## 14. Enforcement Integration

The Lifecycle Enforcer must:

- Validate prompt headers  
- Verify referenced artefacts exist  
- Ensure template compliance  
- Block execution if non-compliant  

CI may optionally parse prompt metadata for audit logging.

---

## 15. Escalation Protocol

If a prompt reveals structural ambiguity:

1. Stop execution.  
2. Request clarification.  
3. Escalate to ADR if architectural.  
4. Update Story if scope drifted.  
5. Resume only when artefacts are updated.  

---

## 16. Philosophy

Prompt governance exists to:

- Transform AI from improviser into executor  
- Ensure architecture survives founders  
- Preserve enterprise credibility  
- Protect against velocity-induced decay  

Discipline precedes speed.

---

**Status:** Active  
**Version:** v1.0  


⸻
