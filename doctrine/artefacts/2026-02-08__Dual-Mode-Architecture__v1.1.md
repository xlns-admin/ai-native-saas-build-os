2026-02-08__SaaS-Build__Dual-Mode-Architecture__v1.1__source.md

Design Principle

The lifecycle stages remain identical.

What changes is:
	•	Artefact depth
	•	Validation strictness
	•	Governance surface area

This prevents cognitive fragmentation.

You don’t maintain two systems.
You maintain one system with selectable enforcement layers.

⸻

Mode Selection Rule (Stage 0)

Before Stage 1 begins, the Orchestrator must declare:

Build Mode:
[ ] Core Mode
[ ] Enterprise Mode

If no mode is selected → BLOCK.

Mode determines which artefacts are mandatory.

⸻

CORE MODE

Designed for:
	•	MVPs
	•	Solo builds
	•	Low regulatory exposure
	•	Internal tools
	•	Proof of concept

Objective:
Move fast without being reckless.

Core Mode Mandatory Controls
	•	Named Human Orchestrator
	•	Product Vision
	•	Functional + Non-functional requirements
	•	Canonical Definitions
	•	Architecture diagram
	•	Schema draft
	•	Orchestration Manifest
	•	Work units + acceptance criteria
	•	Independent review step
	•	Rollback plan
	•	Decision capture

Core Mode does NOT require:
	•	Formal assumption register
	•	Kill criteria
	•	Data classification matrix
	•	Incident protocol
	•	Cost governance framework
	•	Versioning strategy beyond v1
	•	Orchestrator continuity plan

It is disciplined, not bureaucratic.

⸻

ENTERPRISE MODE

Designed for:
	•	External SaaS products
	•	Paid customers
	•	Regulated data
	•	Multi-tenant systems
	•	Investor-backed scale

Objective:
Prevent existential risk.

Enterprise Mode Additional Mandatory Controls

Stage 0
	•	Assumption Register
	•	Kill Criteria

Stage 2
	•	Data Classification Matrix
	•	AI boundary formalisation
	•	Entitlement & Monetisation architecture

Stage 4
	•	Versioning & Deprecation Strategy
	•	Performance Budget
	•	Cost Budget

Stage 8
	•	Audit Logging Standard
	•	Traceability policy

Stage 9
	•	Incident Response Protocol
	•	Escalation model
	•	Monitoring dashboards

Stage 10
	•	Documentation freshness cadence
	•	ADR review cycle

Stage 11
	•	Orchestrator Continuity Plan

Enterprise Mode BLOCKS on any missing governance layer.

⸻

Lifecycle Enforcer Adjustment

The Enforcer now checks:
	1.	Selected Mode
	2.	Required artefacts for that mode
	3.	Stage completeness against mode

It does not change stage names.
It changes enforcement depth.

This is critical.

The structure must remain stable across modes.

⸻

Why This Is Architecturally Clean

You are not reinventing SDLC.

You are layering governance like:
	•	TLS on top of TCP
	•	Kubernetes on top of containers
	•	DevOps on top of Agile

The base lifecycle stays.
The resilience layer changes.

That is elegant systems thinking.

⸻

Psychological Benefit

Core Mode:
	•	Encourages building.
	•	Removes excuse paralysis.
	•	Keeps AI builds tight.

Enterprise Mode:
	•	Signals seriousness.
	•	Reduces investor anxiety.
	•	Survives audit.
	•	Scales beyond founder dependency.

⸻

Implementation Options

We now have three clean architectural paths:

Option A — Two Separate Enforcers

Core Enforcer
Enterprise Enforcer

Simple, but duplicative.

⸻

Option B — Single Enforcer with Mode Flag

Lifecycle Enforcer v1.1
Mode-aware enforcement table.

Most elegant.
Least duplication.
Most scalable.

⸻

Option C — Progressive Escalation

All builds start in Core.
Upgrade to Enterprise Mode when:
	•	Revenue > X
	•	Users > Y
	•	Regulated data introduced
	•	Funding event occurs

This mirrors real-world SaaS evolution.

⸻

