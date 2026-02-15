# AI-Native-SaaS-Build-OS__v2.3

AI-Native SaaS Build OS  
Multi-Tenant Compliance Architecture Edition

---

**Document:** AI-Native-SaaS-Build-OS__v2.3  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v2.3  
**Review Cycle:** Annual  
**Classification:** Canonical Doctrine  
**Supersedes:** v2.2  
**Applies to:** All multi-tenant SaaS products governed by the Build OS  

---

## 0. Purpose of v2.3

v2.3 defines the architectural requirements and governance artefacts required to operate a multi-tenant SaaS platform with:

- Tenant-isolated compliance evidence  
- Tenant-scoped audit exports  
- Tenant-scoped security controls  
- Explicit global shared service boundaries  
- Enforceable data residency and retention rules per tenant class  

This is not multi-tenant product design.

This is multi-tenant compliance survivability.

---

## 1. Canonical Terms

### Tenant

**Definition:**  
An isolated security and compliance boundary representing one customer organisation, with its own identities, data, entitlements, policies, and audit evidence.

---

### Shared Service

**Definition:**  
A platform capability used by multiple tenants, whose operational controls must be treated as global evidence with explicit tenant attribution where possible.

---

### Tenant Control Plane

**Definition:**  
The set of services and artefacts that govern tenant configuration, entitlements, policies, and enforcement.

---

### Tenant Data Plane

**Definition:**  
The set of services and data stores that hold tenant business data and produce tenant-specific operational events.

---

## 2. Multi-Tenant Compliance Principles

### 2.1 Principle: Attribution First

Every compliance-relevant event must be attributable to:

- A `tenant_id`, or  
- A `global_scope` marker, with justification  

---

### 2.2 Principle: Tenant Isolation is Enforced, Not Assumed

Isolation claims must be enforced at:

- Data layer (RLS or equivalent)  
- Service layer (scoped credentials)  
- Observability layer (log partitioning)  
- Operational tooling layer (tenant-aware administration)  

---

### 2.3 Principle: Evidence Must Be Tenant-Exportable

For any tenant, the system must generate an audit export containing only:

- Their data  
- Their logs and events  
- Their access history  
- Controls applicable to them  
- Relevant shared-service evidence with traceable applicability  

---

### 2.4 Principle: Policies Can Diverge Per Tenant Class

Enterprise tenants may require:

- Retention windows  
- Residency constraints  
- Encryption requirements  
- Incident notification SLAs  
- Custom DPA terms  

The system must model and enforce policy variance without branching the codebase.

---

## 3. Tenancy Models and Compliance Trade-Offs

### 3.1 Tenancy Isolation Options

| Model | Data Isolation | Compliance Strength | Complexity | Typical Use |
|-------|---------------|--------------------|------------|-------------|
| Shared DB, shared schema, RLS | Logical | Medium–High (if correct) | Medium | Default SaaS |
| Shared DB, tenant schemas | Stronger logical | High | High | Regulated SaaS |
| Tenant DB per tenant | Strong physical | Very High | Very High | High-risk enterprise |
| Dedicated stack per tenant | Maximum isolation | Maximum | Extreme | Top-tier regulated |

Whichever model is chosen:

- The compliance narrative must match the isolation model  
- The evidence model must support export and attribution  

---

## 4. Required Multi-Tenant Compliance Artefacts

v2.3 introduces mandatory artefacts.

---

### 4.1 Tenant Isolation Claim (TIC)

Must include:

- Chosen tenancy model  
- Enforceable guarantees (not marketing claims)  
- Known limitations  
- Test evidence plan  

---

### 4.2 Tenant Policy Matrix (TPM)

Must define per tenant class:

- Retention policy  
- Residency policy  
- Encryption policy  
- Access policy  
- Audit export policy  
- Incident notification policy  

---

### 4.3 Tenant Audit Export Specification (TAES)

Must define:

