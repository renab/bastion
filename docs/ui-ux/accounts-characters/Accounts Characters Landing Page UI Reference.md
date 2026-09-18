# Bastion — Accounts / Characters Reference

## Status

Current product and UI/UX reference for the Bastion Accounts / Characters domain.

The approved Accounts / Characters visual direction remains valid.

This document supersedes earlier Accounts / Characters reference language where it conflicts with the current deterministic-core architecture, Skill Plan ownership model, Doctrine-tier model, or canonical visual-reference handoff rules.

---

# Purpose

Accounts / Characters is the canonical Bastion surface for:

- EVE account grouping;
- character association;
- character-scoped ESI authorization;
- authorization health and scope management;
- subscription/account context;
- character navigation;
- access to the shared Skill Plan library.

Character-specific deep work belongs in Character Detail.

System-level integrations and corporation-wide configuration belong in Settings rather than Accounts / Characters.

---

# Primary Sub-Surfaces

Accounts / Characters contains two sibling primary sub-surfaces:

1. Roster
2. Skill Plans

The Roster is account- and character-centric.

Skill Plans is the shared enterprise training-definition library.

Character-specific Skill Plan application, live-queue alignment, readiness, projection and comparison belong in Character Detail rather than in the shared Skill Plans library.

---

# Roster

## Purpose

The Roster is the normal entry point for:

- account organization;
- character association;
- authorization health;
- compact operational state;
- navigation into Character Detail.

The visual model is account-first.

Each account renders as a grouped container containing exactly three Bastion character-association positions.

---

# Account Model

An account is the visible parent container.

Characters are associated beneath that account.

Bastion supports up to three associated character positions per account.

The account container may show:

- optional Bastion-local account alias;
- Alpha / Omega / Unknown subscription state where known;
- number of currently associated characters;
- compact authorization-health rollup from child characters.

The optional account alias is Bastion-local organizational metadata.

It is not an EVE account identity or source-of-truth claim.

---

# Character Association Capacity

Bastion exposes exactly three character-association positions within each account container.

An unassociated position means:

> Bastion currently has no character associated with this position.

It does not prove the corresponding EVE character slot is actually empty unless roster completeness has been independently established.

Therefore the normal unassociated-state label is:

**Associate Character**

Do not label the position:

**Empty Slot**

unless Bastion has authoritative evidence that the EVE slot is genuinely empty.

Backend account-concurrency and subscription constraints remain planning inputs rather than separately managed seat objects.

---

# Account Container Layout

Each account container should be compact and information-dense.

The account-level header may contain:

- Bastion-local alias;
- subscription state;
- child-character authorization-health rollup;
- associated-character count.

Below the account header are exactly three character positions.

Each position is either:

- an associated character; or
- an Associate Character action.

---

# Associated Character Presentation

An associated character position should prominently show:

- official EVE portrait where available;
- full canonical character name;
- compact ESI authorization state;
- current or recent ship where useful;
- current or recent location where useful;
- compact training or queue warning where relevant;
- freshness/degradation indicator where source data is stale.

Do not substitute generic avatars when official EVE portraits are available.

Selecting the associated character opens the canonical Character Detail page.

The Roster should remain compact and should not expand into full training, capability, Industry or PI management.

---

# Unassociated Character Position

An unassociated position renders as:

**Associate Character**

It may provide a short secondary explanation that Bastion has no character associated with that position.

It must not imply that the underlying EVE account slot is known to be empty.

---

# Character ESI Authorization

ESI authorization is character-scoped.

Account containers may summarize authorization health across their child characters, but the underlying authorization belongs to each character.

The Roster and Character Detail show summary authorization state.

Detailed authorization management occurs in a dedicated character authorization drawer.

---

# Authorization Drawer

The character authorization drawer is a shared Accounts / Character Detail interaction surface.

It supports:

- Authorize ESI;
- Reauthorize ESI;
- inspect granted scopes;
- inspect required scopes;
- identify missing scopes;
- explain which Bastion features are degraded by missing scopes;
- inspect authorization freshness;
- disconnect authorization.

The drawer should clearly distinguish:

- current authorization state;
- granted scopes;
- missing scopes;
- affected features;
- corrective actions.

Refresh tokens, raw credentials, secrets or equivalent sensitive material are never displayed.

Secrets must not appear in ordinary Bastion domain tables, logs, Analytics, documentation or user-facing diagnostics.

---

# Authorization States

## Healthy

Required scopes are present and recent refresh activity is successful.

## Partial Scopes

The character remains connected, but one or more Bastion features are degraded.

Show:

- exact missing scope;
- affected domain or feature;
- clear reauthorization path.

## Unauthorized

Character association exists, but ESI authorization has not been granted.

Identity and Bastion association may remain visible while ESI-dependent features show explicit degradation.

## Expired / Failed Authorization

Use a high-salience reauthorization state.

## Stale Data

Preserve the last observed information only with explicit freshness context.

Do not present stale state as current.

Missing or stale data must never be interpreted as zero, absence or healthy state.

---

# Account Actions

Supported account-level actions may include:

- create Bastion account grouping;
- edit local alias;
- archive account grouping;
- associate character;
- correct character association;
- move/reassociate a character between account containers where necessary.

An account grouping is a Bastion organizational construct.

Do not infer unsupported EVE account identity details from the grouping itself.

---

# Character Actions From Roster

Supported character-level actions may include:

- open Character Detail;
- authorize ESI;
- reauthorize ESI;
- inspect authorization health;
- inspect scopes;
- disconnect authorization;
- correct account association.

Deep character-specific work should transition to Character Detail rather than indefinitely expanding inside the Roster.

---

# Account Concurrency

Account subscription and parent-account concurrency are deterministic backend planning inputs.

They may influence:

- doctrine fieldability;
- multi-character operational readiness;
- character-training value;
- opportunity planning.

Do not expose a permanent standalone Seat Management object.

Concurrency consequences should surface contextually where they matter.

Josh remains one human operator, so account concurrency and human/operator feasibility are separate constraints.

---

# Skill Plans Sub-Surface

Skill Plans is a sibling primary sub-surface to Roster.

It is the shared enterprise library and authoring environment for canonical training definitions.

Characters reference canonical shared plans rather than receiving duplicated private copies.

The Skill Plans domain has its own detailed product/UI reference.

---

# Shared Skill Plan Library Responsibilities

The shared Skill Plans surface supports:

- list canonical plans;
- search plans;
- filter plans;
- create plan;
- edit plan;
- clone plan;
- retire plan;
- inspect current revision;
- inspect historical revisions;
- author requirements;
- author milestones;
- define capability outcomes;
- manage dependency/reference-order semantics;
- generate supported EVE-importable skill-plan artifacts;
- track publication state;
- track source/template freshness;
- track deterministic validation state.

Character-specific application is explicitly outside the shared-library responsibility.

---

# Character-Specific Skill Plan Boundary

The shared Skill Plan library does not act as the primary character-comparison workspace.

Character Detail owns:

- plan assignment/application;
- current character readiness;
- trained-skill reconciliation;
- live-queue alignment;
- milestone projection;
- Doctrine Tier readiness;
- What-If scenarios;
- character-specific blockers;
- missing skillbooks;
- character-specific training timing.

This keeps canonical training definitions separate from pilot execution state.

---

# Skill Plan Sources

Skill Plans may be derived from or linked to:

- Doctrine Tier;
- doctrine;
- approved fit or fit variant;
- hull;
- module;
- PI capability;
- Industry capability;
- research capability;
- invention capability;
- reaction capability;
- other deterministic Bastion capability objects;
- standalone manually authored training goals.

Doctrine owns Doctrine Tier readiness semantics.

A doctrine-derived Skill Plan consumes the selected Doctrine Tier and resolves its concrete training requirements.

Skill Plan does not own a parallel independent Doctrine-style Tier I–V readiness hierarchy.

---

# Cross-Domain Behavior

## Doctrines

Doctrines consume:

- character eligibility;
- character support/readiness;
- parent-account concurrency;
- approved fit/variant state;
- inventory/fit availability.

Do not duplicate Doctrine management inside Accounts / Characters.

## Skill Plans

Accounts / Characters exposes the shared Skill Plan library.

