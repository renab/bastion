# Bastion — Inventory / Assets Reference

Status: **Approved reference pack; canonical visuals approved**

Current authoritative design key:

- `bastion-inventory-assets-domain-v1`
- current Galaxy leaf at time of this reference: `dbaa1d28-62bc-433d-8253-99e954ec6dd4`

Related design records include:

- `bastion-design-source-priority-v1`
- `bastion-default-design-context-v1`
- `bastion-procurement-logistics-ui-v1`
- current Bastion Doctrine, Market/Trade, Finance, Industry/PI, Accounts/Characters, and Attention design records
- still-valid inherited Nirauan inventory/market architecture where not superseded

This document defines the intended product semantics and interaction model for the Bastion **Inventory / Assets** domain.

Written semantics and current structured Bastion design records outrank incidental labels, sample values, or omissions in generated reference images.

---

# 1. Product Role

Inventory / Assets is a first-class Bastion operating domain for answering two different but connected questions:

1. **What physical assets does Naffin Enterprises currently control, and where are they?**
2. **What portion of those assets is operationally available, allocated, staged, committed, or unavailable to Bastion workflows?**

Inventory / Assets is not merely an ESI asset browser.

It is the deterministic asset-state layer used by Doctrines, Procurement / Logistics, Industry, PI, Market / Trade, Finance, Analytics, and Accounts / Characters where character custody matters.

Inventory / Assets owns physical holdings and operational availability. It does not own market execution or accounting.

---

# 2. Domain Boundaries

## Inventory / Assets owns

- enterprise physical holdings
- asset identity
- current physical location
- custodian / owner context
- current quantity
- unique assembled-asset identity
- free vs allocated availability
- reservations and commitments
- staging state
- in-transit state
- configured hangar/container purpose
- asset readiness inputs
- freshness and source provenance
- movement/audit evidence where defensible

## Market / Trade owns

- current quotes
- order books
- open orders
- market positions
- fills
- order aging
- liquidation/listing execution
- current market valuation services

Inventory may display Market / Trade valuation context, but does not own it.

## Procurement / Logistics owns

- approved purchase requirements
- purchase orders
- sourcing
- haul loads
- movement execution
- import/export execution
- purchase-fit handoff to EVE

Inventory supplies current coverage and receives the resulting physical state.

## Finance owns

- historical acquisition basis
- accounting classification
- realized/unrealized treatment
- enterprise books

Inventory may display Finance context, but does not redefine it.

---

# 3. Source Model

Bastion's target Inventory model is not reconstructed from heterogeneous legacy Galaxy operational record kinds.

Target runtime state comes from:

- current ESI asset/location telemetry where exposed;
- current Bastion enterprise ownership/custody mappings;
- Bastion allocation/reservation state;
- Bastion hangar/container purpose configuration;
- Bastion logistics state;
- cross-domain references.

Legacy Galaxy acquisition records, snapshots, corrections and operational facts remain migration/provenance evidence. They are not the target runtime schema.

---

# 4. Physical Asset Hierarchy

For corporation storage, the familiar path is:

**System → Structure / Station → Hangar → Container → Item / Stack**

Bastion must not force every physical asset into that exact corporation-hangar shape.

The generalized path is:

**Solar System → actual Station/Structure or Space Location → actual EVE inventory location → Container/Ship sublocation → Asset/Stack**

Inventory-node types may include:

- corporation hangar division
- Item Hangar
- Ship Hangar
- ship
- ship cargo
- specialized ship bay
- container
- delivery / contract / other ESI-exposed inventory location
- other explicit physical inventory node supported by the source model

The UI should represent the real physical hierarchy rather than inventing a synthetic one for visual convenience.

---

# 5. Enterprise Scope

Inventory / Assets represents enterprise-controlled property, not merely corporation-owned ESI assets.

Enterprise scope may include:

- Naffin Enterprises corporation property
- character-held enterprise property
- enterprise-mapped market/trader property
- enterprise-controlled assembled ships
- enterprise inventory physically held by authorized operating characters

Custody and beneficial enterprise ownership are distinct concepts where necessary.

Physical possession by a character must not silently redefine accounting ownership.

---

# 6. Unique Assets vs Fungible Stock

Bastion distinguishes unique physical assets from fungible inventory.

## Unique assets

Examples:

- assembled ships
- fitted doctrine hulls
- specifically rigged variants
- named operational ships
- uniquely identified containers where identity matters

These retain item identity.

A fitted Vagabond is not merely `Vagabond x1`.

Its operational meaning may depend on rigs, current fitting, cargo/ammo, location, doctrine association, physical readiness, custodian, and staging state.

