# Bastion — Character Detail Reference

## Status

Current product and UI/UX reference for the Bastion Character Detail surface.

The approved primary Character Detail / Training visual direction remains valid.

This document supersedes earlier Character Detail reference language where it conflicts with current Skill Plan, Doctrine Tier, deterministic-core, MCP, or canonical visual-reference semantics.

---

# Purpose

Character Detail is the canonical deep-work surface for one character.

It combines:

- identity and account context;
- authorization health;
- authoritative live training state;
- Skill Plan projection;
- capability/readiness;
- Doctrine eligibility and readiness;
- Industry / PI capability;
- character-specific operational history.

Character Detail presents character-specific state.

It should not duplicate the full management surfaces of:

- Doctrines;
- Skill Plans;
- PI;
- Industry;
- Inventory;
- Procurement;
- Finance.

Instead, it presents character-specific consequences and links into the owning domain.

---

# Primary Sections

Character Detail contains five primary sections:

1. Overview
2. Training
3. Capabilities
4. Industry & PI
5. Activity

Assigned Skill Plans are surfaced primarily in Overview and Training rather than becoming another duplicate top-level character section.

---

# Character Header

The compact character header contains:

- official EVE portrait;
- full canonical character name;
- parent account;
- optional parent account alias;
- subscription state where useful;
- total skill points;
- ESI authorization health;
- current or recent location with freshness;
- current or recent ship with freshness;
- current training item;
- focused or important assigned Skill Plan context;
- next meaningful projected capability/readiness milestone.

The header should remain operationally dense.

Avoid turning it into a large decorative profile card.

---

# Overview

Overview summarizes the character's current operational state.

It may include:

- ESI health;
- current training snapshot;
- assigned Skill Plans;
- next projected milestone;
- current capability highlights;
- Doctrine readiness highlights;
- important blockers;
- current/recent ship and location;
- useful cross-domain links.

Detailed training work belongs in Training.

---

# Training

## Core Principle

The live EVE skill queue is authoritative execution state.

Skill Plans are intent and training-definition overlays.

Bastion never treats a Skill Plan reference order as if it were the live EVE queue.

The primary training representation is an EVE-familiar vertical skill queue.

---

# Live Queue Rows

Each queue row may contain:

- skill name;
- target level;
- compact level/progression pips or equivalent cue;
- current-training emphasis;
- duration;
- time remaining;
- contributing Skill Plan markers;
- contributing milestone markers.

Avoid heavy row coloring.

Use compact explicit icons/tags for:

- plan contribution;
- divergence;
- missing requirement;
- shared requirement;
- milestone relationship.

---

# Queue Summary

The Training surface may summarize:

- queued skill count;
- total queued training time;
- queued skill points where useful;
- queue freshness;
- empty or imminently empty queue warning.

Missing or stale queue data must degrade explicitly.

---

# Character With No Assigned Plan

A character with no actively assigned/tracked Skill Plan still receives the complete authoritative live queue.

Do not fabricate a milestone layer.

The absence of a Bastion plan must not reduce the usefulness of normal character training visibility.

---

# Multiple Assigned Skill Plans

A character may have multiple active assigned Skill Plans.

Bastion evaluates every active assigned plan against:

- trained skills;
- the authoritative ordered live queue;
- relevant Doctrine/source definitions.

One plan may be visually focused.

All active plans still contribute to:

- requirement coverage;
- milestone projection;
- overlap analysis;
- divergence analysis;
- readiness evaluation.

---

# Shared Skill Contribution

If one trained or queued skill contributes to multiple plans or milestones, display that overlap on the single skill row.

Do not duplicate the skill entry.

The inspector may expose all plans/milestones that depend on the selected skill.

---

# Doctrine-Derived Skill Plans

Doctrine owns Doctrine Tier readiness.

Skill Plan supplies the concrete training target required to reach that readiness state.

When an assigned Skill Plan derives from a Doctrine Tier, Character Detail must retain and display the exact source identity:

- Doctrine;
- Doctrine revision;
- doctrine role/variant where relevant;
- fit/variant where relevant;
- target Doctrine Tier.

Readiness terminology should therefore look like:

- Vagabond Tier II Ready;
- Target: Vagabond Tier III;
- Vagabond Tier III blocked by support requirement;
- Outrider Tier II projected in 4d 9h.

