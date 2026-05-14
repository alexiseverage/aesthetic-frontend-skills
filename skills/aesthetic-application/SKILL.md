---
name: aesthetic-application
license: MIT
description: >
  Use this skill when you need a complete developer-ready design specification for a named
  aesthetic: W3C DTCG design tokens, CSS custom properties, cultural marker lists,
  component-level notes, and accessibility flags. Translates aesthetic understanding into
  implementable values across all 7 dimensions. Use when the user asks to 'make it look
  like X', requests design tokens or CSS variables, or needs a developer handoff spec
  grounded in an aesthetic. Depends on aesthetic-literacy.
  Do not use before an aesthetic is confirmed; do not use for accessibility resolution or component architecture.
metadata:
  version: "1.0.0"
  layer: applied
  status: stable
  tags: "design-tokens, css-variables, aesthetic-translation, component-spec, developer-handoff, dtcg"
  activation_keywords: "make it look, apply this aesthetic, design tokens for, translate this aesthetic, aesthetic but accessible, CSS variables for, design spec, full spec, component notes, cultural markers"
  depends_on: "aesthetic-literacy"
  known_limits: "Does not resolve accessibility conflicts; does not cover component architecture, interaction design, or layout structure"
  last_evaluated: ""
  eval_suite: ""
---

# Aesthetic Application

## Summary

Translates a named aesthetic into a complete, developer-ready design specification: a structured token specification table, cultural marker lists, component-level notes, and a flags section for conflicts. All decisions are concrete and implementable — never abstract mood descriptions. Covers all 7 dimensions of the aesthetic framework.

## When to Apply This Skill

Apply when:
- The user asks to "make it look like X", "apply this aesthetic", or "design tokens for X"
- The user needs a developer-handoff spec from an aesthetic direction
- The user asks for CSS variables, design tokens, or component notes grounded in an aesthetic
- The `image-analysis` skill has produced grounded values that need to be formatted as tokens

Do NOT apply when:
- No aesthetic has been identified (run `aesthetic-literacy` disambiguation first)
- The user wants implementation advice on components, accessibility resolution, or performance (out of scope)

## Dependencies

Requires: `aesthetic-literacy` (7-dimension framework, dictionary, non-negotiables)  
Works alongside: `image-analysis` (grounded values from images preferred over dictionary approximations when available)

## Knowledge Base Path

Before loading any profile, resolve the knowledge base root:

| Context | Resolved path |
|---|---|
| Project-level install | `knowledge/aesthetics/` at the **workspace root** |
| User/global install (`-g`) | `~/.agents/skills/knowledge/aesthetics/` |

Identify the workspace root by locating a parent directory containing `.git`, `package.json`, or `.agents/`.

> Throughout this skill, `knowledge/aesthetics/` refers to the resolved path above.

## 6-Step Application Workflow

### Step 1 — Confirm the aesthetic

Name the aesthetic explicitly. Do not proceed ambiguously.

- If the user is vague ("make it look cool" / "futuristic feel"), apply the `aesthetic-literacy` disambiguation protocol first
- If the requested term is a **subset or related aesthetic** (e.g., "outrun", "datamoshing", "old money", "Web 2.0 Gloss") rather than a canonical slug, identify the parent aesthetic, load its dictionary entry, read the **Subsets / Related** section, and note the subset's specific emphases that should be amplified. State: "Applying [parent aesthetic] in [connotation mode] mode, with [subset] emphasis."
- If the aesthetic has a knowledge profile at `knowledge/aesthetics/<slug>.md`, load it — especially the `## Analysis` section for grounded implementable values
- If no profile exists, use the `aesthetic-literacy` dictionary as the starting point
- State explicitly: "Applying [aesthetic name] in [connotation mode] mode."

### Step 2 — Establish connotation intent

Choose and state one of the four connotation modes:

| Mode | What it means | When to use |
|---|---|---|
| **Authentic** | Pure, period-accurate expression | Niche audiences, cultural products, self-aware contexts |
| **Nostalgic quotation** | Evokes but updates — contemporary usability, recognizable aesthetic DNA | Consumer products, lifestyle brands |
| **Ironic pastiche** | Knowing exaggeration for wit or commentary | Editorial, creative projects |
| **Contemporary revival** | Filtered through current design sensibility, fresh interpretation | Modern tech products with heritage positioning |

If the user has not specified, infer from context and state your inference explicitly. Ask if uncertain.

### Step 3 — Gather constraints

Collect and note the following before producing output:

