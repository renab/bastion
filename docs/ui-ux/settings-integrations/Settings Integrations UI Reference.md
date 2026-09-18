# Settings / Integrations UI Reference

![Settings and integrations workspace](settings-integrations-workspace.png)

## Product purpose and concept

Settings / Integrations is a low-frequency secondary administration surface reached from the application cog. It owns organization-wide configuration: Operations HQ/home system, Market HQ/trade hub, enterprise defaults, planning policies, system-level integration health, release/update controls, and advanced diagnostics. It does **not** own EVE account/character association, character portraits, character-scoped ESI authorization, skill queues, or subscriptions; those remain in Accounts / Characters.

The primary surface uses a compact left settings index and a high-opacity form/detail pane. Operations HQ and Market HQ are distinct settings with validation/impact preview; only Operations HQ anchors home operations. Integration panels show connector health, last successful sync, capabilities, degraded reason, and safe configuration actions without secrets. Update/engine controls show version/provenance/candidate status and explicit review/promotion boundaries.

### States and workflow

| State | Behavior |
| --- | --- |
| Healthy integration | show last success and supported capability, not credentials |
| Degraded/offline | explain affected features and recovery action |
| Changing HQ/default | show impact preview and require explicit save; do not silently migrate dependent state |
| Candidate update | evidence/diff/review state; never auto-promote an unreviewed engine/SDE candidate |

**Must not do:** put ESI auth here; show token values/secrets; represent Market HQ as Operations HQ; or surface this as a primary sidebar work domain.

## Source audit

- Current Galaxy `bastion-settings-integrations-domain-v1` (`3c5663ec-12d4-4d6b-9d76-7da59a0d8453`) sets cog-only, organization/system integration ownership and excludes Accounts/Characters ESI controls.
- Current Galaxy `bastion-account-character-module-v1` (`cae3eae1-ac22-499c-9681-d19b46212dc6`) supplies the ESI ownership boundary.
- Current Galaxy `bastion-update-management-v1` (`7660e036-cb72-4761-9b3b-05fbc272239b`) and `bastion-pyfa-update-pipeline-v1` (`64ad9e86-317b-47a4-8278-020e07b17e86`) require reviewed candidate promotion and provenance.

## Visual-generation brief and mockup audit

Render a 16:9 `Settings / Integrations` high-opacity administrative form reached via a small cog breadcrumb. Display separate Operations HQ and Market HQ configuration cards with impact preview, integration health rows (no tokens), a Pyfa/SDE candidate update panel with diff/review state, and a compact advanced diagnostics section. Include prototype/sample/not-live label. Avoid characters, account seats, ESI auth flows, exposed secrets, or an oversized public settings dashboard.

Audit: setting ownership is organization/system-level; the two HQs are visibly distinct; updates are candidates awaiting review; connection state conveys capability/freshness without leaking secrets.

## Interpretation boundary

Can change: index organization, field names, health visual, and diagnostic depth. Must preserve cog/low-frequency access, system-level ownership, Accounts ESI exclusion, separate HQ semantics, and explicit candidate-promotion boundary.
