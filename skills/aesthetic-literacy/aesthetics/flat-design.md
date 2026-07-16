---
slug: flat-design
label: Flat Design
family: digital-internet-native
era: 2010–2019 peak GUI simplification; absorbed into design-system defaults afterward
aliases: ["flat UI", "metro-inspired", "Flat 2.0"]
status: canonical
evidence_level: limited
related: ["skeuomorphism", "material-design", "corporate-memphis", "swiss-international"]
subsets: []
---

# Flat Design

Flat Design is a minimalist interface language that removes photoreal surface simulation, bevels, heavy shadows, and decorative texture so color, typography, spacing, and icon clarity carry the interface. Its best translations are disciplined reductions that preserve affordance, not blank surfaces that make every control ambiguous.

## Scope

Use Flat Design for dashboards, SaaS tools, admin panels, documentation, operating-system-like utilities, and content-heavy apps where clarity, low visual noise, and efficient hierarchy matter. Avoid it when a project needs tactile luxury, emotional storytelling, high material richness, or when removing all depth would make buttons, links, and labels hard to distinguish.

## 7-Dimension Profile

**Palette**: clean solid color fields, crisp white or neutral backgrounds, direct accent/background separation, Metro-like bright blocks, pastel brand systems, and monochrome utility palettes. Avoid faux-material gloss, heavy gradients, or texture-as-depth.

**Type**: clear sans-serif hierarchy, strong scale contrast, large labels replacing decorative chrome, icon-plus-label systems, bold section headers, and tabular utility text. Typography becomes a primary affordance and hierarchy tool.

**Texture**: almost none; flat fills, thin outlines, simple separators, and icon clarity dominate. Later Flat 2.0 variants may use light shadows or subtle dividers, but they remain functional affordance cues rather than material simulation.

**Shape**: rectangles, circles, simple icons, flat buttons, tiles, card hybrids, pill toggles, and thin-rule segmentation. Shapes should be direct and unembellished, with rounding used for system consistency rather than plush tactility.

**Motion**: functional transitions, simple easing, direct state changes, slide reveals, tab transitions, and lightweight microfeedback. Motion should clarify navigation and state rather than compensate for weak hierarchy.

**Spatial**: clean grouping, generous spacing, tile systems, card grids, direct dashboard panels, and visible hierarchy through spacing and color instead of ornament or simulated depth.

**Cultural markers**: anti-skeuomorphic simplification, modern GUI cleanup, “content first” rhetoric, Metro-era tiles, iOS 7-era visual flattening, startup minimalism, and 2010s OS/app redesign waves.

## Non-Negotiables

**Non-negotiables**: reduced/no material simulation + solid color fields + simplified icons + typography/spacing-led hierarchy + clear affordances after ornament is removed. If controls become indistinguishable from static labels, the design has become over-flat rather than flat.

## Connotation

Flat Design was historically a reaction against skeuomorphic excess, especially in early-2010s operating systems and app redesigns. Today it often reads less like a named aesthetic and more like the baseline grammar of modern UI. Use it intentionally when reduction and clarity are the point; otherwise it can feel generic, underdesigned, or over-sanitized.

## Related / Subsets

- `skeuomorphism` is the direct conceptual opposite: material mimicry and tactile reference versus deliberate reduction.
- `material-design` shares simplification but reintroduces structured depth, component doctrine, and motion systems.
- `corporate-memphis` overlaps through flat color and reduced texture, but it is illustration/brand-world focused rather than interface-structure focused.
- `swiss-international` is a print-era precursor for grid, hierarchy, and typographic discipline, but Flat Design is native to screens and interaction affordances.
- Metro, iOS 7 Flat, Holo, and Flat 2.0 are useful internal variants but not separate canonical subset entries here.

## Frontend / UI Guidance

Start by proving the interaction hierarchy works without ornament: button states, links, focus, selection, disabled states, and content groups must remain obvious. Use spacing, labels, color contrast, icon clarity, and predictable component shapes to replace the cues removed with shadows and textures. When adding depth back, keep it subtle and functional.

## CSS Translation

- Color roles: `--flat-bg`, `--flat-surface`, `--flat-text`, `--flat-muted`, `--flat-accent`, `--flat-danger`, `--flat-success`.
- Surfaces: solid fills, simple boundaries, low or no shadow, and direct hover/focus states.
- Borders/dividers: thin rules, color-block segmentation, outline buttons, and high-contrast focus rings.
- Radius language: 0–4px for historical pure flat; moderate system radius is acceptable for contemporary Flat 2.0 if hierarchy remains crisp.
- Layout: tile grids, simple cards, direct nav bars, settings panes, and content-first vertical grouping.
- Motion: short functional transitions with `prefers-reduced-motion` support; avoid cinematic easing as a substitute for affordance.

## Typography / Fonts

Use legible screen sans-serifs such as Segoe UI, Roboto, Helvetica Neue, Inter, Open Sans, or Lato. Thin weights can quote early flat design, but body and control text should remain readable. Use scale, weight, color, and spacing to create hierarchy; avoid ornamental type that tries to replace missing interaction cues.

## Cultural / Ethical Notes

Flat Design can make interfaces cleaner, but it can also hide affordances and over-rely on color. Preserve WCAG contrast, visible focus states, and explicit labels rather than assuming minimalism equals usability. When referencing historical platform styles such as Metro or iOS 7, be specific rather than presenting all modern minimal UI as the same movement.

## Anti-Patterns

- Deleting all depth without replacing it with clear hierarchy and control affordance.
- Low-contrast ghost text, outline-only buttons, or icon-only controls with no accessible labels.
- Treating every minimal interface as Flat Design regardless of interaction logic.
- Reintroducing gloss, leather, stitched texture, or photoreal material cues while still calling it flat.
- Using motion theatrically to make an otherwise ambiguous interface feel designed.
