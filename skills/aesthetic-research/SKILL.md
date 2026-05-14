---
name: aesthetic-research
license: MIT
description: >
  Use this skill when you need to build or update a visual reference library for a named
  aesthetic. Searches image sources (Pinterest, Dribbble, Behance, Google Images), collects
  10-25 reference images, annotates them across the 7-dimension framework, and writes a
  structured knowledge profile to knowledge/aesthetics/<slug>.md. Profiles are append-only
  — new runs append a dated section, never overwrite. Requires internet access. Depends on
  aesthetic-literacy.
  Do not use when a profile already exists and tokens are needed — use aesthetic-application instead.
compatibility: Requires internet access to search image sources (Pinterest, Dribbble, Behance, Google Images).
allowed-tools: browser, fetch
metadata:
  version: "1.0.0"
  layer: applied
  status: stable
  tags: "visual-research, knowledge-base, image-collection, dimension-analysis"
  activation_keywords: "research this aesthetic, find examples of, what does X look like visually, search for references, gather visual references, build a profile for, get me images of"
  depends_on: "aesthetic-literacy"
  known_limits: "Does not produce design tokens or CSS values; image sourcing depends on tool availability and target site accessibility"
  last_evaluated: ""
  eval_suite: ""
---

# Aesthetic Research

## Summary

Researches a named aesthetic by collecting visual reference images, annotating them across the 7-dimension framework from `aesthetic-literacy`, and writing a structured knowledge profile to `knowledge/aesthetics/<slug>.md`. On repeat runs, appends a dated update section rather than overwriting.

## When to Apply This Skill

Apply when:
- A named aesthetic needs visual evidence grounding before token production
- The user asks to "look up", "research", or "find references" for an aesthetic
- The agent is about to apply an aesthetic for which no knowledge profile yet exists
- The user explicitly requests an updated or deeper research pass

Do NOT apply when:
- A research profile already exists and the user wants to produce tokens/assets (use `aesthetic-application` directly)
- The aesthetic is well-covered in the dictionary and the user wants a quick characterization (use `aesthetic-literacy` alone)

## Dependencies

Requires: `aesthetic-literacy` (7-dimension framework, slug conventions)

## Knowledge Base Path

Before reading or writing any profile, resolve the knowledge base root:

| Context | Resolved path |
|---|---|
| Project-level install | `knowledge/aesthetics/` at the **workspace root** |
| User/global install (`-g`) | `~/.agents/skills/knowledge/aesthetics/` |

Identify the workspace root by locating a parent directory containing `.git`, `package.json`, or `.agents/`. If the resolved path does not exist and you need to write, create it first.

> Throughout this skill, `knowledge/aesthetics/` refers to the resolved path above.

## Workflow

### Step 1 — Check for existing profile

Check whether `knowledge/aesthetics/<slug>.md` already exists.

- **If yes**: Note the existing image count and last updated date. This run will APPEND to the profile, not replace it.
- **If no**: This run creates the profile from scratch.

Slug format: lowercase-hyphenated (e.g., `dark-academia`, `frutiger-aero`, `neubrutalism`).

