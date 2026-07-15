# Migration and Research Backfill Backlog

Goal: turn the warning-mode audit output and the Storybook Gothic pilot into a future Kanban backlog for migrating aesthetic dictionary entries to the target canonical-entry model.

Source of evidence:
- `make audit` reports 1406 schema audit warning(s).
- `python3 scripts/validate_dictionary.py --schema-mode warn` reports 122 full entries checked, 122 full entries valid, 1 redirect valid, and 1341 target-schema warning(s).
- `python3 scripts/validate_profile.py --schema-mode warn` reports 67/67 profiles valid and 5 target-schema warning(s).
- Storybook Gothic is the only current dictionary entry already in the target canonical-entry shape and is the migration exemplar.

## Classification rules

- Mechanical normalization: warnings that can be fixed without new aesthetic research or design judgment. These are schema housekeeping fixes such as exact shared-field synchronization, explicit missing boilerplate sections for already-limited profiles, or confirming an already-canonical entry remains compliant.
- Content backfill needed: a research profile already exists, but the dictionary entry still needs to be rewritten into the target canonical sections using the existing profile and research notes. These should be engineer/writer cards, not researcher-first cards, unless the implementer finds a contradiction.
- Research/provenance required: the dictionary entry has no `knowledge/aesthetics/<slug>.md` research profile. These need researcher-first cards before canonical-entry migration.

## Summary counts

- Full dictionary entries: 122
- Redirect entries: 1
- Research profiles: 67
- Dictionary entries missing research profiles: 55
- Profiles without dictionary entries: 0
- Dictionary/profile relationship warnings: 60 total
  - 55 missing research profiles
  - 5 alias mismatches
- Profile target-schema warnings: 5
- Dictionary target-schema warnings: 1341

## Mechanical normalization

These can be batched as a small cleanup card. They should be done before or alongside content backfill because they reduce noisy audit output without changing the migration model.

1. Already canonical / exemplar
   - `storybook-gothic`

2. Shared-field alias mismatches between dictionary and profile
   - `decora-kei`
   - `guochao`
   - `high-performance-hmi`
   - `mexican-rotulismo`
   - `risograph`

3. Research profiles missing the target `## Image Descriptions` marker while declaring `evidence_level: limited` and `image_count: 0`
   - `decora-kei`
   - `guochao`
   - `high-performance-hmi`
   - `mexican-rotulismo`
   - `risograph`

Recommended card: normalize the five profile/dictionary relationship warnings and add explicit no-image-corpus image-description notes where appropriate, then rerun `make audit` to confirm the relationship/profile warning count drops.

## Content backfill needed, no researcher first

These entries already have research profiles, so the next step is canonical-entry backfill from existing repository evidence. Use Storybook Gothic as the target shape. Each batch should keep entries small enough for review, update the dictionary entry only when the research profile supports the claim, and avoid inventing provenance.

- `aesthetic-movement`
- `ai-slop-synthetic-corporate-art`
- `anime-mecha-realism`
- `apple-core-tech`
- `b2b-quick-order-grid`
- `balletcore`
- `barbiecore`
- `beaux-arts`
- `biomechanical`
- `bloomberg-terminal-monochrome`
- `blue-note-jazz-modernism`
- `board-game-box-art`
- `casino`
- `cassette-futurism`
- `cheminformatics-map-explorer`
- `chibi-mecha`
- `chicano-lowrider-art`
- `chinoiserie`
- `coastal-grandmother`
- `companion-bot`
- `convenience-store-backoffice`
- `cute-tech`
- `cyberpunk`
- `cybersigilism`
- `decora-kei`
- `dieselpunk`
- `dreamcore-weirdcore`
- `fairground-carnival-poster-art`
- `goblincore`
- `gorpcore`
- `gothic-revival`
- `guochao`
- `harm-reduction-zine`
- `hauntology`
- `high-performance-hmi`
- `high-tech-architecture`
- `italian-radical-design`
- `j-gov-futurism`
- `japanese-metabolism`
- `konbini-utility`
- `liminal-space-backrooms`
- `lotto`
- `magical-girl`
- `mecha-kaiju`
- `mexican-rotulismo`
- `nanopunk`
- `new-objectivity`
- `nu-goth-pastel-goth`
- `polish-poster-school`
- `post-apocalyptic-scavenged-tech`
- `prairie-school`
- `prescription-label-clarity`
- `queer-nightlife-ephemera`
- `risograph`
- `scandi-noir`
- `shaker-design`
- `space-western`
- `sports-scorebug`
- `steampunk`
- `techno-noir`
- `tiki-polynesian-pop`
- `trading-card-game-design`
- `ulm-school`
- `uncanny-android`
- `wabi-sabi-slow-living`
- `witchcore`

