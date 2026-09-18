# Procurement / Logistics UI Reference

![Procurement and logistics workflow workspace](procurement-logistics-workspace.png)

## Product purpose and concept

Procurement / Logistics translates durable needs into explicit acquisition and movement work. A source domain may create a proposal, but it remains planning until an operator promotes it into an approved requirement. Purchase Orders represent what is bought; Transport Loads represent how acquired goods move or stage. A PO may feed several loads and a load may allocate compatible lines across several orders. Status belongs to each object, not to a decorative global lifecycle banner.

The page is a requirements-and-orders workboard with a selected-object inspector: proposal rationale, approval evidence, PO line economics, issued-by character, Market HQ assumptions, acquisition state, load allocation, route/staging, and receipt/custody handoff. It supports skillbook sourcing comparison and explicit acceptance of remote injection versus Market HQ acquisition. Buttons create proposals, approve requirements, issue a PO, assemble a load, or record acquired/staged state according to the current object.

### States and workflow

Proposal -> approved requirement -> purchase order -> acquired -> assigned to transport load -> in transit/staged -> satisfied after observed custody. These are object-local status transitions, not automatic cross-domain truth.

Blocked states include price/market depth unavailable, approval needed, unassigned load, capacity/risk constraint, and unobserved receipt. A no-work state shows create/import a proposal, not an empty procurement dashboard.

**Must not do:** directly purchase from a doctrine/industry/skill-plan recommendation; conflate PO and load; claim acquisition proves arrival; or treat Market HQ as Operations HQ.

## Source audit

- Current Galaxy `bastion-procurement-logistics-workflow-v1` (`9a4b6f9c-c85d-4a9e-8c57-ec782bcc2fbd`) settles proposal-to-execution, provisional Amarr Market HQ, skillbook economics, and PO/load distinction.
- Current Galaxy `bastion-surface-refinement-v1` (`33659d9e-c51d-4916-b0a5-b28ee9813f0e`) explicitly rejects the decorative global lifecycle banner.
- Current Galaxy `bastion-cross-domain-navigation-v1` (`44cb69f8-0733-4a15-9328-f1ff41d94bbc`) supplies cross-domain drill-through.

## Visual-generation brief and mockup audit

Render a 16:9 dense `Procurement / Logistics` workboard with separate lists for proposals, approved requirements, purchase orders, and transport loads. Open a right PO inspector showing line items, issued-by field, Market HQ, acquisition, and load allocations. Include a small explicit `Approve Requirement` action and a `Create Transport Load` action, not a single global lifecycle ribbon. Label all sample data as prototype/not live.

Audit: PO and load are visibly distinct objects; a load can allocate multiple PO lines; status is local to rows/inspectors; Market HQ is named separately from Operations HQ; no purchase is implied without approval.

## Interpretation boundary

Can change: board/list arrangement, object badges, route representation, and line-item economics. Must preserve proposal approval boundary, PO/load separation, object-local state, physical receipt/custody handoff, and Market HQ distinction.
