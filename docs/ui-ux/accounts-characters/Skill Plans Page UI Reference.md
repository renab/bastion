# Bastion — Skill Plans Reference

## Status

Current product and UI/UX reference for Bastion Shared Skill Plans.

This document replaces earlier Skill Plan references that treated Skill Plans as owning an independent Tier I–V readiness ladder or depended on an embedded assistant/LLM.

The current model is:

- Bastion Skill Plans are fully deterministic;
- Doctrine owns Doctrine Tier I–V readiness;
- a selected Doctrine Tier deterministically resolves to a concrete Skill Plan training target;
- standalone Skill Plans may represent non-doctrine capabilities without inheriting an artificial Tier I–V model;
- Bastion MCP exposes the deterministic Skill Plan stack to an external assistant;
- inference occurs outside Bastion.

The semantic reference is ready to drive fresh visual references.

A new render is required for:

1. the normal Skill Plan Builder;
2. the Add Requirements From… / Requirement Proposal state.

---

# Purpose

Shared Skill Plans is Bastion's canonical training-definition and queue-construction domain.

It defines:

- concrete skill targets;
- skill target levels;
- prerequisite closure;
- hard requirements;
- support/mastery requirements;
- capability outcomes;
- milestones;
- deterministic reference ordering;
- source relationships;
- revision history;
- validation state;
- supported export artifacts.

Skill Plans define training intent.

They do not represent the authoritative live EVE queue.

Character-specific execution, projection, queue alignment and readiness belong in Character Detail.

---

# Core Domain Boundary

A Skill Plan answers:

> What training definition should exist for this capability?

Character Detail answers:

> How does this specific character's trained state and live queue relate to that definition?

Doctrine answers:

> What does operational readiness mean for this doctrine, fit and tier?

These responsibilities must remain separate.

---

# Doctrine Tier Ownership

Doctrine owns Doctrine Tier I–V readiness.

Skill Plan does not maintain a separate parallel Doctrine-style tier hierarchy.

A Doctrine Tier defines the readiness target.

Bastion deterministically resolves that Doctrine Tier into a concrete Skill Plan target.

The resolution path is conceptually:

`Doctrine Tier -> fit/capability semantics -> capability tags -> mastery/support mappings -> hard requirements + support requirements -> prerequisite closure -> concrete Skill Plan target`

For doctrine-derived training, Skill Plan should retain the exact source:

- Doctrine;
- Doctrine revision;
- Doctrine Tier;
- doctrine role/variant where relevant;
- approved fit/variant or fit-state profile where relevant.

Do not duplicate the readiness ladder inside Skill Plans.

---

# Doctrine Tier Progression

Doctrine tiers should normally represent cumulative readiness.

A higher Doctrine Tier should normally include or exceed the readiness requirements of lower tiers where that is semantically appropriate.

Bastion validation should identify contradictory definitions.

For a character eventually targeting a higher Doctrine Tier, Character Detail or queue-generation workflows may offer:

## Fastest to Target Tier

Treat the selected Doctrine Tier's complete cumulative requirement set as one optimization target.

## Progress Through Doctrine Tiers

Respect lower Doctrine Tier readiness boundaries in order.

For example, a character targeting Vagabond Tier III may progress through:

- Vagabond Tier I readiness;
- Vagabond Tier II readiness;
- Vagabond Tier III readiness.

Those readiness boundaries are derived from Doctrine.

They are not independent Skill Plan tiers.

---

# Standalone Skill Plans

Not every Skill Plan derives from a Doctrine.

Standalone plans may represent:

- PI capability;
- Industry capability;
- research;
- invention;
- reactions;
- scanning/exploration;
- logistics/support capability;
- general training;
- custom enterprise capability.

Standalone plans define their own explicit requirements and milestones.

They only use tiers or stages if their source capability explicitly defines such semantics.

Bastion does not force every Skill Plan into a universal Tier I–V ladder.

---

# Primary Surfaces

Skill Plans contains two primary UX states:

1. Plan Library
2. Plan Builder

The Plan Library is the browse/select/create surface.

The Plan Builder is the dominant deep-work surface.

Versions and revision history are secondary/contextual rather than permanently consuming the main authoring canvas.

---

# Plan Library

## Purpose

The Plan Library answers:

> What canonical training definitions currently exist, what are they for, what are they sourced from, and what state are they in?

It is a dense enterprise definition library rather than a character-comparison dashboard.

---

# Plan Library Layout

Prefer a dense searchable/filterable list or table with a contextual preview inspector.

