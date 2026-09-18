# Knowledgebase UI Reference

![Knowledgebase evidence workspace](knowledgebase-workspace.png)

## Product purpose and concept

Knowledgebase is Naffin Enterprises' searchable institutional memory: canonical internal knowledge, direct observations, authored guides/notes, and external research evidence with confidence and provenance. It is not a generic wiki list or an inherited `Sites` concept. It is both a search/retrieval system and a Markdown authoring/viewing environment; structured facts/evidence remain separately addressable when deterministic semantics matter.

The primary surface is search-first: query facets and result kinds left, selected rendered Markdown center, evidence/fact/provenance inspector right. Editing opens a Markdown-first composition surface with preview and explicit revision/save semantics. A source drawer exposes evidence lineage, confidence, extraction/observation date, supersession, and links to related operational objects.

### States and workflow

Search -> inspect rendered entry -> inspect evidence -> open canonical source or edit a Markdown-backed note -> save revision -> evidence/fact links remain distinct. Empty state teaches search, create note, or record observation; unavailable source marks a coverage gap rather than deleting the conclusion.

**Must not do:** flatten accepted knowledge and raw evidence into indistinguishable notes; use generic wiki cards; bury authoring behind Settings; or present unverified external research as a canonical conclusion.

## Source audit

- Current Galaxy `bastion-knowledgebase-domain-v1` (`5348ffbe-9fd6-4d9b-9e0a-f6bf1d3a0930`) establishes searchable institutional knowledge, evidence, confidence, and provenance.
- Current Galaxy `bastion-knowledgebase-markdown-authoring-v1` (`e5fdee5e-9f55-407b-be7d-225706f6992f`) establishes Markdown authoring/viewing with separate structured semantics.
- Current Galaxy `bastion-cross-domain-navigation-v1` (`44cb69f8-0733-4a15-9328-f1ff41d94bbc`) supplies inspection and canonical-source handoff.

## Visual-generation brief and mockup audit

Render a 16:9 `Knowledgebase` desktop workspace with search/facets, result list, richly rendered sample Markdown note with a small table, related facts/evidence, and a provenance inspector. Include a clear `Edit Markdown` action and source/full-page controls. Label prototype/sample/not live. Avoid wiki-card landing pages, generic hero art, and `Sites` terminology.

Audit: the rendered Markdown note is central; provenance remains a dedicated inspector; result kinds separate observation, guide, research, and conclusion; authoring is first-class.

## Interpretation boundary

Can change: search facets, editor split view, typography, and entry taxonomy. Must preserve search-first retrieval, Markdown as a first-class surface, evidence/provenance separation, and revision-aware interpretation.
