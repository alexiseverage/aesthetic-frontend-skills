---
slug: handheld-creature-encyclopedias
label: Handheld Creature Encyclopedias
family: digital-internet-native
era: Late1990s–present portable creature-record interfaces and descendants
aliases: ["portable creature index UI", "creature field-guide interfaces"]
status: canonical
evidence_level: standard
related: ["8-bit-pixel", "skeuomorphism", "wiki-encyclopedia-vernacular", "cozy-life-sim-interfaces"]
subsets: []
---

# Handheld Creature Encyclopedias

## Scope

A descriptive interface grammar for portable creature-record systems: numbered entries, selected-specimen viewport, concise attributes, collection/discovery status, and practical search or reorder controls. Early LCD/pixel indexes, dual-screen records, contemporary portable console indexes and phone descendants share this information task while differing materially in appearance. It is not a name for all Pokémon art or a claim of one historical movement.

The [research profile](../../../knowledge/aesthetics/handheld-creature-encyclopedias.md) documents30 unique works,26 complete published interface images and four official manuals with inspected screen diagrams. Pokémon dominates29/30; Yo-kai Watch3 provides a useful medal-binder comparison. Multiple states, platforms of HOME and close sequel recolors are deduplicated. The evidence supports this concentrated lineage rather than a universal account of all creature-collecting games.

## 7-Dimension Profile

**Palette**: Early monochrome pink/green LCD and black fields give way to red, blue, yellow, teal and lavender display planes. Strong selected bands, reversed names and status marks carry operational hierarchy. White/cream record fields and pale specimen grounds remain common. There is no mandatory red casing: Arceus uses a paper research book, Quest an open book, and GO a pale phone matrix. Preserve readable foreground/ground contrast and a distinct selection signal.

**Type**: Compact pixel uppercase and short numeric fields dominate early screens; later systems use small mixed-case sans text, table labels and larger creature names. Index numbers, names, status, dimensions and descriptive prose occupy different levels. Use a monospace display for indexes with readable sans body text; source game fonts remain unidentified. Reproduce hierarchy and economical wording rather than tiny handheld raster sizes.

**Texture**: LCD pixels, graph grids, striped instrument grounds, glossy/beveled metal rails and crisp inset screens form electronic branches. Paper and book variants are documented counterexamples. Texture surrounds data instead of obscuring it. A faint grid can support the specimen window; mandatory scanline animation, damaged screens and heavy glitch are unsupported shortcuts.

**Shape**: Bounded specimen viewport, numbered rows or thumbnails, selection brackets/cursor, narrow status strip and command rail. Rounded or beveled frames coexist with sharp pixel boxes. Unknown entries may use silhouettes, question marks or numbers. A device silhouette is useful but not sufficient: its controls and record layout must perform the encyclopedia task.

**Motion**: Still images establish composition, not timing. Manuals document rotation, zoom, screen switching, search, sorting and pause/resume; GO support describes registration animation. Actual game playback was not inspected, so easing, duration and sound remain unknown. Proposed web adaptation uses intentional stillness and immediate record/filter/note updates for comparison. No flashing status lamp, idle specimen bob or forced reveal is required; reduced motion keeps the same complete workflow.

**Spatial**: List/index and selected specimen/attributes form paired regions, split across screens in some handhelds. Compact counters and command hints surround that core. Modern examples may replace the list with a thumbnail matrix or shelf of numbered books. On narrow web layouts, stack index controls and record in reading order rather than shrink a two-screen image. Retain selected heading, current index and search state.

**Cultural markers**: Field research, creature discovery, collection progress, taxonomy, habitat, fictional abilities and personal logs. The original games' species, regional lore and branded devices belong to their creators. Make new creatures and terminology; neither a copied mascot nor a ball logo is necessary. Seen, documented and unknown states should be explicitly named rather than represented by color alone.

## Non-Negotiables

**Non-negotiables**: A working indexed collection; a selected specimen with structured data; explicit discovery/registration state; coherent display/list/command hierarchy. The interface itself must convey the field-guide device or record system, beyond placing creature images in generic cards.

## Connotation

**Mode:** nostalgic quotation with a contemporary usable field-guide task.

Conveys curiosity, portable reference and completing a personal record. It can be scientific-looking without claiming real biological data. Clearly label fictional habitats and measurements, avoid coercive completion streaks, and allow browsing without enforced discovery gates.