Do not use oversized decorative cards as the primary representation.

A plan row may show:

- Plan name;
- capability/purpose;
- source capability;
- target Doctrine Tier where applicable;
- sequencing mode;
- current revision;
- validation state;
- lifecycle state;
- last updated time.

Example conceptual rows:

| Plan | Capability | Source | Mode | Revision | Validation | State |
| --- | --- | --- | --- | --- | --- | --- |
| C3 Vagabond | Combat | Vagabond Doctrine Tier III | Milestone Priority | v7 | Valid | Published |
| Outrider | Mining Command | Outrider Doctrine Tier II | Milestone Priority | v4 | Review | Published |
| PI Core | Planetary Industry | PI Capability | Breadth | v5 | Valid | Published |
| Research Core | Research / Invention | Standalone | Breadth | v3 Draft | Valid | Draft |

---

# Plan Library Preview

Selecting a plan populates the contextual preview.

The preview should answer:

## What is this?

- plan name;
- capability objective;
- short description;
- lifecycle state.

## What is it derived from?

- Doctrine/Tier where applicable;
- fit/variant where applicable;
- other linked capability/source objects.

## How is it organized?

- sequencing mode;
- requirement count;
- milestone count;
- hard/support requirement summary.

## Is it healthy?

- validation state;
- source freshness;
- mastery/template freshness;
- stale-linked-object warnings.

## What changed recently?

- current revision;
- latest change summary;
- publication state.

---

# Plan Library Actions

Primary actions:

- Create Plan;
- Build From…;
- Open Builder.

Secondary actions may include:

- Clone;
- Retire;
- View History;
- Export where supported.

---

# Build From…

Build From… is a first-class creation path.

Supported source classes may include:

- Doctrine Tier;
- doctrine role/variant;
- approved fit/variant;
- ship/hull;
- module;
- PI capability;
- Industry capability;
- research/invention capability;
- reaction capability;
- another supported Bastion capability object.

The source object is not merely descriptive metadata.

It participates in deterministic requirement resolution.

---

# Character Comparison Boundary

The shared Skill Plan library is not the primary character-comparison workspace.

Do not make character readiness, live queue state or per-character plan comparison the central library experience.

Character-specific application belongs in Character Detail.

The library may show lightweight usage context such as:

- assigned to 3 characters;
- referenced by 2 doctrines.

Those counts must remain secondary.

---

# Empty Library State

If no Skill Plans exist, show purposeful creation paths:

- Create Empty Plan;
- Build From Doctrine / Fit / Hull / Capability;
- Import supported Skill Plan artifact.

Do not show an unexplained empty table.

---

# Plan Builder

## Purpose

The Builder is the canonical authoring surface for one Skill Plan revision.

The builder must support direct manual authoring and deterministic source-based requirement generation without requiring an assistant.

---

# Builder Layout

Use a simultaneous three-pane workspace.

## Left — Skill Catalogue

Browse and add skills.

## Center — Plan / Reference Queue

Show the plan's requirements, generated reference ordering and inline milestones.

## Right — Context Inspector

Inspect/edit the selected:

- plan;
- skill requirement;
- milestone;
- source relationship.

Do not separate Queue Definition and Milestones into mutually exclusive primary tabs when they need to be visible together.

---

# Builder Header

The builder header should show compact high-value context:

- plan name;
- source capability;
- target Doctrine Tier where applicable;
- capability objective;
- lifecycle state;
- current revision;
- sequencing mode;
- validation state.

Primary controls may include:

- Save Draft;
- Validate;
- Publish;
- New Revision where appropriate;
- History;
- Add Requirements From….

Do not require an embedded Plan Assistant control.

---

# Skill Catalogue

The Skill Catalogue should use familiar EVE interaction grammar without copying unrelated EVE actions.

It should support:

- searchable skill list;
- skill category navigation;
- compact skill rows;
- level pips I–V;
- current plan target state;
- add/increment affordance;
- drag/drop;
- context menus.

The catalogue should be visible at the same time as the plan during authoring.

---

# Skill Catalogue Row

A skill row may show:

- skill name;
- level pips I–V;
- existing plan target level where present;
- compact prerequisite/support indicator where relevant;
- add/increment control.

Avoid overloading the row with every possible relationship.

Deep detail belongs in the right inspector.

---

# Adding Skills

The canonical requirement is:

**Skill + Target Level**

Adding a skill does not mean directly modifying an EVE live queue.

The plan stores the target requirement.

