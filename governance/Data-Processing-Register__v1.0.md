# Data-Processing-Register__v1.0.md
AI-Native SaaS Build OS

---

**Document:** Data-Processing-Register__v1.0.md  
**Owner:** Human Orchestrator  
**Oversight:** Security Lead  
**Status:** Active  
**Version:** v1.0  
**Review Cycle:** Annual  
**Applies To:** All production and operational data processing activities  

---

# Data Processing Register

This document constitutes the Record of Processing Activities under Article 30 of the UK GDPR and EU GDPR.

It documents all personal data processing performed by the SaaS platform in a structured, auditable format.

---

## 1. Purpose

The purpose of this register is to:

- Provide a complete inventory of personal data processing
- Document lawful bases for processing
- Demonstrate accountability under GDPR
- Support regulatory audits
- Ensure processing reflects actual operational data flows

This register must reflect reality, not intention.

---

## 2. Scope

This register applies to:

- Core product processing
- Tenant-level processing
- AI-assisted processing
- Logging and monitoring data
- Employee and contractor data
- Marketing and analytics data
- Support and customer service interactions

All processing involving identifiable individuals must be declared.

---

## 3. Data Controller and Processor Roles

### Organisation Role

The platform operates as:

- **Data Processor** when acting on behalf of tenants
- **Data Controller** for:
  - Employee and contractor data
  - Marketing data
  - Website analytics
  - Operational logs not tied to tenant ownership

Role classification must be declared per processing activity.

---

# 4. Processing Activity Records

Each processing activity must follow the structure below.

---

## Processing Activity Record Template

### 1. Activity Name

Descriptive title of the processing activity.

---

### 2. Controller / Processor Role

Indicate:

- Controller  
- Processor  
- Joint Controller  

---

### 3. Purpose of Processing

Clear and specific purpose.

Avoid vague statements such as “service improvement.”

---

### 4. Categories of Data Subjects

Examples:

- End users  
- Tenant administrators  
- Employees  
- Website visitors  
- Support requesters  

---

### 5. Categories of Personal Data

Examples:

- Name  
- Email address  
- IP address  
- Usage data  
- Device identifiers  
- Billing information  
- Authentication tokens  

Sensitive data must be explicitly identified.

---

### 6. Special Category Data

State:

- None  
- Or specify category (e.g. health data, biometric data)

If special category data is processed, additional lawful basis must be documented.

---

### 7. Lawful Basis for Processing

Specify one:

- Contract  
- Legitimate interest  
- Legal obligation  
- Consent  
- Vital interest  
- Public task  

If Legitimate Interest:

- A documented Legitimate Interest Assessment must exist.

---

### 8. Data Recipients

List:

- Internal roles with access  
- Sub-processors  
- Infrastructure providers  
- AI service providers  

Must align with Sub-Processor Register.

---

### 9. International Transfers

State:

- None  
- Or specify destination country  

If outside UK/EU:

Specify transfer mechanism:

- Standard Contractual Clauses  
- UK International Data Transfer Agreement  
- Adequacy Decision  
- Binding Corporate Rules  

---

### 10. Retention Period

Specify:

- Exact time period  
- Or clear retention trigger  

Retention must align with the Data Retention & Deletion Policy.

---

### 11. Technical & Organisational Security Measures

Summarise:

- Encryption at rest  
- Encryption in transit  
- Access controls  
- Audit logging  
- Tenant isolation controls  
- Key management  
- Monitoring  

Reference relevant policy documents.

---

### 12. Automated Decision Making

State:

- None  
- Or describe logic and safeguards  

If AI processing occurs:

- Confirm whether human review exists  
- Describe AI boundary controls  
- Confirm no uncontrolled automated legal effects occur  

---

# 5. Master Processing Inventory

This table summarises all processing activities.

| Activity Name | Role | Purpose | Data Subjects | Personal Data | Lawful Basis | International Transfer | Retention |
|---------------|------|----------|---------------|----------------|---------------|------------------------|-----------|

This table must always match the detailed records above.

---

# 6. AI-Specific Processing Declaration

Where AI services are used:

- Data types sent to AI must be declared  
- Whether prompts include personal data must be declared  
- Data minimisation strategy must be stated  
- Whether provider stores prompts must be documented  
- Whether training reuse occurs must be stated  

AI processing must be traceable to declared purposes.

---

# 7. Data Minimisation Statement

Only data necessary for the declared purpose may be processed.

The following are prohibited unless explicitly justified:

- Collecting data “just in case”
- Retaining logs indefinitely
- Training AI on tenant data without explicit agreement
- Expanding data use beyond original declared purpose

---

# 8. Update Requirements

This register must be updated:

- When new features introduce new processing  
- When a new sub-processor is added  
- When retention periods change  
- After any incident affecting personal data  
- When AI tooling changes data flow  

All updates must be versioned.

---

# 9. Ownership

The Human Orchestrator retains accountability for accuracy of this register.

Operational maintenance may be delegated.

Accountability may not be delegated.

---

# 10. Review Cycle

This register must be reviewed:

- Annually  
- After major architectural changes  
- After security or data incidents  
- After introduction of new AI systems  

---

## Version History

| Version | Date | Change | Author |
|---------|------|--------|--------|
| v1.0 | 2026-02-08 | Initial Article 30 Record of Processing Activities | System |

---

# Governing Principle

If you process personal data, you must know:

- Why you process it  
- What you process  
- Who sees it  
- Where it goes  
- How long it lives  
- How it is protected  

If you cannot answer those six questions, you do not control your system.
