---
slug: cozy-life-sim-interfaces
label: Cozy Life-Sim Interfaces
family: digital-internet-native
era: 2000s–present life-simulation menus and contemporary farm/craft variants
aliases: ["cozy life simulation UI", "cozy inventory interfaces"]
status: canonical
evidence_level: standard
related: ["cottagecore", "skeuomorphism", "cute-arcade-puzzle-boards", "handheld-creature-encyclopedias"]
subsets: []
---

# Cozy Life-Sim Interfaces

## Scope

A descriptive interface language from life-simulation, town, farming and adjacent craft-management games: recognizable possessions and materials, pockets or inventory wells, friendly category tabs, recipe/letter/book surfaces, and dialogue that treats the player as a neighbor. The organizing chrome, selection and feedback must carry the character of the world. A countryside screenshot inside a standard card is insufficient.

The [research profile](../../../knowledge/aesthetics/cozy-life-sim-interfaces.md) documents 30 deduplicated works: 28 complete published game-interface images and two official Nintendo manuals with inspected screen diagrams. Different screens from one authored game system count once. Farm/RPG and management examples are identified as adjacent variants, not proof that every game or scene in those genres is cozy. The modern term is not retroactively assigned as a historical movement name.

## 7-Dimension Profile

**Palette**: Warm cream, honey, leaf green, teal, soft peach and brown recur around illustrated objects. Ooblets supplies strong violet/coral, Fields of Mistria deep blue, Fae Farm dark brown/gold and Spiritfarer teal/gold counterexamples. Distinguish a calm reading surface from a saturated selection/action accent. Cozy does not mean universally pastel or low contrast; missing materials and selected items need text and shape as well as color.

**Type**: Friendly rounded sans lettering, irregular pixel letters, handwritten-looking annotations, condensed headings and occasional bookish serif titles coexist. Most systems separate item names, quantities, descriptions and controller prompts. Animal Crossing's broad rounded text is an anchor rather than a requirement to copy its proprietary face. Use a readable rounded/system sans for working content; constrain display irregularity to titles or short labels. Exact screenshot fonts remain unidentified unless independently documented.

**Texture**: Cream paper, wood trim, thick page edges, subtle patterns, dimensional item illustrations and soft undershadows turn lists into belongings. Pixel-art variants use stepped bevels and clear outlines instead of blurred realism. Fae Farm's dark carved frames and Portia's diagram book are different material branches. Texture belongs around the text plane, never across small letters or quantities.

**Shape**: Round item pockets, chunky pill controls, scalloped or asymmetric speech panels, projecting book tabs and name plaques are common. Regular slot matrices remain orderly beneath that softness. Squared pixel panels and rectangular notebook pages are supported variants; making every surface a blob destroys the hierarchy. Item silhouette, count badge, selected rim and category icon should remain distinct.

**Motion**: This corpus establishes still layouts, not measured animation curves. Nintendo manuals document selection, submenus and drag actions; screenshots do not establish easing, response speed or reveal cadence. Proposed web treatment: immediate crafting/count/selection updates and intentional stillness while reading. A small optional press may reinforce a raised button, but no idle wobble, forced typewriter delay, time gate or celebratory motion is necessary. Reduced motion must retain all state and feedback.

**Spatial**: Common structures are inventory/list left with item details right, an open book with category tabs, or a low dialogue surface with an overlapping portrait/name plaque. Toolbars, currency and time badges form a utility periphery. World imagery may stay visible, blur or dim; the foreground plane remains readable. Narrow web layouts should stack the same task hierarchy and keep a textual selected-item heading rather than shrink a game screenshot or require precision dragging.

**Cultural markers**: Neighborly dialogue, gathering, crafting, tending, trading, letters, small collections and domestic personalization. Animal Crossing is a major anchor alongside independently authored farm and town systems. Adjacent Chinese cultivation, space-farm and folklore examples prevent the vocabulary from being equated with one rustic Western fantasy. A friendly interface does not make monetization, grind, labor or accessibility constraints disappear.

## Non-Negotiables

**Non-negotiables**: A useful belongings/materials/neighborly task metaphor; tactile or illustrated interface chrome that belongs to that world; unmistakable selection, quantities and action feedback; a friendly readable hierarchy. The controls and working surface must embody the aesthetic, not merely contain appropriate images.

## Connotation

**Mode:** contemporary playful simulation quotation.

Conveys care, small-scale agency, collecting and making a place one's own. It can be colorful, intricate or gently fantastical. Avoid claiming a universally relaxing experience: players differ, and several sampled games include combat, timers, loss or demanding management. Apply the grammar to a real web task without reproducing game friction or suggesting an official Nintendo or other studio product.

## Related / Subsets

