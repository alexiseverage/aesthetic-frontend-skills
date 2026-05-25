---
slug: vorticism
label: Vorticism
family: historical-design-movements
era: 1914–1915
aliases: ["Vorticist", "BLAST style"]
---

**Palette**: Stark black (#1a1a1a), hot pink/magenta (#e5007d), white (#ffffff) — the iconic BLAST magazine palette; industrial gray (#6b6b6b), blood red (#a80000) as secondary accents

**Type**: Grotesque No. 9 — bold, condensed, sans-serif; all-caps headlines at maximum weight; large-scale display type as structural element, not accompaniment; the "Blast" and "Bless" typographic list format (manifesto as UI pattern)

**Texture**: Machine-cut hard edges; newsprint flat ink; no painterly gesture — the surface is hard, industrial, unadorned; the "vortex" as concentrated energy pattern

**Shape**: Intersecting sharp angles — acute triangles, jagged diagonals, hard-edged polygons; forms converge toward a central vortex point, then explode outward; no curves, no organic line

**Motion**: Concentrated explosive energy — movement radiates from a central vortex, unlike Futurism's centrifugal scatter; the force is contained, compressed, then released

**Spatial**: Blocky, compressed compositions; forms interlock like machine parts; tight crowding around a central axis; the vortex as spatial organizing principle — everything drawn toward or ejected from one point

**Cultural markers**: *BLAST* magazine (1914–1915), only two issues — the purest artifact; Wyndham Lewis's angular figure compositions; Epstein's *Rock Drill*; Gaudier-Brzeska's carved forms; Pound's "Vortex" manifesto

**Non-negotiables**: hard-edged angular geometry + black/pink palette + centralized explosive composition

## Connotation
**Mode: authentic.** Vorticism is the most extreme case in the collection: it was too short-lived (1914–1915, two magazine issues) and too aggressively avant-garde to be "revived" or "quoted" in a diluted form. When a designer uses black/pink angular geometry with centralized explosive composition, they are extending the Vorticist project — there is no "soft Vorticism," no "Vorticism-inspired." The aesthetic's defining quality is its refusal to accommodate the viewer. Nostalgic quotation is impossible because there was never a popular Vorticism to feel nostalgic for; ironic pastiche is impossible because the style is already operating at maximum intensity.

## Scope
**Suitable:** Punk and experimental music artist sites, avant-garde fashion editorials and lookbooks, manifesto-style landing pages for creative projects, art school and design portfolio sites, event pages for underground/experimental culture, literary magazines with confrontational editorial stance. The "Blast/Bless" pattern (alternating pro/con lists in bold all-caps) is a distinctive UI pattern for feature comparisons and manifestos.

**NOT suitable:** Corporate websites, e-commerce, financial services, healthcare, education platforms, government sites, anything requiring accessibility compliance or user comfort. Vorticism is deliberately hostile to conventional UX — its sharp angles, maximum-contrast palette, and compressed spatial language fight against readability and ease. Use it only where confrontation IS the desired user experience, and never as a complete site design system.

## Subsets / Related
- [[futurism]] — parallel contemporary; Vorticism is the harder-edged British counterpoint — less romantic about speed, more industrial, more compressed; both share machine-age subject matter but diverge in composition (vortex vs. scatter)
- [[constructivism]] — later influence; Vorticism's angular abstraction and bold typographic scale prefigure Constructivist poster language

## CSS Translation
- **Palette**: `--vrt-black: #1a1a1a; --vrt-pink: #e5007d; --vrt-white: #ffffff; --vrt-gray: #6b6b6b; --vrt-red: #a80000;`
- **Google Fonts**: Anton (heavy condensed sans, closest to Grotesque No. 9), Barlow Condensed Black, Oswald (700 weight)
- **Texture**: Flat solid blocks — `box-shadow: none`; hard edge everywhere; SVG vortex-radial patterns for background energy
- **Border-radius**: 0px — sharp angles define the aesthetic; jagged clip-path polygons
- **Layout**: Central-axis composition with radiating elements; `transform: rotate()` on angled blocks; the "Blast/Bless" pattern — alternating `ul` lists (pro vs. con, feature vs. anti-feature) with bold all-caps headings
