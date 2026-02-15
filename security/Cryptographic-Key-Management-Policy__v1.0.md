# Cryptographic-Key-Management-Policy__v1.0.md
AI-Native SaaS Build OS

---

**Document:** Cryptographic-Key-Management-Policy__v1.0.md  
**Owner:** Human Orchestrator  
**Status:** Active  
**Version:** v1.0  
**Review Cycle:** Annual  
**Escalation Requirement:** Mandatory for Enterprise Hardening Level 2 and above  
**Related Artefacts:**  
- Technical-Architecture-Contract__vX.Y.yaml  
- Vulnerability-Management-Policy__vX.Y.md  
- Threat-Model__vX.Y.md  
- Shared-Service-Boundary-Register__vX.Y.md  
- Tenant-Isolation-Claim__vX.Y.md  

---

# Cryptographic Key Management Policy

---

## 1. Purpose

This policy defines how cryptographic keys are generated, stored, used, rotated, revoked, and destroyed within the SaaS platform.

The objective is to ensure confidentiality, integrity, and controlled access to encrypted data across all environments.

---

## 2. Scope

This policy applies to:

- Application encryption keys  
- Database encryption keys  
- Cloud provider-managed keys  
- TLS certificates  
- API signing keys  
- Token signing secrets  
- Backup encryption keys  
- AI service integration keys  
- Any secret used to authenticate or encrypt data  

This policy applies to:

- Development  
- Staging  
- Production  
- Backup environments  

---

## 3. Definition

A cryptographic key is a secret value used to encrypt, decrypt, sign, verify, or authenticate data within the system.

---

## 4. Key Management Principles

All cryptographic keys must adhere to the following principles:

1. Least privilege access  
2. Separation of duties  
3. No hardcoded secrets  
4. Centralised secret storage  
5. Rotation by default  
6. Auditable access  

Keys are treated as critical security assets.

---

## 5. Key Generation

Keys must:

- Be generated using approved cryptographically secure random number generators (CSPRNG)  
- Meet minimum length requirements appropriate to the algorithm  
- Not be manually generated or reused across environments  

Approved algorithms include:

- AES-256 for symmetric encryption  
- RSA-2048 or higher for asymmetric encryption  
- ECDSA or Ed25519 where appropriate  
- TLS 1.2+ for transport encryption  

Weak or deprecated algorithms must not be used.

---

## 6. Key Storage

Keys must never be:

- Stored in source code  
- Committed to Git repositories  
- Embedded in frontend applications  
- Logged in plaintext  
- Shared via unsecured communication channels  

Keys must be stored in:

- Managed secret stores (e.g. cloud-native key vaults)  
- Hardware-backed key management systems where available  
- Encrypted configuration systems with role-based access  

Secrets must be environment-isolated.

---

## 7. Access Control

Access to keys must:

- Be role-based  
- Be logged  
- Require authentication  
- Be restricted to minimum required scope  

Production keys must not be accessible from development environments.

Access must be revoked immediately upon:

- Role change  
- Termination  
- Suspicion of compromise  

---

## 8. Key Usage Rules

Keys must be:

- Used only for their declared purpose  
- Scoped per environment  
- Scoped per tenant where required (multi-tenant isolation)  

Shared master keys across tenants are prohibited unless explicitly documented and risk-assessed.

All key usage must align with the Access-Control-Matrix.

---

## 9. Key Rotation

Rotation must follow:

| Key Type | Rotation Frequency |
|-----------|-------------------|
| TLS Certificates | Before expiry (automatic renewal preferred) |
| API Secrets | Every 90 days |
| Database Encryption Keys | Annual or upon suspected compromise |
| Token Signing Keys | Every 180 days |
| Compromised Keys | Immediate |

Automated rotation is preferred.

Where rotation is manual:

- A change record must exist  
- A rollback plan must exist  
- Rotation must be verified  

---

## 10. Key Revocation & Compromise Handling

If key compromise is suspected:

1. Revoke immediately.  
2. Rotate affected credentials.  
3. Invalidate issued tokens.  
4. Investigate access logs.  
5. Document the incident.  

This process must integrate with the Incident Response Playbook.

---

## 11. Backup & Recovery

Backup encryption keys must:

- Be stored separately from primary systems  
- Be recoverable through documented procedures  
- Be tested annually for restoration capability  

Loss of encryption keys must be treated as potential data loss.

---

## 12. Multi-Tenant Considerations

For multi-tenant architectures:

- Tenant-level encryption keys are preferred for high-sensitivity environments.  
- Shared service keys must be documented in the Shared-Service-Boundary-Register.  
- Key separation strategy must be declared in the Tenant-Isolation-Claim.  

Cross-tenant cryptographic key sharing is prohibited without documented architectural justification and risk acceptance.

---

## 13. AI & Third-Party Key Use

API keys for AI services must:

- Be stored in secure vaults  
- Be scoped per environment  
- Be rate-limited where supported  
- Not expose tenant-sensitive data without explicit approval  

External model providers must not receive platform encryption keys.

AI systems must not generate or store cryptographic keys autonomously.

---

## 14. Audit & Monitoring

The following must be logged:

- Key creation events  
- Access attempts  
- Failed access attempts  
- Rotation events  
- Revocation events  

Logs must be immutable and retained according to the Data Retention Policy.

Suspicious access patterns must trigger review.

---

## 15. Risk Acceptance

Exceptions require:

- Written justification  
- Explicit risk acceptance  
- Defined compensating controls  
- Expiry date  

Permanent exceptions are prohibited.

Expired exceptions block production deployment.

---

## 16. Policy Review

This policy must be reviewed:

- Annually  
- After any security incident involving keys  
- Upon significant architectural change  

Major key strategy changes require ADR approval.

---

## 17. Non-Goals

This policy does not:

- Define encryption architecture  
- Replace secure coding practices  
- Guarantee protection against insider threats  

It defines disciplined key lifecycle control.

---

## 18. Ownership

The Human Orchestrator retains accountability for key governance.

Operational delegation does not transfer responsibility.

---

## Version History

| Version | Date | Change | Author |
|----------|------------|--------|--------|
| 1.0 | 2026-02-08 | Initial canonical cryptographic key management policy | System |

---
