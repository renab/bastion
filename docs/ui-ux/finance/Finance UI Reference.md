# Finance / Books UI Reference

![Finance and books workspace](finance-workspace.png)

## Product purpose and concept

Finance / Books is management accounting for current position, period performance, liabilities, transactions, valuation confidence, and cross-domain financial meaning. It is not a historical-basis archaeology view and does not force an uncertain balance into a polished dashboard. Current position, realized period performance, projections, liquidity, controlled assets, liabilities, and unresolved/reconciliation state are separate concepts. Liquidity is a non-additive lens into assets, not a component to add again to Total Assets.

The workspace supports a position view, a period-performance view, transaction/ledger review, and a selected-item inspector. It uses tables and timelines for accountable details, and compact trend/waterfall visuals only where they answer a question. Candidate classifications, reconciliation hypotheses, and valuation assumptions are reviewable working states, never silently frozen immutable facts. Cross-links open controlled Inventory, Market, Industry/PI, Procurement, losses, or evidence.

### States and workflow

| State | Behavior |
| --- | --- |
| Reconciled measurement | source, observation time, valuation basis, and confidence visible |
| Estimate or projected value | separately labeled and excluded from realized totals |
| Open reconciliation/candidate | review queue, evidence and decision action; not a final account balance |
| Missing/stale source | explicit coverage gap, no inferred zero |

Workflow: choose period or current position -> drill into line item -> inspect evidence/classification -> link to owning operational source -> record/review a reconciliation decision in the canonical finance workflow. Prototype actions are illustrative only.

**Must not do:** invent balancing equity; double-count liquidity; collapse on-planet/uncontrolled goods into assets; treat a candidate tab as immutable ledger history; or make Finance an executive KPI wall.

## Source audit

- Current Galaxy `bastion-surface-refinement-v1` (`33659d9e-c51d-4916-b0a5-b28ee9813f0e`) identifies Finance as a high-priority unresolved design seam and requires current-vs-period, asset/liability/equity/cash, realized-vs-projected, and cross-domain clarity.
- Current Galaxy `bastion-pi-domain-v1` (`884e9970-22e6-4e5a-8c48-dcfcee0ddea2`) sets the PI custody recognition boundary.
- Finance reconstruction lineage remains qualified: current reconciliation truth must come from authoritative records/evidence, not this sample visual.

## Visual-generation brief and mockup audit

Render a 16:9 dense `Finance / Books` management-accounting workspace. Show a deliberately non-additive Current Position panel (controlled assets, liabilities, net position, liquidity lens), period performance with realized/projection separation, a transaction/evidence table, and a right `Reconciliation Candidate` inspector with provenance/confidence and cross-links. Mark `PROTOTYPE - SAMPLE DATA - NOT LIVE`. Avoid a large inspirational summary, a fabricated balanced equity figure, or a tab labelled immutable candidates.

Audit: liquidity is visibly a lens, not added into assets; estimate/projection labels are distinct; the candidate inspector is reviewable; and evidence/cross-domain source links are present.

## Interpretation boundary

Can change: account categories, charts, period controls, and sample figures. Must preserve non-additivity, realized/projection distinction, custody boundary, evidence/confidence, and explicit unresolved reconciliation states.
