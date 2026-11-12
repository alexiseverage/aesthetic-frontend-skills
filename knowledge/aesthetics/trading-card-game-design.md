---
slug: trading-card-game-design
label: Trading Card Game Design
first_researched: "2026-07-08"
last_updated: "2026-11-12"
source: mixed
image_count: 32
evidence_level: standard
new_aesthetic: false
aliases: ["TCG design", "CCG frame design", "collectible card UI"]
---

# Trading Card Game Design

## Dimension Synthesis

Updated 2026-11-12 from 32 complete individually inspected card artifacts. These are recurring structures and documented exceptions, not population-frequency percentages.

| Dimension | Recurring grammar | Exceptions / limits | Confidence |
|---|---|---|---|
| Palette | Color codes identity/resources, while pale rules zones contrast with art and dark/metallic frames. | Mono and multicolor, black/white/silver and full-art variants differ by game; rarity is not always encoded by hue. Visually estimated, not sampled tokens. | High. |
| Type | Ranked name, cost/resource, classification, mechanics, statistics and tiny collector/artist/legal metadata. | Medieval serif, readable serif and condensed sans differ. Exact cross-game fonts unverified. | High. |
| Texture | Marbled/stone/paper frames, metallic bevels, pale rules panels and premium/foil-looking printed variants. | Still scans cannot establish foil reflectance, embossing, viewing-angle response or animated shimmer. Ordinary flat cards are valid. | High for visible treatment, unknown for physical dynamics. |
| Shape | Usually rounded rectangular object with art, title, rules and symbol zones; costs/stat medallions encode roles. | Full-art continuity, split Class layout and sideways Lorcana location show non-universal frame geometry. | High. |
| Motion | No historical animated/card-handling behavior inspected. | User selection, inspection and fixed finish comparison are proposed application behavior. | Unknown. |
| Spatial | Compact repeatable hierarchy permits visual comparison and rule retrieval. | Art can break the frame; not every card has combat values or a separated lower rules box. | High. |
| Cultural markers | Deck construction, resource identities, set/collector/rarity marks, illustrator credit and promotional variants. | Intellectual property, legal/tournament systems and rarity economies belong to their specific games. | High for sampled physical game families. |

## Image Descriptions

All 32 complete card faces were inspected individually. The [linked audit](../media-audits/trading-card-game-design.json) preserves identity, creator, source, exact image route and source-access limitations. No card art, logos, characters, icons or rules text are reused in an application.