Bastion then derives prerequisites and reference ordering deterministically.

---

# Plus Button

The compact `+` control increments the plan target:

- absent -> I;
- I -> II;
- II -> III;
- III -> IV;
- IV -> V.

At V, the control is disabled or has no increment action.

---

# Level Pips

Clicking a level pip may directly set the target level.

Example:

Selecting IV on an absent skill creates:

`Skill -> Level IV`

Bastion then derives required prerequisite closure.

---

# Catalogue Context Menu

Appropriate actions include:

- Show Skill Details;
- Set Target Level I–V;
- Add / Increment Target;
- Add to Milestone…;
- Show Prerequisite Tree;
- Show Plan Uses / Milestones.

Do not copy unrelated EVE context-menu actions such as market, assets or live-training controls merely because EVE exposes them.

---

# Drag From Catalogue to Plan

Dragging a skill into the plan adds or changes its target requirement.

If the interaction does not unambiguously imply a target level, Bastion should ask for the level rather than guessing.

---

# Drag From Catalogue to Milestone

Dragging a skill onto a milestone associates that requirement with the milestone.

The plan-level skill requirement and milestone requirement relationship remain structured and inspectable.

---

# Requirement Classes

Skill Plan requirements should clearly distinguish their reason for existence.

Core classes include:

## Explicit Requirement

Directly authored or explicitly accepted into the plan.

## Hard Requirement

Mechanically necessary for the linked capability, hull, module, fit or role.

## Derived Prerequisite

Automatically required because another accepted requirement depends on it.

## Support / Mastery Requirement

Not required merely to access the hull/module/capability, but required by the selected support/mastery definition for effective operation.

One requirement may carry multiple provenance/reason relationships.

Do not reduce these semantics to one unexplained list of skills.

---

# Prerequisite Closure

Bastion deterministically derives prerequisite closure from authoritative EVE data.

If the plan requires a skill at a given level, Bastion adds the required prerequisite skill/levels.

A prerequisite needed by multiple requirements appears once.

Its inspector should explain all dependents.

---

# Removing Requirements

Removing an explicit requirement triggers prerequisite re-evaluation.

If a skill remains required by:

- another explicit target;
- another source capability;
- another milestone;
- a retained support/mastery requirement;

it remains in the plan.

Bastion explains why it is still required.

Derived prerequisites that become truly orphaned may be removed from the draft.

The resulting changes should remain visible in the plan diff.

---

# Plan Row Context Menu

Appropriate actions include:

- Change Target Level;
- Associate with Milestone…;
- Show Prerequisites;
- Show Dependents / Why Required;
- Insert Milestone After This Boundary;
- Remove Explicit Requirement.

Manual-ordering actions appear only when Manual / Explicit Order is active.

---

# Reference Queue

The center pane shows the plan as a readable reference queue.

It may expand canonical skill targets into individual level-training steps where useful for ordering.

For example:

A canonical requirement of:

`Medium Projectile Turret IV`

may appear in reference ordering as the needed individual level steps.

The displayed queue is a planning/reference structure.

It is not the character's live EVE skill queue.

---

# Explicit vs Derived Visibility

The plan should make it possible to distinguish:

- explicitly requested requirement;
- source-derived hard requirement;
- mastery/support requirement;
- prerequisite-derived requirement.

Do not rely on heavy full-row color coding.

Use compact badges/icons and inspector detail.

---

# Reference Duration

Where a character-neutral training-time calculation is meaningful, Bastion may display reference duration estimates.

Do not confuse those estimates with the completion time for a specific character.

Character-specific trained state, implants, attributes, current queue and projected completion belong in Character Detail.

---

# Sequencing Modes

Sequencing mode controls the Skill Plan's reference ordering.

It does not modify the live EVE queue.

Three supported modes are:

1. Breadth / Fast Unlocks
2. Milestone Priority
3. Manual / Explicit Order

---

# Breadth / Fast Unlocks

Purpose:

Favor broad early capability.

Within prerequisite constraints, prefer:

- shorter training steps;
- lower-level requirements;
- broad prerequisite coverage;
- early inexpensive capability gains.

Tradeoff:

Deep specialization or a specific high-level capability may take longer.

---

# Milestone Priority

Purpose:

Reach authored milestones as quickly as possible in their intended priority/order.

Prioritize requirements on the critical path to the next milestone.

Tradeoff:

Unrelated cheap improvements may be deferred.

---

# Manual / Explicit Order

The author controls reference ordering.

Manual ordering remains subject to deterministic prerequisite validation.

