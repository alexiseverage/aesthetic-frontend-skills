---
slug: corporate-memphis
label: Corporate Memphis / Illustration Flat
first_researched: "2026-07-15"
last_updated: "2026-07-15"
source: mixed
image_count: 0
evidence_level: limited
new_aesthetic: false
aliases: [Alegria, "Big Tech Art Style"]
---

# Corporate Memphis / Illustration Flat

> Origin: A late-2010s corporate illustration style built from flat vector shapes, bright solid colors, abstracted faceless figures, and friendliness-at-scale branding. Provenance is strongest for the Big Tech deployment history and for the style’s association with Facebook’s Alegria system; frontend translation claims should be read as synthesis from that broader visual culture.

## Source / Evidence Links

- https://en.wikipedia.org/wiki/Corporate_Memphis
- https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
- https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant / Avoid |
|---|---|---|---|
| Palette | bright flat solids, coral/blue/yellow/green brand accents, low-shading fills | slightly muted startup palettes, broad skin-tone abstraction, white backgrounds | textured illustration, moody dark realism, or metallic depth |
| Type | neutral geometric or neo-grotesque sans paired with illustrations rather than competing with them | rounded startup sans, soft product-marketing headers | ornate display typography dominating the page |
| Texture | no texture or very light vector grain; almost entirely flat fills | simple shadowless layering, sparse line accents | heavy painterly rendering or tactile material simulation |
| Shape | blob limbs, rounded geometric scenery, oversized plants/devices, simplified objects | circles, arcs, abstract office props, exaggerated gestures | naturalistic anatomy or detailed facial characterization |
| Motion | friendly lightweight loops, onboarding illustration drift, simple SVG bobbing | card reveals, gentle scroll illustration movement | intense character animation that distracts from product comprehension |
| Spatial | generous whitespace with one hero illustration or spot illustrations supporting product narrative | explanatory landing pages, empty states, onboarding panels | dense operational dashboards where decorative figures compete with tasks |
| Cultural markers | faceless vector humans, abstract diversity signaling, startup/help-center friendliness, Big Tech-safe optimism | SaaS landing-page explainer art, HR-tech inclusivity imagery | any flat illustration system with no corporate/product framing |

## Image Descriptions

No dedicated image corpus was collected during this pass. The profile is grounded in historical and descriptive summary material instead:

1. [https://en.wikipedia.org/wiki/Corporate_Memphis] — strongest source in this pass; explicitly describes minimalism, flat elements, bright solid colors, and cartoon-like figures with disproportionate limbs, and ties the style to Facebook’s 2017 Alegria rollout and later Big Tech adoption.
2. [https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html] — accessibility baseline for turning flat illustration palettes into readable product surfaces and CTA pairings.
3. [https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion] — accessibility baseline for keeping looping onboarding art decorative rather than mandatory.

## Analysis

Wikipedia’s Corporate Memphis summary provides the clearest concise grounding in this pass: the style is flat, bright, vector-based, and tied to outsized simplified figures, with Facebook/Alegria as a pivotal deployment point. That evidence supports a frontend reading in which the aesthetic lives less in component chrome than in surrounding product illustration systems — hero art, empty states, explainer sequences, and brand storytelling panels.

Representative interface patterns are single-hero product illustrations, onboarding scenes with abstracted people using giant devices, customer-support or productivity explainers, and empty states softened by approachable vector figures. The style works best when it remains secondary to the product structure rather than replacing the information architecture itself.

Accessibility and fatigue are the main constraints. Flat bright palettes often produce cheerful but weak contrast pairings, so WCAG checks matter for text over illustrated backgrounds and for CTA colors derived from illustration palettes. Motion should also stay minimal; bobbing figures and looping leaves are on-model, but product comprehension should never depend on decorative SVG animation.

Anti-patterns for implementation: treating all flat illustration as Corporate Memphis, using abstract people where task diagrams would be clearer, relying on decoration to signal inclusivity without substantive product clarity, and extending the style into data-dense application surfaces where it adds little but generic startup gloss.

## Connections

- `flat-design` — shares minimal surfaces and reduced ornament, but Flat Design is a component/system language while Corporate Memphis is primarily an illustration and brand-world language.
- `material-design` — both can coexist in modern products, but Material governs interface structure whereas Corporate Memphis typically decorates marketing and empty-state contexts around it.
- `web-2-gloss` — near-opposite tone: Corporate Memphis is shadowless and vector-flat where Web 2.0 Gloss is shiny, rounded, and reflection-heavy.

## Research Updates

- 2026-07-15 — Initial limited research profile created from a descriptive historical summary and accessibility references. A future pass could add primary design-system examples from Facebook/Alegria-era brand materials.
