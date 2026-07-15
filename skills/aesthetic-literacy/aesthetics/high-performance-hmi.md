---
slug: high-performance-hmi
label: High-performance HMI
family: technical-institutional
era: 2000s–present
aliases: ["HP HMI", "High Performance SCADA", "high-performance SCADA graphics", "process-operator graphics", "operator-centered industrial UI"]
status: canonical
evidence_level: limited
related: ["material-design", "flat-design", "j-gov-futurism", "brutalism"]
subsets: []
---

# High-performance HMI

High-performance HMI is a standards-backed industrial operator-interface philosophy translated into frontend dashboard practice. The core visual thesis is exception-first cognition: quiet grayscale overview, clear process structure, and chromatic color reserved for abnormal or action-bearing state. Existing evidence is limited but grounded in ISA-101 and industrial HMI literature rather than image-corpus review.

## Scope

Use High-performance HMI for process monitoring, incident command, infrastructure status, fleet or plant dashboards, security operations, observability systems, and analytical products where abnormal-state salience matters. It fits tools where users compare live values, trends, alarms, setpoints, and process states under attention pressure.

Avoid it for brand-led landing pages, playful consumer apps, lifestyle commerce, decorative sci-fi dashboards, or retro control-room cosplay. The aesthetic is serious, safety-aware, and operator-functional.

## 7-Dimension Profile

**Palette**: Exception-driven grayscale. Backgrounds and surfaces use low-saturation industrial neutrals with near-black text. Chromatic color is rationed: red for critical alarm, amber/orange for warning, blue for selected or control focus, and muted green for confirmed normal/available states. The base stays calm so abnormal conditions become salient.

**Type**: Utility sans or industrial grotesk with tabular numerals. Use neutral sans families for labels and interface text; reserve monospace for tag IDs and PLC/process codes. Numbers are heavier than labels, and tabular figures are mandatory for trend tables, alarm counts, and setpoints.

**Texture**: Flat matte operator-console surface. Texture is created by data itself: trend lines, grid ticks, pipe paths, status lamps, and ruled table rows. Prefer flat colors, 1px rules, inline SVG traces, and muted diagram strokes over faux metal, gloss, glass blur, or cyberpunk noise.

**Shape**: Rectilinear instrumentation. Panels, trend panes, process blocks, alarm rails, and status tables are squared or barely rounded. Pipes and connectors use orthogonal or 45-degree routes. Controls are compact rectangles rather than pill-shaped SaaS components.

**Motion**: Minimal, state-driven, and safety-aware. Live values update with short linear transitions, trend traces scroll steadily, and alarm escalation may blink or pulse only when it communicates urgency. Reject delight motion, bounce, parallax, and decorative reveal choreography.

**Spatial**: Dense overview-first operations layout. Screens prioritize situational awareness: overview map/diagram first, then alarm summary, trends, and detail panels. Use repeatable modules, compact gutters, strict alignment, persistent status/alarm areas, and drill-down detail panes.

**Cultural markers**: Alarm banners and priority columns, tank/pipe/process diagrams, KPI tiles with setpoint/actual/deviation triples, sparklines and trend panes, muted grayscale console fields, maintenance state chips, operator log tables, and ISA-101/SCADA-adjacent seriousness.

## Non-Negotiables

**Non-negotiables**:

- Neutral/grayscale base with chromatic accents reserved for abnormal or meaningful state.
- Overview/detail hierarchy for situational awareness.
- Readable trend, metric, alarm, and process modules.
- Minimal decorative motion; every animation communicates state or flow.

## Connotation

**Mode:** contemporary operational doctrine.

High-performance HMI should apply industrial HMI doctrine to modern web dashboards without imitating obsolete SCADA chrome. The tone is trustworthy, calm, and safety-aware. Its hardness serves cognition, not expressive rawness.

## Related / Subsets

- `flat-design` overlaps through low ornament and flat surfaces, but High-performance HMI’s color philosophy is stricter and safety-oriented.
- `material-design` overlaps in component clarity, but HMI is not consumer-friendly or brand-warm by default.
- `j-gov-futurism` shares dense institutional data, but HMI is real operational doctrine rather than fictional bureaucratic atmosphere.
- `brutalism` shares hardness, but HMI’s harshness serves cognition and alarm salience, not expression.

No canonical subsets are defined yet.

## Frontend / UI Guidance

Design for operators who need a stable overview, fast exception detection, and reliable drill-down. Start with the process or system map, persistent alarms, current operating mode, and trend context; place secondary controls and explanatory copy around that core.

Do not style status colors as brand accents. Treat red, amber, blue, and green as state semantics and ensure color is reinforced by labels, icons, and position for accessibility.

## CSS Translation

- Color roles: `--bg-console`, `--surface-panel`, `--surface-muted`, `--text-primary`, `--text-secondary`, `--state-critical`, `--state-warning`, `--state-selected`, and `--state-normal`.
- Borders/dividers: 1px ruled grids, alarm rails, table row lines, process connectors, and compact panel separators.
- Radius language: squared or barely rounded 0–3px panels and controls.
- Effects: inline trend SVGs, grid ticks, status lamps, data strokes, and muted focus outlines; avoid glassmorphism, faux metal, and decorative glows.
- Layout: overview-first dashboard, persistent alarm/status zones, split detail panes, compact gutters, repeatable modules, and strict alignment.
- Motion: short linear value updates, step changes, trend scroll, alarm escalation, and `prefers-reduced-motion` alternatives for blinking states.

## Typography / Fonts

Use neutral sans typography with tabular numerals and clear hierarchy between labels, values, units, and deltas. Monospace is appropriate for tag IDs, PLC addresses, or process codes, but not for all text.

Avoid expressive display typography. If type draws attention away from live values, alarms, or comparisons, it is off-model.

## Cultural / Ethical Notes

This style is tied to operational safety and situational awareness. Do not use alarm colors, blinking, or industrial seriousness decoratively in contexts where users might confuse state severity.

Because the current profile has no reviewed image corpus, keep claims tied to ISA-101 and industrial HMI literature. Do not present retro SCADA screenshots, cyberpunk dashboards, or simulated hardware as canonical evidence.

## Anti-Patterns

- Decorative red, amber, or green accents unrelated to state.
- Dark sci-fi dashboards with glows, parallax, and cinematic chrome.
- Dense tables without overview, trend, or alarm hierarchy.
- Pill-shaped consumer SaaS components that weaken instrumentation logic.
- Motion used for delight rather than process state, escalation, or update feedback.