Drag reordering is enabled in this mode.

---

# Drag Reordering

Direct queue-row drag ordering is meaningful only in Manual / Explicit Order mode.

In automatic modes:

- do not silently convert to Manual;
- do not pretend the dropped location is authoritative.

If the user attempts manual reorder, explain that the current order is policy-generated and offer an explicit switch to Manual.

---

# Milestones

Milestones are first-class Bastion plan objects.

They are not EVE skill queue entries.

A milestone represents a meaningful capability/readiness outcome reached after a requirement boundary.

---

# Milestone Types

Examples include:

- skill unlock;
- module unlock;
- hull/ship unlock;
- doctrine eligibility;
- Doctrine Tier readiness;
- PI capability;
- Industry capability;
- research capability;
- invention capability;
- reaction capability;
- role/fleet support capability;
- custom enterprise outcome.

---

# Milestone Fields

A milestone may contain:

- stable identity;
- name;
- description;
- type;
- capability unlocked;
- rationale;
- linked Doctrine / hull / module / domain object;
- explicit/resolvable required skills and levels;
- completion boundary;
- source/provenance;
- authoring state.

---

# Inline Milestone Markers

Milestones appear inline in the reference queue as distinct non-skill marker rows/cards.

They visually punctuate the training plan with capability outcomes.

Do not represent milestones as if they were EVE skills.

---

# Milestone Insertion

The author may insert a milestone after a selected requirement boundary.

Supported affordances may include:

- inline `+ Milestone`;
- row context action.

Bastion validates whether the milestone's requirements are actually satisfied by that boundary.

---

# Milestone Placement

Milestone semantics are defined by their requirement set.

Their visual position is derived from where those requirements become satisfied in the current reference order.

Changing an automatic sequencing mode may therefore move a milestone marker without changing the milestone's semantic definition.

---

# Doctrine Readiness Markers

A Doctrine Tier readiness boundary may appear in a doctrine-derived plan.

That readiness outcome remains owned by Doctrine.

The Skill Plan displays it as a source-derived milestone/outcome.

Do not allow the Skill Plan to silently redefine what the Doctrine Tier means.

Changes to the underlying Doctrine Tier definition should surface as source drift requiring review.

---

# Milestone Inspector

Selecting a milestone populates the right inspector with:

- name;
- description;
- type;
- capability outcome;
- rationale;
- requirement set;
- completion boundary;
- linked source objects;
- Doctrine/Tier where applicable;
- provenance;
- validation state.

---

# Plan Inspector

When the overall plan is selected, the right inspector may show:

- plan name;
- description;
- capability objective;
- source capability;
- Doctrine/Tier where applicable;
- sequencing mode;
- Alpha/Omega constraints where relevant;
- linked objects;
- source/template freshness;
- lifecycle state.

---

# Skill Requirement Inspector

Selecting a skill requirement may show:

- target level;
- explicit / derived state;
- hard / support/mastery role;
- source capability;
- support/mastery category;
- prerequisite tree;
- dependents;
- why required;
- milestone associations;
- provenance.

This is the primary answer to:

> Why is this skill in this plan?

---

# Add Requirements From…

`Add Requirements From…` is a first-class deterministic workflow.

It allows the user to seed or extend a Skill Plan from a higher-level capability object.

Supported sources may include:

- Doctrine Tier;
- doctrine role/variant;
- fit;
- hull;
- module;
- PI capability;
- Industry capability;
- research/invention capability;
- reaction capability;
- other deterministic Bastion capability objects.

The workflow must not immediately mutate the plan.

It first opens a Requirement Proposal review surface.

---

# Requirement Proposal Drawer

Use a large review drawer over the Builder.

The drawer should explain exactly what Bastion resolved and why.

Primary sections:

1. Source Capability
2. Resolved Capability Tags
3. Hard Requirements
4. Derived Prerequisites
5. Support / Mastery Categories
6. Proposed Milestones
7. Diff Summary

---

# Source Capability

Show the exact source object.

For a Doctrine-derived source this may include:

- Doctrine name;
- Doctrine revision;
- Doctrine Tier;
- role/variant;
- approved fit revision.

Source identity must remain explicit and versioned.

---

# Capability Tags

Bastion uses deterministic capability tags to connect hulls/modules/fits/doctrines with support/mastery definitions.

Conceptual examples:

