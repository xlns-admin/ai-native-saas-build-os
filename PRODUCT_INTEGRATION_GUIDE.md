# Product Integration Guide  
AI-Native SaaS Build OS

This document defines how product repositories must integrate with the Build OS.

It is procedural.  
It is binding.  
It is not advisory.

---

## 1. Purpose

The Build OS provides:

- Lifecycle doctrine
- Canonical templates
- Architecture contracts
- Validation rules
- Enterprise control artefacts

Product repositories consume and instantiate these artefacts.  
They do not modify them.

---

## 2. Mandatory OS Declaration

Every product repository must declare the Build OS version it is governed by.

This must exist at:

/governance/build-os.yaml

Example:

```yaml
build_os:
  version: "v2.3"
  repository: "xlns-admin/ai-native-saas-build-os"
  contract_type: "Technical-Architecture-Contract"
  contract_version: "v1.2"

Failure to declare OS version is a governance breach.
```
---

## 3. Contract Instantiation Flow

Step 1
Copy template from:

/templates/architecture/

Step 2
Rename using product naming convention:

YYYY-MM-DD__Technical-Architecture-Contract__vX.Y.yaml

Step 3
Place in product repository:

/contracts/architecture/

Step 4
Populate all required fields.

Step 5
Run validator (local or CI).

---

## 4. Enforcement Handshake

Products must:
	•	Import validator runtime from OS
	•	Reference validator rules
	•	Execute validation in CI before merge

CI must fail if:
	•	Required contract fields are missing
	•	OS version mismatch occurs
	•	Non-compliant architecture configuration detected

The OS is authoritative.
Products cannot override validation logic locally.

---

## 5. Deviation Protocol

If a product requires deviation from OS doctrine:
	1.	Create an ADR in the product repo.
	2.	Reference the specific OS clause.
	3.	Document rationale.
	4.	Accept explicit risk statement.
	5.	Record review approval.

Undocumented deviation is non-compliant.

---

## 6. Template Usage Rules

Templates in /templates/:
	•	Are immutable
	•	Must never be edited in product repos
	•	Must be versioned in OS via PR

If a template change is required:
	•	Submit OS PR
	•	Increment version
	•	Update changelog
	•	Update validator rules if necessary

---

## 7. OS Upgrade Process

When OS releases a new version:
	1.	Review changelog.
	2.	Evaluate breaking changes.
	3.	Update product /governance/build-os.yaml.
	4.	Re-run contract validation.
	5.	Update contract if required.

Products must not auto-upgrade without review.

---

## 8. Enforcement Philosophy

The OS exists to:
	•	Prevent silent architectural drift
	•	Prevent undocumented AI autonomy
	•	Preserve auditability
	•	Ensure survivability beyond individual contributors

This is a systems discipline layer.
Not a productivity layer.

---

## 9. Directory Expectations in Product Repos

Minimum required structure:

/contracts/
/governance/
/architecture/
/adr/
/ci/

These mirror OS expectations but remain product-scoped.

---

## 10. Non-Goals

The Build OS does not:
	•	Host product code
	•	Replace CI pipelines
	•	Define feature roadmaps
	•	Make architectural decisions for products

It defines guardrails.
Execution remains product responsibility.

---

## 11. Escalation

If a product cannot comply with OS doctrine:
	•	Escalate to OS Owner
	•	Document deviation formally
	•	Do not bypass enforcement

---

## 12. Summary

The Build OS is doctrine.

Products inherit it.
Contracts bind to it.
CI enforces it.
ADR documents deviation.

Discipline precedes velocity.

---
