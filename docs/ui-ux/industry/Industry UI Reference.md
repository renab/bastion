# Bastion Industry UI Reference

These renderings are approved visual-direction references for the Bastion **Industry** domain. They capture the intended product language, information hierarchy, density, and interaction patterns more closely than the current prototype.

They are not literal final screenshots or pixel-perfect specifications. Exact layouts, wording, values, component dimensions, and controls may evolve during the dedicated Bastion UI/UX design pass. Settled Bastion domain rules take precedence if an implementation conflicts with a rendering.

## Reference screens

### Industry Overview

![Industry Overview](industry-overview.png)

The primary Industry landing page. It demonstrates proactive Opportunities generated from controlled on-hand inventory, long-term Production Programs, Active Jobs, Ready / Blocked Plans, warm production-graph and SDE provenance, and dense operational information without turning the page into a generic KPI-card dashboard.

The page should answer: *What can we profitably turn current inventory into, what industrial programs are intentional, what is currently running, and what needs intervention?*

### Opportunity Detail

![Industry Opportunity Detail](industry-opportunity-detail.png)

The detailed view of a single Industry Opportunity. It demonstrates starting inventory, a downstream production chain, multiple economic exit points, a recommended and rejected/alternative path, procurement requirements, economic breakdown, logistics impact, feasibility, market and sensitivity analysis, and explicit promotion from Opportunity into a durable production plan.

The important interaction principle is that Bastion explains not only which path is recommended, but why deeper or shallower exit points lost—without requiring the operator to understand the raw solver implementation.

### Production Program

![Industry Production Program](industry-production-program.png)

A durable long-term Production Program / Industry Goal. Unlike a one-time Opportunity, it represents something Naffin Enterprises intentionally wants to produce repeatedly and therefore optimizes for steady-state economics rather than a current-inventory windfall.

It demonstrates target throughput, forecast margin, capital employed, program status, bottlenecks, make-vs-buy choices, reactions, invention, manufacturing, PI inputs, external purchases, constraint analysis, stock buffers / days of cover, forecast-versus-realized production, program economics, and re-optimization or procurement actions.

The page should answer: *Is this production system performing as designed, where is the bottleneck, and should part of the chain be bought, built, expanded, reduced, or redesigned?*

### Execution & Jobs

![Industry Execution and Jobs](industry-execution-jobs.png)

The operational execution surface after an Industry Opportunity or Production Program has produced an accepted plan. It demonstrates running, ready, and blocked jobs; facility and slot availability; dependency-aware job bundles; exact blockers; links into Procurement / Logistics; and completion reconciliation into Inventory.

Accepted plans may contain multiple linked EVE jobs. The interface should make dependency order obvious and help the operator execute the plan without implying that Bastion can perform unsupported EVE actions automatically.

## Shared visual language

These renderings guide Bastion more broadly where applicable:

- **EVE-inspired black glass:** dark or near-black translucent surfaces, restrained transparency, subtle nebula context, and high-opacity panels where readability demands it. Avoid glossy, frosted-mobile aesthetics.
- **Precision borders:** crisp pixel-thin borders and edge highlights around panels, tables, inspectors, drawers, controls, inputs, and graph regions.
- **Corporate branding:** use Naffin Enterprises colors for stylistic shell, selected state, focus, hover, and brand identity only. Semantic/data colors remain independent.
- **Operational density:** compact, readable information; progressive disclosure; contextual drawers; purposeful charts and graphs. Avoid oversized decorative cards and production-facing design-rationale text.
- **Tables versus graphs:** tables support exact scanning and actions; flow views explain relationships such as production value chains.
- **Contextual right-side action regions:** suitable for a primary recommendation, program controls, or execution detail, but not a generic permanent sidebar.
- **Explainability:** recommendations to produce, stop at an exit point, buy rather than build, change a chain, or procure an input must expose their assumptions and economic reasoning.

## Industry architecture reinforced by the references

### Opportunity Engine

Industry asks what high-value, economically sensible transformations can be made from controlled inventory. Blueprint, BPC, and formula ownership does not bound the search: the engine may consider feasible acquisition of blueprints, BPCs, formulae, inputs, and invention/copy/research capability. Every meaningful intermediate may be an economic exit point; the deepest chain is not automatically best.

### Production Programs

Long-term strategic production uses a separate optimization mode: for a deliberately repeated output, what is the best sustainable architecture? It may combine build, react, invent, buy, import, internal stock, and PI inputs. Full vertical integration is not presumed optimal.

### Warm production graph

Bastion maintains a versioned cached production graph. Topology is discovered and persisted; normal operation re-evaluates profitability against inventory, markets, facility costs, skills, logistics, and commitments. New item types may expand the graph incrementally, while new EVE SDE/mechanics versions may trigger an affected-subgraph or full rebuild.

### Finance boundary

Industry recommendations use economic opportunity cost. Finance retains authoritative accounting: projected Industry profit is not booked Finance profit, and output enters normal Inventory/Finance valuation only when authoritative telemetry confirms enterprise-controlled custody.

## Reference status

These assets are approved visual-direction references for future Bastion UI/UX design and prototype implementation. They are not backend schema, mandatory literal wording, final component dimensions, mandatory fictional values, or permission to invent EVE capabilities.