- `weapon.medium_projectile`;
- `weapon.medium_energy`;
- `tank.shield.active`;
- `tank.shield.buffer`;
- `tank.armor.active`;
- `propulsion.mwd`;
- `drone.light`;
- `command_burst.shield`;
- `harvest.gas`;
- `scan.probe`.

The exact taxonomy is a backend/domain-model concern, but the resulting profile must be inspectable.

A source should not produce unexplained skill recommendations.

---

# Capability Resolution

A source object may contribute capability tags from several deterministic layers.

Examples:

## Hull

May establish:

- hull class;
- racial spaceship operation;
- broad base capability.

## Module

May contribute:

- weapon family;
- tank type;
- propulsion;
- EWAR;
- scanning;
- command burst;
- harvesting capability.

## Fit

Combines the fitted modules and approved operational module-state profile.

## Doctrine

Adds intended operational role, Doctrine Tier and doctrine-specific inclusion/exclusion policy.

Doctrine may therefore narrow or override generic hull-level support categories.

---

# Fit-Aware Resolution

For doctrine/fit seeding, support requirements must be based on the approved fit/variant and its actual operational semantics.

Do not rely only on generic hull mastery.

Examples:

A shield-fit Vagabond should not import armor support merely because a generic hull competency model contains armor skills.

A fit using drones should resolve the relevant drone support categories.

A fit with an Expanded Probe Launcher intentionally offline during normal combat must respect the approved module-state semantics rather than pretending every fitted module is continuously active.

---

# Hard Requirements

Hard Requirements are mechanically necessary.

Examples include skills required to:

- fly the hull;
- online/use required modules;
- operate required capabilities;
- satisfy mechanical prerequisites.

Hard Requirements must be visually distinct from support/mastery recommendations.

---

# Derived Prerequisites

Bastion automatically computes prerequisite closure for the proposed hard and support requirements.

The proposal should show which requirements are:

- newly added;
- already present;
- being raised;
- shared with existing plan requirements.

---

# Support / Mastery Categories

Support/mastery categories are deterministic competency templates inspired conceptually by EVE's Mastery system.

They represent transitive skills that materially improve effective operation beyond minimum eligibility.

Possible categories include:

- core spaceship operation;
- fitting;
- shield tank;
- armor tank;
- active tank;
- buffer tank;
- capacitor/engineering;
- navigation;
- targeting/sensors;
- weapon operation;
- weapon application;
- drones;
- command bursts;
- mining/resource harvesting;
- scanning/exploration;
- PI;
- Industry;
- research;
- invention;
- reactions;
- other capability-specific groups.

---

# Support / Mastery Depth

Mastery/support templates may define Tier I–V depth within a category.

Those category-depth tiers are deterministic resolver data.

They are not an independent top-level Skill Plan readiness ladder.

For a doctrine-derived plan, the selected Doctrine Tier determines which support/mastery category depths apply.

Example conceptually:

Vagabond Doctrine Tier III may require:

- Core Spaceship Operation: support depth III;
- Active Shield Tank: support depth III;
- Medium Projectile: support depth III;
- Navigation: support depth III;
- Light Drones: support depth II.

These are resolver inputs behind the Doctrine Tier.

The Skill Plan receives the resulting concrete skills and target levels.

---

# Considered but Excluded Categories

Where useful for explainability, Requirement Proposal should show relevant categories that Bastion considered but did not include.

Example:

**Armor Tanking — Excluded**

Reason:

Linked approved doctrine uses active shield tank and defines no armor-support requirement.

This allows the deterministic resolver to be inspected rather than appearing magical.

---

# Requirement Proposal Diff

Every proposed change should be compared with the current draft.

Useful states include:

- Add;
- Raise Target;
- Already Covered;
- Derived;
- Remove.

A requirement should explain both:

- what is changing;
- why it is changing.

---

# Requirement Proposal Actions

Primary actions:

- Accept Proposal;
- Hard Requirements Only;
- Cancel.

`Hard Requirements Only` intentionally creates or extends the plan using the mechanically required subset without accepting optional support/mastery recommendations.

This action must remain explicit.

---

# Mutation Boundary

No Requirement Proposal modifies the current plan until accepted.

On acceptance:

- structured requirements enter the draft;
- prerequisite closure is updated;
- milestones are updated where applicable;
- source/provenance links are retained;
- validation reruns.

---

# Mastery / Support Template Versioning

Mastery/support category templates are versioned deterministic data.

A template update must not silently mutate an already published Skill Plan.

If a template changes, affected plans may show:

**Template Update Available**

or:

**Needs Review**

The user can inspect:

- old template revision;
- new template revision;
- skill target diff;
- affected milestones;
- Doctrine readiness impact.

Only explicit acceptance updates the plan draft.

---

# Source Version Drift

Linked source objects are versioned where applicable.

Examples include:

- Doctrine revision;
- fit revision;
- mastery/support template revision;
- capability-definition revision.

If a source changes after plan publication, Bastion does not silently rewrite the plan.

Instead, validation exposes the drift and its effect.

---

# Validation

Skill Plan validation is deterministic.

It does not require LLM inference.

Use three severity levels:

1. Blocking
2. Review Required
3. Advisory

---

# Blocking Validation

Blocking issues prevent publication.

Examples include:

- missing prerequisite;
- invalid target level;
- impossible Manual ordering;
- milestone boundary that does not satisfy milestone requirements;
- unresolved hard requirement;
- unsupported mechanical claim;
- broken source relationship required by the plan.

---

# Review Required

Review Required issues permit publication only after deliberate acknowledgement.

Examples include:

- linked Doctrine has a newer revision;
- linked fit has changed;
- mastery/support template revision changed;
- support requirement was deliberately removed;
- source update changes Doctrine readiness;
- milestone moved materially;
- previously accepted capability relationship became stale.

Acknowledgement should be retained with the revision.

---

# Advisory Validation

Advisories are informational or optimization-oriented.

They never block publication.

Examples include:

- redundant explicit requirement;
- requirement already covered transitively;
- several milestones sharing the same prerequisite;
- a different automatic sequencing mode reaches a milestone sooner;
- target skill exceeds the needs of all currently linked source capabilities.

---

# Validation Presentation

Normal Builder use should remain visually quiet.

Header examples:

**Valid**

or:

**Validation · 2 Blocking · 3 Review**

Affected queue rows and milestones may carry compact inline markers.

Selecting validation opens a `Validation & Impact` drawer.

---

# Validation & Impact Drawer

Each diagnostic should show:

- issue;
- severity;
- why it matters;
- affected object;
- source/provenance;
- source/Doctrine/readiness impact where relevant;
- Jump to;
- deterministic Fix where one is safe.

Examples:

**Source Revision Changed**

C3 Vagabond Doctrine v8 supersedes linked v7.

Two resolved support requirements changed.

Actions:

- Review Source Diff;
- Jump to Source.

**Doctrine Readiness Impact**

Removing a required support skill means the concrete plan no longer satisfies the linked Vagabond Tier III definition.

Actions:

- Restore Requirement;
- Review Doctrine.

---

# Deterministic Fixes

Bastion may offer deterministic repair actions when no policy judgment is required.

Examples:

- Add Missing Prerequisite;
- Regenerate Automatic Ordering;
- Remove Orphaned Derived Requirement;
- Restore Required Target;
- Update Derived Requirements From Source after explicit review.

Do not automatically make subjective policy decisions.

---

# Publish Rules

Blocking issues prevent publication.

Review Required issues require explicit acknowledgement.

Advisories do not block publication.

Published revisions retain:

- validation state;
- acknowledged Review items;
- source revisions;
- template revisions;
- provenance.

---

# Revisions

Skill Plans are versioned first-class objects.

Editing a published plan creates a draft revision.

Publishing creates a new immutable historical revision/version.

Do not silently rewrite existing published history.

---

# Current Revision

Open the latest/current revision by default.

The Builder header should include a compact:

**History**

or:

**Versions**

control.

Do not permanently dedicate a large region of the main Builder to revision history.

---

# History Drawer

History opens in a drawer.

Show:

- revision/version;
- date;
- state;
- short change summary.

Selecting an older published revision shows it read-only.

---

# Revision Diff

Default comparison:

**Selected historical revision vs Current**

The diff may cover:

- skills added;
- skills removed;
- target levels changed;
- prerequisite closure changed;
- milestones added/removed/moved;
- milestone metadata changed;
- sequencing mode changed;
- reference order changed;
- linked source changed;
- capability/rationale changed;
- mastery/support template revision changed.

---

# Revising Historical Versions

Do not edit an old published version in place.

If the user wants to resume from an older state:

**Create Draft From This Version**

This produces a new draft while preserving the original revision.

---

# Lifecycle States

Useful lifecycle states may include:

- Draft;
- Published;
- Needs Review;
- Retired.

Source/template drift may move a published plan into a review-needed state without destroying the last published definition.

---

# Export

Where technically supported, Bastion may generate an EVE-importable Skill Plan artifact.

Only EVE-supported skill-plan content is exported.

