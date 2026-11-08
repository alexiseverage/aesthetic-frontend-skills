---
slug: shokuhin-sanpuru-display
label: Shokuhin Sanpuru Display
family: vernacular-commercial
era: Early-20th-century Japanese food replicas through contemporary practice
aliases: ["Japanese food-replica display", "food sample display", "shokuhin sampuru display"]
status: canonical
evidence_level: standard
related: ["skeuomorphism", "konbini-utility"]
subsets: []
---

# Shokuhin Sanpuru Display

Food represented as durable, carefully finished objects: texture, serving vessels, frozen gestures and practical display labels make dishes legible before an order is placed.

## Scope

This entry concerns the visual and commercial system around Japanese food replicas, including restaurant cabinets, maker displays, miniature merchandise and sculptural variants. It does not classify ordinary food photography or every Japanese restaurant interior as the same aesthetic.

The key relationship is between a specific modeled dish, its material surfaces, its serving arrangement and the display that makes it understandable. Food should shape the interface's object language and selection behavior, rather than serve as a themed stock image inside generic cards.

## 7-Dimension Profile

**Palette**: Ingredient-derived red, yellow, green, orange, brown and cream sit against white ceramics, dark trays, wood or neutral shelves. Transparent colored drinks and bright confectionery expand the palette. No single red/white brand palette defines the practice.

**Type**: Plain price slips, compact dish labels, handwritten notes and upright retail tags support recognition. Display type varies by restaurant and maker. Use legible dish names and tabular prices; decorative pseudo-Japanese lettering has no evidential basis.

**Texture**: Deliberately different surface responses distinguish crumb, grain, noodles, leaves, clear liquid, ice, sauce and ceramic. Many sauces and cut surfaces are glossy; not everything is wet plastic. Edges, translucency and small-scale relief matter as much as color.

**Shape**: Specific food forms retain recognizable proportions and serving silhouettes. Bowls, oval plates, trays, skewers, glasses and garnishes establish scale. Suspended noodles, falling sauce and pouring food freeze a gesture into a rigid sculpture; these are variants rather than mandatory features.

**Motion**: The replicas and audited displays are still. Apparent pouring or lifting is physically suspended. A web translation can use immediate selection and order updates; animation is not needed to establish the material system.

**Spatial**: A useful display offers several distinct dishes at once, often on shelves with labels immediately below. Plates and stands isolate silhouettes; denser cabinets still preserve dish identity. Miniature merchandise changes scale while retaining recognizable surface detail.

**Cultural markers**: Japanese restaurant display, department-store dining, yōshoku menus, specialist craft and Gujō Hachiman workshop culture provide context. Makers also extend the craft into souvenirs, educational diagrams and playful sculpture. Neither sushi nor a generic “kawaii” face is required.

## Non-Negotiables

**Non-negotiables**: recognizable modeled food; differentiated material texture; purposeful serving/display geometry; clear dish identity or selection information.

## Connotation

**Mode:** contemporary craft interpretation.

The combination should feel appetizing, precise and slightly surprising. Its commercial roots concern showing the customer what a dish contains and how it is served. Ganso Sample's own history cautions that exact invention stories are uncertain; Iwasaki's 1932 business formation should not be presented as proof of a single inventor.

## Related / Subsets

- `skeuomorphism` shares material imitation and object affordances; this entry specifically uses food-replica craft and menu-display logic.
- `konbini-utility` shares clear food identification and retail information, but its packaged labels and convenience-store systems differ from modeled dishes and display vessels.
- Restaurant cabinets, maker demonstration pieces, miniature goods and impossible-serving sculptures are related variants.

## Frontend / UI Guidance

Build a menu selector as a shelf of original modeled food objects. Make a plate, tray or bowl the actual selection surface, with a price slip directly beneath it. A selected dish can move into a clear order tray or receive a contrasting label and checkmark. Keep dish name, quantity, total and removal controls in semantic HTML.

Use a modest number of detailed dishes, preserving room between silhouettes. On mobile, stack shelf rows or show two generously sized objects per row; keep all labels and totals visible without horizontal dragging. Ingredient details and allergen information must remain readable text.

## CSS Translation

Proposed application values: cabinet charcoal `#272b29`, warm shelf `#976541`, ceramic cream `#f4eee0`, label paper `#fff9e9`, ink `#25271e`, tomato `#ad392a`, garnish `#416d40`. These are design choices, not measured historic standards.

Use original SVG/3D/raster material studies with distinct rough, glossy and translucent areas. Give vessels a visible rim and stable contact shadow. A shelf lip and narrow paper ticket can organize the composition; avoid one universal shadow and border radius. Keep gradients and texture away from label text. Add a non-color selected indicator and robust focus ring; reduced motion keeps every order operation intact.

## Typography / Fonts

Use a clear system sans-serif or modest serif for dish names and compact tabular numerals for prices. A handwritten accent may fit a maker's price note, but should not carry ingredients or controls. Use proper language-specific fonts when actual Japanese copy has been reviewed; English-only copy can preserve the display structure without borrowed script.

## Cultural / Ethical Notes

Credit food-replica craft as a living commercial practice. Do not imply that generated or procedural assets are work by an actual Japanese maker. Avoid misleading claims about actual portion size, ingredients or allergens. Reference photographs are analytical evidence, not assets licensed for an unrelated menu.

## Anti-Patterns

- Ordinary food photos inside an otherwise generic product grid.
- Flat emoji food with no material differentiation or vessel geometry.
- Everything rendered with the same glossy coating.
- Dense shelf decoration that separates labels from dishes or obscures controls.
- Treating cultural identity as a bundle of sushi, kanji and mascot faces.

Research and attributed visual examples: [Shokuhin Sanpuru Display](../../../knowledge/aesthetics/shokuhin-sanpuru-display.md).
