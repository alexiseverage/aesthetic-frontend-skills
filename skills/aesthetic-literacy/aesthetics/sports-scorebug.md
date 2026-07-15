---
slug: sports-scorebug
label: Sports Scorebug
family: technical-institutional
era: 1990s–present
aliases:
- score bug
- broadcast score overlay
- sports broadcast graphics
status: canonical
evidence_level: limited
related:
- high-performance-hmi
- j-gov-futurism
subsets: []
---

# Sports Scorebug

Sports Scorebug is a broadcast-graphics aesthetic built around persistent score-state modules, compressed clock/period/team hierarchy, team-color rails, ticker strips, and short functional motion. It reads as live, authoritative, and spectator-first.

## Scope

Use it for live dashboards, event apps, esports overlays, standings widgets, operational micro-interfaces, watch-party tools, and status overlays. Avoid it for long-form editorial pages unless they are framed as live coverage shells.

## 7-Dimension Profile

**Palette**: Broadcast-safe dark/light modules, team-color rails, high-contrast score fields, neutral clock/status surfaces, ticker backgrounds, and sponsor-chip accents that never interrupt game state.

**Type**: Condensed broadcast sans, tabular numerals, all-caps labels, compact abbreviations, high-weight scores, clear period/quarter labels, and legible clock text.

**Texture**: Overlay rails, segmented bars, ruled stat columns, slight inner shadows, subtle digital glow, ticker strips, and broadcast package chrome.

**Shape**: Pills, brackets, split score capsules, ticker strips, boxed clocks, possession pips, timeout dots, sponsor chips, and expandable stat drawers.

**Motion**: Stat flips, wipe updates, score bumps, clock pulses, possession nudges, ticker crawls, lower-third reveals, and drawer expansions. Motion must be brief and state-driven.

**Spatial**: Persistent edge modules, low-occlusion layering, score/time/period priority, expandable anchored stat regions, lower thirds, and sponsor chips that do not block primary state.

**Cultural markers**: Game clock, period/quarter labels, timeout pips, possession arrows, shot clocks, down-and-distance, team abbreviations, lower thirds, sponsor bugs, ticker strips, and live update rituals.

## Non-Negotiables

**Non-negotiables**:

- Persistent score/time/period state.
- Broadcast-safe compression and edge anchoring.
- Team, possession, or event-state encoding.
- Short functional motion for live updates.

## Connotation

**Mode:** authentic contemporary broadcast graphics.

It reads as live, authoritative, and spectator-first. Decorative sports branding without persistent game state will not carry the aesthetic.

## Related / Subsets

- `high-performance-hmi` shares density, but scorebug is spectator-first and edge-anchored rather than operator-control doctrine.
- `j-gov-futurism` shares compressed panels, but this is broadcast live-state compression rather than bureaucratic futurescape.

No canonical subsets are defined yet.

## Frontend / UI Guidance

Use a persistent score module, clock, period, team identifiers, possession/status pips, and expandable stat drawer. Ensure overlays avoid important content and remain legible over video or imagery.

## CSS Translation

- Color roles: `--bg-bug`, `--surface-score`, `--team-home`, `--team-away`, `--accent-live`, `--ticker-bg`, and `--line-overlay`.
- Borders/dividers: segmented rails, split capsules, boxed clock, stat columns, and ticker separators.
- Radius language: capsules and brackets for broadcast modules; keep clock and score fields stable.
- Effects: subtle inner shadow/glow, wipe transitions, flip numerals, and ticker movement.
- Layout: edge-anchored overlay with low-occlusion rules and responsive compact variants.
- Motion: score bumps, flips, wipes, and ticker crawl with reduced-motion alternatives.

## Typography / Fonts

Use condensed broadcast sans with tabular numerals. Abbreviations are expected, but critical team/clock/period state must remain understandable.

## Cultural / Ethical Notes

Live sports state affects attention and accessibility. Avoid rapid flashing, provide reduced-motion options, and do not let sponsor or promo elements obscure play-critical information.

## Anti-Patterns

- Sports-themed hero branding without persistent live state.
- Full-screen dashboards that ignore edge-overlay grammar.
- Team colors with insufficient contrast for scores or clocks.
- Long decorative animations that delay updates.
- Sponsor chips larger than score/time state.
