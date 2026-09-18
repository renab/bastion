# Bastion Planetary Industry UI Reference

![Bastion PI visual direction](pi-ui-reference.png)

This is an approved visual-direction and information-architecture reference for Bastion **Planetary Industry (PI)**. It should guide hierarchy, operational density, panel relationships, network-centric views, black-glass visual language, and the separation of active, planning, exceptional, and data-unavailable states.

It is not a pixel-perfect implementation specification. Fictional names, values, tab labels, graph geometry, button copy, component dimensions, backend schema, and unsupported EVE capabilities are not authoritative. Where a rendering and a current Bastion decision conflict, the current decision wins.

## Authoritative design sources

- **Structured authority:** Galaxy `wormlife` / `architecture_decision` / `bastion-pi-domain-v1`, current leaf `884e9970-22e6-4e5a-8c48-dcfcee0ddea2` (active design iteration).
- **Human-readable design context:** `wormlife-trial/05 Planning/Outbound Flight - Bastion Design Notes.md`.
- **Historical lineage:** `wormlife-trial/05 Planning/Outbound Flight - Nirauan Design Notes.md`, except where superseded.
- **Standing operating rules:** `wormlife-trial/04 Reference/Assistant Operating Rules.md`.

The design record establishes PI as a first-class Bastion planning and operations domain. It is a whole-network optimization system, not a planet browser, extractor-program list, generic KPI dashboard, or recreation of EVE's planetary surface UI.

## Product model

The core workflow is:

**Plan the network → deploy manually in EVE → operate from Bastion → simulate through stale ESI → compare reality against the accepted plan → continuously optimize toward equilibrium.**

The dominant concepts are production flow, target architecture, current state, observed versus simulated state, tending/intervention timing, equilibrium/drift, and explainable optimizer recommendations.

### Normal home-system scope

PI planning normally follows the configured **Operations HQ / home system**. The optimizer uses its planets plus available PI-capable characters, colony slots, relevant skills, known facility limits, and applicable tax/logistics assumptions. Its objective is to maximize sustainable economic output subject to the operator's selected interaction budget—not raw theoretical output alone.

Remote/off-home colonies remain visible and operable when deliberately retained, but do not silently enter normal home-system optimization. Changing Operations HQ must not rewrite existing PI history or plans: prior-home plans become **Needs Rebase / Home Changed** and the affected colonies are surfaced as one aggregated Attention item.

## Primary surfaces

### PI Overview — live network operations

The active-home landing page is a whole production-chain graph:

`Extraction colonies → P1/intermediate flows → factory colonies → target output`

Nodes should communicate character, planet, role, product, projected/current throughput, feed or storage health, observed/simulated freshness, next intervention, and meaningful healthy/starving/accumulating/expired/stale state. Edges communicate commodity, direction, rate, and healthy/degraded/stopped state. Motion is allowed only when it explains real flow and must respect reduced-motion preferences.

The summary favors Accepted Plan, Target Output, Projected Throughput, Next Intervention, Network Health, and Simulation Confidence. A contextual operational region keeps Next Intervention and Optimization / Drift actionable without displacing the network graph.

### PI Planner — design and optimize

The planner chooses a production goal and interaction/tending cadence such as twice daily, daily, every two days, or custom. Optional constraints may cover imports, hauling tolerance, capital, rebuild tolerance, reserved slots, and excluded planets or characters.

Return a small set of strong candidate networks, not raw solver output. Compare output/day, modeled economic value/day, interaction cadence, planets/characters, hauling burden, tax, rebuild effort, resilience/confidence, and bottlenecks. **Accept Plan** makes a candidate the durable target architecture; it never changes colony layouts in EVE.

### Accepted PI Plan — target architecture and current versus plan

An accepted plan is a durable first-class object. It records the target chain/output, character-to-colony assignments, planet roles, expected extraction and processor throughput, buffers, pickup/drop cadence, factory feed, final output, assumptions, and tending cadence.

The central comparison is **Planned vs Current**: extraction, utilization, buffers, factory feed, tending cadence, and final output. Fresh authoritative observations win over projections; recommendations become explicit plan revisions rather than silent mutations.

### Colony detail — contextual process flow

Open colony detail from a network node in a drawer/inspector first, with **Open Full View** for deeper work. Prefer material flow—`ECU/resource source → storage/launchpad → processors → output`—over a reimplementation of the EVE planetary map. Show program expiry, processors, storage utilization, CPU/PG where useful, routes, projected runtime/output, latest authoritative observation, simulated state, and variance from the accepted plan.

## Contextual workflows

- **Intervention / service run:** group required manual EVE actions by character and planet, with due time, consequence, and defer/snooze where appropriate.
- **Optimization proposal:** show the observed issue, evidence, proposed change, expected output/economic and tending effects, rebuild cost, affected colonies, and confidence. Actions are Accept as Plan Revision, Defer, or Keep Current Plan—never an automatic plan change.
- **Observed versus simulated reconciliation:** retain prediction history; when fresh ESI or user-confirmed state differs materially, show projected amount, observed amount, error, affected flows, and updated confidence.
- **Plan comparison:** compare strong candidates side-by-side on output, value, cadence, colony/character use, hauling, tax, rebuild cost, and resilience.
- **PI logistics / collection plan:** PI owns immediate colony servicing. Once goods enter controlled structure/station/hangar custody, Inventory, Logistics, and Finance own them.

## Landing and exceptional states

| State | Required behavior |
| --- | --- |
| Active home network | Normal network Overview; off-home colonies appear as a compact persistent warning and review action. |
| Off-home only / home changed | Migration/rebase view, not empty onboarding. Show current home, grouped off-home colonies, known plan, and actions to review, retain remotely, plan current home, or rebase/retire. |
| No colonies anywhere | Purposeful **Start Planetary Industry** onboarding. Show home planets, PI-capable characters, skills, capacity, and data health; lead with **Design First PI Network**. |
| State unavailable | Never infer zero colonies from missing/stale ESI. Identify affected characters/scopes and direct authorization repair to **Accounts / Characters**, not Settings. |

## Observed, simulated, and financial boundaries

**Observed state** is the latest authoritative ESI or user-observed colony state. **Simulated state** is a deterministic projection forward while telemetry is stale. New authoritative observations replace projection as current truth while retaining prediction/error history.

PI can display modeled market, opportunity, throughput, and chain value for planning. However, on-planet, launchpad/storage, POCO-side, simulated, or otherwise planetary-chain goods are excluded from Finance Total Assets, Net Position, and enterprise Inventory valuation. Financial recognition starts only when goods are actually observed in enterprise-controlled structure, station, or hangar custody.

PI taxes, construction charges, and other real costs are recognized when incurred. A personal character's enterprise PI payment creates enterprise expense plus reimbursement payable; reimbursement settles that liability and is not a second expense.

## Interpretation freedom

Future UI/UX work may improve layout, proportions, responsive behavior, drawer/modal usage, progressive disclosure, graph composition, typography, table structure, controls, and density. It must preserve workflow semantics, source-of-truth handling, plan-versus-live distinction, observed-versus-simulated distinction, home-system behavior, manual-deployment boundary, optimizer objective, and the Finance custody boundary.

**Status:** approved visual direction and information-architecture reference; not a pixel contract.
