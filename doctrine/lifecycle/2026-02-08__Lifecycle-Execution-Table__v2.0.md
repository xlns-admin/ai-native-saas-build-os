2026-02-08__Lifecycle-Execution-Table__v2.0.md

Lifecycle Execution Table v2.0

(Includes Enterprise Hardening Layer Integration)

This table defines mandatory artefacts per stage.

If Enterprise Level is declared as:
	•	Level 1 — Disciplined Build
	•	Level 2 — Governed System
	•	Level 3 — Enterprise Hardened

Additional artefacts become mandatory.

Progression is blocked if required artefacts for the declared level are missing.

⸻

Stage 0 — Intent & Authority Lock

Core Required (All Levels):
	•	Named Human Orchestrator
	•	Explicit problem statement
	•	Explicit non-goals
	•	Outcome-based success criteria
	•	Decision authority declaration

Level 2+ Additional:
	•	Risk appetite statement
	•	Data sensitivity declaration (initial)

Level 3 Additional:
	•	Regulatory exposure declaration
	•	Compliance intent declaration (e.g. SOC 2 alignment planned)

Block if:
	•	Multiple decision authorities exist
	•	Success defined as “shipping”
	•	Regulatory exposure not declared for Level 3

⸻

Stage 1 — Vision & Product Framing

Core Required:
	•	One-page product vision
	•	User personas with operational context
	•	Value proposition without tool dependency
	•	Explicit constraints

Level 2+ Additional:
	•	Stakeholder map
	•	High-level threat exposure identification

Level 3 Additional:
	•	Business impact classification (low / medium / high criticality)

Block if:
	•	Vision depends on specific tooling
	•	System criticality not declared at Level 3

⸻

Stage 2 — Scope & Boundary Definition

Core Required:
	•	Functional scope
	•	Non-functional requirements
	•	Data boundaries
	•	AI boundaries
	•	Explicit out-of-scope list

Level 2+ Additional:
	•	Preliminary risk register
	•	Availability targets
	•	Performance targets

Level 3 Additional:
	•	Data classification draft
	•	Regulatory control impact notes

Block if:
	•	AI allowed autonomous decision-making
	•	NFRs undefined
	•	Data classification absent for Level 3

⸻

Stage 3 — Canonical Definitions

Core Required:
	•	Glossary-ready definitions
	•	Single meaning per term
	•	No metaphor inside definitions

Level 2+ Additional:
	•	Definition review checkpoint recorded

Level 3 Additional:
	•	Terminology consistency audit (traceable)

Block if:
	•	Terms drift between artefacts
	•	Undefined recurring concepts

⸻

Stage 4 — Architecture & System Design

Core Required:
	•	Architecture diagram
	•	Data model / schema draft
	•	Integration identification
	•	ADR log initiated
	•	Explicit trade-offs

Level 2+ Additional:
	•	Formal threat model (STRIDE or equivalent)
	•	Initial access control model
	•	Logging strategy

Level 3 Additional:
	•	Version-controlled threat model
	•	Access control matrix
	•	Encryption and data residency decisions
	•	Secure SDLC control checklist

Block if:
	•	Architecture implied by code
	•	No threat model at Level 2+
	•	No access model at Level 3

⸻

Stage 5 — Lifecycle Orchestration Definition

Core Required:
	•	Canonical Orchestration Manifest
	•	Agent roles defined as functions
	•	Inputs, outputs, constraints
	•	Shared state declaration
	•	Human approval gates

Level 2+ Additional:
	•	AI Delegation Policy
	•	AI usage boundaries formally documented

Level 3 Additional:
	•	Prompt logging policy
	•	Model usage registry
	•	Authority boundary review

Block if:
	•	Agents share mutable hidden state
	•	Authority boundaries overlap
	•	AI may alter schema or security controls autonomously

⸻

Stage 6 — Backlog & Execution Planning

Core Required:
	•	Discrete work units
	•	Acceptance criteria per unit
	•	Dependency ordering
	•	Failure conditions defined

Level 2+ Additional:
	•	Security acceptance criteria embedded
	•	Risk tags per work unit

Level 3 Additional:
	•	Compliance traceability linkage per work unit
	•	Change management trigger conditions defined

Block if:
	•	Tasks lack acceptance criteria
	•	Dependencies implicit
	•	Security validation not embedded at Level 2+

⸻

Stage 7 — Implementation (AI-Assisted)

Core Required:
	•	Code traceable to requirements
	•	ADR compliance
	•	AI bounded by declared scope
	•	No architecture drift

Level 2+ Additional:
	•	Dependency vulnerability scan
	•	Static analysis pass
	•	Review evidence recorded

Level 3 Additional:
	•	Secure code review logged
	•	Secrets management validation
	•	Control compliance evidence captured

Block if:
	•	AI introduces new scope
	•	Code cannot trace to requirement
	•	Security scanning absent at Level 2+

⸻

Stage 8 — Review & Validation

Core Required:
	•	Independent review
	•	Adversarial testing
	•	Human approval before merge

Level 2+ Additional:
	•	Security validation report
	•	Known limitations documented

Level 3 Additional:
	•	Formal validation sign-off
	•	Control verification evidence
	•	Penetration or threat reassessment if required

Block if:
	•	Self-validation
	•	Review skipped due to confidence
	•	No security validation at Level 2+

⸻

Stage 9 — Release & Operational Readiness

Core Required:
	•	Release criteria defined
	•	Rollback plan
	•	Monitoring defined
	•	Incident ownership declared

Level 2+ Additional:
	•	Incident classification model
	•	Escalation path defined

Level 3 Additional:
	•	Incident Response Playbook
	•	Communication protocol
	•	Audit logging verified
	•	Business continuity considerations

Block if:
	•	No rollback path
	•	No monitoring
	•	No incident protocol at Level 2+

⸻

Stage 10 — Documentation & Memory Preservation

Core Required:
	•	ADRs complete
	•	Trade-offs recorded
	•	Risks logged
	•	System narrative updated

Level 2+ Additional:
	•	Documentation completeness metric
	•	Decision latency tracked

Level 3 Additional:
	•	Evidence repository updated
	•	Compliance mapping matrix updated
	•	Retention policy applied

Block if:
	•	Knowledge exists only in chat history
	•	Compliance traceability absent at Level 3

⸻

Stage 11 — Post-Delivery Reflection

Core Required:
	•	Outcome measured vs success criteria
	•	Lifecycle gaps identified
	•	Lessons captured
	•	Playbook updates proposed

Level 2+ Additional:
	•	Metric performance review
	•	Incident trend analysis

Level 3 Additional:
	•	Control effectiveness review
	•	Risk register updated
	•	Governance refinement logged

Block if:
	•	Reflection skipped
	•	Metrics not reviewed at Level 2+
	•	Controls not reviewed at Level 3

⸻

Global Enterprise Enforcement Rule

If a maturity level is declared:
	•	All artefacts at that level and below become mandatory.
	•	Regression to a lower level requires documented justification.
	•	Release is blocked if declared-level artefacts are incomplete.

⸻
