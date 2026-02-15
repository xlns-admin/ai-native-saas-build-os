# MCP-Architecture__v1.0

AI-Native SaaS Build OS  
Model Context Protocol Architecture

---

**Document:** MCP-Architecture__v1.0  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.0  
**Review Cycle:** Annual  
**Classification:** Canonical Doctrine  
**Supersedes:** None  
**Applies to:** All governed product repositories implementing AI model invocation  

---

## 1. Purpose

This document defines a minimal, enterprise-credible **Model Context Protocol (MCP) Architecture** for an AI-native SaaS ecosystem.

This architecture introduces a **single governed path** for all model interactions, enabling:

- Deterministic routing of AI work to approved models and tools  
- Policy-controlled context injection and redaction  
- Auditability, cost control, and tenant-safe isolation  
- Compatibility with multi-agent orchestration patterns  

This artefact is architecture doctrine.  
It is not a product specification.

---

## 2. Canonical Definition

**MCP Layer:**  
The MCP Layer is a centralised control plane service that mediates all interactions between an application and AI models by enforcing policy, injecting authorised context, executing approved tools, and recording an auditable trace of every request and response.

---

## 3. Scope

### 3.1 In Scope

- Runtime model invocation governance  
- Context assembly and injection  
- Tenant policy enforcement  
- Tool execution mediation  
- Full request, response, and tool trace logging  
- Cost and rate-limit controls  
- Deterministic agent role routing  

### 3.2 Out of Scope

- Training or fine-tuning models  
- Model hosting infrastructure  
- UI-level prompt authoring  
- Autonomous decision-making without human or policy gates  
- Complex “AI memory” beyond controlled retrieval  

---

## 4. Architectural Principles

1. **Single Egress Rule**  
   All model calls must traverse the MCP Layer. No direct model provider calls are permitted from application code.

2. **Policy Before Execution**  
   Every invocation is evaluated against a policy profile before context is injected or execution begins.

3. **Context Is Loaded State**  
   Context injection is treated as state assembly, not conversational convenience.

4. **Tenant Isolation Is Mandatory**  
   No cross-tenant context retrieval is permitted unless explicitly policy-authorised and logged.

5. **Auditability Is Default**  
   Every invocation produces a trace sufficient to explain why an output occurred.

6. **Tools Are Privileged**  
   Tool usage is permissioned explicitly per invocation and per agent role.

---

## 5. Reference Architecture

### 5.1 Primary Components

**Application Runtime**  
- UI, API, and backend services that request AI work  
- Must not call model providers directly  

**MCP Layer**  
- Sole interface for model invocation  
- Enforces policies, builds context, routes to models, manages tools, and records traces  

**Policy Engine**  
- Evaluates invocation against rules  
- Applies data classification, redaction requirements, and tool permissions  

**Context Store**  
- Canonical sources of truth for retrieval  
- Examples: ADRs, schemas, runbooks, product requirements, known constraints  

**Trace Store**  
- Immutable audit log for AI execution  
- Stores metadata and optionally redacted payloads  

**Model Providers**  
- Approved external LLM providers or internal model endpoints  

**Tool Gateway**  
- Controlled interface for tool execution  
- Applies allowlists, parameter validation, and timeouts  

---

## 6. Control Flow

### 6.1 Invocation Lifecycle

1. **Request Received**  
   Application calls MCP with a structured invocation request.

2. **Policy Evaluation**  
   MCP applies policy based on tenant, agent role, and intent.

3. **Context Assembly**  
   MCP retrieves authorised context from approved sources.  
   Redaction is applied according to data classification.

4. **Model Routing**  
   MCP selects an approved model profile based on role and workload.

5. **Tool Mediation (Optional)**  
   If tools are allowed, MCP executes tools through Tool Gateway.  
   Tool inputs and outputs are validated and traced.

6. **Response Construction**  
   MCP returns a structured response with output plus metadata.  
   Human approval gates are enforced outside MCP.

7. **Trace Recording**  
   MCP writes an immutable execution trace and cost record.

---

## 7. Interfaces

### 7.1 MCP Execution Endpoint

**Endpoint**  
`POST /mcp/execute`

