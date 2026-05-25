---
slug: flat-design
label: Flat Design
family: digital-internet-native
era: 2010–2019 (peak Windows Phone 7, 2010; iOS 7, 2013)
aliases: ["flat UI", "metro-inspired", "Flat 2.0"]
---

**Palette**: Pure, uncompromised color — crisp white backgrounds (#FFFFFF), flat black text (#000000), iOS system blue (#007AFF), Metro's bold accent tiles (cyan, orange, magenta, lime green). No gradients, no texture. Each color is used at full saturation and opacity — the color is the surface, not a treatment on the surface. Flat 2.0 (2015+) reintroduces subtle tonal variation but never gradient-for-depth.

**Type**: Geometric sans-serifs optimized for screen readability — Segoe UI (Microsoft Metro), Helvetica Neue UltraLight (iOS 7), Roboto (Android Holo). Thin weights (300, UltraLight) convey lightness and modernity; generous tracking for spaciousness. Typography IS chrome in flat design — without shadows and bevels, type weight, size, and spacing become the primary hierarchy tools.

**Texture**: None. This is the defining negative space of flat design — the rejection of texture, grain, shadow, and material simulation. Flat 2.0 reintroduced subtle elevation (1–2px `box-shadow` on cards, thin `border-bottom` on active states) but only as a usability compromise, not an aesthetic return. CSS: `background: #FFF; box-shadow: none; text-shadow: none; border-radius: 0–4px`.

**Shape**: Hard edges or minimal rounding (0–4px border-radius). Buttons are flat rectangles with color-differentiation as the sole affordance signal. Icons are outlined, thin-stroke, monochrome glyphs. iOS 7's icon grid: rounded squares with 0px internal border-radius. Metro's live tiles: hard-edged rectangles that serve as both icon and content surface.

**Motion**: Purposeful, physics-grounded motion as information architecture. iOS 7's parallax wallpaper, app-launch zoom, and swipe-back gesture create spatial relationships between screens. Metro's live tiles animate content transitions in-place. Animation communicates "where you are" in the app hierarchy, not decorative flair. CSS: `transition: all 0.3s ease` for state changes; `transform: translateX()` for off-canvas navigation.

**Spatial**: Flat, layered planes with no simulated depth. Content stacks vertically; parallax scrolling creates the illusion of z-space without shadow. Full-bleed photography with overlaid semi-transparent text. The spatial philosophy: information architecture through position and motion, not material depth and shadow. White space is generous — content breathing room, not emptiness.

**Cultural markers**: Microsoft Metro / Windows Phone 7 (2010) — the originator; Apple iOS 7 (2013) — the canonizer; Google Holo (2011) and Material Design (2014) — the successors. The "flat vs skeuomorphic" war of 2013 was the defining design debate of the decade. NN/g's usability research (22% slower task completion on pure flat UIs) drove the Flat 2.0 compromise.

**Non-negotiables**: no gradients + no texture + geometric sans-serif typography + color-as-surface (not color-as-treatment) + outlined iconography

**Historical note**: Flat 2.0 (2015+) — the usability compromise. Subtle shadows returned to differentiate interactive elements from static ones, but only as functional affordances (1–2px `box-shadow`), never as material simulation. The "flat design era" is 2010–2015 pure flat + 2015–2019 Flat 2.0; by 2020 the aesthetic was absorbed into design system defaults and ceased to be a named movement.

**Precursor**: *Swiss International Style* (existing entry) — the print-design methodology that established the grid, Helvetica, and content-first hierarchy that flat design inherited. But Swiss was a PRINT system (posters, brochures, signage); flat design is a UI system (touch targets, screen readability, interaction states). The NN/g usability problems (is this a button or text?) are problems Swiss never faced. Separate entries with bidirectional linking.

**Subsets / Related**: *Metro (Microsoft)* — the originating variant: live tiles, Segoe UI, typography-as-chrome, all-caps navigation, bold accent tiles. *iOS 7 Flat* — Apple's variant: UltraLight Helvetica Neue, translucent overlays, parallax, pastel accent colors. *Holo (Android)* — transitional: neon-blue accents, hard edges, dark backgrounds; replaced by Material Design in 2014. *Long Shadow* — a 2013–2014 micro-trend within flat design: 45-degree shadows extending ~2.5x object size from icons; CSS via `text-shadow` or pseudo-element tricks. Too narrow for its own entry; documented here as a Flat Design variant.

## Google Fonts

Segoe UI (system), Roboto, Open Sans, Lato — clean geometric sans-serifs with generous x-height for screen readability. Thin weights (300) for iOS 7 lightness; regular (400) for body; medium/bold (500–700) for hierarchy. Avoid serifs, slabs, or humanist faces.

## Connotation

**Contemporary revival** (Flat 2.0). Flat design proper is a historical period-piece of 2010–2015, but Flat 2.0's usability compromises have been absorbed into modern design system defaults. Today, "flat" is less a named aesthetic and more the baseline assumption — buttons are flat rectangles with color differentiation; shadows are functional affordances, not style statements.

## Scope

Excellent for dashboards, admin panels, SaaS tools, documentation sites, and content-heavy applications where readability and clarity are paramount. Flat design's minimalism reduces cognitive load on task-focused interfaces. Poor for luxury branding, entertainment, emotional storytelling, or any context where aesthetic distinctiveness is the primary goal — flat design is intentionally generic, which is both its strength (universal usability) and limitation (lack of personality). Use as a system-level aesthetic rather than a brand-differentiator.