Do not present this as a Skill Plan-owned tier.

---

# Standalone Skill Plans

Not every Skill Plan derives from a Doctrine.

Standalone plans may represent:

- PI;
- Industry;
- research;
- invention;
- reactions;
- scanning;
- general support training;
- other enterprise capability.

These plans continue to project their own explicit milestones and capability outcomes without requiring Doctrine Tier semantics.

---

# Live Queue Regression

For every active assigned Skill Plan, Bastion deterministically reconciles the plan against:

- currently trained skills;
- the authoritative live queue;
- exact skill target levels;
- prerequisite relationships;
- source capability requirements;
- exact plan revision.

Each requirement is classified where relevant as:

- already trained;
- present in live queue;
- required but absent from live queue;
- queued beyond a milestone-critical point;
- satisfied as a shared requirement used by multiple plans/milestones.

---

# Milestone Projection

Bastion determines where each milestone becomes satisfied under the actual live queue ordering.

The projection does not assume the Skill Plan's reference ordering is being followed.

Projected output may include:

- completion queue position;
- projected completion timestamp;
- completion state if already satisfied;
- contributing required skills;
- missing requirements;
- shared requirements;
- delta versus reference sequencing where useful.

---

# Projected Milestone Markers

Character Detail may inject projected milestone markers into the displayed live queue at the point where the milestone becomes satisfied.

A marker may contain:

- originating Skill Plan;
- exact Skill Plan revision;
- Doctrine and target Doctrine Tier where applicable;
- milestone name;
- concise description;
- projected completion date;
- capability/readiness outcome;
- state.

Possible states include:

- Satisfied;
- Projected;
- Blocked;
- Unprojectable;
- Degraded / Stale.

---

# Doctrine Tier Projection

When the milestone represents a Doctrine Tier readiness boundary, the marker is a derived Doctrine-readiness outcome.

The concrete requirements still come from the resolved Skill Plan.

For example:

**Vagabond Tier III Ready**

may be injected at the queue position where all concrete requirements for the linked Vagabond Doctrine Tier III are satisfied.

The marker should retain:

- Doctrine identity;
- Doctrine revision;
- target tier;
- Skill Plan revision used for the requirement projection.

---

# Selected Milestone Inspector

Selecting a projected milestone opens a persistent detail pane.

The detail pane may show:

- milestone name;
- originating Skill Plan;
- plan revision;
- Doctrine/Tier where applicable;
- capability/readiness unlocked;
- required skills;
- already-trained requirements;
- contributing live-queue skills;
- projected completion;
- missing blockers;
- missing skillbooks;
- source/provenance;
- delta from reference sequencing;
- linked Doctrine/Capability object.

The inspector should explain why the milestone occurs where it does.

---

# Queue Divergence

A live queue may differ substantially from a Skill Plan reference order.

Bastion explains that divergence rather than treating either side as inherently wrong.

Possible divergence states include:

- milestone earlier than reference;
- milestone later than reference;
- required skill absent from live queue;
- unrelated queued training delaying capability;
- later plan requirement trained early;
- shared queued skill serving several plans.

The reference plan is planning intent.

The live EVE queue is execution truth.

---

# Missing Requirements

If a milestone cannot complete because one or more required skills are absent from the live queue:

- mark it Blocked or Unprojectable;
- identify the exact missing requirements;
- do not fabricate a completion timestamp;
- show the last currently satisfiable state where useful.

Missing skillbooks are requirements/blockers rather than fake queue entries.

---

# Readiness Model

Character Detail distinguishes several different readiness dimensions.

A character may:

- lack hard required skills;
- satisfy hard skills but fall below desired support depth;
- satisfy the training requirements for a Doctrine Tier;
- lack the physical fit;
- have the fit but lack required consumables;
- have the fit but be unsuitable for selected content;
- be both ready and suitable.

Do not collapse all of these states into one generic Ready flag.

---

# Doctrine Tier Readiness

For doctrine-derived plans, Character Detail may expose:

- highest currently satisfied Doctrine Tier;
- assigned/target Doctrine Tier;
- next missing readiness boundary;
- concrete missing training;
- physical fit readiness;
- content suitability.

