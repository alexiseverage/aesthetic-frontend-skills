# Examples — Image Analysis

## Example prompts

Tasks that should activate this skill:

1. "I have 15 vaporwave reference images. Extract implementable CSS values."
2. "Analyze the images in the vaporwave profile and fill in the Analysis section."
3. "What hex colors are dominant in these screenshots?"
4. "What border-radius ranges are typical in neubrutalism based on these references?"
5. "Get me implementable values from these images — I need to build tokens."

6. "Here's a screenshot of a dashboard UI. Give me everything I need to build it in code."

---

## Ideal response pattern

**For prompt 1 (vaporwave images — full analysis):**

The agent extracts and outputs implementable values across all 6 extraction targets, then appends the `## Analysis` section to the profile:

```markdown
## Analysis

_Analyzed: 2025-06-12 | Images reviewed: 15 | Analyst: image-analysis skill_

### Color

| Role | Hex | Notes |
|---|---|---|
| Background primary | #1A0A2E | Deep purple-black void |
| Surface / card | #2E1A4A | Slightly lighter purple |
| Primary text | #F0C4E4 | Pale pastel pink |
| Accent 1 | #C77DFF | Lavender neon |
| Accent 2 | #00B4D8 | Cyan |
| Accent 3 | #FF6B9D | Magenta-pink |

**Palette cluster 1 — Void base**: #1A0A2E, #2E1A4A, #0D0620
**Palette cluster 2 — Pastel neon**: #C77DFF, #00B4D8, #FF6B9D, #F0C4E4

Contrast pairs: background/text #1A0A2E / #F0C4E4 ~7.4:1 (WCAG AA pass)

### Shape

- Border-radius range: 0px (common for panels) / 4px–8px (occasional buttons)
- Geometry: rectilinear — grid floor perspective implies strict rectilinear grid
- Silhouette energy: expansive — elements float in void, not contained

### Typography

- Type category: display + sans-serif
- Historical style: late-80s corporate / condensed promotional (display); early 90s publication (body)
- Primary weight: 700–900 (display)
- Secondary weight: 400 (body)
- Tracking (primary): very wide ~0.15em–0.25em (spaced-out heading style)
- Case convention: uppercase-dominant (headings); mixed (body)
- Scale contrast: high — display sizes 3–5× larger than body

### Spacing & Density

- Baseline spacing unit (estimated): 8px
- Inline gaps: ~8px–16px
- Component gutters: ~24px–32px
- Section spacing: ~64px–96px
- Density: spacious — void aesthetic, objects isolated

### Texture

| Technique | CSS implementation | Opacity/strength |
|---|---|---|
| VHS scan lines | `repeating-linear-gradient(to bottom, transparent, transparent 2px, rgba(0,0,0,0.3) 3px)` | 30% |
| CRT phosphor glow | `text-shadow: 0 0 8px #C77DFF, 0 0 16px #C77DFF` | full |
| Noise grain | `filter: url(#noise)` SVG filter or noise image overlay | 5%–8% |
| Subtle vignette | `radial-gradient(ellipse, transparent 50%, rgba(0,0,0,0.5) 100%)` | 50% |

### Motion (inferred)

- Implied easing: ease-out / dreamy slow fade
- Animation type hints: slow loop, gentle float, parallax depth
- Pace character: leisurely — unhurried, uncanny delay
- Reduced-motion dependency: moderate — glitch effects are motion-dependent; static fallback needed
```

---

## Anti-examples

**Anti-example 1: Description instead of implementable value**

> "The palette uses deep purples and pastel pinks with neon accents. The shapes are mostly rectangular."

Why it fails: "Deep purples", "pastel pinks", and "mostly rectangular" are all descriptions. The agent must produce hex values (`#1A0A2E`, `#F0C4E4`), specific border-radius values (`0px` or `4px`), and CSS property names. Every output must be directly pasteable into code.

**Anti-example 2: Claiming to identify exact fonts by name**

> "The typeface used appears to be Eurostile Extended Bold."

Why it fails: Exact font identification from screenshots is unreliable and should not be asserted. The correct output is type category + historical style + visual description: "condensed geometric display, very heavy weight, 80s-style extended letterforms — likely Eurostile-adjacent or custom display, but cannot confirm font name from image."

**Anti-example 3: Motion values stated as facts from static images**

> "The animation duration is 300ms with a cubic-bezier(0.25, 0.46, 0.45, 0.94) easing."

Why it fails: Duration and easing cannot be measured from static images. The agent must state clearly when motion is inferred vs. measured: "Pace character: leisurely (inferred from composition, not measured). Estimated duration for primary transitions: 400ms–600ms based on aesthetic character."

**Anti-example 4: Modifying the Dimension Synthesis section**

> "After analysis, I updated the Dimension Synthesis table with more accurate palette values."

Why it fails: The `## Analysis` section is the only section this skill writes. Dimension Synthesis belongs to `aesthetic-research` and must not be modified by `image-analysis`. Each skill appends its own section; no skill modifies another skill's section.

---

## Ideal response pattern — UI screenshot (prompt 6)

**For prompt 6 (dashboard UI screenshot — full analysis including layout):**

The agent extracts all standard values (color, shape, typography, spacing, texture, motion) AND appends a `### Layout` section:

```markdown
### Layout

- Grid definition: `grid-template-columns: 280px 1fr`
- Sidebar width: 280px (fixed)
- Content column: 1fr (fluid)
- Min layout width: 320px
- Max layout width: 1440px (centered, margin: 0 auto)
- Breakpoint behavior — tablet (768px–1023px): sidebar collapses off-canvas; content takes full width; `grid-template-columns: 1fr`
- Breakpoint behavior — mobile (<768px): single column; sidebar becomes top nav or hamburger drawer; panels stack vertically in source order
- Z-axis layers: 2 observable layers — TerminalWindow (z-index: 10) overlaps TerminalDialogPanel (z-index: 1); overlap removed on mobile
- Scroll behavior: whole page scrolls as one unit (inferred — no fixed sidebar indicators visible)
```
