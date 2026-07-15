# Aesthetic Application Output Contract

This contract is the installed-user handoff shape for `aesthetic-application`. It keeps token/spec output predictable when a user asks to apply a named aesthetic to a product surface.

## Inputs to resolve first

- Confirmed canonical slug from `aesthetic-literacy/references/aesthetic-index.md` or a direct `aesthetics/<slug>.md` load.
- Canonical dictionary entry loaded from `aesthetic-literacy/aesthetics/<slug>.md`.
- Connotation mode: authentic, nostalgic quotation, ironic pastiche, or contemporary revival.
- Platform and constraints: web/native/print, dark mode, reduced motion, and known accessibility requirements.

Do not load root research logs for routine app design. Use root `knowledge/aesthetics/` only for provenance, maintenance, or research requests, or when the canonical entry explicitly marks a high-risk ambiguity.

## Required output sections

1. Token Specification
   - Color roles with hex values.
   - Typography roles with family/category, weight, size, line-height, and tracking.
   - Shape, motion, spacing, and optional layout tokens.
2. Cultural Markers
   - Include 3–5 concrete signals.
   - Avoid 2–3 anti-signals.
3. Component Notes
   - Buttons, cards, inputs, navigation, hero/header, headings, dividers, links, badges/tags, modals/overlays, alerts/notifications, and icons.
4. Flags
   - WCAG contrast risks, reduced-motion risks, dark-mode gaps, aesthetic fatigue risk, and unresolved blend/user-decision conflicts.

## Quality bar

- Values must be implementable: `#C0C0C0`, `border-radius: 24px`, `cubic-bezier(...)`, not vague mood prose.
- Every dimension should map back to the canonical entry's 7-dimension profile.
- CSS and token suggestions should preserve non-negotiables before decorative variants.
- Cultural markers should explain what to include and what to avoid so the output does not collapse into a generic theme.
