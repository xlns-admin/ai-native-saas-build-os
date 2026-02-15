# Glossary__v1.1

AI-Native SaaS Build OS  
Canonical Terminology

---

**Document:** Glossary__v1.1  
**Owner:** Build OS Maintainer  
**Status:** Canonical  
**Version:** v1.1  
**Review Cycle:** Annual  
**Classification:** Internal Doctrine  
**Supersedes:** Glossary__v1.0  
**Applies to:** All repositories governed by the AI-Native SaaS Build OS  

---

## 1. Purpose

This glossary defines canonical terminology used across:

- Build OS doctrine  
- Product governance repositories  
- Agile delivery processes  
- Enterprise SaaS operations  

Definitions are binding across governed repositories.

If a term appears in doctrine, contracts, ADRs, lifecycle artefacts, or enforcement logic, its meaning is defined here.

---

# Section 1 — Governance & OS Doctrine

---

## Build OS

**Definition:**  
The AI-Native SaaS Build OS is the canonical governance framework defining lifecycle control, architecture contracts, enforcement logic, and compliance discipline across product repositories.

**Elaboration:**  
Products inherit the OS. They do not modify it.

**See:**  
AI-Native-SaaS-Build-OS__v2.3.md  

---

## Architecture Decision Record (ADR)

**Definition:**  
A structured record documenting the context, decision, alternatives considered, and consequences of an architectural choice.

**Elaboration:**  
ADRs prevent silent architectural drift and create traceable decision lineage. Required for architectural deviation from doctrine or contract.

---

## Technical Architecture Contract (TAC)

**Definition:**  
A machine-readable YAML contract declaring the runtime architecture and security posture of a product.

**Elaboration:**  
Validated in CI to prevent misconfiguration and governance breaches.

---

## Lifecycle Stage

**Definition:**  
A formally defined build phase requiring specific artefacts before progression.

**Elaboration:**  
Stages enforce structured evolution from concept to release.

---

## Artefact

**Definition:**  
A versioned, governed document that formalises policy, decision, or specification.

**Elaboration:**  
Artefacts are enforceable documentation units, not informal notes.

---

# Section 2 — Agile & Product Delivery Terms

---

## Scope

**Definition:**  
The defined boundary of work agreed for implementation within a lifecycle stage or sprint.

**Elaboration:**  
Scope must map to requirements and contracts. Scope expansion without documentation is a governance breach.

---

## Requirements Document

**Definition:**  
A formal specification of functional and non-functional expectations for a feature or system.

**Elaboration:**  
Non-functional requirements include performance, security, availability, compliance, and scalability.

---

## Functional Requirement

**Definition:**  
A statement describing what the system must do.

---

## Non-Functional Requirement (NFR)

**Definition:**  
A statement describing how the system must behave or perform.

**Elaboration:**  
Examples include latency targets, security posture, availability SLA, and compliance constraints.

---

## Product Vision

**Definition:**  
A concise statement describing the long-term outcome the product intends to achieve.

**Elaboration:**  
Vision informs roadmap. Contracts enforce execution discipline.

---

## Roadmap

**Definition:**  
A prioritised sequence of future features and strategic initiatives.

**Elaboration:**  
Roadmap informs backlog; lifecycle artefacts govern implementation.

---

## Epic

**Definition:**  
A large body of work that can be broken into smaller deliverable units.

---

## Story (User Story)

**Definition:**  
A small, testable unit of functionality describing user intent and value.

**Elaboration:**  
Stories are the smallest planning unit permitted for AI execution.

---

## Issue

**Definition:**  
A tracked work item including features, bugs, tasks, or refactors.

---

## Sprint

**Definition:**  
A fixed time-boxed iteration during which a defined set of stories is implemented.

---

## Sprint Planning

**Definition:**  
A structured session defining scope for the upcoming sprint.

---

## Sprint Retrospective

**Definition:**  
A structured review session evaluating process, quality, and team effectiveness after a sprint.

---

## Greenlight Meeting

**Definition:**  
A formal approval checkpoint allowing a scoped initiative to proceed to implementation.

**Elaboration:**  
Equivalent to lifecycle stage progression approval.

---

# Section 3 — Engineering & Architecture Terms

---

## Separation of Concerns

**Definition:**  
An architectural principle that isolates distinct responsibilities into independent modules.

**Elaboration:**  
UI, domain logic, data access, and orchestration must remain separate.

---

## Refactor

**Definition:**  
Structural improvement of code without altering external behaviour.

---

## Rebuild

**Definition:**  
Replacement of an internal system component while preserving functional intent.

---

## Re-platform

**Definition:**  
Migration of a system to a new infrastructure or technology stack while maintaining product objectives.

---

## Feature

**Definition:**  
A user-visible capability delivering defined value.

---

## Functionality

**Definition:**  
System behaviour enabling a feature.

---

## Bug

**Definition:**  
A deviation from expected behaviour defined by requirements or contract.

---

## Technical Debt

**Definition:**  
Accumulated future cost created by expedient implementation decisions that compromise maintainability or upgradeability.

**Elaboration:**  
Controlled through strict typing, ADR discipline, schema governance, and upgrade protocols.

---

## Scope Creep

**Definition:**  
Uncontrolled expansion of agreed scope without corresponding documentation or approval.

---

## Release

**Definition:**  
A packaged deployment of changes made available to users.

---

## Time to Value (TTV)

**Definition:**  
The elapsed time between implementation start and delivery of measurable user benefit.

---

# Section 4 — AI-Native & Enforcement Terms

---

## Lifecycle Enforcer

**Definition:**  
The enforcement mechanism blocking lifecycle progression when required artefacts are missing or invalid.

---

## Validator

**Definition:**  
A machine-readable rule set enforcing structural compliance of contracts.

---

## Enforcement Runtime

**Definition:**  
Executable code applying validation rules within CI.

---

## AI Execution Unit

**Definition:**  
A constrained AI agent operating within defined authority and contract boundaries.

---

## Orchestrator

**Definition:**  
The accountable human authority directing AI execution units and approving outputs.

---

## Model Context Protocol (MCP)

**Definition:**  
A structured interface governing how AI agents interact with system tools and boundaries.

---

# Section 5 — Enterprise & Compliance Terms

---

## Access Control Matrix

**Definition:**  
A structured mapping of roles to permissions within a system.

---

## Threat Model

**Definition:**  
A structured analysis identifying potential system attack vectors and mitigation strategies.

---

## Compliance Mapping

**Definition:**  
A documented crosswalk aligning system controls to regulatory frameworks such as SOC 2 or ISO 27001.

---

## Incident

**Definition:**  
A security, availability, or integrity event impacting system operation.

---

## Business Continuity

**Definition:**  
Organisational capability to continue critical operations during disruption.

---

## Disaster Recovery (DR)

**Definition:**  
Technical procedures restoring system operation following catastrophic failure.

---

## 6. Term Governance Rule

New terms introduced into doctrine, contracts, or lifecycle artefacts must:

- Be added to this glossary via Pull Request  
- Include a single-sentence extractable definition  
- Include short elaboration  
- Reference authoritative artefacts where applicable  

Conflicting definitions are prohibited.

Deprecated terms must be explicitly marked and versioned.

---

**Status:** Active  
**Version:** v1.1  
