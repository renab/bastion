# Bastion — Doctrines Reference

Status: **Design semantics approved; canonical visual references assembled**

Current authoritative design key:

- `bastion-doctrine-domain-v1`
- current Galaxy leaf at time of this reference: `bf56403f-71e7-432d-909f-00e9227bdfc4`

Related current design records:

- `bastion-doctrine-tiering-v1`
- `nirauan-doctrine-management-domain-v1`
- `nirauan-site-fit-weather-capability-resolver-v1`
- `nirauan-fit-optimizer-v1`

This document defines the intended product semantics and interaction model for the Bastion **Doctrines** domain.

Written semantics and current structured design records outrank incidental labels, values, or omissions in generated reference images.

---

# 1. Product Role

Doctrines is a first-class Bastion domain for defining and managing operational capabilities.

A Doctrine is **not merely a fitting**.

It describes a governed operational capability consisting of:

- intended operating theater and activity;
- fleet or single-ship composition;
- role slots;
- hulls;
- fit variants;
- operational fit-state profiles;
- Doctrine Tier readiness requirements;
- pilot eligibility;
- content suitability;
- evidence and provenance;
- inventory/readiness state;
- gaps and follow-up proposals;
- revision history.

Canonical hierarchy:

**Doctrine  
→ composition role / slot  
→ hull  
→ fit / variant  
→ pilot eligibility / readiness  
→ capability approval / exclusion  
→ procurement gap**

Fits are subordinate implementation objects inside Doctrine. They are not a peer top-level Bastion domain.

Doctrines may represent:

- a single ship operated by one pilot;
- several permitted variants of one hull;
- several hulls serving different roles;
- a fixed fleet composition;
- a scalable multibox or harvesting fleet;
- specialized operational roles such as chain control.

---

# 2. Deterministic Architecture Boundary

Bastion itself is entirely deterministic.

No core Doctrine workflow may depend on LLM inference.

Architecture:

**Bastion UI  
→ deterministic Bastion Doctrine services**

**Bastion MCP  
→ the same deterministic Bastion Doctrine services**

**External assistant  
→ MCP  
→ Bastion deterministic Doctrine services**

The external assistant may:

- interpret natural-language intent;
- compare deterministic results;
- request calculations;
- suggest constraints;
- prepare a structured proposal;
- explain tradeoffs;
- propose edits through MCP.

It must not provide hidden logic required for Bastion to function.

Assistant-originated changes enter the normal Bastion flow:

**draft / proposal  
→ deterministic validation  
→ diff  
→ human review  
→ acceptance / rejection  
→ revisioned persistence**

There is no required embedded Doctrine assistant pane.

---

# 3. Doctrine Identity

A Doctrine has stable identity across revisions.

A Doctrine Revision contains the authoritative definition for a particular version of that Doctrine.

Changing material capability semantics creates a revision rather than silently rewriting history.

Examples of revisioned changes include:

- Doctrine Type changes;
- Tier requirement changes;
- fit or composition changes;
- role changes;
- changed suitability;
- changed module-state assumptions;
- changed fleet minimums;
- changed operating strategy;
- approval or exclusion changes.

The latest revision opens by default.

Historical revisions remain available through History and are read-only.

---

# 4. Doctrine Type

Every Doctrine Revision requires an explicit **Doctrine Type** before deterministic compatibility evaluation can run.

Doctrine Type is not inferred from:

- Doctrine name;
- hull;
- fit contents;
- description;
- previous usage;
- assistant interpretation.

Doctrine Type is a structured pair:

**Theater + Activity Family**

The pair selects the deterministic evaluator family and relevant compatibility dimensions.

Specific difficulty or content selections do **not** belong in Doctrine Type.

Examples that are compatibility context rather than Type:

- C1–C6 or C13;
- Level 1–5 mission level;
- exact combat site;
- exact anomaly;
- exact signature;
- weather / wormhole effect;
- NPC faction;
- strategy;
- operator model;
- fleet size or composition.