## Related / Subsets

- **Pixel Art** supplies one rendering method; later3D and book indexes show that pixels are not the definition. This system requires indexed records and discovery status.
- **Skeuomorphism** supplies device/book affordances broadly; this entry narrows them to creature reference and collection tasks.
- **Wiki Encyclopedia Vernacular** uses links, citations, revision and article structure. A portable creature index emphasizes selected specimens, short attributes and registration status rather than general article editing.
- **Cozy Life-Sim Interfaces** organizes belongings, materials and making. This entry organizes numbered creature knowledge; decorative creature imagery alone establishes neither.

Supported branches are monochrome LCD lists, colored pixel instruments, dual-screen data/index pairs, modern portable matrices and illustrated record books. These are descriptive variants, not separate historical movements.

## Frontend / UI Guidance

Build a searchable record browser with number/name ordering, habitat filtering, visible result count, an empty state and clear reset. Pair a persistent selected-item heading with specimen image, status and structured attributes. A collection state change must update its counters. If filtering removes the selected record, either select the first visible record or explain that selection is outside the filter; never show a misleading highlighted row.

Native radios can select records, native selects can filter/order and buttons can document or clear a field record. Do not fake D-pad functionality or rely on sound, hover or drag. Add text labels to status symbols, accessible names to controls and focus rims distinct from selected brackets. Note forms should trim whitespace, associate errors, preserve per-record drafts on navigation and export actual saved data. State page-only persistence honestly within the field log.

Use desktop index/detail columns and mobile stacked panes.44px controls,16px working text and wrapping names adapt the grammar without importing old hardware limitations. Keep the authored screen legible in either host theme; avoid making the entire device too low contrast to resemble an LCD. Stillness is suitable for close comparison and note writing.

## CSS Translation

Authored web tokens, not recovered game source code:

```css
.fieldlink { --shell:#d34c39; --ink:#182f35; --screen:#e8f0da; --muted:#40564c; --select:#244e53; --focus:#132e72; background:var(--shell); color:var(--ink); border:3px solid #6d2d28; border-radius:34px 34px 14px 14px; box-shadow:0 9px 0 #762e28; font:16px/1.5 Arial,sans-serif; }
.fieldlink-screen { background:var(--screen); border:5px solid #344b48; border-radius:12px; }
.fieldlink-index { font:700 14px/1.4 "Courier New",monospace; font-variant-numeric:tabular-nums; }
.fieldlink-record[aria-checked="true"] { background:var(--select); color:#fff; border-inline-start:6px solid #e8bd55; }
.fieldlink button,.fieldlink input,.fieldlink select { min-height:44px; }
.fieldlink :focus-visible { outline:3px solid var(--focus); outline-offset:4px; }
.fieldlink *,.fieldlink *::before,.fieldlink *::after { animation:none; transition:none; }
```

Proposed spacing4/8/12/16/24/32px; specimen viewport square, data definition list two columns, desktop index around36% and record64%, mobile stack at680px. Display title28–48px, names24–32px, index14px, body16px. Keep texture in decorative viewport background, never over data. No timing or breakpoint is presented as measured from the source games.

## Typography / Fonts

Courier New/monospace indexes and Arial/sans-serif working text require no font download and offer broad system fallback. Use short tracked uppercase for device labels only. Do not use a proprietary game wordmark as a font or apply pixelated rendering to ordinary prose. Localized names must wrap without losing index/status; provide script-appropriate system fallbacks.

## Cultural / Ethical Notes

Credit publisher and identifiable UI authors separately. Full source screens/manuals were analyzed, not licensed for redistribution. Use original creatures, silhouettes, names and device details; avoid branded names, logos, characteristic mascot likenesses and copied lore. Do not conflate Pokémon, Yo-kai or other regional creature traditions. Fictional attributes are editorial content, not real zoological facts. Collection completion must remain optional.

## Anti-Patterns

- Generic image cards with an unchanged app toolbar.
- A decorative device whose list, filters, counters or buttons do nothing.
- Treating all variants as red, pixelated, tiny, glitchy or animated.
- Status communicated only by a silhouette or color; inaccessible unknown entries.
- Unlabeled D-pad controls, forced audio, flashing LEDs, mandatory drag or autoplay.
- Presenting static references as proof of actual motion or current app behavior.
