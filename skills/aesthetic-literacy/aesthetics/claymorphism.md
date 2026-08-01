---
slug: claymorphism
label: Claymorphism
family: emerging-hybrid
era: 2022–present
aliases: ["clay UI", "puffy design", "soft 3D"]
status: canonical
evidence_level: limited
related: ["neumorphism", "glassmorphism", "material-design"]
subsets: []
---

# Claymorphism

Claymorphism is a born-digital soft-3D UI aesthetic where opaque matte cards and controls look puffy, inflated, and gently pressed from clay-like material. It developed as a practical successor to Neumorphism: instead of depending on a same-color page background, it uses self-contained inner and outer shadows that can sit on varied surfaces.

## Scope

Use Claymorphism for creative-tool marketing, children's or edtech products, wellness onboarding, approachable SaaS first-run flows, playful lifestyle modules, and small component systems where warmth matters more than density. Avoid it for data-heavy dashboards, critical healthcare/finance flows, enterprise admin tables, or interfaces where low-contrast pastel surfaces and shadow-only affordances would undermine precision or accessibility.

## 7-Dimension Profile

**Palette**: warm off-whites, cool gray-whites, powder blue, lavender, muted coral, sage, peach, and other softened pastels. Chroma stays gentle; pure black, pure white, and saturated primaries usually feel too hard.

**Type**: rounded friendly sans-serifs such as Nunito, Quicksand, Baloo 2, Fredoka, or similar system-rounded faces. Use regular-to-semibold weights, generous line height, and labels that feel legible rather than airy-thin.

**Texture**: opaque matte surfaces with the defining triple-shadow recipe: one outer cast shadow, one darker inset depth shadow, and one lighter inset highlight. The result should suggest modeling clay or Play-Doh, not glass, chrome, blur, or gradient plastic.

**Shape**: inflated cards, pill buttons, scooped inputs, circles, and very large radii, typically above 20px. Nothing should feel sharp, brittle, or architectural.

**Motion**: soft hover lift, squishy press states, bouncy toggle travel, and slow eased transitions. Motion should make controls feel elastic while preserving reduced-motion alternatives.

**Spatial**: generous padding, warm negative space, and shallow organic relief. Elements appear puffed from a shared soft material rather than floating as separate elevation planes.

**Cultural markers**: early-2020s Dribbble and CSS community soft-UI discourse, clay.css/claymorphism utility packages, the post-Neumorphism accessibility correction, puffy toy-like SaaS and children's-app visuals, and a broader reaction against hard-edged Neubrutalism.

## Non-Negotiables

**Non-negotiables**: triple shadow with outer + dark inset + light inset layers; border radius large enough to read as inflated; opaque matte surfaces; background-independent rendering; and a pastel-forward palette. A rounded pastel card without the inner/outer clay shadow system is only soft UI, not Claymorphism.

## Connotation

Claymorphism reads as contemporary, soft, friendly, and slightly childlike. Its nostalgia is material rather than period-specific: it borrows the tactile memory of craft clay while remaining a 2020s CSS-native interface style. Use that warmth deliberately; do not mistake playfulness for universal trust.

## Related / Subsets

- `neumorphism` is the direct predecessor: both are soft 3D, but Neumorphism depends on same-surface paired shadows while Claymorphism uses self-contained puffy inner shadows.
- `glassmorphism` is an adjacent 2020s soft-UI system, but it relies on transparency and blur rather than opaque clay relief.
- `material-design` shares card-based UI and depth language, but Material's elevation model is standardized and flatter where Claymorphism is inflated and toy-like.
- No canonical subset entries are defined yet.

## Frontend / UI Guidance

Keep Claymorphism focused on cards, onboarding choices, playful CTAs, app shells with low density, toy-like toggles, and friendly empty states. Pair the soft surfaces with explicit labels, focus rings, and contrast-tested text; do not let shadow depth be the only sign of interactivity. Reserve simpler components for dense tables, legal copy, search results, and critical forms.

## CSS Translation

- Color roles: `--clay-bg`, `--clay-surface`, `--clay-accent`, `--clay-shadow`, `--clay-highlight`, and `--clay-text`.
- Shadows: combine a soft outer cast shadow with darker and lighter inset shadows; deepen inset shadows for pressed states.
- Radius language: 24–50px card/button radii, pill CTAs, circular toggles, and scooped input wells.
- Effects: matte opacity, no blur, no transparent glass, no glossy chrome, and minimal gradients.
- Motion: eased lift on hover, squish on active states, and spring-like toggles with `prefers-reduced-motion` fallbacks.

## Typography / Fonts

Use rounded sans families such as Nunito, Quicksand, Baloo 2, Fredoka, or a friendly system sans. Body copy should remain readable at normal weights; avoid thin low-contrast labels that repeat Neumorphism's accessibility failure, and avoid sharp industrial type that fights the puffy material.

## Cultural / Ethical Notes

Claymorphism was framed as a production-friendlier answer to Neumorphism, but it still risks weak contrast and unclear affordance if softness overrides usability. Treat it as a limited-evidence, trend-sourced interface aesthetic; keep focus states, text contrast, target sizes, and reduced-motion behavior explicit.

## Anti-Patterns

- Calling any pastel rounded card Claymorphism without the triple-shadow clay surface.
- Using transparent blur, chrome gradients, or glass effects as the primary material.
- Applying the style to dense dashboards, records, or compliance flows.
- Removing outlines, labels, or contrast because the surface is meant to feel soft.
- Letting playful puffy controls undermine tasks that need authority or precision.
