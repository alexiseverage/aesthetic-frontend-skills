---
name: image-analysis
license: MIT
description: >
  Use this skill when you have visual reference images and need implementable design values
  extracted from them: hex color codes, pixel measurements, CSS technique names, easing
  patterns. Appends a structured Analysis section to an existing knowledge profile. Every
  output is a concrete value, never a description. Use when the user asks to extract colors,
  get CSS values, analyze images for tokens, or identify typography and border-radius values
  from screenshots. Depends on aesthetic-literacy.
  Do not use when no images are available; do not use for qualitative descriptions.
compatibility: Requires visual reference images or screenshots to be provided or accessible via browser tools.
allowed-tools: browser
metadata:
  version: "1.0.0"
  layer: applied
  status: stable
  tags: "image-analysis, color-extraction, css-values, typography-inference, design-tokens, knowledge-base"
  activation_keywords: "analyze these images, extract colors from, what CSS values, implementable values, extract the palette, get the border radius, what hex colors, what font weight, design values from images"
  depends_on: "aesthetic-literacy"
  known_limits: "Cannot extract values without visual input; typography inference is approximate without embedded font metadata"
  last_evaluated: ""
  eval_suite: ""
---

# Image Analysis

## Summary

Analyzes images in a knowledge profile (or user-provided images) and extracts implementable design values — hex colors, px measurements, CSS technique names, easing patterns — never descriptions. Appends a structured `## Analysis` section to `knowledge/aesthetics/<slug>.md`. Never creates new files; always appends to an existing profile.

## When to Apply This Skill

Apply when:
- A knowledge profile exists (or images have been provided) and concrete implementable values are needed for token production
- The user asks to "extract colors", "get CSS values", "analyze these images", or "what border-radius is that"
- The `aesthetic-application` skill needs grounded implementable values, not dictionary approximations
- The `## Analysis` section in a profile is empty or needs updating

Do NOT apply when:
- No images are available (use `aesthetic-literacy` dictionary values as a starting point instead)
- The user wants a qualitative description of the aesthetic (use `aesthetic-literacy`)

## Dependencies

Requires: `aesthetic-literacy` (dimension framework vocabulary)  
Works alongside: `aesthetic-research` (provides the images to analyze)

## Knowledge Base Path

Before reading or writing any profile, resolve the knowledge base root:

| Context | Resolved path |
|---|---|
| Project-level install | `knowledge/aesthetics/` at the **workspace root** |
| User/global install (`-g`) | `~/.agents/skills/knowledge/aesthetics/` |

Identify the workspace root by locating a parent directory containing `.git`, `package.json`, or `.agents/`.

> Throughout this skill, `knowledge/aesthetics/` refers to the resolved path above.

## Critical Rule: Values, Not Descriptions

**Every output must be implementable.** This means:

| ✅ Correct | ❌ Wrong |
|---|---|
| `#2A1F3D` | "deep purple" |
| `8px–16px border-radius` | "slightly rounded" |
| `backdrop-filter: blur(12px) saturate(180%)` | "frosted glass effect" |
| `font-weight: 700, tracking: 0.12em` | "bold and spaced" |
| `cubic-bezier(0.34, 1.56, 0.64, 1)` | "springy animation" |
| `0deg–15deg, noise overlay at 8% opacity` | "textured background" |

If you cannot produce an implementable value (e.g., exact duration is unclear from a static image), provide a range and note the uncertainty: "60ms–120ms (estimated from composition)".

## What to Extract

### 1. Color

- **Dominant palette**: Extract actual hex values from the image (color-sample the most prominent areas)
- **Role assignment**: Which colors serve as background, surface, primary, secondary, accent?
- **Palette clusters**: Group into 2–4 named clusters (e.g., "cool base", "warm accent")
- **Contrast ratios**: Note approximate contrast between background/foreground pairs
- **Saturation/value characteristics**: HSL range descriptions as supplements (e.g., "S: 60–80%, L: 30–50%")

### 2. Shape

- **Border-radius**: Identify the range used across UI elements (e.g., "4px–8px on inputs, 12px–16px on cards, fully-rounded on badges")
- **Geometry type**: Rectilinear / rounded-rectilinear / organic / mixed
- **Aspect ratios**: Typical button, card, and container proportions if observable
- **Silhouette energy**: Compact/contained vs. loose/expansive

### 3. Typography

> **Important**: You cannot identify exact font names from images. Do NOT claim to identify fonts by name.

Extract instead:
- **Type category**: Serif / sans-serif / monospace / display / script
- **Historical style**: Humanist sans / geometric sans / old-style serif / transitional / slab / etc.
- **Weight distribution**: Primary weight + secondary weight (e.g., "700 primary, 400 body")
- **Tracking**: Tight / normal / wide / very wide (with em value estimate if possible)
- **Case convention**: Uppercase / title case / lowercase-dominant / mixed
- **Scale contrast**: High-contrast type scale (display vs. body size) vs. modest contrast

