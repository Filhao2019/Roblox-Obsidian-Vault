---
title: Materials Textures and PBR
date: 2026-11-02
tags: [3d, materials, textures, pbr]
status: researched
---

# Materials Textures and PBR

How surfaces get their look in Roblox: built-in Materials, MaterialVariants (tileable PBR for Parts and Terrain), SurfaceAppearance (PBR for a specific UV-mapped MeshPart), plus the cheaper atlas/trim-sheet/gradient techniques that most top games use. See [[Fidelity Tiers Low to High]] for where each fits and [[Performance Budgets and Optimization]] for cost.

## Tools

| Tool | Applies to | Use |
|---|---|---|
| `Part.Material` + Color | Parts | Cheapest. Built-in materials use much less memory than custom textures |
| MaterialVariant (under MaterialService) | Parts and Terrain by name or via `BasePart.MaterialVariant` | Reusable tileable PBR; has StudsPerTile, CustomPhysicalProperties |
| SurfaceAppearance | One MeshPart | Overrides mesh texture; ColorMap, NormalMap, RoughnessMap, MetalnessMap, EmissiveMask |
| MeshPart.TextureID | MeshPart | Plain albedo (hand-painted/gradient) |
| Vertex colors | Imported meshes | Lightweight color from Blender vertex painting |

## SurfaceAppearance facts

- Five maps: Color (optional alpha), Normal (OpenGL tangent space, flat is 127/127/255), Roughness, Metalness, Emissive mask (EmissiveStrength / EmissiveTint).
- AlphaMode: Overlay (default), Transparency (cutouts; MeshPart.Transparency 0 for hard-edged foliage), TintMask, Opaque (beta).
- Color tinting has no cost: reuse one ColorMap with different tints. Roughness may need about +0.1 for consistent lighting.
- Maps are normally set in Studio rather than changed by scripts mid-game; wait for the "Successfully uploaded compressed SurfaceAppearance" output message before judging in-game results.
- Non-albedo maps for rigid accessories are capped at 256x256; full-body clothing up to 1024x1024.
- Formats: albedo/normal RGB 24-bit; roughness, metalness, emissive single-channel 8-bit grayscale.

## Texture sizing

- 256 px for 5x5 stud objects, 512 px for 10x10, 1024 px for 20x20. Default part material density: 1024 on an 8x8 stud face; terrain 512 across 8 studs.
- A single UV set; all UVs within 0:1 (overlap allowed so trim sheets work).
- Uploaded image formats: png, jpg, tga, bmp.

## Looks used by top games

- **Studded / nostalgic:** built-in materials with studs, e.g. [[Grow a Garden]] (Wikipedia describes studded textures evocative of old Roblox games); toggled in [[Doors]] Retro Mode.
- **Hand-painted / gradient:** pets in [[Adopt Me]], [[Pet Simulator 99]], [[Steal An Egg]]: soft gradient albedo, rim highlights, no normal map (observation, unverified per game). Bake gradients into a 256-512 px atlas shared by many pets.
- **Toon look from lighting:** high Brightness plus saturated ColorCorrection and low Ambient contrast; optional Bloom for gem/egg glints ([[Lighting and Atmosphere]]).
- **Trim sheets:** one 1024 px PBR sheet shared across wall/floor/trim pieces; Roblox's Laser Tag template teaches shared trim-sheet UVs.
- **Texture atlas:** pack many small props onto one sheet to save memory and enable instancing (same TextureId).
- **PBR for horror/shooters:** [[Violence District]], [[Forsaken]], [[Rivals]]-style maps use metal/roughness differences for wet floors, steel, concrete (unverified).

## Where to get textures

CC0 PBR sets from ambientCG and Poly Haven; Roblox's own material reference lists roughness/metalness values for common surfaces; see [[Free and Paid Asset Sources]].

## References

- [PBR textures / SurfaceAppearance](https://create.roblox.com/docs/art/modeling/surface-appearance) — official · maps, AlphaMode, limits
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official · sizes and formats
- [Material reference](https://create.roblox.com/docs/art/modeling/material-reference) — official · roughness/metalness values
- [Materials (Parts)](https://create.roblox.com/docs/parts/materials.md) — official · material enum docs
- [MaterialVariant class](https://create.roblox.com/docs/reference/engine/classes/MaterialVariant) — official · properties
- [Texturing PBR for characters](https://create.roblox.com/docs/en-us/art/characters/creating/texturing-pbr) — official · character PBR
- [SurfaceAppearance (legacy article)](https://developer.roblox.com/en-us/articles/surface-appearances) — legacy official · introduction
- [Blender to Roblox workflow](https://create.roblox.com/docs/art/blender) — official · vertex painting, trim sheets
- [Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art) — official tutorial · asset library, trim sheets
- [Terrain materials](https://create.roblox.com/docs/parts/custom-terrain-materials) — official · custom terrain materials
- [Grow a Garden (Wikipedia)](https://en.wikipedia.org/wiki/Grow_a_Garden) — encyclopedia · studded look
- [Doors (Wikipedia)](https://en.wikipedia.org/wiki/Doors_(game)) — encyclopedia · Retro Mode
- [ambientCG](https://ambientcg.com/) — CC0 PBR textures
- [Poly Haven license](https://polyhaven.com/license) — CC0 assets
- [Creation.dev texture packs](https://www.creation.dev/tools/texture-packs) — third-party list · Roblox texture packs (verify licenses)
- [Stylized Grass and Flowers Asset Pack](https://builtbybit.com/resources/stylized-grass-and-flowers-asset-pack.106964/) — marketplace · stylized foliage textures

Links: [[3D Assets MOC]] · [[00 Home]]
