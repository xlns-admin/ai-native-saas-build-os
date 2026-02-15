# Vendor-Risk-Management-Policy__v1.0.md
AI-Native SaaS Build OS

---

**Document:** Vendor-Risk-Management-Policy__v1.0.md  
**Owner:** Security Lead  
**Oversight:** Architecture Lead  
**Status:** Active  
**Version:** v1.0  
**Review Cycle:** Annual  
**Escalation Level:** Enterprise Governance Control  
**Applies To:** All third-party vendors supporting platform operations  

---

# Vendor Risk Management Policy

---

## 1. Purpose

This policy defines the process for identifying, assessing, approving, monitoring, and reviewing third-party vendors and service providers that support the SaaS platform.

Its objectives are to:

- Protect customer data  
- Prevent supply chain compromise  
- Ensure continuity of service  
- Maintain regulatory compliance  
- Reduce dependency risk concentration  

This policy applies to all third-party vendors that:

- Process or store data  
- Provide infrastructure  
- Deliver security services  
- Provide AI capabilities  
- Deliver operational tooling  
- Access internal systems  

---

## 2. Scope

Vendors include, but are not limited to:

- Cloud infrastructure providers  
- AI model providers  
- Payment processors  
- Email and SMS gateways  
- Monitoring and logging services  
- CI/CD tooling  
- Support tooling  
- Identity providers  
- Data enrichment services  
- Sub-processors  

Open-source libraries are governed separately under dependency management controls but may trigger vendor review if tied to external services.

---

## 3. Vendor Classification

Each vendor must be classified prior to approval.

### 3.1 Tier Classification

| Tier | Risk Level | Description | Example |
|------|------------|------------|---------|
| Tier 1 | Critical | Directly processes production or tenant data | Cloud provider, database provider |
| Tier 2 | High | Indirect access to sensitive systems | CI/CD, logging provider |
| Tier 3 | Moderate | Limited system impact | Monitoring dashboards |
| Tier 4 | Low | No access to sensitive systems | Documentation tools |

Tier classification determines assessment depth and review frequency.

---

## 4. Pre-Approval Assessment

Before onboarding a vendor, the following must be completed.

---

### 4.1 Security Review

- SOC 2 Type II or ISO 27001 certification (where applicable)  
- Security whitepaper review  
- Encryption practices reviewed  
- Access control mechanisms reviewed  
- Incident response capability assessed  
- Data residency assessed  

If certifications are unavailable, compensating controls must be documented.

---

### 4.2 Privacy & Data Protection Review

- Data Processing Agreement executed  
- Sub-processor list obtained  
- Data transfer mechanisms verified (SCCs, UK IDTA, etc.)  
- Data retention policies reviewed  
- Deletion procedures confirmed  

---

### 4.3 Operational Resilience Review

- Uptime SLA reviewed  
- Redundancy model assessed  
- Business continuity plan reviewed  
- Disaster recovery RTO and RPO documented  
- Historical outage record assessed  

---

### 4.4 Financial & Viability Review (Critical Vendors Only)

- Business stability review  
- Funding status (if startup)  
- Acquisition risk exposure  
- Dependency concentration risk  

---

## 5. Risk Acceptance & Approval

Each vendor must have:

- Documented risk rating  
- Approved risk acceptance statement  
- Named approving authority  

Critical vendors require:

- Security Lead approval  
- Architecture Lead approval  
- Executive acknowledgement  

No vendor may be used without documented approval.

---

## 6. Contractual Requirements

Contracts must include:

- Data protection clauses  
- Security breach notification timelines  
- Audit rights (where possible)  
- Sub-processor transparency  
- Termination rights  
- Data deletion guarantees upon termination  

For AI vendors, contracts must clarify:

- Data usage rights  
- Model training data restrictions  
- Prompt retention policies  
- Logging behaviour  

---

## 7. Continuous Monitoring

Vendors must be monitored for:

- Security breaches  
- Certification expiry  
- SLA violations  
- Ownership changes  
- Public security disclosures  

Review frequency:

- Tier 1: Annual  
- Tier 2: Annual  
- Tier 3: Every two years  
- Tier 4: At discretion  

---

## 8. Sub-Processor Transparency

All vendors that process customer data must be listed in:

- Data Flow & Sub-Processor Register  
- Customer-facing sub-processor disclosure page (where required)  

Changes must trigger:

- Risk reassessment  
- Customer notification if required  

---

## 9. Concentration Risk Management

Where possible:

- Avoid single points of vendor dependency  
- Evaluate exit strategy before onboarding  
- Document migration feasibility  
- Maintain export capabilities for critical data  

Critical question before approval:

“If this vendor disappears tomorrow, what breaks?”

If the answer is “everything,” mitigation must be documented.

---

## 10. AI Vendor Controls

AI vendors must additionally be evaluated for:

- Data retention policies  
- Training data usage  
- Cross-tenant data isolation  
- Prompt injection risk exposure  
- Model drift risk  
- Regional hosting controls  

Use of unapproved AI tools is prohibited.

---

## 11. Incident Response Involving Vendors

If a vendor experiences a breach:

1. Activate Incident Response Playbook  
2. Assess blast radius  
3. Notify customers if required  
4. Review vendor risk rating  
5. Consider suspension or termination  

---

## 12. Vendor Termination Process

Upon termination:

- Confirm data deletion  
- Revoke API keys  
- Remove integrations  
- Archive risk assessment documentation  
- Update Sub-Processor Register  

Termination must not leave orphaned access.

---

## 13. Ownership

Primary Owner: Security Lead  
Oversight: Architecture Lead  
Review Cycle: Annual  

---

## 14. Version Control

Version: v1.0  
Status: Active  
Review Frequency: Annual or upon material vendor change  

---

# Governing Principle

A vendor is an extension of your attack surface.

Approval without assessment is negligence.  
Dependency without exit strategy is fragility.  
Convenience without governance is debt.

Risk does not disappear because it is outsourced.

It is merely transferred — and must be managed.

---
