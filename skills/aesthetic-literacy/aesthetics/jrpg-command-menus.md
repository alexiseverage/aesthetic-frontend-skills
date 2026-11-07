---
slug: jrpg-command-menus
label: JRPG Command Menus
family: digital-internet-native
era: 1980s–present
aliases: ["Japanese role-playing game menus", "JRPG party menus"]
status: canonical
evidence_level: standard
related: ["8-bit-pixel", "dvd-menu", "fictional-user-interface-diegetic"]
subsets: []
---

# JRPG Command Menus

## Scope

A command-and-party interface grammar documented across Japanese role-playing games: named actions branch into inventories, abilities, equipment and character status while resource information stays organized. This descriptive catalog label spans blue console windows, parchment handheld menus and modern graphic interfaces. It does not claim that every Japanese game has one national visual style. Preserve navigable command hierarchy and explicit party state; raster pixels, blue gradients and portraits are branches rather than universal requirements.

Evidence: 30 qualifying unique inspected artifacts. See the [research profile](../../../knowledge/aesthetics/jrpg-command-menus.md) for claim support, direct-media audit, exceptions and source concentration. This descriptive classification was screened against current names, aliases and subsets; related systems are boundaries, not duplicate identities.

## 7-Dimension Profile

**Palette**: Dark blue/white console windows recur, but gray, cream, yellow, red and cyan systems are directly represented. Contrast separates selected command, resource values and help text; a single blue palette cannot define the whole corpus.

**Type**: Short action labels, aligned resource abbreviations and strong numerical hierarchy. Older raster lettering and newer italic or condensed display systems coexist; avoid treating a pixel font as compulsory.

**Texture**: Bounded window planes range from flat black/white through beveled gradients to paper and graphic collage. Keep ornamental texture subordinate to resource legibility.

**Shape**: Rectangular command lists, nested selection windows, party slots and status meters dominate. Portrait circles, angled modern cutouts and parchment panels are documented variants.

**Motion**: Inspected Final Fantasy menu videos show discrete selection, subpanel changes and character/status continuity. Their playback samples do not establish universal durations. Proposed web changes should be immediate, with optional brief panel transitions and an instant reduced-motion fallback.

**Spatial**: A visible command tree beside party/resources and contextual explanations. Handheld dual screens distribute these roles across stacked surfaces; modern widescreen menus spread them across large panels.

**Cultural markers**: Party membership, equipment, abilities, HP/MP-like resources and an explicit return path. Recognize individual game makers and eras rather than equating the grammar with Japanese culture as a whole.

## Non-Negotiables

**Non-negotiables**:

- A named command hierarchy with a clear route back.
- Party or character resources presented as structured state.
- An unmistakable selected action and contextual explanation.

## Connotation

**Mode:** contemporary revival.

A deliberate quotation of planning between encounters: preparation, companionship and tactical choice. It can reward thoughtful exploration, but becomes tiring when ordinary tasks require unnecessary submenus.

## Related / Subsets

8-bit pixel describes raster construction; these menus survive beyond pixels. DVD Menu concerns authored disc navigation rather than party resources. Diegetic interfaces may situate controls inside a fictional world; JRPG menus are often explicitly outside it. No new child subset is asserted; the documented branches remain prose guidance within this entry.

## Frontend / UI Guidance

Use an expedition inventory or equipment planner. Keep command buttons separate from resource readouts, show item quantities and disabled reasons, and update the selected character consistently. On narrow screens, place commands before party details and help in reading order. Native buttons work better than imitating an entire gamepad input system without its affordances.

## CSS Translation

These are **proposed application tokens**, not sampled historical colors or measured timings. Background `#091a46`, surface `#17396e`, text `#f4f7ff`, muted `#b5c9e5`, accent `#e6cc72`, success `#9be2cb`, danger `#8e273c`. Display `Georgia, serif` at `clamp(2rem,5vw,4.5rem)`, weight 700, line-height 1.02, tracking -0.035em; body `Trebuchet MS, sans-serif` at 1rem/1.5, weight 400, tracking 0; labels 0.8125rem/1.3, weight 700, tracking 0.06em; numeric outputs use tabular figures at 1rem/1.3. Space 1–6: `4,8,12,20,32,48px`; radius `2px` for functional fields and `0` for panel edges (a circular dial/label retains its own geometry). Default state changes are instant; optional feedback `120ms ease-out` is a proposed web value, disabled under `prefers-reduced-motion: reduce`. No automatic decorative loop is required.

```css
.aesthetic-surface {
  --paper: #091a46; --panel: #17396e; --ink: #f4f7ff; --muted: #b5c9e5;
  --accent: #e6cc72; --success: #9be2cb; --danger: #8e273c;
  color: var(--ink); background: var(--paper);
  font-family: Trebuchet MS, sans-serif; font-variant-numeric: tabular-nums;
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

Do not reuse game screenshots, franchise crests, character art or music. Game UI Database carries restrictive AI/ML asset-use language; its images were inspected analytically only and were not supplied to generation. Avoid invented Japanese lettering or claims that all JRPGs share one style.

## Anti-Patterns

- A blue gradient over generic dashboard cards without commands or party state.
- Hover-only selection, unexplained disabled commands, or color-only health warnings.
- Mandatory combat animation, autoplay sound or inaccessible gamepad-only controls.