**Alias check**: If the user's requested term differs from the canonical slug (e.g., user said "webcore", profile slug is `early-internet`), record the requested term as an alias:
- If the profile already exists, append the new term to its `aliases` frontmatter field if not already present.
- If the profile is being created now, populate `aliases` with the requested term if it differs from the slug.
- Also add the term to the `aliases` field of the matching dictionary entry in the `aesthetic-literacy` skill (`aesthetics/<slug>.md`, co-located with that skill's SKILL.md) if that file exists and does not already list it.
  > **Note**: If the `aesthetic-literacy` skill is installed at a different path (e.g., user-global at `~/.agents/skills/` vs. the current project install), the dictionary file may not be writable or locatable. In that case, skip the dictionary write and record the alias only in the profile frontmatter `aliases` field.

### Step 2 — Construct query variants

Generate at least 2 query variants to broaden coverage:

- `<aesthetic name> UI`
- `<aesthetic name> design`
- `<aesthetic name> web`
- `<aesthetic name> app` (for digital-native aesthetics)
- `<aesthetic name> graphic design` (for print/historical aesthetics)

URL-encode the query: spaces → `%20`, special chars → percent-encoded.

### Step 3 — Search for visual references

For each query variant, search using available image sources and browser tools. Good sources include Pinterest, Dribbble, Behance, Google Images, or any image repository with relevant design content. Use whatever tools are configured in your environment.

### Step 4 — Save images

For each image found:
1. Save it to `knowledge/aesthetics/<slug>/images/` with sequential naming: `01.png`, `02.png`, etc.
2. Note the source URL for reference

**Target**: 15 images  
**Minimum acceptable**: 10 images (below this, flag `evidence_level: limited`)  
**Maximum**: 25 images (stop here even if more are available)

If a result links to a page without a usable image, skip it.

### Step 5 — Broaden search if needed

If total images collected across all query variants is < 10, broaden your search:

1. Try **Dribbble**: `https://dribbble.com/search/<encoded-query>`
2. Try **Behance**: `https://www.behance.net/search/projects?search=<encoded-query>`
3. Try a general image search

Even with < 10 images from all sources combined, always produce a profile — set `evidence_level: limited` in the frontmatter and note this clearly in the `## Research Updates` section.

### Step 6 — Annotate images

For each image, briefly note what you observe across the 7 dimensions. These are raw observations, not synthesis. Example:

```
Image 3: VHS scan lines, pastel pink/lavender gradient, katakana text, perspective grid floor, classical marble statue, dreamy unmoored composition
```

### Step 7 — Synthesize dimensions

Aggregate annotations across all images. For each dimension, classify findings into three tiers:

- **Canonical** (≥70% of images): This property defines the aesthetic — deviation breaks it
- **Common** (30–70%): Frequently observed but not load-bearing — presence reinforces, absence doesn't break
- **Variant** (<30%): Occasional — signals aesthetic range, not requirement

## Profile Format

Write to `knowledge/aesthetics/<slug>.md` using this exact structure. Field constraints:
- `slug`: lowercase letters, numbers, and hyphens only — must match the filename (e.g. `dark-academia`)
- `image_count`: integer ≥ 0, cumulative across all research runs
- `evidence_level`: `standard` (≥10 images) or `limited` (<10 images)
- `new_aesthetic`: boolean — `true` if not in the `aesthetic-literacy` dictionary
- `aliases`: list of alternative/community names that resolve to this slug

```markdown
---
slug: <slug>
label: <Human-Readable Label>
first_researched: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
source: <image-source>     # e.g. pinterest, dribbble, behance, mixed
image_count: <integer>
evidence_level: standard   # standard (≥10) | limited (<10)
new_aesthetic: false       # true = not in aesthetic-literacy dictionary
aliases: []                # alternative names / community terms that resolve to this aesthetic
---

# <Label>

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant (<30%) |
|---|---|---|---|
| Palette | ... | ... | ... |
| Type | ... | ... | ... |
| Texture | ... | ... | ... |
| Shape | ... | ... | ... |
| Motion | ... | ... | ... |
| Spatial | ... | ... | ... |
| Cultural markers | ... | ... | ... |

## Image Descriptions

1. [pin URL if available] — brief annotation across 7 dimensions
2. ...

## Analysis

_To be populated by the image-analysis skill._

## Connections

Related aesthetics from the dictionary: [list with one-line distinction from each]

## Research Updates

_Populated on repeat research runs._
```

## Append-Only Rule

**NEVER overwrite a profile.** On repeat runs, add this section at the end:

```markdown
## Research Update <YYYY-MM-DD>

- Additional images reviewed: <count>
- Evidence level after update: standard | limited
- Source(s): pinterest | dribbble | behance | other
- New canonical observations: ...
- Dimension changes: [dimension]: [was] → [now] (or "unchanged")
```

Do NOT modify earlier sections. The profile is an append-only research log.

## Naming Novel Aesthetics

If the researched aesthetic is not present in the `aesthetic-literacy` dictionary, set `new_aesthetic: true` in the profile frontmatter. The profile becomes the canonical definition — there is no dictionary entry to fall back to.

## Recording Aliases

When a requested term resolves to an existing aesthetic rather than introducing a new one, record the term so future lookups succeed without ambiguity:

1. Add the term to `aliases` in the knowledge profile frontmatter (`knowledge/aesthetics/<slug>.md`)
2. Add the term to `aliases` in the dictionary entry (`aesthetics/<slug>.md`, co-located with the `aesthetic-literacy` skill)
3. Do this even when no new visual research is performed — alias bookkeeping is a valid, minimal outcome of a research run.## Examples

Load [EXAMPLES.md](EXAMPLES.md) when uncertain about output format, ideal response structure, or to review anti-patterns.

## Gotchas

- **Never overwrite an existing profile.** Profiles are append-only research logs. Overwriting destroys earlier dimension data, image counts, `## Analysis` sections, and update history.
- **Don't stop at fewer than 10 images without broadening first.** Broaden to Dribbble, Behance, or general image search. Even if all sources combined yield < 10 images, produce the profile with `evidence_level: limited`. A limited-evidence profile is better than no profile.
- **Keep image descriptions and dimension synthesis structurally separate.** Raw per-image observations go in `## Image Descriptions`. Frequency analysis goes in `## Dimension Synthesis`. Conflating them makes the profile hard to update on future runs.
- **Don't claim to identify exact font names from screenshots.** Describe type category and visual characteristics instead (e.g., "geometric sans-serif, medium weight, wide tracking").