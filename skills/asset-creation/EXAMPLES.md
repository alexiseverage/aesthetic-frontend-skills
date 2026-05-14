# Examples — Asset Creation

## Example prompts

Tasks that should activate this skill:

1. "Generate a vaporwave background texture using my knowledge profile."
2. "Create a style reference for the Y2K aesthetic from the images I've collected."
3. "Make an SVG icon for a 'share' button in the neubrutalism aesthetic."
4. "Vectorize this PNG logo so I can use it as SVG."
5. "Generate a background — I don't have the API set up, just tell me what to do."

---

## Ideal response pattern — generate with style reference

**For prompt 1 (vaporwave background, style reference exists):**

```
Loading vaporwave knowledge profile...

Generating background texture:
Prompt: "abstract atmospheric scene, infinite grid receding to horizon, neon
cyan grid lines, deep purple-black void background, faint star field, vignette
edges, digital retro mood, 1980s computer aesthetic, no figures, no text"

[Image generation tool] generate called
→ Output saved to knowledge/aesthetics/vaporwave/generated/background-01.png

Asset generated successfully.
```

---

## Ideal response pattern — graceful degradation (no generation tools)

**For prompt 5 (no image generation tools configured):**

```
No image generation tools are configured in this environment.
Here’s the full spec for manual generation:

ASSET TYPE: Background texture
ASSET FORMAT: Raster (PNG or WebP)

PROMPT (ready to paste into any image generation tool):
"abstract background, soft gradient, blurred bokeh lights, warm terracotta
and cream color palette, organic noise texture, matte surface, soft diffuse
lighting, interior lifestyle mood, no figures, no text"

Save output to: knowledge/aesthetics/<your-slug>/generated/
```

---

## Ideal response pattern — SVG to React component

**For prompt 4 (SVG → React):**

```typescript
interface ShareIconProps {
  fill?: string;
  size?: number;
  motion?: boolean;
  className?: string;
}

export function ShareIcon({
  fill = "#1A1A1A",
  size = 24,
  motion = false,
  className,
}: ShareIconProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      className={className}
      aria-hidden="true"
    >
      <path d="..." fill={fill} />
    </svg>
  );
}
```

---

## Anti-examples

**Anti-example 1: Failing silently when no generation tools available**

> "I couldn't generate the image because no image generation tools are configured."

Why it fails: The skill must never fail silently. When no tools are available, the agent should provide the full prompt text and asset spec so the user can generate it manually. Unavailable tools trigger the manual-instructions branch, not an error.

**Anti-example 2: Using a raster generation mode for a UI icon**

> Generating a raster background image for a "play button icon for a music app".

Why it fails: Icons and UI elements should use a vector/SVG generation mode. Raster modes produce bitmap-style output inappropriate for scalable UI assets. Asset type should drive mode selection.

**Anti-example 3: Texture language in vector prompt**

> Prompt: "glossy metallic badge with raised edge emboss and polished silver surface"

Why it fails: "Glossy", "metallic", "emboss", and "polished silver surface" are material/texture language. In vector generation modes, these produce raster-style rendering artifacts. Vector prompts should use geometry and color language: "circular badge shape, flat silver fill #C0C0C0, bold black stroke 3pt, no gradients, no shadows".

**Anti-example 4: Hardcoding colors in React SVG component**

```typescript
// Wrong
<path d="..." fill="#C77DFF" />
```

Why it fails: Colors must be driven by props, not hardcoded. Components must accept `fill` and `accent` props with defaults drawn from the aesthetic profile. This enables theme switching and keeps the component reusable across aesthetic contexts.
