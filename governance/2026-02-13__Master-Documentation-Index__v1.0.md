# 2026-02-13__Master-Documentation-Index__v1.0.md

# Master Documentation Index
AI-Native SaaS Build OS

This index is the canonical entry point for all doctrine, lifecycle control, templates, contracts, and enforcement artefacts in this repository.

It exists to provide:
- a single navigation surface for humans,
- a stable reference map for product teams,
- an auditable inventory for governance and assurance reviews.

---

## 1. Repository Scope and Authority

This repository is **doctrine**.

- **Doctrine is authoritative**. Product repositories inherit doctrine, they do not modify it.
- **Templates are immutable** in product repositories. Changes occur only here via PR.
- **Contracts bind products** to declared architecture and control requirements.
- **Enforcement gates** validate contracts and block non-compliant changes in CI.

Primary integration guidance:
- `PRODUCT_INTEGRATION_GUIDE.md`
- `2026-02-13__Build-OS-Governance-Charter__v1.0.md`

---

## 2. Canonical Doctrine

### 2.1 Build OS (Current Canonical Version)
- `/doctrine/artefacts/2026-02-08__AI-Native-SaaS-Build-OS__v2.3.md`

### 2.2 Doctrine Extensions
- `/doctrine/artefacts/2026-02-08__Enterprise-Hardening-Layer__v1.0.md`
- `/doctrine/artefacts/2026-02-08__Dual-Mode-Architecture__v1.1.md`

### 2.3 Mobile and Client-Side Doctrine
- `/doctrine/artefacts/2026-02-13__Mobile-Support-Policy__v1.0.md`

### 2.4 MCP Doctrine
- `/doctrine/artefacts/2026-02-13__MCP-Architecture__v1.0.md`
- `/doctrine/artefacts/2026-02-13__MCP-Evolution-Roadmap__v1.0.md`
- `/doctrine/artefacts/2026-02-13__MCP-Maturity-Self-Assessment-Checklist__v1.0.md`

### 2.5 Lifecycle Enforcement Doctrine
- `/doctrine/enforcement/2026-02-08__Lifecycle-Enforcer__System-Prompt__v1.0.md`
- `/enforcement/checklists/2026-02-08__Lifecycle-Enforcer__Checklist-View__v1.0.md`

---

## 3. Lifecycle Control and Execution

These artefacts define the lifecycle stages, required outputs, escalation logic, and validation protocol.

- `/lifecycle/2026-02-08__Lifecycle-Execution-Table__v2.0.md`
- `/lifecycle/2026-02-08__Artefact-Production-Matrix__v2.0.md`
- `/lifecycle/2026-02-08__Escalation-Matrix__v1.0.md`
- `/lifecycle/2026-02-13__Lifecycle-Validation-Protocol__v1.0.md`

---

## 4. Architecture (Reference Specifications)

Reference specifications describe the OS-level architecture position and default assumptions.

- `/architecture/2026-02-08__Technical-Architecture-Specification__v1.1.md`

---

## 5. Contracts

Contracts are machine-readable declarations used for governance, validation, and auditability.

### 5.1 Contract Templates (Copy into Product Repos)
- `/templates/architecture/2026-02-14__Technical-Architecture-Contract-Template__v1.2.yaml`

### 5.2 Reference Contracts (OS-Owned Examples / Canonical Reference)
- `/contracts/architecture/README.md` (folder placeholder until reference contracts are published)

---

## 6. Templates

Templates are canonical, versioned artefact forms intended to be copied into product repositories and instantiated.

### 6.1 Architecture Templates
- `/templates/architecture/2026-02-14__Technical-Architecture-Contract-Template__v1.2.yaml`
- `/templates/architecture/2026-02-08__Technical-Architecture-Specification-Template__v1.0.md`

### 6.2 Compliance Templates
- `/templates/compliance/2026-02-13__Client-Application-Security-Addendum__CASA__v1.0.md`
- `/templates/compliance/2026-02-13__Mobile-Release-and-Compatibility-Policy__MRCP__v1.0.md`

### 6.3 Governance Templates
- `/templates/governance/README.md` (placeholder)

