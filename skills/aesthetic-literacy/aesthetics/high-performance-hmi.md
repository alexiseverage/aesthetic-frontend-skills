---
slug: high-performance-hmi
label: High-performance HMI
family: technical-institutional
era: 2000s–present
aliases: ["HP HMI", "High Performance SCADA", "high-performance SCADA graphics", "process-operator graphics", "operator-centered industrial UI"]
---

**Palette**: Exception-driven grayscale. Backgrounds and surfaces use low-saturation industrial neutrals (`#D8D3C8`, `#B8B6AE`, `#747872`, `#2E3332`) with near-black text (`#151817`). Chromatic color is rationed: red (`#D7261E`) for critical alarm, amber (`#D99A18`) for warning, blue (`#2F6F9F`) for selected/control focus, and muted green (`#4E7A4A`) for confirmed normal/available states. The dominant rule is not "dark dashboard" or "colorful telemetry"; the base stays calm so abnormal conditions become immediately salient.

**Type**: Utility sans or industrial grotesk with tabular numerals. Use Inter, IBM Plex Sans, Roboto Condensed, or a similar neutral sans; reserve monospace for tag IDs and PLC/process codes. Numbers are heavier than labels (`font-weight: 700–800` for live values; `400–500` for labels), labels are compact uppercase or title case, and tabular figures are mandatory for trend tables, alarm counts, and setpoints. Display typography is inappropriate unless it serves a metric hierarchy.

**Texture**: Flat matte operator-console surface. Texture is created by data itself: trend lines, grid ticks, pipe paths, status lamps, and ruled table rows. CSS should prefer `background-color`, 1px rules, inline SVG trend traces, and muted diagram strokes. Avoid faux metal, gloss, glass blur, ornamental gradients, or cyberpunk noise.

**Shape**: Rectilinear instrumentation. Panels, trend panes, process blocks, alarm rails, and status tables are squared or barely rounded (`border-radius: 0–3px`). Pipes and connectors use orthogonal or 45-degree routes. Controls are compact rectangles, not pill-shaped SaaS components. Diagram symbols should feel like process instrumentation, not marketing icons.

**Motion**: Minimal, state-driven, and safety-aware. Live values update with short linear transitions (`120–220ms linear`), trend traces scroll steadily, and alarm escalation may blink or pulse only when it communicates urgency. Prefer stepwise state changes, progress fills, and process-flow indicators; reject delight motion, bounce, parallax, and decorative reveal choreography.

**Spatial**: Dense overview-first operations layout. Screens prioritize situational awareness: overview map/diagram first, then alarm summary, trends, and detail panels. Use repeatable modules, compact gutters (`4–8px`), strict alignment, persistent status/alarm areas, and drill-down detail panes. Empty space is functional separation, not lifestyle breathing room.

**Cultural markers**: alarm banners and priority columns; tank/pipe/process diagrams; KPI tiles with setpoint/actual/deviation triples; sparklines and trend panes; muted grayscale console fields; maintenance state chips; operator log tables; ISA-101/SCADA-adjacent seriousness.

**Non-negotiables**: neutral/grayscale base + chromatic accents reserved for abnormal/meaningful state + overview/detail hierarchy + readable trend/metric modules + minimal decorative motion. If color becomes decorative or the dashboard loses operator situational awareness, it is no longer high-performance HMI.

## Connotation

**Contemporary revival** — apply the industrial HMI doctrine to modern web dashboards without imitating obsolete SCADA chrome. The tone is serious, safety-aware, and operator-functional. It is appropriate for infrastructure, industrial IoT, energy, water, logistics, observability, incident response, and other tools where attention must go to exceptions. Avoid ironic pastiche: making it look like retro control-room cosplay undermines the trust signal.

## Scope

**Suitable for**: process monitoring, incident command, infrastructure status, fleet/plant dashboards, security operations, observability systems, and analytical products where abnormal-state salience matters. **NOT suitable for**: brand-led landing pages, playful consumer apps, lifestyle commerce, or decorative sci-fi dashboards.

**Related / Subsets**: Related to *flat-design* through low ornament and flat surfaces, but the color philosophy is stricter and safety-oriented. Related to *material-design* only in component clarity, not in consumer friendliness. Adjacent to *j-gov-futurism* through dense institutional data, but HMI is real-world operational doctrine rather than fictional bureaucratic atmosphere. Distinct from *brutalism*: its hardness serves cognition and alarm salience, not expressive rawness.
