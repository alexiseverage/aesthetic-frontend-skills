# Aesthetic Artifact Schema Reference

This skill-local reference gives installed users the compact production schema without requiring the root `docs/` or `knowledge/` tree. It mirrors the repository RFC at `docs/refactor-rfc-aesthetic-artifact-model.md` but is intentionally short enough to load during normal agent work.

## Three artifacts

1. Canonical aesthetic entry: `aesthetic-literacy/aesthetics/<slug>.md`
   - Production-facing design guidance used by `aesthetic-literacy` and `aesthetic-application`.
   - Safe hot-path resource for ordinary app design.
   - Should be concise, concrete, and implementation-ready.
2. Structured research profile: root `knowledge/aesthetics/<slug>.md`
   - Source-grounded synthesis, evidence links, and dimension frequency analysis.
   - Use only when the user asks for provenance, maintenance, research, or source-backed uncertainty resolution.
3. Append-only research log: root `knowledge/aesthetics/<slug>/research-log.md` or adjacent maintainer files
   - Dated observations, corrections, and evidence changes.
   - Not part of the installed-user hot path.

## Canonical entry required frontmatter

```yaml
slug: lowercase-hyphen-slug
label: Human Label
family: taxonomy family
era: historical period or contemporary
aliases: []
status: canonical
evidence_level: legacy | synthesis | researched
related: []
subsets: []
```

Redirect entries may use a smaller schema with `redirect` or `superseded_by` pointing to the canonical target.

## Canonical entry required body contract

Canonical entries should include or preserve these sections/labels:

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

## Hot-path rule

For normal app-design work, load the canonical entry first and stay there unless the user explicitly asks for research depth. Do not load root research logs for routine token generation, CSS translation, or component styling. Root research resources are maintainer/provenance resources, not the default installed-user path.
