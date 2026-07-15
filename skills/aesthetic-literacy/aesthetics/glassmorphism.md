---
slug: glassmorphism
label: Glassmorphism
family: emerging-hybrid
era: 2020–2022
aliases: []
status: canonical
evidence_level: limited
related: ["neumorphism", "organic-digital", "y2k"]
subsets: []
---

# Glassmorphism

Glassmorphism is a UI-native frosted-glass style built from transparency, blur, luminous borders, and layered depth. Its core premise is not “blur everything,” but a controlled relationship between a visible background field and a translucent foreground surface that remains readable.

## Scope

Use Glassmorphism for dashboards, onboarding panels, login shells, translucent navigation, settings cards, modal surfaces, and premium app moments where ambient depth helps the interface feel light. It is strongest on bounded surfaces with clear hierarchy; it weakens when every layer becomes equally transparent.

The aesthetic depends on background interaction. If a panel is fully opaque, or if the backdrop is not meaningfully visible through it, the result may be soft modern UI but not glassmorphism.

## 7-Dimension Profile

**Palette**: Colorful gradients, atmospheric color fields, pale blues, violets, pinks, cool neutrals, and white or near-white foreground chrome. Use enough panel opacity or overlay support to keep text contrast stable.

**Type**: Clean sans-serif labels and headings, semibold white or dark copy depending on the pane, compact metadata, and restrained uppercase tags. Ornamental type competes with the surface effect and should stay out of core UI.

**Texture**: Blur, translucency, frosted overlays, soft internal glow, light borders, noise-free depth, shadowed floating cards, and transparent status chips. The texture is optical and layered rather than tactile or distressed.

**Shape**: Rounded cards, floating panes, pill inputs, soft-corner modal shells, stacked overlays, media tiles, and translucent nav bars. Sharp brutalist edges should not dominate.

**Motion**: Smooth depth transitions, subtle parallax, hover lift, focus glow, animated background gradients, reveal fades, and cursor-reactive highlights. Avoid constant blur pulses or drifting layers that disorient users.

**Spatial**: Foreground translucent cards over visible background color or imagery, clear z-depth separation, dashboard widgets, login surfaces, onboarding panes, floating utility panels, and enough spacing for each layer to read.

**Cultural markers**: Frosted panels, colorful ambience, premium app polish, depth through transparency, finance/productivity dashboards, onboarding cards, and translucent navigation chrome.

## Non-Negotiables

**Non-negotiables**:

- Translucent foreground surfaces with visible backdrop interaction.
- Blur or frosted-glass treatment paired with light borders or separation support.
- Layered z-depth: foreground panes over ambient color, imagery, or gradients.
- Legibility controls; without readable content, the glass effect fails as UI.

## Connotation

**Mode:** contemporary revival.

Glassmorphism reads as premium, airy, app-native, and slightly futuristic, with moderate fatigue from early-2020s overuse. It still works when used for purposeful depth rather than novelty blur.

## Related / Subsets

- `neumorphism` is another surface-led UI trend, but it relies on soft extruded shadows on same-color surfaces rather than transparency and backdrop interaction.
- `organic-digital` overlaps in gradients and softness, but Organic Digital is biomorphic and shape-led while Glassmorphism is pane-led.
- `y2k` can share glow and synthetic polish, but Y2K is denser, shinier, and chrome-heavy.

No canonical subsets are defined yet.

## Frontend / UI Guidance

Use glass surfaces to group information without fully blocking ambient context: account cards over gradient backgrounds, onboarding panels, lightweight nav bars, media overlays, or dashboard widgets. Keep dense tables, long paragraphs, and critical forms on more opaque panes.

Set foreground/background contrast intentionally. Test the exact background behind each translucent component instead of assuming white text over blur will pass.

## CSS Translation

- Color roles: `--glass-bg`, `--glass-border`, `--ambient-blue`, `--ambient-violet`, `--ambient-pink`, `--text-on-glass`, and `--shadow-soft`.
- Borders/dividers: 1px translucent white or dark strokes, inner highlights, and subtle separators.
- Radius language: soft rounded cards, pills, modal shells, and floating panes.
- Effects: `backdrop-filter: blur(...)`, semi-transparent backgrounds, layered box-shadows, gradient backdrops, and restrained glow.
- Layout: foreground pane over color field, separated layer stacks, floating nav, dashboard card grids, and modal overlays.
- Motion: hover lift, focus glow, reveal fade, slow gradient shift, and parallax only with reduced-motion support.

## Typography / Fonts

Use clean sans-serif systems with sufficient weight and size to survive blurred or luminous surroundings. Avoid decorative display faces and ultra-light type on low-opacity panes; the typography should clarify the surface, not add another competing effect.

## Cultural / Ethical Notes

Many showcase examples understate accessibility risk. Treat contrast and motion as part of the aesthetic implementation, not as cleanup afterward. Avoid hiding essential state solely in transparency, shimmer, or depth changes.

## Anti-Patterns

- Stacking many translucent layers until hierarchy disappears.
- Relying on blur as the only separator for dense data.
- White text over busy gradients without opacity, scrim, or contrast support.
- Opaque cards with a token blur value but no visible backdrop interaction.
- Constant parallax, blur pulsing, or glass drift that ignores reduced-motion settings.
