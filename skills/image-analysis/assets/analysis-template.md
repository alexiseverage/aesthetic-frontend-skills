# Analysis Output Template

Append the following section to `knowledge/aesthetics/<slug>.md`:

```markdown
## Analysis

_Analyzed: <YYYY-MM-DD> | Images reviewed: <count> | Analyst: image-analysis skill_

### Color

| Role | Hex | Notes |
|---|---|---|
| Background primary | #XXXXXX | ... |
| Surface / card | #XXXXXX | ... |
| Primary text | #XXXXXX | ... |
| Accent / highlight | #XXXXXX | ... |
| Secondary accent | #XXXXXX | ... |

**Palette cluster 1 — [name]**: #XXX, #XXX, #XXX
**Palette cluster 2 — [name]**: #XXX, #XXX, #XXX

Contrast pairs: background/text ~X:1 (WCAG [pass|fail] AA)

### Shape

- Border-radius range: [X]px–[X]px (inputs/buttons) / [X]px–[X]px (cards) / [X]px (modal/overlay)
- Geometry: [rectilinear | rounded-rectilinear | organic | mixed]
- Silhouette energy: [compact | expansive]

### Typography

- Type category: [serif | sans-serif | monospace | display | script]
- Historical style: [humanist | geometric | old-style | transitional | slab | etc.]
- Primary weight: [100–900]
- Secondary weight: [100–900]
- Tracking (primary): [tight ~−0.01em | normal | wide ~0.05em | very wide ~0.12em+]
- Case convention: [uppercase | title | lowercase-dominant | mixed]
- Scale contrast: [high | moderate | low]

### Spacing & Density

- Baseline spacing unit (estimated): [X]px
- Inline gaps: ~[X]px
- Component gutters: ~[X]px
- Section spacing: ~[X]px
- Density: [compact | moderate | spacious | airy]

### Texture

| Technique | CSS implementation | Opacity/strength |
|---|---|---|
| [texture name] | `[css property + value]` | [X%] |

### Motion (inferred)

- Implied easing: [spring | ease-out | linear | ease-in-out]
- Animation type hints: [fade | slide | spring | morph]
- Pace character: [immediate | moderate | leisurely]
- Reduced-motion dependency: [high | low | none]

### Layout (UI screenshots only)

- Grid definition: `grid-template-columns: [value]`
- Sidebar width: [X]px (fixed) or [X]% (fluid)
- Content column: [1fr | X%]
- Min layout width: [X]px
- Max layout width: [X]px (or unconstrained)
- Breakpoint behavior — tablet ([X]px): [description]
- Breakpoint behavior — mobile ([X]px): [description]
- Z-axis layers: [count] observable layers; stacking notes
- Scroll behavior: [whole page scrolls | sidebar fixed | inferred]
```
