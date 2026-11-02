---
title: VFX Textures and Flipbooks
date: 2026-11-02
tags: [vfx, research]
status: researched
---

# VFX Textures and Flipbooks

Choose the texture and animation to support one readable event. The guidance below was checked against official documentation on 2026-11-02; the exercises have not been built or measured in Studio.

## Static texture versus flipbook

A particle texture is a 2D image. Flipbooks divide a texture into frames. The current API documents 2×2, 4×4, 8×8 and custom layouts. `FlipbookMode` chooses loop, one-shot, ping-pong or random playback; one-shot timing follows particle lifetime rather than `FlipbookFramerate`. `FlipbookStartRandom` can vary the starting frame. `FlipbookIncompatible` helps diagnose an invalid texture/layout pairing. [ParticleEmitter API](https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter).

| Visual need | Proposed starting point | What to inspect |
|---|---|---|
| Brief impact silhouette | One static texture | Readability during one short burst |
| Smoke shape that evolves | One-shot flipbook | First/last frame and lifetime alignment |
| Repeating flame | Loop with variation | Visible repetition across many particles |
| Ambient twinkles | Random playback or randomized start | Whether noise overwhelms the scene |

These are original selection suggestions, not universal production settings.

## Embedded references

![[particle-emitters-Color-Examples.jpg|800]]

Official particle color example, reused from [[Particles and Beams Visual Study]]. Compare silhouette and contrast before adding animation. This is a documentation example, not game footage.

![[particle-emitters-Texture-Examples.mp4]]

Official texture demonstration. Pause and compare the visible shape at several ages. Both files: Roblox Corporation and creator-docs contributors, CC BY 4.0, unchanged; pinned original media links and hashes are in [[Media Attribution and Reuse]] and the visual-study note.

## Blending and illumination

`LightEmission` changes normal/additive blending; it does not illuminate nearby geometry. `LightInfluence` controls response to environmental light. Use an actual light source if nearby surfaces need illumination. [ParticleEmitter API](https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter).

## Original authoring and review exercise

Create a small grayscale smoke sheet with transparent edges and consistent frame dimensions. Keep a source file, export, license and revision together. Build one emitter with the effect disabled by default, then compare single bursts against a dark wall and a bright wall. Inspect frame boundaries, cropping, abrupt disappearance and overlapping transparent layers.

Record the selected texture, layout, mode, lifetime and tested device in [[Evidence Record]]. Compare a static version with the animated version before increasing texture size. Test repeated triggers, low graphics settings and nearby UI text. There is no measured texture budget or phone-performance result in this note.

For a worked official example, Roblox's volcano tutorial layers multiple emitters and uses flipbooks for animated ash/smoke. Study the division of visual jobs rather than copying the entire volcano into every effect. [Create volcanic eruptions](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes).

## Mentioned in

- [[VFX Fundamentals]]
- [[VFX Implementation in Luau]]
- [[VFX Packs and Marketplaces]]


## References

- [ParticleEmitter](https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter) — official API · flipbooks, blending and diagnostic properties.
- [Create volcanic eruptions with VFX](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) — official tutorial · layered effect study.
- [[Particles and Beams Visual Study]] — media captions and original source links.
- [[Media Attribution and Reuse]] — media licensing and integrity record.

Links: [[VFX MOC]] · [[00 Home]]
