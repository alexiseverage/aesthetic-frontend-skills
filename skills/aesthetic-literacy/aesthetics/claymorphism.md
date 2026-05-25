---
slug: claymorphism
label: Claymorphism
family: emerging-hybrid
era: 2022–present
aliases: ["clay UI", "puffy design", "soft 3D"]
---

**Palette**: Pastel-forward, soft, and approachable. Base surfaces use warm off-whites (`#F5F0EB`, `#FAF8F5`, `#FFF9F0`) or cool grey-whites (`#F0F4F8`, `#ECEFF1`). Accent colours are desaturated and gentle — soft lavender (`#C9B8F9`), muted coral (`#F0A8A0`), powder blue (`#A8D8EA`), sage green (`#B5CDA3`), warm peach (`#F5D0B0`). Colours never hit full saturation — the aesthetic is soft everywhere, including chroma. The palette avoids pure white (`#FFFFFF`) and pure black (`#000000`) — even backgrounds carry a hint of warmth or coolness. CSS custom properties: `--clay-bg: #F5F0EB; --clay-surface: #FFF9F0; --clay-accent: #C9B8F9; --clay-text: #5A4E4A`.

**Type**: Soft, rounded sans-serifs with friendly proportions. Google Fonts: `'Nunito'` (the canonical claymorphism font — rounded terminals, friendly x-height), `'Quicksand'` (geometric, rounded), `'Baloo 2'` (playful, slightly inflated), `'Fredoka'` (soft, approachable). Weight range: 400–600 for body text (heavier than neumorphism's thin weights — claymorphism wants readability over ethereality). Generous letter-spacing (`0.5px–1px`) and line-height (`1.5–1.6`). Typography should feel puffy and approachable, not sharp or architectural. CSS: `font-family: 'Nunito', 'Quicksand', sans-serif; font-weight: 500; letter-spacing: 0.5px; color: var(--clay-text)`.

**Texture**: Soft, puffy, clay-like 3D surfaces — the defining texture. Achieved through a TRIPLE `box-shadow` strategy: one outer shadow (the cast shadow), one dark inner shadow (depth on bottom/right), one light inner shadow (highlight on top/left). Unlike neumorphism (which requires the element background to match the page background), claymorphism's inner shadows are self-contained — they work on ANY background colour. The surface is opaque, smooth, and matte — like modelling clay or Play-Doh, not glossy plastic. No gradients, no transparency, no images. CSS:
```css
.clay-card {
  background: var(--clay-surface);
  border-radius: 32px;
  box-shadow:
    8px 8px 16px 0 rgba(0,0,0,0.15),           /* outer: cast shadow */
    inset -8px -8px 12px 0 rgba(0,0,0,0.1),    /* inner: dark depth */
    inset 8px 8px 12px 0 rgba(255,255,255,0.6); /* inner: light highlight */
}
.clay-card:active {
  box-shadow:
    2px 2px 4px 0 rgba(0,0,0,0.1),
    inset -8px -8px 12px 0 rgba(0,0,0,0.15),
    inset 8px 8px 12px 0 rgba(255,255,255,0.4); /* deeper press = stronger inset */
}
```
The triple-shadow is the non-negotiable CSS fingerprint. Community npm packages (`claymorphism-css`, `clay.css`) provide ready-made presets.

**Shape**: Generously rounded, puffy, inflated forms. `border-radius: 20–50px` — significantly larger than Material Design's 4dp or neumorphism's 10–15px. Cards, buttons, and inputs look like they were inflated with air, then gently pressed down. Circles and pill shapes are common. Input fields use inset shadows to create a scooped-out, debossed look. Shape language communicates softness, safety, and approachability — nothing is sharp, nothing is hard-edged. CSS: `border-radius: 32px` on cards, `border-radius: 50px` on buttons, `border-radius: 16px` inset on inputs.

**Motion**: Bouncy, playful, soft. Hover states gently lift (`transform: translateY(-2px)` with eased transition). Button presses squish inward (`:active` state deepens the inset shadows for a pressing-into-clay feel). Checkbox toggles slide with a soft spring (`cubic-bezier(0.34, 1.56, 0.64, 1)` for overshoot bounce). Transitions are 300–400ms with generous easing — nothing snaps. CSS: `transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)` for bouncy interactions; `transition: box-shadow 0.2s ease` for press states. The motion vocabulary is: everything responds like it's made of something soft and slightly elastic.

**Spatial**: Generous, airy, with soft depth. Elements sit on pages with ample padding (24–32px per card) — claymorphism needs breathing room to read the shadow shapes. Unlike Material Design's z-axis elevation system (floating cards at distinct heights), claymorphism creates a gentle, organic relief — elements are slightly puffed up from the page rather than floating above it. The spatial philosophy is: everything is made of the same soft material, just at slightly different depths. White space is generous but warm — `background-color: var(--clay-bg)` ensures empty space carries colour, not cold emptiness.

**Cultural markers**: Coined by Michał Malewicz (the same designer who coined neumorphism in 2019) in early 2022 as the practical successor to neumorphism's failed promise. Spread through Dribbble and CSS-Tricks (2022–2023). Adopted by SaaS landing pages targeting creative tools, children's apps, wellness platforms, and design-tool marketing. The aesthetic embodies the late-2020s turn toward softness, accessibility, and warmth — a deliberate contrast to the hard-edged neubrutalism that dominated 2021–2023. The npm package `claymorphism-css` and Figma community templates established it as a named, documented aesthetic with its own tooling ecosystem.

**The neumorphism-to-claymorphism evolution**: Neumorphism (2019) had one fatal flaw — its extrusion illusion depended on element background matching page background. A neumorphic card on a white section and a grey section looked like two different cards. Claymorphism solves this by using INNER shadows for the 3D effect, not the background-relative shadows that neumorphism relied on. A claymorphic card looks the same on any background. This is the critical technical difference that made claymorphism a separate aesthetic, not just a neumorphism 2.0. It is genuinely a different technique producing a different visual result, deployed to solve a specific constraint.

**Non-negotiables**: triple box-shadow (outer + dark inset + light inset) + border-radius ≥ 20px + opaque matte surface (no transparency, no blur, no gradients) + background-independent rendering (works on any background colour) + soft pastel-forward palette

## Connotation

**Contemporary revival** — claymorphism is a born-digital 2022 aesthetic with no historical precedent; it synthesizes softness as an explicit reaction to neubrutalism's hardness and neumorphism's failure. It is genuinely new, not a revival. **Nostalgic quotation** — subtle: the Play-Doh/clay material metaphor evokes childhood craft materials, lending implicit warmth-nostalgia without referencing any specific era. **Ironic pastiche** — used knowingly in toy/gaming brands and children's products where the "puffy clay" look is deliberately playful; less ironic than self-aware. **Authentic** — not applicable; claymorphism has no original historical period. It is a native digital aesthetic invented whole in the 2020s.

## Scope

**Suitable for**: creative-tool marketing sites, children's apps and edtech platforms, wellness/meditation apps, SaaS onboarding flows (the softness reduces intimidation), design portfolios, lifestyle blogs — any interface where approachability and warmth are higher priorities than information density. Excellent for reducing cognitive friction in signup flows and first-time user experiences. **NOT suitable for**: data-heavy dashboards (inner shadows compete with data visualization), financial platforms, healthcare records, enterprise admin panels, accessibility-first interfaces where high contrast is required (the soft palette inherently reduces contrast ratios), or any context where the playful/puffy look undermines authority. The aesthetic trades precision and density for warmth — don't use it where precision matters more.

**Subsets / Related**: *Neumorphism* (existing entry) — the direct predecessor; shares the soft-3D philosophy but differs in mechanism (neumorphism = background-dependent dual-shadow; claymorphism = background-independent triple-shadow). Neumorphism is historically significant; claymorphism is its practical production-ready successor. *Glassmorphism* (existing entry) — the alternative 2020s soft-UI approach; glassmorphism uses `backdrop-filter: blur()` and transparency; claymorphism uses opaque surfaces with inner shadows. Different mechanism, different visual effect, different use cases. *Neubrutalism* (existing entry) — the stylistic opposite; neubrutalism is hard-edged, high-contrast, deliberately rough; claymorphism is soft, low-contrast, deliberately gentle. The two represent the 2020s oscillation between aggression and softness. *Material Design* (existing entry) — shares card-based layout and rounded corners but differs in shadow model (single dp-based vs triple inner/outer) and spatial philosophy (floating planes vs puffed-up surfaces).

**CSS translation notes**: The triple-shadow is the defining technique — outer shadow at `rgba(0,0,0,0.15–0.25)` for cast depth, dark inset at `rgba(0,0,0,0.1–0.15)` for bottom/right depth, light inset at `rgba(255,255,255,0.4–0.6)` for top/left highlight. Press states reverse the relationship: dark inset deepens, outer shrinks. Google Fonts: Nunito, Quicksand, Baloo 2, Fredoka. CSS `cubic-bezier(0.34, 1.56, 0.64, 1)` for the bouncy-soft feel. No `backdrop-filter`, no `linear-gradient`, no `opacity < 1` on surfaces. The aesthetic is CSS-only — no images, no SVG filters, no JavaScript required.
