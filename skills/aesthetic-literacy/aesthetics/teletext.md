---
slug: teletext
label: Teletext
family: technical-institutional
era: 1970s European broadcast services; continuing services, art and web interpretations
aliases: ["Broadcast teletext", "Teletext design", "Ceefax-style teletext"]
status: canonical
evidence_level: standard
related: ["8-bit-pixel", "bloomberg-terminal-monochrome", "early-internet"]
subsets: []
---

# Teletext

## Scope

The character-cell visual language of European broadcast teletext and its documented artistic continuations: constrained lettering/mosaic graphics, saturated role colors, compact page panels and, in information services, numeric addresses and structured directories. This is a medium-derived system, not a single movement or a generic retro-computer theme.

The 1976 UK specification defines a 24-row, 40-character page, character-based graphics and display controls. That historical format is a useful reference, not a universal claim about every teletext standard or a reason to shrink modern text. Art-only interpretations need teletext process/context, since pixelation alone also belongs to many other systems.

## 7-Dimension Profile

**Palette**: Black, white and saturated red/green/yellow/blue/magenta/cyan roles; black grounds are common, while white fields, blue panels and colored bands also occur. Use color to separate titles, links, page numbers and sections. Essential dark-blue-on-black text is a contrast failure even when historically evocative.

**Type**: Character-cell alignment, monospaced numerals and labels, constructed mosaic wordmarks, short rows and occasional double-height headings. Mixed case is legitimate. Exact glyph forms vary by hardware/renderer; no universal teletext font is established by the corpus.

**Texture**: Hard cell edges, stepped diagonals, contiguous or separated mosaic patterns, checker-like tonal shorthand and intentionally flat fields. Some artworks are entirely text. Scanlines, blur, bloom and damaged signal are optional receiver quotations, not the medium's defining texture.

**Shape**: Rectangular title/footer bands, numeric directory rows, dot leaders, block pictures and sparse character drawings. Saturated panel changes provide hierarchy without rounded cards or drop shadows. Artistic compositions may be portraits, diagrams, text or sparse symbols.

**Motion**: Stable pages and explicit page/subpage changes are central to the inspected information interfaces. One artist GIF cycles discrete compositions; static captures do not establish receiver flash or cycle timings. Prefer stillness for reading, deliberate swaps and optional reveal actions. Do not require blinking; preserve every state under reduced motion.

**Spatial**: Compact aligned columns, short text groups, stable address/status rows, subordinate page references and clear band/column divisions. Both dense directories and generous black-space art occur. Reflow useful information on mobile while retaining alignment and page identity; a literal tiny television emulator is not required.

**Cultural markers**: Broadcast information services such as Ceefax, ORACLE, 4-Tel, NOS Teletekst, ARD Text and Yle Teksti-TV; numbered pages, subpages, topic indexes, programme schedules, weather diagrams and contemporary teletext art. These services are examples, not interchangeable brands or a single national tradition.

## Non-Negotiables

**Non-negotiables**: Character-cell/constructed-mosaic logic; disciplined limited color roles and hard geometry; a coherent chosen branch. For software, preserve numeric page/reference hierarchy and readable information organization. A standalone artwork must retain documented teletext context rather than relying on arbitrary game pixels.

## Connotation

**Mode:** contemporary interpretation of a continuing broadcast medium, or nostalgic quotation of a named period/service. Signals economical, direct public information and constrained digital craft. Some services and artists remain active; do not call the entire medium extinct or confuse it with the web's origin.

## Related / Subsets

- **8-Bit / Pixel Aesthetic**: shares low-resolution graphics and restricted palettes; game sprites, scores and tile worlds are not teletext's information-address system.
- **Bloomberg Terminal Monochrome**: shares compact numerical information; finance commands, live ticks and simultaneous expert panes are different from broadcast pages/subpages.
- **Early Internet / Web 1.0**: shares low-fidelity directories; browser chrome, tiled GIF backgrounds, webrings and homepage culture are not required here.
- Service-page, mosaic-art and text-art branches belong within this entry. Do not equate all global teletext/videotex protocols with the European source corpus.

## Frontend / UI Guidance

Use a useful directory, event schedule, reference browser, media guide or compact information dashboard. Numeric page lookup can be a real labeled form with validation; topic navigation must remain understandable without knowing page codes. Use proper tables for tabular schedules, real links/buttons and explicit saved/selected state. A reveal/disclosure is appropriate for optional details, with readable labels and complete keyboard support.

Use HTML for semantic content and opaque fields for reading. Decorative mosaic marks should be hidden from assistive technology. Distinguish the current page from a pending/error state; do not simulate a broadcast wait or publish invented current news. Announce significant content changes and move focus deliberately when replacing a view.

## CSS Translation

Proposed screen roles: background `#000000`, text `#FFFFFF`, section/link `#00FFFF`, identifier `#FFFF00`, saved/positive `#00FF00`, accent `#FF00FF`, warning `#FF5555`, title/action field `#0000BB`. These are contemporary values, not sampled broadcast colors. White on blue is useful; blue on black is not suitable for essential text. Pair color with a label, underline, state mark or code.

Use 0px radii, solid rules, flat title strips, tabular numerals, monospaced layout roles and a 4/8/12/16/24px spacing scale. Keep body text around 16px with comfortable leading. Numeric columns can align with CSS grid/table; content should wrap or reflow at narrow widths. Use integer-coordinate SVG/CSS mosaic assets with crisp edges. Disable inherited site animation/transitions for deliberate stillness and include an explicit reduced-motion branch.

## Typography / Fonts

System monospace or Courier New can carry a readable modern interpretation; a correctly licensed teletext-specific font may improve glyph fidelity when its character coverage is adequate. Document any added font's source/license and fallback. Constructed mosaic lettering belongs in short titles or decorative graphics, never as the only accessible copy. Preserve lowercase and accented content rather than forcing all prose into capitals.

## Cultural / Ethical Notes

Credit artists and broadcaster archives; inspection does not grant image/font/logo reuse rights. Create original titles/mosaics rather than copying broadcaster marks. Clearly label fictional listings or simulated data. Art can engage politics, celebrity or regional symbols; these subjects are not mandatory teletext motifs, and depicted allegations must not become factual product copy. Optional flashing should be omitted for ordinary software.

## Anti-Patterns

- Generic gaming sprites or green hacker terminals presented as the whole medium.
- Saturated color without page/reference or character-cell structure.
- Blurred type, compulsory CRT curvature, glass panels or soft floating cards.
- Essential text squeezed into a 40-column miniature on a phone.
- Color-only links, undocumented codes, fake loading delays, automatic page cycling or essential blinking.

## Source Notes

[1976 BBC/IBA/BREMA specification, transcribed mirror](https://decode-orc.github.io/analogue-video-specifications/teletext/BBC-Broadcast-Teletext-1976/BBC-Broadcast-Teletext-1976/), [mb21 archive](https://teletext.mb21.co.uk/gallery/oracle/main1.shtml), [MUTA collection](https://www.vilkecollection.fi/muta/index.html), [Horsenburger](https://www.horsenburger.com/teletextartgallery), [Paula Lehtonen](https://www.paulalehtonen.net/paula_lehtonen/works_pages/teletextart.html), and the inspected [NOS](https://nos.nl/teletekst), [ARD](https://www.ard-text.de/) and [Yle](https://yle.fi/aihe/tekstitv?P=100) viewers support the boundary. The research profile documents 30 unique qualifying artifacts, grouped views, one excluded low-information example and the source bias.
