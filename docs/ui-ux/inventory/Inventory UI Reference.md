# Inventory UI Reference

![Inventory physical custody explorer](inventory-workspace.png)

## Product purpose and concept

Inventory answers where enterprise-controlled things physically are before asking what they are for. Its primary hierarchy is **System -> Structure/Station -> Hangar -> Container -> item stack**. Purpose, ownership, valuation, liquidity, doctrine allocation, industry allocation, and commitment remain orthogonal filters/metadata. A selected stack inspector identifies controlled quantity, committed quantity, custody evidence, reservations, related doctrine/industry/procurement context, and source/full-page handoff.

Movement planning is intent first: selecting quantities may create a move intent or allocation proposal. A committed transfer remains a distinct operational commitment with source, destination, owner, and state. Inventory never turns a planned move into observed custody and never treats in-transit/PI quantities as controlled on-hand inventory.

### States and workflow

| State | Behavior |
| --- | --- |
| Observed controlled stack | physical tree plus timestamp/source evidence |
| Reserved/committed | preserve free vs committed quantities and owning object |
| Unknown/stale location | mark data unavailable; do not infer a container |
| Empty physical location | a useful empty branch with incoming commitments, not a fake stack |

Workflow: traverse custody -> inspect stack -> filter by purpose/commitment -> create move intent/reservation -> explicitly commit via Logistics or Procurement -> observe final custody.

**Must not do:** organize primarily by project/purpose; equate allocated with moved; place Market HQ and Operations HQ into one synthetic location; or use estimated value as proof of custody.

## Source audit

- Current Galaxy `bastion-inventory-ui-v1` (`af4d24a9-a401-4bd1-a5ab-6d24a7b4e700`) approves physical-first hierarchy.
- Current Galaxy `bastion-procurement-logistics-workflow-v1` (`9a4b6f9c-c85d-4a9e-8c57-ec782bcc2fbd`) supplies order/load/staging semantics.
- Current Galaxy `bastion-pi-domain-v1` (`884e9970-22e6-4e5a-8c48-dcfcee0ddea2`) excludes planetary-chain quantities from controlled inventory until observed in custody.

## Visual-generation brief and mockup audit

Render a 16:9 `Inventory` physical explorer with a left tree labeled System, Structure/Station, Hangar, Container, a central item-stack table with free/committed/intent fields, and a selected-stack right inspector plus compact move-intent drawer. Include incoming/staged/in-transit distinctions, prototype sample labels, and a small topology-aware location cue. Avoid project-first cards, a decorative logistics lifecycle banner, and untraceable values.

Audit: the hierarchy is unmistakably physical; commitments are overlays rather than branches; the inspector separates observed, free, reserved, and planned states; and the action creates intent rather than pretending it moves assets.

## Interpretation boundary

Can change: tree depth display, item art, table columns, and custody evidence formatting. Must preserve physical-first navigation, orthogonal metadata, observation boundary, and intent-versus-commitment distinction.
