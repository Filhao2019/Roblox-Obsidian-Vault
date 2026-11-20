---
title: When to Use Which Fidelity
date: 2026-11-02
tags: [3d, fidelity, decision-guide]
status: researched
---

# When to Use Which Fidelity

A decision guide for picking a [[Fidelity Tiers Low to High]] tier per object. Short version: spend polygons and texture memory where the player's eye and wallet are (collectibles, hero props, the first room), spend almost nothing on everything else, and design for the phone first because most Roblox sessions run on mobile (Roblox's own docs tell developers to pick a baseline low-end device and test on it throughout development).

## Decision table

| Object role | Default tier | Why | Budget guide (rule of thumb) |
|---|---|---|---|
| Collectible pet / brainrot / fish | 3 (stylized mid-poly) | Players trade and screenshot it; silhouette must read at icon size | 1.5k-8k tris, 512-1024 px albedo |
| Rare/legendary variant | 3 + effects | Rarity via size, color, glow, particles rather than polygons | same mesh + VFX |
| Hero prop (door, boss, key item) | 3-4 | Close-up viewing, camera lingers | 3k-15k tris, PBR optional |
| Environment kit (walls, floors) | 2-4 with trim sheet | Reused hundreds of times; one texture, instanced | 100-1,500 tris/piece |
| Background props / filler | 1-2 | Never inspected | under 500 tris |
| Terrain / ground | Terrain or big Parts | Streaming-friendly | n/a |
| Far scenery | Lowest + RenderFidelity Performance | Not readable at distance | automatic LOD |
| Characters (player) | Avatar, never replace | Avatar standard; see [[Characters Pets and Creatures]] | n/a |

## Rules

1. **Hero vs background:** one per screen. If three objects all demand attention, none do.
2. **Near vs far:** Roblox's Automatic RenderFidelity drops detail at 250 and 500 studs, so heavy detail beyond that distance is wasted. Mesh textures further than that barely show.
3. **Phones first:** mobile tolerates fewer draw calls and much less memory. Roblox's example baseline is under 1,000 draw calls and 1,000,000 triangles, and community mobile advice goes lower (about 500 draw calls / 500k triangles). Use built-in materials where possible: they cost far less memory than custom textures.
4. **Collectibles need readable silhouettes:** apply a squint test (blur the model; can you still name it?). Exaggerate heads, ears, tails. [[Adopt Me]] and [[Steal a Brainrot]] both rely on chunky, instantly recognizable shapes.
5. **Horror buys fidelity with light, not polygons:** [[Doors]], [[Violence District]], [[Forsaken]] and [[99 Nights in the Forest]] lean on dark palettes, fog and point lights; spend the budget on lighting quality (Future/ShadowMap, see [[Lighting and Atmosphere]]) and a few PBR hero props.
6. **Sims and tycoons buy cheapness:** [[Grow a Garden]], [[Steal An Egg]], [[Break and Steal an Egg]] and [[Throw Food For Animals]] run huge simultaneous player counts; many parts, studded textures and simple meshes keep devices alive. See [[Steal and Collect Tycoon Formula]].
7. **Shooters buy clarity:** [[Rivals]]-style maps favor readable sightlines over detail; keep props low-poly, collision simple (Box/Hull) and avoid transparency (partial transparency causes overdraw).
8. **Consistency over fidelity:** a Tier 4 prop in a Tier 1 world looks wrong. Match shading style (flat vs painted vs PBR) inside any one scene.

## Mixing tiers safely

- Share a palette/lighting treatment: apply the same ColorCorrection and Atmosphere to unify tiers.
- Tier boundaries by role: blocky base + painted collectible + one PBR showcase.
- Use trim sheets and atlases so many pieces share one texture, and reuse meshes to keep draw calls low (Roblox's guidance on duplicate assets and Packages).
- Test on a low-end phone and MicroProfiler before polishing (see [[Performance Budgets and Optimization]]).

## Worked examples

- **Pet egg hatch scene:** egg Tier 3 hero (2-4k tris, glow emissive), pet reveal Tier 3 at close range, stage dressing Tier 1.
- **Horror corridor:** modular Tier 3-4 walls (shared trim sheet, 512 px maps), two hero props with SurfaceAppearance, everything else flat color; use Atmosphere haze to hide pop-in.
- **Tycoon plot:** Parts for ground and conveyors; low-poly meshes for decorative statues; one 8-12k tri showcase item behind a gate.

## References

- [Design for performance](https://create.roblox.com/docs/performance-optimization/design) — official · baseline device, draw calls, built-in materials
- [Meshes: RenderFidelity and CollisionFidelity](https://create.roblox.com/docs/parts/meshes) — official · LOD distances
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications) — official · 20k per-mesh limit
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official · texture size by object size
- [Instance streaming](https://create.roblox.com/docs/workspace/streaming) — official · streaming overview
- [Content streaming recommendations](https://create.roblox.com/docs/optimization/content-streaming) — official · radius defaults
- [MicroProfiler](https://create.roblox.com/docs/performance-optimization/microprofiler) — official · profiling on mobile
- [Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art) — official tutorial · greybox then polish
- [Real world building and scripting optimization](https://devforum.roblox.com/t/3127146) — DevForum · community mobile budgets
- [Does face-count matter?](https://devforum.roblox.com/t/does-face-count-matter/633111) — DevForum · triangles vs draw calls debate
- [Adopt Me merchandise interview](https://brandsuntapped.com/?p=8177) — interview · distinct silhouettes
- [Doors (Wikipedia)](https://en.wikipedia.org/wiki/Doors_(game)) — encyclopedia · horror hotel
- [Grow a Garden (Wikipedia)](https://en.wikipedia.org/wiki/Grow_a_Garden) — encyclopedia · studded cheap aesthetic
- [Roblox art style explained](https://www.vasundhara.io/blogs/roblox-art-style-explained-what-makes-roblox-so-unique) — blog · why simple styles work
- [How to choose the right art style for your Roblox game](https://dev.to/vasundhara/how-to-choose-the-right-art-style-for-your-roblox-game-1dj6) — blog · style selection

Links: [[3D Assets MOC]] · [[00 Home]]
