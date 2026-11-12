---
slug: wacky-pomo
label: "Wacky Pomo"
family: vernacular-commercial
era: "late 1980s–early 2000s commercial graphics; later revivals"
aliases: ["Wonka Pomo"]
status: canonical
evidence_level: standard
related: ["memphis", "kidcore", "clowncore", "groovival"]
subsets: []
---

# Wacky Pomo

## Scope

A retrospective commercial cluster of warped signs, cartoon apparatus and exuberant dimensional lettering across children’s television, packaging, retail and early software. The transferable system is playful construction: uneven contours, exaggerated depth and clear activity zones. It is more specific than bright colors or a Memphis squiggle.

## 7-Dimension Profile

**Palette**: Hot orange, lime, purple, cyan and yellow with strong dark outlines and white reading areas. Two or three dominant colors can be enough; full rainbow is a variant, not a requirement.

**Type**: Bulging, pinched, tilted or irregular short lettering often has an outline, extrusion or contrasting shadow. Ordinary sans labels and straight captions coexist with display distortion. Neither every letter nor every text baseline must wobble.

**Texture**: Molded plastic, rubbery bevels, cartoon machinery, cut paper and illustrated light effects. Selectively contrast slick rounded objects with flat sign panels; indiscriminate grain is not a defining trait.

**Shape**: Asymmetric lobes, splats, zigzags, springs, tubes and comic machine parts. Repeat a small coherent shape vocabulary through enclosures, buttons and dividers; preserve obvious clickable interiors.

**Spatial**: Nested activity compartments around a large irregular title or central apparatus. Hard rectangular information areas can sit inside an unruly frame. Let outline and color separate layers; mobile should stack complete activity zones.

**Cultural markers**: Youth-oriented commercial play, surprise, experimentation and comic inventions. Nickelodeon is one important source among toy, food, retail and software examples; do not make a network’s slime or characters compulsory.

**Motion**: Historical timing/easing is unknown in this still-led corpus. A current application may be intentionally still, with immediate state changes or brief optional feedback. Any squash, reveal or parameter transition is a design proposal, not an observed historical standard. Reduced motion preserves the complete composition and every task.

## Non-Negotiables

**Non-negotiables**: Irregular constructed display or enclosures; exaggerated material/depth cues; purposeful cartoon apparatus or contour rhythm; stable readable task areas.

## Connotation

**Mode:** nostalgic quotation.

Youth-oriented commercial play, surprise, experimentation and comic inventions. Nickelodeon is one important source among toy, food, retail and software examples; do not make a network’s slime or characters compulsory. Strong decorative cues require editing around the task; recognition should come from the whole material/type/space system rather than copied source imagery.

## Related / Subsets

Memphis emphasizes patterned geometric surfaces; Wacky Pomo adds cartoon apparatus and distorted object-like lettering. Kidcore is broader childhood color/toy culture. Clowncore does not own every playful irregular form. Groovival centers revival flowers and retro letter rhythm.

Related catalog owners: `memphis`, `kidcore`, `clowncore`, `groovival`. Internal variants remain descriptive unless they establish a separately useful, researched system.

## Frontend / UI Guidance

Build a party challenge builder: choose activities, expand rules and add tickets to a visible basket. Use a springy outline on selection, irregular number tabs and an apparatus-like header. Keep rule text and quantities on plain panels.

Use real buttons, labeled inputs and visible selected/disabled/error states. Support keyboard operation, 44px touch targets and announced feedback. Reflow modules on narrow screens; decorative geometry must not intercept pointer events or obscure focus. Use original abstract/object artwork; people imagery and copied source screenshots should not carry the interface identity.

## CSS Translation

All values below are **proposed application tokens**, estimated from the visual family and authored for current web use; they are not sampled historical measurements.

```css
.aesthetic-surface {
  --background: #FFF5CD;
  --surface: #FFFFFF;
  --text: #241532;
  --text-muted: #615266;
  --primary: #6638A6;
  --secondary: #DB3E12;
  --accent: #B5E744;
  --radius-small: 8px;
  --radius-medium: 24px;
  --radius-large: 40px;
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

Typography proposal: rounded display, 700 weight, `clamp(2rem, 5vw, 4.5rem)/1.05`, tracking `-.02em`; system sans reading face, 400 weight, `16px/1.55`; 600-weight utility labels, `14px/1.35`; optional tabular monospace numeric values. Use 20px minimum panel padding, a 20px layout gap and an approximately 1120px maximum reading/application width. These numbers are responsive starting points, not era specifications. Reflow content; do not shrink a fixed scene to mobile.

Keep text and focus indicators on solid surfaces. Decorative texture and geometry should reuse the entry’s own shape system, stay inert, and leave open reading zones. Default state changes can be immediate; any optional 120–240ms transition must preserve a complete still state.

## Typography / Fonts

Rounded or irregular display paired with system sans. A custom outlined HTML heading is a current translation; no universal Wacky Pomo font is established. Reserve distorted treatment for short titles.

## Cultural / Ethical Notes

Youth-oriented commercial play, surprise, experimentation and comic inventions. Nickelodeon is one important source among toy, food, retail and software examples; do not make a network’s slime or characters compulsory. Credit creators and preserve uncertainty; source access is not a reuse license. Do not trace signature compositions, copy characters/marks, or turn sacred/personal symbols into generic ornament. Keep demonstration prices, schedules and form outcomes honest. Archive-attributed creator/date fields remain qualified where originals were not recovered. The research is still-led: historic timing, easing and hidden software states were not measured.

## Anti-Patterns

Generic rainbow cards; copying Nickelodeon marks or characters; rotating body text; every label in a novelty font; hidden controls disguised as scenery.

## Source Notes

The [research profile](../../../knowledge/aesthetics/wacky-pomo.md) records 30 qualifying unique inspected artifacts, source distribution, grouped views, exclusions and confidence limits. Exact colors and UI behavior above are authored application proposals. Context:

- [Retrospective name and archive scope; not an original movement manifesto.](https://cari.institute/aesthetics/wacky-pomo)
- [First-person production-design oral history; supports tactile sets, playful machinery and commercial context.](https://www.theringer.com/2021/08/10/tv/nickelodeon-network-style-slime-history-double-dare)
- [Designer account of the 2013 revival, dynamic grids and mixed type; its credits must not be retroactively assigned to the 1990s.](https://www.a-o-k.net/nick-jr2)
