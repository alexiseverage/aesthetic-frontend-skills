# Routing Fixtures — Skill Trigger Test Cases

Golden task inputs for validating skill routing. Each case specifies the expected
skill to activate and (for negative/cross-skill cases) the skill that should NOT be
activated.

Run these manually or feed them into an eval harness to confirm routing accuracy.

---

## `aesthetic-literacy`

### Positive triggers (should activate aesthetic-literacy)

| # | Input | Expected skill |
|---|---|---|
| 1 | "What is Y2K aesthetic? Describe it formally." | aesthetic-literacy |
| 2 | "Explain vaporwave as a design system — all 7 dimensions." | aesthetic-literacy |
| 3 | "What are the non-negotiables of brutalism?" | aesthetic-literacy |
| 4 | "What's the difference between cottagecore and dark academia?" | aesthetic-literacy |
| 5 | "What fonts are canonical for the Bauhaus aesthetic?" | aesthetic-literacy |
| 6 | "Describe frutiger aero — palette, shape, cultural context." | aesthetic-literacy |
| 7 | "My client wants something 'retro and warm' — what aesthetics should I consider?" | aesthetic-literacy |
| 8 | "What does the synthwave aesthetic look like as a semiotic system?" | aesthetic-literacy |
| 9 | "Is neubrutalism a subset of brutalism, or a separate aesthetic?" | aesthetic-literacy |
| 10 | "What are the connotation modes for art deco today?" | aesthetic-literacy |
| 11 | "I keep seeing 'quiet luxury' used for very different things. What does it actually mean?" | aesthetic-literacy |
| 12 | "What motion characteristics define the organic-digital aesthetic?" | aesthetic-literacy |

### Negative triggers (should NOT activate aesthetic-literacy)

| # | Input | Should NOT activate | Should activate instead |
|---|---|---|---|
| 1 | "Generate a vaporwave background texture." | aesthetic-literacy | asset-creation |
| 2 | "Extract the hex colors from these vaporwave screenshots." | aesthetic-literacy | image-analysis |
| 3 | "Build a design token spec for dark academia." | aesthetic-literacy | aesthetic-application |
| 4 | "Research the solarpunk aesthetic and collect visual references." | aesthetic-literacy | aesthetic-research |
| 5 | "My button component has insufficient contrast against the Y2K background — fix it." | aesthetic-literacy | (out of scope — accessibility tooling) |

---

## `aesthetic-research`

### Positive triggers (should activate aesthetic-research)

| # | Input | Expected skill |
|---|---|---|
| 1 | "Research the solarpunk aesthetic and collect visual references." | aesthetic-research |
| 2 | "Find me 15 visual examples of the dark academia aesthetic from Dribbble and Pinterest." | aesthetic-research |
| 3 | "Build a knowledge profile for vaporwave." | aesthetic-research |
| 4 | "Gather reference images for glitch aesthetic — at least 10." | aesthetic-research |
| 5 | "What does cottagecore look like visually? Search for examples and document them." | aesthetic-research |
| 6 | "I've never seen frutiger aero before — show me what it looks like by pulling references." | aesthetic-research |
| 7 | "Get me visual inspiration for a memphis-style app UI." | aesthetic-research |
| 8 | "Search for neubrutalism web design examples and write up what you find." | aesthetic-research |
| 9 | "Update my vaporwave profile with 10 new references from Behance." | aesthetic-research |
| 10 | "I've found a new aesthetic called 'technocore' — research it and create a profile." | aesthetic-research |
| 11 | "Pull examples of swiss international style from design archives." | aesthetic-research |

### Negative triggers (should NOT activate aesthetic-research)

| # | Input | Should NOT activate | Should activate instead |
|---|---|---|---|
| 1 | "I have a vaporwave profile. Now give me the design tokens." | aesthetic-research | aesthetic-application |
| 2 | "Analyze these 8 vaporwave images I already have." | aesthetic-research | image-analysis |
| 3 | "What is the dark academia aesthetic?" | aesthetic-research | aesthetic-literacy |
| 4 | "Generate a vaporwave texture." | aesthetic-research | asset-creation |
| 5 | "The vaporwave profile already exists — give me a CSS spec from it." | aesthetic-research | aesthetic-application |

---

## `image-analysis`

### Positive triggers (should activate image-analysis)

| # | Input | Expected skill |
|---|---|---|
| 1 | "Extract the hex colors from these screenshots." | image-analysis |
| 2 | "What border-radius is used in these UI examples?" | image-analysis |
| 3 | "Analyze these images and give me implementable CSS values." | image-analysis |
| 4 | "What font weight is used in this design?" | image-analysis |
| 5 | "Get me the exact colors and spacing from these reference images." | image-analysis |
| 6 | "I've collected 12 vaporwave images — extract the palette as hex codes." | image-analysis |
| 7 | "What easing function would produce the motion I see in this animation reference?" | image-analysis |
| 8 | "Identify the typography from this screenshot — weight, size, letter-spacing." | image-analysis |
| 9 | "These glassmorphism examples — what CSS backdrop-filter values would replicate them?" | image-analysis |
| 10 | "Append an Analysis section to my dark-academia.md profile using these images." | image-analysis |
| 11 | "What are the concrete token values I can pull from this design system screenshot?" | image-analysis |

### Negative triggers (should NOT activate image-analysis)

