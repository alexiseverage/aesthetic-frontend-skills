---
name: asset-creation
license: MIT
description: >
  Use this skill when you need to generate visual assets — backgrounds, textures, icons,
  decorative shapes, or SVG elements — using an image generation tool, grounded in a
  knowledge profile aesthetic. Also handles vectorizing raster images and converting SVG
  outputs to typed React components. Not for UI components with behavior or structural
  layouts — use aesthetic-application for those. Gracefully degrades to manual prompt
  specifications when no image generation tool is configured.
  Do not use for UI components with behavior, interaction, or layout structure.
compatibility: Requires an image generation tool to generate assets. Gracefully degrades to providing manual prompt specifications when no tool is configured.
allowed-tools: image-generation
metadata:
  version: "1.2.0"
  version_notes: "1.2.0 — extended graceful degradation paths and SVG-to-React conversion support"
  layer: applied
  status: stable
  tags: "asset-generation, svg, react-components, image-generation"
  activation_keywords: "generate an image, create a texture, make an SVG, vectorize, background image, generate an icon, create a background, SVG to React"
  known_limits: "Depends on external image generation tool availability; vector output quality varies by tool; does not produce UI component code"
  last_evaluated: ""
  eval_suite: ""
---

# Asset Creation

## Summary

Generates visual assets (backgrounds, textures, icons, UI elements) using available image generation tools, grounded in a knowledge profile aesthetic. Can generate new assets, vectorize raster images, and convert SVG outputs to React components.

## Knowledge Base Path

Before loading any profile or saving output, resolve the knowledge base root:

| Context | Resolved path |
|---|---|
| Project-level install | `knowledge/aesthetics/` at the **workspace root** |
| User/global install (`-g`) | `~/.agents/skills/knowledge/aesthetics/` |

Identify the workspace root by locating a parent directory containing `.git`, `package.json`, or `.agents/`.

> Throughout this skill, `knowledge/aesthetics/` refers to the resolved path above.

## Companion Skill

**Before doing any other work in this skill**, check whether a tool-specific companion skill is listed in your available skills (e.g. `recraft`). If one is present, load it now. That skill handles all image generation API and MCP calls — this skill provides the workflow, prompt structure, and output conventions. Once the companion skill is loaded, defer all generation calls to it.

If no companion skill is listed, check your active tool set directly for an image generation tool (e.g. a `generate_image` MCP tool). If none is found, follow the graceful degradation path in the companion skill or the `## API Reference` section below.

## When to Use This Skill

Use this decision table before generating anything. The wrong tool produces unusable output.

| What is being created | Approach | This skill? |
|---|---|---|
| Icon, badge, illustration, background, texture, decorative shape | image generation tool → raster or SVG | ✅ Yes — owns it entirely |
| Decorative SVG element needed as a composable React component | image generation → SVG → React (workflow 4) | ✅ Yes — SVG code becomes the component |
| UI component with dynamic content or behavior (card, modal, tooltip, panel) | Design tokens from `aesthetic-application` + CSS | ❌ No — tokens style it; `asset-creation` may contribute a decorative passenger inside it |
| Structural layout component (sidebar, grid container, nav shell) | Design tokens from `aesthetic-application` + CSS | ❌ No — pure token/CSS concern; this skill has nothing to contribute |

**The key test**: Can the thing be expressed as static geometry with no dynamic content or event handling? If yes, an image generation tool can generate it. If it renders variable text, responds to user interaction, or defines layout structure, it belongs to `aesthetic-application` tokens — not here.

**Decorative passengers**: A structural component (e.g. a fortune card) can *contain* an asset-creation output (e.g. a gem icon SVG component) as a decorative element. In that case, run `aesthetic-application` for the component shell and `asset-creation` for the embellishment separately.

## Prompt Guidelines

### Short vs. structured prompts

- **Short prompts** (3–8 words): Invoke the generation tool's interpretive mode. Good for mood/exploration. Unpredictable output.
- **Structured prompts** (15–50 words): Provide architectural control. Use for production assets.

### Vector/icon/UI element prompt structure

Build prompts in this priority order (earlier elements receive higher model weight):

