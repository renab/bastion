# Finance / Books UI Reference

![Finance and books workspace](finance-workspace.png)

## Product purpose and concept

Finance / Books is Bastion’s management-accounting workspace for understanding the company’s current financial position, historical movement, liabilities, realized performance, projected near-term outcomes, and unresolved reconciliation work.

It should answer five questions clearly:

1. What does Naffin Enterprises currently control?
2. What does it owe, and what is owed to it?
3. What is the current net position?
4. What changed over time, and why?
5. What financial events still require classification, reconciliation, or operator action?

Finance is not a generic executive KPI dashboard, and it is not a historical-basis archaeology screen.

It must keep several concepts explicitly separate:

- current recognized assets;
- liabilities;
- net position;
- liquidity;
- realized period performance;
- projected future activity;
- valuation basis;
- unresolved reconciliation state.

Liquidity is a non-additive lens into recognized assets. It is not added again to Total Assets.

Projected values, candidate classifications, and reconciliation hypotheses remain working states until they are supported by authoritative evidence or explicitly accepted through the Finance workflow.

---

## Primary information architecture

Finance / Books uses four primary surfaces:

- **Overview**
- **Ledger**
- **Liabilities**
- **Reconciliation**

The default landing surface is **Overview**.

Period Performance is an important Overview component rather than a separate first-class page.

---

# 1. Overview

## Purpose

The Overview answers:

> What is the company’s current financial position, how has that position changed, what happened during the selected period, and what recent financial activity needs attention?

The page is composed of:

1. current-position summary;
2. valuation-basis control;
3. Position History;
4. Period Performance;
5. Recent Financial Activity;
6. contextual Financial Event Inspector.

---

## Current-position summary

The top summary area should contain four distinct concepts.

### Controlled Assets

Current recognized enterprise assets under the selected valuation basis.

Example breakdowns may include:

- Cash & Equivalents
- Inventory
- Fixed / Strategic Assets
- Other Recognized Assets

Exact category taxonomy may evolve.

### Liabilities

Current recognized obligations.

Typical breakdowns may include:

- Reimbursement Payables
- Contracts / Deposits / Escrow
- Other Liabilities

The top-level amount should link into the canonical Liabilities page.

### Net Position

Calculated as:

**Controlled Assets - Liabilities**

Net Position should remain visually prominent but should not obscure the underlying asset and liability composition.

Where useful, also show:

- prior-period change;
- absolute delta;
- percentage change;
- last-updated time.

### Liquidity Lens

Liquidity is deliberately separate and explicitly labeled:

**Liquidity Lens — non-additive**

It may include:

- Wallet Cash
- Market Escrow
- Near-term Receivables

Liquidity is a subset/lens over current position and must not be added again to Controlled Assets or Net Position.

---

# Valuation basis

Finance should expose a compact page-level **View Basis** selector.

Initial supported modes:

- **Books**
- **Liquidation**

A future **Economic** mode may be added only if it can be defined consistently across domains.

## Books

Shows recognized accounting/carrying treatment under Bastion’s Finance rules.

## Liquidation

Shows current net-realizable / liquidation-oriented values using current defensible market and realizability assumptions.

Changing the basis may alter:

- Controlled Assets;
- Net Position;
- Position History;
- asset drill-down values.

It should not rewrite historical ledger events or transform projected amounts into realized values.

Do not show every valuation concept simultaneously in the top summary if doing so makes the position unreadable.

---

# Position History

Position History is the primary historical visual on the Overview.

Prefer a line-based chart showing:

- Assets
- Liabilities
- Net Position

Liquidity may be available as an optional overlay rather than a permanent fourth accounting series.

## Controls

Support:

- date range;
- granularity;
- valuation basis;
- optional liquidity overlay;
- optional material-event markers.

## Event markers

Material events may appear on the timeline, such as:

