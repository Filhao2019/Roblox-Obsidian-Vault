---
title: Voxel and Brainrot Model Style
date: 2026-11-20
tags: [3d, voxel, brainrot, low-poly, blender, workflow]
status: untested
---

# Voxel and Brainrot Model Style

Brainrot and "steal / grow" simulators win on readability, not detail. Their units are chunky, saturated, flat-coloured models that read on a phone at 30 studs and cost almost nothing to render. This note covers the three cheap ways to build that look: voxels, Part-built models and low-poly flat meshes. It includes a Blender script, run on 2026-11-20, that turns a voxel grid into one merged, palette-textured GLB. The Roblox import step has not been tested yet, so the note stays `untested`.

![[pickle-pancake-voxel.png]]

*Original example built by the script below: "Pickle Pancake", 410 voxels, 624 triangles, one 8 × 1 px palette texture. GLB: `_Media/Voxel/pickle-pancake-voxel.glb`.*

## What the genre actually uses

- **[[Steal a Brainrot]]** units are meshes of Italian-brainrot meme characters. The exact polycount and texture method are not documented (unverified). The vault's earlier reading of them as voxel-ish is also unverified ([[Fidelity Tiers Low to High]]).
- **[[Grow a Garden]]** reads as cartoon, built from Parts and simple models rather than meme meshes (unverified).
- **Escape Tsunami for Brainrots** and **Plants vs Brainrots** reuse the same meme roster and add mutation tints on top ([[Brainrot Games Roundup]]).
- Fully voxel, Minecraft-like Roblox games exist. Islands (Easy.gg) is the best-known example ([[Fidelity Tiers Low to High]] tier 2).

Takeaway: the "slop" look is a *budget* decision. Every unit is one colour block per part, with no PBR and a silhouette that survives at a distance. Voxels are the fastest way for a solo developer or an AI agent to hit that look consistently.

## Pick a route

| Route | Best for | Cost | Watch out |
|---|---|---|---|
| Voxel mesh (MagicaVoxel, Blockbench or the script below) → GLB → Import 3D | Collectible units, pets, props with many colours | One MeshPart, a few hundred tris | Palette colours can shift on import. Check one model in Studio before batch-exporting. |
| Part-built in Studio (F3X, the Voxel To Part plugin) | Map props, plots, conveyors, anything players walk on | One Part per box. Hundreds of parts per unit hurts mobile | Merge runs of same-colour voxels into longer Parts. Never one Part per voxel on a collectible that spawns many times. |
| Low-poly flat mesh (Blender, flat shading, palette strip) | Meme characters with curves (faces, food, animals) | 100–2,000 tris per prop | Keep flat shading and the same palette as the voxel units so the two styles mix. |

## Style rules