- **Cottagecore** centers pastoral craft and slow-living imagery. Life-sim interfaces center operational pockets, recipes, quantities and selection; they may use urban, space or dark jewel-toned worlds.
- **Skeuomorphism** supplies books, drawers and material affordances more broadly. This entry adds friendly illustrated possessions and neighborly simulation context; photoreal leather is not required.
- **Cute Arcade Puzzle Boards** uses a discrete puzzle field, move logic and arcade signage. A life-sim inventory organizes belongings and making rather than treating every item as a game-board piece.
- **Handheld Creature Encyclopedias** centers indexed creature records, discovery and attribute comparison. A life-sim worktable centers owned materials, recipes and domestic tasks; a creature portrait alone does not establish either system.

Supported branches include soft pocket/dialogue systems, pixel farm menus, illustrated craft books and darker fantasy wood/teal variants. These are descriptive branches, not newly coined historical movements.

## Frontend / UI Guidance

Use the grammar for craft planners, inventory managers, recipe builders, local project notebooks, small community exchanges or collectible indices. Build functional recipe selection, required-versus-owned material rows, meaningful unavailable states, a finished-project shelf and useful save/undo actions. Keep counts mathematically coherent; repeated crafting consumes the actual available materials. An undo must restore the exact transaction, not reset unrelated work.

Native labeled radios can select recipes or categories; pills must retain visible focus and text. Pair illustrated objects with names and quantities, and expose selection through checked/pressed state. A material shortage should explain what is missing. Any optional dragging requires equivalent buttons. Avoid sound dependence, forced animations and hover-only descriptions. Forms need clear labels and associated errors; a local printable label or real text download is preferable to decorative export controls.

On desktop, place a pocket inventory beside a larger recipe page and keep the finished shelf below. On mobile, stack recipe selection, requirements and action without hiding current supplies. Keep controls at least44px, retain readable text and allow wrapping labels. Strong focus rims should be visually separate from selected rims. A dark host theme may preserve the authored cream paper surface if its surroundings and controls remain legible.

## CSS Translation

Proposed worktable tokens; these are authored web values, not recovered game source styles:

```css
.cozy-worktable {
  --paper: #fff4d7;
  --ink: #354a3b;
  --muted: #52644f;
  --leaf: #285d48;
  --mint: #c6dcc0;
  --honey: #ebbf67;
  --coral: #a34432;
  color: var(--ink);
  background: #dbe8c8;
  font: 600 16px/1.5 "Trebuchet MS", Arial, sans-serif;
}
.cozy-page { background: var(--paper); border: 3px solid #a78b55; border-radius: 30px 20px 28px 18px; box-shadow: 0 7px 0 #b9a16b; }
.cozy-pocket { border: 2px solid #8c9d76; border-radius: 40% 44% 36% 42%; background: var(--mint); }
.cozy-worktable button { min-height: 44px; border-radius: 999px; }
.cozy-worktable :focus-visible { outline: 3px solid #173c68; outline-offset: 4px; }
.cozy-worktable input, .cozy-worktable textarea { border: 2px solid var(--muted); border-radius: 12px; background: #fffaf0; }
.cozy-worktable *, .cozy-worktable *::before, .cozy-worktable *::after { animation: none; transition: none; }
```

Use4/8/12/16/24/32px spacing,14–16px labels,16px working prose and32–58px friendly display headings. Rounded controls may have a4px dark undershadow and a contrasting selected rim; do not use shadow alone to communicate focus or availability. Proposed layout breakpoint680px, not a measured game adaptation. Controls keep native semantics and stable geometry under reduced motion.

## Typography / Fonts

Trebuchet MS with Arial and sans-serif fallback provides a zero-download friendly working stack; system availability changes its exact appearance. Use bold rounded-looking headings and ordinary mixed-case labels. A brief italic neighbor note can be personal without turning the whole UI into script. For a pixel branch, choose a licensed readable pixel font and preserve whole-pixel rendering, but never simulate authenticity by making body text too small. Japanese and other scripts require appropriate readable fallbacks rather than stretching Latin novelty lettering.

## Cultural / Ethical Notes

Credit the actual game, studio and UI artist where known. Reference screenshots and manuals are research sources, not reusable component assets. Create original objects, names, iconography and surface treatments; avoid studio logos, character likenesses, proprietary fonts or a confusingly faithful screen replica. A generic cozy label must not flatten distinct Japanese, Chinese, indie and other game traditions. Avoid coercive scarcity, repetitive clicking or monetization disguised as comforting care.

## Anti-Patterns

- A generic grid of cards with farm screenshots and unchanged controls.
- Declaring cream, rural scenery, blobs or a specific Nintendo typeface universal.
- Unlabeled item icons, color-only shortages, tiny counts or hover-only tooltips.
- Fake crafting that never consumes stock, decorative save/export controls or an undo that erases unrelated projects.
- Idle wobble, forced letter-by-letter prose, time gates, mandatory drag actions or inaccessible low-contrast material effects.
- Presenting proposed responsive/timing values as measurements of the source games.
