---
slug: paint-by-number
label: Paint by Number
family: material-print-craft
era: "Commercial hobby kits from the mid-twentieth century onward"
aliases: ["Paint-by-numbers","Malen nach Zahlen"]
status: canonical
evidence_level: standard
related: ["pop-art","patchwork-quilting"]
subsets: []
---

# Paint by Number

## Scope

A numbered-region painting system translated into a visual language: bounded shapes, indexed color keys and a visible journey from unpainted template to assembled picture. Finished paintings may conceal their numbers and outlines. This scope includes historical and current hobby kits, rather than all flat illustration or all amateur painting.

## 7-Dimension Profile

**Palette**: A finite keyed palette, from muted olive, cream and rust in historical landscapes to saturated turquoise, violet and yellow in current kits. No universal vintage palette. Suggested UI colors are estimates, not physical paint measurements.

**Type**: Numbers are functional identifiers on templates and keys, while packaging uses varied display lettering. Pair clear tabular numerals with a readable interface face; do not pretend a packaging font defines all kits.

**Texture**: Discrete paint regions and subtle canvas or board grain. Paint coverage can soften outlines in finished work. Avoid a heavy grunge layer that obscures the region map.

**Shape**: Nested irregular closed regions model foliage, water, garments and architectural planes. Small regions cluster in details; broad fields establish sky and depth. Region boundaries are not necessarily black in finished pictures.

**Motion**: No historical timing established from stills. Proposed UI: an immediate region-fill state with an optional 160 ms opacity transition; reduced motion receives the same completed state without animation.

**Spatial**: One composition resolves from many interlocking areas. A separate numbered key supports navigation. Multiple panels may continue one image and count as one work.

**Cultural markers**: Commercial hobby painting, accessible stepwise making and the contribution of kit designers alongside hobby painters. The sampled corpus spans historical US manufacturers and current German kits; it is not a global census.

## Non-Negotiables

**Non-negotiables**: Closed paint regions organized into a coherent composition; a meaningful indexed key or stepwise completion relationship; readable controls separate from fine decorative detail.

## Connotation

**Mode:** playful, patient, gently rewarding.

A small achievable project, a box of possibilities and the pleasure of seeing separate parts become one picture. Avoid claims about therapeutic efficacy.

## Related / Subsets

Related to patchwork-quilting through assembly of many bounded regions, but uses indexed paint rather than sewn pieces. Pop-art can share flat color, but does not require a numbered production key. This is a distinct craft/process translation.

## Frontend / UI Guidance

Build a project checklist or onboarding progress tracker whose numbered key buttons correspond to original painted regions. Completing a real task fills its matching region and updates a textual completion count. Offer ordinary checkbox controls, explicit undo/reset and a final complete state. Do not require precise tapping on tiny painted cells.

## CSS Translation

Use an original SVG with shared numbered region identifiers, CSS custom properties for the finite paint palette and a paper-colored base. Keep form text in HTML. A 160 ms fill/opacity change is proposed; disable transitions under prefers-reduced-motion. Use a single-column key below the picture on narrow screens.

## Typography / Fonts

Readable humanist sans for tasks and tabular numerals for keys. Packaging lettering can inspire a small optional title, but no historical font identification is asserted.

## Cultural / Ethical Notes

Credit kit designers and unknown hobby painters separately. Do not trace commercial paintings, licensed characters or museum reproductions into production assets. Original region drawings should serve the interface and avoid implying an authentic vintage kit.

## Anti-Patterns

- Treating every flat illustration as paint by number.
- Leaving illegible decorative numbers over finished content.
- Requiring color perception or tiny region targets to complete a task.
- Using an AI-marked lifestyle image as historical evidence.

## Source Notes

The [research profile](../../../knowledge/aesthetics/paint-by-number.md) records 31 unique inspected artifacts, claims and limits. [Paint By Number Museum collection](https://www.paintbynumbermuseum.com/search-the-collection); [Schipper landscape kits](https://www.malennachzahlen-schipper.com/schipper_en/categories/landscapes/); [Grant and Goodridge exhibition catalogue](https://20northgallery.com/wp-content/uploads/2018/12/20N_Grant-Goodridge-Paint-By-Number-Collections_exhibit-catalogue_2nd-edition_web-rdcd_12.18.2018.pdf).