Recommended batch order:
1. Mechanical/profile-backed pilot batch: `decora-kei`, `guochao`, `high-performance-hmi`, `mexican-rotulismo`, `risograph`. This batch proves cleanup plus canonical backfill on entries with known profile warnings.
2. Interface/domain-specific profile-backed entries: `b2b-quick-order-grid`, `bloomberg-terminal-monochrome`, `cheminformatics-map-explorer`, `companion-bot`, `convenience-store-backoffice`, `harm-reduction-zine`, `high-performance-hmi`, `j-gov-futurism`, `konbini-utility`, `lotto`, `prescription-label-clarity`, `sports-scorebug`.
3. Contemporary culture profile-backed entries: `balletcore`, `barbiecore`, `coastal-grandmother`, `cyberpunk`, `cybersigilism`, `decora-kei`, `dreamcore-weirdcore`, `goblincore`, `gorpcore`, `hauntology`, `liminal-space-backrooms`, `nu-goth-pastel-goth`, `queer-nightlife-ephemera`, `scandi-noir`, `witchcore`.
4. Historical/material profile-backed entries: `beaux-arts`, `biomechanical`, `blue-note-jazz-modernism`, `chicano-lowrider-art`, `chinoiserie`, `dieselpunk`, `gothic-revival`, `guochao`, `high-tech-architecture`, `italian-radical-design`, `japanese-metabolism`, `mexican-rotulismo`, `new-objectivity`, `polish-poster-school`, `prairie-school`, `risograph`, `shaker-design`, `techno-noir`, `tiki-polynesian-pop`, `ulm-school`, `wabi-sabi-slow-living`.
5. Entertainment/speculative profile-backed entries: `ai-slop-synthetic-corporate-art`, `anime-mecha-realism`, `apple-core-tech`, `board-game-box-art`, `casino`, `cassette-futurism`, `chibi-mecha`, `cute-tech`, `fairground-carnival-poster-art`, `magical-girl`, `mecha-kaiju`, `nanopunk`, `post-apocalyptic-scavenged-tech`, `space-western`, `steampunk`, `trading-card-game-design`, `uncanny-android`.

## Research/provenance required

These entries are high-risk for direct migration because the audit reports no matching research profile. They need researcher-first cards that create `knowledge/aesthetics/<slug>.md` and, when sources are gathered, append a research log if useful. Only after that should an engineer migrate the dictionary entry to the target canonical shape.

- `1990s-minimalism`
- `8-bit-pixel`
- `art-deco`
- `art-nouveau`
- `arts-and-crafts`
- `atomic-age`
- `bauhaus`
- `brutalism`
- `city-pop`
- `claymorphism`
- `constructivism`
- `corporate-grunge`
- `corporate-memphis`
- `cottagecore`
- `dark-academia`
- `de-stijl`
- `desktop-publishing`
- `die-neue-typographie`
- `early-internet`
- `flat-design`
- `frutiger-aero`
- `futurism`
- `glassmorphism`
- `glitch`
- `grunge-typography`
- `material-design`
- `maximalism`
- `memphis`
- `mid-century-modern`
- `myspace-chaos`
- `neubrutalism`
- `neumorphism`
- `new-wave-typography`
- `op-art`
- `organic-digital`
- `pen-and-pixel`
- `pop-art`
- `psychedelic`
- `punk-zine`
- `rave-flyer`
- `scandinavian-modern`
- `skeuomorphism`
- `solarpunk`
- `streamline-moderne`
- `suprematism`
- `swiss-international`
- `synthwave`
- `vaporwave`
- `vienna-secession`
- `vorticism`
- `warm-minimalism`
- `wartime-propaganda`
- `web-2-gloss`
- `wpa-poster-style`
- `y2k`

