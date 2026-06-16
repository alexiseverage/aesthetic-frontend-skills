---
slug: sports-scorebug
label: Sports Scorebug
family: technical-institutional
era: 1990s–present
aliases: ["score bug", "broadcast score overlay", "sports broadcast graphics"]
---

**Palette**: Dark neutral overlay fields, white numerals, team-color bands, alert yellow/red, and sponsor-safe secondary grey (`#101820`, `#F8FAFC`, `#2563EB`, `#DC2626`, `#FACC15`). Team colors are bounded to rails/chips so score/time hierarchy stays stable.

**Type**: Condensed broadcast sans with tabular numerals, all-caps labels, compact abbreviations, and high-weight scores. Use narrow widths and consistent digit metrics; labels should survive compression and video backgrounds.

**Texture**: Overlay rails, segmented bars, ruled stat columns, slight inner shadows, and subtle digital glow. Texture is broadcast compositing rather than decorative skeuomorphism; transparency must preserve legibility.

**Shape**: Pills, brackets, split score capsules, ticker strips, boxed clocks, possession pips, and expandable stat drawers. Corners are medium (`4–10px`) with beveled/bracketed broadcast authority.

**Motion**: Stat flips, wipe updates, score bumps, clock pulses, possession nudges, ticker crawls, and drawer expansions. Motion is short and functional (`120–300ms`) because it competes with live action.

**Spatial**: Persistent edge modules, low-occlusion layering, score/time/period priority, expandable but anchored stat regions, and sponsor chips that do not interrupt game state.

**Cultural markers**: Game clock, period/quarter labels, timeout pips, possession arrows, shot clocks, down-and-distance, team abbreviations, lower thirds, sponsor bugs, ticker strips.

**Non-negotiables**: persistent score-state module + compressed score/time/period hierarchy + broadcast-safe legibility + short functional motion. If these are removed, the result becomes a generic adjacent style rather than Sports Scorebug.

## Connotation

**Authentic to contemporary broadcast graphics**. It reads as live, authoritative, and spectator-first; decorative sports branding without persistent game state will not carry the aesthetic.

## Scope

Suitable for live dashboards, status overlays, event apps, esports, standings widgets, and operational micro-interfaces. Not suitable for long-form editorial pages unless framed as a live coverage shell.

**Related / Subsets**: Distinct from `high-performance-hmi`: both are dense, but scorebug is spectator-first and edge-anchored rather than operator-control doctrine. Distinct from `j-gov-futurism`: it is broadcast compression, not bureaucratic futurescape.
