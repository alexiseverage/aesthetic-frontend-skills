---
slug: j-gov-futurism
label: J-Gov Futurism
first_researched: "2026-06-05"
last_updated: "2026-06-05"
source: primary-source-screenshots + behance
analyzed: "2026-06-05"
image_count: 9
evidence_level: limited
new_aesthetic: true
aliases: [sibyl-ui, institutional-brutalism, nihon-noir-tech, clinical-brutalism, diegetic-bureaucratic-ui]
---

# J-Gov Futurism

> **Origin**: Diegetic UI aesthetic derived from the Sibyl System interface in the anime *Psycho-Pass* (2012–). Sits at the intersection of bureaucratic brutalism, surveillance infrastructure, and specifically Japanese governmental record-keeping aesthetics. The reference triangle: between the holographic maximalism of *Minority Report*, the terminal-green minimalism of classic cyberpunk, and the paper-form density of a real Japanese government document — and deliberately rejects the glamour of the first two in favor of the banality of the third.

---

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant (<30%) |
|---|---|---|---|
| **Palette** | warm off-white/beige base (~`#EDEAE5`); dark charcoal section headers (~`#232323`); near-black text (~`#1A1A1A`); vivid teal sole accent (~`#00C8C0`) | amber/gold for scientific chart data lines (~`#C8900A`); white reversed on dark header bars; mid-gray rule lines (~`#7A8890`) | dark-background oscilloscope sub-panels (~`#141820`); light-blue avatar panel background |
| **Type** | monospace/tabular `# FIELD : VALUE` all-caps data register; large ultra-heavy numerals (weight 800–900) for primary metric; dense small body in Japanese + Latin bilingual | bold kanji primary name label; lighter-weight romanized subtitle; dark filled section header bars with white/light label | small monospace status pill chips; Japanese tab navigation row |
| **Texture** | flat matte surface; no gradients, no gloss, no blur; single/double-pixel rule lines in mid-gray | repeating crosshatch strip at full-width bezel bottom (ventilation grille motif); faint dashed grid lines in chart areas | banded/striped texture on some section header bars; diamond watermark motif on avatar panel background |
| **Shape** | `border-radius: 0` throughout; chamfered 45° corner cuts on outer bezels via `clip-path`; strict bounded rectangular sub-panels; no drop shadows | small teal status chips (~2px radius); thin vertical teal left-edge severity stripe on metric panel | slightly fanned/overlapping profile cards on case board (the single organic exception) |
| **Motion** | linear fill for progress/loading bars; binary loaded/not-loaded state transitions; no easing, no spring | — | — |
| **Spatial** | high information density; multiple simultaneous sub-panels; persistent address bars top and bottom; strict non-overlapping grid; spatial logic of form/spreadsheet not canvas | large dominant metric numeral anchoring panel; record-in-hierarchy address/path logic (`/ID_STJ/00547_ASJU0056`) | fanned overlapping case board exception |
| **Cultural markers** | `# FIELD : VALUE` colon-spaced monospace labels; `TS No : 000000-0000` session IDs; barcode serial `00000 - XXXX - 00000 - 0` at bottom bar; chamfered bezel hardware; crosshatch bottom strip | teal status chips; large dramatic score numeral as sole expressive element; bilingual kanji + romanized subtitle for person records; anime portrait in bordered sub-panel | real-time oscilloscope sub-panel; platform watermark diamond motif |

---

## Image Descriptions

1. **Case board / overview screen** — The single organic moment in the entire UI: profile image cards slightly fanned and overlapping, evoking a physical evidence board. Faint thin gray connecting lines between card elements with small filled circle nodes — a sparse relationship/network diagram layered behind card content. Everywhere else in the system: zero overlap, zero bleed, zero layering. This exception proves the rule. Confirms warm beige base, chamfered corner bezels, dark charcoal header bars throughout.

2. **User profile card, full view** — Confirms: chamfered corner bezel with crosshatch hatching strip at full-width bottom edge; `TS No : 001145-0003` session identifier and `/ID_STJ/00547_ASJU0056` path string in small monospace at top status bar; dark filled section header bars ("PROFILE", "LAST RECORDED", "RESULT") with white label text; solid teal-fill on active/linked address fields (flat, no gradient, no border-radius); PSYCHOPASS score panel with large ultra-heavy type, "Clear Color" label, mini histogram of historical score distribution; `00475 - AFTE - 34575 - 3` barcode serial number at bottom status bar.