- **WCAG AA**: Note any contrast conflicts. Flag them — do NOT resolve them. The developer decides how to handle aesthetics that conflict with accessibility requirements.
- **Dark mode**: Does the aesthetic have a natural dark mode variant? Or does dark mode fundamentally alter the aesthetic?
- **Platform**: Web, iOS, Android, print? (Motion and font capabilities differ significantly.)
- **Blending**: Is this a hybrid of multiple aesthetics? Name both parents. Identify the dimension that creates conflict.

### Step 4 — Make concrete per-dimension decisions

Work through all 7 dimensions. Every decision must be an implementable value:

| Dimension | Required output |
|---|---|
| **Palette** | Hex values with role assignment (background, surface, primary, secondary, accent) |
| **Typography** | Font family names (or type category if font is not specified), weights, sizes, tracking, line-height |
| **Texture** | CSS property + value (or "none") |
| **Shape** | Border-radius values (px), geometry style note |
| **Motion** | Duration range (ms), easing (named or cubic-bezier), preferred animation type |
| **Spatial conventions** | Baseline spacing unit (px), scale (4px / 8px / 12px etc.), density descriptor |
| **Cultural markers** | 3–5 signals to include; 2–3 signals to avoid |

### Step 5 — Resolve conflicts

If the aesthetic blend creates conflicts, resolve them explicitly:

- Name both parent aesthetics
- Identify the specific dimension where they conflict
- State the resolution per-dimension:
  - Which parent wins?
  - Or: a synthesis value that serves both?
  - Or: the conflict is user-resolved (flag it, don't guess)

Do not produce an unresolved blend. Unresolved blends produce incoherent output.

### Step 6 — Produce output

Produce all 4 output sections below.

---

## Output Formats

### 1. Token Specification

A flat, system-agnostic table of all token values covering Color (7 tokens), Typography (8 tokens), Shape (3), Motion (3), Spacing (6), and Layout (4 optional). Translate into your project's token system (CSS custom properties, Tailwind config, DTCG JSON, Sass variables, Swift/Android tokens, etc.).

Load [assets/token-spec-template.md](assets/token-spec-template.md) for the full blank template with all token names, categories, and notes.

> **Output format note**: The token table is the primary, format-agnostic output. If the developer explicitly requests DTCG JSON, CSS custom properties, or Tailwind config, translate into the requested format. A DTCG JSON example is in EXAMPLES.md.

### 2. Cultural Markers

**Include (3–5 signals)**:
- Signal 1
- Signal 2
- Signal 3

**Avoid (2–3 signals)**:
- Anti-signal 1
- Anti-signal 2

### 3. Component Notes

Brief, implementable notes for 12 key UI components: Buttons, Cards, Inputs, Navigation, Hero/header, Headings, Dividers, Links, Badges/tags, Modals/overlays, Alerts/notifications, Icons.

Load [assets/component-notes-template.md](assets/component-notes-template.md) for the full template with all component rows.

### 4. Flags

Issues that need developer attention — do not resolve, just surface:

- **WCAG conflicts**: List any color pairs from the palette that do not meet AA contrast (4.5:1 for text, 3:1 for large text)
- **Reduced-motion**: Note if the aesthetic is motion-dependent (effects that disappear under `prefers-reduced-motion`)
- **Dark mode gaps**: If a dark mode variant was not produced, note it
- **Aesthetic fatigue risk**: If the aesthetic is in "peak saturation" stage, note it for timing awareness
- **Blend conflicts unresolved**: Any conflicts from Step 5 that were flagged for user decision

## Examples

Load [EXAMPLES.md](EXAMPLES.md) when uncertain about output format, token table structure, or how to handle blend conflicts. Contains a complete Y2K spec, brutalist+WCAG resolution, and Art Deco blend example.

## Gotchas

- **Never output prose descriptions instead of tokens.** The developer needs `#C0C0C0`, not "metallic surfaces". Every output must be an implementable value.
- **Don't declare an aesthetic incompatible with WCAG AA without checking.** Raw brutalism (black on white, white on black) trivially meets AA. Identify the actual conflicting color pairs — don't make blanket incompatibility claims.
- **Never leave a blend unresolved.** "Combining the elegance of X with the clean lines of Y" is a brief, not a spec. Name the conflict dimension and produce explicit per-dimension decisions.
- **Always include Cultural Markers.** Tokens without the include/avoid cultural signal lists produce a generic spec that could be anything. Cultural markers are non-negotiable output.

## References

Load [REFERENCES.md](REFERENCES.md) when you need token format specs, accessibility thresholds, or font sourcing:
- W3C DTCG JSON token format → DTCG Format Specification
- WCAG contrast thresholds → WCAG 2.1 SC 1.4.3; WebAIM Contrast Checker
- Font sourcing → Google Fonts, Fonts In Use