- Required export formats  
- Contents list  
- Evidence sources  
- Redaction rules  
- Shared-service evidence inclusion rules  

---

### 4.4 Shared Service Boundary Register (SSBR)

Must list:

- Each shared capability (auth, messaging, billing, observability)  
- Data handled  
- Tenant attribution capability  
- Risk classification  
- Compensating controls  

---

### 4.5 Multi-Tenant Threat Model Addendum

Must cover:

- Cross-tenant data exposure risks  
- Authentication boundary failure modes  
- Admin privilege escalation risks  
- Logging leakage risks  
- Shared-service compromise blast radius  

---

## 5. Compliance Architecture Requirements

### 5.1 Identity and Access

Requirements:

- `tenant_id` is mandatory on every identity and session  
- Role assignment is tenant-scoped by default  
- Global roles are explicit, rare, and auditable  
- Admin actions require reason logging  

Control:

- Access Control Matrix must model tenant scopes explicitly  

---

### 5.2 Data Isolation

Requirements:

- Every row carries `tenant_id`  
- RLS or equivalent is enforced on every query path  
- Server-to-server operations assert tenant context  
- Background jobs must not default `tenant_id`  

Control:

- “No Tenant Context, No Write” rule  

---

### 5.3 Observability Isolation

Requirements:

- Logs include `tenant_id` for tenant operations  
- Logs do not contain tenant PII unless explicitly permitted  
- Monitoring dashboards are tenant-filterable  
- Alerting identifies tenant impact  

Control:

- Log Partition Policy with enforced tenant tagging  

---

### 5.4 Evidence Collection

Requirements:

- Compliance evidence produced as events  
- Evidence events carry `tenant_id` or `global_scope`  
- Evidence queryable per tenant and time window  

Control:

- Evidence Freshness and Drift rules apply per tenant class  

---

### 5.5 Data Retention and Deletion

Requirements:

- Tenant policy drives retention windows  
- Deletion is tenant-scoped and provable  
- Shared-service logs support tenant-level redaction where required  

Control:

- Deletion Certificates issued per tenant  

---

## 6. Multi-Tenant Compliance Drift Detection

Drift detection is tenant-aware.

Every drift flag must be attributable to:

- A `tenant_id`, or  
- A `global_scope` marker with affected tenant set  

Examples:

- Tenant-specific RLS misconfiguration  
- Enterprise retention policy violation  
- Global authentication provider change without evidence refresh  

---

## 7. Release Gates for Multi-Tenant Builds

Stage 9 Release blocks if:

- Tenant Isolation Claim is missing or stale  
- Tenant Policy Matrix is incomplete  
- Tenant Audit Export cannot be generated for at least one tenant class  
- Multi-tenant Threat Model Addendum is missing  
- Cross-tenant leakage tests are failing  

---

## 8. Test Requirements for Tenant Isolation

Minimum required tests:

- Cross-tenant read attempt must fail  
- Cross-tenant write attempt must fail  
- Admin impersonation must be logged  
- Tenant audit export must exclude other tenant data  
- Log streams must not leak tenant identifiers without authorisation  

A happy-path-only test suite is invalid at Level 3.

---

## 9. Multi-Tenant Compliance Maturity Levels

Level 1 — Tenant awareness and basic isolation  
Level 2 — Tenant audit export and tenant policy variance  
Level 3 — Tenant-scoped drift detection and automated evidence  

---

## 10. What v2.3 Adds

v2.3 introduces:

- A formal tenancy compliance model  
- Explicit shared-service boundaries  
- Tenant-exportable audit evidence  
- Policy variance without code branching  
- Multi-tenant drift detection  

This is the difference between:

“We have RLS.”

And:

“We can survive an enterprise audit.”

---

## Version History

- v2.3 — Multi-tenant compliance architecture added. New mandatory artefacts defined.

---

**Status:** Active  
**Version:** v2.3