### 4. Spacing & Density

- **Spacing scale hints**: Observable gap sizes (e.g., "8px between inline elements, ~32px section gutters")
- **Grid density**: Compact / moderate / spacious / airy
- **Padding/margin patterns**: Observable interior padding on cards/buttons (approximate px values)
- **Z-axis layering**: Number of observable depth layers, stacking behavior

### 5. Texture

CSS technique mapping — identify which CSS/SVG properties would reproduce the observed texture:

| Observed texture | CSS technique |
|---|---|
| Frosted glass panel | `backdrop-filter: blur(Xpx) saturate(Y%)` |
| Noise grain | `background: url(noise.svg)` at Z% opacity, or CSS `filter` |
| Gradient mesh | `radial-gradient()` or `mesh-gradient` |
| Vignette | Radial gradient dark edges over image |
| Scan lines | Repeating linear gradient, thin dark stripes |
| Glow | `box-shadow: 0 0 Xpx Ypx color` or `filter: blur()` |
| Metallic sheen | Linear gradient at ~45deg with light/dark passes |

### 6. Motion

From static images, motion can only be inferred from compositional cues. State clearly when this is inference, not measurement.

- **Implied easing**: Spring/bounce (if elements appear "landed" with exaggerated scale), fade (if layered transparency), slide (directional emphasis)
- **Animation type hints**: Scroll-based (implied by parallax layers), hover-trigger (observable hover states if present)
- **Pace character**: Immediate/snappy vs. leisurely — infer from visual tension
- **Reduced-motion considerations**: Note if the aesthetic depends heavily on motion for legibility

## Output: Appending the Analysis Section

Append an `## Analysis` section to `knowledge/aesthetics/<slug>.md`. Load [assets/analysis-template.md](assets/analysis-template.md) for the full template with all section headers and placeholder values. Always include sections for Color, Shape, Typography, Spacing & Density, Texture, and Motion (inferred). Include a Layout section only for UI screenshots.

The metadata line must be: `_Analyzed: <YYYY-MM-DD> | Images reviewed: <count> | Analyst: image-analysis skill_`

### 7. Layout & Responsive

For UI screenshots and layout images, extract structural and responsive values in addition to visual ones:

- **Grid definition**: Observable column structure (e.g., `grid-template-columns: 280px 1fr`)
- **Column proportions**: Sidebar vs. content ratio as concrete values, not percentages
- **Breakpoint behavior**: What happens to the layout at tablet and mobile widths (inferred from composition)
- **Spacing scale**: Padding inside components, gaps between components, section spacing — all in px
- **Z-axis / layering**: Number of depth layers, which elements overlap and their stacking order
- **Scroll behavior**: Whether sidebar appears fixed or scrolls with content; inferred from layout structure
- **Min/max widths**: Minimum width before layout breaks, maximum container width if observable
- **Component reflow**: How grids and multi-column components behave at smaller widths

## When Images Are User-Provided

If the user provides images directly (not from the knowledge base):

1. Perform the same extraction process
2. Ask for the target aesthetic slug before writing
3. If a profile exists, append to `## Analysis`
4. If no profile exists, note that the `aesthetic-research` skill should be run first to create the profile — but proceed with analysis if the user confirms
5. If the user never provides a slug, derive one from the filename or dominant content (e.g., `cyberpunk-dashboard` from a dark UI screenshot), state the derived slug, and proceed — do not stall waiting for input

## Examples

Load [EXAMPLES.md](EXAMPLES.md) when uncertain about output format, ideal response structure, or to review anti-patterns. The full vaporwave analysis example there shows the expected level of detail.

## Gotchas

- **Every output must be an implementable value, never a description.** "Deep purples" and "slightly rounded" are not outputs. `#1A0A2E` and `4px–8px border-radius` are. If you cannot produce an exact value, give a range and note the uncertainty.
- **Don't claim to identify exact font names from screenshots.** This is unreliable and should not be asserted. Output type category + historical style + visual characteristics instead.
- **Don't state motion values as facts from static images.** Motion can only be inferred from compositional cues. Always flag motion observations as "inferred from composition" rather than measured.
- **Never modify the `## Dimension Synthesis` section.** Only append to `## Analysis`. The synthesis from `aesthetic-research` is permanent — do not alter it.

## References

Load [REFERENCES.md](REFERENCES.md) when you need CSS syntax or accessibility specs:
- CSS property syntax (backdrop-filter, filter, gradients, box-shadow) → MDN Web Docs sections
- WCAG contrast ratios → WCAG 2.2 SC 1.4.3
- Contrast verification → WebAIM Contrast Checker
