---
slug: high-performance-hmi
label: High-performance HMI
first_researched: "2026-06-16"
last_updated: "2026-07-15"
source: ISA-101 + industrial HMI literature
image_count: 0
evidence_level: limited
new_aesthetic: false
aliases: ["HP HMI", "High Performance SCADA", "high-performance SCADA graphics", "process-operator graphics", "operator-centered industrial UI"]
---

# High-performance HMI

> **Origin**: Standards-backed industrial operator-interface philosophy translated into frontend dashboard practice. The core visual thesis is exception-first cognition: quiet grayscale overview, clear process structure, and color reserved for abnormal or action-bearing state.

## Source / Evidence Links

- https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards
- https://corsosystems.com/posts/the-high-performance-hmi-handbook-and-you-part-1

---

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant / Avoid |
|---|---|---|---|
| **Palette** | grayscale operating base; red/amber accents reserved for alarms/exceptions | muted blue selected states; green confirmed normal state | dark sub-panels for specialized traces only |
| **Type** | neutral sans with tabular numerals; compact labels; heavy live values | monospace tag IDs and process codes | condensed industrial grotesk for dense modules |
| **Texture** | flat matte panels, ruled grids, trend traces | diagram strokes and status lamps | simulated hardware frames, used sparingly |
| **Shape** | rectilinear panels, process blocks, alarm rails | orthogonal pipe diagrams and compact controls | slight radius on noncritical chips |
| **Motion** | state-driven updates, trend scroll, alarm escalation | short linear value transitions | no decorative motion |
| **Spatial** | overview-first dense dashboard; persistent alarm/status zones | split overview/detail layouts | mobile crops that reduce density but keep exception hierarchy |
| **Cultural markers** | tank/pipe diagrams, KPI tiles, alarm priority tables, trends | operator logs and maintenance chips | SCADA nostalgia only if clearly subordinated to modern readability |

---

## Image Descriptions

No image corpus was collected for this limited-evidence profile (`image_count: 0`). The dimensional synthesis above is grounded in the cited source links and the implementation brief rather than reviewed image evidence; future canonical migration should not treat this profile as having source-backed visual corpus descriptions until images are collected.

---

## Analysis

_Analyzed: 2026-06-16 | Images reviewed: 0 | Analyst: implementation brief synthesis_

High-performance HMI translates industrial operator doctrine into web UI. ISA-101 frames HMI as a standards-backed discipline for process visualization; Corso Systems' HMI Handbook discussion emphasizes high-performance graphics as a cognitive/situational-awareness practice rather than decorative dashboard styling.

### Color

The palette must remain quiet until state changes require attention. Red, amber, and orange are not brand accents; they are operational signals.

### Typography

Tabular numerals and compact labels matter because operators compare live values, setpoints, and trend histories under time pressure.

### Texture

Texture comes from data primitives: process pipes, trend grids, ruled tables, and status lamps. Faux industrial texture weakens the professional signal.

### Motion

Motion is low-dependency and should communicate live state, process flow, or alarm escalation. Decorative animation is off-model.

### Layout

The layout should start with an overview and support drill-down. Persistent alarm and status zones are more important than hero imagery.

---

## Connections

- **`material-design` / `flat-design`** — shares clarity and flatness, but HMI is exception-driven and industrial, not consumer-friendly.
- **`j-gov-futurism`** — shares dense institutional data, but HMI is real operational doctrine rather than fictional bureaucracy.
- **`brutalism`** — shares hardness, but HMI's harshness serves cognition and safety, not expression.

---

## Research Updates

*2026-06-16 — Initial knowledge profile created from `.hermes/research/new-aesthetic-candidates/final-selection-implementation-brief.md`; promoted into the dictionary in the same change set, so `new_aesthetic: false`.*