Do not create flat types such as:

- `C2 PvE`
- `C3 PvE`
- `Level 4 Mission`

Those are compatibility targets inside the appropriate Doctrine Type.

---

# 5. Theater Taxonomy

The initial controlled theater taxonomy is:

## Wormhole Space

Activity families:

- PvE Combat
- PvP / Response
- Exploration
- Gas Harvest
- Ore Harvest
- Chain Operations
- Haul / Logistics

## High Security Space

Activity families:

- Mission Running
- Combat Sites / Escalations
- Incursion PvE
- Exploration
- Mining / Harvest
- PvP / Response
- Haul / Logistics

## Low Security Space

Activity families:

- Mission Running
- Combat Sites / Escalations
- Faction Warfare
- Exploration
- Mining / Harvest
- PvP / Response
- Haul / Logistics

## Null Security Space

Activity families:

- Ratting / Anomalies
- Combat Sites / Escalations
- Exploration
- Mining / Harvest
- PvP / Response
- Fleet Warfare
- Haul / Logistics

Activity families need not be symmetrical across theaters.

The same broad human concept may require different deterministic evaluators in different theaters.

For example:

- wormhole PvE is not mission running;
- mission running is not nullsec ratting;
- nullsec Fleet Warfare is not interchangeable with a generic response fit;
- wormhole Chain Operations is not ordinary hauling.

Future special theaters such as Abyssal may be introduced when their deterministic evaluator semantics justify a distinct domain.

Do not provide a generic `General` or `Cross-Theater` escape hatch.

If one physical fitting legitimately serves multiple theaters or activities, separate Doctrine definitions may reference the reusable fit as appropriate.

---

# 6. Doctrine Library

The Doctrine Library is the primary browse/create/manage surface.

It should be dense, searchable, filterable and optimized for quickly answering:

- what capabilities exist;
- where they apply;
- which are operational now;
- which need attention;
- which have current readiness gaps.

Primary filtering dimensions should include:

- Theater;
- Activity Family;
- status;
- single-ship vs fleet composition;
- hull;
- current readiness state;
- suitability state;
- assigned/intended pilot;
- revision/currentness.

Each library row/card should emphasize Doctrine identity rather than the fit.

Useful summary content includes:

- Doctrine name;
- Theater + Activity Family;
- current revision;
- composition summary;
- current meaningful Tier range;
- overall readiness summary;
- suitability summary;
- important unresolved gap;
- recent evidence or validation status where useful.

A selected Doctrine may open a preview inspector without destroying Library filters, scroll position or selection context.

Primary action:

**Create Doctrine**

Doctrine creation must require an explicit Theater + Activity Family.

Compatibility evaluation remains unavailable until the Type is valid.

---

# 7. Doctrine Detail

Doctrine Detail is the canonical management surface.

Primary structure:

**Header  
+ Doctrine Tier rail  
+ main capability pane  
+ persistent contextual inspector**

Major sections:

- Overview
- Tiers & Fits
- Suitability
- Readiness
- Evidence

History is accessed through the shared compact History drawer pattern.

The header should show:

- Doctrine name;
- Theater;
- Activity Family;
- status;
- current revision;
- single-ship or fleet/composition nature;
- current high-level readiness;
- History entry point.

Doctrine Type must be visible but should not dominate the page after creation.

Changing Doctrine Type is a material revisioned operation and must warn that suitability may need review.

---

# 8. Doctrine Tier

Doctrine owns readiness **Tier I–V** where progressive readiness is meaningful.

Skill Plans do not own an independent parallel Tier I–V ladder.

A Doctrine does not have to invent five fake tiers merely because the common vocabulary supports I–V.

Only meaningful tiers need to be defined.

A Tier may define:

- tier identifier;
- intended role/capability;
- approved fit or fit-state profile;
- required hard skills;
- support/mastery depth;
- module capability assumptions;
- composition requirements;
- operational limitations;
- compatibility/suitability relationships;
- limiting mechanics;
- evidence/provenance.

