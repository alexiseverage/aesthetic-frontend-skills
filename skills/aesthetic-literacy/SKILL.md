---
name: aesthetic-literacy
license: MIT
description: >
  Use this skill when a user names or describes a visual aesthetic (Y2K, vaporwave, brutalist,
  cottagecore, dark academia, etc.), wants to compare or disambiguate aesthetics, or needs
  formal characterization before producing design tokens or assets. Provides the 7-dimension
  framework (palette, type, texture, shape, motion, spatial conventions, cultural markers)
  and a curated dictionary of 112 major aesthetics. Foundation for aesthetic-research,
  image-analysis, asset-creation, and aesthetic-application.
  Do not use for component implementation, layout, or accessibility decisions.
metadata:
  version: "1.0.0"
  layer: foundation
  status: stable
  tags: "aesthetic-movements, design-era, visual-culture, aesthetic-dictionary, period-style, semiotics, connotation"
  activation_keywords: "aesthetic, look and feel, style like, Y2K, vaporwave, brutalist, cottagecore, dark academia, retro, vintage, era, period style, design movement, vibe"
  known_limits: "Does not cover component implementation, layout, or accessibility; limited to the 112 dictionary entries and any research profiles present"
  last_evaluated: ""
  eval_suite: ""
---

# Aesthetic Literacy

## Summary

Gives an agent a structured framework for understanding named aesthetic movements as semiotic systems — not just visual preferences. Provides a 7-dimension decomposition model (palette, type, texture, shape, motion, spatial conventions, cultural markers) and a curated dictionary of 112 major aesthetics organized by family. Enables identification, characterization, disambiguation, and connotation-aware application of any named visual aesthetic.

Used as the foundation for `aesthetic-research`, `image-analysis`, `asset-creation`, and `aesthetic-application`.

## When to Apply This Skill

Apply when:
- A user names an aesthetic ("Y2K", "brutalist", "cottagecore") and wants to understand it formally
- A user uses a vague descriptor ("retro", "cozy", "clean") that needs mapping to a concrete aesthetic
- A user asks about the difference between two related aesthetics
- A design aesthetic needs to be characterized before tokens or assets are produced
- Another skill (`aesthetic-research`, `aesthetic-application`) needs to reason about aesthetic identity

Do NOT apply when the request is purely about component implementation, layout structure, or accessibility. Those are outside the scope of this skill.

## The 7-Dimension Framework

Every aesthetic is a system expressible along 7 formal dimensions. Always characterize all 7. Never reduce an aesthetic to one dimension alone (typically palette).

| # | Dimension | What it covers |
|---|---|---|
| 1 | **Palette** | Core hue family, saturation level, value range, contrast behavior, characteristic combinations |
| 2 | **Type** | Type category (serif/sans/mono/display), historical style, weight distribution, case convention, letter-spacing norms |
| 3 | **Texture** | Surface quality (smooth, noisy, glossy, matte, aged, digital artifact), technique (CSS gradient, SVG filter, backdrop-filter, image overlay) |
| 4 | **Shape** | Border-radius personality, geometry (rectilinear/curved/geometric/organic), silhouette energy, UI element proportions |
| 5 | **Motion** | Timing character (snappy/slow/elastic/linear), easing personality, animation types present (fade/slide/spring/morph), reduced-motion behavior |
| 6 | **Spatial Conventions** | Density (sparse/dense), whitespace use, layering / z-axis depth, grid structure (strict/free/radial), content hierarchy approach |
| 7 | **Cultural Markers** | Iconographic vocabulary, motifs, symbols, textual register — elements that signal membership in the aesthetic community |

### Non-Negotiables

Each aesthetic has 2–4 non-negotiable dimensions or properties. Removing them destroys the aesthetic identity even if other dimensions are correct. Always identify non-negotiables explicitly.

Example: Y2K requires metallic/chrome surface + bubbly geometry + acid/iridescent color. Remove any one and it becomes "vaguely retro digital" rather than distinctly Y2K.

### Connotation Layer

Every aesthetic carries cultural connotations beyond its visual properties, shaped by:
- **Origin context**: When and where did the aesthetic emerge? What cultural moment produced it?
- **Contemporary connotation**: How is it read today — authentic period document, nostalgic quotation, or ironic pastiche?
- **Audience resonance**: Who recognizes it and what do they associate with it?
- **Fatigue risk**: Has saturation reduced the aesthetic's cultural signal?

Connotation modes (use these terms explicitly):
- **Authentic**: Applied in its original spirit — earnest, not knowing
- **Nostalgic quotation**: Affectionate backward glance; warmth without irony
- **Ironic pastiche**: Self-aware quotation; the knowingness is part of the message
- **Contemporary revival**: Formal vocabulary from a historical period, updated execution — neither pastiche nor parody

## Aesthetic Dictionary

Dictionary entries are co-located with this skill in the `aesthetics/` subdirectory. Load the relevant file when characterizing a specific aesthetic.

**Lookup by slug**: `aesthetics/<slug>.md` (relative to this SKILL.md)

