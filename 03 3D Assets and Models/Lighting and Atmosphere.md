---
title: Lighting and Atmosphere
date: 2026-11-02
tags: [3d, lighting, atmosphere, post-processing]
status: researched
---

# Lighting and Atmosphere

Lighting is the cheapest way to change a game's fidelity tier: the same meshes read as cozy sim or dread-filled horror depending on technology, Atmosphere, Sky and post effects. This note covers the engine options and how top games use them. Pair with [[Materials Textures and PBR]] and [[Performance Budgets and Optimization]].

## Lighting technology

| Setting | What it does | When to use |
|---|---|---|
| Voxel | 4x4x4 voxel light map, soft and cheap | Mobile-heavy sims and tycoons |
| ShadowMap | Crisp sun/directional shadows | Balanced; shooters and adventure |
| Future | Most advanced: per-pixel point/spot light, realistic shadows | Horror, showcase, PC/console-first |
| Compatibility | Deprecated; Roblox suggests Voxel plus a Retro ColorGrading preset | Avoid |

Newer settings: `Lighting.Technology` is being superseded by LightingStyle (artistic intent) and PrioritizeLightingQuality (quality vs view distance), per the enum docs.

## Atmosphere and sky

- **Atmosphere** properties: Color, Decay, Density, Glare, Haze, Offset. Haze and Glare must be above 0 to show. When Lighting has an Atmosphere, legacy Fog properties are hidden. Use dense Haze for horror depth; tint Decay toward the mood color.
- **Sky** objects set skybox, sun/moon; time of day via `Lighting.ClockTime`.
- Fog hides pop-in from streaming ([[Environment and Map Design]]).

## Post-processing (per official list)

BloomEffect (glow), BlurEffect, ColorCorrectionEffect (brightness/contrast/saturation/tint), DepthOfFieldEffect (best on opaque surfaces), SunRaysEffect, ColorGradingEffect (`TonemapperPreset` Default vs Retro). Effects under Lighting apply to everyone; under Camera only to that player. Editor Quality Level must be raised in Studio to see some effects.

## How top games light

- **Bright saturated sims** ([[Grow a Garden]], [[Adopt Me]], [[Pet Simulator 99]], [[Steal An Egg]]): high Brightness, strong sun, mild Bloom on rare items, saturation boost; mostly cheap lighting so phones cope (observation, unverified).
- **Dark horror** ([[Doors]], [[Violence District]], [[Forsaken]], [[99 Nights in the Forest]]): low ambient, warm point lights as the only guide, fog/haze and dark ColorCorrection. Reviews describe Doors's subdued ominous palette and dim lighting as central to tension. Future lighting is the likely choice for dynamic lamps (unverified).
- **Arena shooters** ([[Rivals]]): neutral even lighting for readable sightlines (games.gg).
- **Seasonal swaps:** Halloween themes (the chart snapshot is Halloween week) are made with ColorCorrection tint, fog color and sky replacement, see [[Live Ops and Update Cadence]].
- **Nostalgia:** Doors's Retro Mode and Roblox's Retro tonemapper preset mimic pre-2019 looks.

## Recipes (starting points, tweak by eye)

1. Cozy sim: Voxel or ShadowMap, ClockTime 14, Brightness 3, Atmosphere Density 0.2 Haze 0, ColorCorrection Saturation +0.15, Bloom Intensity 0.2.
2. Horror: Future, Ambient near black, Atmosphere Density 0.4 Haze 2 Color dark gray, ColorCorrection Contrast +0.1 Brightness -0.05, no Bloom except emissives.
3. Arena: ShadowMap, neutral Sky, light SunRays off, no DoF (DoF hurts competitive clarity).

## References

- [Technology enum](https://create.roblox.com/docs/reference/engine/enums/Technology.md) — official · Voxel/ShadowMap/Future, LightingStyle
- [Technology enum (alternate path)](https://create.roblox.com/docs/reference/engine/enums/Technology) — official · same
- [Atmosphere class](https://create.roblox.com/docs/reference/engine/classes/Atmosphere) — official · property list
- [Post-processing effects](https://create.roblox.com/docs/en-us/environment/post-processing-effects) — official · effect list
- [Guide to Lighting](https://devforum.roblox.com/t/guide-to-lighting/2764787) — DevForum · community guide
- [Improve Lighting (step by step)](https://devforum.roblox.com/t/improve-lighting-step-by-step/1387033) — DevForum · tutorial
- [Background blur in LNX Concert](https://devforum.roblox.com/t/how-do-you-get-a-backround-blur/879209) — DevForum · DepthOfField/Bloom discussion
- [Roblox lighting and atmosphere guide](https://gamertagmythras.com/blog/roblox/roblox-lighting-atmosphere-guide) — blog · settings walk-through
- [Lighting plugins](https://www.creation.dev/tools/lighting-plugins) — third-party list · post-FX panels
- [Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art) — official tutorial
- [Doors (Wikipedia)](https://en.wikipedia.org/wiki/Doors_(game)) — encyclopedia · hotel setting
- [Doors horror coverage (PCGamesN)](https://www.pcgamesn.com/roblox/doors-horror-game) — news · atmosphere reception
- [Doors on Know Your Meme](https://knowyourmeme.com/memes/subcultures/roblox-doors) — community · tone
- [Rivals guide hub](https://games.gg/rivals/guides/) — guide site · map readability
- [Best Roblox horror games](https://hone.gg/blog/roblox-horror-games/) — list · horror references


## Visual study

- [[Environment and Materials Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[3D Assets MOC]] · [[00 Home]]
