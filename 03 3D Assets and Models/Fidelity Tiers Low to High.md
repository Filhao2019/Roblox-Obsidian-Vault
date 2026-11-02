---
title: Fidelity Tiers Low to High
date: 2026-11-02
tags: [3d, fidelity, art-style, performance]
status: researched
---

# Fidelity Tiers Low to High

Roblox games span five practical fidelity tiers, from Part-built blockouts to near-realistic PBR scenes. The top chart is dominated by tiers 1-3 (cheap, readable, mobile-safe); tiers 4-5 appear mostly in horror and shooters where mood and realism sell the experience. Triangle counts below are working rules of thumb (the only hard official number is **20,000 triangles per individual mesh**, see [[Modeling for Roblox]]); texture sizes follow Roblox's own guidance of roughly 256 px per 5 studs, 512 px per 10 studs and 1024 px per 20 studs. Pick a tier per object, not per game: see [[When to Use Which Fidelity]].

## Tier summary

| Tier | Look | Typical tris / object | Textures | Material approach | Top-game examples |
|---|---|---|---|---|---|
| 1. Blocky / Part-built | Bricks, wedges, cylinders, CSG unions, studs | 12 per Part (cube); unions a few hundred | None or built-in Material enums | `Part.Material` + Color, SmoothPlastic/Plastic/Grass | [[Grow a Garden]] (studded plots), [[Brookhaven RP]], [[Murder Mystery 2]], [[Blox Fruits]] islands (partly) |
| 2. Low-poly flat-shaded | Faceted meshes, solid colors, vertex color | 100-2,000 (props), 2k-5k (hero) | None, or one tiny 64-256 px palette | Vertex colors or a palette strip, Plastic/SmoothPlastic | [[Steal a Brainrot]] (voxel-ish characters, unverified detail), [[Throw Food For Animals]], [[Break and Steal an Egg]] (unverified) |
| 3. Stylized mid-poly, hand-painted | Soft shapes, gradients, painted albedo | 1,500-8,000 (pets/characters), 500-3,000 (props) | 256-1024 px albedo, trim sheets, atlases | Albedo-only MeshPart TextureID, toon shading via lighting | [[Adopt Me]], [[Pet Simulator 99]], [[Steal An Egg]], [[Dress To Impress]] (UGC items), [[Fisch]], [[Dandys World]] |
| 4. PBR SurfaceAppearance | Normal/rough/metal maps, trims | 3,000-15,000 per mesh (under the 20k cap) | 512-1024 px per map, shared trim sheets | SurfaceAppearance, MaterialVariant on Parts | [[Rivals]] maps, [[Violence District]], [[Forsaken]], [[Doors]] hero rooms |
| 5. High-detail realistic | Photoscan-like props, volumetric lighting | up to 20,000 per mesh, many pieces; scenes of 500k-1M tris | up to 1024-2048 px, multiple maps | Full PBR + Future lighting + post FX | [[99 Nights in the Forest]] (unverified), top horror showcases, [[Doors]] later floors |

Game-to-tier mapping above is observation-based and marked unverified where no developer source exists; verify by inserting the game's models in Studio or via screenshots.

## Tier 1: Blocky / Part-built

