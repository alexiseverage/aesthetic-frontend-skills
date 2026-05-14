# Examples — Aesthetic Research

## Example prompts

Tasks that should activate this skill:

1. "Research glitch art UI and build me a profile."
2. "I want to do a vaporwave project — can you find visual references first?"
3. "Do another research pass on neubrutalism UI, update the existing profile."
4. "Build a knowledge profile for 'solarpunk web design'."
5. "Find me references for Y2K but specifically product UI, not fashion."

---

## Ideal response pattern — new profile

**For prompt 1 (glitch art — new profile):**

The agent:
1. Confirms no existing profile at `knowledge/aesthetics/glitch-art.md`
2. Constructs queries: "glitch art UI", "glitch art design", "datamosh web"
3. Searches available image sources for glitch art UI references, saves images (target 15) to `knowledge/aesthetics/glitch-art/images/`
4. Annotates each image across 7 dimensions (brief per-image notes)
5. Synthesizes dimension frequency table (canonical/common/variant)
6. Writes the full profile with YAML frontmatter, dimension synthesis, image descriptions, empty Analysis section, Connections section
7. Reports: "Profile created at `knowledge/aesthetics/glitch-art.md` — 17 images collected, evidence level: standard."

**Dimension synthesis excerpt:**

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant (<30%) |
|---|---|---|---|
| Palette | JPEG artifact smearing, magenta/cyan channel bleed on dark background | Electric green on black, desaturated base with error-color accent | Full-spectrum pixel sort artifacts |
| Texture | Digital corruption artifacts, pixel displacement, bit-error noise | Scan lines overlaid on content | VHS static, compression blocking |
| Shape | Fragmented hard-edged rectangles; no clean geometry | Channel-shift horizontal banding | Pixel sorting creating diagonal streams |

---

## Ideal response pattern — append to existing profile

**For prompt 3 (vaporwave — repeat run, existing profile):**

The agent:
1. Finds existing `knowledge/aesthetics/vaporwave.md` with `first_researched: 2025-01-10`, `image_count: 14`
2. States: "Existing profile found (14 images, standard evidence). This run will append — not overwrite."
3. Performs new image search with additional queries
4. Collects additional images
5. Appends `## Research Update 2025-06-12` section with:
   - Additional images reviewed count
   - Any new canonical observations
   - Dimension change summary (or "unchanged" for stable dimensions)
6. Does NOT modify any earlier sections of the file

---

## Anti-examples

**Anti-example 1: Overwriting an existing profile**

Agent loads `knowledge/aesthetics/vaporwave.md` and rewrites the entire file with the new research.

Why it fails: Profiles are append-only research logs. Overwriting destroys earlier dimension data, image counts, and update history. Earlier analysis (especially image-analysis outputs in `## Analysis`) is permanent — it must be preserved.

**Anti-example 2: Stopping at < 10 images without broadening**

> "Only 7 relevant images were found for 'solarpunk UI'. I couldn't find enough references to build a profile."

Why it fails: The skill requires broadening to Dribbble, Behance, or general image search before declaring insufficient. Even if all sources combined yield fewer than 10 images, the agent must produce a profile with `evidence_level: limited` and note the limitation explicitly. A limited-evidence profile is better than no profile.

**Anti-example 3: Mixing image description with synthesis**

> "In image 4 I can see pastel colors, which suggests canonical use of pastels in vaporwave."

Why it fails: Image descriptions (Step 6) are raw observations. Synthesis (Step 7) is the aggregation step. These must be kept structurally separate — raw per-image notes go in `## Image Descriptions`; frequency analysis goes in `## Dimension Synthesis`. Conflating them makes the profile hard to update on future runs.

**Anti-example 4: Naming exact fonts from screenshots**

> "Image 7 uses Helvetica Neue for the body text."

Why it fails: It is not possible to reliably identify specific font names from screenshots. The correct behavior is to describe the type category and visual characteristics (e.g., "geometric sans-serif, medium weight, wide tracking, lowercase-dominant") rather than assert a specific font name. Font identification belongs in `image-analysis`, and even there, exact font names from images should not be claimed.