---

## 7. Compliance and Control Artefacts

These artefacts define the minimum enterprise control surface for security, privacy, change management, and operational resilience.

### 7.1 Tenant and Isolation Controls
- `/compliance/2026-02-08__Tenant-Isolation-Claim__v1.0.md`
- `/compliance/2026-02-08__Tenant-Policy-Matrix__v1.0.md`
- `/compliance/2026-02-08__Tenant-Audit-Export-Spec__v1.0.md`
- `/compliance/2026-02-08__Shared-Service-Boundary-Register__v1.0.md`
- `/compliance/2026-02-08__Tenant-Data-Classification-Policy__v1.0.md`

### 7.2 Security Governance
- `/compliance/2026-02-08__Threat-Model__v1.0.md`
- `/compliance/2026-02-08__Access-Control-Matrix__v1.0.md`
- `/compliance/2026-02-08__Vulnerability-Management-Policy__v1.0.md`
- `/compliance/2026-02-08__Cryptographic-Key-Management-Policy__v1.0.md`
- `/compliance/2026-02-08__Secure-SDLC-Policy__v1.0.md`
- `/compliance/2026-02-08__Secure-AI-Usage-Policy__v1.0.md`
- `/compliance/2026-02-08__Vendor-Risk-Management-Policy__v1.0.md`

### 7.3 Change and Incident Controls
- `/compliance/2026-02-08__Change-Management-Protocol__v1.0.md`
- `/compliance/2026-02-08__Incident-Response-Playbook__v1.0.md`

### 7.4 Data Governance and Privacy
- `/compliance/2026-02-08__Data-Processing-Register__v1.0.md`
- `/compliance/2026-02-08__Data-Flow-and-Sub-Processor-Register__v1.0.md`
- `/compliance/2026-02-08__Data-Retention-and-Deletion-Policy__v1.0.md`

### 7.5 Resilience and Continuity
- `/compliance/2026-02-08__Business-Continuity-Plan__v1.0.md`
- `/compliance/2026-02-08__Disaster-Recovery-Runbook__v1.0.md`

### 7.6 Control Mapping
- `/compliance/2026-02-08__Formal-Control-Mapping-Matrix__v1.0.md`
- `/compliance/2026-02-08__Governance-and-Control-Register__v1.0.md`

---

## 8. Enforcement (Validation and CI Gatekeeping)

These artefacts implement automated compliance checks and CI enforcement for contracts.

### 8.1 Validator Rules and Specs
- `/enforcement/validators/2026-02-14__Technical-Architecture-Contract__Validator-Rules__v1.0.yaml`
- `/enforcement/validators/2026-02-14__Technical-Architecture-Contract__Validator-Spec__v1.0.md`

### 8.2 Validator Runtime
- `/enforcement/runtime/2026-02-14__Contract-Validator-Runtime__v1.0.py`

### 8.3 CI Integration Pattern
- `/enforcement/ci/2026-02-14__Contract-Validation__CI-Pattern__v1.0.md`

### 8.4 GitHub Actions Workflow
- `/.github/workflows/contract-validation.yml`

---

## 9. Changelog

- `/changelog/changelog.md`

---

## 10. Governance Documents (Root)

- `2026-02-13__Build-OS-Governance-Charter__v1.0.md`
- `PRODUCT_INTEGRATION_GUIDE.md`
- `README.md`

---

## 11. Conventions

### 11.1 Naming Convention
All artefacts follow:
`YYYY-MM-DD__<Artefact-Name>__vX.Y.ext`

### 11.2 Versioning Policy
- **Major**: structural lifecycle change.
- **Minor**: new artefact or new section.
- **Patch**: wording clarification or non-structural edits.

### 11.3 Change Control
OS artefacts are updated only via PR with:
- version increment,
- changelog entry,
- backward compatibility note where applicable.

---

## 12. TODO Placeholders (Intentionally Empty)

These folders exist for future OS expansion and must remain empty until populated by canonical artefacts:

- `/templates/governance/README.md`
- `/contracts/architecture/README.md`
- `/compliance/README.md` (if present as placeholder content only)

---

End of index.
