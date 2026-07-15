# Append-only Research Log Entry Template

This template documents the proposed append-only research log format. It is not a current strict validator target.

## Entry

```yaml
logged_at: "YYYY-MM-DD"
researcher: "agent-or-human-id"
source_url: "https://example.invalid/source-or-image"
source_id: "optional local corpus identifier"
evidence_type: "image | text | video | primary-source | secondary-source | field-note | correction"
affected_dimensions: ["palette", "type", "texture", "shape", "motion", "spatial", "cultural-markers", "connotation", "boundaries"]
confidence: "low | medium | high"
supersedes: "optional earlier log entry id"
```

## Observation

Describe the specific evidence observed. Keep it concrete: what is visible, stated, measured, or sourced? Do not turn one observation into broad canonical guidance without corroboration.

## Dimension Impact

Explain which dimension(s) this evidence affects and whether the evidence looks canonical, common, variant, or merely adjacent.

## Canonical Entry Impact

State one of:

- No canonical change recommended yet.
- Update the structured research profile only.
- Candidate change for the canonical aesthetic entry after review.
- Correction that supersedes an earlier claim.

## Follow-up

List missing evidence, review needs, cultural-sensitivity concerns, broken links, or comparisons with neighboring aesthetics.

## Append-only Rules

- Add new entries after existing entries.
- Do not delete earlier entries to hide uncertainty or disagreement.
- Correct mistakes by adding a new entry with `evidence_type: correction` and a `supersedes` reference.
- Preserve source URLs or source identifiers unless they contain secrets or private user data.
- Keep raw personal data out of logs; summarize sensitive sources without copying private content.
