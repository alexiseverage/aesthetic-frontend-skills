# References — Asset Creation

## Image Generation

This skill is tool-agnostic. Install a tool-specific skill alongside this one for generation workflows (e.g. the `recraft` skill for Recraft V4 API/MCP access). Generated outputs — raster images and SVG files — are saved to `knowledge/aesthetics/<slug>/generated/`.

## SVG & Vector Assets

- **MDN Web Docs: SVG** — [https://developer.mozilla.org/en-US/docs/Web/SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) — Reference for SVG element and attribute syntax when constructing or modifying vectorized outputs.

- **SVGR** — [https://react-svgr.com/](https://react-svgr.com/) — Tool for converting SVG files to React components. Useful as a fallback or companion to the manual SVG → component conversion described in this skill.

## React Component Conventions

The SVG → React component conversion in this skill follows the `react-component-standards` skill (**optional external skill — install separately** with `npx skills add react-component-standards`). The SVG → React workflow in this skill is self-contained and does not require it; load `react-component-standards` only if you want full project-wide component conventions (naming, prop types, barrel exports) applied to the generated output.

## Image Formats & Compression

- **Sharp** — [https://sharp.pixelplumbing.com/](https://sharp.pixelplumbing.com/) — Recommended Node.js library for post-processing generated raster images (resize, compress, convert to WebP).

- **Squoosh CLI** — [https://github.com/GoogleChromeLabs/squoosh](https://github.com/GoogleChromeLabs/squoosh) — Browser and CLI tool for image optimization; useful for compressing generated texture assets before committing or serving.
