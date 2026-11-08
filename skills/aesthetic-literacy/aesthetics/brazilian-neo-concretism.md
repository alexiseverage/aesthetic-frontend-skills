---
slug: brazilian-neo-concretism
label: Brazilian Neo-Concretism
family: historical-design-movements
era: "1959–early 1960s, with dated participatory continuations"
aliases: ["Brazilian Neoconcretism", "Neoconcretismo"]
status: canonical
evidence_level: standard
related: [bauhaus, de-stijl, op-art]
subsets: []
---

# Brazilian Neo-Concretism

## Scope

The experiential abstraction developed by Brazilian artists and poets around the 1959 Neo-concrete exhibition and manifesto: relationships among material support, color, planes, gaps, space and the participant. Early-1960s reliefs, objects and books are central to this translation. The formal exhibition moment and later participatory continuations have distinct dates; neither all Brazilian modernism nor every later work by an associated artist belongs automatically.

A useful interface makes its actual structure respond to the reader's choices. Geometric decoration, primary colors or a photograph of a hinged sculpture alone cannot establish this aesthetic. Still painting, woodcuts and poetry also belong; mechanical movement is not compulsory.

## 7-Dimension Profile

**Palette**: White/black and saturated red, yellow or blue often articulate a plane or edge. Restrained pale reliefs, natural metal, oxidized steel, printed grain and later mixed materials are documented exceptions. Let color identify a functional plane and reveal a relation as it opens or changes position. Exact historical pigments are unmeasured; no universal primary-color triad.

**Type**: Much sculpture is unlettered. Contemporary exhibition print and concrete poetry use spare sans words, deliberate intervals, small lowercase labels, narrow columns and large empty regions. The supporting publication vocabulary is not a universal sculpture font. Use plainly readable sans labels and a few short spatial display words, preserving meaningful text order. Exact historic faces remain unidentified.

**Texture**: Painted wood, canvas/board, sheet metal, hinges, cardboard, strings and woodcut grain. Keep material relationships visible through thickness, seams and cast shadows where they explain structure. Avoid an indiscriminate chrome finish or grunge overlay. Photographic patina and archival paper aging are not required original properties.

**Shape**: Planes, squares, rectangles, triangles, arcs, cuts, folds, notches, voids, hinges and continuous strips. Organic refers to an experiential relationship rather than necessarily a rounded biomorphic outline. Empty space and the support itself participate in the composition; a seam can become an opening rather than a decorative border.

**Motion**: Actual filmed handling changes relationships between planes in Clark's objects. Other works invite changing viewpoint or spatial reading without autonomous motion. A contemporary interface can use deliberate user-triggered opening or reordering; all timing/easing is a proposal, not measured historical choreography. Reduced motion retains every change immediately. Avoid perpetual spin, hover-only parallax and forced optical stimulation.

**Spatial**: Active edges, off-center overlap, negative space, unbound pages and changing relations between supports. Large quiet fields can oppose narrow concentrated activity. Structure should respond to the user while labels, focus and semantic reading order stay comprehensible. On mobile, recompose panels into a readable sequence instead of shrinking a complex sculpture diagram into tiny controls.

**Cultural markers**: Rio's 1959 exhibition, Gullar's manifesto, artists' distinct routes through Concrete art, embodied perception and participatory experiments. Clark, Pape and Oiticica are central but do not erase de Castro, Amilcar, Weissmann and the poets. Do not replace this context with tropical foliage, carnival motifs or generalized Brazilian branding.

## Non-Negotiables

**Non-negotiables**:

- Meaningful interdependence among content, its supporting plane, gaps and the user's viewpoint or action.
- Deliberate geometric relationships with empty space doing visible structural work.
- Agency and perceptible state change, including a fully usable keyboard route when interaction is offered.
- Historically bounded attribution; proposed interface behavior remains a contemporary translation.

## Connotation

**Mode:** contemporary revival.

Open, exploratory and attentive to experience. An editable modular workspace can become a small active object: opening a working surface reveals content and moves its neighboring planes. It should still communicate plainly whether a change is saved, reversible or exported. Conceptual openness belongs in composition, not ambiguous software controls.

