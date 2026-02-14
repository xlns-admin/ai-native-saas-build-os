2026-02-13__SaaS-Build__Mobile-Support-Policy__v1.0__source.md

(Build OS Doctrine Section)

1. Purpose

This policy defines how mobile applications are treated within the AI-Native SaaS Build OS.

Mobile is not a feature.
Mobile is a client execution environment with distinct architectural, security, operational, and compliance constraints.

No mobile implementation may proceed without explicit declaration under this policy.

⸻

2. Classification of Mobile Clients

Mobile support must be explicitly classified into one of the following levels:

Level A — Responsive Web Only
	•	No native application.
	•	Mobile access delivered through responsive browser UI.
	•	No offline support.
	•	No push notifications.
	•	No device-level integrations.

Level B — Progressive Web Application (PWA)
	•	Browser-based installable experience.
	•	Limited offline read caching only.
	•	No offline write operations.
	•	Browser-based push notifications (where supported).
	•	No access to privileged device APIs.

Level C — Hybrid / Native Shell
	•	Web-based application wrapped in a native container.
	•	Native push notifications supported.
	•	Secure device storage used for tokens.
	•	Limited device APIs allowed (declared explicitly).
	•	No offline write queue unless separately approved.

Level D — Full Native Client
	•	Platform-specific application (iOS / Android).
	•	Offline write queue permitted.
	•	Background processing permitted.
	•	Device APIs permitted per approved scope.
	•	Requires extended security review and threat model update.

Movement between levels requires:
	•	An Architectural Decision Record (ADR).
	•	Updated Threat Model.
	•	Updated Technical Architecture Contract.
	•	Lifecycle Enforcer approval.

⸻

3. Architectural Requirements

All mobile implementations must:
	•	Depend on stable, versioned APIs.
	•	Use explicit API versioning policy.
	•	Avoid embedding business logic in the client.
	•	Treat the server as the system of record.
	•	Enforce schema contracts centrally.

Client code must never define canonical business rules.

⸻

4. Security Requirements

All mobile implementations must comply with:

4.1 Authentication
	•	Short-lived access tokens.
	•	Secure storage (OS-provided keystore / secure enclave).
	•	No long-lived secrets embedded in client code.
	•	MFA enforcement where applicable.
	•	Explicit session expiry behaviour.

4.2 Local Data Handling
	•	Local storage must be minimised.
	•	Cached data classification must be declared.
	•	Sensitive data must not persist beyond session without encryption.
	•	Logout must clear local storage.

4.3 Transport Security
	•	TLS required.
	•	Certificate validation mandatory.
	•	Certificate pinning decision must be documented via ADR.

4.4 Device Risk
	•	Rooted / jailbroken device detection strategy must be declared.
	•	Reverse engineering risk acknowledged.
	•	No client-side trust assumptions.

⸻

5. Offline Behaviour Policy

Offline behaviour must be explicitly declared in the Technical Architecture Contract:
	•	none
	•	read_cache_only
	•	write_queue_with_reconciliation

Offline write capability requires:
	•	Conflict resolution strategy.
	•	Data reconciliation logic.
	•	Explicit auditability of replayed writes.

Offline write without reconciliation design is prohibited.

⸻

6. Push Notification Governance

Push implementation must declare:
	•	Provider
	•	Tenant scoping model
	•	Opt-in mechanism
	•	Audit logging of sends
	•	Revocation process

Push notifications must not contain sensitive data unless encrypted and justified.

⸻

7. Privacy & Permission Governance

Mobile apps must:
	•	Declare minimum necessary device permissions.
	•	Justify each permission in the Threat Model.
	•	Align with Data Classification Policy.
	•	Comply with regional privacy laws (e.g., GDPR, CCPA where applicable).

Permission creep is treated as scope creep.

⸻

8. Release & Operational Requirements

Mobile releases must include:
	•	Defined rollout strategy (staged release recommended).
	•	Crash monitoring enabled.
	•	Performance monitoring enabled.
	•	Rollback capability (where platform permits).
	•	Store compliance checklist completed (if native).

Releases dependent on manual intervention are non-compliant.

⸻

9. Threat Model Extension Requirement

When mobile is introduced, the Threat Model must be updated to include:
	•	Device compromise scenarios.
	•	Man-in-the-middle attacks.
	•	Token extraction risk.
	•	Local storage exfiltration.
	•	Replay attacks from offline queue.

Failure to update the Threat Model blocks progression.

⸻

10. Lifecycle Enforcement Integration

The Lifecycle Enforcer must block:
	•	Native builds without ADR.
	•	Offline write without reconciliation design.
	•	Mobile release without crash monitoring.
	•	Permission requests without documented justification.
	•	API drift affecting mobile clients.

⸻

11. Escalation Principle

Mobile increases system complexity and security surface area.

Therefore:
	•	Mobile is an escalation event.
	•	Mobile requires architectural maturity.
	•	Mobile must not be introduced to compensate for unclear product-market fit.

⸻

12. Design Principle

APIs are permanent.
Clients are replaceable.

Mobile clients must be treated as replaceable surfaces over stable contracts.

⸻