1. **Graphic type**: What category of graphic (app icon, UI button, badge, logo mark, illustration)
2. **Shape logic**: Primary shapes and their relationships (circle containing arrow, overlapping rectangles)
3. **Color system**: Named palette colors or hex values; fill vs. stroke
4. **Line discipline**: Stroke weight description (thin 1pt, medium 2pt, bold 4pt), closed vs. open paths
5. **Layout**: Composition center / alignment / padding
6. **Constraints**: What NOT to include (no gradients, no shadows, no text, no photorealistic detail)

**Important for vector prompts**: Avoid texture and material language ("metallic", "glossy", "rough"). Use geometry and color language only.

### Raster/background/texture prompt structure

1. **Scene type**: Category (abstract background, product surface, atmospheric landscape, pattern tile)
2. **Environment**: Primary environmental elements
3. **Material**: Surface characteristics (matte, translucent, grain-heavy)
4. **Lighting**: Direction, quality, source (soft overhead, neon backlight, golden hour side light)
5. **Mood**: Emotional tone (melancholic, euphoric, uncanny, serene)

### Text in images

Enclose text in quotes within the prompt: `"HELLO WORLD"` → Most generation tools render the exact string. Useful for logo generation and typographic exploration.

## Workflows

### 1. Generate from aesthetic profile

```
1. Load knowledge/aesthetics/<slug>.md
2. Extract palette from ## Analysis (if present) or ## Dimension Synthesis
3. Build prompt using asset-type-appropriate structure above
4. Use the image generation tool available in your environment to generate the asset
5. Save output to knowledge/aesthetics/<slug>/generated/
6. Report: asset path, tool used, prompt used
```

### 2. Create a style reference

Use when: The profile has collected reference images and the generation tool supports style learning from reference images.

```
1. Select 1–4 representative images from knowledge/aesthetics/<slug>/images/
2. Use the image generation tool's style reference / style training feature
3. Save the resulting style ID or reference identifier for use in subsequent generation requests
```

### 3. Vectorize a raster image

```
1. Use the image generation tool's vectorization feature (if available)
2. Save SVG output to knowledge/aesthetics/<slug>/generated/<name>.svg
```

### 4. Convert SVG to React component

When converting an SVG output to a React component:

- TypeScript functional component
- Color fills as typed props with defaults drawn from the knowledge profile palette (source: use the `## Analysis` → Color section if already loaded; otherwise load `knowledge/aesthetics/<slug>.md` and read that section)
- Optional `motion?: boolean` prop to gate animation hooks
- No hardcoded colors in JSX — all colors via props or CSS custom properties
- Export as named export

Example prop interface:
```typescript
interface IconProps {
  fill?: string;       // defaults to aesthetic primary color
  accent?: string;     // defaults to aesthetic accent color
  size?: number;       // defaults to 24
  motion?: boolean;    // gates animation hooks
  className?: string;
}
```

## API Reference

This skill does not prescribe a specific API. Use whatever image generation tools are configured in your environment. See a tool-specific skill (e.g. `recraft`) for API details.

## Examples

Load [EXAMPLES.md](EXAMPLES.md) when uncertain about output format, graceful degradation behavior, or SVG→React component structure.

## Gotchas

- **Never fail silently when no generation tools are available.** Always provide the full prompt text and asset spec so the user can generate manually. Unavailable tools trigger the manual-instructions branch, not an error.
- **Don't use raster generation mode for icons or UI elements.** Icons need vector/SVG mode. Raster mode produces bitmap output inappropriate for scalable UI assets. Asset type must drive mode selection.
- **Avoid texture and material language in vector prompts.** Words like "glossy", "metallic", "emboss", "polished" produce raster-style rendering artifacts in vector mode. Use geometry and color language only: shapes, fills, stroke weights, colors.
- **Don't hardcode colors in SVG React components.** All colors must be driven by props with defaults drawn from the aesthetic profile. Hardcoded fills break theme switching and reusability.

## References

Load [REFERENCES.md](REFERENCES.md) when you need tool docs or library references:
- SVG element and attribute syntax → MDN Web Docs: SVG section
- SVG-to-React component conversion → SVGR docs
- Image optimization for raster outputs → Sharp, Squoosh CLI