3. **Area Level monitor — dual-register screen** — Left sub-panel: dark background, vertical teal bar chart, "Area Level: 20.3" in large white type — oscilloscope/live-readout instrument aesthetic. Right sub-panel: off-white background, large tabular numerals in bold weight (87.9, 25.8 visible), teal-filled cell highlights for active records. The two modes — dark instrument panel and light form panel — co-exist on one screen without visual tension, unified by the same teal accent and hard sub-panel borders.

4. **Forensics analysis / progress screen** — Vertical checklist of items (MLC-01 through MLC-10), each with a horizontal teal fill bar indicating completion state — no checkboxes, no icons, just fill level. Master progress bar: large teal fill on the left, dark unfilled on the right, "COMPLETE 65%" in large type. Terminal/command-line application logic applied to a visual GUI. Confirms teal as the active/progress color.

5. **Raman spectroscopy chart** — Amber/gold thin data line plotted on the same off-white background as the rest of the UI — no contrasting dark chart area. Faint dotted/dashed grid lines. Axis labels tiny. Reads as a scientific instrument printout or lab report reproduced on paper. Confirms amber as the sole scientific-data chart color, distinct from the teal accent.

6. **Scientific/data composite screen** — Additional forensics data and scientific chart panels. Confirms consistency of amber chart lines, beige background, small monospace labels, and thin ruled table lines across multiple data types on a single screen. Dual panel layout confirms the sub-panel grid logic.

7. **User profile, close crop** — Clearest available view of the `# FIELD : VALUE` label format: `# NAME : YUICHI TOKITOU`, `# DATE OF BIRTH : 19 FEB 2098`. All-caps, spaced colon separators, monospace alignment — reads as a config file or database dump rendered as a visual interface. PSYCHOPASS/FIXED POINT OBSERVATION sub-panel: thin vertical teal left-edge stripe, score 26.3 in large ultra-heavy type, "Clear Color" label, mini vertical-bar histogram of historical score distribution, "RECORDED AVERAGE" secondary label with smaller number.

8. **User profile, full panel view** — Shows complete layout: anime-style illustrated portrait in clearly bordered rectangular sub-panel (left); Japanese tab navigation row as small dark pills; barcode-format serial number at bottom status bar; small mode chip. Confirms warm beige base throughout, bilingual Japanese/Latin field labels, multiple simultaneous sub-panels without overlap.

9. **Melancholia / virtual avatar screen** — Virtual avatar displayed against a light-blue background with small scattered diamond shapes — the only decorative element in the entire UI system, and even here it reads as platform branding/watermark rather than aesthetic choice. Selected avatar panel has vivid teal border treatment; unselected panels are borderless or thin-ruled. "Rainy Blue" platform badge in small pill format. Analytics sub-panel with teal-filled data bars and large numeric value. Confirms teal as the active/selected state color throughout the system.

---

## Analysis

_Analyzed: 2026-06-05 | Images reviewed: 9 | Analyst: image-analysis skill_

### Color

| Role | Hex | Notes |
|---|---|---|
| Background / bezel base | `#EDEADF` | Warm off-white, HSL ~42°, 15%, 90%; slight yellow-tan undertone; never grey |
| Section header bars | `#232220` | Near-black warm charcoal, HSL ~45°, 5%, 14%; white text reversed out |
| Primary text | `#1E1C18` | Warm near-black, HSL ~45°, 10%, 11%; used for all body + label copy |
| Teal accent (primary) | `#00B8BF` | Vivid cyan-teal, HSL ~182°, 100%, 37%; sole chromatic accent across all light panels |
| Teal accent (dark panel variant) | `#00D4D8` | Slightly lighter/brighter rendering of same teal on dark oscilloscope backgrounds |
| Amber / gold chart lines | `#C8900A` | Warm amber, HSL ~42°, 91%, 41%; used exclusively for scientific data line plots |
| Rule / border lines | `#9A9890` | Warm medium gray, HSL ~42°, 5%, 59%; used for all 1–2px sub-panel dividers |
| Faint chart grid lines | `#CCCAC4` | Near-invisible warm light gray; used for dashed axis grid in chart areas only |
| Header bar text | `#F0EEEA` | Slightly warm white; reversed out of charcoal header bars |
| Dark panel background | `#16181A` | Very dark cool near-black, HSL ~210°, 10%, 10%; oscilloscope / live-readout sub-panels only |
| Avatar background / diamond motifs | `#88C0CC` | Muted cyan-blue; decorative only, used on virtual avatar platform background |

