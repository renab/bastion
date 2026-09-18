# Executive Brief UI Reference

![Executive Brief consolidated chain workspace](executive-brief-workspace.png)

## Product purpose and concept

Executive Brief is Bastion's default, map-first operational cockpit: the consolidated live chain and opportunity workspace, not a shallow dashboard plus a separate Chain page. One real system is one draggable node and one real wormhole connection is one edge. The map owns the viewport; a compact active-character strip and bounded intervention feed support it without creating a KPI-card wall.

The main page holds pan/zoom/recenter/auto-layout controls, system-type border colors, independently-selected opportunity value fill/glow, category filters, Relative/Fixed heatmap control, Operations HQ context, and a concise legend. Selecting a system opens a right inspector with local filters, sites, opportunities, connection facts, and **Open Source / View Full Page** handoff. The inspector may open a canonical domain detail but does not duplicate that domain's management UI.

The attention rail is only for intervention-worthy work and meaningful completed events: acknowledge/dismiss completed items; defer/snooze unresolved work; auto-resolve only when the owning source state resolves. Active characters use compact portraits and full canonical names, then link to Accounts / Characters.

### Page, states, and workflow

| Surface | Purpose | Dominant information | Important states |
| --- | --- | --- | --- |
| Executive Brief | Work a live chain in place | truthful topology map | loading, stale topology, no active chain, disconnected source |
| System inspector drawer | Compare a selected system locally | sites, local opportunity list, connection context | no matching local opportunities, stale evaluation |
| Attention drawer | Triage cross-domain intervention | owner, reason, next action, lifecycle | acknowledged, deferred, snoozed, resolved |

Workflow: filter the chain -> select a system -> assess local opportunities -> open the owning source or canonical page -> act there -> return to the preserved map context. The only permitted top-level history is the traversal breadcrumb (for example, `Executive Brief > system > site > opportunity`), never invented organizational hierarchy.

**Must not do:** invent spatial geometry; show a second Chain & Opportunities destination; let alerts or character details push the map below the desktop fold; present Total/Capability-Covered/Actionable as interchangeable counts; or make the map a decorative mini-widget.

## Source audit

- Current Galaxy `wormlife-local-operations-console-v1` (`4071f967-3d43-4dba-a083-26064c35492a`) establishes the consolidated no-scroll map workspace and supporting context.
- Current Galaxy `bastion-chain-map-interaction-v1` (`40c20d1a-e083-4fe9-aaeb-488060e93e9c`) separates system-class stroke from heatmap fill/glow and preserves topology truth.
- Current Galaxy `bastion-attention-model-v1` (`7f908da4-fa47-4c90-815f-946155c23db9`) supplies the actionable lifecycle model.
- Current Galaxy `bastion-cross-domain-navigation-v1` (`44cb69f8-0733-4a15-9328-f1ff41d94bbc`) settles drawer/full-page handoff and traversal-aware breadcrumbs.
- The page labels capability coverage and actionability as explanation-bearing opportunity semantics; no market/ESI action is implied by the prototype.

## Visual-generation brief and mockup audit

The reference must depict a 16:9 desktop Bastion workspace with a dominant node-link map (not a fictional star chart), compact full-name character strip, small attention queue, selected-system drawer, filter chips, Relative/Fixed control, Operations HQ distinct from Market HQ, and a visible `PROTOTYPE - SAMPLE DATA - NOT LIVE` label. It must avoid tall scrolling, a duplicate Chain nav item, generic dashboard cards, and readable real operational data.

Audit: the generated reference centers one-system-per-node topology; keeps the right drawer local; shows independent semantic color channels in its legend; and makes the map materially larger than supporting panels.

## Interpretation boundary

Can change: exact layout, node glyphs, dense table columns, background asset, sample quantities, and control labels. Must preserve: consolidation, truthful topology, map dominance, local inspector filters, attention lifecycle, active-character compactness, Operations-vs-Market HQ distinction, and source/full-page handoff.
