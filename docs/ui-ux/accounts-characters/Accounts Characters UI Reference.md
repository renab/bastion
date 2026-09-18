# Accounts / Characters UI Reference

![Accounts and characters workspace](accounts-characters-workspace.png)

## Product purpose and concept

Accounts / Characters is the first-class canonical surface for EVE account and character control. It owns account grouping, Alpha/Omega subscription state, portraits, individual ESI authorization health/scopes/re-authorization/disconnect, live skill queue, shared skill-plan assignment, milestone dates, capability summary, and skillbook sourcing economics. It is not a Settings panel, and an account seat is not a top-level operational entity.

The primary workspace uses a compact account group/character roster alongside a selected character profile. The profile makes current queue, plan milestones, training readiness, and source-aware skillbook comparison inspectable. A skillbook recommendation compares remote injection with Market HQ acquisition; a corporate plan export is an explicit generated artifact, never a silent write to EVE. Character and account detail opens in a context-preserving drawer before full-page handoff.

### States and workflow

| State | Product behavior |
| --- | --- |
| Connected and fresh | show scope health, queue and plan evidence timestamps |
| Authorization missing or stale | explain unavailable fields and offer re-authorize; do not fabricate live state |
| Alpha constraint | surface plan blockage/capability effect rather than treating it as an account-seat warning |
| No linked characters | onboarding to connect an EVE account; no empty data grid |

Workflow: select account -> select character -> inspect plan/milestones -> compare skillbook sourcing -> export corporate plan or initiate procurement proposal -> act in Procurement after explicit promotion.

**Must not do:** move ESI controls into Settings; shorten canonical names conversationally; treat remote injection as free; represent proposed skillbook needs as a purchase order; or imply auth permits actions beyond available scopes.

## Source audit

- Current Galaxy `bastion-account-character-module-v1` (`cae3eae1-ac22-499c-9681-d19b46212dc6`) owns ESI and account/character boundaries.
- Current Galaxy `bastion-procurement-logistics-workflow-v1` (`9a4b6f9c-c85d-4a9e-8c57-ec782bcc2fbd`) settles skillbook sourcing and promotion semantics.
- Current Galaxy `bastion-cross-domain-navigation-v1` (`44cb69f8-0733-4a15-9328-f1ff41d94bbc`) settles contextual drill-through.
- ESI is the live truth for supported character/account state; the visual uses prototype/sample values and explicitly renders missing-scope degradation.

## Visual-generation brief and mockup audit

Render a 16:9 dense desktop `Accounts / Characters` page: account-group roster with Alpha/Omega badges, portrait-led full canonical sample names, one selected character profile, ESI authorization health/scopes, live skill queue, shared plan milestones, skillbook remote-vs-Market-HQ comparison, and an explicit `Export Corporate Plan` action. The selected profile can be a right glass drawer. Include `PROTOTYPE - SAMPLE DATA - NOT LIVE`. Avoid seat cards, Settings navigation for ESI, generic avatars, and any secret/token content.

Audit: the reference maintains account-to-character grouping; makes reauthorization a visible recovery action; shows a concrete plan-to-procurement handoff without conflating it with purchase execution; and does not position accounts as a dashboard metric.

## Interpretation boundary

Can change: profile layout, portrait source treatment, exact scope labels, comparison columns, and milestone visualization. Must preserve: Accounts ownership of ESI, character-level canonical detail, Alpha/Omega relevance, live queue/plan/milestone context, explicit export, and procurement promotion boundary.
