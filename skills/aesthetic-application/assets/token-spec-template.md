# Token Specification Template

A flat, system-agnostic table of all token values. Translate into your project's token system (CSS custom properties, Tailwind config, DTCG JSON, Sass variables, Swift/Android tokens, etc.).

| Token | Category | Value | Notes |
|---|---|---|---|
| `background` | Color | `#XXXXXX` | Page / canvas background |
| `surface` | Color | `#XXXXXX` | Card, panel, elevated layer |
| `primary` | Color | `#XXXXXX` | Primary interactive / brand color |
| `secondary` | Color | `#XXXXXX` | Secondary brand or supporting color |
| `accent` | Color | `#XXXXXX` | Highlight, call-to-action |
| `text-primary` | Color | `#XXXXXX` | Body and heading text |
| `text-secondary` | Color | `#XXXXXX` | Muted / supporting text |
| `font-primary` | Typography | `[font name or type category]` | Primary typeface; include fallback stack |
| `font-secondary` | Typography | `[font name or null]` | Display or accent typeface if needed |
| `weight-display` | Typography | `700` | Display heading weight |
| `weight-body` | Typography | `400` | Body text weight |
| `tracking-display` | Typography | `0.05em` | Letter-spacing for display headings |
| `size-display` | Typography | `48px` | Largest display size |
| `size-heading` | Typography | `32px` | Section heading size |
| `size-body` | Typography | `16px` | Body text size |
| `line-height-body` | Typography | `1.5` | Body line-height multiplier |
| `radius-sm` | Shape | `Xpx` | Small corner radius (e.g. badges, inputs) |
| `radius-md` | Shape | `Xpx` | Medium corner radius (e.g. cards) |
| `radius-lg` | Shape | `Xpx` | Large corner radius (e.g. modals, panels) |
| `duration-fast` | Motion | `Xms` | Micro-interactions, hover transitions |
| `duration-base` | Motion | `Xms` | Standard transitions |
| `easing-standard` | Motion | `cubic-bezier(X, X, X, X)` | Default easing curve |
| `spacing-unit` | Spacing | `Xpx` | Base unit (grid baseline) |
| `spacing-xs` | Spacing | `Xpx` | Extra-small gap / padding |
| `spacing-sm` | Spacing | `Xpx` | Small gap / padding |
| `spacing-md` | Spacing | `Xpx` | Medium gap / padding |
| `spacing-lg` | Spacing | `Xpx` | Large gap / padding |
| `spacing-xl` | Spacing | `Xpx` | Extra-large section spacing |
| `layout-columns` | Layout | `grid-template-columns: value` | Primary column structure; populate from image-analysis if available |
| `layout-sidebar-width` | Layout | `Xpx` | Sidebar width if applicable; omit if no sidebar present |
| `layout-content-max` | Layout | `Xpx` | Max content container width |
| `layout-min-width` | Layout | `Xpx` | Minimum layout width before breakpoint |

_Layout tokens are populated only when the `image-analysis` skill has extracted layout values from UI screenshots. Omit this section if no layout data is available._

> **Output format note**: The token table above is the primary, format-agnostic output. If the developer explicitly requests DTCG JSON, CSS custom properties, or Tailwind config, translate the table into the requested format. A DTCG JSON example is in EXAMPLES.md.
