# Bastion branding assets

These assets translate the approved Naffin Enterprises logo references into reusable Bastion UI artwork. All production files have transparent backgrounds.

## Palette

| Role | Value |
| --- | --- |
| Corporation blue | `#3054CD` |
| Corporation gold | `#CD8A30` |
| Dark neutral | `#1A1A1A` |

Silver and pale-blue tints are supporting wordmark colors. Semantic UI colors—danger, warning, success, and opportunity heat—remain independent of the corporation palette and must not be inferred from the logo colors.

## Inventory and intended use

- `logos/svg/naffin-emblem.svg` — preferred self-contained emblem for sidebar navigation and compact headers. It embeds the raster wormhole core while retaining vector compass and orbital geometry.
- `logos/svg/naffin-lockup.svg` — preferred self-contained full lockup. It embeds the raster wormhole core while retaining vector frame and path-based lettering; no local font is needed.
- `logos/svg/naffin-lockup-hybrid.svg` — compatibility copy of the self-contained hybrid lockup.
- `logos/svg/naffin-emblem-vector.svg` and `logos/svg/naffin-lockup-vector.svg` — simplified all-vector alternatives for workflows that prohibit embedded raster content.
- `logos/raster/wormhole-core-2048.png` — transparent 2048 px raster core used by the hybrid SVG.
- `logos/raster/naffin-emblem-{64,128,256,512}.{png,webp}` — compact UI and favicon-like exports. Use 64 or 128 px at their native dimensions; choose 256 or 512 px for high-density displays.
- `logos/exports/naffin-lockup-1600.{png,webp}` — documentation and splash exports at 1600 px wide.
- `logos/references/naffin-emblem-approved-reference.png` and `logos/references/naffin-full-lockup-approved-reference.png` — preserved approved source references; do not use these as runtime UI assets.

## Selection guide

| Context | Asset |
| --- | --- |
| Sidebar / compact navigation | `naffin-emblem.svg` or the closest native-size emblem raster |
| Application header | `naffin-lockup-hybrid.svg` when space permits; `naffin-emblem.svg` in compact layouts |
| Full splash / documentation | `naffin-lockup-hybrid.svg` or `naffin-lockup-1600.png` |
| Favicon-like use | `naffin-emblem-64.png` or `naffin-emblem-64.webp` |
| Vector-only delivery | `naffin-emblem-vector.svg` or `naffin-lockup-vector.svg` |

## Scaling and implementation notes

- Preserve the aspect ratio and clear space around the cardinal markers. Do not stretch, recolor, crop through, or place the mark on a visually busy field without contrast testing.
- Prefer SVG in the application. Use the provided raster size nearest to the rendered size rather than downsampling the 1600 px lockup at runtime.
- The production SVGs intentionally combine vector geometry with an embedded PNG data URI so they remain self-contained while preserving the turbulent, luminous appearance of the approved reference. `wormhole-core-2048.png` remains available separately for compositing and regeneration.
- The wormhole core is safe for moderate UI scaling and downscaling. Do not scale it beyond its 2048 x 2048 source resolution for final output.
- At 32–64 px, fine orbital beads and gradients naturally simplify. Use the emblem-only asset; do not use the full lockup at those sizes.
- The full-vector wormhole is an intentionally simplified stylization for resolution-independent use. Choose the hybrid when close visual fidelity to the approved luminous center matters more than an all-vector file.

## Reproduction

`tools/generate_brand_assets.py` records the deterministic vector construction and raster export process. After the initial extraction, it reuses the isolated transparent core stored in this repository.
