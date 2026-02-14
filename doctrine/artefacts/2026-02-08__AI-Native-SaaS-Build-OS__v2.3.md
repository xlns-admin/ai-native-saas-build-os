2026-02-08__AI-Native-SaaS-Build-OS__v2.3.md

Multi-Tenant Compliance Architecture Edition

⸻

0. Purpose of v2.3

v2.3 defines the architectural requirements and governance artefacts needed to operate a multi-tenant SaaS with:
	•	tenant-isolated compliance evidence
	•	tenant-scoped audit exports
	•	tenant-scoped security controls
	•	explicit global shared services boundaries
	•	enforceable data residency and retention rules per tenant class

This is not “multi-tenant product design.”
This is multi-tenant compliance survivability.

⸻

1. Canonical Terms

Tenant is an isolated security and compliance boundary representing one customer organisation, with its own identities, data, entitlements, policies, and audit evidence.

Shared Service is a platform capability used by multiple tenants, whose operational controls must be treated as global evidence with explicit tenant attribution where possible.

Tenant Control Plane is the set of services and artefacts that govern tenant configuration, entitlements, policies, and enforcement.

Tenant Data Plane is the set of services and data stores that hold tenant business data and produce tenant-specific operational events.

⸻

2. Multi-Tenant Compliance Principles

2.1 Principle: Attribution First

Every compliance-relevant event must be attributable to:
	•	a tenant_id, or
	•	a global_scope marker, with justification.

2.2 Principle: Tenant Isolation is Enforced, Not Assumed

All isolation claims must be enforced at:
	•	data layer (RLS or equivalent)
	•	service layer (scoped credentials)
	•	observability layer (log partitioning)
	•	operational tooling layer (tenant-aware admin)

2.3 Principle: Evidence Must Be Tenant-Exportable

For any tenant, you must be able to generate an audit export containing only:
	•	their data
	•	their logs and events
	•	their access history
	•	the controls that apply to them
	•	relevant shared-service evidence with traceable applicability

2.4 Principle: Policies Can Diverge Per Tenant Class

Enterprise tenants may require:
	•	retention windows
	•	residency constraints
	•	encryption requirements
	•	incident notification SLAs
	•	custom DPA terms

The system must model and enforce policy variance without branching the codebase.

⸻

3. Tenancy Models and Compliance Trade-Offs

3.1 Tenancy Isolation Options

Model	Data Isolation	Compliance Strength	Complexity	Typical Use
Shared DB, shared schema, RLS	Logical	Medium–High if correct	Medium	Default SaaS
Shared DB, tenant schemas	Stronger logical	High	High	Regulated SaaS
Tenant DB per tenant	Strong physical	Very High	Very High	High-risk enterprise
Dedicated stack per tenant	Max isolation	Maximum	Extreme	Top-tier regulated

v2.3 requires that whichever model is chosen:
	•	the compliance story must match the isolation model
	•	the evidence model must support export and attribution

⸻

4. Required Multi-Tenant Compliance Artefacts

v2.3 introduces a new artefact set.

4.1 Tenant Isolation Claim (TIC)

File:
YYYY-MM-DD__SaaS-Build__Tenant-Isolation-Claim__vX.Y__source.md

Must include:
	•	chosen tenancy model
	•	enforceable guarantees (not marketing)
	•	known limitations
	•	test evidence plan

4.2 Tenant Policy Matrix (TPM)

File:
YYYY-MM-DD__SaaS-Build__Tenant-Policy-Matrix__vX.Y__source.md

Must include per tenant class:
	•	retention policy
	•	residency policy
	•	encryption policy
	•	access policy
	•	audit export policy
	•	incident notification policy

4.3 Tenant Audit Export Spec (TAES)

File:
YYYY-MM-DD__SaaS-Build__Tenant-Audit-Export-Spec__vX.Y__source.md

Must define:
	•	required export formats
	•	contents list
	•	evidence sources
	•	redaction rules
	•	shared-service evidence inclusion rules

4.4 Shared Service Boundary Register (SSBR)

