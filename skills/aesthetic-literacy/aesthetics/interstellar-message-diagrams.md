---
slug: interstellar-message-diagrams
label: "Interstellar Message Diagrams"
family: technical-institutional
era: "1960s experimental pictograms, 1970s spaceflight artifacts, and later radio and simulated messages"
aliases: ["Interstellar pictograms", "Extraterrestrial message graphics"]
status: canonical
evidence_level: standard
related: ["engraved-celestial-atlas", "8-bit-pixel", "ufo-sighting-bulletins"]
subsets: []
---

# Interstellar Message Diagrams

## Scope

Diagrams made to carry or explain a message intended for a recipient who may share no human language. The artifacts range from engraved plaques and playback instructions to on/off bitmaps, numerical primers and simulated reception exercises. Keep physical carrier, encoded states and proposed interpretation visibly distinct. [Research profile](../../../knowledge/aesthetics/interstellar-message-diagrams.md)

## 7-Dimension Profile

**Palette**: Use the contrast between marks and substrate. Warm metal and black engraving suit plaques. Two clearly separated states suit binary messages. An analytical color key can identify sections in a rendering.

**Type**: Use repeated dots, ticks, designed raster glyphs and compact numbers inside the message. Set explanatory labels in a distinct human-readable sans or mono face.

**Texture**: Represent the physical carrier with fine shallow engraving or a subdued metal grain. Use discrete, sharp raster cells for a decoded bit pattern.

**Shape**: Compose with calibrated rings, signal curves, repeated tick lengths, cell matrices and discrete corner markers. Repeat geometry to establish a visual convention.

**Motion**: A plate and a decoded frame can stay still. Frame sizing, bit stepping and toggling interpretive overlays are useful inspection controls. Keep the underlying sequence stable.

**Spatial**: Use generous separation between unrelated diagrams or visibly order a primer from reference examples toward more complex groupings. Give the encoded figure and its legend distinct regions.

**Cultural markers**: Identify the author, project, medium and publication or transmission status. Shape and number may support a proposed reading. Treat receiver knowledge and interpretation as open questions.

## Non-Negotiables

**Non-negotiables**:

- A visible relation between an encoded mark system and its proposed reading.
- Consistent geometry or calibration that teaches the visual convention.
- A clear distinction between original marks and the human-facing interpretation layer.

## Connotation

**Connotation**: Technical interpretation through the perspective of the mission, author or simulator. Retain the speculative character of a message with an unknown reader.

## Related / Subsets

Engraved Celestial Atlas organizes known terrestrial observations into plates. An interstellar message establishes its own units and conventions. 8-bit Pixel shares sharp cells, while UFO Sighting Bulletins organize reported events through editorial metadata.

## Frontend / UI Guidance

Build a signal reader with two legal frame widths for one bitstream. Keep the count stable while the chosen raster changes. Use a separate legend and let readers toggle highlight color. Include a plain-language diagram description and a visible selected state.

## CSS Translation

Use frame `#101a24`, active bit `#f5e574`, empty cell `#263540` and optional annotation `#80d4e2`. Square corners and 1px registration rules keep the bit field crisp. Keep cells discrete at narrow widths and allow raw data to wrap.

## Typography / Fonts

Use a compact tabular mono face for row width, bit count and data. A readable sans-serif supports interpretation and control language. Leave the bitmap glyphs as drawn data.

## Cultural / Ethical Notes

Credit the primary carrier or publication. Label a proposed or simulated broadcast. Describe interpretations as the designers’ suggestions where documented. Keep any staged decoding interface clearly fictional.

## Anti-Patterns

- Generic science-fiction display effects that obscure the marks.
- Adding extra encoded channels to a two-state reproduction.
- Legend text or color embedded in the bit field as though transmitted.