## Related / Subsets

Bauhaus and De Stijl share geometric/color concerns but differ in setting, programs and theories. Kinetic Art is adjacent in movement; Neo-concrete practice also includes still painting, print and poetry, so it is not a subset of motion effects. Concrete poetry is a documented relation. Later therapeutic, environmental or performance practices need their own dated scope rather than blanket inclusion here.

## Frontend / UI Guidance

Build information-bearing planes: an accordion whose opening alters the neighboring field, a dashboard with explicit panel reordering, a book-like editor with unbound sections, or a comparison surface whose gaps and edges change with selection. Give every plane a readable name and real content. Use flat opaque fields, narrow seams, restrained physical depth and a few decisive colored edges. Custom geometry must be part of control/layout behavior, not an unrelated image inside ordinary cards.

Preserve content when panels close or move. Provide visible earlier/later buttons alongside any drag affordance; update DOM order to match visual order and retain focus on the moved section. Native disclosure/buttons and labeled inputs should expose current state, bounds, validation and completion. Autosave claims require actual persistence; a visit-only editor should say so and provide a real export if keeping work matters.

Keep working text upright during decorative folds. A loader should represent real progress, a carousel should have explicit controls and no compulsory autoplay, and dialogs need a visible close action, Escape and focus return. Spatial novelty must not hide navigation or turn an essential action into an unexplained geometric puzzle.

## CSS Translation

Proposed modern tokens, not sampled historic pigments: field `#f3f2eb`, ink `#202824`, red `#b52f2c`, yellow `#e9bb38`, blue `#214ea4`, plane `#faf9f4`. Use 0 px corner radius, 1–2 px seams, 8/16/24/40 px spacing and a narrow 8–16 px active-color edge. Choose ink on yellow/pale, light text on red/blue, then test rendered states. Color alone cannot mark the selected panel.

Use CSS grid to make opening and order affect real layout. An original SVG can show cut/hinge relationships, but labels and actions belong in HTML. Short decorative plane transforms may use a proposed 220 ms ease-out on explicit user action; do not rotate text or animate layout continuously. Under `prefers-reduced-motion: reduce`, remove nonessential transforms/transitions and perform the same state update directly. Stable light material fields can remain opaque within either host theme.

## Typography / Fonts

Installed Arial or Helvetica Neue can supply clear sans utility and short spatial display words; fallback to system sans. These approximate categories rather than identify a historic typeface. Use roughly 14–16 px working labels, 16 px body copy with 1.5 line height, and a small number of 40–80 px display words where space permits. Avoid giant illegible letters, fragmented accessible names or artificial font authenticity. New fonts require verified license, fallback and loading budget.

## Cultural / Ethical Notes

Distinguish original works, later reconstructions, museum handling replicas and contemporary interpretations. Museum photographs do not authorize handling collection objects, copying artist work or claiming affiliation. Later Clark therapeutic practice is outside this design brief and provides no basis for health claims. The manifesto's theories should not be reduced to a universal formula or used to deny individual artists' differences. Preserve creator, concept and production dates when sources disagree.

## Anti-Patterns

- Generic rounded dashboard cards with a Neo-concrete artwork pasted inside.
- Treating every primary-color triangle, all Brazilian geometry, or all works by a signatory as Neo-concrete.
- Endless spinning, optical flicker, hover-only meaning, rotating functional text or drag-only order changes.
- Collapsing 1959 concepts, later fabrications and 1970s therapeutic practice into one date/style.
- Counting pages, configurations or film frames as independent works; inventing original timings, fonts or pigments.

Source basis: [1959 exhibition catalogue](https://portal.lygiaclark.org.br/acervo/10979/1-exposicao-neoconcreta), [MoMA on de Castro](https://www.moma.org/artists/8474-willys-de-castro), [MAM Rio relief/Nucleus context](https://mam.rio/obras-de-arte/relevos-espaciais-1959-1960-nucleos-1960-1966/), [Glenstone Book of Time](https://www.glenstone.org/exhibitions/lygia-pape), and the linked 30-artifact research profile, including actual filmed handling and retained source conflicts.