- capital contribution;
- major purchase;
- major sale;
- asset loss or write-off;
- liability settlement;
- large reimbursement batch;
- reconciliation adjustment.

Selecting a marker should open contextual detail without losing the selected financial view.

The chart must visually reinforce that:

**Net Position = Assets - Liabilities**

It should not imply that the three series are unrelated metrics.

---

# Period Performance

Period Performance remains part of Overview.

It should clearly separate:

- **Realized**
- **Projected Additional**
- **Expected Total**

Typical rows may include:

- Revenue / Proceeds
- Cost of Goods Sold
- Operating Expenses
- Realized Result

Projected activity must never be silently folded into realized results.

The projected column may include defensible future items such as:

- expected market fills;
- accepted purchase commitments;
- expected industry completion;
- scheduled liabilities;
- other explicitly modeled near-term activity.

Projected values must retain source, freshness, confidence, and assumption context where material.

---

# Recent Financial Activity

The lower part of Overview contains a compact **Recent Financial Activity** table.

This is a filtered operational slice of the full Ledger, not the entire durable transaction history.

Useful columns include:

- Date
- Direction
- Type
- Description
- Counterparty
- Domain Source
- Amount
- Account / Classification
- Status
- Evidence
- Open / Inspect

Typical statuses may include:

- Matched
- Pending
- Needs Review
- Projected
- Reconciled

Selecting a row opens the Financial Event Inspector.

The full historical browser lives on the Ledger page.

---

# 2. Ledger

## Purpose

The Ledger is the canonical Finance browser for durable recognized financial events.

It is not simply an EVE wallet-journal clone.

It should combine relevant financial events from across Bastion, including:

- market sales;
- purchases;
- industry costs;
- taxes and fees;
- reimbursements;
- capital contributions;
- capital returns;
- losses and write-offs;
- insurance recoveries;
- contract payments;
- reconciliation adjustments;
- other recognized enterprise financial events.

## Filters

Support combinations such as:

- date / accounting period;
- account / classification;
- source domain;
- character / custodian;
- counterparty;
- cash vs non-cash;
- realized vs projected;
- operating vs capital;
- credit vs debit;
- matched / pending / unresolved.

Every material event should retain provenance and link back to its underlying source evidence.

---

# 3. Liabilities

## Purpose

Liabilities is a first-class operational surface for obligations that still require settlement or tracking.

This includes real enterprise workflow such as reimbursement payables created when a character personally pays an enterprise expense.

## Primary table

Useful columns include:

- Liability Type
- Payee / Counterparty
- Origin
- Amount
- Date Incurred
- Due / Age
- Status
- Linked Event
- Settlement Action

## Statuses

Examples:

- Open
- Pending Payment
- Scheduled
- Partially Settled
- Settled
- Disputed / Needs Review

## Useful views

Support:

- grouped by payee;
- grouped by source domain;
- aging view;
- open total;
- recently settled.

Settling a liability must link back to the original expense/event and must not create a second expense where the cost has already been recognized.

---

# 4. Reconciliation

## Purpose

Reconciliation is the review queue for financial events whose classification, evidence, or matching is incomplete.

Examples include:

- unmatched wallet or market events;
- partially matched events;
- missing source evidence;
- low-confidence classification;
- suspected duplicate events;
- events requiring operator approval.

The Reconciliation page should behave like a workbench rather than a passive report.

---

# Financial Event Inspector

The right-side inspector is a reusable contextual surface across Finance.

It should not always be labeled “Reconciliation Candidate.”

Its title and actions should adapt to the selected object.

## Typical content

- event identity;
- amount;
- direction;
- source domain;
- location;
- counterparty;
- classification;
- confidence;
- source coverage;
- supporting evidence;
- cross-domain links;
- reconciliation state.

## Contextual behavior

### From Overview

Inspect recent activity without leaving the current position view.

### From Ledger

Inspect event evidence/classification and open the canonical full record when necessary.

### From Liabilities