| Family | Count | Representative Slugs |
|---|---|---|
| **Digital / Internet-Native** | 21 | y2k, vaporwave, synthwave, early-internet, glitch, frutiger-aero, 8-bit-pixel, skeuomorphism, web-2-gloss, flat-design, material-design, corporate-grunge, myspace-chaos, neumorphism, claymorphism, pen-and-pixel, j-gov-futurism, liminal-space-backrooms, dreamcore-weirdcore, ai-slop-synthetic-corporate-art, hauntology |
| **Contemporary Lifestyle** | 14 | cottagecore, dark-academia, warm-minimalism (supersedes quiet-luxury), maximalism, 1990s-minimalism, decora-kei, magical-girl, witchcore, gorpcore, balletcore, barbiecore, coastal-grandmother, goblincore, nu-goth-pastel-goth |
| **Historical Design Movements** | 33 | art-nouveau, art-deco, swiss-international, bauhaus, memphis, brutalism, arts-and-crafts, vienna-secession, futurism, vorticism, suprematism, constructivism, de-stijl, streamline-moderne, wpa-poster-style, wartime-propaganda, scandinavian-modern, die-neue-typographie, mid-century-modern, pop-art, op-art, psychedelic, atomic-age, punk-zine, new-wave-typography, grunge-typography, desktop-publishing, rave-flyer, city-pop, blue-note-jazz-modernism, chinoiserie, gothic-revival, wabi-sabi-slow-living |
| **Emerging / Hybrid** | 8 | organic-digital, solarpunk, corporate-memphis, glassmorphism, neubrutalism, quiet-luxury (redirect → warm-minimalism), cybersigilism, scandi-noir |
| **Technical / Institutional** | 5 | high-performance-hmi, sports-scorebug, prescription-label-clarity, bloomberg-terminal-monochrome, cheminformatics-map-explorer |
| **Material / Print Craft** | 4 | risograph, harm-reduction-zine, queer-nightlife-ephemera, fairground-carnival-poster-art |
| **Vernacular / Commercial** | 11 | mexican-rotulismo, guochao, konbini-utility, convenience-store-backoffice, b2b-quick-order-grid, lotto, casino, tiki-polynesian-pop, chicano-lowrider-art, board-game-box-art, trading-card-game-design |
| **Speculative / Robotics** | 16 | cyberpunk, cassette-futurism, nanopunk, techno-noir, apple-core-tech, uncanny-android, dieselpunk, steampunk, post-apocalyptic-scavenged-tech, space-western, cute-tech, companion-bot, mecha-kaiju, anime-mecha-realism, biomechanical, chibi-mecha |

*Full listing: see `aesthetics/` directory. 112 total entries across 8 families.*

Each entry specifies: palette, type, texture, shape, motion, spatial conventions, cultural markers, non-negotiables, connotation, and subsets/related aesthetics (where applicable). Fatigue notes appear where applicable.

---

## Disambiguation Protocol

When aesthetic cues are vague or overlapping:

1. **Extract cues**: List the mood/descriptor words the user gave ("warm", "retro", "cozy", "clean")
2. **Map to clusters**: Identify which aesthetics in the dictionary are compatible with those cues
3. **Identify the axis of ambiguity**: What single question would resolve the ambiguity? (Often: era/decade, warmth vs. coolness, earnest vs. ironic)
4. **Ask ONE targeted question**: Never ask multiple disambiguation questions at once
5. **Confirm and proceed**: After the answer, name the aesthetic you're working with and continue

## Examples

Load [EXAMPLES.md](EXAMPLES.md) when uncertain about output format, ideal response structure, or to review anti-patterns.

## Gotchas

- **Don't reduce an aesthetic to one dimension (usually palette).** A design with Y2K palette but flat surfaces and neutral sans-serif type will not read as Y2K. All 7 dimensions must be addressed, and non-negotiables (e.g., bubbly geometry + metallic surface for Y2K) are as important as palette.
- **Don't conflate neighboring aesthetics.** Vaporwave and synthwave share palette adjacency but differ in origin, cultural loading, and formal properties. Conflating them produces a hybrid with neither aesthetic coherence nor cultural clarity.
- **Don't conflate a subset with its parent aesthetic.** If a user requests a term that is a documented subset (e.g., "outrun" within synthwave, "datamoshing" within glitch, "old money" adjacent to quiet-luxury), name the canonical parent aesthetic, load the full dictionary entry, read the **Subsets / Related** section, and amplify the subset's specific properties rather than treating it as a synonym. The subset's distinct characteristics — palette emphasis, motifs, technique constraints — are the design signal.
- **Don't skip disambiguation for vague descriptors.** "Retro" spans at least 5 distinct aesthetics. Ask one targeted question before producing any design decisions.
- **Always run a connotation audit before confirming a historical aesthetic.** Art Deco may read as "timeless luxury" or "Gilded Age excess" depending on execution context. Surface the ambiguity first.

Do NOT run disambiguation when the aesthetic is named explicitly and unambiguously.

## Knowledge Base Lookup

Before characterizing any aesthetic, check whether a research profile exists at `knowledge/aesthetics/<slug>.md`. If it does, the profile supersedes dictionary definitions for dimension frequencies (canonical/common/variant tiers are empirically grounded there). Always prefer the profile's dimension analysis over the dictionary entry.

**Path resolution**: check `knowledge/aesthetics/` at the workspace root first (identify workspace root by locating a parent directory containing `.git`, `package.json`, or `.agents/`); fall back to `~/.agents/skills/knowledge/aesthetics/` for user/global installs.

Slug format: lowercase-hyphenated (e.g., `dark-academia`, `frutiger-aero`, `neubrutalism`).

If a profile does not exist and the aesthetic is unknown or niche, defer to the `aesthetic-research` skill before proceeding.