## Fungible stock

Packaged/stackable inventory may aggregate by type, physical location, state, and purpose.

Examples:

- ammunition
- minerals
- PI commodities
- packaged modules
- packaged hulls where individual identity is not operationally relevant

Aggregation must still support drilldown to source locations and allocations.

---

# 7. Physical Observation

Physical observation is separate from Bastion operational state.

Observed fields may include:

- item/type
- item identity where unique
- owner/custodian
- system
- structure/station
- hangar
- container/ship
- quantity
- packaged/assembled state
- fitting/rig/cargo where available
- observation timestamp
- source freshness
- degraded/unknown source state

The UI must distinguish a fresh physical observation from stale or unavailable telemetry.

---

# 8. Allocation and Placement Are Independent

Bastion must not collapse physical observation, allocation and placement into one overloaded status.

Two independent operational dimensions are required.

## Allocation

- **Free**
- **Reserved**
- **Committed**
- **Unavailable**

## Placement

- **Unstaged**
- **Staged**
- **In Transit**
- **At Market**

These dimensions may coexist.

Examples:

- Reserved + Staged
- Reserved + Unstaged
- Committed + In Transit
- Free + At Market
- Unavailable + Unstaged

---

# 9. Allocation Semantics

## Free

The asset/quantity is not consumed by another Bastion commitment and may be considered for a compatible requirement.

## Reserved

The asset/quantity is earmarked for an accepted requirement or target but has not yet crossed into active execution.

Examples:

- doctrine readiness target
- approved Industry project
- deliberately configured stock policy
- approved procurement fulfillment allocation

## Committed

The asset/quantity is bound to an active execution context and must not be considered free for a competing requirement.

Examples:

- active Industry job
- active logistics load
- active fulfilled procurement requirement awaiting delivery
- explicit operational deployment state where Bastion models it as committed

## Unavailable

The enterprise controls the asset, but it cannot currently satisfy the evaluated requirement.

Reasons may include wrong physical location, incompatible fit/rig state, inaccessible hangar/location, stale/untrusted telemetry, already consumed by another hard constraint, required physical state not met, or source uncertainty.

Unavailable must expose the reason.

---

# 10. Free Quantity

For stackable assets:

**Free Quantity = Observed Usable Quantity − Active Reserved Quantity − Active Committed Quantity**

The calculation is scoped to the requirement being evaluated.

Location, physical state, access policy and freshness may further reduce usable quantity.

Bastion must not double-count one physical stack against incompatible simultaneous requirements.

---

# 11. Projection Does Not Reserve Stock

A core Bastion rule:

**Planning and readiness projection do not automatically reserve inventory.**

A Doctrine may ask whether current assets could satisfy a fit. Industry may ask whether stock could satisfy a job. Procurement may ask how much of a request is already covered.

Those calculations may project available coverage without consuming stock.

A real reservation/commitment appears only when an explicit workflow has been accepted, an active execution object requires it, or Josh deliberately configures a stock policy that reserves it.

Doctrine existence alone must not auto-hoard modules, hulls, ammunition or consumables.

---

# 12. Allocation Conflict

When multiple accepted requirements compete for the same free stock, Bastion must surface a conflict.

It must not silently assign the same asset twice.

A conflict view should identify:

- contested item/type
- total observed quantity
- free quantity
- competing consumers
- existing reservation/commitment
- priority or sequencing context
- actions available to resolve the conflict

The owning workflows remain responsible for the operational decision.

Inventory provides the deterministic conflict truth.

---

# 13. Placement and Staging

Ownership is not readiness.

## Unstaged

The asset exists but is not at the operational location/state expected by the consuming workflow.

## Staged

The asset is physically located and configured as required for the consuming workflow.

## In Transit

The asset has been assigned to an active Bastion Logistics movement.

## At Market

The asset is physically positioned at the configured Market HQ / market-execution location.

`At Market` is a placement state, not a financial classification.

---

# 14. Doctrine Readiness

Doctrine readiness consumes Inventory state.

Important distinction:

**Allocated / Reserved** means Bastion has committed the asset to the Doctrine requirement.

**Staged** means it is physically where/in the state the Doctrine expects.

A Doctrine may therefore report:

- pilot ready ✅
- hull allocated ✅
- modules allocated ✅
- consumables allocated ✅
- staged at operational base ❌

This is a readiness failure, but not an ownership failure.

---

# 15. Rigged Variants

Loose rigs do not make a differently rigged Doctrine variant ready.

If a Doctrine requires a distinct physical rig configuration, Inventory must resolve readiness against the appropriate assembled/rigged hull.

