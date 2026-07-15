# Routing fixtures

This public package exposes exactly two skills. These fixtures document the intended
selection boundary between aesthetic understanding and application handoff.

## `aesthetic-literacy`

### Positive triggers

| # | User Request | Expected Skill |
|---|---|---|
| 1 | "What is Y2K aesthetic? Describe it formally." | aesthetic-literacy |
| 2 | "Explain vaporwave as a design system — all 7 dimensions." | aesthetic-literacy |
| 3 | "What are the non-negotiables of brutalism?" | aesthetic-literacy |
| 4 | "What's the difference between cottagecore and dark academia?" | aesthetic-literacy |
| 5 | "What fonts are canonical for the Bauhaus aesthetic?" | aesthetic-literacy |

### Negative triggers

| # | User Request | Should NOT Activate | Better Fit |
|---|---|---|---|
| 1 | "Build a design token spec for dark academia." | aesthetic-literacy | aesthetic-application |
| 2 | "My button component has insufficient contrast against the Y2K background — fix it." | aesthetic-literacy | out of scope — accessibility tooling |

## `aesthetic-application`

### Positive triggers

| # | User Request | Expected Skill |
|---|---|---|
| 1 | "Build a token spec for vaporwave." | aesthetic-application |
| 2 | "Give me CSS custom properties for dark academia." | aesthetic-application |
| 3 | "Make this landing page feel like Art Deco; give developer-ready notes." | aesthetic-application |
| 4 | "Translate Bauhaus into colors, type, shape, and spacing tokens." | aesthetic-application |
| 5 | "Write component notes for buttons, cards, inputs, and modals in Y2K style." | aesthetic-application |

### Negative triggers

| # | User Request | Should NOT Activate | Better Fit |
|---|---|---|---|
| 1 | "What does this aesthetic look like?" | aesthetic-application | aesthetic-literacy |
| 2 | "Is vaporwave different from synthwave?" | aesthetic-application | aesthetic-literacy |
| 3 | "Fix my React component architecture." | aesthetic-application | out of scope — component architecture tooling |
