---
slug: de-stijl
label: De Stijl / Neo-Plasticism
family: historical-design-movements
era: 1917–1931
aliases: ["De Stijl", "Neo-Plasticism", "Mondrian style", "The Style"]
---

**Palette**: The grid in color — red (#e01f26), blue (#225095), yellow (#fac901), black (#1a1a1a), white (#ffffff), gray (#c0c0c0); no mixing, no tints, no pastels; each color occupies its own orthogonal plane

**Type**: Geometric sans-serif — simple, bold, horizontal; type set in strict horizontal blocks only, never angled or curved; the letterform is a rectangular element in the grid, not a decorative object

**Texture**: Flat, matte, absolute — the surface is always honest and unadorned; no gradient, no shadow, no material reference; the plane IS the texture

**Shape**: Rectangles only — strict horizontal and vertical lines; no curves, no circles, no triangles, no diagonals; the rectangle is the sole formal unit; Mondrian's 1920s grid paintings are the canonical reference

**Motion**: None — static equilibrium is the goal; the tension is between rectangles, not movement between them; the composition is a resolved moment, not a process

**Spatial**: Asymmetrical grid — each rectangle maintains its own plane; thick black lines separate blocks of color and white; white space is an active structural element, not background; overlapping planes never intersect diagonally

**Cultural markers**: Mondrian's mature grid paintings (1920–1931); Rietveld's Red-Blue Chair (1923) and Schröder House (1924); Van Doesburg's *De Stijl* journal; the 45° diagonal split (Van Doesburg's Elementarism, 1924) that fractured the movement

**Non-negotiables**: strict horizontal/vertical grid + primary palette (red/blue/yellow + black/white) + rectangles only — no curves, no diagonals

## Connotation

**Authentic** — De Stijl (1917–1931) was a utopian philosophical project: Mondrian, van Doesburg, and Rietveld believed pure geometric abstraction could reveal universal harmony and reorganize society. The grid was a spiritual instrument, not a layout tool. **Nostalgic quotation** — ubiquitous: the Mondrian dress (YSL, 1965), White Stripes album covers, every "Mondrian-inspired" branding exercise. These borrow the surface vocabulary without the philosophical weight. **Contemporary revival** — CSS Grid and modern web layout are De Stijl's structural principles realized as infrastructure; the grid-as-design-philosophy is now the grid-as-browser-engine. Direct visual quotation persists in high fashion, architecture, and editorial design. **Ironic pastiche** — the L'Oréal Mondrian haircolor ads and similar pop-culture appropriations treating the grid as graphic wallpaper; common enough to be its own minor mode.

## Scope

**Suitable for**: art museum/gallery websites, architecture portfolios, editorial layout, fashion brand sites, design-agency landing pages, modern furniture e-commerce — any project where "structured creativity" or "order-through-abstraction" is the brand message. CSS Grid is the native implementation; De Stijl layouts are trivially achievable in modern CSS. **NOT suitable for**: data-heavy dashboards (primary-color blocks compete with data visualization), accessibility-first interfaces (red/blue adjacency creates vibration for colorblind users), text-heavy documentation (the asymmetric grid fights linear reading flow), or any project requiring visual calm. The aesthetic demands attention — it actively resists being background. Avoid when the user needs to focus on content rather than form.

## Subsets / Related
- [[bauhaus]] — contemporary dialogue; Van Doesburg lectured at the Bauhaus; De Stijl's grid thinking influenced Bauhaus curriculum, but De Stijl is stricter in formal vocabulary (rectangles only, no circles/triangles)
- [[suprematism]] — precursor; Suprematism introduced floating abstract geometry on white ground; De Stijl codified it into a grid system with a more constrained shape vocabulary
- [[swiss-international]] — descendant; the Swiss grid system is De Stijl's mathematical-grid principle applied to typographic layout, stripped of the primary-color vocabulary

## CSS Translation
- **Palette**: `--ds-red: #e01f26; --ds-blue: #225095; --ds-yellow: #fac901; --ds-black: #1a1a1a; --ds-white: #ffffff; --ds-gray: #c0c0c0;`
- **Google Fonts**: system-ui sans-serif stack; DM Sans or Inter for a clean geometric face; no decorative or serif type
- **Texture**: Absolute flat — `box-shadow: none; background: solid;` — no gradients, no shadows, no transparency
- **Border-radius**: **0px everywhere** — this is the single most border-radius: 0 aesthetic in the dictionary; rectangles must be sharp
- **Layout**: CSS Grid is the native implementation — `grid-template-columns` and `grid-template-rows` with `grid-gap` as thick black borders; asymmetric placement within strict orthogonal tracks; `border` properties for the defining black lines between blocks; hero sections as Mondrian-style grid compositions