A character satisfying Vagabond Tier III training does not imply that every C3 site is suitable.

Doctrine Tier and content suitability remain separate dimensions.

---

# Doctrine Suitability

Suitability comes from the Doctrine domain.

Possible states may include:

- Approved;
- Conditional;
- Not Suitable;
- Unknown / Unvalidated.

Character Detail may surface the result contextually but should link to the Doctrine domain for the complete suitability model and evidence.

---

# Capabilities

The Capabilities section shows explicit current capability/readiness by role or domain.

Examples may include:

- Doctrine eligibility;
- Doctrine Tier readiness;
- ships/hulls;
- module eligibility;
- scanning/exploration;
- logistics/support roles;
- PI;
- Industry;
- research;
- invention;
- reactions.

Show:

- current capability;
- blockers;
- recently unlocked capability;
- planned future capability.

Link to the canonical owning domain rather than duplicating its management UI.

---

# Industry & PI

Industry & PI is a character-specific capability/readiness view.

It may show:

- PI colony capacity;
- current colony usage;
- relevant PI skills;
- manufacturing slots;
- research capability;
- invention capability;
- reaction capability;
- relevant blockers.

The full PI and Industry planning/operations workflows remain in their own domains.

---

# Activity

Activity is a curated character-specific timeline.

Appropriate events may include:

- ESI authorization changes;
- meaningful skill completions;
- milestone completions;
- Doctrine Tier readiness changes;
- important capability unlocks;
- meaningful operational state changes.

Do not expose raw ESI event exhaust simply because the data exists.

---

# What-If Scenarios

Scenario mode is a first-class Training workflow.

Use an explicit mode switch:

**Live Queue | Scenario**

Live Queue is authoritative.

Scenario is hypothetical.

Scenario state must never masquerade as EVE execution state.

---

# Scenario Baseline

A scenario begins by cloning the current authoritative live queue state into a hypothetical Bastion planning state.

The same familiar vertical queue grammar should be used so comparison remains easy.

Scenario visuals must remain clearly distinct from live queue visuals.

---

# Scenario Actions

Supported scenario actions may include:

- clone Live Queue into Scenario;
- drag/reorder scenario queue entries;
- insert planned skills;
- insert prerequisites;
- remove planned scenario entries;
- prioritize a milestone;
- reset scenario to live;
- save named scenario;
- compare scenario to live;
- compare saved scenarios where useful;
- produce an ordered recommendation or supported importable plan artifact.

Do not provide an Apply to EVE control.

Do not imply Bastion can directly rewrite/reorder the live EVE skill queue.

---

# Scenario Impact Analysis

Scenario mode should include a persistent impact-analysis region.

It may show:

- Doctrine-readiness date delta;
- milestone completion delta;
- total training-time delta;
- capabilities unlocked earlier;
- capabilities delayed;
- new/missing prerequisites;
- new skillbook requirements;
- skillbook sourcing cost;
- plan-alignment changes.

The impact analysis is deterministic.

---

# Scenario Recalculation

Bastion recalculates all affected active plans and milestones against the hypothetical ordering.

Outputs may include:

- milestone-completion delta;
- Doctrine-readiness date delta;
- capability unlocked earlier;
- capability delayed;
- total queue-duration delta;
- newly required prerequisite;
- missing skillbook requirement;
- skillbook sourcing cost;
- plan-alignment changes.

---

# Cross-Plan Scenario Effects

Changing one queue entry may affect several assigned Skill Plans.

Scenario recalculation should therefore evaluate all active assigned plans rather than only the visually focused plan.

Shared requirements remain shared rather than duplicated.

---

# Skillbook Sourcing

Missing skillbooks appear in the context of the affected skill, milestone or plan.

Bastion may distinguish:

- already injected;
- missing;
- available through supported remote-injection mechanics;
- Market-HQ physical sourcing;
- incremental sourcing cost.

Viewing a Skill Plan does not itself create procurement.

Procurement begins only after explicit training investment/plan acceptance.

---

# Authorization

Character Detail shows compact ESI authorization health.

Detailed ESI management occurs in the shared Character ESI Authorization drawer defined by Accounts / Characters.

Supported actions include:

- Authorize;
- Reauthorize;
- inspect scopes;
- identify degraded features;
- Disconnect.

Secrets are never exposed.