The existing Bastion Doctrine rule remains: a rig-changing variant is normally a distinct physical hull/variant.

Inventory must preserve that distinction.

---

# 16. Industry and PI

Industry and PI consume Inventory as stock state.

Inventory provides free material quantity, reserved material quantity, committed WIP/input quantity where modeled, location, purpose, staging/access, and freshness.

Industry/PI own recipe/job/colony semantics, production planning, profitability, and job execution.

Inventory must not convert every potential plan into a material reservation.

Only accepted/active workflow state reserves or commits stock.

---

# 17. Procurement Integration

Procurement uses Inventory to determine whether a requirement still exists.

Flow:

**Originating need → inventory coverage projection → remaining gap → approved procurement requirement → purchase order → acquired → in transit / staged → satisfied**

When purchased stock arrives, Inventory should update the originating requirement based on actual delivered/staged physical state.

Partial fulfillment should reduce remaining requirement quantity rather than create duplicate demand.

---

# 18. Logistics Integration

Logistics owns movement execution.

Inventory owns the current physical and allocation state before/after movement.

An asset assigned to a Bastion haul load should generally become:

**Committed + In Transit**

When delivered to the required target:

**Reserved/Committed + Staged**

or return to **Free + Staged** depending on the owning workflow.

Inventory must not infer successful delivery merely because a logistics plan exists.

Actual physical state must reconcile from telemetry or explicit confirmed evidence.

---

# 19. Market / Trade Integration

Inventory may display current market value, estimated liquidation value, market location, order linkage, and at-market placement.

But Market / Trade owns prices, order state, fills, listing decisions, and liquidation/listing execution.

`Liquidatable` is a derived availability/intent view. It is not equivalent to `Free`.

An asset may be Free but strategically non-liquidatable.

---

# 20. Finance Integration

Inventory may show historical acquisition basis, accounting classification, and current enterprise asset value context.

But Finance owns those facts.

Physical movement between hangars or characters does not create a new acquisition basis.

Hangar purpose must never silently rewrite capital/expense classification, beneficial ownership, historical cost, or realized/unrealized treatment.

---

# 21. Hangar and Container Purpose

Nirauan's hangar-semantics idea becomes explicit Bastion configuration.

Every mapped hangar/container may have:

- one **Primary Purpose**
- zero or more optional descriptive/search tags

Primary Purpose drives deterministic workflow defaults.

Initial purpose examples:

- Export
- Industry
- Doctrine Stock
- Fuel
- Inputs
- Outputs
- Staging

These are configuration values, not guesses based on EVE names.

---

# 22. Purpose Inheritance

A container inherits its parent hangar's primary purpose by default.

A child container may explicitly refine or override that purpose.

Example:

Hangar purpose: **Industry**

Child containers:

- Reaction Inputs
- PI Inputs
- Finished Goods

The exact label may be custom, while deterministic behavior may still map to a controlled primary purpose where needed.

Optional tags help search and presentation but must not silently alter deterministic behavior.

---

# 23. Purpose Boundary

Hangar/container purpose may influence grouping, default filters, Doctrine readiness interpretation, Procurement gap logic, Industry input selection, Logistics destinations, dashboard attention, and replenishment policies.

It must not redefine ownership, accounting basis, historical cost, or financial classification.

---

# 24. Minimum Stock Policies

Bastion may support deliberately configured minimum-stock policies.

Example:

> Maintain 5,000 rounds of doctrine ammunition staged at Cervantes.

Such a policy may create a durable reserved/replenishment target.

This must be explicitly configured.

Doctrine existence alone does not create automatic minimum-stock reservations.

A configured policy may generate a Procurement proposal when actual free/staged stock falls below its threshold.

It must not silently create spend.

---

# 25. Inventory Browser

The canonical Inventory / Assets surface is a three-pane browser.

## Left Pane — Physical Location Tree

Shows physical hierarchy such as system, structure/station, corporation hangar, character hangar, ship, container, and specialized bay.

Configured primary purposes may be shown beside nodes.

The tree should support expansion/collapse, counts, stale/degraded cues, search match highlighting, selection persistence, and location totals where useful.

## Center Pane — Asset Table

Dense operational table.

Recommended columns include:

- Item / Type
- Quantity
- Free
- Allocated
- Placement
- Purpose
- Custodian
- Location
- Freshness

Columns adapt to selected scope and asset type.

## Right Pane — Asset Inspector

Persistent contextual inspector for the selected stack or unique item.

---

# 26. Enterprise Search and Filters

Inventory search should work across the enterprise.

Useful filters include:

- system
- structure/station
- custodian
- corporation vs character custody
- category/group/type
- free
- reserved
- committed
- unavailable
- unstaged
- staged
- in transit
- at market
- configured purpose
- Doctrine-linked
- Industry-linked
- Procurement-linked
- stale/degraded source
- assembled vs packaged
- unique ships

Filters must operate on deterministic inventory state, not prose labels.

---

# 27. Stack Inspector

For a fungible stack, show:

- type
- observed quantity
- free quantity
- reserved quantity
- committed quantity
- unavailable quantity/reason where applicable
- exact physical location
- configured purpose
- active allocations
- consuming workflows
- current market valuation context by reference
- Finance basis/classification context by reference
- freshness
- provenance
- history/audit evidence where useful

A user should be able to open the owning Doctrine, Industry job, Procurement requirement or Logistics load directly from an allocation.

---

# 28. Unique Ship Detail

Assembled/fitted ships require richer treatment.

Show:

- hull
- ship name
- unique item identity
- custodian
- enterprise ownership context
- exact physical location
- fitting
- rigs
- cargo/ammo
- specialized bay contents where useful
- Doctrine / variant association
- allocation state
- placement/staging state
- readiness
- current required actions
- Market / Trade valuation context
- Finance basis/classification references
- movement/audit evidence
- freshness/provenance

The ship-detail surface should feel like an operational asset record, not a generic item card.

---

# 29. Ship Fit Boundary

Inventory displays the current physical fit.

Doctrine owns canonical Doctrine fit semantics.

If the physical ship diverges from its assigned Doctrine variant, Inventory should expose the divergence and link to Doctrine/readiness.

It should not silently rewrite the Doctrine.

Likewise, changing a Doctrine does not mean a physical hull is magically refitted.

Physical state and desired canonical state remain separate.

---

# 30. Asset Readiness

For a selected unique asset, readiness may include:

- physically present
- correct hull
- correct rig identity
- correct installed fit
- required consumables present
- correct staging location
- not allocated elsewhere
- source fresh enough
- access available
- Doctrine association valid

Readiness failures should expose the first meaningful blocker.

---

# 31. Movement and Audit Evidence

Inventory may show movement/history where evidence exists.

Evidence quality states:

- **Directly Observed**
- **Derived**
- **User Confirmed**

Derived events must be labeled as derived.

---

# 32. Corporation Container Logs

Corporation container logs are useful supporting evidence.

They are not a perfect warehouse transaction ledger.

Bastion must not fabricate a precise actor/removal event that the source does not prove.

The Inventory UI may show directly logged events, inferred custody changes, unresolved movement, and current final physical state.

The final physical state may be authoritative even when the exact intermediate movement is not.

---

# 33. Freshness

Inventory decisions depend on telemetry freshness.

Every relevant asset scope should expose freshness.

Possible states:

- Current
- Aging
- Stale
- Authorization Missing
- Source Error
- Unknown

A stale observation must not be visually indistinguishable from a fresh one when it affects readiness or allocation.

Bastion must not silently substitute unrelated sources when required ESI data is unavailable.

---


# 33A. Canonical EVE Location Naming

Inventory location paths must use actual EVE containment and naming only.

Valid examples include:

- `Jita → Jita IV - Moon 4 - Caldari Navy Assembly Plant → Item Hangar → Container → Item`
- `Jita → Jita IV - Moon 4 - Caldari Navy Assembly Plant → Ship Hangar → Ship`
- `J154212 → <actual player structure> → Corporation Hangar Division → Container → Item`
- `Solar System / Space Location → Ship → Cargo Hold / Specialized Bay → Item`

Rules:

- Do not create a synthetic `Character Hangar` node.
- Use actual EVE locations such as `Item Hangar`, `Ship Hangar`, `Deliveries`, ship cargo and specialized bays where exposed.
- Do not carry Wormlife-era nicknames into Bastion location identity.
- Region/constellation may be used as filters or geographic browsing context, but are not physical containment parents in the Inventory tree.
- The browser tree, selected-item inspector and ship-detail location fields must all use the same normalized physical-location resolver.
- If an intermediate location cannot be resolved authoritatively, stop at the last authoritative node or show `Unknown/Unresolved`; never invent a plausible location.

---

# 34. Character Location Boundary

Character location tracking in Bastion uses **ESI per authorized character**.

Nexum does not own Bastion character-location state.

Nexum remains authoritative for live wormhole topology, mapped chain state, signatures/sites, and wormhole spatial context.

Inventory may use ESI-derived character location to understand custody/location of character-held assets where appropriate.

---