**Palette cluster 1 — Institutional base**: `#EDEADF`, `#9A9890`, `#232220`, `#1E1C18`
**Palette cluster 2 — Active accent**: `#00B8BF`, `#00D4D8`
**Palette cluster 3 — Data channels**: `#C8900A`, `#CCCAC4`
**Palette cluster 4 — Exception surfaces**: `#16181A`, `#88C0CC`

Contrast pairs:
- `#1E1C18` text on `#EDEADF` background: ~17:1 (WCAG AAA pass)
- `#F0EEEA` text on `#232220` header bar: ~14:1 (WCAG AAA pass)
- `#EDEADF` text reversed on `#00B8BF` teal: ~2.8:1 (WCAG AA fail — teal used as fill/indicator, not readable text background; white `#FFFFFF` on `#00B8BF` is ~3.1:1, borderline AA for large text only)
- `#00D4D8` bars on `#16181A` dark panel: ~8:1 (WCAG AA pass)

### Shape

- **Outer bezel corners**: 45° chamfered cut, NOT CSS `border-radius`. CSS implementation: `clip-path: polygon(12px 0%, calc(100% - 12px) 0%, 100% 12px, 100% calc(100% - 12px), calc(100% - 12px) 100%, 12px 100%, 0% calc(100% - 12px), 0% 12px)` (chamfer ~12px estimated from screen proportions; exact value may be 10–14px)
- **All interior sub-panels**: `border-radius: 0` — hard right angles throughout
- **Small status chips / tab labels**: `border-radius: 0` (no rounding, or at most 1–2px)
- **"Rainy Blue" platform badge (virtual avatar screen)**: `border-radius: 12px–14px` (pill/capsule — exception; platform branding element only)
- **Teal left-edge severity stripe**: 4–6px wide vertical bar, `border-radius: 0`, solid fill
- **Geometry**: rectilinear throughout; chamfered only on outermost hardware bezel
- **Silhouette energy**: compact, contained; nothing bleeds, nothing overlaps (except case board cards in 01.jpg)

### Typography

- **Data register type** (`# FIELD : VALUE` labels, status bar IDs, serial numbers): monospace category; geometric mono style; weight ~400; tracking normal ~0em; all-caps; tabular figures; letter-spacing on colon separators creates readable column alignment
- **Large kanji name** (時任雄一 and equivalents): sans-serif; weight ~800–900; tracking tight ~−0.01em to 0em; the largest expressive typographic element after the score numeral
- **Score numeral** (26.3, 29.4, etc.): sans-serif; weight ~800–900; scale dramatically larger than all surrounding type — estimated 5–6× body size; zero tracking
- **Romanized subtitle** (Yuichi Tokitou, etc.): sans-serif; weight ~300–400; tracking normal; set smaller and lighter beneath kanji
- **Section headers** (PROFILE, LAST RECORDED, RESULT, PSYCHOPASS): sans-serif; weight ~600–700; tracking wide ~0.06–0.08em; uppercase; rendered as white text reversed into filled dark header bar
- **Body/form text** (Japanese narrative fields, biographical records): sans-serif; weight ~400; tracking normal; small — approximately 10–12px equivalent screen size; bilingual Japanese/Latin
- **"RECORDED AVERAGE", "Clear Color", secondary labels**: sans-serif; weight ~400; tracking wide ~0.05em; very small
- **Scale contrast**: high — score numeral (display-size) vs. all surrounding text (very small body). Exactly two sizes dominate: very large (score + primary kanji name) and very small (everything else). Nothing in between

### Spacing & Density

- **Baseline unit** (estimated): 8px
- **Top status bar height**: ~24px
- **Section header bar height**: ~28–32px
- **Bottom status bar height**: ~28px
- **Internal sub-panel padding**: ~16px (horizontal); ~12px (vertical)
- **Gaps between section header bars and content**: ~8px
- **Rule/divider lines between fields**: 1px at `#9A9890`; vertical rhythm every ~24px in dense form areas
- **Score numeral sub-panel left-edge stripe width**: 4–6px
- **Tab navigation pill height**: ~20–22px; gap between pills: ~4px
- **Mini histogram bar width**: ~2–3px each; gap ~1px; total histogram width ~80px estimated
- **Density**: compact — multiple simultaneous sub-panels, no decorative whitespace; all space is either occupied by content or is functional data gap

### Texture

