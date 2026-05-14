# Examples — Aesthetic Application

## Example prompts

Tasks that should activate this skill:

1. "Give my app a Y2K vibe — full design spec for a developer."
2. "Brutalist aesthetic, must meet WCAG AA."
3. "Art Deco but modern and minimal."
4. "I want a dark academia UI for my reading app. CSS variables please."
5. "Design tokens for a quiet luxury e-commerce site."

---

## Ideal response pattern — full spec (Y2K)

**For prompt 1:**

The agent:
1. Confirms: "Applying Y2K aesthetic in nostalgic quotation mode."
2. Notes constraints: "No WCAG constraint specified — will flag conflicts. No platform specified — assuming web. Dark mode not specified — will flag gap."

Then produces all 4 output sections:

**Token Specification (excerpt):**

| Token | Category | Value | Notes |
|---|---|---|---|
| `background` | Color | `#FFFFFF` | White chrome base |
| `surface` | Color | `#E8E8F0` | Metallic silver panel |
| `primary` | Color | `#C0C0C0` | Chrome / silver |
| `secondary` | Color | `#A0A0C0` | Iridescent blue-silver |
| `accent` | Color | `#00FFCC` | Acid green / cyber teal |
| `text-primary` | Color | `#1A1A2A` | Near-black on chrome |
| `text-secondary` | Color | `#606080` | Muted metallic grey |
| `font-primary` | Typography | `Arial Black, Impact, sans-serif` | Heavy grotesque; wide tracking |
| `font-secondary` | Typography | `VT323, Courier New, monospace` | Pixel / terminal accent face |
| `weight-display` | Typography | `900` | Maximum weight for display |
| `weight-body` | Typography | `400` | Regular body |
| `tracking-display` | Typography | `0.12em` | Wide tracking on display headings |
| `size-display` | Typography | `56px` | Hero display |
| `size-heading` | Typography | `32px` | Section heading |
| `size-body` | Typography | `15px` | Body text |
| `line-height-body` | Typography | `1.6` | Generous line-height |
| `radius-sm` | Shape | `2px` | Near-sharp (beveled feel) |
| `radius-md` | Shape | `8px` | Chamfered rectangle |
| `radius-lg` | Shape | `9999px` | Full pill shape |
| `duration-fast` | Motion | `120ms` | Hover flash |
| `duration-base` | Motion | `300ms` | Shine sweep / slide |
| `easing-standard` | Motion | `cubic-bezier(0.0, 0.0, 0.2, 1.0)` | Snappy decelerate |
| `spacing-unit` | Spacing | `8px` | Base grid unit |
| `spacing-xs` | Spacing | `4px` | Tight inner padding |
| `spacing-sm` | Spacing | `8px` | Component inner padding |
| `spacing-md` | Spacing | `16px` | Standard gap |
| `spacing-lg` | Spacing | `32px` | Section padding |
| `spacing-xl` | Spacing | `64px` | Page-level section spacing |

**Optional: DTCG JSON format** (produce this block only when the developer explicitly requests JSON):

```json
{
  "background": { "$value": "#FFFFFF", "$type": "color" },
  "surface": { "$value": "#E8E8F0", "$type": "color" },
  "primary": { "$value": "#C0C0C0", "$type": "color" },
  "accent": { "$value": "#00FFCC", "$type": "color" },
  "text-primary": { "$value": "#1A1A2A", "$type": "color" },
  "font-primary": { "$value": "Arial Black, Impact, sans-serif", "$type": "fontFamily" },
  "weight-display": { "$value": 900, "$type": "fontWeight" },
  "radius-lg": { "$value": "9999px", "$type": "dimension" },
  "duration-base": { "$value": "300ms", "$type": "duration" },
  "easing-standard": { "$value": "cubic-bezier(0.0, 0.0, 0.2, 1.0)", "$type": "cubicBezier" },
  "spacing-unit": { "$value": "8px", "$type": "dimension" }
}
```

**Cultural Markers:**

Include:
- Chrome/metallic gradients on interactive elements
- Pixel fonts or bold display type with wide tracking
- Holographic or iridescent surface treatment on hero elements
- Rounded pill shapes alongside sharp corners (contrast pairing)
- Star/burst decorative marks

Avoid:
- Flat minimalism (zero visual dimension — directly contradicts Y2K)
- Neutral greige / quiet luxury color stories
- Clean, contemporary sans-serif body type without stylistic treatment

**Component Notes excerpt:**

