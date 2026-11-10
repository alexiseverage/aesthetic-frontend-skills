---
slug: makeup-face-chart-studio
label: Makeup Face-Chart Studio
family: technical-institutional
era: Contemporary makeup planning, backstage worksheets and chart art
aliases: ["makeup planning sheets", "facechart studio"]
status: canonical
evidence_level: standard
related: ["model-comp-cards", "anatomical-flap-atlases", "photographic-contact-sheet"]
subsets: []
---

# Makeup Face-Chart Studio

## Scope

A working beauty graphic in which a printed or drawn face carries localized pigment and a record of the intended look. Product recipes, swatches, feature names, ruled notes and artist labels make it useful for planning and communication. Rich chart art and spare backstage sheets are both documented branches. A beauty portrait behind conventional controls does not establish this system.

The [research profile](../../../knowledge/aesthetics/makeup-face-chart-studio.md) analyzes 30 unique works, with contemporary brand and individual-artist concentration disclosed. Exact invention history remains unknown; no universal face shape, complexion or pink palette is implied.

## 7-Dimension Profile

**Palette**: White or warm white paper, dark or fine gray contours, localized cosmetic color. Warm neutrals, vivid blue/violet, red lips, pink cheeks, metallic accents and fantasy skin treatments coexist. Treat paper, contour and pigment as distinct roles. A skin-tone field is optional; uncolored templates can carry the plan.

**Type**: Restrained worksheet labels, handwritten product notes and small artist/brand credits. Educational and campaign sheets add numbered steps, condensed headers or short brush subheads. Keep editable recipe text legible; handwriting is a limited annotation voice, not the sole interface face.

**Texture**: Powder grain, pencil lashes, soft shading, visible paper, smudged swatches and drawn glossy highlights. Actual foil or stones occur in expressive studies. Preserve crisp text and contours around material effects. A glossy painted highlight is not proof of a reflective screen animation.

**Shape**: Face and feature outlines; eye, cheek and lip regions; short strokes and pigment pans; ruled fields and small recipe/detail panels. Fine-line, broad-outline, frontal and three-quarter templates differ. Use original feature drawings instead of tracing proprietary chart templates.

**Motion**: Static planning and comparison dominate the inspected evidence. Still updates suit color/zone changes and saved feedback. Avoid autoplay, moving faces and flashing glitter. Optional transition timing is a contemporary proposal and should become immediate under reduced motion.

**Spatial**: A dominant open face workspace with subordinate recipe, swatch and metadata regions. Practical sheets often place the face above ruled product notes; instructional posters add sequential detail blocks. Preserve paper margins, clear zones and a readable writing area as the layout stacks on mobile.

**Cultural markers**: Makeup artists, backstage team communication, cosmetics counters, beauty education, client planning and expressive chart-making. Brand and artist sources document specific practice rather than a universal beauty norm. These are working documents as well as artworks.

## Non-Negotiables

**Non-negotiables**: A recognizable original face/feature plan; localized pigment rather than a decorative image alone; meaningful look/zone/recipe information; open paper and clear contour hierarchy.

## Connotation

**Mode:** contemporary revival.

Conveys preparation, craft, experimentation and an artist’s working process. A digital planner can feel like a studio sheet while offering accessible native controls. Avoid medical authority, simulated skin analysis and claims that one template represents every client.

## Related / Subsets

- **Model Comp Cards** pair photographs and casting information; face charts communicate a designed makeup look.
- **Anatomical Flap Atlases** reveal anatomical structures; this system maps cosmetic intent and product notes.
- **Photographic Contact Sheet** organizes repeated exposures; the chart centers a dominant face plan and recipe.

Backstage recipe sheet, blank training template, rendered chart art and campaign look tutorial are descriptive branches. They are not additional canonical subsets.

## Frontend / UI Guidance

Build a look-planning form whose fields, pigment controls and disclosures belong to the sheet. Let users select a feature zone, choose a named pigment, inspect a finish and record a look name or notes. Update the face graphic and an equivalent text recipe together. Make saved state clear and invalidate it when the plan changes.

Use real labels, native buttons/radios/selects and visible focus. A swatch needs a name and selected indicator beyond hue. Keep essential controls outside facial contours rather than relying on tiny drawing hotspots. On mobile, stack pigment and recipe tools below the face with full-width touch targets. Provide a text summary of the illustration, and keep custom SVG IDs unique when the component appears more than once.

## CSS Translation

Proposed application values, not recovered historical specifications:

```css
.face-studio {
  --paper: #fffdf8;
  --ink: #342b30;
  --rule: #b4a5a4;
  --pigment: #964568;
  color: var(--ink);
  background: var(--paper);
  font-family: Arial, sans-serif;
}
.face-studio :focus-visible {
  outline: 3px solid #6c3455;
  outline-offset: 4px;
}
.face-studio input,
.face-studio textarea {
  border: 0;
  border-bottom: 1px solid var(--rule);
  border-radius: 0;
}
```

Use 1px worksheet rules, generous paper margins and a dominant face column with a narrower pigment/recipe rail. Soft SVG radial gradients and small deterministic dot patterns can suggest powder without filtering text. Keep zones in separate paths so changes are localized. Use `minmax(0,1fr)`, flexible labels and `min-width:0`; do not shrink handwriting to preserve a desktop sheet. Intentional stillness should also remove inherited control transitions.

## Typography / Fonts

A plain sans serif supports small labels and recipes; a restrained serif studio title or short handwritten note can provide contrast. System Georgia/Arial and an italic annotation are a viable zero-download combination. Custom handwriting must remain readable and licensed. Do not copy a cosmetics wordmark or a real artist’s signature as decoration. Keep numbers, pigment names and instructions as selectable text.

## Cultural / Ethical Notes

Original or cleared chart art is required; the linked references are not an asset pack. Offer an inclusive interpretation without treating a face template as a biological standard or an ethnicity classifier. Do not attach real artist endorsements, invented client data or real-person quotes to a fictional studio. Cosmetic ingredients, medical effects and skin-safe application advice require separate evidence; a digital pigment planner need not make those claims. Craft-material experiments on paper are not instructions to apply those materials to skin.

## Anti-Patterns

- A beauty photo gallery with generic form cards and pink styling.
- A decorative face with no usable zone, pigment or recipe relationship.
- Unlabeled color-only swatches, tiny hotspots and handwritten body text.
- Simulated clinical analysis or a universal ideal face.
- Counting cropped eyes, process frames, template pages or repeated backstage views as unrelated works.
