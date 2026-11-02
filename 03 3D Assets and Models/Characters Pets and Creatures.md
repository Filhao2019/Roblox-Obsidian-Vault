---
title: Characters Pets and Creatures
date: 2026-11-02
tags: [3d, characters, pets, rigging, creatures]
status: researched
---

# Characters Pets and Creatures

Collectibles are the product in the biggest games: pets in [[Pet Simulator 99]] and [[Adopt Me]], eggs and pets in [[Steal An Egg]], brainrots in [[Steal a Brainrot]], toons in [[Dandys World]], fish in [[Fisch]]. This note covers design for rarity and readability, rig choices, and monsters. For tiers see [[Fidelity Tiers Low to High]]; for hatching systems see [[Pet Egg and Gacha Systems]].

## Design rules for collectibles

1. **Silhouette first:** the shape alone must identify the creature at 64 px icon size and at a distance on a phone. Adopt Me's style guide is built on a hero set of the most-wanted pets with distinct silhouettes and bright family-friendly colors.
2. **Rarity reads without text:** escalate along multiple channels, never just one: size (bigger), color saturation/contrast, material (metallic, glass, gold), emissive glow, particles, aura, idle animation, sound. Pet Simulator 99 uses rarity tiers from Common to Exclusive plus Huge/Titanic-style size jumps (size tiers observed, unverified).
3. **Variants reuse the base mesh:** recolor via tint/texture swap and add VFX ([[Reward and Rarity VFX]]) so 100 pets do not need 100 meshes; one ColorMap can be tinted for free (SurfaceAppearance).
4. **Chunky proportions:** big head, short limbs, simple faces. They survive low LOD, look cute and animate easily.
5. **Budget:** 1.5k-8k triangles per pet, 256-1024 px texture, 8-25 bones (rules of thumb). Following pets multiply: 50 pets visible x 5k tris = 250k tris, so budget for the crowd, not the single model.
6. **Brainrots:** Wikipedia describes Steal a Brainrot's characters as voxel characters based on Italian brainrot memes. Fan packs of the same characters exist as high-poly baked-texture rigged models; the in-game versions are intentionally simpler. Copying meme characters carries licensing risk (the game itself removed Tung Tung Tung Sahur in September 2025 over a licensing dispute and restored it in November 2025).

## Rig choices

| Rig | Use | Notes |
|---|---|---|
| R6 | Legacy/blocky avatars | 6 parts, cheap, limited animation |
| R15 | Standard avatar, NPC humanoids | 15 parts, layered clothing support; [[Dress To Impress]] builds on layered clothing |
| Custom MeshPart rig (R1 single mesh or Motor6D parts) | Pets, monsters, bosses | Single skinned MeshPart with Bone instances, or segmented parts joined with Motor6D |
| Static + procedural animation | Following pets, collectibles | Bob/rotate with Tween or CFrame; zero skeletal cost |

Skinned mesh facts: influence is assigned in Blender/Maya and stored on the MeshPart at import; Studio shows Bone instances for the Animation Editor; bones do not change collision. One DevForum report says 20+ bones on skinned MeshParts caused lag. See [[Modeling for Roblox]] and [[Animation Implementation in Luau]].

## NPCs and monsters

- **Horror entities** ([[Doors]]): distinct silhouettes (tall, many-eyed, glitchy) and signature audio/VFX cues matter more than polygon count. Doors entities are described as hostile or helpful (Wikipedia).
- **Survival creatures** ([[99 Nights in the Forest]]): readable threat shapes at night; fog plus emissive eyes.
- **Toons vs Twisted** ([[Dandys World]]): cute design inverted into corrupted versions: reuse the base, change proportion, texture and animation.
- **Asymmetric killers** ([[Violence District]], [[Forsaken]]): strong costume silhouette and weapon read.
- **Bosses** ([[Blox Fruits]]): larger-than-avatar scale, simple attack tells.

## Free creature sources (check licenses)

Quaternius Cute Animated Monsters Pack, Ultimate Animated Animal Pack, Animated Dinosaur Pack, Easy Enemy Pack, Bestiary - Dungeon Monsters Kit (all in the Quaternius catalog), Kenney Mini Forest/Mini Dungeon. Fan brainrot packs: Italian Brainrot Characters (itch.io, Sketchfab), but they are fan art of memes (check license and IP). Mixamo-style retargeting is possible for humanoids (verify terms, see [[Free and Paid Asset Sources]]).

## References

- [Rigging and skinning](https://create.roblox.com/docs/art/modeling/rigging) — official · bones, R1 rigged meshes
- [Skinned MeshParts are live](https://devforum.roblox.com/t/skinned-meshparts-are-live/831011/224) — DevForum · skinned mesh thread
- [Skinned deformation without bones](https://devforum.roblox.com/t/how-to-achieve-skinned-mesh-deformation-without-bones/4753104) — DevForum · bone-count lag report
- [Surface appearance](https://create.roblox.com/docs/art/modeling/surface-appearance) — official · tint reuse
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official · character texture sizes
- [Character bodies export](https://create.roblox.com/docs/avatar/character-bodies/export) — official · avatar export
- [Emote export](https://create.roblox.com/docs/avatar/emotes/export) — official · animation export settings
- [Adopt Me art direction interview](https://brandsuntapped.com/?p=8177) — interview · hero pet style guide
- [Pet Simulator 99 wiki](https://roblox.fandom.com/wiki/BIG_Games_Pets/Pet_Simulator_99) — fan wiki · pet rarities
- [Steal a Brainrot (Wikipedia)](https://en.wikipedia.org/wiki/Steal_a_Brainrot) — encyclopedia · voxel characters, licensing dispute
- [Dandy's World (Wikipedia list)](https://en.wikipedia.org/wiki/Dandy%27s_World) — encyclopedia · Toons and Twisted Toons
- [Doors (Wikipedia)](https://en.wikipedia.org/wiki/Doors_(game)) — encyclopedia · entities
- [Dress to Impress (Wikipedia)](https://en.wikipedia.org/wiki/Dress_to_Impress_(video_game)) — encyclopedia · avatar clothing
- [Brainrot Model Pack animated + VFX](https://builtbybit.com/resources/brainrot-model-pack-animated-vfx.117855/) — marketplace · animated brainrots
- [Italian brainrot meme characters 2](https://sketchfab.com/3d-models/italian-brainrot-meme-characters-2-cac813a642194a6ba2a191e6ffdb7ec7) — Sketchfab · check license
- [Trallaleo Trallala (Printables)](https://www.printables.com/model/1406088-trallaleo-trallala-steal-a-brainrot) — Printables · fan 3D print
- [Quaternius catalog](https://quaternius.com) — CC0 · animated monsters/animals
- [Quaternius cars pack](https://quaternius.itch.io/lowpoly-cars) — itch.io · CC0 with Patreon-only exception
- [Kenney assets](https://kenney.nl/assets) — CC0 · Mini Forest, Mini Dungeon
- [Roblox rigging forum: devforum skinned](https://devforum.roblox.com/t/skinned-meshparts-are-live/831011/224) — DevForum · discussion thread

Links: [[3D Assets MOC]] · [[00 Home]]