File:
YYYY-MM-DD__SaaS-Build__Shared-Service-Boundary-Register__vX.Y__source.md

Must list:
	•	each shared capability (auth, messaging, billing, observability)
	•	data handled
	•	whether tenant attribution is possible
	•	risk classification
	•	compensating controls

4.5 Multi-Tenant Threat Model Addendum

File:
YYYY-MM-DD__SaaS-Build__Threat-Model__Multi-Tenant-Addendum__vX.Y__source.md

Must cover:
	•	cross-tenant data exposure risks
	•	auth boundary failure modes
	•	admin privilege risks
	•	logging leakage risks
	•	shared-service compromise blast radius

⸻

5. Compliance Architecture Requirements

5.1 Identity and Access

Requirements:
	•	tenant_id is mandatory on every identity and session
	•	role assignment is tenant-scoped by default
	•	global roles are explicit, rare, and auditable
	•	admin actions require reason logging

Control:
	•	Access Control Matrix must model tenant scopes explicitly.

5.2 Data Isolation

Requirements:
	•	every row carries tenant_id
	•	RLS or equivalent is enforced on every query path
	•	server-to-server operations must assert tenant context
	•	background jobs must not “default” tenant_id

Control:
	•	“No Tenant Context, No Write” rule.

5.3 Observability Isolation

Requirements:
	•	logs must include tenant_id for all tenant operations
	•	logs must not contain tenant PII unless explicitly permitted
	•	monitoring dashboards must be tenant-filterable
	•	alerting must identify tenant impact

Control:
	•	Log Partition Policy, with tenant tagging.

5.4 Evidence Collection

Requirements:
	•	compliance evidence must be produced as events
	•	evidence events must carry tenant_id or global_scope
	•	evidence must be queryable per tenant and time window

Control:
	•	Evidence Freshness and Drift rules apply per tenant class.

5.5 Data Retention and Deletion

Requirements:
	•	tenant policy drives retention windows
	•	deletion is tenant-scoped and provable
	•	shared-service logs must have tenant-level redaction ability where needed

Control:
	•	Deletion Certificates per tenant.

⸻

6. Multi-Tenant Compliance Drift Detection

v2.2 drift detection becomes tenant-aware.

New rule:
A drift flag must be attributable to:
	•	tenant_id, or
	•	global_scope with affected tenant set.

Examples:
	•	tenant-specific RLS misconfiguration
	•	enterprise tenant retention policy violated
	•	global auth provider change without evidence refresh

⸻

7. Release Gates for Multi-Tenant Builds

Stage 9 Release now BLOCKS if:
	•	Tenant Isolation Claim is missing or stale
	•	Tenant Policy Matrix is incomplete
	•	Tenant Audit Export cannot be generated for at least one tenant class
	•	Multi-tenant threat model addendum is missing
	•	Cross-tenant leakage tests are not passing

⸻

8. Test Requirements for Tenant Isolation

Minimum tests required:
	•	cross-tenant read attempt must fail
	•	cross-tenant write attempt must fail
	•	admin impersonation must be logged
	•	tenant audit export must exclude other tenant data
	•	log streams must not leak tenant identifiers without authorisation

A “happy path only” test suite is invalid at Level 3.

⸻

9. Multi-Tenant Compliance Maturity Levels (Updated)

Level 1: Tenant awareness, basic isolation
Level 2: Tenant audit export, tenant policy variance
Level 3: Tenant-scoped drift detection, tenant evidence automation

⸻

10. What v2.3 Adds

v2.3 gives you:
	•	a formal tenancy compliance model
	•	explicit shared-service boundaries
	•	tenant-exportable audit evidence
	•	policy variance without code branching
	•	multi-tenant drift detection

This is the difference between “we have RLS” and “we can survive an enterprise audit.”

⸻

Version History

v2.3 — Multi-tenant compliance architecture added, new mandatory artefacts defined.

⸻

If you want, the next move is to generate the four new artefact templates (TIC, TPM, TAES, SSBR) so they’re copy-paste ready and consistent with your naming and definition discipline.