Character-specific queue regression and readiness projection occur in Character Detail.

## Procurement

Missing skillbooks do not automatically create procurement.

A sourcing or procurement requirement begins only after explicit training-investment or plan acceptance.

## Executive Brief

Executive Brief may reuse the same official character portraits and compact operational identity language for active characters.

## Settings

Settings does not duplicate character ESI authorization controls.

Settings owns low-frequency system-level configuration and integrations.

---

# Edge States

## No Accounts

Show purposeful onboarding.

Primary actions may include:

- Create Account Group;
- Associate Character;
- Authorize Character.

Do not show an empty operational roster without explanation.

## Account With No Associated Characters

Show three Associate Character positions.

Do not imply actual EVE emptiness.

## Character Unauthorized

Show character identity and Bastion association with explicit authorization-required state and exact feature degradation.

## Partial Scopes

Show the missing scope and affected features.

Unknown information is not zero.

## Expired / Failed Authorization

Provide a clear reauthorization path.

## Stale Queue / Location / Ship State

Show freshness and degradation.

Do not render stale values as current.

## No Shared Skill Plans

Provide purposeful actions such as:

- Create Plan;
- Build From…;
- Import supported Skill Plan artifact.

---

# Deterministic Product Boundary

Accounts / Characters must be fully functional without LLM inference.

All normal behavior is implemented through deterministic Bastion domain services.

This includes:

- account grouping;
- character association;
- authorization state;
- scope health;
- roster state;
- subscription/concurrency metadata;
- Skill Plan library state;
- navigation;
- validation and domain relationships.

No core Accounts / Characters workflow depends on an embedded assistant or LLM.

---

# MCP Boundary

Bastion MCP exposes the same deterministic Accounts / Characters domain state and operations used by the human UI.

An external assistant may use MCP to:

- inspect account structure;
- inspect character association;
- inspect authorization health;
- inspect character capabilities;
- query deterministic Skill Plan state;
- invoke supported deterministic operations;
- submit structured draft changes where permitted.

The assistant performs inference outside Bastion.

Bastion remains fully usable when no assistant is connected.

Assistant-originated changes use normal Bastion provenance, draft, diff and review semantics.

---

# Visual Direction

The approved Accounts / Characters visual direction remains valid.

The preferred Roster presentation is:

- dense account-first horizontal groupings;
- three character positions per account;
- official character portraits;
- full canonical names;
- compact ESI health;
- compact operational/training state;
- contextual authorization management.

Avoid:

- generic card-wall dashboards;
- separate account-seat management UI;
- generic character avatars;
- full training trajectories on the Roster;
- duplicated ESI controls in Settings;
- character-comparison workflows inside the shared Skill Plan library.

---

# Canonical Visual References

The following images are the approved canonical visual references for this surface:

- `accounts-characters-roster-reference-v1.png`
  - Primary Accounts / Characters Roster state.
  - Shows account-first grouping, three character-association positions, official portraits, compact training/ship/auth state, and the Accounts / Skill Plans sub-surface relationship.
  - This existing approved render remains valid and does not require regeneration.

- `accounts-characters-authorization-drawer-reference-v1.png`
  - Shared Character ESI Authorization drawer state.
  - Shows authorization status, granted scopes, missing scopes, feature degradation, freshness, reauthorization and disconnect actions.
  - This drawer may be invoked from either the Roster or Character Detail.

These images communicate approved layout, hierarchy, density and interaction-state direction.

The companion Markdown and current structured Bastion design decisions remain authoritative for semantics.

Generated sample names, values, ESI scopes, counts, ship names, labels or incidental controls in the images must not override the written specification.

---

# Visual Reference Status

The Accounts / Characters handoff consists of:

- this companion reference;
- `accounts-characters-roster-reference-v1.png`;
- `accounts-characters-authorization-drawer-reference-v1.png`.

No additional Roster rerender is required following:

- Doctrine-owned tiering;
- the deterministic-core clarification;
- the external-assistant-via-MCP architecture;
- the Shared Skill Plans semantic refactor.

The authorization drawer is the canonical shared ESI management visual for both Roster and Character Detail.