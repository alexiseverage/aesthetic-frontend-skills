# Copilot Instructions Template — aesthetic-frontend-skills

Copy the snippet below into your project's `.github/copilot-instructions.md`
(or append to an existing file). This works for all install methods — project-scoped,
git submodule, or user-scope — because skills are referenced by name, not by path.

---

## Project install (any method)

```markdown
## Available Skills

The following skills are available in this project. Load the relevant skill before
performing the described task.

- **aesthetic-literacy**
  Understand and characterize any named aesthetic (Y2K, vaporwave, brutalist, cottagecore,
  dark academia, etc.) across 7 formal dimensions. Foundation skill — load before any
  aesthetic work. Activate on: aesthetic, look and feel, style like, vibe, era, design
  movement.

- **aesthetic-research**
  Research a named aesthetic by collecting visual references from image sources (Pinterest,
  Dribbble, Behance, Google Images) and writing a structured knowledge profile to
  `knowledge/aesthetics/<slug>.md`. Activate on: research this aesthetic, find examples,
  visual references, build a profile.

- **image-analysis**
  Extract implementable design values from reference images: hex colors, px measurements,
  CSS technique names, easing patterns. Appends an Analysis section to knowledge profiles.
  Activate on: analyze these images, extract colors, CSS values, hex colors, border radius.

- **asset-creation**
  Generate visual assets (backgrounds, textures, icons, SVGs) using an available image
  generation tool, grounded in a knowledge profile. Also converts SVGs to typed React
  components. Activate on: generate an image, create a texture, make an SVG, SVG to React.

- **aesthetic-application**
  Translate a confirmed aesthetic into W3C DTCG design tokens, CSS custom properties,
  cultural markers, component notes, and accessibility flags. Activate on: make it look
  like, design tokens, CSS variables, full spec, component notes.

Knowledge profiles are stored in `knowledge/aesthetics/`. Skills read and write to this
directory automatically.
```

---

## User-scope install (`npx skills add alexiseverage/aesthetic-frontend-skills -g` or manual copy to `~/.agents/skills/`)

If you installed skills to `~/.agents/skills/`, agent clients that support Agent Skills discover them automatically — no `.github/copilot-instructions.md` entry is needed for skill discovery.

You may still want to add a note to your instructions so the agent knows when to apply them:

```markdown
## Available Skills

Aesthetic design skills are installed at user scope and available globally:
aesthetic-literacy, aesthetic-research, image-analysis, asset-creation,
aesthetic-application.

Knowledge profiles are stored in `~/.agents/skills/knowledge/aesthetics/` (user/global install)
or `knowledge/aesthetics/` at this project root (project-level install). Skills detect
which path to use automatically.
```

---

## Notes

- The `knowledge/aesthetics/` directory must be scaffolded before first use.
  - **Project-level install**: `mkdir -p knowledge/aesthetics` at your project root
  - **User/global install (`-g`)**: `mkdir -p ~/.agents/skills/knowledge/aesthetics`
- Skills resolve the correct path automatically: workspace-root `knowledge/aesthetics/` first, then `~/.agents/skills/knowledge/aesthetics/`.
- The canonical project-level install location for Agent Skills is `.agents/skills/`. The `npx skills` CLI installs here by default.
- Skill files are discovered by name. The `name` and `description` fields in each SKILL.md frontmatter control how the agent selects them.