| Component | Aesthetic application |
|---|---|
| **Buttons** | Pill shape (9999px radius) or chamfered rectangle; metallic gradient fill (#C0C0C0 → #F5F5F5 → #808080); bold text; inset border-style hover |
| **Cards** | Raised with hard drop shadow (no blur, 3px offset); silver or translucent surface; pixel border |
| **Inputs** | Inset bevel effect; `1px solid #808080` outer, `1px solid #FFFFFF` inner; no border-radius |

**Flags:**

- ⚠️ WCAG: Silver (#C0C0C0) on white (#FFFFFF) fails AA (contrast ~1.4:1). Darken metallic text elements or use `#2A2A2A` for text over metallic backgrounds.
- ⚠️ Reduced-motion: Shine sweep animation on metallic surfaces is motion-dependent. Provide static metallic gradient fallback.
- ℹ️ Dark mode gap: Y2K is inherently light (chrome on white); dark mode equivalent not produced.

---

## Ideal response pattern — brutalist + WCAG AA

**For prompt 2:**

The agent does NOT say "Brutalism and WCAG AA are incompatible."

Instead:

1. Notes: "Raw brutalism (black text on white, or white text on black) is inherently high-contrast and trivially meets AA. The actual conflict zone is interactive elements and focus states."

2. Produces tokens with high-contrast black/white base palette — no WCAG flag for body text.

3. Flags specific conflicts:
   - "Yellow (#FFD600) on white fails AA (2.0:1) — used sparingly as accent only, never as text background"
   - "Focus rings: default browser blue may be insufficient on dark brutalist backgrounds — specify explicit `outline: 3px solid #FFD600` with sufficient contrast on the specific background it appears against"

4. Provides resolution that preserves aesthetic:
   - "Use black/white as the primary WCAG-compliant text layer; reserve yellow and red as decorative accents for non-text elements only."

---

## Ideal response pattern — aesthetic blending (Art Deco + minimal)

**For prompt 3:**

The agent:
1. Names both parents: "Art Deco (historical) + Contemporary Minimalism"
2. Identifies conflict dimension: "Ornament density — Art Deco is ornament-rich; minimalism eliminates ornament"
3. Resolves per-dimension:

| Dimension | Art Deco | Minimalism | Resolution |
|---|---|---|---|
| Palette | Rich gold, deep navy, black | Monochrome or near-neutral | Gold (#C9A84C) as single accent; navy (#1A2744) as primary; black/white base |
| Typography | Geometric display, high contrast, elaborate letterforms | Clean sans, restrained | Geometric Art Deco display type (Futura-adjacent) for headings only; minimal body |
| Texture | Fan rays, chevrons, stepped arches | None | Single decorative divider motif per section; no field textures |
| Shape | Stepped octagonal forms | Pure rectangles | Right angles maintained; geometric Art Deco proportions on containers |
| Ornament | Abundant | Zero | One typographic ornament per page maximum |

---

## Anti-examples

**Anti-example 1: Abstract mood descriptions instead of tokens**

> "The Y2K aesthetic is characterized by futuristic optimism and metallic surfaces that evoke the digital revolution of the late 1990s."

Why it fails: This is a prose description, not a token. The developer needs `#C0C0C0` not "metallic surfaces". Every output from this skill must be implementable.

**Anti-example 2: Saying brutalism and WCAG AA are incompatible**

> "Brutalism's raw, unstyled approach fundamentally conflicts with WCAG AA requirements."

Why it fails: Raw brutalism (black on white, white on black) trivially meets AA contrast. The skill must identify ACTUAL conflicts (specific color pairs, focus state issues) rather than making a blanket incompatibility claim. See the brutalist ideal response above.

**Anti-example 3: Unresolved blend**

> "Art Deco minimalism would combine the elegance of Art Deco with clean minimalist lines."

Why it fails: This is the vague starting point, not the resolution. The skill must name the conflict dimension, then produce explicit per-dimension decisions that choose one parent or synthesize. "Elegance of Art Deco with clean minimalist lines" is not a spec — it is a brief.

**Anti-example 4: Missing cultural markers**

Producing tokens and CSS variables without cultural markers.

Why it fails: Cultural markers are what make the spec feel like the aesthetic rather than just a color scheme. "Brutalist" tokens in neutral colors without cultural markers (raw HTML-like typography, unstyled states, deliberate friction) produce a generic spec that could be anything. The include/avoid lists are non-negotiable outputs.
