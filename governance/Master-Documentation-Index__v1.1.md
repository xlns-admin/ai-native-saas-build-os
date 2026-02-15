# Master-Documentation-Index__v1.1

AI-Native SaaS Build OS  
Authoritative Documentation Entry Point  

---

**Document:** Master-Documentation-Index__v1.1  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.1  
**Review Cycle:** Quarterly  
**Classification:** Governance  
**Supersedes:** Master-Documentation-Index__v1.0  
**Applies to:** ai-native-saas-build-os repository  

---

## 1. Purpose

This document is the single authoritative index of all canonical artefacts within the AI-Native SaaS Build OS repository.

It defines:

- Canonical location
- Structural domain
- Artefact authority
- Governance tier alignment
- Traceable entry point for audit and enforcement

No artefact outside this index is considered authoritative.

If an artefact exists but is not listed here, it is governance drift.

---

# 2. Repository Domain Structure

The repository is organised into deterministic top-level domains:

.github/  
architecture/  
changelog/  
contracts/  
doctrine/  
enforcement/  
examples/  
governance/  
lifecycle/  
operations/  
policies/  
prompts/  
runtime/  
security/  
stages/  
templates/  
tenancy/  
validators/  

---

# 3. Canonical Artefact Index

---

## 3.1 Governance

**Location:** `/governance/`

- Governance-and-Control-Register__v1.0.md
- ADR_Template__v1.0.md
- pull-request-template.md
- README.md

**Root Governance Artefacts:**

- Build-OS-Governance-Charter__v1.2.md
- Glossary__v1.1.md
- PRODUCT_INTEGRATION_GUIDE.md

---

## 3.2 Lifecycle

**Location:** `/lifecycle/`

- Artifact-Production-Matrix__v2.0.md
- Escalation-Matrix__v1.0.md
- Lifecycle-Execution-Table__v2.0.md
- Lifecycle-Validation-Protocol__v1.0.md
- Epic_Template__v1.0.md
- Story_Template__v1.0.md

---

## 3.3 Security

**Location:** `/security/`

- Access-Control-Matrix__v1.0.md
- Client-Application-Security-Addendum__CASA__v1.0.md
- Cryptographic-Key-Management-Policy__v1.0.md
- Mobile-Release-and-Compatibility-Policy__MRCP__v1.0.md
- Secure-AI-Usage-Policy__v1.0.md
- Secure-SDLC-Policy__v1.0.md
- Tenant-Isolation-Claim__v1.0.md
- Threat-Model__v1.0.md
- Vendor-Risk-Management-Policy__v1.0.md
- Vulnerability-Management-Policy__v1.0.md

---

## 3.4 Compliance

**Location:** `/compliance/`

- Data-Flow-and-Sub-Processor-Register__v1.0.md
- Data-Retention-and-Deletion-Policy__v1.0.md
- Formal-Control-Mapping-Matrix__v1.0.md
- Data-Processing-Register__v1.0.md
- README.md

---

## 3.5 Tenancy

**Location:** `/tenancy/`

- Shared-Service-Boundary-Register__v1.0.md
- Tenant-Policy-Matrix__v1.0.md
- 2026-02-13__Master-Documentation-Index__v1.0.md

---

## 3.6 Operations

**Location:** `/operations/runbooks/`

- Disaster-Recovery-Runbook__v1.0.md
- Business-Continuity-Plan__v1.0.md

**Location:** `/operations/`

- Incident-Response-Playbook__v1.0.md

---

## 3.7 Architecture

**Location:** `/architecture/technical/`

- Technical-Architecture-Specification__v1.1.md

**Location:** `/architecture/`

- README.md

---

## 3.8 Contracts

**Location:** `/contracts/architecture/`

- README.md

---

## 3.9 Validators

**Location:** `/validators/`

- 2026-02-14__Technical-Architecture-Contract__Validator-Spec__v1.0.yaml
- Technical-Architecture-Contract__Validator-Rules__v1.0.yaml

---

## 3.10 Runtime

**Location:** `/runtime/`

- Contract-Validator-Runtime__v1.0.py

---

## 3.11 Enforcement

**Location:** `/enforcement/checklists/`

- Lifecycle-Enforcer__Checklist-View__v1.0.md

**Location:** `/enforcement/ci/`

- Contract-Validation__CI-Pattern__v1.0.md

---

## 3.12 Doctrine

**Location:** `/doctrine/artefacts/`

- AI-Native-Build-Maturity-Model__v1.0.md
- AI-Native-SaaS-Build-OS__v2.3.md
- Dual-Mode-Architecture__v1.1.md
- Enterprise-Hardening-Layer__v1.0.md
- MCP-Architecture__v1.0.md
- MCP-Evolution-Roadmap__v1.0.md
- MCP-Maturity-Self-Assessment-Checklist__v1.0.md
- Mobile-Support-Policy__v1.0.md
- README.md

---

## 3.13 Policies

**Location:** `/policies/`

- CI-Quality-Gate-Policy__v1.0.md
- Prompt-Governance-Addendum__v1.0.md

---

## 3.14 Prompts

**Location:** `/prompts/`

- Lifecycle-Enforcer__System-Prompt__v1.0.md

---

## 3.15 Templates

**Location:** `/templates/architecture/`

- 2026-02-14__Technical-Architecture-Contract-Template__v1.2.yaml

**Location:** `/templates/compliance/`

- README.md

**Location:** `/templates/execution/`

- Diff-Prompt__Template__v1.0.md
- Refactor-Prompt__Template__v1.0.md
- Work-Item-Governance-Standard__v1.0.md

---

## 3.16 Examples

**Location:** `/examples/`

- README.md

---

## 3.17 Stages

**Location:** `/stages/`

- README.md

---

## 3.18 GitHub Automation

**Location:** `/.github/workflows/`

- contract-validation.yml

---

# 4. Structural Authority Rule

This index governs:

- Canonical artefact location
- Naming compliance
- Domain boundaries
- Audit traceability

Any structural change requires:

1. Update to this document  
2. Pull Request approval  
3. Version increment  
4. Changelog entry  

---

# 5. Drift Detection Rule

Governance drift occurs if:

- An artefact exists but is not listed here
- A file is renamed without version increment
- A new domain folder is introduced without Charter update
- Duplicate artefacts exist across domains

Drift must be corrected immediately.

---

# 6. Review & Maintenance

This index must be reviewed:

- Quarterly
- After structural change
- After major version release
- Before external audit

---

Effective Date: 2026-02-15  
Status: Active  
Version: v1.1
