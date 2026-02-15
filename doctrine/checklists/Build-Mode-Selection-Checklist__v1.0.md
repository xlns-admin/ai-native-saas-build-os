# Build-Mode-Selection-Checklist__v1.0

AI-Native SaaS Build OS  
Governance Decision Instrument

---

**Document:** Build-Mode-Selection-Checklist__v1.0  
**Owner:** Build OS Maintainer  
**Status:** Approved  
**Version:** v1.0  
**Review Cycle:** Annual  
**Classification:** Canonical Doctrine  
**Supersedes:** None  
**Applies to:** All new builds governed by the AI-Native SaaS Build OS  

---

## 1. Purpose

This checklist formalises the decision between:

- Core Mode
- Enterprise Mode

Mode selection defines governance depth, enforcement strictness, and artefact requirements.

Mode must be selected before Stage 1 begins.

If no mode is declared → lifecycle progression must block.

Mode selection is a risk posture decision.

---

## 2. Core Decision Rule

Select **Enterprise Mode** if ANY of the following conditions apply.

If none apply, Core Mode may be selected.

---

## 3. Customer & Commercial Risk

- [ ] The system will serve external paying customers.
- [ ] The system will handle contractual SLAs.
- [ ] The system will process regulated industry data.
- [ ] Enterprise customers are expected within 12 months.
- [ ] The product will be marketed as production-grade SaaS.
- [ ] Investor or board scrutiny applies.
- [ ] Legal liability exposure exists beyond internal use.

If one or more are true → Enterprise Mode recommended.

---

## 4. Data Sensitivity & Compliance Risk

- [ ] Personal data (PII) will be processed.
- [ ] Special category data will be processed.
- [ ] Multi-tenant data isolation is required.
- [ ] Data residency requirements exist.
- [ ] Data retention policies vary by customer class.
- [ ] Audit export capability will be required.
- [ ] External compliance (SOC 2, ISO 27001, FCA, HIPAA, etc.) is anticipated.

If any are true → Enterprise Mode required.

---

## 5. Operational Risk

- [ ] 24/7 availability expectations exist.
- [ ] Incident response time commitments exist.
- [ ] On-call support model is required.
- [ ] Uptime guarantees will be advertised.
- [ ] Financial transactions will be processed.
- [ ] Messaging or payments infrastructure involved.
- [ ] Production data loss would cause reputational damage.

If any are true → Enterprise Mode required.

---

## 6. Architectural Complexity

- [ ] Multi-tenant architecture.
- [ ] Shared services across customers.
- [ ] Role-based access control beyond simple user roles.
- [ ] Admin impersonation capability.
- [ ] Background jobs operating across tenants.
- [ ] AI-driven automation affecting customer outcomes.

If more than one applies → Enterprise Mode recommended.

---

## 7. Growth Trajectory Risk

- [ ] User growth projected to exceed 1,000 users.
- [ ] Revenue target exceeds early-stage threshold.
- [ ] Funding event planned within 12–18 months.
- [ ] Acquisition target scenario plausible.
- [ ] Platform intended to host additional products.

If future scale is anticipated → Enterprise Mode may prevent rework.

---

## 8. Core Mode Suitability Criteria

Core Mode is suitable if ALL of the following are true:

- [ ] Internal or experimental use only.
- [ ] No regulated data.
- [ ] Limited user base.
- [ ] No contractual uptime commitments.
- [ ] No investor scrutiny.
- [ ] No external audit requirement.
- [ ] Short-lived or exploratory system.

Core Mode is not a shortcut.
It is appropriate for constrained environments.

---

## 9. Escalation Rule

If uncertainty exists:

- Default to Enterprise Mode, or
- Document the rationale for Core Mode in an ADR.

Mode decisions must be traceable.

---

## 10. Mode Declaration Requirements

Upon selection:

1. Update `/governance/build-os.yaml` with:
   - Selected mode
   - Justification summary
   - Date of declaration

2. Record ADR if:
   - Core Mode selected despite risk indicators, or
   - Enterprise Mode selected proactively.

3. Commit mode declaration before Stage 1 artefacts are created.

---

## 11. Mode Upgrade Rule

If risk posture changes:

- Funding event
- Customer onboarding
- Regulated data introduction
- Multi-tenant expansion

Then:

1. Perform gap analysis.
2. Raise Mode Upgrade ADR.
3. Implement missing artefacts.
4. Update governance declaration.
5. Re-run enforcement checks.

Silent escalation or downgrade is prohibited.

---

## 12. Governance Philosophy

Mode selection is not about speed.

It is about survivability.

Core Mode builds.
Enterprise Mode endures.

The Build OS does not prevent ambition.
It prevents fragility.

---

**Status:** Active  
**Version:** v1.0
