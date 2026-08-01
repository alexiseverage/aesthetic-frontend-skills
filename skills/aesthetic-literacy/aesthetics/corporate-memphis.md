---
slug: corporate-memphis
label: Corporate Memphis / Illustration Flat
family: emerging-hybrid
era: 2017–2022 (now fatigued)
aliases:
  - Alegria
  - Big Tech Art Style
status: canonical
evidence_level: limited
related:
  - flat-design
  - material-design
  - web-2-gloss
subsets: []
---

## Scope

Corporate Memphis / Illustration Flat is the late-2010s product-brand illustration language associated with Big Tech, Facebook’s Alegria rollout, SaaS onboarding, help centers, and scalable friendliness. Use it for historical analysis, intentionally generic startup satire, or carefully limited empty states and onboarding art. It is fatigued as a primary brand system and should not be applied where authentic specificity, serious civic messaging, or dense product comprehension matters.

## 7-Dimension Profile

**Palette**: Bright flat solids, coral, blue, yellow, green, sage, mustard, sky blue, broad skin-tone abstractions, and white backgrounds. Colors are cheerful and shadowless but must still meet contrast requirements when paired with text or CTAs.

**Type**: Neutral geometric or neo-grotesque sans-serif that stays secondary to illustration. Rounded startup sans and clean product-marketing headers are common; ornate display type is off-model.

**Texture**: Flat vector fills, little or no texture, no shadows, and only sparse line accents or very light vector grain. Painterly rendering and metallic depth break the style.

**Shape**: Blob limbs, faceless abstract people, rounded geometric scenery, oversized plants and devices, simplified office props, circles, arcs, and exaggerated gestures.

**Motion**: Friendly lightweight loops, gentle SVG bobbing, onboarding drifts, simple card reveals, and decorative motion that never carries essential product meaning.

**Spatial**: Generous whitespace with one hero illustration or a few spot illustrations supporting a product narrative. Works in marketing panels, empty states, and onboarding; weak in dense dashboards.

**Cultural markers**: Faceless vector humans, abstract diversity signaling, single-leaf plant motifs, giant device props, startup help-center optimism, Big Tech-safe friendliness, and SaaS explainer art.

## Non-Negotiables

**Non-negotiables**: flat illustration; abstract faceless blob figures; desaturated-to-bright corporate palette; product-marketing or onboarding context; visible fatigue risk.

## Connotation

**Connotation**: Approachable startup optimism, institutional safety, and generic friendliness. Because of overuse, it often now connotes bland platform paternalism, shallow inclusivity signaling, and “generic SaaS” rather than fresh playfulness.

## Related / Subsets

- `flat-design` — shares reduced surfaces, but Flat Design is a component/system language while Corporate Memphis is illustration-led brand-world language.
- `material-design` — can coexist structurally around these illustrations, but Material governs interface components rather than decorative product scenes.
- `web-2-gloss` — near-opposite tone: shadowless vector flatness versus shiny rounded reflections.
- Subsets include Alegria-style product illustration, SaaS empty-state illustration, and abstract diversity illustration.

## Frontend / UI Guidance

Use it as supporting illustration, not as the interface itself. Keep figures decorative and avoid placing critical labels on busy illustration backgrounds. Pair flat art with real product screenshots, concrete task diagrams, or strong copy when comprehension matters. Treat fatigue as an implementation constraint: a little can soften an empty state, while a full brand world can feel dated immediately.

## CSS Translation

- Palette tokens: `--cm-coral: #ff6f61; --cm-sage: #88b08b; --cm-mustard: #f2c94c; --cm-sky: #56ccf2; --cm-ink: #253044;`.
- Build illustration with SVG or flat CSS shapes; avoid `box-shadow`, gradients, and texture-heavy filters.
- Keep composition airy: `display: grid; gap: clamp(2rem, 6vw, 6rem); align-items: center;`.
- Use `@media (prefers-reduced-motion: reduce)` to disable bobbing loops.

## Typography / Fonts

Use DM Sans, Inter, TT Norms-like, Nunito Sans, or similar neutral/rounded geometric sans. Typography should clarify product value rather than compete with the illustration.

## Cultural / Ethical Notes

Corporate Memphis often uses racially ambiguous faceless bodies as a low-cost diversity signal. Avoid using abstract people as a substitute for substantive inclusion, and do not deploy cheerful generic figures to launder harmful, extractive, or confusing product experiences. Check color contrast and reduced-motion behavior because decorative softness can hide accessibility failures.

## Anti-Patterns

Do not treat all flat illustration as Corporate Memphis, overfill dashboards with decorative people, rely on inclusivity-by-blob, use weak contrast pastel text, or make product comprehension depend on looping SVG animation. If specificity matters, commission or select more grounded visual language.
