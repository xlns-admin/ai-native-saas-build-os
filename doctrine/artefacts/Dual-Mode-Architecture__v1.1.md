# Dual-Mode-Architecture__v1.1

AI-Native SaaS Build OS  
Governance Layering Model

---

**Document:** Dual-Mode-Architecture__v1.1__source  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.1  
**Review Cycle:** Annual  
**Classification:** Canonical Doctrine  
**Supersedes:** Dual-Mode-Architecture__v1.0__source  
**Applies to:** All repositories governed by the AI-Native SaaS Build OS  

---

## 1. Purpose

This document defines the Dual-Mode Architecture principle for the AI-Native SaaS Build OS.

The lifecycle stages remain identical.

What changes between modes is:

- Artefact depth  
- Validation strictness  
- Governance surface area  

This prevents cognitive fragmentation.

There are not two systems.

There is one lifecycle with selectable enforcement layers.

---

## 2. Design Principle

The lifecycle structure must remain stable.

Governance depth is layered on top of a fixed stage architecture.

The OS does not fork.
It scales in enforcement density.

This ensures:

- Structural consistency  
- Cognitive simplicity  
- Upgrade clarity  
- Governance continuity  

---

## 3. Mode Selection Rule (Stage 0)

Before Stage 1 begins, the Orchestrator must declare:

Build Mode:
[ ] Core Mode
[ ] Enterprise Mode

If no mode is selected → **BLOCK.**

Mode selection determines mandatory artefacts and enforcement depth.

Mode must be recorded in:

`/governance/build-os.yaml`

---

# 4. Core Mode

### Designed For

- MVPs  
- Solo builds  
- Internal tools  
- Proof of concept systems  
- Low regulatory exposure  
- Non-customer-facing prototypes  

### Objective

Move fast without being reckless.

---

## 4.1 Core Mode Mandatory Controls

- Named Human Orchestrator  
- Product Vision  
- Functional + Non-functional requirements  
- Canonical Definitions  
- Architecture diagram  
- Schema draft  
- Orchestration Manifest  
- Work units with acceptance criteria  
- Independent review step  
- Rollback plan  
- Decision capture (ADR or equivalent)  

---

## 4.2 Core Mode Exclusions

Core Mode does NOT require:

- Formal Assumption Register  
- Kill Criteria  
- Data Classification Matrix  
- Incident Response Protocol  
- Cost Governance Framework  
- Versioning strategy beyond v1  
- Orchestrator Continuity Plan  

Core Mode is disciplined, not bureaucratic.

---

# 5. Enterprise Mode

### Designed For

- External SaaS products  
- Paid customers  
- Regulated data environments  
- Multi-tenant systems  
- Investor-backed scale environments  

### Objective

Prevent existential risk.

Enterprise Mode extends Core Mode with additional mandatory controls.

---

## 5.1 Enterprise Mode Additional Mandatory Controls

### Stage 0
- Assumption Register  
- Kill Criteria  

### Stage 2
- Data Classification Matrix  
- AI boundary formalisation  
- Entitlement & Monetisation architecture  

### Stage 4
- Versioning & Deprecation Strategy  
- Performance Budget  
- Cost Budget  

### Stage 8
- Audit Logging Standard  
- Traceability Policy  

### Stage 9
- Incident Response Protocol  
- Escalation Model  
- Monitoring Dashboards  

### Stage 10
- Documentation freshness cadence  
- ADR review cycle  

### Stage 11
- Orchestrator Continuity Plan  

Enterprise Mode **BLOCKS** on any missing governance layer.

---

# 6. Lifecycle Enforcer Adjustment

The Lifecycle Enforcer must:

1. Detect selected Build Mode  
2. Load required artefact set for that mode  
3. Validate stage completeness against mode requirements  

Stage names do not change.

Enforcement depth changes.

Structural consistency is non-negotiable.

---

# 7. Architectural Rationale

This model layers governance rather than duplicating systems.

It mirrors resilient system design patterns:

- TLS layered over TCP  
- Kubernetes layered over containers  
- DevOps layered over Agile  

The base lifecycle remains stable.

The resilience layer scales with risk exposure.

This is deliberate architectural symmetry.

---

# 8. Psychological and Strategic Effects

### Core Mode

- Encourages building  
- Reduces paralysis  
- Maintains tight AI execution  
- Prevents governance theatre  

### Enterprise Mode

- Signals operational seriousness  
- Reduces investor anxiety  
- Supports audit survival  
- Enables scale beyond founder dependency  

Mode selection is strategic intent made explicit.

---

# 9. Implementation Options

## Option A — Separate Enforcers

- Core Enforcer  
- Enterprise Enforcer  

Simple but duplicative.

---

## Option B — Single Enforcer with Mode Flag

Lifecycle Enforcer v1.1  
Mode-aware enforcement matrix.

Most elegant.  
Least duplication.  
Most scalable.

---

## Option C — Progressive Escalation

All builds begin in Core Mode.

Upgrade to Enterprise Mode when:

- Revenue exceeds defined threshold  
- User count exceeds defined threshold  
- Regulated data introduced  
- Funding event occurs  
- Multi-tenant expansion begins  

This mirrors real-world SaaS evolution.

---

# 10. Governance Integrity Rule

A repository must not silently escalate or de-escalate modes.

Mode change requires:

1. Formal declaration update  
2. ADR documenting rationale  
3. Artefact gap analysis  
4. Enforcement recalibration  

Silent governance downgrade is prohibited.

---

# 11. Summary

Dual-Mode Architecture ensures:

- One lifecycle  
- Multiple enforcement depths  
- Scalable governance  
- Reduced cognitive fragmentation  

The system remains structurally stable.

Governance density adapts to risk.

---

**Status:** Active  
**Version:** v1.1


⸻
