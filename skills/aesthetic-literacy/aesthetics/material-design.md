---
slug: material-design
label: Material Design
family: digital-internet-native
era: 2014–present living Google design system
aliases: ["Material", "Material UI", "MDL"]
status: canonical
evidence_level: limited
related: ["flat-design", "skeuomorphism", "neumorphism", "glassmorphism"]
subsets: []
---

# Material Design

Material Design is Google’s adaptable design system and visual language, combining grid structure, component doctrine, controlled depth, role-based color, and meaningful motion into coherent cross-device digital experiences. It should read as a disciplined system, not just cards and shadows copied into any app.

## Scope

Use Material Design for Android applications, enterprise dashboards, admin consoles, utility tools, content-heavy products, and teams that need consistent components, accessible interaction patterns, and scalable system governance. Avoid it when a project needs luxury distinctiveness, experimental editorial expression, anti-system personality, or a visual identity that should not read as Google-like or app-default.

## 7-Dimension Profile

**Palette**: structured theme colors, primary/secondary accents, surface/content roles, tonal palettes, dynamic color variants, strong separation between background, surface, text, error, and state layers. Arbitrary decorative palettes weaken Material’s system logic.

**Type**: systematized UI hierarchy, legible sans labels, predictable scale ramps, app-bar titles, compact metadata, and tabular utility text. Typography serves component clarity rather than expressive display.

**Texture**: clean opaque surfaces, controlled elevation, state layers, ripples, cards, chips, dialogs, and subtle dividers. Material avoids photoreal mimicry while still preserving affordance through paper-like surface behavior.

**Shape**: cards, floating action buttons, dialogs, lists, chips, navigation rails, sheets, rounded but disciplined controls, pill filters, and modular containers governed by shared tokens.

**Motion**: responsive transitions, state continuity, meaningful choreography, ripple feedback, shared-axis movement, container transforms, and restrained feedback tied to navigation or interaction state.

**Spatial**: grid-based layout, 8dp-like rhythm, clear alignment, component hierarchy across breakpoints, card stacks, app bars, segmented content regions, and explicit surface relationships.

**Cultural markers**: Google I/O 2014 launch, Android and Google product ecosystem influence, open-source component kits, Material 3 / Material You, design-token governance, and enterprise/product-team adoption.

## Non-Negotiables

**Non-negotiables**: coherent component system + structured surface hierarchy + role-based color + legible sans UI type + meaningful state/motion feedback. Cards, shadows, or ripples alone do not make an interface Material if spacing, state, and component roles are inconsistent.

## Connotation

Material Design is a living system rather than a nostalgic revival. Its ubiquity makes it safe, familiar, and scalable, but also potentially generic. In contemporary work it often connotes Android/product-team discipline, system maturity, and Google-adjacent defaultness unless customized carefully.

## Related / Subsets

- `flat-design` helped normalize simplified digital surfaces, but Material reintroduces controlled depth, state logic, and component doctrine.
- `skeuomorphism` is the historical excess Material moved away from; Material keeps affordance without photoreal material skins.
- `neumorphism` also uses depth cues, but Material’s depth is standardized and scalable where Neumorphism is subtle, same-surface, and fragile.
- `glassmorphism` is a later alternative using translucent blur rather than opaque paper-and-ink surfaces.
- Material You / Material 3 is treated here as a current internal evolution, not a separate canonical subset entry.

## Frontend / UI Guidance

Adopt Material as a coherent language: define tokens, hierarchy, elevation/state logic, spacing rhythm, typography scale, and component roles together. Use cards, chips, dialogs, app bars, lists, and FABs only where they clarify tasks. If customizing heavily, preserve predictable focus states, color roles, and motion semantics.

## CSS Translation

- Color roles: `--md-primary`, `--md-secondary`, `--md-surface`, `--md-surface-variant`, `--md-on-surface`, `--md-error`, `--md-outline`.
- Borders/dividers: tokenized outlines, surface variants, list separators, and state-layer overlays rather than arbitrary decoration.
- Radius language: component-governed radius for cards, chips, sheets, and controls; avoid one-off handcrafted geometry that breaks system coherence.
- Effects: elevation shadows, state-layer opacity, ripple feedback, and opaque surfaces; avoid photoreal texture or gratuitous gloss.
- Layout: app bars, navigation rails, card grids, list/detail screens, drawers, dialogs, and breakpoint-aware product scaffolds.
- Motion: container transforms, shared-axis transitions, ripples, pressed/hover/focus state changes, and `prefers-reduced-motion` alternatives.

## Typography / Fonts

Use Roboto, Roboto Flex, Google Sans where appropriate, or comparable highly legible sans-serif UI families with explicit type scales. Keep weights, line-height, and label sizing consistent across components. Avoid expressive display type driving the core app structure.

## Cultural / Ethical Notes

Material’s maturity can improve accessibility and consistency, but copying it without contrast checks, focus states, or product-fit can produce generic and inaccessible interfaces. Treat the official system as a governance model, not a cosmetic kit. Be careful when a brand should not appear Google-like or when platform conventions conflict with the desired product identity.

## Anti-Patterns

- Copying card shadows without adopting spacing, hierarchy, state, or component roles.
- Treating every modern app with rounded cards as Material Design.
- Overusing motion to showcase polish rather than explain state changes.
- Weak surface/text contrast caused by careless dynamic color or brand overrides.
- Mixing Material components with unrelated bespoke geometry until the system loses predictability.