### 7.2 Invocation Request (Canonical Fields)

- `tenant_id`  
- `invocation_id`  
- `agent_role`  
- `intent`  
- `policy_profile`  
- `input_payload`  
- `context_refs` (optional explicit references)  
- `tool_allowlist` (optional)  
- `output_schema` (optional)  

### 7.3 Invocation Response (Canonical Fields)

- `invocation_id`  
- `status` (success | blocked | failed)  
- `output_payload`  
- `trace_id`  
- `cost_estimate`  
- `policy_decisions` (summary)  

---

## 8. Agent Role Routing

Agent roles are logical functions, not personas.

Examples:

- `architect.validation`  
- `builder.implementation`  
- `critic.adversarial_review`  
- `historian.decision_capture`  
- `support.classification`  
- `ops.runbook_assist`  

Routing rules map:

- role → approved model profile  
- role → allowed tools  
- role → context source allowlist  
- role → output schema constraints  

---

## 9. Policy Profiles

Policy profiles are named bundles of constraints.

Minimum viable profiles:

- `public_safe`  
- `internal_non_sensitive`  
- `tenant_confidential`  
- `regulated_restricted`  

Policy controls include:

- allowed model list  
- max tokens / budget caps  
- tool permissions  
- context retrieval sources  
- redaction rules  
- retention rules for traces  
- rate limits  

---

## 10. Context Assembly

### 10.1 Approved Context Sources

MCP may retrieve context only from declared sources.

Examples:

- `architectural_decision_records`  
- `domain_schema`  
- `non_functional_requirements`  
- `runbooks_and_incident_playbooks`  
- `known_constraints_and_non_goals`  

### 10.2 Retrieval Rules

- Retrieval must be explicit and traceable  
- Each retrieved item must include a source reference  
- Cross-tenant retrieval is forbidden by default  
- Sensitive content must be redacted before leaving MCP  

---

## 11. Traceability and Audit

Each invocation must produce:

- invocation metadata (tenant, role, intent)  
- policy decisions and enforcement outcomes  
- context items retrieved (references)  
- model profile used  
- tool calls executed (inputs, outputs, validation results)  
- response payload (or redacted payload)  
- token usage and cost  
- duration and failure reasons  

### 11.1 Trace Retention

Retention is policy-driven and must align with:

- data classification  
- regulatory obligations  
- contractual commitments  

---

## 12. Failure Handling

### 12.1 Failure Classes

**Blocked**  
Policy denies execution.

**Halted**  
Ambiguity detected or required inputs missing.

**Failed**  
Provider error, tool failure, timeout, validation failure.

### 12.2 Mandatory Behaviour

- On policy block, return deterministic refusal and reason  
- On ambiguity, halt and request clarification  
- On tool failure, surface partial outputs and trace  

---

## 13. Security Requirements

- Authentication and authorisation enforced per tenant  
- All context retrieval permissioned and logged  
- Tool parameters validated to prevent injection  
- Secrets must never be included in model context  
- Encryption at rest required for trace and context stores  

---

## 14. Cost and Rate Governance

MCP must record and expose:

- cost per invocation  
- cost per tenant per period  
- cost per agent role  
- rate limit events  
- budget cap blocks  

Minimum viable controls:

- per-tenant rate limits  
- per-tenant daily and monthly budgets  
- per-role token caps  

---

## 15. Integration Guidance

### 15.1 Recommended Placement

- Application runtime calls MCP via internal API  
- Orchestration workflows (e.g., n8n) call MCP, not model providers  
- Lifecycle Enforcer validates adherence to Single Egress Rule  

### 15.2 Non-Goal

MCP is not orchestration.  
It is the governed model execution layer.

---

## 16. Compatibility Notes

This architecture supports:

- AI squad and agent orchestration patterns  
- Multi-tenant compliance constraints  
- Enterprise governance requirements  
- Migration between model providers through routing abstraction  

---

## 17. Versioning

- **Major:** Breaking change to invocation contract or policy model  
- **Minor:** New policy profile, new role mapping, new trace field  
- **Patch:** Clarifications and non-breaking refinements  

---

## Version History

**v1.0** — Initial canonical MCP Architecture doctrine artefact.

---



