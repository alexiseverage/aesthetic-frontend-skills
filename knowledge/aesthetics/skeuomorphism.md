---
slug: skeuomorphism
label: Skeuomorphism
first_researched: "2026-07-15"
last_updated: "2026-11-12"
source: "2026-11-12 direct media audit; 33 qualifying unique artifacts; see audit below"
image_count: 33
evidence_level: standard
new_aesthetic: false
aliases: ["realistic UI", "material mimicry"]
---

# Skeuomorphism

> Origin: A design strategy that preserves ornamental cues from older physical objects to make new tools feel familiar, especially in software interfaces that imitate paper, leather, switches, or desk objects. Provenance is strong at the conceptual level, and digital-interface translation is one of the clearest modern applications of the concept.

## Source / Evidence Links

- https://en.wikipedia.org/wiki/Skeuomorph
- https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
- https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

## Dimension Synthesis

| Dimension | Canonical (≥70%) | Common (30–70%) | Variant / Avoid |
|---|---|---|---|
| Palette | material-derived colors: leather browns, paper creams, metallic silvers, felt greens, wood tones | glass highlights, stitched neutrals, realistic app-specific palettes | flat anti-material minimalism with no object reference |
| Type | labels that mimic product categories: notebook headers, dial numerals, switch captions | engraved or embossed effects, serif or humanist pairings tied to material mood | generic flat system type with no object cueing |
| Texture | leather grain, paper fibers, chrome, felt, stitched seams, beveled controls | shadows, embossing, glossy buttons, drop shadows, lined paper | texture-free surfaces where only the name remains |
| Shape | knobs, switches, tabs, notebooks, shelves, reels, calculators, page curls | segmented toggles, card stacks, deck-like containers | abstract invisible controls with no physical analogy |
| Motion | flips, presses, toggles, page turns, reel spins, inertia-inspired feedback | slot-machine, knob-turn, shutter-like transitions | hyper-minimal motion detached from physical metaphor |
| Spatial | object-on-desk framing, layered panels, physically suggestive depth, clear foreground controls | shelves, stacks, analog tool arrangements | same-surface ambiguity that erases tactile metaphors |
| Cultural markers | early smartphone/desktop app realism, “familiarity through imitation,” leather-and-wood software excess, tactile metaphors for new media | notebook apps, bookshelf UIs, analog-tool simulacra | any 3D UI regardless of material reference |

## Image Descriptions

No dedicated image corpus was collected during this pass. The profile is grounded in the core conceptual source and accessibility references instead:

1. [https://en.wikipedia.org/wiki/Skeuomorph] — strongest source in this pass; defines skeuomorphs as derivative objects retaining ornamental cues from earlier necessary structures, and explicitly notes their role in making new systems feel familiar and easier to use.
2. [https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html] — accessibility baseline for readable labels and controls when material textures compete with text.
3. [https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion] — baseline for keeping physically metaphorical motion supportive rather than excessive.

## Analysis

The key evidence here is conceptual and directly transferable to UI work. Wikipedia’s skeuomorph definition explains why the style matters: new tools borrow cues from older objects so users can infer function through familiarity. In software, that has historically produced leather notebooks, page curls, dials, calculator buttons, wood shelves, and glassy controls that imitate real-world tools.

Representative interface patterns are notebook apps, bookshelf metaphors, analog control panels, dial-driven widgets, and photoreal utility apps. The style is strongest when the borrowed material cue genuinely helps the user infer interaction or domain — for example, a page-like note surface or a mixer-like audio control — rather than when realism becomes gratuitous decoration.

Accessibility constraints are mixed. Real-world metaphors can clarify affordances, but heavy texture, low-contrast embossing, and decorative chrome can also obscure text and clutter the interface. Motion should reinforce the object metaphor without becoming theatrical, and texture should never carry the only contrast distinction between states.

Anti-patterns for implementation: photorealism for its own sake, faux materials that lower readability, mixing too many object metaphors in one surface, and treating skeuomorphism as synonymous with “3D.” The cited source supports a functional familiarity principle first, with ornament as a byproduct rather than the whole point.

## Connections

- `flat-design` — Flat Design rejects the material mimicry Skeuomorphism depends on.
- `neumorphism` — soft-UI descendant that keeps tactile depth cues while stripping away most explicit material realism.
- `frutiger-aero` — can share glossy/skewed physicality, but Frutiger Aero is atmospheric and eco-futurist rather than object-imitation driven.

## Research Updates

- 2026-07-15 — Initial limited research profile created from the conceptual source and accessibility references.


## Direct media audit — 2026-11-12

This audit supersedes earlier generic dimension claims and limited source counts; earlier notes are retained as research history.
This audit inspected 34 complete still interfaces and three functioning browser applications. Thirty-three unique works qualify: 16 archival interfaces, 14 current publisher-supplied instrument/effect interfaces, and three contemporary browser works. Four plain/chrome-dominated examples are excluded as weak boundary comparisons. Alternate views, GUI crops, theme variants and repeated software-version captures were not counted separately. Multiple controls or instruments in one screenshot do not inflate the count.

The discovery pool covered the GUIdebook application categories and 17 publisher product routes, followed by full-image or press-kit inspection. Seven D16 GUI/perspective images were temporarily retained from its [official press resources](https://d16.pl/press), which explicitly offer high-resolution interface graphics. Other originals were streamed for linked study. Source screenshots and copyrighted software designs are references, not application assets. Current publisher screenshots are not assigned historical release dates. The GUIdebook index names several captures as reproductions; those are documented design representations rather than claimed original screen recordings. Small complete originals remain useful for the full control map; fine material claims are reserved for larger images.

The corpus is biased toward desktop utilities and audio tools, with seven products each from two contemporary publishers. It does not independently establish the prevalence of iOS leather/bookcase applications or universal usability benefits. [Apple's original iPad announcement](https://www.apple.com/newsroom/2010/01/27Apple-Launches-iPad/) provides period context for touch, books and content applications, not visual evidence for every later skin. [The calculator author's account](https://web.dev/articles/designcember-calculator) identifies the modern working solar-calculator study. A working recreation is kept distinct from historical software.

### Synthesis and confidence

- **Palette — high for material range:** SK01–SK11, SK14, SK18–SK20 and SK21–SK34 show gray, silver, cream, wood, dark enamel, red and even vivid green. Brown leather is one possible referent, not a compulsory palette.
- **Type — high for task labels, moderate for broader traditions:** the calculator key groups, printed dial numerals, narrow instrument labels and segmented readouts in SK03–SK11 and SK21–SK37 map typography to physical use. Readability matters more than faux embossing. This sample offers little evidence about long-form paper reading.
- **Texture — high:** SK02–SK03, SK08–SK11, SK16 and SK21–SK34 triangulate brushed metal, wood ends, textured faceplates, inset screens and directional contact shadows. More texture is not automatically more useful: SK12, SK13, SK15 and SK17 show why generic chrome is weak evidence by itself.
- **Shape — high:** analog faces, telephone/calculator key maps, binder rings, toggles, knobs, transport keys and fader slots have recognizable source objects. SK04 demonstrates that even low-resolution flat pixel art can carry an explicit object metaphor.
- **Spatial — high:** SK02, SK14, SK16 and SK21–SK34 organize a whole device or functional panel. iTunes SK10 combines physical transport controls with an ordinary digital list. Skeuomorphism does not require every data region to imitate a cabinet or shelf.
- **Motion — moderate for inspected contemporary tasks; low historically:** SK35 faders change state, SK36 computes a result, and SK37 opens a language wheel while a clock updates. Static instrument screenshots establish no rotary response or meter damping timings. Press displacement and dial interpolation are implementation choices; pause and reduced-motion behavior must preserve the task.
- **Cultural markers — moderate:** physical desktop tools and audio instruments are grounded in source-specific familiarity, rather than a universal assumption that everyone has used the referent. No claim is made that simulated material guarantees intuitiveness or that the strategy ended with flat smartphone interfaces.

Collection stopped after the working target was exceeded and repeated instruments confirmed the same rules: coherent light direction, readable task grouping, and material cues tied to an action. A wider mobile/book corpus could refine that branch but is not needed to justify the selected instrument application. The studio concentration limits prevalence claims.


### Full-media observations

**SK01 — Calculator in IRIX 5.3 (Calculator)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/calculator/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/calculator/irix53-1-1.png). Accessed 2026-11-12; 204 × 271. Directly observed: IRIX calculator uses an inset dark display, yellow pill function keys and a distinct white numeric block. Physical calculator grouping and shallow bevels are legible at its complete 203 × 270 original size; the source identifies this as a reproduced screenshot. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK02 — Calculator in IRIX 5.3 (IVcalc)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/calculator/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/calculator/irix53-2-1.png). Accessed 2026-11-12; 316 × 390. Directly observed: IVcalc renders a whole orange calculator in exaggerated perspective against black. Tilted key grid, raised blue arithmetic keys and a sloped gray display imitate an object rather than ordinary window chrome. This is a separate IRIX application, not another crop of the previous calculator. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK03 — Calculator in Mac OS X Panther (Calculator)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/calculator/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/calculator/macosx103-1-1.png). Accessed 2026-11-12; 256 × 308. Directly observed: Panther calculator has a brushed silver case, inset pale yellow LCD, rounded gradient keys and dark drop shadow. Equal key spacing preserves a physical keypad map; one enlarged zero and tall equals express different affordances. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK04 — Clock in Workbench 1.0 (Clock 1.9)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/clock/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/clock/amigaos10-1-1.png). Accessed 2026-11-12; 170 × 180. Directly observed: Workbench clock depicts a white analog face, black hour markers and hands within a saturated blue rectangular window. Flat low-resolution pixels still perform object imitation; photographic texture is not required for the metaphor. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK05 — Clock in BeOS R5.0.1 PE (Clock)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/clock/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/clock/beos5.png). Accessed 2026-11-12; 93 × 112. Directly observed: BeOS clock has a compact yellow title bar over a deeply beveled silver square frame. Tiny red numerals and thin hands sit on a white dial. Raised frame and recessed face make the time instrument read as a contained object. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK06 — Clock in IRIX 5.3 (clock)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/clock/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/clock/irix53-2-1.png). Accessed 2026-11-12; 114 × 114. Directly observed: IRIX clock puts a plain dark analog dial inside thin beveled window chrome. White ticks and overlapping light hands carry the object metaphor with almost no decorative material. Source labels capture a reproduction. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK07 — Clock in OS/2 Warp 4 (System Clock)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/clock/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/clock/os2warp4.png). Accessed 2026-11-12; 213 × 240. Directly observed: OS/2 clock combines bright green embossed circular rim with red raised tick blocks and beveled hands. The lurid customization is an important counterexample to a mandatory brown/leather palette; analog face still drives the metaphor. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK08 — CD player in IRIX 5.3 (CDman)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/cdplayer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/cdplayer/irix53.png). Accessed 2026-11-12; 795 × 280. Directly observed: CDman uses cyan digital readouts on black, large recessed displays and deeply raised transport buttons in gray hardware-like clusters. Tall stop key and illuminated green play triangle identify state through form and color; still image gives no transport timing. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK09 — CD player in System 7.5.3**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/cdplayer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/cdplayer/macos753-1-1.png). Accessed 2026-11-12; 369 × 132. Directly observed: Apple CD player in System 7.5.3 resembles a compact dark stereo faceplate: magenta segmented elapsed-time display, metallic rectangular transport keys, and a vertical volume fader. Raised highlights consistently imply light from above. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK10 — CD player in Mac OS X Panther (iTunes 4)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/cdplayer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/cdplayer/macosx103-1-1.png). Accessed 2026-11-12; 797 × 524. Directly observed: iTunes 4 combines brushed metal outer case and round transport keys with a conventional striped data table. The small pale green LCD-like status display and hardware controls are skeuomorphic; the entire data list need not imitate a physical cabinet. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK11 — CD player in OS/2 Warp 4**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/cdplayer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/cdplayer/os2warp4.png). Accessed 2026-11-12; 318 × 132. Directly observed: OS/2 CD player has a pale striated marble panel, embossed track-number strip and a row of raised metallic transport symbols. Material simulation is vivid while organization remains a narrow functional toolbar. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK12 — Notepad in Workbench 1.0 (Amiga Notepad 1.5)** — boundary comparison, excluded from count

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/notepad/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/notepad/amigaos10.png). Accessed 2026-11-12; 300 × 200. Directly observed: Amiga Notepad is a plain white text area inside blue pixel window chrome. The notepad name alone does not establish a physical paper metaphor; exclude this as a boundary comparison. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK13 — Calendar in Mac OS X Panther (iCal)** — boundary comparison, excluded from count

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/calendar/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/calendar/macosx103-1-1.png). Accessed 2026-11-12; 798 × 524. Directly observed: iCal combines a brushed metal case, shallow tactile buttons and an ordinary white weekly schedule grid. The window material is simulated, but the main planner has little object-specific construction; retain as a weak boundary comparison, excluded from the main count. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK14 — Calendar in EPOC R5/Psion Series 7 (Agenda)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/calendar/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/calendar/epocr5s7-1-1.png). Accessed 2026-11-12; 640 × 480. Directly observed: Psion Agenda explicitly draws an open ring-bound planner: central silver binder rings, white facing pages, ochre edge and folded lower corners. Blue date strips and a side toolbar adapt the physical book rather than reproducing every mechanical constraint. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK15 — Address book in Mac OS X Panther (Address Book)** — boundary comparison, excluded from count

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/addressbook/); [inspected media](https://guidebookgallery.org/pics/gui/applications/office/addressbook/macosx103-1-1.png). Accessed 2026-11-12; 602 × 314. Directly observed: Panther Address Book shows a metallic browser shell around three ordinary list/content columns. A contact icon alone is weak evidence of a physical address-book metaphor; excluded from the main count as a chrome-only boundary. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK16 — Media player in Mac OS X Panther (QuickTime Player)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/mediaplayer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/mediaplayer/macosx103.png). Accessed 2026-11-12; 425 × 423. Directly observed: QuickTime has a curved brushed metal control shelf beneath the screen, circular transport buttons, recessed pale timeline and small physical volume slider. The product reads as a compact playback device rather than a generic content card. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK17 — Media player in Windows 98 SE (Media Player 6.01)** — boundary comparison, excluded from count

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/mediaplayer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/mediaplayer/win98se.png). Accessed 2026-11-12; 294 × 429. Directly observed: Windows Media Player 6.01 has ordinary gray application chrome, lightly embossed disabled transport symbols and a black screen. The video medium and toolbars alone offer weak object-material specificity; excluded as a boundary comparison. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK18 — Sound in OS/2 Warp 4**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/sound/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/sound/os2warp4.png). Accessed 2026-11-12; 498 × 320. Directly observed: OS/2 sound editor uses a striking white striated stone texture around a dense black waveform screen. Metallic transport symbols and hardware-style timing readouts coexist with genuinely digital waveform editing. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK19 — Sound in Windows 95 (Sound Recorder)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/sound/); [inspected media](https://guidebookgallery.org/pics/gui/applications/multimedia/sound/win95.png). Accessed 2026-11-12; 276 × 151. Directly observed: Windows Sound Recorder uses a narrow inset black oscilloscope-like display and five physical tape transport keys. Gray bevels mark depressible controls; position and length labels stay outside the display as instrument readouts. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK20 — Phone dialer in Windows 95 (Phone Dialer)**

Software/interface creator as named in title; capture indexed by Marcin Wichary / GUIdebook; reproduced captures noted in observation. [Provenance](https://guidebookgallery.org/screenshots/phonedialer/); [inspected media](https://guidebookgallery.org/pics/gui/applications/networking/phonedialer/win95.png). Accessed 2026-11-12; 297 × 317. Directly observed: Phone Dialer reproduces the spatial keypad and letter groupings of a telephone, within a conventional gray window. Large raised digits and a tall speed-dial area establish a familiar object/task mapping without wood or leather. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK21 — diva**

u-he. [Provenance](https://u-he.com/products/diva/); [inspected media](https://u-he.com/products/diva/assets/images/uhe-diva-screenshot-fullui-1150x642.jpg). Accessed 2026-11-12; 1150 × 642. Directly observed: Diva renders four large synthesizer modules in black pebbled material over a deep red faceplate with warm wood ends. Silver-centered scalloped knobs, recessed switches and tiny pilot lamps establish a coherent overhead light; dense labels remain functional and sharply organized. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK22 — repro**

u-he. [Provenance](https://u-he.com/products/repro/); [inspected media](https://u-he.com/products/repro/assets/images/uhe-repro-screenshot-fullui-repro-1.jpg). Accessed 2026-11-12; 825 × 500. Directly observed: Repro-1 combines a dark textured panel, warm wood side cheeks, beveled toggle switches, rotary knobs with engraved scales, small red lamps and an inset red preset display. Rigid module boundaries organize dense controls. Keyboard-like lower sequencer is abstract rather than an exact piano. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK23 — ace**

u-he. [Provenance](https://u-he.com/products/ace/); [inspected media](https://u-he.com/products/ace/assets/images/uhe-ace-screenshot-fullui-1150x654.jpg). Accessed 2026-11-12; 1150 × 654. Directly observed: ACE has a gray metal panel, walnut sides and exposed flexible patch cables. Off-white rotary knobs have dark shadowed bases, vertical slider slots are recessed and socket rings imply insertion. Digital amber labels and a central oscilloscope coexist with the hardware metaphor. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK24 — bazille**

u-he. [Provenance](https://u-he.com/products/bazille/); [inspected media](https://u-he.com/products/bazille/assets/images/uhe-bazille-screenshot-fullui.jpg). Accessed 2026-11-12; 825 × 487. Directly observed: Bazille renders a wood-ended modular faceplate with dark rotary knobs, vertical sliders, tiny circular sockets and thin colored patch cables crossing labeled blocks. A central green oscilloscope supports the instrument metaphor; cable clutter is a functional tradeoff, not a requirement for every skeuomorphic UI. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK25 — presswerk**

u-he. [Provenance](https://u-he.com/products/presswerk/); [inspected media](https://u-he.com/products/presswerk/assets/images/uhe-presswerk-screenshot-fullui.jpg). Accessed 2026-11-12; 825 × 567. Directly observed: Presswerk uses a large inset analog dual-needle meter, ribbed black knobs and small rectangular lamps on a charcoal metal case. Screw heads and wood cheeks reinforce assembly; red lettering is reserved for selected areas and readouts. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK26 — satin**

u-he. [Provenance](https://u-he.com/products/satin/); [inspected media](https://u-he.com/products/satin/assets/images/uhe-satin-screenshot-fullui-1150x850.jpg). Accessed 2026-11-12; 1150 × 850. Directly observed: Satin uses a warm ivory brushed panel, two oversized silver-centered knobs and long recessed stereo meters, framed by wood sides. Small cool blue lamps and dark service compartments balance warm physical materials. The tape-machine metaphor is expressed through controls rather than literal spinning reels. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK27 — colourcopy**

u-he. [Provenance](https://u-he.com/products/colourcopy/); [inspected media](https://u-he.com/products/colourcopy/assets/images/uhe-colourcopy-screenshot-fullui-1150x455.jpg). Accessed 2026-11-12; 1150 × 455. Directly observed: Colour Copy uses a flat dark panel with wood sides, scalloped silver knobs and a vivid inset green LCD. Raised square hold/freeze switches and small lamps model tactile controls while the display explains digital delay relationships; no literal tape reels are necessary. Static source establishes no response timing. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK28 — Decimort2**

D16 Group. [Provenance](https://d16.pl/decimort2); [inspected media](https://d16.pl/pub/press/Decimort2-PressKit.zip). Accessed 2026-11-12; 2360 × 761. Directly observed: Brushed silver faceplate, dark inset module and walnut ends form a simulated rack device. One oversized radially brushed frequency knob dominates; smaller ridged controls and colored lamps preserve a clear functional scale hierarchy. Cyan segmented displays sit below the surface. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK29 — Phoscyon2**

D16 Group. [Provenance](https://d16.pl/phoscyon2); [inspected media](https://d16.pl/pub/press/Phoscyon2-PressKit.zip). Accessed 2026-11-12; 3966 × 2948. Directly observed: Dark gray physical sequencer panel uses deeply inset olive displays, ridged round knobs, colored pilot lights and raised rectangular keyboard pads. Hard module seams organize the full interface. A contrasting row of red/yellow keys identifies edit actions. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK30 — Nepheton2**

D16 Group. [Provenance](https://d16.pl/nepheton2); [inspected media](https://d16.pl/pub/press/Nepheton2-PressKit.zip). Accessed 2026-11-12; 2580 × 1941. Directly observed: Black hardware panel organizes instrument channels through repeating red, orange and ivory knob rows. Recessed LCD-like sequencer grid contrasts with raised cream pattern keys and glowing red status lamps. Color encodes control function across channels. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK31 — Drumazon2**

D16 Group. [Provenance](https://d16.pl/drumazon2); [inspected media](https://d16.pl/pub/press/Drumazon2-PressKit.zip). Accessed 2026-11-12; 3068 × 2058. Directly observed: Pale gray instrument shell has warm charcoal modules and red/brown knobs with amber pointers. Strong black/gray borders define channel groups, while raised orange start and colored edit keys establish a physical deck. Modern grid sequencing remains integrated below. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK32 — Devastor2**

D16 Group. [Provenance](https://d16.pl/devastor2); [inspected media](https://d16.pl/pub/press/Devastor2-PressKit.zip). Accessed 2026-11-12; 2360 × 761. Directly observed: Related D16 silver-and-walnut construction repeats the same material vocabulary as Decimort, but this is a distinct distortion product with three filter strips and a routing diagram. Parallel knob groups clarify repeated processing stages; consistent specular light unifies the controls. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK33 — Sigmund2**

D16 Group. [Provenance](https://d16.pl/sigmund2); [inspected media](https://d16.pl/pub/press/Sigmund2-PressKit.zip). Accessed 2026-11-12; 4000 × 3500. Directly observed: Complete perspective promotional rendering shows a rack-like black and warm-gray delay unit, amber analog VU meters and LCD-like time readouts. Four mixer faders and dense knobs map functions onto hardware zones. Large white/black canvas margins are promotional staging rather than an application background. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK34 — Lush2**

D16 Group. [Provenance](https://d16.pl/lush2); [inspected media](https://d16.pl/pub/press/Lush2-PressKit.zip). Accessed 2026-11-12; 3100 × 1891. Directly observed: Textured white synthesizer case has a slightly raised inner faceplate, deep slider slots and a full piano keyboard. Black knobs have soft contact shadows, orange/green slider markings identify parameter roles, and small red lamps identify layer state. Complete GUI or perspective view inspected at legible display size; no motion inferred. Rights/handling: Copyright retained by respective software creators and capture contributors. D16 provides official high-resolution press resources. References are private analysis; no source image is a production asset..

**SK35 — Webamp**

Webamp project; browser recreation of Winamp 2. [Provenance](https://webamp.org/); [inspected media](https://webamp.org/). Accessed 2026-11-12; 1280 × 900. Directly observed: Dark compact stereo panels have lime pixel readouts, tiny metallic transport buttons, narrow horizontal faders and a separate equalizer panel. Setting Volume Bar to 30 and Balance to 25 visibly moves their handles; input values confirm both changes. This is a modern browser recreation, not an original running Winamp binary. No historical animation cadence or sound quality was inferred. Rights/handling: Creator copyright retained. No interface assets reused..

**SK36 — Designcember Calculator**

Thomas Steiner, based on a calculator design by Sassja Ceballos. [Provenance](https://googlechrome.github.io/samples/designcember-calculator/); [inspected media](https://googlechrome.github.io/samples/designcember-calculator/). Accessed 2026-11-12; 1280 × 900. Directly observed: Large blue molded-looking case surrounds a green inset display and a dark segmented solar strip. White rounded raised keys have explicit contact shadows. Clicking 2, +, 2, = writes expression 2+2 and result 4. The responsive desktop layout stretches the case widely; sensor behavior was not tested or required. Rights/handling: Creator copyright retained. No interface assets reused..

**SK37 — Skeuomorphic Clock**

Rishabh Rai, credited in the author’s Webflow listing. [Provenance](https://clock-b4dac8.webflow.io/); [inspected media](https://clock-b4dac8.webflow.io/). Accessed 2026-11-12; 1280 × 900. Directly observed: Nested dark concentric wheels carry year, date and time as physical rotating scales, aligned under a bright radial reading strip. Opening the language button reveals a circular flag selector in a dark inset popup while the clock blurs behind. The clock updates in real time; no full wheel cycle or exact transition duration was measured. This contemporary art clock is distinct from the archival clocks. Rights/handling: Creator copyright retained. No interface assets reused..