## High-demand thin-entry priority plan

All high-demand entries named in the task are in the research/provenance-required class. They also have very short compact dictionary entries, no research profile, 12 target-schema warnings each, and no target canonical sections.

| Priority | Slug | Current evidence | Recommended next card |
| --- | --- | --- | --- |
| P0 | `y2k` | 104-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `art-deco` | 103-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `art-nouveau` | 112-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `swiss-international` | 90-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `cottagecore` | 101-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `dark-academia` | 114-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `early-internet` | 109-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `glassmorphism` | 107-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `neubrutalism` | 104-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `maximalism` | 77-word dictionary entry, no research profile | researcher-first, then canonical migration |
| P0 | `organic-digital` | 100-word dictionary entry, no research profile | researcher-first, then canonical migration |

Recommended P0 research batches:
1. Historical design foundations: `art-deco`, `art-nouveau`, `swiss-international`.
2. Contemporary lifestyle/community aesthetics: `cottagecore`, `dark-academia`, `maximalism`.
3. Web/UI-native aesthetics: `y2k`, `early-internet`, `glassmorphism`, `neubrutalism`, `organic-digital`.

## Recommended future Kanban cards

1. Research P0 historical design foundations
   - Assignee: `researcher`
   - Slugs: `art-deco`, `art-nouveau`, `swiss-international`
   - Deliverable: research profiles with source-grounded dimension synthesis, image/corpus notes, connections, and research update sections.
   - Downstream: engineer canonical-entry migration for the same slugs.

2. Research P0 contemporary lifestyle/community aesthetics
   - Assignee: `researcher`
   - Slugs: `cottagecore`, `dark-academia`, `maximalism`
   - Deliverable: research profiles that distinguish historical/community usage from superficial branding tropes and flag cultural/ethical risks.
   - Downstream: engineer canonical-entry migration for the same slugs.

3. Research P0 web/UI-native aesthetics
   - Assignee: `researcher`
   - Slugs: `y2k`, `early-internet`, `glassmorphism`, `neubrutalism`, `organic-digital`
   - Deliverable: research profiles emphasizing web/app translation, accessibility constraints, representative interface patterns, and anti-patterns.
   - Downstream: engineer canonical-entry migration for the same slugs.

4. Mechanical audit cleanup
   - Assignee: `engineer`
   - Slugs: `decora-kei`, `guochao`, `high-performance-hmi`, `mexican-rotulismo`, `risograph`
   - Deliverable: resolve alias mismatches and profile target-section warnings; verify profile warning count and relationship warning count drop.

5. Profile-backed canonical migration pilot batch
   - Assignee: `engineer`
   - Slugs: `decora-kei`, `guochao`, `high-performance-hmi`, `mexican-rotulismo`, `risograph`
   - Deliverable: target canonical dictionary entries using existing profiles only; verify target warnings decrease and no new validator failures appear.

## Acceptance criteria for future cards

- Run `make audit` before and after each batch and report warning deltas.
- Run `make check` before handoff.
- Run `skills add . -l --full-depth` before handoff.
- Do not copy machine-local paths into docs, commits, PR bodies, or public artifacts.
- Keep source claims in research profiles/logs; keep canonical dictionary entries concise and source-grounded.
- If a batch uncovers contradictory or insufficient evidence, stop that slug and create or block on a researcher card instead of inventing content.
