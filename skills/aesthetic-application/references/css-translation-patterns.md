# CSS Translation Patterns

Use these compact installed-user patterns to translate canonical aesthetic dimensions into CSS. Pick patterns that preserve the loaded `aesthetics/<slug>.md` non-negotiables; do not add effects just because they are available.

## Palette

- Map palette guidance to role tokens first: background, surface, text, muted text, primary, secondary, accent.
- Preserve contrast behavior from the canonical entry: stark, low-contrast, neon-on-dark, muted earth, high-key pastel, etc.
- Flag risky pairs in the output rather than silently changing the aesthetic.

## Texture

- Grain/noise: pseudo-element overlay with low-opacity SVG/PNG noise or CSS `filter` where supported.
- Gloss/chrome: layered linear/radial gradients, high-contrast highlights, and controlled `box-shadow`/`text-shadow`.
- Paper/print: subtle background texture, off-white surfaces, uneven ink color, and restrained shadow.
- Digital artifact: scanlines, pixel steps, blur, displacement, or channel offsets, with reduced-motion alternatives.
- Minimal/no texture: explicitly say `none` instead of adding decorative noise.

## Shape

- Convert geometry to component defaults: button radius, card radius, input radius, icon container shape, and divider style.
- Use border thickness and corner behavior as aesthetic signals when color alone is insufficient.
- Avoid mixing incompatible geometry systems unless the blend conflict is intentionally resolved.

## Motion

- Translate motion character to duration and easing: snappy, languid, elastic, mechanical, cinematic, glitchy, or nearly still.
- Pair any motion-dependent aesthetic with `prefers-reduced-motion` fallbacks.
- Do not use infinite loops or high-flash effects unless the user explicitly requested an experiential surface and risks are flagged.

## Spatial conventions

- Choose a baseline spacing unit and density from the entry: sparse gallery, dense dashboard, poster-like stack, modular grid, scrapbook collage, radial composition, etc.
- Preserve hierarchy rules. Some aesthetics depend on strict Swiss-like grids; others depend on layered ephemera or maximal density.

## Cultural markers

- Render cultural markers as object vocabulary, typography choices, icon treatments, labels, and content tone.
- Keep sacred, regional, or subcultural references respectful and bounded by the canonical entry's ethical notes.
- Include avoid-list markers so the final UI does not drift into costume, stereotype, or adjacent aesthetics.
