# Canonical Aesthetic Entry Example

Use this as a compact installed-user example for new or migrated dictionary entries. It is deliberately smaller than a real entry, but it shows the shape agents should expect when loading `aesthetics/<slug>.md`.

```markdown
---
slug: example-aesthetic
label: Example Aesthetic
family: Contemporary Lifestyle
era: contemporary
aliases: [example style]
status: canonical
evidence_level: synthesis
related: []
subsets: []
---

# Example Aesthetic

## Scope

Define the aesthetic as a usable visual system. State what is in scope, what neighboring aesthetics it is not, and when the entry should be used.

## 7-Dimension Profile

**Palette**: role-based color behavior, contrast norms, and recognizable hue relationships.

**Type**: type categories, weight, spacing, case, and historical or platform references.

**Texture**: surface treatment, material cues, CSS effects, grain, blur, gloss, roughness, or absence of texture.

**Shape**: border radius, geometry, silhouettes, component proportions, and icon shape language.

**Motion**: timing, easing, preferred transitions, and reduced-motion fallback implications.

**Spatial**: density, whitespace, grid behavior, layering, hierarchy, and compositional rhythm.

**Cultural markers**: motifs, object vocabulary, text register, iconography, and signals that make the aesthetic recognizable.

## Non-Negotiables

List the 2–4 dimensions that must survive translation. Removing these should break the aesthetic identity.

## Connotation

Describe origin context, contemporary reading, audience resonance, fatigue risk, and appropriate connotation modes.

## Related / Subsets

Name related slugs, subset emphases, and boundaries so agents avoid flattening neighboring styles.

## Frontend / UI Guidance

Translate the aesthetic into practical product-surface guidance: components, states, hierarchy, density, and interaction tone.

## CSS Translation

Provide implementation-friendly patterns such as gradients, borders, filters, shadows, blend modes, and safe fallback notes.

## Typography / Fonts

Name font categories and sourcing constraints. Prefer categories when a specific font is not required.

## Cultural / Ethical Notes

Flag sacred, regional, subcultural, political, or appropriation-sensitive material. Distinguish homage from costume.

## Anti-Patterns

List common ways the aesthetic becomes generic, offensive, or visually incoherent.
```

Installed agents should treat real entries as canonical production guidance and root `knowledge/aesthetics/` resources as optional provenance context only when requested.