| # | Input | Should NOT activate | Should activate instead |
|---|---|---|---|
| 1 | "Describe the vibe of this image." | image-analysis | aesthetic-literacy |
| 2 | "What aesthetic does this design belong to?" | image-analysis | aesthetic-literacy |
| 3 | "I don't have any images yet — what does vaporwave look like?" | image-analysis | aesthetic-literacy or aesthetic-research |
| 4 | "Generate a background in this style." | image-analysis | asset-creation |
| 5 | "Build a full token spec for this aesthetic." | image-analysis | aesthetic-application |

---

## `asset-creation`

### Positive triggers (should activate asset-creation)

| # | Input | Expected skill |
|---|---|---|
| 1 | "Generate a vaporwave background texture using my knowledge profile." | asset-creation |
| 2 | "Make an SVG icon for a share button in the neubrutalism aesthetic." | asset-creation |
| 3 | "Create a decorative shape for my dark academia landing page." | asset-creation |
| 4 | "Convert this SVG to a typed React component." | asset-creation |
| 5 | "Generate a Y2K-style badge graphic." | asset-creation |
| 6 | "Vectorize this PNG logo." | asset-creation |
| 7 | "I need a texture background for my synthwave site — generate one." | asset-creation |
| 8 | "Create a set of icons in the glassmorphism aesthetic." | asset-creation |
| 9 | "I don't have the API set up — give me a prompt I can paste into Midjourney." | asset-creation |
| 10 | "Turn this SVG file into a React component with fill and size props." | asset-creation |
| 11 | "Generate a motif pattern for a cottagecore landing page header." | asset-creation |

### Negative triggers (should NOT activate asset-creation)

| # | Input | Should NOT activate | Should activate instead |
|---|---|---|---|
| 1 | "Build a Button component with hover states for this aesthetic." | asset-creation | aesthetic-application |
| 2 | "Give me CSS for a card layout in this style." | asset-creation | aesthetic-application |
| 3 | "What does this aesthetic look like?" | asset-creation | aesthetic-literacy |
| 4 | "Extract the colors from these images." | asset-creation | image-analysis |
| 5 | "Build a nav component with animation in the Y2K style." | asset-creation | aesthetic-application |

---

## `aesthetic-application`

### Positive triggers (should activate aesthetic-application)

| # | Input | Expected skill |
|---|---|---|
| 1 | "Give me design tokens for the vaporwave aesthetic." | aesthetic-application |
| 2 | "Translate dark academia into CSS custom properties." | aesthetic-application |
| 3 | "Make it look like cottagecore — full spec." | aesthetic-application |
| 4 | "I need a developer handoff document for this Y2K redesign." | aesthetic-application |
| 5 | "What CSS variables do I need for a swiss international style?" | aesthetic-application |
| 6 | "Apply the glassmorphism aesthetic — give me the full token table." | aesthetic-application |
| 7 | "I want memphis-inspired component notes for my design system." | aesthetic-application |
| 8 | "Turn this neubrutalism aesthetic direction into an implementable spec." | aesthetic-application |
| 9 | "What cultural markers should I include in a brutalism design?" | aesthetic-application |
| 10 | "Generate a W3C DTCG token file for the frutiger aero aesthetic." | aesthetic-application |
| 11 | "Give me the accessibility flags for an art deco colour palette." | aesthetic-application |

### Negative triggers (should NOT activate aesthetic-application)

| # | Input | Should NOT activate | Should activate instead |
|---|---|---|---|
| 1 | "What is vaporwave?" | aesthetic-application | aesthetic-literacy |
| 2 | "Collect visual references for this aesthetic." | aesthetic-application | aesthetic-research |
| 3 | "Extract hex values from these images." | aesthetic-application | image-analysis |
| 4 | "Generate a background image in this style." | aesthetic-application | asset-creation |
| 5 | "Fix the contrast ratio on this button — it fails WCAG AA." | aesthetic-application | (out of scope — accessibility tooling) |

---

## Cross-skill disambiguation

Cases where multiple skills could plausibly activate. The correct routing depends on
reading the user's precise intent.

| # | Input | Correct skill | Why not the alternatives |
|---|---|---|---|
| 1 | "I want to build something in the vaporwave aesthetic." | aesthetic-literacy (first) | Too vague to jump straight to tokens or assets; characterize first, then ask what they need |
| 2 | "Analyze these 12 vaporwave images I collected." | image-analysis | User already has images — this is extraction, not research |
| 3 | "Give me vaporwave references and then extract the colors." | aesthetic-research → image-analysis | Two-step workflow: research first, then analysis; activate sequentially |
| 4 | "Generate a dark academia icon set." | asset-creation | Request is for visual file output (icons), not component code or tokens |
| 5 | "The profile exists — now make it dark academia." | aesthetic-application | Profile exists = no research needed; "make it" = tokens/spec |
| 6 | "What does 'retro' mean for a UI design?" | aesthetic-literacy | Disambiguation task — map vague descriptor to concrete aesthetic(s) |
| 7 | "Build a button component that feels Y2K." | aesthetic-application | Component notes are in scope for aesthetic-application; asset-creation is for static visual files |
| 8 | "I have a brutalism profile. Can you refine the palette?" | aesthetic-application | Profile exists; request is for implementable output, not new research |
| 9 | "Research solarpunk AND give me the tokens." | aesthetic-research → aesthetic-application | Must complete research before producing tokens; run sequentially |
| 10 | "Convert my SVG logo to React and apply the synthwave aesthetic to it." | asset-creation (SVG→React) + aesthetic-application (tokens) | Two separate concerns; handle SVG conversion first, then provide tokens separately |