Inspect:

- original expense;
- payee;
- reimbursement logic;
- settlement history;
- current status.

### From Position History

Selecting a material timeline event may open the same inspector with the relevant contributing records.

## Standard actions

Depending on state:

- Open Source
- View Full Record
- Accept Classification
- Mark for Review
- Defer
- Open Owning Module

The inspector should preserve the user’s current filters, selected period, chart range, and navigation context.

---

# Reconciliation candidate behavior

Where a financial event is unresolved, the inspector may expose a proposed classification.

The proposed classification should include:

- account;
- category;
- source type;
- accounting period;
- supporting evidence;
- confidence.

A proposal is not immutable accounting truth.

It must remain explicitly reviewable until accepted.

Do not invent balancing equity or force a transaction into a category solely to make totals reconcile.

---

# Source and confidence

Every material number should have a defensible path to source data.

Possible source classes include:

- Galaxy durable Finance records;
- ESI wallet data;
- Market transactions/orders;
- Inventory telemetry;
- Industry/PI events;
- Procurement records;
- contracts;
- user-confirmed reconciliations.

When source coverage is incomplete:

- show the gap;
- reduce confidence;
- avoid false precision;
- never infer zero.

Unknown, stale, and unobserved are distinct from zero.

---

# Cross-domain relationships

Finance is a consumer of authoritative objects owned by other Bastion domains.

## Inventory

Provides:

- controlled quantities;
- custody;
- location;
- commitment;
- current realizability.

Finance should inspect Inventory objects in-place but should not become a second inventory browser.

## Market / Trade

Provides:

- orders;
- fills;
- escrow;
- market proceeds;
- fees;
- realized sales.

## Industry

Provides:

- job costs;
- recognized input consumption;
- completed output;
- projected production.

Projected production remains projected until the recognition rules are satisfied.

## PI

PI may expose modeled economic value inside PI, but on-planet / launchpad / POCO-side / simulated goods do not contribute to Finance assets.

Recognition begins only once goods enter enterprise-controlled structure/station/hangar custody.

## Procurement / Logistics

Approved purchase requirements and purchase orders may contribute to forecasts or commitments.

Actual fills and recognized costs become realized financial events.

## Doctrines / Losses

Ship and asset losses, reserve usage, write-offs, and replacements may link into Finance without Finance owning doctrine state.

---

# Realized vs projected boundary

This boundary is mandatory.

## Realized/current

Includes recognized financial and asset state supported by authoritative evidence.

## Projected

May include:

- expected market fills;
- forecast purchases;
- planned liabilities;
- expected production completion;
- modeled proceeds;
- forecast cash movement.

Projected values must be visually distinct and must never silently increase:

- realized revenue;
- current cash;
- recognized assets;
- accounting equity;
- net position.

---

# Capital treatment

Capital activity remains separate from operating performance.

Examples:

- owner contribution;
- non-cash asset contribution;
- return of capital.

Capital should be filterable and traceable in the Ledger and may have its own analytical slice later.

Capital contributions must not be misclassified as operating revenue.

---

# Losses and write-offs

Losses, destruction, unrecoverable inventory, and formal write-offs should be distinguishable from normal operating expenses.

They may appear through:

- dedicated filters;
- ledger classifications;
- Position History event markers;
- Analytics.

Do not hide major losses inside generic expense categories.

---

# Empty and degraded states

## No historical series yet

Show current position and explain that Position History will populate as durable snapshots/events accumulate.

Do not render a fake flat chart.

## No open liabilities

Show a compact healthy empty state:

**No open liabilities**

Do not fill the page with zero-value cards.

## No reconciliation work

Show:

**No unresolved finance events**

with the last reconciliation time/source health if useful.

## Missing wallet authorization

Show the affected character/account, missing scope, and path to Accounts / Characters.

Do not treat missing wallet telemetry as zero cash.

## Stale inventory or market data

