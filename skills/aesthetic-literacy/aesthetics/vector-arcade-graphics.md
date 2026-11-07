---
slug: vector-arcade-graphics
label: Vector Arcade Graphics
family: digital-internet-native
era: 1970s–1980s; later revivals
aliases: ["Vector arcade display graphics", "Vector-display arcade graphics"]
status: canonical
evidence_level: standard
related: ["8-bit-pixel", "synthwave", "tactical-sci-fi-utility-ui", "demoscene"]
subsets: []
---

# Vector Arcade Graphics

## Scope

The spare line-based image grammar of vector-display arcade games: luminous geometric objects, strokes, counters and unusually open dark playfields. The corpus includes monochrome and color games, flat and perspective scenes, and physical illustrated backdrops. This is a display/game graphic system, not a claim that a browser SVG reproduces vector CRT electronics. Preserve line construction and spatial economy instead of adding a neon skyline.

Evidence: 30 qualifying unique inspected artifacts. See the [research profile](../../../knowledge/aesthetics/vector-arcade-graphics.md) for claim support, direct-media audit, exceptions and source concentration. This descriptive classification was screened against current names, aliases and subsets; related systems are boundaries, not duplicate identities.

## 7-Dimension Profile

**Palette**: Black playfields with white, green or a small set of bright colored strokes. Color can divide objects or play regions; not every example is green monochrome.

**Type**: Angular stroke-like capitals and numerical counters, usually short and legible. Place score and status at the perimeter rather than flooding the stage with microtext.

**Texture**: Thin luminous lines on a dark field; modest bloom may suggest light emission. Some cabinets use static illustrated overlays or backdrops. Raster scanlines, pixel tiling and heavy VHS damage are not defining evidence.

**Shape**: Polygonal ships, outlined obstacles, radial webs, trajectories and wireframe perspective. Quantum supplies a useful filled-object counterexample: not every visible shape is an empty outline.

**Motion**: Viewed Tempest, Asteroids and Battlezone video samples show object motion within stable playfield rules. No universal velocity or easing was measured. For web selection interfaces, a short user-triggered trace can reference the display without constant motion or flashing.

**Spatial**: Large empty regions make a few line objects and perimeter counters readable. Perspective trenches, radial tunnels and open two-dimensional fields are distinct compositions.

**Cultural markers**: Arcade scorekeeping, stage/lives indicators, line-built vehicles and geometric playfields. Identify the actual game/display context; a fake tactical HUD or synthwave horizon communicates a different system.

## Non-Negotiables

**Non-negotiables**:

- Line-built geometric objects are the primary image language.
- Dark negative space carries the composition.
- Sparse score/status or stage information remains distinct from the playfield.

## Connotation

**Mode:** nostalgic quotation.

Precision, playful constraint and the arcade encounter. Small bright forms can feel unusually lucid; excessive bloom quickly obscures that clarity.

## Related / Subsets

8-bit pixel builds images from raster tiles. Synthwave often uses scenic grids, sunsets and gradients. Tactical interfaces prioritize many operational readouts; vector arcade graphics use a comparatively sparse game field. Demoscene emphasizes audiovisual computation and performance rather than a single arcade stage. No new child subset is asserted; the documented branches remain prose guidance within this entry.

## Frontend / UI Guidance

Build a stage/session selector with a large original vector illustration, short difficulty controls and a visible start/reset state. Use real text counters outside the illustration. Decorative traces must be optional, bounded and pausable; mobile should keep the illustration legible without shrinking controls.

## CSS Translation

These are **proposed application tokens**, not sampled historical colors or measured timings. Background `#07120f`, surface `#10231c`, text `#d9ffe6`, muted `#a0ccb5`, accent `#9ef56f`, success `#75dbed`, danger `#edaa76`. Display `Courier New, monospace` at `clamp(2rem,5vw,4.5rem)`, weight 700, line-height 1.02, tracking -0.035em; body `Courier New, monospace` at 1rem/1.5, weight 400, tracking 0; labels 0.8125rem/1.3, weight 700, tracking 0.06em; numeric outputs use tabular figures at 1rem/1.3. Space 1–6: `4,8,12,20,32,48px`; radius `2px` for functional fields and `0` for panel edges (a circular dial/label retains its own geometry). Default state changes are instant; optional feedback `120ms ease-out` is a proposed web value, disabled under `prefers-reduced-motion: reduce`. No automatic decorative loop is required.

```css
.aesthetic-surface {
  --paper: #07120f; --panel: #10231c; --ink: #d9ffe6; --muted: #a0ccb5;
  --accent: #9ef56f; --success: #75dbed; --danger: #edaa76;
  color: var(--ink); background: var(--paper);
  font-family: Courier New, monospace; font-variant-numeric: tabular-nums;
}
.aesthetic-surface :focus-visible { outline: 3px solid currentColor; outline-offset: 4px; }
@media (prefers-reduced-motion: reduce) {
  .aesthetic-surface *, .aesthetic-surface *::before, .aesthetic-surface *::after {
    animation: none !important; transition: none !important; scroll-behavior: auto !important;
  }
}
```
Use a responsive content grid with `minmax(0,1fr)` and `min-width:0` on reading/graphic columns. Scope every rule to the artifact. Preserve semantic labels and visible selected states. Material/print cues belong in decorative CSS/SVG layers, with real text and controls above them.

## Typography / Fonts

Use the categories in the profile before choosing a specific face. The proposed system stacks above require no additional font download; they are substitutions, not claims of historical font identity. Use a licensed face for closer reproduction, verify language coverage and retain a legible fallback. Keep body text at a readable size even where source artifacts contain microprint; large expressive display type must not carry field labels or errors.

## Cultural / Ethical Notes

Game names identify references, not reusable brands or assets. Draw original geometry and lettering treatments. Do not add strobing, screen shake or high-intensity glow to manufacture authenticity.

## Anti-Patterns

- Pixel sprites labeled vector art.
- A synthwave cityscape or densely labeled military HUD.
- Low-contrast hairlines and repeated flashes that obscure controls.
