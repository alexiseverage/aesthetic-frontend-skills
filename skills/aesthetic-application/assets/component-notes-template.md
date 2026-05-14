# Component Notes Template

Brief, implementable notes for key UI components. Populate only the components relevant to the current design system scope.

---

### Interactive controls

| Component | Aesthetic application |
|---|---|
| **Buttons** | [border-radius, fill vs outline vs ghost treatment, font-weight, hover / active state (color shift / scale / shadow change / inset), active press feedback] |
| **Links** | [underline convention (always/hover-only/none), color vs text-primary, hover and visited treatment, external link indicator] |
| **Inputs** | [border style and weight, border-radius, focus indicator style (outline/glow/color-shift/underline-only), placeholder opacity and style, error state border treatment] |
| **Checkboxes / radio buttons** | [custom vs native, indicator shape (square vs circle), check mark style (bold/hairline/custom path), border-only vs fill-on-checked, label spacing and weight, disabled state surface] |
| **Select / dropdown** | [trigger border and radius, chevron icon style and weight, dropdown panel shadow character, option row hover state, grouped options separator style, native vs custom component] |
| **Toggles / switches** | [track shape (pill vs rectangular), thumb shape and inset gap, on-state track fill color role (primary/accent), transition character (snap/ease/spring), label placement] |
| **Sliders / range** | [track height and border-radius, thumb shape (circle/rounded rect/custom), active fill color vs empty track color, value label display (tooltip/persistent/none), tick mark presence] |

---

### Navigation & wayfinding

| Component | Aesthetic application |
|---|---|
| **Navigation** | [bar vs sidebar vs minimal/hidden, active indicator (underline/pill/fill/dot), link case and weight, mobile collapse treatment] |
| **Tabs** | [active indicator (underline/filled-tab/pill/bottom-border), inactive opacity and weight, border under full tab row vs none, panel transition (fade/slide/none), overflow handling (scroll/dropdown)] |
| **Breadcrumbs** | [separator character (/ vs › vs • vs —), active vs inactive link treatment, current page bold or plain, home icon vs text] |
| **Pagination** | [item shape (square/circle/pill), active state (fill/outline/underline/weight), prev/next as arrow icon or text, spacing density, ellipsis treatment] |
| **Dropdown menus** | [shadow character (hard/soft/glow/none), border presence and weight, item padding density, hover vs focus state contrast, group separator style (rule/label/space)] |
| **Sidebar / drawer** | [surface color relative to background (same/elevated/sunken/contrasting), edge shadow or border, item hover shape (full-width/pill/underline), nested group indentation and toggle, active item treatment] |
| **Footer** | [column vs single-row layout, surface color relative to background, heading case and weight, link weight and underline convention, divider from main content presence] |

---

### Content & data

| Component | Aesthetic application |
|---|---|
| **Headings** | [case convention (title/upper/sentence), decorative treatment (rule, ornament, border, none), weight contrast with body, tracking at display sizes] |
| **Badges / tags** | [border-radius (pill/square/sharp), fill vs outline vs ghost, font-size and weight, border presence, color role (semantic vs aesthetic)] |
| **Lists** | [marker style (disc/dash/custom SVG/none), marker color (accent/muted/text-primary), item vertical spacing, nested list indent and marker change, ordered numeral style (default/bold/decorated)] |
| **Tables** | [header row treatment (background fill/bottom-border/weight-only), row divider weight and color, zebra striping vs none, cell padding density, border-collapse vs separated, row hover state] |
| **Code blocks** | [monospace font choice, surface color relative to background (dark/offset/same), border treatment (none/subtle/prominent), syntax highlight palette character (warm/cold/high-contrast/monochromatic), line number presence] |
| **Blockquotes** | [decorative treatment (left-bar/full-background/oversized-quote-mark/none), bar or mark color role, font style (italic/roman), attribution size and color] |
| **Avatars** | [shape (circle/rounded rect/square), ring border presence, ring color role and width, fallback initials style (background color role, font weight), stack overlap direction and gap] |
| **Images / media** | [corner radius (match component scale or 0), border or frame treatment (none/thin rule/thick/decorative), caption typography (size, style, alignment), aspect-ratio convention, object-fit treatment] |

---

### Layout & containers

| Component | Aesthetic application |
|---|---|
| **Cards** | [border presence and style, shadow character (hard/soft/none/glow), border-radius, surface color relative to background, hover lift behavior] |
| **Hero / header** | [background treatment (gradient/texture/image/flat/video), display typography scale and decoration, imagery framing and mask treatment, CTA placement character] |
| **Modals / overlays** | [backdrop treatment (blur/solid-tint/none), container border and shadow, border-radius, entry animation (scale/slide/fade), close affordance style] |
| **Accordions / disclosure** | [header border treatment (bottom-only/full-border/none), indicator icon (chevron/plus-minus/arrow), expand animation (height/fade/none), spacing between closed items, open item surface distinction] |
| **Dividers** | [style (solid/dashed/dotted/ornamental/implied-whitespace-only), weight, color relative to surface, decorative midpoint element (none/diamond/ornament/icon)] |

---

### Feedback & status

| Component | Aesthetic application |
|---|---|
| **Alerts / notifications** | [border treatment (left-accent/full-border/none), background tint, icon usage, typographic emphasis style, semantic color roles (error/warning/success/info)] |
| **Toasts / snackbars** | [position (bottom-center/top-right/bottom-right), entry/exit animation character (slide/fade/spring), shadow treatment, max width, action link style and weight] |
| **Loading / skeletons** | [approach (spinner/skeleton-shape/pulse/shimmer/dots), color relative to surface (subtle/contrasting), skeleton geometry (accurate component approximation vs simple blocks), animation character] |
| **Progress bars** | [track color, fill color role (accent/primary/success), height, border-radius (sharp/soft/pill), label position (inside/above/none), striped vs solid fill] |
| **Steppers** | [connector style (solid line/dotted/dashed/none), step indicator shape (circle/diamond/number/check mark), completed vs active vs future state differentiation, label placement (below/right/hidden)] |
| **Empty states** | [illustration style (line art/spot color/single icon/none), headline weight and tone, body text presence, CTA character (primary button/ghost/link/none), vertical centering vs top-aligned] |
| **Tooltips** | [shape (arrow-pointed/rounded/rectangular), background color (surface-inverted/accent/neutral-dark), font size relative to body, shadow character, arrow presence and style] |

---

### Iconography & decoration

| Component | Aesthetic application |
|---|---|
| **Icons** | [preferred style (line/filled/duo-tone/pixel/hand-drawn/none), stroke weight, size relative to adjacent text, color role (inherit/accent/muted)] |
| **Focus rings** | [outline color role (accent/primary/contrast-invert), outline style (solid/dashed/glow via box-shadow), outline-offset, width, native browser default vs fully custom] |
| **Scrollbar** | [width (thin 4–6px/standard/hidden-until-hover), thumb color and border-radius, track color (transparent/surface-tinted), CSS-only vs overlay approach] |
| **Selection highlight** | [`::selection` background color (accent-tinted/inverted/saturated), text color during selection (white/black/auto), custom or browser default] |
| **Backgrounds / textures** | [noise or grain presence (none/subtle/heavy), gradient directionality (linear/radial/conic/mesh), pattern type (none/dot-grid/stripe/halftone/custom SVG), surface layering approach (flat/z-depth planes)] |