Show degraded valuation confidence and the affected basis.

For example:

- Books may remain reliable;
- Liquidation view may be stale or partially unavailable.

## Incomplete evidence

Surface the missing source and confidence impact.

Do not infer a polished balance where evidence is incomplete.

---

# Must not do

Finance must not:

- invent balancing equity;
- double-count liquidity;
- treat projected values as realized;
- count on-planet / uncontrolled PI goods as company assets;
- turn candidate classifications into immutable ledger facts;
- hide unresolved evidence gaps;
- become a generic executive KPI wall;
- duplicate Inventory or Market as full secondary modules;
- collapse capital contributions into operating revenue;
- collapse liability settlement into a second expense;
- imply zero when data is merely missing or stale.

---

# Visual-generation brief

Render a dense 16:9 **Finance / Books** management-accounting workspace in the settled Bastion visual language.

The Overview should contain:

- top navigation tabs:
  - Overview
  - Ledger
  - Liabilities
  - Reconciliation
- a compact **View Basis** selector:
  - Books
  - Liquidation
- accounting-period selector;
- four top summary panels:
  - Controlled Assets
  - Liabilities
  - Net Position
  - Liquidity Lens (non-additive)
- a large line-based **Position History** chart showing:
  - Assets
  - Liabilities
  - Net Position
  - optional Liquidity overlay
  - material event markers
- a **Period Performance** panel with:
  - Realized
  - Projected Additional
  - Expected Total
- a large **Recent Financial Activity** table;
- a contextual **Financial Event Inspector** on the right with:
  - evidence;
  - classification;
  - confidence;
  - source coverage;
  - cross-domain links.

Mark visual sample content clearly as non-live where appropriate.

Avoid:

- generic SaaS KPI-card composition;
- a standalone Period Performance page;
- stacked-bar Position History as the primary history visual;
- a permanent Reconciliation Candidate label for every selected event;
- fabricated balancing figures;
- displaying multiple valuation models simultaneously in a way that obscures the selected basis.

---

# Mockup interpretation

The approved visual reference captures the intended:

- overall proportions;
- operational density;
- four-surface Finance architecture;
- current-position summary;
- valuation-basis control;
- Position History;
- Period Performance;
- recent financial activity;
- contextual inspector.

The following remain flexible during final UI/UX design:

- exact asset-category names;
- exact chart styling;
- exact table columns/order;
- exact numeric examples;
- exact account taxonomy;
- inspector micro-layout;
- responsive behavior.

The following must be preserved:

- Overview / Ledger / Liabilities / Reconciliation architecture;
- Books vs Liquidation basis distinction;
- Liquidity as non-additive;
- Net Position = Assets - Liabilities;
- realized vs projected separation;
- first-class liability workflow;
- evidence/confidence visibility;
- explicit reconciliation state;
- PI custody boundary;
- contextual cross-domain inspection;
- no inferred zero from missing telemetry.

---

# Authoritative design sources

At the time this reference was created, Finance was still inherited primarily from the Nirauan Finance / Books design lineage and the Bastion surface-refinement work rather than from a dedicated `bastion-finance-domain-v1` leaf.

Relevant current sources include:

- current `bastion-surface-refinement-v1`
- current `bastion-pi-domain-v1`
- current Bastion cross-domain navigation decision
- Finance / Books sections in:
  - `wormlife-trial/05 Planning/Outbound Flight - Bastion Design Notes.md`
  - `wormlife-trial/05 Planning/Outbound Flight - Nirauan Design Notes.md`

Before implementation, resolve the current Galaxy records rather than relying on UUIDs copied into this document if those records have since been superseded.

The product-source hierarchy remains:

1. current Galaxy structured decision;
2. current Bastion Design Notes;
3. non-superseded inherited Nirauan design;
4. approved visual reference;
5. prototype implementation.

The visual reference is an approved UI/UX direction, not a pixel contract.