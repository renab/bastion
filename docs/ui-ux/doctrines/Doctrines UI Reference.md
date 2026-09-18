# Doctrines UI Reference

![Doctrines workspace](doctrines-workspace.png)

## Product purpose and concept

Doctrines is the top-level capability library. A doctrine is the operational object; hulls and canonical fit variants are subordinate resources. The primary page is a dense doctrine library with fleet composition, role coverage, approved variants, eligible pilots, readiness, fit-engine provenance, and durable capability gaps. A doctrine detail uses an EVE-familiar hull/fit treatment and connects required hull, fit, skills, assets, and character readiness without claiming a live fitting action.

The fit workflow is deterministic: choose doctrine variant -> evaluate against the approved engine/version and character inputs -> identify specific deficits -> save gaps as durable proposals -> explicitly promote selected gaps to Procurement. Drawers show fit evidence, a pilot readiness comparison, or a gap proposal; full-page handoff goes to the doctrine, selected character, Inventory, or Procurement object.

### States and workflow

| State | Behavior |
| --- | --- |
| Approved and evaluable | show engine/data provenance and readiness by pilot |
| Engine or input stale | flag evidence freshness; do not present certainty |
| Missing fit/skill/hull | durable gap proposal, not automatic buying |
| No doctrines | focused creation/import onboarding with no empty fleet dashboard |

**Must not do:** make Fits a peer top-level domain; silently change an approved doctrine after engine updates; turn readiness deficits into purchased items; or flatten hull, fit, and pilot evidence into one status color.

## Source audit

- Current Galaxy `bastion-doctrines-domain-v1` (`c2ce5dbe-917a-4d37-99c7-909f8190bf8e`) sets doctrine-first hierarchy and readiness/capability scope.
- Current Galaxy `bastion-pyfa-update-pipeline-v1` (`64ad9e86-317b-47a4-8278-020e07b17e86`) requires attributable mechanics/engine provenance and no silent doctrine rewrites.
- Current Galaxy `bastion-procurement-logistics-workflow-v1` (`9a4b6f9c-c85d-4a9e-8c57-ec782bcc2fbd`) supplies explicit proposal promotion.

## Visual-generation brief and mockup audit

Create a 16:9 dense `Doctrines` desktop workspace with doctrine library left, selected doctrine center, subordinate hull and canonical fit variants, an eligible-pilot/readiness table, and a right `Capability Gap` inspector with `Create Procurement Proposal` rather than a buy button. Use sanitized sample names/data, EVE-familiar hull cards, engine provenance, and `PROTOTYPE - SAMPLE DATA - NOT LIVE`. Avoid a separate Fit navigation item, generic SaaS imagery, and ungrounded compatibility claims.

Audit: doctrine is visibly the organizing object; gaps are separate proposal objects; the selected fit has provenance; and the procurement handoff is explicit.

## Interpretation boundary

Can change: library columns, hull imagery, readiness visualization, and fit comparison layout. Must preserve: doctrine-first IA, deterministic/evidenced fit evaluation, durable gap proposals, and explicit procurement promotion.
