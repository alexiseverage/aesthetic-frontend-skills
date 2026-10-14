---
slug: plakatstil
label: Plakatstil
family: historical-design-movements
era: Early twentieth-century German poster design, with later commercial continuations
aliases: ["German Poster Style", "Sachplakat", "Object Poster"]
status: canonical
evidence_level: standard
related: ["art-nouveau", "bauhaus", "polish-poster-school", "wartime-propaganda", "wpa-poster-style"]
subsets: []
---

# Plakatstil

Early modern German poster design in which a recognizable advertising subject and emphatic lettering become a few dominant graphic forms. Lucian Bernhard, Ludwig Hohlwein, and Hans Rudi Erdt supply distinct object-led and figurative branches.

## Scope

Use this aesthetic for product, retailer, venue, and event communication with a strong focal image and a deliberate name/message hierarchy. Preserve graphic simplification and advertising recognition before applying print texture.

The narrower **Sachplakat**, or object-poster, branch favors one enlarged product and its name. Wider Plakatstil may show people, several objects, a service scene, or a landscape. These names share one catalog owner; asking for Sachplakat should select the stricter object-led branch rather than generate another catalog identity.

The research profile inspected 30 unique works across MoMA, MK&G Hamburg, LACMA, and the Smithsonian. It supports varied lettering and selective tonal modeling, not a universal sans-only or perfectly flat rule. [Neue Galerie](https://www.neuegalerie.org/exhibitions/modern-poster-germany) provides historical framing; [Smithsonian's Bernhard study](https://www.americanhistory.si.edu/explore/stories/emergence-modernism-early-20th-century-american-advertising-lucian-bernhard-and-his) explains the object and figurative branches.

## 7-Dimension Profile

**Palette**: A limited set of dominant color roles with clear figure/ground contrast. Black, cream, red, orange, blue, green, and ochre recur in different combinations. Deep grounds with pale subjects and pale fields with dark subjects both belong. These are observed color families, not measured historical pigment values or an obligatory primary-color palette.

**Type**: Large, authored display lettering organized around the subject or sales message. Broad serif capitals, heavy sans lettering, script, italic, and blackletter occur in the corpus. The constant is hierarchy and compositional integration; subordinate details stay smaller and readable. Exact historical font identities are not established by this profile.

**Texture**: Printed color planes, drawn contours, and occasional subordinate material modeling. Lithographic surfaces can support quiet grain, but scan wear and old paper stains are not necessary design intent. Shaded cloth and product highlights are valid variants. Keep digital chrome, glossy app surfaces, and gratuitous distress subordinate to the graphic composition.

**Shape**: Recognizable silhouettes, enlarged products, cropped figures, bold overlaps, diagonal presentation, and a few large planes. Service or figurative branches can retain clothing patterns and small details. Shape simplification does not require an abstract Bauhaus geometry vocabulary.

**Motion**: The historical evidence is still print; animation timing and easing are unknown. Intentional stillness is an appropriate digital translation. Optional product changes or short reveals are proposed interface behavior, with immediate state changes under reduced motion. Do not describe animation as a historical signature.

**Spatial**: Give the advertising hook and principal lettering most of the attention. The object branch can use one dominant product plus a short name; broader branches may use an image zone, a compact copy block, or an anchored lower title. Portrait and landscape formats both occur. Dense support copy is a variant, not permission to lose the main hierarchy.

**Cultural markers**: German-speaking early modern advertising, lithographic printers, consumer goods, retailers, entertainment, and public street posters. Political uses and later American Bernhard advertising are documented branches. Historical brand names, costume, or propaganda slogans are contextual evidence rather than required interface motifs.

## Non-Negotiables

**Non-negotiables**:

- A recognizable advertising subject used as the primary graphic hook.
- Emphatic subject-and-lettering hierarchy rather than neutral interface chrome.
- Simplified large forms and a limited set of dominant color roles.

For the Sachplakat branch, add the stricter constraint of one product and a short dominant name.

## Connotation

**Mode:** contemporary revival.

The style reads as direct, confident, commercial, and graphic. A revival can make a product memorable without copying a historical advertisement. Preserve the poster's communication economy; a distressed background behind an ordinary shop grid will read as general vintage branding instead.

## Related / Subsets

- `art-nouveau`: a same-period neighbor. Floral subjects can overlap, but Plakatstil prioritizes the advertising hierarchy over continuous organic ornament structuring the entire surface.
- `bauhaus`: shares reduction, but product recognition and expressive display lettering differ from workshop-derived geometric construction.
- `polish-poster-school`: shares authored poster imagery; its metaphorical cultural-poster vocabulary differs from Plakatstil's commonly direct commercial recognition.
- `wartime-propaganda`: a documented subject application, not a synonym for the whole style.
- `wpa-poster-style`: shares economical printed color but carries a different American public-program lineage.

**Sachplakat / object poster** is a scoped subset name within this entry, without a separate canonical slug. Figurative, event, retailer, and landscape advertising are broader variants. Choose the branch explicitly when briefing an interface.

## Frontend / UI Guidance

Build product launches, small catalogs, venue announcements, or exhibition introductions around a dominant original illustration and a short display name. Give price, specifications, model selection, and inquiry actions a clear subordinate zone with real semantic controls.

For an interactive object-poster catalog, let model selection replace the dominant illustration and relevant details. Keep the poster silhouette stable and expose the selected state through a border, label, or marker as well as color. On mobile, stack the name, object, and controls while retaining their hierarchy.

## CSS Translation

An example contemporary palette is `--field: #E15B2D`, `--paper: #F0E7CC`, `--ink: #171A16`, and `--secondary: #384A83`. These are proposed implementation values, not sampled historical pigments. Ink/field contrast is approximately 4.80:1; ink/paper approximately 14.22:1. Use paper-backed support copy where softer secondary colors are needed, and verify the actual rendered pairs.

Use a flat field, one large SVG/image zone, oversized display text, and low-radius controls. Quiet grain may sit beneath illustration areas; keep it away from critical text. Allow subject overlap or slight diagonal orientation without clipping semantic controls. Avoid decorative card shadows as the main structure.

Prefer immediate selected-state updates. If a brief reveal is added, mark its duration as a proposed UI token and provide an immediate `prefers-reduced-motion` fallback. No historical animation duration is established.

## Typography / Fonts

Choose the display category for the branch: broad serif or painted block lettering works for an object catalog; compact sans can support service advertising; script or blackletter needs specific reference justification. A system serif such as Georgia or a strong system sans is a practical contemporary fallback, not a claim about the source font.

Reserve expressive treatment for the name and key message. Use readable body type for prices, specifications, buttons, and input labels. Include license, coverage, fallback, and loading cost when adding a font; do not convert all useful text into an image.

## Cultural / Ethical Notes

Keep the named movement, practitioners, and commercial printing context distinct from generic retro advertising. Poster collections include several styles, so collection membership alone is not sufficient classification evidence.

Some historical examples carry political propaganda, stereotypes, or proprietary brands. Contemporary revival should use newly authored content and original assets. [LACMA's provenance account](https://unframed.lacma.org/2024/05/09/julius-paul-poster-collection) also documents dispossession and restitution of a poster collection; historical sourcing deserves more than decorative nostalgia.

## Anti-Patterns

- Treating any flat product advertisement as Plakatstil without the poster hierarchy and historical boundary.
- Requiring one sans font, completely flat interior shading, or zero decorative detail across every variant.
- Replacing the recognizable subject with generic primary-color geometric modules; this drifts toward Bauhaus.
- Using scan damage, fake aging, historical logos, or propaganda copy as the main identity.
- Filling the focal poster area with equally weighted cards, lengthy copy, or inaccessible image-only controls.
