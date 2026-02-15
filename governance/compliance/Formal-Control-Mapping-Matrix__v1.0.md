# Formal-Control-Mapping-Matrix__v1.0.md
AI-Native SaaS Build OS

---

**Document:** Formal-Control-Mapping-Matrix__v1.0.md  
**Owner:** Security Lead  
**Oversight:** Human Orchestrator  
**Status:** Active  
**Version:** v1.0  
**Review Cycle:** Quarterly  
**Classification:** Governance – Controlled  

---

# Formal Control Mapping Matrix (FCMM)

---

## 1. Purpose

This document maps internal SaaS Build OS controls and artefacts to:

- SOC 2 Trust Services Criteria (TSC)
- ISO 27001:2022 Annex A controls

Its purpose is to:

- Demonstrate control coverage
- Identify gaps
- Prevent control drift
- Support audit readiness
- Provide structured traceability across the security lifecycle

This document does not restate controls.  
It maps implemented artefacts to recognised control frameworks.

---

## 2. Scope

This matrix applies to:

- AI-native SaaS platforms
- Multi-tenant architectures
- Cloud-first deployments
- Regulated customer environments

It covers:

- Security
- Availability
- Confidentiality
- Processing Integrity
- Privacy (where applicable)

---

## 3. Control Mapping Methodology

Each row in this matrix must include:

- External framework control reference
- Control description (summarised)
- Internal artefact enforcing the control
- Owner
- Control type (Preventative / Detective / Corrective)
- Evidence source
- Review cadence
- Status (Implemented / Partial / Gap)

No control may be marked “Implemented” without documented evidence.

---

# 4. SOC 2 → Internal Control Mapping

---

## Trust Services Category: Security (Common Criteria)

| SOC 2 Ref | Control Theme | Internal Artefact(s) | Control Type | Evidence Source | Owner | Status |
|------------|--------------|----------------------|--------------|-----------------|-------|--------|
| CC1.1 | Control Environment | Lifecycle Enforcer, Escalation Matrix | Preventative | Governance repo | Human Orchestrator | Implemented |
| CC2.1 | Risk Assessment | Threat Model, Tenant Policy Matrix | Preventative | Threat Model doc | Security Lead | Implemented |
| CC3.2 | Logical Access Controls | Access-Control-Matrix | Preventative | IAM logs | Security Lead | Implemented |
| CC4.1 | Change Management | Change-Management-Protocol | Preventative | Change register | Engineering Lead | Implemented |
| CC5.1 | Monitoring Activities | Secure SDLC + Control Review Cadence | Detective | Audit logs | Security Lead | Implemented |
| CC6.1 | Data Transmission Protection | Cryptographic-Key-Management-Policy | Preventative | TLS config evidence | Security Lead | Implemented |
| CC7.2 | Vulnerability Management | Vulnerability-Management-Policy | Detective | Scan reports | Security Lead | Implemented |
| CC8.1 | Incident Response | Incident-Response-Playbook | Corrective | Incident log | Security Lead | Implemented |

---

## Trust Services Category: Availability

| SOC 2 Ref | Control Theme | Internal Artefact(s) | Evidence Source | Status |
|------------|--------------|----------------------|----------------|--------|
| A1.1 | Capacity Planning | Architecture ADRs | ADR repository | Implemented |
| A1.2 | Backup & Recovery | Disaster-Recovery-Runbook | DR test evidence | Implemented |
| A1.3 | Business Continuity | Business-Continuity-Plan | BCP review log | Implemented |
| A1.4 | Monitoring & Alerts | Operational Monitoring Framework | Monitoring dashboard | Implemented |

---

## Trust Services Category: Confidentiality

| SOC 2 Ref | Control Theme | Internal Artefact(s) | Evidence Source | Status |
|------------|--------------|----------------------|----------------|--------|
| C1.1 | Data Classification | Tenant-Data-Classification-Policy | Classification register | Implemented |
| C1.2 | Encryption at Rest | Cryptographic-Key-Management-Policy | Encryption config | Implemented |
| C1.3 | Data Retention & Deletion | Data-Retention-and-Deletion-Policy | Deletion logs | Implemented |

---

# 5. ISO 27001:2022 Annex A Mapping

---

## A.5 Organisational Controls

| ISO Control | Theme | Internal Artefact | Owner | Status |
|-------------|-------|------------------|-------|--------|
| A.5.1 | Policies for Information Security | Secure-SDLC-Policy | Security Lead | Implemented |
| A.5.7 | Threat Intelligence | Threat-Model | Security Lead | Implemented |
| A.5.19 | Supplier Relationships | Vendor-Risk-Management-Policy + Data-Flow-and-Sub-Processor-Register | Security Lead | Implemented |

---

## A.6 People Controls

| ISO Control | Theme | Internal Artefact | Owner | Status |
|-------------|-------|------------------|-------|--------|
| A.6.1 | Screening | Access-Control-Matrix (Role Assignment Governance) | Security Lead | Implemented |
| A.6.3 | Security Awareness | Security Awareness Procedure | Security Lead | Partial |

---

## A.8 Technological Controls

| ISO Control | Theme | Internal Artefact | Owner | Status |
|-------------|-------|------------------|-------|--------|
| A.8.2 | Privileged Access Management | Access-Control-Matrix | Security Lead | Implemented |
| A.8.9 | Configuration Management | Change-Management-Protocol | Engineering Lead | Implemented |
| A.8.12 | Data Leakage Prevention | Tenant-Isolation-Claim | Security Lead | Implemented |
| A.8.15 | Logging | Incident-Response-Playbook + Monitoring Stack | Security Lead | Implemented |
| A.8.23 | Web Filtering | Infrastructure Configuration | Infrastructure Lead | Implemented |

---

# 6. Gap Identification Section

All identified gaps must be recorded below.

| Framework | Control | Gap Description | Remediation Plan | Target Date | Owner |
|------------|---------|----------------|------------------|-------------|-------|
| ISO 27001 | A.6.3 | Security Awareness training not formalised | Develop awareness programme | YYYY-MM-DD | Security Lead |

No gap may be ignored or hidden.

---

# 7. Evidence Catalogue Reference

Each mapped control must link to:

- Document location
- Log source
- Review artefact
- Version history

Example:

Control CC4.1  
Evidence:
- Change-Management-Protocol__v1.0.md  
- Git change history  
- Pull request review logs  
- Quarterly governance review minutes  

Evidence must be retrievable on demand.

---

# 8. Continuous Compliance Monitoring

Control mapping must be reviewed:

- Quarterly
- After major architectural change
- After security incident
- Before external audit

Automated compliance drift detection must:

- Flag missing artefacts
- Detect stale policy versions
- Identify undocumented structural changes
- Detect new integrations without vendor review

---

# 9. Ownership

Primary Owner: Security Lead  
Oversight: Human Orchestrator  
Audit Interface: Compliance / External Auditor  

Control responsibility must be explicitly assigned.

---

# 10. Version Control

Version: v1.0  
Review Cycle: Quarterly  
Next Review: ____________________

---
