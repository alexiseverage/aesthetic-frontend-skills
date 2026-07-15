# RFC: Aesthetic Artifact Model and Schema Migration

## Status

Proposed baseline for the aesthetic refactor pilot. This document is intentionally non-enforcing: it defines the target model, migration policy, and examples for future validators without making current main fail strict checks.

## Problem Statement

The repository already contains two kinds of durable aesthetic knowledge:

- curated dictionary entries under `skills/aesthetic-literacy/aesthetics/`
- research profiles under `knowledge/aesthetics/`

Recent expansion work has shown that the distinction is valuable but not yet explicit enough for maintainers, future Kanban workers, or validators. Some entries are highly polished canonical guidance, while some research profiles preserve source-backed synthesis and update history. Future work needs a third, append-only audit trail for research observations so contributors can add evidence without rewriting prior conclusions or accidentally changing production guidance.

## Goals

- Define the three-artifact model used by future aesthetic entries.
- Document the target schema for each artifact before enforcing it.
- Give contributors copyable examples for the canonical aesthetic entry and append-only research log.
- Establish a staged enforcement path that starts in audit/warning mode and avoids breaking current main.
- Preserve room for batch migration and human review of culturally specific or evidence-sensitive aesthetics.

## Non-goals

- This RFC does not mass-migrate existing aesthetics.
- This RFC does not introduce strict validation failures for current entries.
- This RFC does not replace the existing `skills/aesthetic-literacy` skill contract.
- This RFC does not require every existing entry to have a research profile immediately.

## Three-artifact Model

### 1. Canonical aesthetic entry

The canonical aesthetic entry is the production-facing dictionary record used by `aesthetic-literacy` and downstream design agents. It lives at:

```text
skills/aesthetic-literacy/aesthetics/<slug>.md
```

It should be concise enough for agents to load during design work, but complete enough to describe the aesthetic as a usable visual system. It owns:

- canonical slug, label, family, era, aliases, status, and evidence level
- related/subset references that can be validated as slugs
- seven dimensions: palette, type, texture, shape, motion, spatial conventions, cultural markers
- non-negotiables that preserve aesthetic identity
- connotation and scope guidance
- frontend/UI guidance, CSS translation, and typography/font guidance
- cultural/ethical notes and anti-patterns
- implementation notes that are stable enough to be production guidance

The canonical entry should not be a raw research dump. If a detail is uncertain, source-specific, or likely to change, record it in a structured research profile or append-only research log first.

### 2. Structured research profile

The structured research profile is the source-grounded synthesis layer. It lives at:

```text
knowledge/aesthetics/<slug>.md
```

It should use validated frontmatter and the existing profile sections where possible. It owns:

- evidence level and corpus metadata
- dimension synthesis with canonical/common/variant tiers
- source bibliography and evidence links
- analysis that explains how evidence maps to frontend guidance
- relationship boundaries between neighboring aesthetics
- research update notes that summarize changes without deleting earlier context

When a profile exists, it supersedes the dictionary entry for empirical dimension frequencies. The canonical entry should distill the profile into usable design guidance, not duplicate every source note.

### 3. Append-only research log

The append-only research log is the durable change/audit trail for evidence observations. It should stay out of the installed-user hot path and live alongside the maintainer-facing research profile, for example:

```text
knowledge/aesthetics/<slug>/research-log.md
knowledge/aesthetics/<slug>/sources.md
knowledge/aesthetics/<slug>/images/
```

The one-file structured profile at `knowledge/aesthetics/<slug>.md` remains the concise synthesis layer; the nested log/sources/images directory preserves provenance and raw update history.

The log owns:

- dated evidence observations
- source URLs or source identifiers
- who/what collected the evidence
- whether the observation affects palette, type, texture, shape, motion, spatial conventions, cultural markers, connotation, or boundaries
- confidence and follow-up notes
- explicit supersession notes when newer evidence changes an earlier interpretation

Append-only means new entries are added after existing entries. Prior log entries should not be deleted or silently rewritten. Corrections should be represented as new dated entries that identify what they supersede and why.

## Source-of-truth Rules

- The canonical aesthetic entry is the source of truth for production design guidance.
- The structured research profile is the source of truth for evidence synthesis and confidence.
- The append-only research log is the source of truth for provenance and update history.
- Validators should eventually check consistency across all three, but early validators must report warnings instead of blocking current main.
- Human review remains required for culturally specific, sacred, regional, or otherwise high-risk aesthetics.