Bastion-specific metadata remains in Bastion, including:

- milestone descriptions;
- rationale;
- source relationships;
- Doctrine relationships;
- provenance;
- validation;
- internal capability semantics.

---

# Relationship to Character Detail

Character Detail consumes a specific Skill Plan revision.

Character Detail is responsible for:

- trained-skill comparison;
- authoritative live-queue regression;
- character-specific plan alignment;
- projected milestone dates;
- Doctrine Tier readiness projection;
- missing-from-queue requirements;
- character-specific What-If scenarios;
- missing skillbooks;
- character-specific sourcing;
- capability unlock timing.

The Skill Plan library itself remains character-neutral.

---

# Projection Contract

Skill Plans must be machine-readable enough for Character Detail to evaluate them against arbitrary real live-queue ordering.

Every milestone must retain:

- stable identity;
- explicit/resolvable requirements;
- source revision;
- capability outcome.

Reference ordering must not be required to determine whether a milestone is satisfied.

---

# Shared Requirements

One skill may satisfy requirements for:

- several milestones;
- several Skill Plans;
- several Doctrine-derived targets.

The data model must support reuse rather than requiring duplicated skill objects.

Character Detail resolves that overlap during projection.

---

# Procurement Boundary

Creating, inspecting or publishing a Skill Plan does not automatically create procurement.

Missing skillbooks may be identified as requirements.

A procurement/sourcing object is created only after an explicit training investment or sourcing decision.

---

# Deterministic Product Boundary

The entirety of the Skill Plans product must function deterministically.

Bastion performs no required in-product LLM inference.

Deterministic Bastion services own:

- authoritative skill lookup;
- prerequisite resolution;
- source-object requirement resolution;
- capability-tag resolution;
- mastery/support category mapping;
- category depth resolution;
- Doctrine Tier -> concrete training target resolution;
- requirement deduplication;
- reference sequencing;
- milestone requirement evaluation;
- milestone placement;
- validation;
- source/template drift detection;
- revision/version diff;
- export;
- Character Detail projection contracts.

No core Skill Plan operation depends on an assistant being available.

---

# MCP Boundary

Bastion MCP exposes the same deterministic Skill Plan/domain services used by the human UI.

An external assistant may use MCP to:

- inspect plans;
- inspect Doctrine and source relationships;
- request deterministic requirement resolution;
- request prerequisite closure;
- request source diffs;
- invoke validation;
- inspect sequencing outputs;
- create/edit drafts using structured operations;
- submit authored milestone descriptions/rationale;
- propose changes;
- explain deterministic results conversationally.

Inference occurs in the external assistant.

It does not occur inside Bastion.

---

# Assistant-Originated Changes

An external assistant may interpret a conversational request such as:

> Build training for this character to become Vagabond Tier III ready.

The assistant then invokes deterministic Bastion MCP operations.

Bastion performs the actual:

- Doctrine Tier lookup;
- requirement resolution;
- mastery/support mapping;
- prerequisite closure;
- validation;
- diff generation.

Any assistant-authored wording or proposed policy choice retains assistant provenance.

Assistant-originated edits enter through the same normal:

- Draft;
- Diff;
- Review;
- Publish

workflow as human edits.

---

# No Embedded Assistant Dependency

Do not design Skill Plans around a permanently embedded Plan Assistant panel.

The product must remain complete without one.

If external-assistant/MCP activity creates a draft or proposal, the Builder may indicate its provenance.

That is ordinary structured product state, not an in-product inference system.

---

# EVE Interaction Reference

EVE's Skill Catalogue and Personal Skill Plan UI are useful familiarity references.

Borrow:

- separate plan-library and builder concepts;
- catalogue visible beside plan;
- skill category browsing;
- search;
- level pips;
- compact `+`;
- drag/drop;
- context menus;
- inline relationship between plan and milestones.

Do not blindly copy:

- EVE's exact styling;
- Certified / Personal / Corporation taxonomy unless Bastion needs it independently;
- character completion UI on canonical enterprise definitions;
- EVE's exact radial milestone wheel;
- apparent fixed milestone limits;
- market/assets actions unrelated to Skill Plan authoring;
- controls implying Bastion can directly edit the live EVE queue.

---

# Visual Direction

Use Bastion's established visual language:

- dense desktop-first information design;
- dark black-glass surfaces;
- subdued nebula background;
- thin precision borders;
- corporation-derived stylistic palette;
- semantic colors reserved for real semantic state;
- compact EVE-familiar training grammar;
- minimal decorative card-wall treatment.

