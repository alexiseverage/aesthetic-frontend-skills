---
slug: fictional-user-interface-diegetic
label: Fictional User Interface / Diegetic Screens
family: speculative-robotics
era: late-20th-century-present screen graphics
aliases: ["FUI", "fantasy user interface", "diegetic UI", "screen graphics", "fictional interface"]
status: canonical
evidence_level: limited
related: ["high-performance-hmi", "tactical-sci-fi-utility-ui", "j-gov-futurism"]
subsets: []
---

# Fictional User Interface / Diegetic Screens

## Scope

Fictional User Interface / Diegetic Screens is the screen-graphics craft of making interfaces that appear to belong inside a fictional world. Use it for story-driven dashboards, sci-fi product narratives, media installations, and cinematic interface moments. It is not the same as a real safety-critical HMI, and it should not be treated as evidence of usable operational design.

The current profile is limited and text-source based. Motion and timing are central to many FUI examples but were not inspected directly; any animation guidance here is a design recommendation unless backed by motion artifacts.

## 7-Dimension Profile

**Palette**: High-contrast luminous accents on dark, glass, or transparent grounds: cyan, teal, amber, red alert, pale green, and white telemetry. Color often maps to fictional status rather than brand warmth.

**Type**: Technical monospace, condensed sans, micro labels, all-caps module names, numeric telemetry, coordinates, timestamps, and dense register text. Friendly marketing typography breaks the in-world instrument feel.

**Texture**: Screen glow, scanlines, holographic translucency, wireframe overlays, grid noise, particle fields, subtle chromatic aberration, and transparent panes. Keep effects below readability thresholds.

**Shape**: Reticles, brackets, wireframes, circular gauges, schematic diagrams, angular panels, node graphs, targeting boxes, and layered data cards.

**Motion**: Data population, scan sweeps, rotating wireframes, diagnostic blips, and panel reveals are common recommendations, but specific pacing remains inferred here. Always include reduced-motion alternatives.

**Spatial**: Layered graphics sit over or inside a diegetic scene: in-world screens, glass displays, cockpit panels, lab monitors, or projected interfaces. The frame should imply a physical or story-world surface.

**Cultural markers**: Territory Studio and related screen-graphics practice, FUI as a named discipline, film/game screen craft, diegetic/non-diegetic UI taxonomy, and fictional technology storytelling.

## Non-Negotiables

**Non-negotiables**: in-world screen framing; dense technical data typography; schematic/reticle geometry; luminous screen texture; a story or system role for the interface. Without diegetic context, it becomes generic sci-fi decoration.

## Connotation

Usually contemporary genre quotation: intelligent systems, worldbuilding, surveillance, engineering, navigation, or mission control. It can feel impressive but untrustworthy if used for real tasks; separate spectacle from product-critical UI.

## Related / Subsets

`high-performance-hmi` is real operator UI with safety and grayscale-first doctrine. `tactical-sci-fi-utility-ui` is a game/military HUD overlay. `j-gov-futurism` shares bureaucratic future atmosphere but not the cinematic screen-graphics craft.

## Frontend / UI Guidance

Use FUI for hero moments, fictional diagnostics, onboarding stories, visualization frames, and non-critical dashboards. Provide a plain readable layer for real controls, errors, prices, legal text, and accessibility-critical tasks.

## CSS Translation

Use dark surfaces, luminous borders, grid backgrounds, conic/radial gauge shapes, SVG wireframes, `filter: drop-shadow`, subtle scanline overlays, and data-population animation gated by `prefers-reduced-motion`.

## Typography / Fonts

Use mono and condensed technical sans for labels, numerals, and short readouts; keep paragraphs in a neutral readable face. Avoid tiny low-contrast microtext for actual content.

## Cultural / Ethical Notes

FUI often borrows military, surveillance, medical, or security language. Do not make false claims of technical accuracy or safety, and avoid copying proprietary film/game interfaces.

## Anti-Patterns

- Using FUI styling for real safety-critical controls.
- Filling screens with unreadable dummy text and calling it usability.
- Copying a recognizable movie/game interface.
- Treating inferred motion as source-proven timing.
