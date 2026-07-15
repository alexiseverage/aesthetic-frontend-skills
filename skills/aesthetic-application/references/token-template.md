# Token Template

Use this installed-user template when producing a system-agnostic token specification. Fill every required row with concrete values. If the project asks for CSS custom properties, DTCG JSON, Tailwind config, Sass, Swift, or Android resources, translate this table into that target format after the table is complete.

## Color tokens

| Token | Value | Role | Notes |
| --- | --- | --- | --- |
| `color.background` | `#` | Page/app background |  |
| `color.surface` | `#` | Cards, panels, elevated surfaces |  |
| `color.text` | `#` | Primary text |  |
| `color.text-muted` | `#` | Secondary text |  |
| `color.primary` | `#` | Main action / brand signal |  |
| `color.secondary` | `#` | Secondary UI signal |  |
| `color.accent` | `#` | Aesthetic accent / highlight |  |

## Typography tokens

| Token | Value | Notes |
| --- | --- | --- |
| `font.display` | family or category |  |
| `font.body` | family or category |  |
| `font.mono` | family or category | optional |
| `font.weight-regular` | numeric weight |  |
| `font.weight-bold` | numeric weight |  |
| `type.heading-size` | px/rem |  |
| `type.body-size` | px/rem |  |
| `type.tracking` | em/px |  |

## Shape, motion, spacing

| Token | Value | Notes |
| --- | --- | --- |
| `radius.small` | px |  |
| `radius.medium` | px |  |
| `radius.large` | px |  |
| `motion.duration-fast` | ms |  |
| `motion.duration-medium` | ms |  |
| `motion.easing-primary` | named or cubic-bezier |  |
| `space.1` | px/rem |  |
| `space.2` | px/rem |  |
| `space.3` | px/rem |  |
| `space.4` | px/rem |  |
| `space.5` | px/rem |  |
| `space.6` | px/rem |  |

## Optional layout tokens

| Token | Value | Notes |
| --- | --- | --- |
| `layout.max-width` | px/rem |  |
| `layout.grid-gap` | px/rem |  |
| `layout.panel-depth` | shadow/elevation value |  |
| `layout.density` | sparse / standard / dense |  |
