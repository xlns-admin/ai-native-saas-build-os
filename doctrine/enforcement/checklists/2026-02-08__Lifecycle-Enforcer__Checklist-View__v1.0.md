2026-02-08__Lifecycle-Enforcer__Checklist-View__v1.0.md

Stage 0 — Intent & Authority Lock

Purpose: Prevent accidental building without ownership, scope, or decision authority.

Required
	•	Named Human Orchestrator (single accountable owner)
	•	Explicit problem statement (what is broken, for whom, and why now)
	•	Explicit non-goals (what this product will not attempt)
	•	Success criteria defined in outcomes, not features
	•	Decision authority declared (who can approve, who can veto)

Block if
	•	Multiple decision-makers exist.
	•	Success is defined as “shipping” rather than outcome.

⸻

Stage 1 — Vision & Product Framing

Purpose: Fix meaning before mechanics.

Required
	•	One-page Product Vision (user, pain, value, constraint)
	•	Target user persona(s) with context, not demographics
	•	Core value proposition stated without solution language
	•	Explicit constraints (budget, time, regulatory, team size)

Block if
	•	Vision depends on a specific tool or technology.
	•	User problem cannot be restated without jargon.

⸻

Stage 2 — Scope & Boundary Definition

Purpose: Prevent scope bleed before it begins.

Required
	•	Functional scope (what the system will do)
	•	Non-functional requirements (performance, security, availability)
	•	Data boundaries (what data exists, what does not)
	•	AI boundaries (what AI may generate, what it may not decide)
	•	Explicit out-of-scope list

Block if
	•	AI is allowed to make autonomous product or architectural decisions.
	•	Non-functional requirements are “to be decided later”.

⸻

Stage 3 — Canonical Definitions

Purpose: Stabilise language before design.

Required
	•	All recurring concepts defined with one glossary-ready sentence
	•	No metaphor inside definitions
	•	Terms used consistently across artefacts
	•	No competing definitions for the same term

Block if
	•	A concept is used before being defined.
	•	Definitions drift between documents.

⸻

Stage 4 — Architecture & System Design

Purpose: Decide structure before writing code.

Required
	•	High-level system architecture diagram (conceptual)
	•	Data model / schema draft
	•	Integration points identified
	•	Architectural Decision Records (ADRs) started
	•	Explicit trade-offs recorded (why this, not that)

Block if
	•	Architecture emerges implicitly from code.
	•	Decisions are justified only by convenience.

⸻

Stage 5 — Lifecycle Orchestration Definition

Purpose: Move from “chatting” to execution control.

Required
	•	Canonical Orchestration Manifest defined
	•	Agent roles defined as functions, not personas
	•	Inputs, outputs, constraints for each agent
	•	Shared state declared and locked
	•	Human approval gates defined

Block if
	•	Agents share mutable hidden state.
	•	Roles overlap without authority boundaries.

⸻

Stage 6 — Backlog & Execution Planning

Purpose: Convert intent into executable units.

Required
	•	Work broken into discrete, reviewable units
	•	Acceptance criteria defined per unit
	•	Dependency ordering explicit
	•	Parallelisable work identified
	•	Failure conditions defined per unit

Block if
	•	Tasks are defined as “build X” without acceptance criteria.
	•	Dependencies are implicit or assumed.

⸻

Stage 7 — Implementation (AI-Assisted)

Purpose: Generate artefacts, not decisions.

Required
	•	AI used only within declared boundaries
	•	Code generated from approved specifications
	•	No architectural changes without ADR update
	•	Outputs traceable back to inputs

Block if
	•	AI introduces new concepts or scope.
	•	Code cannot be traced to an approved requirement.

⸻

Stage 8 — Review, Validation & Adversarial Testing

Purpose: Catch confident failure early.

Required
	•	Independent review step (human or adversarial agent)
	•	Security and edge-case analysis performed
	•	Known limitations documented
	•	Human approval before merge or release

Block if
	•	The same agent validates its own output.
	•	Review is skipped due to “confidence”.

⸻

Stage 9 — Release & Operational Readiness

Purpose: Ship deliberately, not optimistically.

Required
	•	Release criteria met
	•	Rollback plan defined
	•	Monitoring and alerting defined
	•	Ownership for incidents assigned

Block if
	•	Release depends on heroics.
	•	No rollback path exists.

⸻

Stage 10 — Documentation & Memory Preservation

Purpose: Prevent context haemorrhage.

Required
	•	Decisions captured (what and why)
	•	Known trade-offs recorded
	•	Open risks logged
	•	System narrative updated

Block if
	•	Knowledge exists only in conversation history.
	•	Rationale is lost once features ship.

⸻

Stage 11 — Post-Delivery Reflection

Purpose: Improve the system, not just the product.

Required
	•	Outcome measured against original success criteria
	•	Gaps between intent and reality identified
	•	Lifecycle failures noted
	•	Playbook updates proposed (versioned)

Block if
	•	Reflection is skipped due to time pressure.
	•	Learnings are not fed back into the system.

⸻

Lifecycle Enforcer Rule (Global)

If a stage is BLOCKED, the system must refuse to advance.
Speed without discipline is debt.
