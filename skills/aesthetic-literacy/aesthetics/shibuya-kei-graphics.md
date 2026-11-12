---
slug: shibuya-kei-graphics
label: "Shibuya-kei Graphics"
family: vernacular-commercial
era: "1990s–early 2000s Japanese music graphics; later reissues"
aliases: ["Shibuya kei graphic design"]
status: canonical
evidence_level: standard
related: ["city-pop", "blue-note-jazz-modernism", "pop-art", "desktop-publishing"]
subsets: []
---

# Shibuya-kei Graphics

## Scope

A scene-related graphic lens around selected Shibuya-kei record design: editorial sampling of mod, lounge, modernist, pop and retro-futurist references, recomposed through precise typography and packaging. The musical genre is broader than one visual style; neither every Japanese sleeve nor every release by a relevant musician qualifies.

## 7-Dimension Profile

**Palette**: Edited primary colors, cream, teal, orange, pink, black/white and selective metallic or woodgrain variants. Palette depends on the sampled reference system rather than a compulsory Tokyo neon scheme.

**Type**: Outlined or modular titles, clean editorial labels, condensed sans, contrasting scripts and Japanese/Latin mixing in specific works. Type hierarchy and referential recombination matter more than one font or gratuitous Japanese characters.

**Texture**: Clean cutout collage, halftone, printed sleeves, discs, simple pattern fields and materially inventive packaging. Photographs can be present in originals, but the transferable interface grammar is graphic composition and type.

**Shape**: Framed pictures, circles/discs, stars, grids, diagram-like labels, geometric emblems and packaging windows. Motifs vary; use a coherent original sampled vocabulary rather than tracing a designer’s sleeve.

**Spatial**: Editorial panels, surprising scale jumps, asymmetric crops and orderly small credits around a striking title or object. A cover-like focal unit can coexist with a practical track/release list.

**Cultural markers**: 1990s Japanese record/design networks, Mitsuo Shindo, Groovisions and other specific makers. Sampling is an active design method, not permission to copy copyrighted source art. Reissues must retain their own publication dates.

**Motion**: Historical timing/easing is unknown in this still-led corpus. A current application may be intentionally still, with immediate state changes or brief optional feedback. Any squash, reveal or parameter transition is a design proposal, not an observed historical standard. Reduced motion preserves the complete composition and every task.

## Non-Negotiables

**Non-negotiables**: Referential graphic recombination; deliberate editorial typography; a coherent cover/package-like focal composition; scene-specific credits/context without reducing the music to one look.

## Connotation

**Mode:** scene-aware nostalgic quotation.

1990s Japanese record/design networks, Mitsuo Shindo, Groovisions and other specific makers. Sampling is an active design method, not permission to copy copyrighted source art. Reissues must retain their own publication dates. Strong decorative cues require editing around the task; recognition should come from the whole material/type/space system rather than copied source imagery.

## Related / Subsets

City Pop often refers to earlier popular-music packaging and idealized urban imagery. Blue Note Jazz Modernism is a specific modernist recording/design lineage that may be quoted. Pop Art and Desktop Publishing are broader reference systems, not synonyms.

Related catalog owners: `city-pop`, `blue-note-jazz-modernism`, `pop-art`, `desktop-publishing`. Internal variants remain descriptive unless they establish a separately useful, researched system.

## Frontend / UI Guidance

Build a listening guide with release filters, sleeve-like typographic tiles and a working mix queue. Selection changes the queue and liner notes; original geometric artwork carries identity without portraits or copied album covers. Avoid implying commercial audio is available when it is not.

Use real buttons, labeled inputs and visible selected/disabled/error states. Support keyboard operation, 44px touch targets and announced feedback. Reflow modules on narrow screens; decorative geometry must not intercept pointer events or obscure focus. Use original abstract/object artwork; people imagery and copied source screenshots should not carry the interface identity.

## CSS Translation

All values below are **proposed application tokens**, estimated from the visual family and authored for current web use; they are not sampled historical measurements.

```css
.aesthetic-surface {
  --background: #F5EBD8;
  --surface: #FFFCF0;
  --text: #1D3C45;
  --text-muted: #5A6C6A;
  --primary: #176F77;
  --secondary: #BF4933;
  --accent: #D5AD43;
  --radius-small: 0px;
  --radius-medium: 2px;
  --radius-large: 4px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 20px;
  --space-5: 32px;
  --space-6: 48px;
  --motion-fast: 120ms;
  --motion-medium: 240ms;
  --motion-easing: cubic-bezier(.2,.7,.2,1);
}
@media (prefers-reduced-motion: reduce) {
  .aesthetic-surface *, .aesthetic-surface *::before,
  .aesthetic-surface *::after { animation: none; transition: none; }
}
```

Typography proposal: geometric sans display, 700 weight, `clamp(2rem, 5vw, 4.5rem)/1.05`, tracking `-.02em`; system sans reading face, 400 weight, `16px/1.55`; 600-weight utility labels, `14px/1.35`; optional tabular monospace numeric values. Use 20px minimum panel padding, a 20px layout gap and an approximately 1120px maximum reading/application width. These numbers are responsive starting points, not era specifications. Reflow content; do not shrink a fixed scene to mobile.

Keep text and focus indicators on solid surfaces. Decorative texture and geometry should reuse the entry’s own shape system, stay inert, and leave open reading zones. Default state changes can be immediate; any optional 120–240ms transition must preserve a complete still state.

## Typography / Fonts

Geometric/condensed sans titles with restrained serif or mono liner-note contrast. Proposed current pairing. Japanese text must be meaningful, correctly encoded and supported by licensed fonts; English-only original copy is valid.

## Cultural / Ethical Notes

1990s Japanese record/design networks, Mitsuo Shindo, Groovisions and other specific makers. Sampling is an active design method, not permission to copy copyrighted source art. Reissues must retain their own publication dates. Credit creators and preserve uncertainty; source access is not a reuse license. Do not trace signature compositions, copy characters/marks, or turn sacred/personal symbols into generic ornament. Keep demonstration prices, schedules and form outcomes honest. Historical archive images dominate the pool, supplemented with five primary-source packaging works. Some individual attributions are archival. The 800 Cherries Romantico image is a 2023 reissue of 1998 music. One grid poster is one authored work, not a separate count per tile.

## Anti-Patterns

Every Japanese cover called Shibuya-kei; decorative fake Japanese; mandatory city-pop sunsets; copied artist portraits; attributing 2023 reissue art to 1998; conflating a sleeve’s release title with its date.

## Source Notes

The [research profile](../../../knowledge/aesthetics/shibuya-kei-graphics.md) records 31 qualifying unique inspected artifacts, source distribution, grouped views, exclusions and confidence limits. Exact colors and UI behavior above are authored application proposals. Context:

- [First-person Mitsuo Shindo interview, originally 2015, on sampling and making older references fresh.](https://true-false.io/masatoyamaguchi/blogs/text/shindo)
- [Primary studio history: Kyoto formation, Pizzicato Five work and Tokyo move.](https://groovisions.com/about/)
- [Primary project record, 1996 Great White Wonder packaging/poster system.](https://groovisions.com/works/pizzicato-five/)
- [Primary FPM packaging projects and collaborators, dates and media.](https://groovisions.com/works/fpm2/)
- [Institutional retrospective credits refine art-direction/designer distinctions; text consulted, PDF not counted as visual inspection.](https://www.setabun.or.jp/wp/wp-content/uploads/2021/08/shindo_PRvol2.pdf)