Doctrine tiers should normally be cumulative in readiness intent where sensible.

Validation should flag internally contradictory tier definitions.

---

# 9. Tier Rail

Doctrine Detail uses a Tier I–V readiness rail where applicable.

Selecting a Tier drives the central capability view and persistent Tier inspector.

The interface must distinguish four concepts:

## Tier Definition

What this readiness tier means.

## Implementation

Which fit variant, state profile or fleet composition implements it.

## Training Target

The concrete deterministic Skill Plan target generated from the Tier.

## Suitability

Where that Tier + implementation is accepted for use.

These concepts must not visually collapse into one status.

---

# 10. Tier vs Fit

Tier and Fit are separate concepts.

Adjacent tiers may use the same physical fit.

Example:

Tier II and Tier III may use the same Vagabond fit while Tier III requires deeper support/mastery skills.

Conversely, a higher Tier may use a different fit variant if hardware changes are materially required.

The UI should explicitly communicate reuse.

Example label:

**Uses same physical variant as Tier II**

Do not make every Tier appear to be a separate ship fit when it is not.

Tier is the primary capability/readiness selection.

Fit/variant selection is subordinate to the selected Tier and Doctrine definition.

---

# 11. Skill Plan Relationship

Each Doctrine Tier deterministically resolves to a concrete Skill Plan training target.

That target may include:

- hard requirements;
- prerequisite closure;
- mastery/support category depths;
- milestone boundaries;
- explicit exclusions where defined.

Doctrine owns the readiness meaning.

Skill Plans owns the canonical training-definition / queue-construction workflow.

Doctrine Detail may show:

- target requirements;
- training-gap summary;
- completed vs missing requirements;
- major milestones;
- affected pilots;
- projected readiness.

But Doctrine must not duplicate the full Skill Plan builder.

A user can open the resolved target in Skill Plans.

Conceptually:

**Doctrine says what capability is required.**

**Skill Plans defines the deterministic training target and sequencing.**

**Character Detail projects that target against the real pilot and live EVE skill queue.**

---

# 12. Fits and Variants

Fits are subordinate versioned implementation objects.

A fit variant may define:

- hull;
- modules;
- rigs;
- ammo/charges;
- drones;
- cargo assumptions;
- permitted swap packages;
- module-state profile;
- pilot restrictions;
- operating assumptions.

Fits should be deterministically validated using current mechanics and intended pilot capability.

Validation includes where relevant:

- slots;
- CPU;
- powergrid;
- hardpoints;
- calibration;
- module prerequisites;
- incompatible combinations;
- current pilot skills.

Saved fittings alone are not evidence of operational performance.

---

# 13. Rig Boundary

A rig change normally means a distinct physical variant/hull.

Rig changes are not modeled as ordinary routine swaps.

A rig-changing optimization or weather-adapted proposal should be classified by default as:

**new hull / physical variant required**

A destructive refit may be presented as an explicit alternative, but must expose:

- destroyed rigs;
- replacement cost;
- downtime/refit burden;
- loss of the prior ready configuration.

It must never be treated as a free or invisible swap.

---

# 14. Operational Fit-State Profiles

Doctrine semantics may include valid operational module states.

A fitted module being offline does not automatically mean the fit is invalid.

Canonical example:

**Svipul C1/C13**

Operational profile:

- Expanded Probe Launcher offline during normal combat;
- launcher brought online for emergency scan/recovery use.

Bastion must understand this as an intentional valid Doctrine state.

A Fit Variant may therefore define named state profiles such as:

- Normal Combat
- Emergency Scan
- Travel
- Site Entry
- Specialized operating state

Validation evaluates the declared state profile rather than assuming every fitted module must be simultaneously online.

---

# 15. Fleet Composition

Fleet composition is first-class.

A fleet Doctrine is not merely a collection of independent ship fits.

A composition may define:

- role slots;
- required roles;
- optional roles;
- scalable roles;
- minimum count;
- target count;
- maximum count;
- eligible fits per role;
- eligible pilots;
- account/concurrency constraints;
- support assumptions.

A role slot resolves to an actual concurrently available pilot and valid ready fit.

The same character cannot satisfy two simultaneous required roles.

Account/login/subscription concurrency is a hard readiness constraint where applicable.

---

# 16. Harvest Fleet Example

Harvesting generally uses fleet Doctrine semantics rather than “count everyone capable of flying a Prospect.”

A Gas Harvest doctrine may contain:

- one or more Harvester slots;
- optional/required Booster/Support;
- optional Hauling/Compression support;
- minimum / target / maximum harvester counts;
- role-specific variants;
- fleet-level throughput assumptions.

Deterministic evaluation may calculate:

- aggregate harvest rate;
- residue/recovery profile;
- boosted vs unboosted output;
- fleet throughput;
- completion time;
- hauling/compression constraint;
- fieldable composition now.

A skilled pilot alone does not create fieldable harvesting capability.

The pilot must fit a valid role in a valid concurrently fieldable Doctrine composition.

---

# 17. Wormhole Chain Operations

Wormhole Chain Operations is a distinct activity family rather than a subtype of ordinary Haul / Logistics.

Its deterministic evaluator may need to model:

- wormhole mass limits;
- estimated remaining mass;
- ship mass;
- propulsion-state mass;
- rolling sequence;
- polarization constraints;
- required scanning support;
- recovery assumptions;
- minimum viable composition.

This activity family exists because its deterministic compatibility question is materially different from standard transportation.

---

# 18. Computed Compatibility

Doctrine Type determines which compatibility evaluator can run.

The evaluator determines **potential compatibility**, not approval.

For Wormhole PvE, compatibility dimensions may include:

- wormhole class;
- exact site;
- ordered waves;
- incoming/peak damage;
- site EHP;
- neut pressure;
- EWAR;
- target application;
- weather/effect;
- execution strategy;
- operator model;
- fleet composition;
- consumable assumptions.

For other Doctrine Types, the relevant deterministic dimensions differ.

Examples:

Mission Running:

- mission level;
- exact mission where modeled;
- NPC profile;
- incoming damage;
- application;
- strategy.

Gas Harvest:

- gas site/content;
- composition;
- throughput;
- site hazard;
- support;
- hauling.

Chain Operations:

- hole type/mass;
- current mass estimate;
- ship mass;
- propulsion state;
- rolling sequence.

The UI should only expose dimensions relevant to the selected Doctrine Type.

Do not build one giant universal suitability form containing irrelevant fields.

---

# 19. Compatibility Suggestions

The deterministic Doctrine engine may identify potential compatibility such as:

- supported;
- supported but low margin;
- review candidate;
- unsupported;
- unknown / insufficient data.

These are calculated resolver outputs.

They may suggest that an existing Doctrine appears potentially usable for additional content.

Example:

A Wormhole / PvE Combat Vagabond Doctrine may be evaluated against C1–C6 content and produce candidate compatibility for C2/C3 without encoding C2 or C3 into Doctrine Type.

The engine may surface these potential expansions for operator review.

It must never silently convert a calculated result into accepted Doctrine suitability.

---

# 20. Suitability

Readiness Tier and suitability-for-purpose are separate dimensions.

Accepted suitability states:

- **Approved**
- **Conditional**
- **Not Suitable**
- **Unknown / Unvalidated**

Suitability is user-governed Doctrine state.

A deterministic resolver may provide evidence for changing suitability, but it cannot make that approval decision silently.

A Tier V Doctrine is not automatically suitable for all content.

A Tier I Doctrine is not automatically unsuitable for all content.

Suitability is context/evidence specific.

---

# 21. Conditional Suitability

Conditional must contain an actual condition.

It must not function as a vague yellow state.

Examples:

- Approved only with a specific effect/weather;
- Tier IV+ required;
- booster role required;
- two-character operator model required;
- restricted strategy required;
- specific fit-state profile required.

The condition must be structured and reviewable where practical.

---

# 22. Suitability Matrix

Suitability uses a matrix-first interaction model.

Default presentation:

**content rows  
×  
Doctrine Tier / variant columns**

The matrix should show accepted suitability prominently.

Computed viability is supporting information and must remain visually distinct.

A cell may therefore express both:

**Computed:** Supported, low margin  
**Accepted:** Conditional

or:

**Computed:** Review candidate  
**Accepted:** Unknown / Unvalidated

Do not collapse these into one green/yellow/red result.

Accepted Suitability is the operationally governed state.

Selecting a matrix cell opens its contextual inspector.

---

# 23. Suitability Inspector

The selected-cell inspector may show:

- accepted suitability;
- exact context;
- deterministic computed result;
- limiting mechanic;
- margin;
- assumptions;
- fit/variant;
- Tier;
- operator model;
- fleet composition;
- effect/weather;
- evidence;
- confidence;
- provenance;
- freshness;
- approval history.

The matrix should remain compact.

High-dimensional context belongs in the inspector rather than creating a matrix with every possible class × site × effect × strategy × operator × fleet combination.

---

# 24. Readiness

Readiness is layered rather than boolean.

Important layers include:

## Training Readiness

Can the pilot satisfy the selected Doctrine Tier’s deterministic Skill Plan target?

## Fit / Inventory Readiness

Is the required ready physical hull/variant, equipment and consumable state actually available?

## Fleet Composition / Concurrency Readiness

Can the required simultaneous composition actually be fielded?

## Operator-Attention Readiness

Is there a known operational blocker requiring deliberate action?

## Content Suitability

Is this otherwise-ready capability accepted for the selected content/context?

The UI should expose the **first meaningful failing layer** and the next actionable gap.

Examples:

- training missing;
- hull missing;
- required role cannot be staffed concurrently;
- doctrine ready but content Not Suitable;
- all requirements satisfied.

---

# 25. Procurement Boundary

Doctrine readiness may identify an inventory or staging gap.

That gap does not automatically create a purchase order.

Doctrine may produce a structured **procurement proposal**.

Explicit operator action is required before that becomes an approved Procurement requirement.

Conceptually:

**Readiness gap  
→ proposal  
→ operator approval  
→ Procurement**

Doctrine does not silently commit spend.

---

# 26. Evidence

Doctrine evidence is first-class and must remain distinct from both computed viability and accepted suitability.

Evidence may include:

- field runs;
- successful clears;
- losses;
- aborts;
- stress cases;
- deterministic simulation;
- current SDE validation;
- current ESI pilot validation;
- site-mechanics corpus;
- inventory/readiness observations;
- operator notes.

Evidence should preserve:

- provenance;
- timestamp;
- context;
- relevant Doctrine revision;
- fit/variant;
- Tier;
- applicable site/content.

Historical evidence must not silently become current approval.

Field confidence is a separate concept from:

- computed viability;
- accepted suitability.

---

# 27. History and Revision Diff

Doctrine follows the shared Bastion history pattern.

Current revision is shown by default.

A compact **History** drawer lists prior revisions.

Selecting an older revision opens it read-only.

A deterministic diff should show meaningful changes such as:

- Doctrine Type;
- role/composition;
- hull;
- fit variant;
- rigs;
- operational state profiles;
- Tier requirements;
- Skill Plan target;
- suitability;
- evidence linkage;
- readiness assumptions.

History should not require the user to understand underlying Galaxy supersession mechanics.

---

# 28. Doctrine Validation

Doctrine validation uses the shared Bastion severity model:

- **Blocking**
- **Review Required**
- **Advisory**

Examples of Blocking:

- missing Doctrine Type;
- invalid fit;
- contradictory required composition;
- impossible Tier requirement;
- invalid mandatory role reference.

Examples of Review Required:

- Doctrine Type changed and suitability requires revalidation;
- deterministic evaluator result materially conflicts with accepted suitability;
- changed fit materially alters capability;
- rig change creates a new physical variant requirement;
- evidence/provenance is stale for a critical assertion.

Examples of Advisory:

- stronger support skills available;
- low-margin calculated performance;
- optional inventory staging improvement.

---

# 29. Fit Optimizer Integration

The deterministic Fit Optimizer may propose:

- greenfield candidates;
- Doctrine refinement;
- weather-adapted variants;
- minimal refits;
- separate physical variants where necessary.

Optimizer output is a proposal.

It does not become Doctrine merely because it scores well.

Acceptance requires normal review.

Optimizer results should expose:

- hard constraints;
- before/after metrics;
- changed modules;
- changed rigs;
- skill assumptions;
- acquisition cost;
- refit friction;
- inventory impact;
- compromises;
- relevant provenance.

There is no universal “best fit” score.

---

# 30. Doctrine Examples / Edge Cases

## Vega — Vagabond

Illustrates:

- Wormhole Space / PvE Combat;
- deterministic class/site compatibility;
- Tier vs Fit distinction;
- same fit potentially spanning adjacent Tiers;
- suitability potentially differing by site;
- C2/C3 being compatibility rather than Type.

## Svipul C1/C13

Illustrates:

- valid operational module-state profiles;
- offline Expanded Probe Launcher during combat;
- emergency-scan profile;
- fit-state semantics rather than false invalid-fit warnings.

## Squall PI Response

Illustrates:

- pilot-specific variants;
- same Doctrine capability with different valid implementation variants.

## CNI PI Rescue

Illustrates:

- common/lower-skill vs higher-skill pilot variants;
- preserving a practical shared multibox engagement envelope;
- pilot-specific capability without fragmenting the operational Doctrine unnecessarily.

## Prospect Gas Doctrine

Illustrates:

- fleet Doctrine semantics;
- scalable harvester slots;
- optional support/boost roles;
- fieldable fleet composition;
- aggregate throughput rather than independent pilot capability.

## Loki Doctrine

Illustrates:

- standardized future multi-hull / role-pack semantics;
- shared fleet Doctrine patterns.

---

# 31. Source-of-Truth Boundaries

During current Wormlife design work:

- Galaxy remains the authoritative structured ledger for current Doctrine decisions and provenance.
- SDE supplies static mechanics and fitting requirements.
- ESI supplies current pilot and asset state where authorized.
- Nexum supplies live wormhole/system/site/effect context.
- Obsidian supplies human-readable design narrative and documentation.

For the target Bastion architecture:

Once Doctrine is promoted into the structured Bastion domain, callers should consume the deterministic Doctrine domain model directly.

Bastion must not require runtime reconstruction of current Doctrine state from heterogeneous legacy Galaxy records.

---

# 32. Legacy Migration

Current `fit_doctrine`, `pvp_doctrine`, and other scattered Galaxy records are migration evidence.

They are not the target Bastion runtime schema.

Migration should normalize them into first-class objects such as:

- Doctrine;
- Doctrine Revision;
- Doctrine Type;
- Composition;
- Role / Slot;
- Fit Variant;
- Tier;
- Suitability;
- Readiness;
- Evidence;
- History.

Legacy type/purpose must be explicitly mapped to:

**Theater + Activity Family**

Ambiguous mappings require migration review.

Bastion must not dynamically infer Doctrine Type from scattered historical prose at runtime.

Legacy cross-kind supersession ambiguity should disappear from the target operational domain.

---

# 33. Doctrine Creation Flow

Recommended deterministic creation flow:

1. Create Doctrine.
2. Name Doctrine.
3. Select Theater.
4. Select Activity Family valid for that Theater.
5. Select single-ship or fleet/composition model.
6. Define roles/composition where applicable.
7. Attach or build fit/variant implementations.
8. Define meaningful Doctrine Tiers.
9. Resolve deterministic Skill Plan targets.
10. Run deterministic validation.
11. Run applicable compatibility evaluators.
12. Review proposed compatibility.
13. Explicitly establish accepted suitability.
14. Review readiness and gaps.
15. Publish Doctrine revision.