- **What it is:** Everything is Parts (Block, Wedge, Cylinder, Ball) and CSG unions. A cube costs 12 triangles, so a whole base can be hundreds of Parts without hitting mesh limits.
- **When to use:** Greybox/blockout, plots and buildings in [[Grow a Garden]]-style tycoons, quick prototypes, roleplay towns. Wikipedia describes Grow a Garden's aesthetic as using studded textures that evoke old-school Roblox games, which is a deliberate nostalgia-plus-cheap-performance choice.
- **Texture/material:** Built-in materials use far less memory than custom textures (Roblox's own performance guidance), so Tier 1 is the safest on low-end phones.
- **Real examples to study:**
  - Roblox's greybox chapter of the Environmental Art curriculum (blockout first, polish later).
  - Roblox solid modeling docs for Union/Negate workflows.
  - Kenney Mini Dungeon / Mini Forest style kits (blocky but meshed) as shape references.
  - DevForum "low poly build" threads for community conventions.
- **Pros / cons:** Zero import friction, cheap collision. Cons: limited organic shapes, unions can be heavy if over-detailed.

## Tier 2: Low-poly flat-shaded

- **What it is:** Faceted meshes with solid color faces. Common in free packs; trivially cheap and instantly readable.
- **Numbers:** Quaternius-style props are typically a few hundred to a couple thousand triangles; characters 1,000-5,000. A scene of 100 such props is ~100k-300k tris.
- **Texture:** Often just one 64-256 px palette or vertex colors (Blender "Vertex painting" is recommended by Roblox's Blender guide for lightweight color).
- **Where in a game:** Background props, set dressing, enemy fodder, UI-world icons.
- **Real examples:**
  - Quaternius Ultimate Platformer Pack (CC0, 100+ models; FBX/OBJ/glTF/Blend).
  - Quaternius pack catalog (83 packs including Ultimate Nature, Ultimate Crops, Cute Animated Monsters).
  - Kenney Nature Kit and Fantasy Town Kit (CC0, via OpenGameArt listings).
  - Poly Pizza (CC0 and CC-BY low-poly, flat shaded; their uploader rules reject high poly).
  - Synty POLYGON packs (low-poly stylized; paid seat licenses; check engine/license fit before Roblox use).

## Tier 3: Stylized mid-poly with hand-painted or gradient textures

- **What it is:** The dominant "premium Roblox" look: rounded forms, readable silhouette, painted gradient albedo, bold colors. It is what makes pets and collectibles feel desirable on a phone.
- **Numbers (rule of thumb):** Pets/brainrots 1.5k-8k tris, props 500-3k, hero characters up to ~10k. Textures 256-1024 px albedo; no normal map needed. Roblox suggests 256 px for a 5x5 stud object, 512 px for 10x10, 1024 px for 20x20.
- **Style anchors:** Uplift's art direction for [[Adopt Me]] treats pets as the main style setters, using bright family-friendly colors and distinct silhouettes (brand interview), and its job posting requires assets to perform on PC, mobile and console. [[Pet Simulator 99]] pushes saturated, candy-bright themes per world (promotional source, treat cautiously).
- **Real examples:**
  - Kenney Nature Kit / Fantasy Town Kit (single texture atlases, updated for a single texture map).
  - Quaternius Cute Animated Monsters Pack and Ultimate Animated Animal Pack (rigged low-poly creatures to study silhouettes).
  - Fan Italian Brainrot packs on itch.io / Sketchfab (rigged, baked textures) for brainrot proportions only; they are fan art of memes, check licenses.
  - Roblox Laser Tag template and Environmental Art Curriculum for trim-sheet UVs.
  - BuiltByBit Stylized Grass and Flowers pack and Low-Poly FPS Lobby listings (marketplace examples of tier 3 environment kits).

## Tier 4: PBR SurfaceAppearance

- **What it is:** Meshes carrying SurfaceAppearance with ColorMap, NormalMap, RoughnessMap, MetalnessMap and optional EmissiveMask. Roblox supports the metalness workflow only and OpenGL tangent-space normals.
- **Numbers:** 3k-15k tris per mesh, 512-1024 px per map; a trim sheet can serve hundreds of meshes. Keep total draw calls under the baseline budget (Roblox example: under 1,000 draw calls and 1,000,000 triangles on the target device).
- **Where:** Map walls/floors in shooters ([[Rivals]]-style arenas), horror corridors ([[Violence District]], [[Forsaken]]), hero props.
- **Real examples:**
  - Poly Haven CC0 models and textures (Barrel, Marble Bust, Chandelier, Mid Century Lounge Chair listed).
  - ambientCG CC0 PBR surfaces.
  - Roblox "PBR textures" and material reference pages (roughness/metalness values for common materials).
  - BlenderKit royalty-free/CC0 models (check per-asset license).
  - Synty POLYGON Dungeon Pack (770 assets with 4 colorways) as a stylized-PBR-friendly modular set.

## Tier 5: High-detail realistic

- **What it is:** Dense, photoreal or AAA-influenced. Needs Future lighting, post-processing, careful LOD and streaming.
- **Numbers:** Meshes up to 20k tris; scenes often 500k-1M triangles on PC with aggressive streaming. Reviewers praise Roblox games such as Frontlines and The Mimic for looking "not like Roblox," showing that the ceiling is high.
- **Costs:** Highest memory risk on phones; Roblox warns low-end mobile devices have tight memory limits and can crash.
- **Real examples:**
  - Poly Haven photoscan-style models.
  - Sketchfab scanned/CC-BY models (check license, convert to <20k tris).
  - Fab marketplace listings (Epic's license is engine-targeted; check Roblox suitability).
  - ArtStation environmental art breakdowns as reference for lighting and detail passes.

## Mixing tiers

Most hits combine tiers: a Tier 1 base, Tier 3 collectibles, and a few Tier 4 hero objects. See [[Art Styles of Top Games]] and [[Performance Budgets and Optimization]].

## References

- [Meshes (RenderFidelity, CollisionFidelity)](https://create.roblox.com/docs/parts/meshes) — official docs · LOD thresholds 250/500 studs
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications) — official docs · 20,000 triangle per-mesh limit
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official docs · size guidance by object size
- [PBR textures / SurfaceAppearance](https://create.roblox.com/docs/art/modeling/surface-appearance) — official docs · map types and limits
- [Material reference](https://create.roblox.com/docs/art/modeling/material-reference) — official docs · PBR roughness/metalness values
- [Design for performance](https://create.roblox.com/docs/performance-optimization/design) — official docs · draw call/triangle example budget
- [Blender to Roblox workflow](https://create.roblox.com/docs/art/blender) — official docs · vertex painting, trim sheets, Laser Tag template
- [Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art) — official tutorial · greybox to optimize
- [Solid modeling](https://create.roblox.com/docs/parts/solid-modeling) — official docs · Union/Negate for Part-built models
- [Grow a Garden (Wikipedia)](https://en.wikipedia.org/wiki/Grow_a_Garden) — encyclopedia · studded-texture aesthetic
- [Steal a Brainrot (Wikipedia)](https://en.wikipedia.org/wiki/Steal_a_Brainrot) — encyclopedia · voxel characters
- [Adopt Me art direction Q&A](https://brandsuntapped.com/?p=8177) — interview · pets as style setters, silhouettes
- [Pet Simulator 99 wiki](https://roblox.fandom.com/wiki/BIG_Games_Pets/Pet_Simulator_99) — fan wiki · game overview
- [Doors (Wikipedia)](https://en.wikipedia.org/wiki/Doors_(game)) — encyclopedia · Victorian-style hotel
- [List of Roblox games (Wikipedia, via 99 Nights/Dandy's entries)](https://en.wikipedia.org/wiki/99_Nights_in_the_Forest) — encyclopedia · Frontlines/The Mimic "not like Roblox" praise
- [Quaternius Ultimate Platformer Pack](https://quaternius.itch.io/ultimate-platformer-pack) — CC0 pack · 100+ low-poly models
- [Quaternius home](https://quaternius.com) — CC0 pack library · 83 packs
- [Kenney Nature Kit](https://opengameart.org/content/nature-kit) — CC0 pack listing · 330+ nature objects
- [Kenney Fantasy Town Kit](https://opengameart.org/content/fantasy-town-kit) — CC0 pack listing · modular town
- [Kenney assets index](https://kenney.nl/assets) — CC0 library · Mini Dungeon, Mini Forest, City Kits
- [Poly Pizza upload guidelines](https://poly.pizza/docs/uploading) — site docs · CC0/CC-BY, low-poly rules
- [Synty POLYGON Dungeon Pack](https://syntystore.com/products/polygon-dungeon-pack) — paid pack · 770 assets, seat license
- [Poly Haven models](https://polyhaven.com/models) — CC0 models · realistic props
- [Poly Haven license](https://polyhaven.com/license) — license page · CC0
- [ambientCG](https://ambientcg.com/) — CC0 PBR textures
- [BlenderKit licenses](https://www.blendkit.com/docs/licenses/) — license page · Royalty Free vs CC0
- [Italian brainrot meme characters 2](https://sketchfab.com/3d-models/italian-brainrot-meme-characters-2-cac813a642194a6ba2a191e6ffdb7ec7) — Sketchfab model · check license on page
- [Stylized Grass and Flowers Asset Pack](https://builtbybit.com/resources/stylized-grass-and-flowers-asset-pack.106964/) — marketplace · stylized foliage
- [Low-Poly FPS Lobby](https://builtbybit.com/resources/low-poly-fps-lobby.94206/) — marketplace · low-poly arena lobby
- [Intro to Modeling in Blender with Roblox livestream](https://www.blendernation.com/2024/08/01/intro-to-modeling-in-blender-with-roblox-aug-6-livestream-by-roblox-team/) — livestream notice · Roblox-run Blender intro

Links: [[3D Assets MOC]] · [[00 Home]]
