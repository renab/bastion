# Market / Trade UI Reference

![Market and trade workspace](market-trade-workspace.png)

## Product purpose and concept

Market / Trade is the canonical operating view for own contracts, buy orders, sell orders, fills, competitive context, and explainable trade recommendations. It is not a global trader configuration page. Each order records its own **Issued By** character, location, price, progress, current best buy/sell context where meaningful, status, and next action. Market HQ is a separate enterprise setting/assumption, provisionally Amarr, not a claim that every order or asset is there.

The primary page is a dense unified order ledger with type/status/location filters and a selected order inspector. Recommendations explain their comparison basis, freshness, expected spread after fees/logistics, market depth, source inventory/requirement, and caveats; an action may open the order, create a proposal, or send a need to Procurement. It never auto-trades.

### States and workflow

| State | Behavior |
| --- | --- |
| Active order | show owned order, fill/progress, competitive context, issued-by, and next review |
| Expired/filled/cancelled | retain historical event context; dismiss/acknowledge appropriate attention |
| Stale/limited market evidence | label freshness/coverage, suppress certainty |
| No market activity | purposeful empty state with data-source status and navigation to inventory/procurement |

**Must not do:** show a global configured trader; represent recommendations as facts; put PO operations here; or explain architectural HQ boundaries as end-user copy.

## Source audit

- Current Galaxy `bastion-surface-refinement-v1` (`33659d9e-c51d-4916-b0a5-b28ee9813f0e`) settles unified order listing and competitive context requirements.
- Current Galaxy `bastion-procurement-logistics-workflow-v1` (`9a4b6f9c-c85d-4a9e-8c57-ec782bcc2fbd`) supplies Market HQ and procurement handoff boundaries.
- Current Galaxy `bastion-attention-model-v1` (`7f908da4-fa47-4c90-815f-946155c23db9`) covers attention lifecycle for meaningful order events.

## Visual-generation brief and mockup audit

Render a 16:9 `Market / Trade` ledger with a unified rows table for sample buy orders, sell orders, contracts, and fills. Include columns for Issued By, location, own price, fill/progress, best buy/sell, freshness, and action. The selected-order drawer must show an explainable recommendation and a source/procurement handoff. Use no global trader profile, sample data only, and the visible prototype label.

Audit: each row has an Issued By field; the recommendation names economic inputs/caveats; the drawer preserves source/full-page controls; procurement is a handoff, not an embedded PO editor.

## Interpretation boundary

Can change: order grouping, chart design, trade metrics, and recommendation prose. Must preserve row-level issuer, unified trade objects, explainability/freshness, no auto-trade, and explicit Procurement handoff.