| Technique | CSS implementation | Opacity / strength |
|---|---|---|
| Flat matte base surface | `background-color: #EDEADF; box-shadow: none;` | — no texture; flatness is the effect |
| Bottom bezel crosshatch grip strip | `background: repeating-linear-gradient(45deg, #9A9890 0px, #9A9890 1px, transparent 1px, transparent 4px), repeating-linear-gradient(-45deg, #9A9890 0px, #9A9890 1px, transparent 1px, transparent 4px)` on a `#EDEADF` base; height ~20–24px | Lines at ~25% opacity of rule-gray on base |
| Chart grid lines (dashed) | `border: none; background-image: repeating-linear-gradient(90deg, #CCCAC4 0px, #CCCAC4 1px, transparent 1px, transparent [interval]px)` | ~40% opacity |
| Teal solid fill (active state) | `background-color: #00B8BF; border-radius: 0; box-shadow: none; backdrop-filter: none;` | Fully flat, no overlay |
| Dark oscilloscope panel | `background-color: #16181A;` | Fully flat, no gradient or noise |

No blur, no `backdrop-filter`, no `box-shadow`, no gradients, no grain, no noise anywhere. Every surface is completely flat.

### Motion (inferred)

The characters in *Psycho-Pass* interact with the Sibyl System fluidly and without friction — panels materialize, data populates, records load — all with the effortless precision of a system that was designed to be used, not admired. Motion is purposeful and fast, never decorative. The easing vocabulary is smooth and confident: quick-start / smooth-settle, not bounce or spring. Nothing overshoots. Nothing hesitates.

- **Panel entry / reveal**: scan-line wipe top-to-bottom, or opacity fade with subtle upward translate (`translateY(-6px) → translateY(0)`); `duration: 180–280ms`; `cubic-bezier(0.16, 1, 0.3, 1)` (fast start, smooth settle — no bounce)
- **Data field population**: sequential reveal — fields appear in reading order, each delayed by ~30–40ms stagger; individual field `duration: 100–150ms`; `transition: opacity linear`
- **Score / large numeral**: animated count-up from 0 to final value; `duration: 400–600ms`; `timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94)` (ease-out deceleration as it approaches the real value)
- **Progress bar fill**: `transition: width 300ms linear` per segment — no ease-in or ease-out; each MLC bar fills independently at uniform rate; master bar fills proportionally as items complete
- **Teal active-state highlight**: instant snap — `transition-duration: 0ms`; selected cells/fields switch state with no fade; the system acknowledges input immediately
- **Tab / section navigation**: `transition: opacity 80ms linear` crossfade — near-instant; no slide, no push
- **Mini histogram bars**: stagger-reveal left-to-right; each bar `duration: 60ms`; `delay: [index] * 20ms`; `transition: height linear`
- **Implied easing (default)**: `cubic-bezier(0.16, 1, 0.3, 1)` for all panel-level transitions (fast acceleration, smooth deceleration, no overshoot). `linear` for fills and progress. `cubic-bezier(0.25, 0.46, 0.45, 0.94)` for count-up numerals
- **Pace character**: fast and precise — total time from "record requested" to "record displayed" feels under 500ms; the system responds at the speed of a professional tool, not a consumer app
- **Reduced-motion dependency**: low — all motion is additive enhancement; the static layout is fully legible without any animation; `@media (prefers-reduced-motion: reduce)` can set all durations to `0ms` without loss of meaning

### Layout (UI screenshots)

- **Outer bezel model**: full-screen panel with persistent top + bottom status bars; content area between them
- **Top status bar**: full width; ~24px tall; contains session ID left + file path right; separated from content by single 1px rule
- **Bottom status bar**: full width; ~28px tall; contains barcode serial number + mode chip left; crosshatch grip strip occupies bottom ~20–24px of bezel
- **Main content layout (profile screens)**: two-column; left ~60% data/form column + right ~40% portrait column; `grid-template-columns: 3fr 2fr` approximate
- **Section headers**: full width of content area; `width: 100%; background: #232220; color: #F0EEEA; padding: 6px 16px`
- **Sub-panels**: hard-bordered rectangular regions; `border: 1px solid #9A9890; padding: 12px 16px; border-radius: 0`
- **PSYCHOPASS score sub-panel**: approximately half-width of content area; sits below "LAST RECORDED" header; `display: grid; grid-template-columns: 6px 1fr 1fr` (left stripe + score area + histogram area)
- **Tab navigation row (bottom of content)**: full-width row of small dark-filled pill chips; `display: flex; gap: 4px; padding: 4px 16px; background: transparent`
- **Min layout width**: ~600px (estimated; designed for fixed terminal-style display, not responsive)
- **Max layout width**: unconstrained / full-screen
- **Z-axis layers**: 2 layers — bezel frame + content panels; no floating elements, no overlapping (except case board overview screen)
- **Scroll behavior**: inferred as non-scrolling; each screen is a complete record view filling the full panel; navigation via tab chips, not scroll

