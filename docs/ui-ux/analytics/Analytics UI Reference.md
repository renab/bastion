# Analytics UI Reference

![Analytics historical analysis workspace](analytics-workspace.png)

## Product purpose and concept

Analytics is a first-class historical and cross-domain analysis workspace. It consumes domain history but does not replace each domain's live current-state view or authoritative record. Its primary questions are comparisons, trends, cohorts, performance, and operational learning: for example, trend of opportunity realization by source and period, logistics delay by route class, or readiness changes across doctrine iterations.

The main page starts with a saved analytical question, period/cohort/coverage filters, a chart appropriate to the question, a dense drill-down table, and source/metric definition inspector. It distinguishes observed, calculated, estimated, missing, and excluded data. A selected series/row opens a contextual drawer with calculation version, exclusions, source owner, evidence freshness, and **Open Source / View Full Page**.

### States and workflow

| State | Behavior |
| --- | --- |
| Complete analysis | show metric definition, time window, data coverage, drill-down |
| Partial coverage | retain result but make exclusions/missing source visible |
| Metric unavailable | explain missing inputs and link to owning source, not a zero chart |
| No saved analyses | start from a decision question/template rather than an executive dashboard |

**Must not do:** duplicate current Executive Brief cards; treat analytics aggregates as source truth; hide calculation definitions; or turn partial coverage into certainty.

## Source audit

- Current Galaxy `bastion-analytics-domain-v1` (`824a6467-72cc-45fa-9f81-73523177c4c4`) establishes cross-domain historical analysis and non-replacement of owning domains.
- Current Galaxy `bastion-cross-domain-navigation-v1` (`44cb69f8-0733-4a15-9328-f1ff41d94bbc`) supplies context-preserving inspection/handoff.
- Finance/PI/Industry source boundaries remain visible through data coverage and owner links; the prototype does not construct a new truth hierarchy.

## Visual-generation brief and mockup audit

Render a 16:9 `Analytics` analysis workspace, not a dashboard: saved-question selector, period/cohort/coverage filters, one explanatory trend/comparison chart, dense underlying-record table, and a metric definition/provenance drawer with observed/calculated/estimated/missing legend. Mark as prototype sample data. Avoid live chain topology, broad KPI cards, or unexplained scorecards.

Audit: the analytical question is named; coverage/exclusions are first-class; a single chart is supported by a detailed table; source-owner handoffs are visible.

## Interpretation boundary

Can change: analytical templates, chart type, cohort dimensions, and table columns. Must preserve historical/cross-domain purpose, traceable calculation/coverage, underlying-record drill-down, and owner-domain authority.