## Target Schema Summary

### Canonical aesthetic entry

Required frontmatter:

- `slug`: lowercase hyphenated slug matching filename
- `label`: display name
- `family`: taxonomy family
- `era`: approximate period or `contemporary`
- `aliases`: array of alternate names
- `status`: usually `canonical`; redirect entries use a separate minimal schema
- `evidence_level`: for example `researched`, `synthesis`, `legacy`, or another future enum value
- `related`: array of related aesthetic slugs, or an empty array
- `subsets`: array of subset aesthetic slugs, or an empty array

Required body sections or labels:

- `## Scope`
- `## 7-Dimension Profile`
- `**Palette**:`
- `**Type**:`
- `**Texture**:`
- `**Shape**:`
- `**Motion**:`
- `**Spatial**:`
- `**Cultural markers**:`
- `## Non-Negotiables` or `**Non-negotiables**:`
- `## Connotation` or `**Connotation**:`
- `## Related / Subsets`
- `## Frontend / UI Guidance`
- `## CSS Translation`
- `## Typography / Fonts`
- `## Cultural / Ethical Notes`
- `## Anti-Patterns`

### Structured research profile

Required frontmatter should continue to match `skills/aesthetic-research/knowledge/schema.json` until a later RFC changes it. Required body sections should include:

- `## Dimension Synthesis`
- `## Image Descriptions` or an explicit statement that no image corpus was collected
- `## Analysis`
- `## Connections`
- `## Research Updates`

### Append-only research log

Recommended per-entry metadata:

- `logged_at`: ISO date or timestamp
- `researcher`: human or agent identifier
- `source_url` or `source_id`
- `evidence_type`: image, text, video, primary-source, secondary-source, field-note, correction
- `affected_dimensions`: one or more of the seven dimensions plus optional connotation/boundary tags
- `confidence`: low, medium, high
- `supersedes`: optional earlier log entry identifier

Recommended body sections:

- `## Observation`
- `## Dimension Impact`
- `## Canonical Entry Impact`
- `## Follow-up`

## Enforcement Model

### Phase 1: audit/warning mode

Add documentation, examples, and optional validators that warn about missing target-schema fields. Current main must remain green. Warnings should be easy to inspect and should not block ordinary documentation or entry fixes.

Acceptance criteria:

- RFC and templates exist.
- Existing `make check` remains green.
- Skills CLI installation check remains green.
- Any new validator is opt-in or warning-only.

### Phase 2: no-new-regressions

Once maintainers agree on the schema, validators may block newly added or newly touched entries from omitting required fields. Existing legacy entries should be grandfathered or reported separately.

Acceptance criteria:

- New entries must include required frontmatter and body labels.
- Modified entries cannot remove required labels that were already present.
- CI reports legacy gaps separately from new regressions.

### Phase 3: batch migration

Migrate existing entries in small reviewed batches. Each batch should preserve current guidance, add missing schema fields, and avoid shallow filler.

Acceptance criteria:

- Each batch is reviewable in one PR.
- Entries with weak evidence are flagged for research rather than padded.
- Cultural-sensitivity notes are preserved or added where needed.

### Phase 4: strict default

After migration, validators may make the target schema strict by default. Escape hatches should be explicit and rare, such as redirect entries or documented legacy exceptions.

Acceptance criteria:

- Strict checks are part of `make check`.
- Redirect entries have a separate minimal schema.
- Validator output points contributors to the RFC and templates.

## Migration Policy for Future Kanban Workers

- Prefer small conventional commits grouped by artifact type or aesthetic batch.
- Do not invent shallow filler to satisfy a schema field.
- If evidence is missing, create or update research artifacts first.
- Keep append-only logs chronological; add corrections as new entries.
- Do not make strict validators block main until the batch migration is complete.
- Report exact validation commands and output summaries in Kanban handoffs and PR bodies.

## Open Questions for Later Phases

- Should nested append-only research logs also support batch-level logs when one research pass updates several aesthetics?
- Should structured research profiles embed the latest log digest or only link to logs?
- Which fields should become machine-readable YAML versus markdown headings?
- Should cultural-sensitivity review status be a required field for specific families?
- How should redirect/superseded entries participate in no-new-regressions checks?
