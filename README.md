# Bastion

**Bastion** is the unified operational control center for **Naffin Enterprises / Outbound Flight** in EVE Online.

The project is intended to bring wormhole operations, chain intelligence, doctrines, characters, inventory, trade, procurement, logistics, industry, planetary interaction, finance, and operational knowledge into one coherent interface.

## Status

Bastion is currently in active product and architecture design.

The repository presently serves as the durable home for:

- product design
- UI/UX work
- branding and visual assets
- interactive prototypes
- architecture decisions
- migration planning
- future implementation

The application architecture and implementation stack are still being refined.

## Product Goals

Bastion is being designed for a single human operator managing a multi-character wormhole enterprise.

Key goals include:

- reduce context switching between EVE, external tools, notes, and operational data
- present the live wormhole chain as the primary operational workspace
- surface opportunity, readiness, logistics, and economic context together
- preserve accurate source/provenance and historical state
- support doctrine and capability planning using actual character skills and assets
- make inventory, procurement, industry, PI, and finance part of the same operating model
- remain familiar to EVE players without reproducing unnecessary EVE UI friction

## Major Domains

Current first-class product areas include:

- Executive Brief
- Chain & Opportunities
- Accounts & Characters
- Doctrines
- Inventory
- Market / Trade
- Procurement & Logistics
- Industry
- Planetary Interaction
- Finance
- Knowledgebase
- Analytics

Settings is a secondary administration surface behind the application cog rather than a primary product domain. Character ESI authorization belongs to Accounts / Characters; Settings contains only organization, system integration, preference, and advanced controls.

These are still subject to refinement as product design continues.

## UI Direction

Bastion uses EVE Online's visual and interaction language as a familiarity prior:

- dark operational interface
- compact information-dense panels
- EVE-familiar identity treatment
- restrained translucent surfaces
- clear hierarchy and contextual drill-down
- corporation branding used as a theme layer

The Naffin Enterprises prototype palette is currently:

- Primary: #3054CD
- Secondary: #CD8A30
- Dark: #1A1A1A

Production Bastion is intended to consume the corporation's live branding palette from EVE-supported data surfaces where available.

Industry's approved visual-direction references are maintained in [docs/ui-ux/industry/Industry UI Reference.md](docs/ui-ux/industry/Industry%20UI%20Reference.md). They guide product language and interaction hierarchy, not final schema or literal implementation details.

## Branding

The current branding direction centers on a blue/gold wormhole emblem representing:

- wormhole operations
- navigation
- logistics
- connection
- exploration

Brand assets live under:

assets/branding/

The approved high-resolution transparent PNG artwork is the visual source of truth for the full corporate lockup. The emblem may also be used independently at smaller interface sizes.

## Inventory UX

The approved default Inventory hierarchy is:

System → Structure/Station → Hangar → Container → Items

The physical hierarchy is the primary browse model.

Purpose, commitment, valuation, liquidity, doctrine allocation, industry allocation, and other operational metadata remain orthogonal to physical location.

## Chain Map

The chain map is intended to be the dominant operational surface.

Key design principles:

- one node = one real solar system
- edges = real wormhole connections
- truthful topology rather than fake physical star-map geometry
- draggable nodes
- zoomable and pannable canvas
- preserved manual layout
- opportunity heatmap and filters
- selected-system detail drawer
- Operations HQ visually distinct from Market HQ

## Data / Migration

Bastion is the successor platform to the earlier Galaxy-based operational ledger.

Galaxy is migration input, not a permanent production dependency.

The intended migration model is:

- mature concepts → deterministic Bastion domain models
- historical/superseded state → Bastion-native history/version/event structures
- useful evidence/provenance → Bastion-owned evidence and provenance
- obsolete/transitional material → deliberately archived or discarded

Nexum remains the authoritative live source for wormhole topology and current mapped chain state.

ESI/SDE remain authoritative upstream sources for supported EVE telemetry and static game data.

## Development Principles

- use mature, well-known, free/open-source UI frameworks and component libraries
- use a real CSS framework/design system
- avoid ad-hoc inline styling
- do not reimplement commodity components unnecessarily
- reserve custom engineering for Bastion-specific operational workflows
- preserve accessibility and keyboard usability
- keep domain logic deterministic where possible
- distinguish current fact, forecast, history, and evidence

## Repository Layout

docs/        Product, architecture, UI/UX, prototype, and migration documentation
assets/      Branding, logos, mockups, screenshots, and other visual resources
prototype/   Interactive prototype work
app/         Future production frontend and backend
data/        Sanitized sample data and test fixtures
scripts/     Project tooling and helper scripts

The current buildless prototype is in `prototype/dist/`. Open `prototype/dist/index.html` directly or serve that directory with any local static web server.

## Security / Public Repository Policy

This repository is public.

Do not commit:

- ESI refresh tokens
- OAuth/client secrets
- API keys
- credentials
- private operational exports
- live private financial data
- private corp asset dumps
- confidential account or character authentication material

Use sanitized sample data and fixtures for examples and testing.

## License

License to be selected and confirmed before code reuse/distribution assumptions are made.