These are working rules, not measured standards.
- **Palette:** 8–16 colours per model and about 32 for the whole game. Use one ramp per hue (light, base, dark) and shift the dark tone toward blue or purple. See LihFolk's *Voxel Palettes - Ramps Hue Shifting and Limits* in the `voxel-models` plugin.
- **Unit size:** one voxel = 0.5 stud for units and 1 stud for map blocks. Keep one unit size across the whole game, or the models look mismatched side by side.
- **Silhouette first:** test the model as a black shape. It needs a clear head and a prop (shoes, a hat, a held item) visible from 30 studs.
- **Face:** two eye blocks that pop one voxel out of the body, plus a mouth. Pupils or cheeks in a contrasting colour give it personality for 3 voxels.
- **Shading:** flat only. No smooth normals and no bevels. Depth comes from a darker voxel band (like the pancake's middle layer), not from lighting.
- **Scale:** most units are 4–8 studs tall, close to an avatar, so stealing one and carrying it reads clearly.
- **Mutations are materials, not models:** Gold, Diamond and Rainbow swap the colour or texture and add particles on the same mesh ([[Brainrot and Simulator UI Patterns]]). Never model a separate mesh for each mutation.

## Tool chooser

| Tool | Export | Notes |
|---|---|---|
| MagicaVoxel | OBJ (+ MTL + palette PNG), PLY | OBJ is Y-up, PLY is Z-up. Baked lighting only goes out as PLY. |
| Blockbench | glTF, OBJ | Versions before 4.7.0 flip V on glTF export. Good for rigged, low-poly box models. |
| Avoyd | glTF (mesh-optimised) | Since 0.26, per its devlog. |
| Blender | GLB/FBX/OBJ | Remesh modifier **Blocks** mode voxelises a sculpt. Then run Limited Dissolve to merge coplanar faces. The script below builds voxels from code. |
| Goxel, Qubicle, Voxel Max | various | Exports not checked (unverified). |

## Pipeline into Roblox

1. Model on the grid at the agreed unit size, with a palette of 16 colours or fewer.
2. **Cull interior faces** and **merge coplanar faces** of the same colour (greedy meshing or Limited Dissolve). The example dropped from 972 to 624 tris, which is 36%. Flat walls merge even better.
3. Give every face UVs at the centre of its palette cell, using a single N × 1 px texture with **Closest** filtering so cells do not bleed.
4. Export GLB with +Y up. Stay under **20,000 triangles per mesh**, the current Roblox limit; old posts quoting 10k are out of date.
5. Import with Import 3D. Metre units give one Blender metre per stud ([[Modeling for Roblox]]). Check the palette colours against the hex values and anchor the result.
6. For the classic stud look on a mesh, use a SurfaceAppearance or a MaterialVariant stud texture with StudsPerTile. The Studs surface type only works on plain Parts.

## Example: voxel grid → merged GLB (Blender 5.1)

Ran headless on Blender 5.1.2 on 2026-11-20. Its built-in self-check passed: a cube gives 12 tris, a 1×3 same-colour bar merges to 12 tris, and two colours stay as separate faces. It produced the render above. It has not been imported into Studio yet.

Usage: `blender -b --factory-startup --python voxel_model.py -- out_dir`. Change `creature()` to draw your own model. Each voxel is a `(x, y, z)` key mapped to a palette letter, and the front of the model faces −Y.

```python
"""Build a voxel model from a grid, merge coplanar faces, UV to a palette strip, export GLB and render a preview.
Run: blender.exe -b --factory-startup --python voxel_model.py -- out_dir
"""
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector

VOXEL = 0.5  # metres; Roblox Import 3D with metre units gives 0.5 studs per voxel
PALETTE = {  # key: hex. Keep it under ~16 entries so the palette strip stays tiny.
    'g': '4CAF50', 'G': '2E7D32', 'w': 'FFFFFF', 'k': '1B1B1B', 'r': 'E53935',
    'y': 'F4C26B', 'Y': 'C98B3A', 'p': 'FF8FB1',
}
SIDES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def creature():
    """Original example: a pickle on a pancake stack, wearing red sneakers. Front faces -Y."""
    v = {}
    for x in range(-4, 5):  # pancake stack, 3 layers with a darker middle
        for y in range(-4, 5):
            if x * x + y * y <= 18:
                for z in (2, 3, 4):
                    v[x, y, z] = 'Y' if z == 3 else 'y'
    for z in range(5, 15):  # pickle body: cylinder with darker bumps
        for x in range(-2, 3):
            for y in range(-2, 3):
                if x * x + y * y <= 5:
                    v[x, y, z] = 'G' if (x + y + z) % 4 == 0 and x * x + y * y >= 4 else 'g'
    for x in (-1, 1):  # eyes pop one voxel out of the front (y = -3): white top, black pupil
        v[x, -3, 12] = 'w'
        v[x, -3, 11] = 'k'
    v[0, -3, 9] = 'k'
    v[-2, -2, 9] = v[2, -2, 9] = 'p'  # cheeks touch the body at (±1, -2)
    for x in (-2, 2):  # legs and sneakers below the pancakes
        v[x, 0, 1] = 'g'
        for dx in (0, 1 if x > 0 else -1):
            v[x + dx, 0, 0] = v[x + dx, -1, 0] = 'r'
    return v


def build_mesh(voxels, name='Voxel'):
    """Emit only faces whose neighbour is empty, then dissolve coplanar faces of the same colour."""
    keys = sorted(PALETTE)
    bm = bmesh.new()
    verts = {}

    def vert(p):
        if p not in verts:
            verts[p] = bm.verts.new([c * VOXEL for c in p])
        return verts[p]

    for (x, y, z), key in voxels.items():
        for nx, ny, nz in SIDES:
            if (x + nx, y + ny, z + nz) in voxels:
                continue
            # face corners: offset 0/1 along the two axes perpendicular to the normal
            axis = [abs(nx), abs(ny), abs(nz)].index(1)
            u, w = [a for a in range(3) if a != axis]
            base = [x, y, z]
            base[axis] += 1 if (nx, ny, nz)[axis] > 0 else 0
            corners = []
            for du, dw in ((0, 0), (1, 0), (1, 1), (0, 1)):
                p = list(base)
                p[u] += du
                p[w] += dw
                corners.append(vert(tuple(p)))
            face = bm.faces.new(corners)
            face.material_index = keys.index(key)
    bm.normal_update()
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    naive = len(bm.faces) * 2
    bmesh.ops.dissolve_limit(bm, angle_limit=math.radians(1), verts=bm.verts, edges=bm.edges, delimit={'MATERIAL'})
    bmesh.ops.triangulate(bm, faces=bm.faces)
    uv = bm.loops.layers.uv.new()
    for face in bm.faces:  # every face samples the centre of its palette cell
        for loop in face.loops:
            loop[uv].uv = ((face.material_index + 0.5) / len(keys), 0.5)
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    for poly in mesh.polygons:
        poly.material_index = 0
    return mesh, naive


def palette_material():
    keys = sorted(PALETTE)
    img = bpy.data.images.new('Palette', width=len(keys), height=1)
    px = []
    for k in keys:
        h = PALETTE[k]
        px += [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)] + [1]  # byte image is sRGB: store hex as-is
    img.pixels = px
    img.pack()
    mat = bpy.data.materials.new('PaletteMat')
    mat.use_nodes = True
    tex = mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex.image = img
    tex.interpolation = 'Closest'  # no bleeding between palette cells
    bsdf = mat.node_tree.nodes['Principled BSDF']
    bsdf.inputs['Roughness'].default_value = 0.8
    mat.node_tree.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    return mat


def self_check():
    one, _ = build_mesh({(0, 0, 0): 'g'}, 'CheckOne')
    assert len(one.polygons) == 12, len(one.polygons)  # cube = 6 quads = 12 tris
    bar, naive = build_mesh({(0, 0, 0): 'g', (1, 0, 0): 'g', (2, 0, 0): 'g'}, 'CheckBar')
    assert naive == 28 and len(bar.polygons) == 12, (naive, len(bar.polygons))  # 1x3 bar merges to a box
    two, _ = build_mesh({(0, 0, 0): 'g', (1, 0, 0): 'r'}, 'CheckTwo')
    assert len(two.polygons) == 20, len(two.polygons)  # colours stay separate faces


def main(out):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    self_check()
    voxels = creature()
    mesh, naive = build_mesh(voxels, 'PicklePancake')
    mesh.materials.append(palette_material())
    obj = bpy.data.objects.new('PicklePancake', mesh)
    bpy.context.scene.collection.objects.link(obj)
    tris = len(mesh.polygons)
    assert tris < 20000, tris  # Roblox per-mesh limit
    out.mkdir(parents=True, exist_ok=True)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.export_scene.gltf(filepath=str(out / 'pickle_pancake_voxel.glb'), use_selection=True, export_yup=True)

    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_EEVEE'
    scene.render.resolution_x = scene.render.resolution_y = 800
    scene.render.film_transparent = True
    scene.view_settings.view_transform = 'Standard'
    cam = bpy.data.objects.new('Cam', bpy.data.cameras.new('Cam'))
    cam.data.type = 'ORTHO'
    cam.data.ortho_scale = 10
    cam.location = (9, -11, 9)
    target = Vector((0, 0, 3.7))  # middle of the 15-voxel-tall model
    cam.rotation_euler = (target - cam.location).to_track_quat('-Z', 'Y').to_euler()
    scene.collection.objects.link(cam)
    scene.camera = cam
    sun = bpy.data.objects.new('Sun', bpy.data.lights.new('Sun', 'SUN'))
    sun.data.energy = 3.5
    sun.rotation_euler = (math.radians(40), math.radians(15), math.radians(30))
    scene.collection.objects.link(sun)
    world = bpy.data.worlds.new('W')
    world.color = (0.6, 0.6, 0.6)
    scene.world = world
    scene.render.filepath = str(out / 'pickle_pancake_voxel.png')
    bpy.ops.render.render(write_still=True)
    print(f'RESULT voxels={len(voxels)} naive_tris={naive} merged_tris={tris} reduction={1 - tris / naive:.0%}')


main(Path(sys.argv[sys.argv.index('--') + 1]).resolve())  # render paths must be absolute
```

How it works:
- **Face culling:** a face is emitted only when the neighbouring cell is empty, so hidden faces never exist.
- **Merging:** `dissolve_limit` with `delimit={'MATERIAL'}` merges flat neighbours of the same colour into one polygon. Material indices carry the colour until UVs are written; then every face is reset to the one palette material.
- **Palette texture:** an 8 × 1 image, packed into the GLB. Roblox gets one MeshPart and one texture per unit, so a whole roster can share the same palette image.

## Common mistakes

- One Part per voxel on a unit that spawns on every conveyor tick. That means thousands of parts per server.
- Smooth shading or auto-smooth on voxel meshes. Diagonal shading smears appear across flat faces.
- Linear-vs-sRGB mix-ups when writing palette pixels from code. The first render of the example came out too dark until the hex values were stored unconverted.
- Different voxel sizes per artist or per AI batch. Fix the unit size in the brief.
- Copying meme characters 1:1. Brainrot names and designs belong to their creators. Invent your own (food + animal + object mashups work).

## References

- [General specifications](https://create.roblox.com/docs/en-us/art/modeling/specifications) — official doc · 20,000-triangle per-mesh limit
- [Remesh Modifier](https://docs.blender.org/manual/nb/4.0/modeling/modifiers/generate/remesh.html) — official doc · Blocks and Voxel remesh modes
- [RemeshModifier API](https://docs.blender.org/api/5.1/bpy.types.RemeshModifier.html) — official doc · scripting the remesh
- [Building with MagicaVoxel](https://aframe.io/docs/0.8.0/guides/building-with-magicavoxel.html) — tutorial · OBJ vs PLY export and palette texture
- [A complete guide to importing from MagicaVoxel to Sketchfab](https://sketchfab.com/blogs/community/complete-guide-importing-magicavoxel-sketchfab) — tutorial · axis differences between formats
- [Export formats](https://www.blockbench.net/wiki/guides/export-formats) — official doc · Blockbench glTF targets
- [Avoyd 0.26 devlog](https://enkisoftware.itch.io/avoyd/devlog/906201/avoyd-026-mesh-optimisation-and-export-voxels-to-gltf-for-games) — vendor blog · mesh-optimised voxel glTF
- [Voxel To Part Plugin](https://devforum.roblox.com/t/voxel-to-part-plugin/3563871) — DevForum · PLY/Goxel voxels to Parts, small props only
- [3D mesh palette doesn't import properly](https://devforum.roblox.com/t/3d-mesh-palette-doesnt-import-properly/3025496) — DevForum · palette colour shift on import
- [How to get back the old stud texture EASILY!](https://devforum.roblox.com/t/how-to-get-back-the-old-stud-texture-easily-includes-meshes-unions/3157449) — DevForum · stud SurfaceAppearance on meshes and unions
- [HD Stud Materials From 2008-2022 + Auto Converter Script](https://devforum.roblox.com/t/hd-stud-materials-from-2008-2022-auto-converter-script/1911578) — DevForum · MaterialVariant stud set
- [Kenney voxel pack](https://kenney.nl/assets/voxel-pack) — asset page · CC0 voxel blocks and props
- [Voxel pack on OpenGameArt](https://opengameart.org/content/voxel-pack) — asset page · CC0 mirror
- [Easy.gg/Islands](https://roblox.fandom.com/wiki/Easy.gg/Islands) — fan wiki · blocky Roblox game example

Links: [[3D Assets MOC]] · [[00 Home]]