---

## Connections

- **`brutalism`** — shares exposed function, no ornament, structural honesty. Differs: background is warm institutional beige not raw browser defaults; the aesthetic is matte government polish not deliberate ugliness; content is high-density professional data not bare HTML.
- **`swiss-international`** — shares grid rigor, typographic austerity, information-first hierarchy. Differs: warm-toned base not cool modernist white; form-dense bilingual content not editorial Swiss columns; no aesthetic whitespace as design statement; chamfered hardware casing not graphic poster logic.
- **`flat-design`** — shares no gradients, no drop shadows, hard surface geometry. Differs: warm beige base not clean white or bright primaries; chamfered not right-angle only; monospace data-register typography not clean marketing sans; purpose is bureaucratic processing not approachable consumer UI.
- **`neubrutalism`** — shares structural honesty and visible system logic. Differs: institutional restraint not deliberately raw/crude; teal sole accent not high-contrast primary color palette; no thick decorative black borders or oversized UI elements.
- **`early-internet`** — shares monospace data registers and the terminal logic of `# FIELD : VALUE` format. Differs: visually polished matte institutional skin over the data logic; warm beige not terminal green/black; form-panel density not sparse hyperlink-era pages.
- **`skeuomorphism`** — chamfered bezel geometry and crosshatch bottom strip suggest physical hardware texture, overlapping slightly. Differs: no wood grain, no leather, no chrome reflections — the hardware suggestion is structural/functional, not ornamental.

---

## Research Updates

*2026-06-05 — Initial profile created from primary-source anime screenshots (9 images from a local reference set, all capturing the Sibyl System interface in *Psycho-Pass*). Research analysis notes provide full dimension breakdown, typographic analysis, panel-element inventory, and thematic reading. New aesthetic — not currently in the 56-entry aesthetic-literacy dictionary. `new_aesthetic: true` — candidate for promotion after cross-source evidence is gathered.*

## Research Update 2026-06-05

*Web research pass: Behance searches for `psycho pass design`, `psycho pass art`, `sci-fi institutional UI`, `surveillance dashboard UI design`.*

**FUI as the design community label**: Psycho-Pass UI is recognized and tagged in the design community as **FUI** (Fictional User Interface) — an established practice of studying, recreating, and designing in the style of fictional screen interfaces. Related tags applied by other designers: `FUI`, `futuristic`, `sci-fi`, `concept art`. This is the community vocabulary most likely to surface adjacent real-world design work.

**Fan design projects confirming the aesthetic**:
- *PSYCHO-PASS — The Unofficial Wellness App Design* (Yedio 地方{設}畜, Taiwan, 2021; Behance 116846591) — A concept design explicitly evoking "an app issued by the Public Safety Bureau, incorporating the Sibyl System." The designer names health quantification + mental wellness tracking as the institutional logic that maps to the aesthetic. Confirms the governmental/surveillance-apparatus reading is the central identity that other designers recognize and adopt. Tagged FUI, futuristic, sci-fi.
- *Daily UI #6 - User Profile (Psycho Pass)* (Kae Oh, SF, 2017; Behance 49020253) — A profile card UI reinterpretation. Tagged anime, psycho pass, Sci Fi, futuristic. Confirms durability of the aesthetic — designers were replicating it as early as 2017.
- *DOMINATOR - Website Concept* (Thu D, 2022; Behance 135941125) — Website concept for the Dominator weapon from the Psycho-Pass world. Tagged anime, landing page, ui design, website. Confirms the aesthetic extends beyond the Sibyl System specifically to the broader show's visual design language.

**Brutalism cross-corroboration**: Two independent designers created Brutalism-framed Psycho-Pass work ("Brutalism Style Psycho-Pass Poster" and "Diseño Brutalista de Psycho-Pass"). This independently validates the research doc's placement of this aesthetic in close proximity to Brutalism — and is consistent with the `## Connections` section in this profile.

**Real-world institutional UI adjacency**: Behance's "Road video surveillance software" (125065023) — a real CCTV/road monitoring dashboard — surfaces near the top of `surveillance dashboard UI` searches and exhibits similar vocabulary: beige/light base, hard sub-panel grid, functional information density, minimal accent color. Confirms that J-Gov Futurism reads as adjacent to real-world institutional infrastructure UI, not as generic cyberpunk.

**Summary**: The aesthetic has stable recognition in the FUI design subculture, has been independently recreated since at least 2017, and its brutalist/institutional character is the consistent anchor point for how other designers interpret and apply it.