The Builder should visually prioritize the center plan/reference queue.

---

# Builder Visual Hierarchy

Recommended hierarchy:

## Header

Plan identity, source capability, Doctrine Tier where applicable, revision, sequencing and validation.

## Left

Skill Catalogue.

## Center

Plan/reference queue with skill-level steps and inline milestones.

## Right

Context inspector for selected plan/skill/milestone/source.

The full Builder should remain usable within a desktop viewport without unnecessary page-level scrolling where practical.

Pane-internal scrolling is appropriate for long catalogues and queues.

---

# Requirement Proposal Visual Hierarchy

The Add Requirements From… visual reference should demonstrate:

- exact source Doctrine/fit/capability;
- source revision;
- resolved capability tags;
- hard requirements;
- derived prerequisites;
- support/mastery categories;
- included and excluded categories;
- concrete skill changes;
- proposed milestones;
- diff states;
- clear Accept / Hard Requirements Only / Cancel boundary.

The render must make it obvious that Bastion is deterministically resolving a capability into training requirements rather than merely dumping a generic skill list.

---

# Edge States

## Empty Plan

Show useful creation options:

- add individual skills;
- Add Requirements From…;
- add milestone;
- choose source capability.

## Broken Source Relationship

Show exact source failure and affected requirements.

Do not silently detach or guess.

## Source Revision Available

Show review-needed state and diff path.

## Mastery Template Update Available

Show old/new template revisions and impact.

Do not silently mutate the plan.

## Invalid Manual Ordering

Show blocking validation and exact prerequisite conflict.

## Missing Authoritative Mechanics

Do not invent a requirement.

Show unresolved state and block any claim that depends on it.

## No Assistant Connected

No special degradation state is required.

Skill Plans continues to function normally.

---

# Must Not

Do not:

- make character comparison the central shared Skill Plan workflow;
- confuse plan reference ordering with the authoritative live queue;
- represent milestones as EVE skills;
- create a second Doctrine-style Tier I–V hierarchy inside Skill Plans;
- hide requirement provenance;
- collapse hard and support requirements into one unexplained list;
- silently mutate published plans when Doctrine, fit or mastery templates change;
- silently publish assistant-authored changes;
- require LLM inference for any normal Skill Plan workflow;
- silently create Procurement from plan authoring;
- imply direct EVE live-queue write access;
- assume generic hull mastery is sufficient when an approved fit/doctrine provides more specific semantics.

---

# Visual Reference Status

The previous Skill Plans visual reference is superseded because it may encode outdated tier ownership and assistant semantics.

Fresh renders are required.

## Required Render 1 — Normal Builder

Use a populated doctrine-derived example, such as:

**C3 Vagabond — Target: Doctrine Tier III**

The render should demonstrate:

- Skill Catalogue;
- source Doctrine/Tier;
- hard and support requirements;
- derived prerequisites;
- generated reference order;
- inline functional/readiness milestones;
- sequencing mode;
- revision state;
- validation;
- selected requirement or milestone inspector.

Do not show Skill Plan as owning Tier I–V.

Do not show an embedded Plan Assistant.

## Required Render 2 — Add Requirements From…

Show the deterministic requirement-proposal workflow for a doctrine/fit/hull capability.

The render should demonstrate:

- exact source object/revision;
- resolved capability profile;
- capability tags;
- hard requirements;
- support/mastery categories;
- considered exclusions where useful;
- proposed changes;
- provenance;
- diff;
- Accept Proposal;
- Hard Requirements Only;
- Cancel.

These two renders, together with this document, become the current Skill Plans visual/product reference for the later dedicated UI/UX implementation-spec pass.


## Canonical Visual References

The following images are the approved visual references for this surface:

- `skill-plans-builder-reference-v1.png`
  - Normal populated Skill Plan Builder state.
  - Shows Skill Catalogue, deterministic plan/reference queue, inline milestones, source Doctrine/Tier context, revision/validation controls, and selected-item inspector.

- `skill-plans-add-requirements-reference-v1.png`
  - Add Requirements From… / Requirement Proposal state.
  - Shows deterministic source resolution, capability tags, hard requirements, support/mastery categories, exclusions, proposed milestones, diff summary, and acceptance boundary.

These images communicate approved layout, hierarchy, density, and interaction-state direction.

The companion Markdown and current structured Bastion design decisions remain authoritative for semantics. Generated sample names, values, counts, labels, or incidental controls in the images must not override the written specification.