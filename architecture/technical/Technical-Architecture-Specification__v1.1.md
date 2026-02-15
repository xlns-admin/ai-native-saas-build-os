# Technical-Architecture-Specification__v1.1

AI-Native SaaS Build  
Technical Architecture Specification  

---

**Document:** Technical-Architecture-Specification__v1.1  
**Owner:** Human Orchestrator  
**Status:** Approved  
**Version:** v1.1  
**Review Cycle:** Quarterly or on Architectural Change  
**Classification:** Product Architecture — Canonical  
**Supersedes:** Technical-Architecture-Specification__v1.0 (if applicable)  
**Related Contract:** 2026-02-08__SaaS-Build__Technical-Architecture-Contract__v1.0__source.yaml  

---

# 1. Document Purpose

This document describes the logical and operational architecture of the AI-Native SaaS platform.

It defines:

- Hosting model  
- Control plane and execution model  
- Data architecture  
- Messaging integrations  
- Monitoring and resilience  
- Security posture  
- Replaceability principles  

This document explains the Technical Architecture Contract.  
It does not replace it.

The Contract is authoritative.  
This specification provides architectural clarity.

---

# 2. Architectural Design Principles

1. Databases are permanent.  
2. Providers are replaceable.  
3. Workflows are declarative.  
4. Execution is queued.  
5. Human authority remains final.  

These principles override tool convenience.

---

# 3. Infrastructure & Core Platform

## 3.1 Domains

**Provider:** IONOS  
**Purpose:** Domain ownership and registration  
**Classification:** Crown-jewel asset  
**Risk:** Loss equals platform control loss  

Domain ownership must remain separate from runtime hosting providers.

---

## 3.2 DNS, Edge, and WAF

**Provider:** Cloudflare  

**Functions:**
- DNS resolution  
- SSL termination  
- Web Application Firewall  
- DDoS mitigation  
- Bot mitigation (Turnstile)  

**Design Intent:**

All public traffic terminates at Cloudflare before reaching application infrastructure.

No direct origin exposure permitted.

---

## 3.3 Application Runtime

**Platform:** Lovable Cloud Pro  

**Responsibilities:**
- Frontend rendering  
- API surface  
- Edge Functions  
- Integrated Auth  

**Compute Model:**
- Static Edge Hosting (Frontend)  
- Supabase Edge Functions (Deno runtime)  

**Scaling Model:**  
Serverless, auto-scaled.

Application layer must remain stateless where possible.

---

## 3.4 Primary Database

**Platform:** Supabase (Managed PostgreSQL)  
**Hosting:** AWS-backed managed PostgreSQL  

**Security Controls:**
- Encryption at rest  
- Encryption in transit  
- Mandatory Row Level Security (Production)  

**Realtime:**  
Supabase Realtime enabled for near-realtime UI updates.

**Retention:**
- Standard logging retention: 7–14 days  
- Audit retention: 30+ days (plan-dependent)  

PostgreSQL is a non-negotiable core dependency.

---

# 4. Orchestration & Execution Model

This system separates:

- Control Plane  
- Execution Plane  

---

## 4.1 Control Plane

**Tool:** n8n (self-hosted)  
**Hosting:** Hetzner CX23  

**Responsibilities:**
- Workflow routing  
- Event orchestration  
- Dispatch control  
- Retry logic  

n8n coordinates execution.  
It must not contain core business logic.

---

## 4.2 Execution Plane

**Workers:** Hetzner CCX23 instances  

**Purpose:**
- Burst execution  
- Asynchronous task handling  
- Provider dispatch  

**Queue:**
- BullMQ (Open Source)  
- Redis (Upstash) as queue backend  

**Design Constraint:**

All external provider calls must be queued.

No synchronous provider calls from user-facing endpoints.

---

# 5. Messaging & External Channels

## Primary Messaging

**Twilio**
- Global SMS  
- WhatsApp  
- RCS  
- Usage-based billing  

**CM.com**
- UK optimisation  
- Cost fallback  

**Design Principle:**

Aggregator redundancy exists to prevent provider lock-in.

---

## Offline Channel (Future)

**PostGrid — Postal dispatch**

Marked as modular and optional future scope.

---

## Email Infrastructure

**Transactional:** Resend  
**Marketing:** Brevo  

**Separation Required:**

Transactional and marketing email infrastructure must remain logically separate.

---

# 6. Content Builders

**Unlayer**

Used for:
- Email authoring  
- Landing page authoring  

Constraint:
Unlayer exports HTML only.  
Rendering pipeline remains platform-controlled.

---

## Document Signing (Future Scope)

**PandaDoc (TBC)**

Explicitly marked as future and non-core.

---

# 7. Monitoring & Observability

## Error Tracking

**Sentry**

Mandatory for exception monitoring.

---

## Logging

**Betterstack**

Centralised logging.

Short retention acceptable for non-enterprise tier.

---

## Uptime Monitoring

**UptimeRobot**

External availability monitoring.

---

## Business Intelligence

**Looker Studio**

Reads Supabase for:
- Volume  
- Margin  
- Cost tracking  

**GA4**

Marketing analytics only.  
Not system telemetry.

---

# 8. Security & Identity

**Authentication:**  
Supabase Auth  
Password + Magic Link  

**MFA:**  
Supabase TOTP  
Mandatory for administrators  

**Secrets Management:**  
1Password Teams (human credentials only)

**Source Control:**  
GitHub (canonical repository)

**Bot Mitigation:**  
Cloudflare Turnstile  

**Backups:**
- Supabase managed backups  
- Hetzner backup snapshots  

**Workspace Backbone:**  
Google Workspace  

---

# 9. Replaceability Matrix

| Layer | Replaceable | Constraint |
|--------|-------------|------------|
| DNS | Yes | Domain ownership must remain separate |
| App Runtime | Yes | Must support RLS + serverless |
| Database | No (Core) | PostgreSQL required |
| Queue | Yes | Must support retry + rate control |
| Messaging | Yes | Aggregator abstraction required |
| Logging | Yes | Must preserve structured logs |
| Auth | Yes (with migration plan) | Must support JWT + RLS model |

Replaceability must be evaluated before vendor dependency expansion.

---

# 10. Control vs Data Separation

**Control Plane:**
- n8n  
- Worker dispatch  
- Queue orchestration  

**Data Plane:**
- Supabase  
- RLS enforcement  
- Business logic state  

These must never collapse into a single host without ADR approval.

---

# 11. Architecture Constraints

The following are non-negotiable:

- RLS enabled in production  
- Strict TypeScript only  
- No `any` type  
- No synchronous external provider calls  
- Queue-based dispatch for external services  
- All secrets managed outside repository  
- ADR required for architectural change  

Violations require documented deviation.

---

# 12. Versioning Discipline

Any change to:

- Hosting provider  
- Database engine  
- Tenancy model  
- Authentication model  
- Control plane location  
- Logging retention  
- Encryption standards  

Requires:

- ADR  
- Architecture Contract version bump  
- Lifecycle Enforcer validation  

No silent architectural drift permitted.

---

## Version History

v1.1 — Formalised governance headers, replaceability matrix, and architectural constraints.  
v1.0 — Initial specification draft.

---
