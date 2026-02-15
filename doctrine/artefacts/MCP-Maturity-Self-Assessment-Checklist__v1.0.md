# MCP-Maturity-Self-Assessment-Checklist__v1.0

AI-Native SaaS Build OS  
Model Context Protocol Maturity Self-Assessment Checklist

---

**Document:** MCP-Maturity-Self-Assessment-Checklist__v1.0  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.0  
**Review Cycle:** Quarterly  
**Classification:** Canonical Doctrine  
**Supersedes:** None  
**Applies to:** All governed product repositories implementing MCP  

---

## 1. Purpose

This checklist evaluates the maturity of the Model Control Plane (MCP) within an AI-Native SaaS system.

It determines whether the MCP operates as:

- A wrapper  
- A policy gateway  
- An auditable execution fabric  
- An adaptive governance layer  

Assessment must be evidence-based.

Assertions without artefacts do not qualify.

---

## 2. Usage Instructions

For each capability:

- Mark PASS only if implemented and verifiable.  
- Mark PARTIAL if implemented but incomplete.  
- Mark FAIL if absent.  

Maturity level is determined by the lowest failing prerequisite in sequence.

You cannot claim v3 if v2 controls are incomplete.

---

# Section 1 — MCP v1: Centralised Wrapper

---

## 1.1 Single Egress Enforcement

- All AI model calls route through a single MCP endpoint.  
- Direct model invocation is blocked at application level.  
- Evidence required: Architecture diagram + code enforcement.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 1.2 Model Abstraction Layer

- Model provider is abstracted.  
- Swapping providers requires no application code change.  
- Evidence required: Provider interface contract.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 1.3 Invocation Logging

- Logs include timestamp, model, prompt hash, token count, cost estimate.  
- Logs centrally stored.  
- Evidence required: Sample log entries.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 1.4 Role Routing

- Logical agent roles (builder, critic, etc.) defined at MCP layer.  
- No role logic embedded in UI components.  
- Evidence required: MCP routing configuration.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

If any item above is FAIL → MCP is below v1 maturity.

---

# Section 2 — MCP v2: Policy-Enforced Gateway

---

## 2.1 Tenant Context Isolation

- Tenant ID required per invocation.  
- Cross-tenant access technically impossible.  
- Evidence required: Enforced policy + integration tests.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 2.2 Policy Profiles

- Defined execution policies (public, confidential, regulated).  
- Policies enforced automatically.  
- Evidence required: Policy manifest.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 2.3 Context Allowlist

- AI receives only declared inputs.  
- Hidden global state blocked.  
- Evidence required: Context filtering logic.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 2.4 Tool Invocation Controls

- Tools require explicit permission.  
- Tool calls logged.  
- Evidence required: Allowlist registry.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 2.5 Rate Limiting

- Tenant-level rate limiting enforced.  
- Burst controls configured.  
- Evidence required: Rate limit configuration.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

If any v2 item FAIL → MCP cannot claim v2 maturity.

---

# Section 3 — MCP v3: Auditable Execution Fabric

---

## 3.1 Immutable Trace Store

- AI invocation logs are append-only.  
- Tamper detection present.  
- Evidence required: Storage configuration + write controls.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 3.2 Execution Lineage

Output traceable to:

- Input prompt hash  
- Context snapshot  
- Policy profile  
- Model version  

Evidence required: Lineage record.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 3.3 Policy Decision Logging

- Each invocation logs policy decision path.  
- Evidence required: Policy evaluation output.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 3.4 Audit Export Capability

- Tenant-level AI activity exportable.  
- Export includes timestamps, classification, cost.  
- Evidence required: Export example.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 3.5 AI Risk Classification

- Invocation risk tier assigned.  
- Risk tier influences policy enforcement.  
- Evidence required: Risk mapping definition.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

If any v3 item FAIL → MCP cannot claim v3 maturity.

---

# Section 4 — MCP v4: Adaptive Governance Layer

---

## 4.1 Compliance Drift Detection

- Automated checks compare execution against policy.  
- Drift events logged and alerted.  
- Evidence required: Drift detection report.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 4.2 Behavioural Anomaly Detection

- Model output behaviour monitored.  
- Outlier detection configured.  
- Evidence required: Anomaly report.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 4.3 Dynamic Model Routing

Model selection varies by:

- Cost profile  
- Risk profile  
- Workload type  

Evidence required: Routing policy engine configuration.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 4.4 Token Efficiency Optimisation

- Usage trends analysed.  
- Token optimisation implemented.  
- Evidence required: Cost report + optimisation log.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

## 4.5 Governance Dashboard

Real-time metrics available for:

- Invocation volume  
- Policy violations  
- Cost per tenant  
- Risk distribution  

Evidence required: Dashboard screenshot or access.

Status: ☐ PASS ☐ PARTIAL ☐ FAIL  

---

If any v4 item FAIL → MCP remains at v3 maturity.

---

# 5. Maturity Determination

| Level | Qualification Rule |
|-------|-------------------|
| v1 | All v1 items PASS |
| v2 | All v1 + v2 items PASS |
| v3 | All v1–v3 items PASS |
| v4 | All v1–v4 items PASS |

No partial maturity claims permitted.

---

# 6. Integrity Rule

This checklist must be reviewed:

- Quarterly  
- Before enterprise onboarding  
- After major architectural changes  
- Before compliance audits  

Assessment outcome must be recorded in:

- `/governance/build-os.yaml`
- Changelog entry
- Relevant ADR if maturity level changes

---

# 7. Final Principle

An MCP without enforcement is a wrapper.  
An MCP without traceability is theatre.  
An MCP without policy is risk.  
An MCP without adaptation is technical debt waiting to happen.

End of Document.