- **MTG-LEA-46 — Air Elemental**, Richard Thomas. [Source](https://scryfall.com/card/lea/46/air-elemental?utm_source=api); [card](https://cards.scryfall.io/large/front/6/9/69c3b2a3-0daa-4d42-832d-fcdfda6555ea.jpg?1783948708). Thick black rounded perimeter, blue marbled frame, serif/medieval title and top-right mana symbols; bordered art window over pale rules panel, tiny artist credit and bottom-right 4/4 statistic.
- **MTG-LEA-47 — Ancestral Recall**, Mark Poole. [Source](https://scryfall.com/card/lea/47/ancestral-recall?utm_source=api); [card](https://cards.scryfall.io/large/front/7/0/70e7ddf2-5604-41e7-bb9d-ddd03d3e9d0b.jpg?1783948708). Blue marbled frame and pale wavy rules area, one top-right symbol, large centered short serif rule; name/art/type/rules/credit stack.
- **MTG-LEA-232 — Black Lotus**, Christopher Rush. [Source](https://scryfall.com/card/lea/232/black-lotus?utm_source=api); [card](https://cards.scryfall.io/large/front/b/0/b0faa7f2-b547-42c4-a810-839da50dadfe.jpg?1783948669). Brown artifact frame around a dark flower image, zero cost at upper right, parchment rules box with dense left-aligned text; no creature combat statistic.
- **MTG-LEA-186 — Birds of Paradise**, Mark Poole. [Source](https://scryfall.com/card/lea/186/birds-of-paradise?utm_source=api); [card](https://cards.scryfall.io/large/front/5/5/55fe6449-1f23-43dc-adee-d144cd505b5c.jpg?1783948679). Green mottled frame, pale title, upper-right tree resource symbol, art window, tan rules box and small 0/1 bottom-right stat.
- **MTG-LEA-161 — Lightning Bolt**, Christopher Rush. [Source](https://scryfall.com/card/lea/161/lightning-bolt?utm_source=api); [card](https://cards.scryfall.io/large/front/d/5/d573ef03-4730-45aa-93dd-e45ac1dbaf4a.jpg?1783948684). Red/pink marbled border and pale rules area, bright art rectangle, one resource symbol; short centered rule leaves substantial blank rules space.
- **MTG-LEA-24 — Holy Strength**, Anson Maddocks. [Source](https://scryfall.com/card/lea/24/holy-strength?utm_source=api); [card](https://cards.scryfall.io/large/front/e/9/e945a4cd-0eb1-4f54-898d-169ce2748a03.jpg?1783948712). White lace-textured frame with low-contrast pale title, ruled art window and pale rules box; white sun resource symbol top-right. Historical readability weakness is not a requirement to copy.
- **MTG-LEA-98 — Dark Ritual**, Sandra Everingham. [Source](https://scryfall.com/card/lea/98/dark-ritual?utm_source=api); [card](https://cards.scryfall.io/large/front/e/b/ebb6664d-23ca-456e-9916-afcd6f26aa7f.jpg?1783948697). Dark grey/black stone texture with pale title and skull resource symbol; tan rounded rules box stands apart from dark frame.
- **MTG-BLB-122 — Agate Assault**, Slawomir Maniak. [Source](https://scryfall.com/card/blb/122/agate-assault?utm_source=api); [card](https://cards.scryfall.io/large/front/7/d/7dd9946b-515e-4e0d-9da2-711e126e9fa6.jpg?1783910826). Narrow red stone frame; dark title on pale rounded name bar, mana circles upper right, type/set-symbol bar between art and rules, fine collector/artist/legal metadata in black footer.
- **MTG-BLB-82 — Agate-Blade Assassin**, Hristo D. Chukov. [Source](https://scryfall.com/card/blb/82/agate-blade-assassin?utm_source=api); [card](https://cards.scryfall.io/large/front/3/9/39ebb84a-1c52-4b07-9bd0-b360523b3a5b.jpg?1783910839). Grey stone frame and pale boxed title/type/rules zones; projecting bottom-right 1/3 stat lozenge; condensed footer.
- **MTG-BLB-204 — Alania, Divergent Storm**, Joshua Raphael. [Source](https://scryfall.com/card/blb/204/alania-divergent-storm?utm_source=api); [card](https://cards.scryfall.io/large/front/4/3/436d6a84-4cea-4ca7-94aa-9d08280652af.jpg?1783910801). Blue-red multicolor frame, gold title/type/rules edges and crown-like top contour for legendary card; lower oval holo stamp and projecting 3/5 stat.
- **MTG-BLB-123 — Alania's Pathmaker**, Jason Kang. [Source](https://scryfall.com/card/blb/123/alanias-pathmaker?utm_source=api); [card](https://cards.scryfall.io/large/front/d/3/d3871fe6-e26e-4ab4-bd81-7e3c7b8135c1.jpg?1783910825). Red modern frame, title/mana bar and broad art window; pale rules and italic flavor separated by fine line, projecting 4/2 lower-right box.
- **MTG-BLB-124 — Artist's Talent**, Lars Grant-West. [Source](https://scryfall.com/card/blb/124/artists-talent?utm_source=api); [card](https://cards.scryfall.io/large/front/8/b/8b9e51d9-189b-4dd6-87cb-628ea6373e81.jpg?1783910825). Class card splits illustration vertically at left from three stacked level/rules compartments at right; title above and type line below, no conventional large bottom rules box.
- **LOR-1190 — Rapunzel / 4/C1 EN 1**, Grace Tran / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_challenge1_4_13f6e83bc0dc15ba0eb9788650ddce23f3df3fd6/card). Full-art variant: large cost medallion upper-left, amber name band across lower art, strength/shield pair right, narrow classification band and translucent pale rules area with two right-edge lore diamonds.
- **LOR-661 — Elsa / 1TFC EN 3/P1**, Nicholas Kole / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_promo1_3_cef568880146687aee7fedbb77feabd987e0fdd1/card). Purple band with strong condensed white name/subtitle, cost at top-left, strength/willpower at right and parchment rules/flavor zone below; black footer carries event/set and artist marks.
- **LOR-1198 — Kuzco / 8/C1 EN 1**, Koni / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_challenge1_8_ed492b373e5a8049ce3dc162683fc52b879dbc66/card). Emerald full-art card with isolated numeric hexagon at top-left, green name/stat band, semitransparent rules area over continuous imagery and three stacked lore diamonds at right.
- **LOR-679 — Stitch / 21/P1 EN 1**, Alex Kupershmidt / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_promo1_21_f217671965746af13ac6a063b76ece7d3bd3a101/card). Borderless promo with handwritten artist signature inside illustration, red name strip, cost top-left, strength/shield right and three lore diamonds down right rules edge. Signature treatment is variant, not universal.
- **LOR-680 — Maleficent / 22/P1 EN 1**, Lorelay Bové / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_promo1_22_97ff0b8fcf7660222a56df648ae3323b5abcc8f4/card). Blue/sapphire name band below graphic illustration, cost upper-left, strength/shield pair and three lore symbols; translucent flavor area and black legal footer.
- **LOR-681 — Maui / 23/P1 EN 1**, Bill Schwab / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_promo1_23_972659d64f29f656a75e57fe9ea225d4664bef0f/card). Steel-grey name band on borderless signed promo, cost medallion upper-left, paired 8/8 stats, class strip, pale flavor zone and three lore diamonds.
- **LOR-34 — Ursula’s Shell Necklace / 34/204 EN 1**, Jenna Gray / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_set1_34_172c16efcf5b644bfe18dc49e3a096efea555286/card). Black rounded border and thin angular gold inner frame; amber all-caps name strip beneath art, item classification and parchment rules panel with one emphasized keyword, tiny bottom collector/artist/rarity marks.
- **LOR-170 — Scepter of Arendelle / 170/204 EN 1**, Grace Tran / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_set1_170_f07c278ba9ecd7b0a69c3de758c6cbe83d75ffe0/card). Sapphire item card with top-left inkable cost medallion, large object illustration, blue name band, item strip and parchment rules area. No character strength/willpower pair.
- **LOR-2459 — Dragon Fire / 9/C2 EN 1**, Luis Huerta / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_challenge2_9_2cbea7707b0ecf639c53a3ac5038c107d961dacc/card). Full-art action variant with dragon illustration continuing behind rules, numeric cost hexagon, red name/type bands, grey translucent rules region and curved gold bottom footer.
- **LOR-649 — Kuzco's Palace / 213/204 EN 3**, Roberto Gatto / publisher copyright retained. [Source](https://cards.disneylorcana.com/en-US/); [card](https://ravensburger.cloud/ci/lorcana_en_set3_213_82d560c154c3f6fd1c7252c74e8504dc29aa2fd8/card). Landscape location design stored sideways: cost medallion, left move-cost icon and right shield stat in horizontal play orientation, green title band and full-width rules strip below landscape. Portrait orientation is not universal.
- **PK-OP_Prize_SE7_EN_18 — Pokémon TCG card: Fezandipiti ex**, fokkyoo / The Pokémon Company copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series7/en-us/OP_Prize_SE7_EN_18-2x.png). Silver bevel perimeter, teal name/HP strip, game-type symbol upper-right, broad art, red ability lozenge and cost-symbol attack row; bottom weakness/retreat and ex-rule regions, artist/set code and prize stamp.
- **PK-OP_Prize_SE7_EN_36 — Pokémon TCG card: Lillie’s Clefairy ex**, 5ban Graphics / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series7/en-us/OP_Prize_SE7_EN_36-2x.png). Pink textured name/ability fields and silver bevel, art breaking into surrounding regions, trainer portrait inset, large 190 HP/type icon and bottom ex-rule box; illustrated highlights are not evidence of actual animated foil.
- **PK-OP_Prize_SE9_EN_25 — Pokémon TCG card: Mega Starmie ex**, 5ban Graphics / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_25-2x.png). Blue water frame with large 330 HP and evolution badge, art extends across rules, energy icons lead bold attacks with right damage numbers; broad silver/yellow special-rule footer.
- **PK-OP_Prize_SE9_EN_19 — Pokémon TCG card: Mega Dragonite ex**, aky CG Works / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_19-2x.png). Gold/yellow upper strip with large 370 HP and dragon type, evolution portrait, full-art spill behind lower ability/attack area, rounded special-rule footer and small collector metadata.
- **PK-OP_Prize_SE9_EN_26 — Pokémon TCG card: Mega Zygarde ex**, takuyoa / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_26-2x.png). Orange fighting identity and large HP; very dense multi-symbol attack costs down left, damage values at right, illustration behind rules and silver/yellow lower rule plaque.
- **PK-OP_Prize_SE9_EN_24 — Pokémon TCG card: Mega Skarmory ex**, 5ban Graphics / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_24-2x.png). Metallic silver card with large 260 HP and metal-type icon, full-art burst, one large attack row with resource icons and right damage; resistance/retreat strip and special-rule footer.
- **PK-OP_Prize_SE9_EN_62 — Pokémon TCG card: Poké Pad**, Studio Bora Inc. / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_62-2x.png). Trainer item card uses silver frame, wide header with blue Item label, name above bounded object picture, plain large rules area and rounded blue class-rule plaque at bottom; no HP/attack values.
- **PK-OP_Prize_SE9_EN_54 — Pokémon TCG card: Dawn**, Yuu Nishida / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_54-2x.png). Trainer supporter preserves silver frame/name/art/rules stack; orange class label and orange bottom restriction plaque distinguish it from blue Item card.
- **PK-OP_Prize_SE9_EN_28 — Pokémon TCG card: Meowth ex**, 5ban Graphics / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_28-2x.png). Silver-white name strip and 170 HP, image extends beyond art window, red ability marker above regular attack row and bottom ex-rule plaque.
- **PK-OP_Prize_SE9_EN_36 — Pokémon TCG card: Psyduck**, Jiro Sasumo / publisher copyright retained. [Source](https://play.pokemon.com/en-us/rewards/gallery/); [card](https://d1wx537rtdixyy.cloudfront.net/expansions/series9/en-us/OP_Prize_SE9_EN_36-2x.png). Ordinary blue water card with bounded illustration, small species strip, 70 HP, red ability marker, separate attack cost/damage and bottom weakness/retreat/flavor. No universal full-art spill or foil treatment.

## Direct Media Audit

32 selected full-media records, 32 unique qualifying still artifacts, 0 duplicate versions, 0 unresolved candidates or generated historical evidence, 0 downloaded reference files, 0 videos or interactive historical artifacts. Each card is an independently illustrated/composed artifact; this is not a claim of 32 unrelated frame templates. Floor 10 and working target 30 met.

Distribution: Magic 12 (7 Alpha and 5 Bloomburrow), Lorcana 10 across all six ink identities and character/item/action/location roles, Pokémon 10 with Pokémon/item/supporter roles. Scryfall supplies complete Magic scans and metadata; publisher primary sources support functional framing claims. Lorcana and Pokémon images come from official publisher galleries. The sample is limited to English-language versions of three prominent games and includes disproportionate promotional/full-art Pokémon and Lorcana treatments. It does not cover the full TCG field, every period, or physical surface behavior. Selected identities differ; alternate foil/plain versions, recolors and repeated printings were not counted separately.

Magic scans were inspected at 672×936. Lorcana's official 600×837 renditions include AVIF media, decoded transiently in Chromium; failed unsupported-format emits and cropped interim renders are not inspections. The same complete cards were subsequently inspected with all edges visible. Pokémon official 2x images are 660×920. Initial generic-User-Agent Scryfall requests failed and succeeded with the required identifying client header. Lorcana image identifiers required the observed official `/card` viewer suffix. None of these failed access attempts adds to the artifact count.

## Analysis

### Claim-to-artifact map

- Compact title/art/type/rules/credit hierarchy: MTG-LEA-46, MTG-LEA-232 and MTG-BLB-82.
- Readability-led pale title/stat compartments: MTG-BLB-122 and MTG-BLB-123, contrasted with low-contrast MTG-LEA-24.
- Distinct class/type geometry: MTG-BLB-124 split levels, LOR-649 landscape location, PK-OP_Prize_SE9_EN_62 item and PK-OP_Prize_SE9_EN_54 supporter.
- Symbolic resource/stat positions: LOR-661, LOR-170, PK-OP_Prize_SE9_EN_25 and PK-OP_Prize_SE9_EN_26.
- Art-to-rules tension: LOR-1198, LOR-2459 and PK-OP_Prize_SE9_EN_28.
- Ordinary non-full-art counterexample: PK-OP_Prize_SE9_EN_36.
- Still images establish no measured timing/easing or actual holographic movement.

### Functional and cultural context

[Mark Rosewater's primary account, Frames of Reference](https://magic.wizards.com/en/news/making-magic/frames-reference-2003-01-27), explains the 2003 frame revision in terms of readable titles, emphasized statistics and space for rules/art. It identifies Goudy Medieval for the original Magic title treatment, not for every TCG. His contrast discussion is a design explanation, not a blanket accessibility certification.

[Pokémon's official database guide](https://support.pokemon.com/hc/en-us/articles/360001025274-How-do-I-use-the-Trading-Card-Game-database) describes searchable costs, types, rarity and illustrator fields. [The official parent guide](https://parents.pokemon.com/en-us/trading-card-game/) distinguishes Pokémon, Trainer and Energy roles. [Lorcana's official gallery](https://cards.disneylorcana.com/en-US/) identifies the six ink colors and card roles; direct card faces show their actual placement. These support role-dependent hierarchy rather than a single mandatory fantasy frame.

### Application translation

Build a repeatable original card object with readable name, cost, custom object art, class, rules and set metadata. Let art and material signal worldbuilding while information remains retrievable. A deck/loadout interaction can expose costs, uniqueness and capacity; do not imply that an ornamental mock card is a whole working game. Compare finishes through an explicit fixed-state control instead of claiming physical foil measurements or automatic sparkle. Proposed colors, type stacks and breakpoints require implementation testing rather than source authority.

## Connections

`board-game-box-art` packages a whole game; this entry repeats compact playable/collectible information objects. `fairground-carnival-poster-art` shares theatrical promotion but organizes a local event rather than a mechanically comparable deck. `maximalism` can share density without the card grammar. A rectangle plus illustration, generic fantasy ornament, or a foil gradient alone is insufficient.

## Research Updates

### 2026-11-12 — Direct-media expansion and corrections

Current metadata reflects 32 inspected unique cards. This supersedes earlier placeholder claims and unsupported frequency bands. Landscape location, vertical split rules, non-creature roles and ordinary cards correct a universal portrait fantasy/foil template. Movement and physical reflectance remain unknown. Earlier material is preserved below as dated history.

### Historical profile — 2026-07-08


# Trading Card Game Design

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant (<30%) |
|---|---|---|---|
| Palette | System-coded faction/element/rarity colors, metallic foil, gem accents, dark/light rules zones, and promo variants. | Neighbor palettes only when the object model remains intact | Accessibility-first simplifications with solid contrast fields |
| Type | Strict hierarchy for name, cost, type line, rules text, stats, rarity, collector number, icon labels, and artist credit. | Support labels and metadata tuned to the domain | Decorative display accents used sparingly |
| Texture | Laminated print object, foil shimmer, beveled frames, holographic stamps, art windows, etched overlays, and premium edge effects. | Interface chrome that preserves source material logic | Flatter reduced-texture variants for legibility |
| Shape | Vertical rounded rectangle, nested boxes, title/cost band, art window, type line, rules box, stat medallions, crests, and pips. | Repeated UI modules echoing the source object model | Softened modern component variants |
| Motion | Stable frame with implied action inside illustration; digital foil/glow may move while object grammar stays legible. | State transitions linked to the core workflow | Static print-first or reduced-motion fallbacks |
| Spatial | Tightly zoned information architecture: top identity, art, mechanics, stats/footer, and controlled art-to-rules tension. | Secondary panes/lists that preserve scan order | More spacious marketing adaptations |
| Cultural markers | Faction colors, rarity hierarchy, artist credit, expansion logos, collectible numbering, deck legibility, premium print, and showcase frames. | Domain vocabulary and object-specific affordances | Broader adjacent-pop-culture references |

## Image Descriptions

1. [https://scryfall.com/docs/api/frames] — Source evidence for Trading Card Game Design: used to ground history, visual vocabulary, cultural framing, and boundary cautions.
2. [https://magic.wizards.com/en/news/making-magic/frames-reference-2003-01-27] — Source evidence for Trading Card Game Design: used to ground history, visual vocabulary, cultural framing, and boundary cautions.
3. [https://www.coolstuffinc.com/a/jayannelli-07072025-magics-frame-making-the-cut] — Source evidence for Trading Card Game Design: used to ground history, visual vocabulary, cultural framing, and boundary cautions.
4. [https://articles.starcitygames.com/magic-the-gathering/reframing-how-to-think-about-magic-card-frames] — Source evidence for Trading Card Game Design: used to ground history, visual vocabulary, cultural framing, and boundary cautions.
5. [https://www.pokemon.com/us/pokemon-tcg/pokemon-cards] — Source evidence for Trading Card Game Design: used to ground history, visual vocabulary, cultural framing, and boundary cautions.

## Analysis

Trading Card Game Design is application-ready only when its signal is distributed across all seven dimensions rather than resting on palette alone. The load-bearing pattern is: rigid information zoning + faction/rarity signaling + collectible object polish + frame-as-worldbuilding. Frontend translation should begin with that pattern, then apply color, texture, shape, and motion as evidence of it.

Use the source-backed boundary notes; do not reduce the aesthetic to palette alone or flatten adjacent traditions into a generic moodboard.

Source-grounded implementation brief:

### 19) `trading-card-game-design`
- `knowledge/aesthetics/trading-card-game-design.md`
  - Focus on repeatable object grammar: frame systems, faction/rarity encoding, readability, collectible prestige, and frame-as-worldbuilding. Source: `print-game-noir.md` / `trading-card-game-design`.
- `skills/aesthetic-literacy/aesthetics/trading-card-game-design.md`
  - Core dimensions: system-coded palette, rigid typographic hierarchy, laminated/foil/beveled texture, nested-box card shapes, stable frame with art-driven implied motion, tightly zoned spatial layout.
  - Anti-pattern: cloning Magic or Pokémon trade dress too directly.
- Boundary guardrail
  - Separate from `board-game-box-art`, `fantasy-illustration`, and operational HMI. Source: `print-game-noir.md` / `trading-card-game-design`.

## Connections

Related aesthetics from the dictionary and candidate set:
- Distinct from `board-game-box-art` and pure illustration: it is repeatable frame/UI object grammar with rules zones, faction/rarity coding, and collectible tactility.

## Research Updates

Initial profile created on 2026-07-08 from the 20-aesthetic expansion synthesis brief and parent research packets. Evidence level is marked limited because this implementation pass preserved source links and source-backed synthesis but did not download a 10+ image corpus for each entry.

### Parent research excerpt

## 4. `trading-card-game-design` — Trading Card Game Design

Evidence count: 5 sources.

### Source bibliography / URLs
1. Scryfall frame documentation for Magic frame generations/effects: https://scryfall.com/docs/api/frames
2. Magic official rationale for 2003 frame redesign: https://magic.wizards.com/en/news/making-magic/frames-reference-2003-01-27
3. CoolStuffInc analysis of Magic frame organization vs rival TCGs: https://www.coolstuffinc.com/a/jayannelli-07072025-magics-frame-making-the-cut
4. Star City Games piece on showcase frames and frame-as-worldbuilding: https://articles.starcitygames.com/magic-the-gathering/reframing-how-to-think-about-magic-card-frames
5. Pokémon official card database as primary corpus of types, rarities, expansions, and illustrator-indexable card objects: https://www.pokemon.com/us/pokemon-tcg/pokemon-cards

### Visual evidence summary
- TCG design is fundamentally a frame system, not just isolated illustrations. Scryfall’s frame taxonomy shows Magic as a long-lived evolving UI object with multiple frame eras and frame effects. Source: Scryfall.
- Wizards’ 2003 frame explanation makes function primary: readability, title legibility, and long-term system usability justified frame redesign. Source: Wizards official.
- CoolStuffInc stresses the stable ratio and hierarchy of art, name, cost, type line, text box, and power/toughness, showing how little the core Magic object has changed structurally even across decades. Source: CoolStuffInc.
- Star City Games shows how showcase frames alter the perceived world and can make the card feel native to a plane/theme; frame becomes part of narrative immersion, not mere border. Source: Star City Games.
- Pokémon’s official database demonstrates the breadth of modern TCG object taxonomies: energy types, card types, rarities, evolutions, expansions, special illustration rarities, and illustrator filtering. Source: Pokémon database.

### Seven-dimension synthesis
- Palette
  - Canonical: color encodes rules identity; frame/background palette usually maps to faction, element, rarity, or set treatment.
  - Common: metallic foils, rarity glows, gemlike accents, dark text-on-light zones where readability demands it.
  - Variant: showcase/event/promo treatments can temporarily subordinate system color logic to set flavor.
- Type
  - Canonical: highly disciplined typographic hierarchy for name, cost, subtype, rules text, stats, rarity, and collector metadata.
  - Common: display styling on names with utilitarian body text below; icon-text cohabitation.
  - Variant: collectible premium treatments that compress or stylize labels once player literacy is assumed.
- Texture
  - Canonical: laminated print object, foil shimmer, beveled frame simulation, holographic stamps, clean image windows.
  - Common: etched, borderless, extended-art, showcase overlays. Source: Scryfall.
  - Variant: deliberately retro frames or distressed novelty treatments.
- Shape
  - Canonical: vertically oriented rounded-rectangle card with nested boxes and strict zones.
  - Common: crest/crown frame ornaments, mana/energy pips, stat medallions, textbox separators.
  - Variant: borderless art spill, asymmetrical transform markers, premium subframes.
- Motion
  - Canonical: implied action lives inside the illustration, while the frame/UI remains stable and legible.
  - Common: explosive or dynamic art counterbalanced by immobile rules scaffolding.
  - Variant: digital companion products may animate foil/glow, but physical-card identity is still frozen.
- Spatial
  - Canonical: tightly zoned information architecture: title/cost at top, art window, type line, rules text, stats/footer.
  - Common: 40/60-ish art-to-mechanics tension in Magic-like systems; Pokémon shows similarly strict object zoning despite different rules lexicon. Source: CoolStuffInc; Pokémon database.
  - Variant: showcase or borderless products temporarily widen the art window.
- Cultural markers
  - Canonical: faction/element colors, rarity hierarchies, artist credit, expansion logos, collectible numbering, deck-construction legibility, premium print treatments. Source: Scryfall; Pokémon database; Wizards official.
  - Common: lore/world frame treatments, crossover promos, variant-art chase logic.
  - Variant: retro throwback frames and special collector-only formats.

### Related-aesthetic boundaries
- Vs. `board-game-box-art`: TCG design solves repeated object legibility and collecting prestige; board-game box art solves shelf promise and product branding.
- Vs. `high-performance-hmi`: both are information-dense and zoned, but TCGs must remain tactile, fantastical, and collectible rather than purely operational.
- Vs. `corporate-memphis` / flat-design: TCG frames rarely go fully flat because collectible tactility, faction coding, and premium treatment matter.
- Vs. pure `fantasy illustration`: TCG identity depends on frame grammar just as much as artwork.

### Cultural-sensitivity / misuse cautions
- Avoid clo
