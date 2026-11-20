---
title: Modeling for Roblox
date: 2026-11-02
tags: [3d, blender, pipeline, import]
status: researched
---

# Modeling for Roblox

The Blender-to-Roblox pipeline: set units, model within limits, export, import with the Studio 3D Importer, then fix pivot, collision and materials. Studio-native paths (Parts, CSG union/negate, Terrain) are covered at the end. For choosing detail see [[When to Use Which Fidelity]]; for cost see [[Performance Budgets and Optimization]].

## Hard limits (verified in official docs)

- **Individual meshes cannot exceed 20,000 triangles.** Some vendor blogs quote 21,000 or 10,000; trust the official 20,000 and test with your import. Split big models into several MeshParts.
- **One material per mesh.** UV maps must be within 0:1 and use a single UV set; overlapping UVs are allowed. UV texture spaces up to 1024x1024 are documented, while the same page also mentions texture resolutions up to 4096x4096, so test your target before relying on 4K.
- **Normal maps:** OpenGL tangent space only. Metalness workflow only.
- **Formats:** the 3D Importer accepts .fbx, .gltf/.glb and .obj; OBJ is single-mesh only. FBX/glTF carry hierarchy, PBR, rigs and animation.

## Blender setup and export

1. **Units:** Scene > Units, Unit System None, Rotation Degrees (Roblox's guide).
2. **Axes:** Forward Z, Up Y when exporting.
3. **Selection:** enable Limit to Selected Objects.
4. **FBX scale:** Transform > Apply Scalings = **FBX Unit Scale**, other scales left at 1. Alternatives (export scale 0.01, scene unit scale 0.01) can cause re-import issues; glTF avoids the scale steps. Always export a 1 m test cube and check its size in Studio.
5. **Textures:** Path Mode Copy and Embed Textures on. Disable **Add Leaf Bones**. Disable **Bake Animation** unless exporting keyframes.
6. **Studio import:** Scale Unit = Stud, World Forward = Front, World Up = Top, enable Insert Using Scene Position to keep the Blender placement. "Import Only As Model" is on by default; use "Import as Package" for reused assets.

## Pivot and origin

The Blender guide has no dedicated pivot workflow; use the 3D Cursor and "Set Origin" before export so the model's pivot sits at its logical base (floor center for props, hinge for doors). Check pivot in Studio with the Pivot tool.

## Collision and render fidelity

- **CollisionFidelity:** Box (cheapest), Hull, Default, PreciseConvexDecomposition (most accurate, costliest), Tunable (CollisionPrecision slider).
- **RenderFidelity:** Automatic switches detail by distance: highest under 250 studs, medium 250-500, lowest 500+; Performance and Precise override.
- **Rule:** Box for decor and pickups, Hull/Default for interactive props, Precise only for gameplay-critical concave shapes.

## Rigging pets and creatures

Roblox rigging links a mesh to a skeleton from Blender or Maya; influence weights are baked into the MeshPart on import and Studio exposes Bone instances for the Animation Editor. Single-mesh creatures (pets, trees, accessories) are R1-style rigged meshes. Bones affect appearance only, not collision. Community reports that 20+ bones on skinned MeshParts can hurt performance, so keep pet rigs to roughly 10-25 bones (rule of thumb, unverified). Details: [[Characters Pets and Creatures]].

## Studio part-building and CSG

- **Union** merges parts into a UnionOperation; **Negate** carves holes after union; **Separate** reverses unions. CSG works only on watertight geometry. Runtime: UnionAsync, SubtractAsync, IntersectAsync.
- **Terrain Editor:** generate, sculpt, paint, import heightmap and colormap; custom terrain materials allow up to 62 materials with Expanded Terrain enabled.
- Use Parts for blockouts and plots; export finished shapes to MeshParts to cut triangle and collision cost.

## Learning resources

- Roblox Creator Docs: Blender workflow, export requirements, rigging, 3D importer, environmental art curriculum (greybox, trim sheets, asset library, optimize).
- Roblox livestream "Intro to Modeling in Blender with Roblox" (Aug 2024, check Roblox's YouTube for recording).
- Blender low-poly tutorials (Cat Pea list, Blender Studio low-poly tree tutorial, All3DP guide) and paid Mammoth Interactive Roblox courses.
- DevForum low-poly threads: how to make low-poly builds and trees.
- AI-assisted paths exist (Meshy + Blender course; Roblox Studio generation tools) but still must meet the 20k limit.

## References

- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications) — official · 20,000 triangle limit
- [Blender to Roblox workflow](https://create.roblox.com/docs/art/blender) — official · units, scale, import settings
- [Export requirements](https://create.roblox.com/docs/art/modeling/export-requirements) — official · FBX flags
- [3D Importer](https://create.roblox.com/docs/art/modeling/3d-importer) — official · formats, import options
- [Studio Importer](https://create.roblox.com/docs/studio/importer) — official · import workflow
- [Meshes](https://create.roblox.com/docs/parts/meshes) — official · collision/render fidelity
- [Meshes in Studio](https://create.roblox.com/docs/building-and-visuals/studio-modeling/meshes-in-studio) — official · in-Studio mesh work
- [Rigging and skinning](https://create.roblox.com/docs/art/modeling/rigging) — official · bones, R1 rigged meshes
- [Solid modeling](https://create.roblox.com/docs/parts/solid-modeling) — official · union/negate/separate
- [Building unique 3D objects tutorial](https://create.roblox.com/docs/tutorials/building/modeling/building-unique-3d-objects) — official tutorial · CSG workflow
- [In-Game CSG System](https://developer.roblox.com/resources/In-Game-CSG-System) — legacy official · runtime CSG
- [Terrain](https://create.roblox.com/docs/parts/terrain) — official · terrain overview
- [Terrain Editor](https://create.roblox.com/docs/studio/terrain-editor) — official · tools
- [Custom terrain materials](https://create.roblox.com/docs/parts/custom-terrain-materials) — official · 62 materials
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official · UV/texture rules
- [Avatar character bodies export](https://create.roblox.com/docs/avatar/character-bodies/export) — official · avatar export settings
- [Katsbits: Roblox & Blender FBX scale](https://www.katsbits.com/codex/?p=8437) — tutorial · 0.01 scale approach, cube test
- [Nilo: optimize model for Roblox export](https://nilo.io/articles/optimize-model-for-roblox-export) — vendor blog · poly count tips (verify vs official)
- [Nilo: Roblox triangle limit](https://nilo.io/articles/vibe-code-roblox-triangle-limit) — vendor blog · conflicting limit figures
- [Nilo: advanced Roblox custom meshes](https://nilo.io/articles/advanced-roblox-custom-meshes) — vendor blog · collision/render table
- [3D Import Recap Apr-May 2023](https://devforum.roblox.com/t/3d-import-recap-apr-may-2023/2413182/16) — DevForum · importer updates
- [Skinned MeshParts are live](https://devforum.roblox.com/t/skinned-meshparts-are-live/831011/224) — DevForum · skinned mesh discussion
- [Skinned deformation without bones](https://devforum.roblox.com/t/how-to-achieve-skinned-mesh-deformation-without-bones/4753104) — DevForum · workaround thread
- [Intro to Modeling in Blender with Roblox](https://www.blendernation.com/2024/08/01/intro-to-modeling-in-blender-with-roblox-aug-6-livestream-by-roblox-team/) — livestream · Roblox-run
- [How to make a low poly tree](https://devforum.roblox.com/t/how-to-make-a-low-poly-tree/1344712) — DevForum · low-poly tree
- [How can I make a low poly build](https://devforum.roblox.com/t/how-can-i-make-a-low-poly-build/539908) — DevForum · low-poly builds
- [Ultimate Low Poly Character Modeling with Blender for Roblox Studio](https://mammoth-interactive.teachable.com/courses/2546537) — paid course · characters
- [Low poly models with Meshy AI, Blender 4 and Roblox](https://mammoth-interactive.teachable.com/courses/2540635) — paid course · AI-assisted
- [Low-poly to high-poly Blender course](https://www.blendernation.com/2024/07/21/game-asset-course-low-poly-to-high-poly-3d-modeling-in-blender-full-tutorial/) — course notice · game asset workflow
- [Low-poly tree texturing (Blender Foundation)](https://apricot.blender.org/tutorial-low-poly-tree-part-4/) — tutorial · modeling and texturing
- [Blender low-poly tutorial (All3DP)](https://all3dp.com/2/blender-low-poly-tutorial/) — tutorial · low-poly basics

Links: [[3D Assets MOC]] · [[00 Home]]
