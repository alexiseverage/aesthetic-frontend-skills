---
slug: frutiger-aero
label: Frutiger Aero
first_researched: "2026-07-15"
last_updated: "2026-11-12"
source: "2026-11-12 direct media audit; 33 qualifying unique artifacts; see audit below"
image_count: 33
evidence_level: standard
new_aesthetic: false
aliases: []
---

# Frutiger Aero

> Origin: A mid-2000s to early-2010s soft-tech style that combines glossy UI surfaces, nature imagery, luminous gradients, and optimistic “technology in harmony with nature” messaging. Provenance is unusually clear for a nostalgia-era internet label because the cited overview identifies both the period and the later naming/revival context.

## Source / Evidence Links

- https://en.wikipedia.org/wiki/Frutiger_Aero
- https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
- https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant / Avoid |
|---|---|---|---|
| Palette | sky blue, aqua, leaf green, white glow, clean water/glass tones | citrus accents, rainbow light flares, chrome-white blends | flat grayscale severity with no atmosphere |
| Type | clean humanist sans, light glossy labels, airy headers | rounded system sans, soft futurist UI text | gritty editorial serif systems as the main voice |
| Texture | glossy surfaces, glass bubbles, dew/water motifs, shine bands, smooth gradients | translucent swooshes, lens flare, bokeh-like polish | rough distress, matte paper, anti-polish textures |
| Shape | rounded tabs, orb icons, curved swooshes, leaf/wave motifs, soft-corner panels | bubbles, capsules, floating badges | sharp brutalist outlines or square-only systems |
| Motion | gentle glow, float, sweep, water-like reveal, polished transitions | ambient movement, orb hover states | aggressive erratic motion contradicting the serene optimism |
| Spatial | airy UI over bright environmental imagery, layered hero fields, product surfaces that feel clean and buoyant | dashboard cards over luminous backgrounds | dense dark enterprise compression with no wonder signal |
| Cultural markers | nature-meets-technology optimism, Vista-era polish, eco-futurist stock imagery, glossy desktop/UI nostalgia | green-tech branding, air-and-water metaphors | any 2000s gloss lacking the nature harmony frame |

## Image Descriptions

No dedicated image corpus was collected during this pass. The profile is grounded in a direct style overview plus accessibility references instead:

1. [https://en.wikipedia.org/wiki/Frutiger_Aero] — strongest source in this pass; explicitly identifies the period, notes the later naming/revival context, and describes the style’s optimistic technology-in-harmony-with-nature imagery and skeuomorphic elements.
2. [https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html] — accessibility baseline for copy over luminous gradients, nature imagery, and glow-heavy UI surfaces.
3. [https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion] — accessibility baseline for atmospheric sweep and float effects.

## Analysis

The Frutiger Aero summary is unusually useful because it already compresses both provenance and semantic content: mid-2000s/early-2010s prevalence, UI origins, later internet-aesthetic naming, and the core nature-plus-technology optimism. That makes frontend translation clearer than with many nostalgia labels. The style is not just “glossy”; it is glossy in a bright, ecological, reassuring register.

Representative interface patterns are rounded desktop-era controls, watery hero backgrounds, orb-like icon containers, bright environmental stock-photo compositions, and polished surfaces that feel clean rather than metallic. The aesthetic is strongest in landing pages, splash screens, operating-system nostalgia, and optimistic tech-brand framing rather than in dense operational software.

Accessibility constraints are obvious but manageable. Glow, water, and sky imagery can wash out text unless copy sits on stabilized surfaces or stronger contrast bands. Motion such as floating bubbles or sweeping light should remain atmospheric rather than communicative, and should defer to `prefers-reduced-motion`.

Anti-patterns for implementation: mistaking any glossy 2000s UI for Frutiger Aero, removing the nature-harmony frame and leaving only generic shine, or putting essential text directly over high-luminance photography. The cited source supports a narrower and more coherent reading than simple “Vista nostalgia.”

## Connections

- `web-2-gloss` — shares rounded gloss, but Web 2.0 Gloss is badge/startup friendly while Frutiger Aero is softer, more environmental, and more eco-futurist.
- `glassmorphism` — both can use transparency and atmosphere, but Glassmorphism is a contemporary card pattern while Frutiger Aero is a broader image-world with skeuomorphic optimism.
- `organic-digital` — overlaps in humane-tech softness, though Organic Digital is more biomorphic and abstract where Frutiger Aero remains glossier and more environmental.

## Research Updates

- 2026-07-15 — Initial limited research profile created from a direct style overview and accessibility references.


## Direct media audit — 2026-11-12

This audit supersedes earlier generic dimension claims and limited source counts; earlier notes are retained as research history.
This audit inspected 35 complete still artifacts from a 120-record discovery pool, plus three contemporary interactive websites at 1280 × 900. Thirty-three unique still works qualify. One plain font specimen is a boundary comparison; an amber globe image has unresolved attribution-route identity and is excluded. Repeated campaign images, alternate views and icon-pack members were not counted separately. No search thumbnails contribute to the count. Historical images were streamed for linked analysis; only private browser-state captures of the contemporary sites were retained. No reference image is a production asset.

The still corpus is concentrated in CARI's curated index and its supplied scans. Many different designers and media are represented, but this is not independent archive triangulation. Credited original routes are preserved in the private ledger; [Microsoft's Songsmith project](https://www.microsoft.com/en-us/research/project/songsmith-2/) and [Launchy's author site](https://www.launchy.net/) confirm product context. The credited NXE portfolio route returned 403. Index dates are not automatically screenshot dates: the Launchy image contains Word 2010 despite a 2007 index title. SWIM is an unbuilt, undated concept. These uncertainties constrain chronology claims.

### Synthesis and confidence

- **Palette — high for range, moderate for prevalence:** FA02–FA19, FA26–FA35 include fresh cyan/lime, dark emerald, violet, warm orange/yellow and monochrome silver. Blue/green is characteristic, not mandatory in every interface. One archive's selections cannot establish global prevalence.
- **Type — moderate:** FA01, FA16–FA17, FA20–FA21 and FA29–FA35 show readable humanist sans labels, compact utility hierarchies and occasional light display headings. FA24 illustrates type anatomy but is excluded as a complete aesthetic example. Frutiger is an association in the retrospective name, not a claim that Windows used that family.
- **Texture — high:** FA03–FA04, FA10, FA15–FA17 and FA28–FA35 repeat glossy upper highlights, transparent or reflective material, soft glows and dimensional icon edges. Object surfaces and window hierarchy matter as much as wallpaper.
- **Shape — high:** FA03, FA10–FA17 and FA22–FA23 establish circles, droplets, pebbles, rounded consumer hardware and shallow beveled controls. Dense rectangular schedule cells in FA35 remain compatible with the larger visual system.
- **Spatial — high:** FA02, FA07, FA10, FA12–FA14 and FA26–FA35 use layered atmospheric environments or restrained foreground utility planes. Real software can be dense; do not impose spacious hero composition on every Aero task.
- **Motion — low historically, moderate for observed revival behavior:** FA36 changes text size; FA37 opens and changes windows; FA38 changes scroll layers and declares randomized cloud/butterfly loops. These are present-day sites inspected in meaningful states, not three historical motion artifacts. No historical transition cadence is established. The application proposes a slow 12-second, seven-unit sphere drift, with pause and reduced-motion stillness.
- **Cultural markers — moderate:** the retrospective category joins consumer software, advertising, product objects and luminous interiors. Ecological imagery is common but neither proof of sustainability nor compulsory in every utility panel. Contemporary nostalgic websites are separated from period evidence. This corpus does not represent every regional design tradition.

Collection stopped after 33 qualifying works, spanning utility UI, icons, product photography, commercial illustration, wallpaper and interiors. Later examples confirmed material and hierarchy variation rather than adding a new defining rule. Source concentration and missing historical playback remain explicit limitations, not reasons to inflate confidence.


### Full-media observations

**FA01 — Microsoft Songsmith Main UI (2009)**

CARI credits: UI Designer Unknown. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjk1MzE1Mi9vcmlnaW5hbF80YzI3NjhjZTI0MDAxNTA5YTNiYWU3N2I2NjgzMWQwOS5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1030 × 551. Directly observed: Utility variant: gray-blue window chrome surrounds a multicolored song timeline. Rounded glossy transport controls and softly lit sliders organize a dense, readable grid; no landscape is needed. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA02 — Concept for Ebisquare (2005)**

CARI credits: Barbara Holzer, Holzer Kobler Architecture. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwODYzNC9vcmlnaW5hbF9mZTVkZjZhOTM1ZjFiMmY3ZmRiOWUyNDQ2ODBlN2ZhNy5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1440 × 960. Directly observed: Architectural render uses white continuous ribbon levels, cyan water flooring and enlarged green foliage panels. Broad luminous reflections and translucent railings merge clean retail technology with a stylized ecosystem. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA03 — Sparkling Lounge- Crystalized Suite Swarovski (2005)**

CARI credits: Simone Micheli Architects. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNzEzMi9vcmlnaW5hbF8zNjIxYTA3NDJjMGYxMTYxMGNjNDliN2MzZmE5MTY0NC5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 931 × 1054. Directly observed: Chartreuse-lit room combines glossy black pebble seats and transparent screens with white circular dots. Specular highlights and luminous lower edges, rather than landscape, establish synthetic softness. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA04 — Nvidia - 3D Your PC (2010)**

CARI credits: Agency: Ars Thanea. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjc0Ni9vcmlnaW5hbF9jNzUwMDJkZTE1ODcwNDc0YmI3ZjIxN2JlYmNhOGZkYi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 600 × 378. Directly observed: Dark emerald advertising scene uses an intense radial green glow from a screen, airborne bubbles, and small bokeh hexagons. Product and person remain sharply lit against atmospheric depth; this is the darker techno variant. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA05 — Cappy KV (2011)**

CARI credits: Agency: Ogilvy, Istanbul. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjY0MC9vcmlnaW5hbF80YmIxOThkNjVhMjYyYmQ1MDhjZjI2NGViOTUyODcyZC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 600 × 777. Directly observed: Central abundant fruit tree is composited into a symmetrical city street under pastel sky and rainbow. High-key light, floating leaves and saturated citrus color create frictionless commercial nature; tree imagery alone would miss the composite realism. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA06 — Advertisement for Oasis (2010)**

CARI credits: Matt Dartford. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjYxMi9vcmlnaW5hbF83MTQwM2M0ZThkMzNlNWIzZDY5ZTE3Y2Y5MTk0NmNjYy5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 912 × 1020. Directly observed: Bottle-centered blue advertisement has an explosive radial splash, suspended fruit and toy-like glossy gold animals. Every object has exaggerated reflective volume; composition is busy and highly synthetic rather than flat eco iconography. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA07 — I Am Your Land, Original Concept (2012)**

CARI credits: Neil Duerden. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjQ5Ny9vcmlnaW5hbF9lZTMyOTk1MzMzNmRlOTRjM2Y5ZTgyMDFkYzQ4MGQ0Ny5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1200 × 1509. Directly observed: Dark green composite builds a spherical landscape from cascading water, clipped trees and an impossible city inside an arc of rainbow. Nature is hyperreal, polished and spatially composited, not botanical line art. Human portrait is analytical reference only. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA08 — RockShox "Made in Harmony With Nature" (2009)**

CARI credits: Neil Duerden. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjQ2My9vcmlnaW5hbF84NjRkOWUyMTQ2NGZkYzY2YmFkZDJjNGRmMjZmY2FjNS5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 720 × 1061. Directly observed: Bright white ad grows pale green curling ribbons and leaves from a bicycle fork. Fine parallel lines, translucent circles and dimensional flower highlights bridge vector ornament with photographic product. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA09 — Perrier Citron Fresh Spring Water (2009)**

CARI credits: Garth Glazier. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjQyOC9vcmlnaW5hbF9hNWQxYWQzMDFmNDZiYjEyM2E1ZmNiZmI4ODRhOWI4Zi5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 886 × 653. Directly observed: White-backed collage uses angled green glass bottles, translucent branded droplets, flowers and large narrow sans lettering. Smooth highlights meet splatter texture; busy lime composition is not merely a blue-sky wallpaper. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA10 — Illustration by John Harwood (2009)**

CARI credits: John Harwood. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjQwMS9vcmlnaW5hbF84ZjdkYWY4NTQ1NTYxZjU2MjRkNjRlMGQ5ZDFlY2M5YS5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1420 × 676. Directly observed: Extremely spare white illustration pairs a flowing dark-to-light blue ribbon with a dense cloud of transparent reflective spheres. Depth depends on varied sphere sizes, overlapping specular highlights and a soft contact glow. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA11 — SWIM Las Vegas (Year Unknown)**

CARI credits: Slick Design. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjMxNC9vcmlnaW5hbF83MWFiZTU4NTBjMzUxNzU0YjUxY2U5MzhjYzdmNDU2MC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1800 × 1350. Directly observed: Unbuilt restaurant visualization uses saturated blue underwater panels and lime seating in a clean white room. Repeating rounded partitions, reflective floors and luminous watery surfaces establish architectural translation; date remains unknown. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA12 — Froyo Yogurteria (2012)**

CARI credits: Ahylo Studio. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNjIwOS9vcmlnaW5hbF9hZmZhMGVmMDg4ZThlOWVlZDVkZjg3ODVkNDFmYjU1Ny5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1200 × 1800. Directly observed: Lime ceiling carries dense hanging rods and glowing white droplet lamps above a reflective rippled white service counter. Wood wall is secondary; bright rounded lighting is integrated into functional space. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA13 — Bliss Spa, Atlanta Midtown (2009)**

CARI credits: Larry Sassi, Yeekai Lim. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNTk2Mi9vcmlnaW5hbF8xNGFkZjljOGZlNGQ5YWRkZWQxZDZjZDc3ZTQ3MzM2My5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1800 × 1195. Directly observed: Spa interior repeats sky-blue cloud murals, backlit white shelving and curved pale counters. Product labels remain a compact grid, while the large blue field and luminous borders make the room airy. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA14 — Smashing Magazine "World Environment Day" Wallpaper Calendar (2009)**

CARI credits: Vanesa Gazze for Smashing Magazine. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNTgxMC9vcmlnaW5hbF8yMmQ2YjNkMzMxODY3Yzc3NGE3YmJiZTI0MzNlNmNkNC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1800 × 1125. Directly observed: Environmental calendar wallpaper mixes photographic leaves and grass with translucent swirls, a star-like sun flare and floating seeds. A paper calendar is deliberately layered within a richly synthetic green/cyan atmosphere. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA15 — Ariel Detergent Logo (2013)**

CARI credits: Unknown designer for Procter & Gamble/Ariel. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwNDIzMi9vcmlnaW5hbF9mYzBhODNlNTUzNWYyNjRhMTY0YzJiYjM0YjZhMTlmZC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1000 × 1000. Directly observed: Red rounded wordmark contrasts with a thick green interwoven orbital symbol. Multi-stop gradients, white specular streaks and a bright central flare make a logo behave like polished transparent material. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA16 — Windows Icons V2 (2008)**

CARI credits: Chris Scholten (saviourmachine). [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwMzc0MC9vcmlnaW5hbF82NzVmYzkxYWJmYWEwZTU1ZDcyMmNhMDM4ZGYwMzg1Zi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1024 × 768. Directly observed: One icon pack, not dozens of independent artifacts: rounded square tiles use translucent bezels, upper white gloss and strong multicolor gradients. Pictograms vary, while edge highlights maintain one physical construction. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA17 — Logitech Harmony 1100 UI (2009)**

CARI credits: Unknown designer for Logitech. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwMjI4Ny9vcmlnaW5hbF8wZTY1MzE4Nzk1NTA4ZmQ5M2Y1YTc4ZDJlZjRmOTU1Ny5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 450 × 450. Directly observed: Remote display photographed at an angle uses blue light trails behind radial transport buttons. Large yellow pause dominates dark glass circular controls; luminous edges separate small labels from the background. Complete 450px source supports construction, not fine type measurements. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA18 — Phoenix Children's Hospital, AZ (2011)**

CARI credits: HKS Architects. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwMTUzOS9vcmlnaW5hbF82OGVkOTA4OGE4ZDkwYmRkMjI2MzkxZGJmY2U3OTg2ZS5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1498 × 1116. Directly observed: Hospital reception uses violet curved soffit and polished floor, with a backlit botanical photo wall behind a pale counter. Floral photo detail is large-scale and luminous; this is an architectural variant rather than interface evidence. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA19 — Children's Healthcare of Atlanta, GA (2007)**

CARI credits: Interior Design- Tara Rae Hill, LittleFISH Think Tank. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjgwMTMyNC9vcmlnaW5hbF80NzA0ZTAxZTY4NzZlZDMzNjg5YjQwZDIzMTg0MzBlOC5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 738 × 1113. Directly observed: Hospital interior is warm red and yellow, with a huge sunflower macro image and sweeping rounded floor/ceiling bands. This counteracts a mandatory blue-green rule while retaining clean glossy optimism. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA20 — Microsoft Encarta Kids (2005)**

CARI credits: Unknown designers for Microsoft. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc5ODE4My9vcmlnaW5hbF9jY2ZmZDE1YjkzMWEyMDgzZmMzYTZlNzdmOGEyZDA1Yi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 804 × 602. Directly observed: Encarta Kids interface uses a lime navigation strip and orange rays behind a central translucent leaf. Dimensional subject icons flank the center in tilted shallow buttons; compact humanist sans labels remain dark and readable. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA21 — Microsoft Surface (2008)**

CARI credits: Initial concept-  Steven Bathiche, Andy Wilson. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTY1OC9vcmlnaW5hbF9kOGEyOTQ2YTYyNGFlODJjYzFiYzVjYzk2ZTA5OWIyYy5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 640 × 412. Directly observed: Surface table photograph shows mint luminous touch surface, semi-transparent panels, white compact data and overlapping rectangular images. Physical hands are reference-only; a still cannot establish gesture timing or whether the displayed medical data is functional. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA22 — Summer Sphere Vector (2011)**

CARI credits: Razvodovska. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTQ5NC9vcmlnaW5hbF8xZDY5YTcxZTQ4ZWE0Nzc0N2Y0ZDdlZmY0NjNlODMxNS53ZWJwIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjoxODAwLCJoZWlnaHQiOjE4MDAsImZpdCI6Imluc2lkZSIsIndpdGhvdXRFbmxhcmdlbWVudCI6dHJ1ZX0sIndlYnAiOnsicXVhbGl0eSI6NzV9LCJqcGVnIjp7InF1YWxpdHkiOjc1fSwicm90YXRlIjpudWxsfX0=). Accessed 2026-11-12; 597 × 600. Directly observed: Complete spherical illustration shades from white rim and sky blue into acid green grass. Transparent polygon leaves, tiny butterflies, white bokeh and central flare give idealized nature a glassy container. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA23 — Orbotix Sphero (2011)**

CARI credits: Ian Bernstein and Adam Wilson. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTQ3Ni9vcmlnaW5hbF8wMWQxMTM1NDYxMWYxOWQ3ODcwMzFiZTEyYmRlMDk2MS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 600 × 400. Directly observed: Three illuminated spherical devices are staged against navy, with red/green/cyan transmitted light and elliptical shadows. Product material is glossy translucent white; still photography gives no rolling or pulse timing. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA24 — Droid Sans (2007)** — boundary comparison, excluded from count

CARI credits: Steve Matteson of Ascender Corporation for Android. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTMzNy9vcmlnaW5hbF9lM2QzOWIwMWUzOTljYmRkMGQ1YmYzNzllNzYzZTZjYS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1522 × 1800. Directly observed: Type specimen demonstrates open humanist sans forms, double-storey a and clear counters in regular/bold. Useful typography evidence, but a plain type specimen alone does not qualify as a full Aero composition. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA25 — Egg Planet Illustration + Tutorial (2010)** — boundary comparison, excluded from count

CARI credits: Alexandra Fomicheva. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTI3Ny9vcmlnaW5hbF8zODBiZThiZTIxNDhlNWI3ZjcxNWJlMDM0ZTk4ZTE1NC5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 796 × 596. Directly observed: Amber earth-shaped egg is lit from within and mirrored on a glasslike plane, with translucent shell pieces and warm bokeh. Link supplied by index points to a different green-planet tutorial; treat source identity as unresolved, excluded. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA26 — Earth Day. Green Planet. Illustration + Tutorial (2009)**

CARI credits: Alexandra Fomicheva. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTI3My9vcmlnaW5hbF83Yjg3MDNiYTkzMTBjNGY0ZjY3NWQ1YzRhOGE0ZmQyNi5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1600 × 1200. Directly observed: Green Earth composite wraps grass, white clouds and a fruit tree around a lit globe, with rainbow arcs and thin parallel wave lines. Lettering has a pale dimensional edge. Artificial ecological abundance is composed as a floating glossy object. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA27 — Alfoart Splash Screen (2008)**

CARI credits: Alexandra Fomicheva. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTI1Ny9vcmlnaW5hbF83NGQ5YzkzMGJmODg5M2I3ZDM5NGYwOGRmYmNhMjg5OS5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 615 × 535. Directly observed: Monochrome portfolio splash arranges modeled consumer objects around an elliptical reflective floor, overlaid with fine looping wave lines. White vignette and silver gloss provide spatial depth without green ecological imagery. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA28 — Sony Vaio OEM Wallpaper (2007)**

CARI credits: Unknown Designers for Sony. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NTA4NS9vcmlnaW5hbF9hNjY3MTc5NTdjOTQwNzhjMjdhODA4MTBiN2I1OGFiYS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1800 × 1125. Directly observed: Yellow/lime wallpaper uses a sweeping translucent concave ribbon and light grain beneath a very small pale central wordmark. Broad diffuse highlights and quiet asymmetric curves establish a material field, not a collection of nature symbols. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA29 — Ubuntu Netbook Remix UI (2010)**

CARI credits: Canonical Ltd., Moblin Project. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NDg2NS9vcmlnaW5hbF9lZjUzMDRmZmQxOWVmODkzNTdmYWU3MjIzNTUwZjM4MS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1024 × 600. Directly observed: Ubuntu interface uses a purple translucent field and a dense 4-column icon grid with a left category rail. Dimensional object icons and inset lit borders coexist with compact sans labels; evidence for a dark utility variant. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA30 — Windows Mobile 6 Interface (2007)**

CARI credits: Unknown designers for Microsoft. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjc1NDgwNy9vcmlnaW5hbF9lMzNmNGM0MWNiN2RhZDNiNGM0NzZjOWFiM2MzOWE4NS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 550 × 733. Directly observed: Small original mobile screen uses a glossy cyan title strip, thin bright separators, compact white humanist type and a faint radial cyan lower glow. List rows remain restrained; gradients belong to hierarchy rather than every text container. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA31 — Xbox 360 NXE dashboard (2008)**

CARI credits: Rowland Brown for Microsoft . [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjcyNTE3MC9vcmlnaW5hbF84MmEyOTZhM2ZiMDE4MDY2ZTRjMzJhYTBlMmZmOTQzNC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 1280 × 720. Directly observed: NXE screenshot stages receding lime tiles on a cool gray floor with soft reflections, subtle circular texture and a hazy green background. Large white category type establishes spatial navigation; still image cannot establish transition duration. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA32 — Launchy (2007)**

CARI credits: https://www.launchy.net/. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjcyNDkwNC9vcmlnaW5hbF9kZDQ3MDA1M2RkMDc4ZTZhZTA0MGZhNDkxMjQ2OWFjMi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 372 × 280. Directly observed: Complete compact launcher screenshot has black glass top, gray upper sheen, a raised document icon and a white search field over a dense small-text suggestion list. Date in source title is approximate: Word 2010 appears in this capture, so do not date the exact screenshot to 2007. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA33 — eyeOS 2.5 (2011)**

CARI credits: Marc Cercós, Pau Garcia-Milà, Eduardo Pérez, David Plaza, Hans Pufal.. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjcxNTc5NS9vcmlnaW5hbF8xYTE2NjMwZTIzMGJmODIwNTIzMDI2ZDUyM2E2M2M1OS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 867 × 638. Directly observed: Blue web desktop shows pale rectangular application window with a dense object-icon grid, bottom taskbar and a small glossy green weather tile. Clear panel hierarchy keeps chromatic highlights subordinate to utility. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA34 — openSUSE 11.3 (2010)**

CARI credits: openSUSE, KDE development teams. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjcxNTYxMC9vcmlnaW5hbF9lYmE2ZmRmN2M2MjNhM2E3MTNiNzY1MDhiYWEyYThkYy5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 800 × 600. Directly observed: Green/cyan desktop layers a translucent folder panel, white start menu and large soft bokeh beneath a sharp curved wallpaper band. Icon shadows and faint glass edges create depth with ample negative space. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA35 — Windows Vista Media Center (2007)**

Designer unspecified in CARI record. [Provenance](https://cari.institute/aesthetics/frutiger-aero); [inspected media](https://images.are.na/eyJidWNrZXQiOiJhcmVuYV9pbWFnZXMiLCJrZXkiOiIzMjcxNTQzNS9vcmlnaW5hbF8yMjc2NjkxOGJlOWQzMmM2N2RmNzljODE0MjRiMzY2OS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE4MDAsImhlaWdodCI6MTgwMCwiZml0IjoiaW5zaWRlIiwid2l0aG91dEVubGFyZ2VtZW50Ijp0cnVlfSwid2VicCI6eyJxdWFsaXR5Ijo3NX0sImpwZWciOnsicXVhbGl0eSI6NzV9LCJyb3RhdGUiOm51bGx9fQ==). Accessed 2026-11-12; 848 × 480. Directly observed: Media Center guide uses dark transparent blue cells, bright cyan outlines and a single luminous selected programme. Thin humanist heading contrasts with dense legible schedule text; large image behind grid is deliberately muted. Static inspection establishes no animation timing. Rights/handling: Linked analysis only; streamed for inspection; no publication permission inferred..

**FA36 — Contemporary interactive community** — boundary comparison, excluded from count

Consumer Aesthetics Network. [Provenance](https://frutigeraero.org/); [inspected media](https://frutigeraero.org/). Accessed 2026-11-12; 1280 × 900. Directly observed: Green wave wallpaper supports glossy dark segmented navigation and a translucent body panel. Changing text size from Medium to Large visibly reflows the paragraph while preserving the panel hierarchy. No active CSS animations were reported in the inspected state; mascot is reference-only and is not used in the application. Rights/handling: Copyright retained by respective creators; no source images shipped..

**FA37 — Contemporary interactive vista** — boundary comparison, excluded from count

Vista Aero project; creator unspecified on welcome panel. [Provenance](https://windowsvista.pages.dev/); [inspected media](https://windowsvista.pages.dev/). Accessed 2026-11-12; 1280 × 900. Directly observed: Contemporary tribute uses thin glass window edges, gray glossy taskbar and bright 3D object icons against a photographic green landscape. Maximize changes the welcome window size but does not fill the viewport in this implementation; closing it and double-clicking Explorer opens a folder grid. Computed style reports 0.28/0.22-second transitions on one wrapper; this is not a historical Vista timing measurement. Rights/handling: Copyright retained by respective creators; no source images shipped..

**FA38 — Contemporary interactive parallax** — boundary comparison, excluded from count

Creator unspecified on inspected page. [Provenance](https://frutigeraero.pages.dev/); [inspected media](https://frutigeraero.pages.dev/). Accessed 2026-11-12; 1280 × 900. Directly observed: At initial scroll position, sky and white clouds fill the scene. Scrolling 1800 pixels reveals a crisp reflective city and saturated grass while layers shift at different rates. Browser reports randomized cloud drift around 54–70 seconds and butterfly flutter around 5–10 seconds on this visit; these are declared contemporary CSS durations, not timed historical footage. Rights/handling: Copyright retained by respective creators; no source images shipped..

