# Bastion branding assets

The approved Naffin Enterprises transparent PNG artwork is the canonical Bastion branding source. Production variants are direct, aspect-preserving resizes of that artwork rather than reconstructed vector approximations.

## Palette

| Role | Value |
| --- | --- |
| Corporation blue | `#3054CD` |
| Corporation gold | `#CD8A30` |
| Dark neutral | `#1A1A1A` |

Semantic UI colors—danger, warning, success, and opportunity heat—remain independent from corporation brand colors.

## Production inventory

- `logos/raster/naffin-emblem-master.png` — canonical transparent emblem at the approved source resolution.
- `logos/raster/naffin-emblem-{64,128,256,512}.{png,webp}` — direct compact exports for navigation and favicon-like uses.
- `logos/exports/naffin-lockup-master.png` — canonical transparent full lockup at the approved source resolution.
- `logos/exports/naffin-lockup-1600.{png,webp}` — direct 1600 px documentation and splash exports.
- `logos/references/naffin-emblem-approved-reference.png` and `logos/references/naffin-full-lockup-approved-reference.png` — preserved supplied references.
- `logos/svg/` — deprecated reconstruction experiments retained only for design history. Do not use these in Bastion.

## Selection guide

| Context | Asset |
| --- | --- |
| Sidebar / compact navigation | Closest native-size `naffin-emblem` PNG/WebP |
| Application header | `naffin-lockup-master.png`, or `naffin-emblem-master.png` in compact layouts |
| Full splash / documentation | `naffin-lockup-master.png` or `naffin-lockup-1600.png` |
| Favicon-like use | `naffin-emblem-64.png` or `naffin-emblem-64.webp` |

## Scaling guidance

- Preserve transparency, aspect ratio, and clear space around the cardinal markers.
- Do not crop the compass points, wordmark, divider, or tagline.
- Use the provided raster size nearest to the rendered size.
- Avoid upscaling beyond the master artwork's native dimensions except for the documented 1600 px convenience export.
- At 32–64 px, use the emblem alone; the full lockup is not intended to remain legible at favicon sizes.

## Reproduction

`tools/generate_brand_assets.py` regenerates production raster variants directly from the preserved approved references.
