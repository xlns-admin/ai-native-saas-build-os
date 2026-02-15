# Access-Control-Matrix__v1.0.md
AI-Native SaaS Build OS

---

**Document:** Access-Control-Matrix__v1.0.md  
**Owner:** Human Orchestrator  
**Status:** Canonical Template  
**Version:** v1.0  
**Escalation Requirement:** Mandatory for Enterprise Hardening Level 2 and above  
**Related Artefacts:**  
- Threat-Model__vX.Y.md  
- Tenant-Isolation-Claim__vX.Y.md  
- Tenant-Data-Classification-Policy__vX.Y.md  
- Technical-Architecture-Contract__vX.Y.yaml  

---

# Access Control Matrix

---

## 1. Document Purpose

This document defines the authoritative access control model for the system.

It specifies:

- Roles  
- Permissions  
- Resources  
- Scope boundaries  
- Approval authority  
- Enforcement model  

Access control must be enforceable in architecture, not convention.

---

## 2. Access Control Model Declaration

### 2.1 Model Type

Select and declare the primary model:

- ☐ RBAC (Role-Based Access Control)  
- ☐ ABAC (Attribute-Based Access Control)  
- ☐ Hybrid RBAC + ABAC  
- ☐ Policy-as-Code  

Declared Model:  

---

### 2.2 Enforcement Layer

Access control must be enforced at:

- ☐ API layer  
- ☐ Application layer  
- ☐ Database layer  
- ☐ Infrastructure layer  

Enforcement must not rely solely on UI restrictions.

---

## 3. Trust Boundaries

Define logical boundaries:

- Tenant boundary  
- Admin boundary  
- Internal service boundary  
- CI/CD boundary  
- AI execution boundary  

Each boundary must include:

- Defined entry points  
- Defined authentication mechanism  
- Defined authorisation model  

Implicit trust boundaries are prohibited.

---

## 4. Role Catalogue

All roles must be explicitly defined.

No implied privileges.

### 4.1 System Roles

| Role ID | Role Name | Scope | Description | Assignable By |
|----------|------------|--------|-------------|----------------|

Examples:

- super_admin  
- tenant_admin  
- tenant_user  
- read_only_user  
- support_operator  
- system_service_account  
- ai_execution_agent  

Each role must define:

- Privilege scope (global / tenant / resource-specific)  
- Escalation path  
- Audit requirements  

If a role is not documented here, it does not exist.

---

## 5. Resource Catalogue

All protected resources must be listed.

| Resource ID | Resource Type | Sensitivity Level | Tenant Scoped | Notes |
|-------------|--------------|-------------------|--------------|-------|

Examples:

- user_profile  
- payment_record  
- audit_log  
- api_key  
- configuration_setting  
- orchestration_manifest  
- shared_state  
- tenant_schema  

Resource classification must align with the Tenant Data Classification Policy.

---

## 6. Permission Matrix

This is the core control table.

| Role | Create | Read | Update | Delete | Execute | Approve | Cross-Tenant Access |
|------|--------|------|--------|--------|---------|----------|---------------------|

Permissions must be:

- Explicit  
- Deny-by-default  
- Least-privilege  

If a permission is not declared, it is denied.

---

## 7. Privileged Operations Register

High-risk operations must be isolated.

Examples:

- Role modification  
- Tenant deletion  
- Data export  
- Key rotation  
- Infrastructure changes  
- Production deployment  

For each privileged operation:

| Operation | Required Role | Multi-Factor Required | Approval Required | Audit Logged |
|------------|---------------|----------------------|------------------|--------------|

Privileged operations must:

- Require elevated authentication  
- Generate immutable audit records  
- Be reviewable  

---

## 8. AI Agent Permissions

AI agents must be treated as constrained execution identities.

For each agent:

| Agent ID | Read Scope | Write Scope | Execute Scope | Decision Authority |
|-----------|------------|------------|---------------|--------------------|

Rules:

- AI agents cannot modify access control policy.  
- AI agents cannot elevate privileges.  
- AI agents cannot access cross-tenant data unless explicitly permitted.  
- AI agents must operate under least privilege.  
- AI actions must be traceable to a human authority boundary.  

---

## 9. Tenant Isolation Rules

Define explicitly:

- Whether roles are tenant-scoped or global  
- Whether support staff can impersonate tenants  
- Whether impersonation requires dual approval  

Cross-tenant access must:

- Be logged  
- Require justification  
- Be time-bound  
- Be reviewable  

Isolation enforcement must reference the Tenant Isolation Claim.

---

## 10. Approval & Escalation Model

For actions requiring approval:

- Who approves?  
- Is dual control required?  
- Is time-based expiry enforced?  

Example:

- Production deployment → requires Engineering Lead approval  
- Tenant data export → requires Compliance approval  
- Role elevation → requires dual approval  

Approval records must be retained according to retention policy.

---

## 11. Logging & Audit Requirements

All access control decisions must log:

- Actor ID  
- Role  
- Resource accessed  
- Action attempted  
- Outcome (allowed / denied)  
- Timestamp  
- Tenant ID  
- Correlation ID  

Audit logs must be:

- Immutable  
- Retained according to Data Retention Policy  
- Accessible for compliance review  
- Protected against tampering  

---

## 12. Review Cadence

Access control matrix must be reviewed:

- Quarterly  
- After major feature release  
- After security incident  
- After role structure changes  
- Before Enterprise onboarding  

Review must be documented.

---

## 13. Change Management

Any change to access control must:

- Trigger an ADR  
- Trigger Threat Model review  
- Be documented in change log  
- Be peer-reviewed  
- Be validated by Lifecycle Enforcer  

Unreviewed access changes are prohibited.

---

## 14. Residual Risk Statement

Document known limitations:

- Legacy compatibility exceptions  
- Temporary elevated roles  
- Migration allowances  
- Technical debt areas  

All exceptions must include:

- Justification  
- Compensating control  
- Expiry date  

---

## Approval

Security Lead:  
Engineering Lead:  
Product Owner:  

Date Approved:  

---

## Version History

| Version | Date | Change | Author |
|----------|------------|--------|--------|
| 1.0 | 2026-02-08 | Initial enterprise-grade access control matrix template | System |

---