# 35. Attention Model

Stable inventory state does not belong in the Executive Brief attention feed merely because it exists.

Inventory should emit attention only for material intervention conditions, such as:

- important configured stock below threshold
- allocation conflict
- stale source blocking readiness
- staging requirement overdue
- unexpected disappearance/movement where material
- procurement requirement now satisfied/invalidated by inventory change

Normal holdings remain in Inventory.

---

# 36. History

Inventory history is contextual.

It should normally appear through selected asset inspector, movement drawer, allocation history, or cross-domain drilldown.

Do not create a separate top-level inventory-history module unless future use proves it necessary.

---

# 37. Validation / Conflict States

## Blocking

- negative derived free quantity
- one unique asset committed to two mutually exclusive executions
- missing physical asset referenced by an active hard commitment
- invalid/unknown required location preventing trustworthy readiness

## Review Required

- stale asset state affecting an active readiness decision
- inferred movement contradicting current allocation
- physical fit diverges from assigned Doctrine variant
- configured purpose conflicts with a workflow assumption

## Advisory

- asset could be staged more efficiently
- free stock is above/below a configured target
- duplicate stock exists at multiple locations

---

# 38. Deterministic Architecture

All normal Inventory behavior belongs in deterministic Bastion services.

This includes current asset normalization, location tree construction, free quantity calculation, allocation conflict detection, staging/readiness checks, purpose inheritance, stock-threshold evaluation, cross-domain linkage, and revision/history/diff where applicable.

The external assistant may use Bastion MCP to inspect, explain, propose and operate workflows.

Bastion must not require LLM inference to determine inventory truth.

---

# 39. Migration

Legacy Galaxy records such as acquisitions, inventory snapshots, fit records, movement notes and reconciliations are migration/provenance evidence.

They must normalize into stable Bastion objects such as:

- Asset / Unique Item
- Stack
- Location
- Inventory Node
- Allocation
- Purpose Mapping
- Stock Policy
- Movement / Evidence
- Cross-Domain Reference

Bastion callers must not reconstruct current inventory by traversing scattered historical Galaxy record kinds.

---

# 40. UX Guardrails

Do not:

- design Inventory as a raw ESI dump
- design it from legacy Galaxy record kinds
- merge Market / Trade into Inventory
- merge Finance accounting ownership into Inventory
- infer hangar purpose from its name
- treat character custody as accounting ownership
- equate owned with ready
- equate reserved with staged
- auto-reserve stock merely because a Doctrine exists
- double-count one physical stack against competing commitments
- collapse all unique assembled ships into quantity-only rows
- treat loose rigs as equivalent to the required rigged Doctrine hull
- fabricate a perfect movement audit when telemetry cannot prove it
- hide stale source state
- silently substitute Nexum for ESI character location

---

# 41. Visual Design Continuity

Inventory / Assets must inherit the established Bastion visual system used by the approved Accounts / Characters, Character Detail and Doctrine references.

Important continuity cues include:

- dark navy/black EVE-inspired base
- restrained blue/cyan Bastion edge/accent treatment
- persistent left navigation rail
- space-backed navigation treatment
- dense operational information hierarchy
- compact rectangular panels
- fine blue border/chrome treatment
- semantic state colors independent of branding
- EVE-native imagery/icons where appropriate
- strong selected-row/tree-node state
- compact tables rather than generic SaaS cards
- typography and spacing consistent with the existing Bastion reference pack

Do not reinterpret Inventory as a generic warehouse dashboard.

---

# 42. Canonical Visual References

The canonical Inventory / Assets handoff set uses these exact filenames:

- `inventory-assets-browser-reference-v1.png` — enterprise-wide Inventory / Assets browser with physical location tree, dense asset table, free/allocated state, purpose labels and selected stack inspector.
- `inventory-ship-detail-reference-v1.png` — unique assembled ship detail showing physical identity, location, fit/rig/cargo, Doctrine association, allocation, staging and readiness.

Only approved canonical renders should be supplied to the future UI/UX designer.

Exploratory, rejected, failed, superseded or composite generation images are non-authoritative and should not enter the designer ingest set.

---

# 43. Designer Handoff Priority

When implementation-ready UI/UX specifications are later produced, precedence is:

1. current structured Bastion design state;
2. this companion reference;
3. approved canonical images;
4. incidental sample values or labels visible in generated images.

The future designer may improve layout, density, progressive disclosure, interaction ergonomics, table behavior, selection behavior, and drawer/panel mechanics.

The designer must not silently change settled Bastion Inventory semantics.

Semantic conflicts should be flagged for review rather than resolved by invention.
