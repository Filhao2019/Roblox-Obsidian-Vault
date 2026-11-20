---
title: Performance Budgets and Optimization
date: 2026-11-02
tags: [3d, performance, mobile, streaming]
status: researched
---

# Performance Budgets and Optimization

Budgets for triangles, draw calls, textures and memory, plus the Roblox settings that enforce them. Roblox gives only example numbers; the true limit is your lowest-end target device. Code-side performance lives in [[Code Performance and Optimization]]; model construction in [[Modeling for Roblox]].

## Budget cheat sheet

| Resource | Official / documented | Community guidance | Working target (mobile-first) |
|---|---|---|---|
| Triangles per mesh | 20,000 max | n/a | 500-8,000 typical |
| Triangles in view | Example: stay under 1,000,000 | About 500,000 | 300k-500k |
| Draw calls | Example: under 1,000 | About 500 scene, UI under 150 | 300-500 |
| Textures | 256 px / 5 studs, 512 / 10, 1024 / 20 | Atlas and trim sheets | Reuse, remove duplicates |
| Transparency | Use only 0 or 1 | n/a | Avoid partial (overdraw) |
| Bones per skinned mesh | none | 20+ reported laggy | under 25 |
| Frame time | 16.67 ms at 60 FPS | n/a | 33 ms at 30 FPS on low phones |

Official page example: stay below 1,000 draw calls and 1,000,000 triangles on a baseline device. Older official guidance quoted about 600 draw calls and 650,000 triangles for cluttered areas. Treat both as examples and measure.

## Settings that matter

- **RenderFidelity:** Automatic (default) = highest under 250 studs, medium 250-500, lowest beyond. Use Performance for background props.
- **CollisionFidelity:** Box for decor; Hull/Default for interactive; Precise only when needed; Tunable for balance. Collision cost scales with shape complexity and with how many parts move.
- **StreamingEnabled:** on by default for new places. Defaults: StreamingTargetRadius 1024 studs, StreamingMinRadius 64. Recommended: ModelStreamingBehavior Improved, StreamOutBehavior Opportunistic, StreamingIntegrityMode PauseOutsideLoadedArea, optional PredictiveStreamingMode. Only Workspace content streams; avoid moving assemblies with huge instance counts.
- **Instancing:** meshes sharing MeshId, TextureId, Material and Transparency batch into fewer draw calls, so reuse the same mesh asset and avoid duplicate uploads. Packages stop duplicate IDs.
- **Built-in materials** cost far less memory than custom textures.
- **LevelOfDetail SLIM** avatars keep crowded scenes populated across devices.
- **Transparency:** only 0 or 1 to avoid overdraw.
- **Streaming and teleports:** splitting a place trades join time per teleport against memory.

## Profiling workflow

1. Pick a baseline phone and test on it all project long. Studio's device emulator is inaccurate for memory.
2. Open the Scene rendering stats (Draw/triangles) in crowded areas and the Developer Console memory tab.
3. Use the MicroProfiler on mobile: the mobile client menu enables it and the web UI is viewed from a development machine on the same network. Blue frames mean the render thread is the bottleneck (object density, movement, lighting); red frames usually point to object complexity, texture size or visual effects.
4. Fix the biggest cost first: duplicate assets, over-tessellated meshes, oversized textures, particle counts.

## Habits that scale

- Build modular kits (walls, floors) with shared trim sheets, see [[Materials Textures and PBR]].
- Keep decoration meshes under 500 tris; spend on collectibles ([[Characters Pets and Creatures]]).
- Prefer event-driven scripts and disconnect unused connections (frame budget).
- Don't store everything in ReplicatedStorage (clients load all of it).
- Light with Voxel/ShadowMap for sims and reserve Future for showcase scenes ([[Lighting and Atmosphere]]).

## References

- [Design for performance](https://create.roblox.com/docs/performance-optimization/design) — official · 1,000 draw calls / 1M tris example
- [MicroProfiler](https://create.roblox.com/docs/performance-optimization/microprofiler) — official · mobile profiling
- [Studio MicroProfiler (legacy path)](https://create.roblox.com/docs/studio/microprofiler) — official · frame colors
- [Instance streaming](https://create.roblox.com/docs/workspace/streaming) — official · streaming behavior
- [Content streaming recommendations](https://create.roblox.com/docs/optimization/content-streaming) — official · radius defaults
- [Meshes](https://create.roblox.com/docs/parts/meshes) — official · render/collision fidelity
- [MeshPart reference](https://robloxapi.github.io/ref/class/MeshPart.html) — API mirror · MeshPart properties
- [RenderFidelity enum](https://create.roblox.com/docs/reference/engine/enums/RenderFidelity.md) — official · enum values
- [TriangleMeshPart reference](https://create.roblox.com/docs/reference/engine/classes/TriangleMeshPart.md) — official · collision fidelity property
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications) — official · 20k per mesh
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official · size guidance
- [Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art) — official tutorial · Chapter 5 optimize
- [Real world building and scripting optimization](https://devforum.roblox.com/t/3127146) — DevForum · 500k tris / 500 draw call mobile budget
- [Does Roblox use mesh instancing?](https://devforum.roblox.com/t/does-roblox-use-mesh-instancing/399564) — DevForum · instancing rules
- [Rendering updates, Sept 2017](https://devforum.roblox.com/t/rendering-updates-september-2017/54148) — DevForum · clustering and instancing (dated)
- [Does face-count matter?](https://devforum.roblox.com/t/does-face-count-matter/633111) — DevForum · triangle cost discussion
- [How could I optimize this?](https://devforum.roblox.com/t/how-could-i-optimize-this/1325227) — DevForum · RenderFidelity tips
- [How to use MicroProfiler for mobile testing](https://www.creation.dev/learn/how-to-use-microprofiler-service-roblox-mobile-testing) — third-party guide · verify vs official
- [Skinned meshes with 20+ bones lag](https://devforum.roblox.com/t/how-to-achieve-skinned-mesh-deformation-without-bones/4753104) — DevForum · bone count report

Links: [[3D Assets MOC]] · [[00 Home]]