The canonical authorization-drawer visual is:

`accounts-characters-authorization-drawer-reference-v1.png`

Do not create a separate Character Detail-specific authorization interaction unless a genuinely different page-specific state is later required.

---

# Freshness

Live queue, trained skills, location, ship state and projections all retain freshness metadata.

When authoritative state becomes stale:

- show degradation;
- degrade projection confidence;
- do not preserve stale milestone dates as if they remain current.

Missing or stale state is never equivalent to zero.

---

# Deterministic Product Boundary

Everything Character Detail calculates or displays operationally must be available through deterministic Bastion services.

This includes:

- skill-state reconciliation;
- live-queue regression;
- requirement classification;
- milestone projection;
- Doctrine Tier readiness;
- capability evaluation;
- What-If recalculation;
- validation;
- freshness/degradation.

No LLM inference is required for Character Detail to function.

---

# MCP Boundary

Bastion MCP exposes the same deterministic Character Detail, Skill Plan, Doctrine and training services used by the human UI.

An external assistant may use MCP to:

- inspect live training state;
- inspect plan alignment;
- query Doctrine Tier readiness;
- compare deterministic scenarios;
- identify blockers;
- request deterministic recalculation;
- explain results conversationally;
- propose structured scenario or plan changes;
- submit authored metadata or draft changes.

Inference happens in the external assistant.

The assistant does not own hidden mechanics or calculations that Bastion itself cannot reproduce.

Assistant-originated changes use normal Bastion draft, diff, approval and provenance semantics.

---

# Cross-Domain Navigation

Character Detail should preserve context while allowing traversal into canonical owning domains.

Examples:

- Doctrine;
- Skill Plan;
- PI;
- Industry;
- Inventory;
- Procurement.

Use context-preserving drawers where useful and full-page handoff when deeper management is required.

Breadcrumbs should retain traversal context where practical.

---

# Visual Direction

The approved Character Detail visual direction remains valid.

The Training surface should retain:

- EVE-familiar vertical skill queue;
- current-skill emphasis;
- compact level cues;
- duration at a glance;
- multiple assigned-plan contribution markers;
- injected milestone markers at actual projected queue boundaries;
- persistent right-side milestone/scenario inspector;
- explicit Live Queue / Scenario distinction;
- compact queue divergence information.

Avoid:

- replacing the queue with a standalone Gantt as the primary representation;
- duplicating queue rows for shared requirements;
- heavy semantic row coloring;
- suggesting direct write access to the EVE queue;
- presenting Doctrine Tier readiness as a Skill Plan-owned tier;
- embedding required LLM/assistant inference into the page.

---

# Canonical Visual References

The following images are the approved canonical visual references for this surface:

- `character-detail-training-reference-v1.png`
  - Primary Character Detail Training / Live Queue state.
  - Shows authoritative live EVE queue, multiple assigned Skill Plan overlays, shared-skill contribution markers, projected milestone markers, queue divergence, and selected milestone detail.
  - This existing approved render remains valid and does not require regeneration.

- `character-detail-scenario-reference-v1.png`
  - What-If Scenario state.
  - Shows hypothetical queue editing, explicit Live Queue / Scenario separation, Doctrine-readiness milestones, cross-plan contribution, training-time impact, capability unlock impact, missing prerequisites/skillbooks, and plan-alignment deltas.
  - This is the canonical visual reference for first-class Scenario mode.

Shared authorization visual:

- `accounts-characters-authorization-drawer-reference-v1.png`
  - Defined in the Accounts / Characters reference.
  - Used when Character Detail opens character ESI authorization management.

These images communicate approved layout, hierarchy, density and interaction-state direction.

The companion Markdown and current structured Bastion design decisions remain authoritative for semantics.

Generated sample character names, skill names, dates, durations, ISK values, plan percentages, Doctrine examples or incidental controls in the images must not override the written specification.

---

# Visual Reference Status

The Character Detail handoff consists of:

- this companion reference;
- `character-detail-training-reference-v1.png`;
- `character-detail-scenario-reference-v1.png`;
- shared use of `accounts-characters-authorization-drawer-reference-v1.png`.

No rerender is required for the approved primary Training reference.

The Scenario reference completes the major first-class alternate Training state needed by the future UI/UX designer.