Nothing in this workflow requires assistant inference.

---

# 34. Doctrine Editing Flow

Editing a published Doctrine occurs through a new draft/revision.

The editor should make material changes visible before publication.

Example:

Changing:

**Wormhole Space / PvE Combat**

to:

**High Security Space / Mission Running**

is not a cosmetic classification edit.

It changes evaluator dispatch and therefore requires review of compatibility/suitability assumptions.

---

# 35. Cross-Domain Navigation

Doctrine should link contextually to:

- Skill Plans;
- Character Detail;
- Inventory;
- Procurement;
- Sites / Knowledge;
- Opportunities/analytics where relevant.

Examples:

Training gap  
→ open resolved Skill Plan target.

Pilot readiness  
→ open Character Detail.

Missing hull  
→ open Inventory / readiness context.

Approved procurement proposal  
→ open Procurement.

Suitability evidence  
→ open site/mechanics evidence where relevant.

Cross-domain navigation should preserve parent Doctrine context where practical.

---

# 36. UX Guardrails

Do not:

- treat Fit as a peer top-level Doctrine domain;
- infer Doctrine Type from the ship or fit;
- encode wormhole class into Doctrine Type;
- encode mission level into Doctrine Type;
- create a parallel Skill Plan Tier ladder;
- equate Tier with Suitability;
- equate computed viability with approval;
- use one universal green/red “capable” badge;
- silently create procurement;
- silently approve optimizer output;
- treat rig changes as routine module swaps;
- treat every fleet member independently when composition/concurrency matters;
- require the user to interpret Galaxy supersession chains;
- build core workflows around an embedded assistant;
- let generated mockup labels override this specification.

---

# 37. Visual Design Continuity

Doctrine surfaces should inherit the established Bastion visual system already used by the approved Accounts / Characters and Character Detail reference packs.

Important continuity cues include:

- dark navy/black EVE-inspired base;
- restrained electric blue/cyan Bastion accents;
- persistent left navigation rail;
- space-backed lower navigation treatment;
- dense operational data presentation;
- compact rectangular panels with fine blue borders;
- strong information hierarchy rather than generic dashboard cards;
- semantic success/warning/error colors kept distinct from corporation-brand accents;
- EVE-native identity imagery where appropriate;
- clear selected-row and selected-tab states;
- typography, spacing, panel density and action-button treatment consistent with the existing approved Bastion references.

The Doctrine references should not be reinterpreted as a generic dark SaaS dashboard.

---

# 38. Canonical Visual References

The approved Doctrine handoff set uses these exact filenames:

- `doctrines-library-reference-v1.png` — Doctrine Library overview, Theater/Activity filtering, readiness/status summary, and selected Doctrine inspector.
- `doctrine-detail-reference-v1.png` — Doctrine Detail showing Doctrine identity, Tier rail, Tier/fit distinction, Skill Plan relationship, readiness, and actions.
- `doctrine-suitability-reference-v1.png` — Suitability matrix showing accepted suitability separately from deterministic computed viability, with selected-context inspector.

Only these canonical renders should be supplied to the future UI/UX designer for this reference pack.

Exploratory, rejected, superseded, failed, or composite generation images are non-authoritative and must not enter the canonical ingest set.

---

# 39. Designer Handoff Priority

When implementation-ready UI/UX specifications are later produced, precedence is:

1. current structured Bastion/Galaxy design state;
2. this companion reference;
3. approved canonical images;
4. incidental text or sample values visible inside generated images.

The future designer may refine presentation, hierarchy, density, progressive disclosure and interaction ergonomics.

The designer must not silently change settled Doctrine product semantics.

Any semantic conflict or ambiguity should be flagged for review rather than resolved by inventing new behavior.
