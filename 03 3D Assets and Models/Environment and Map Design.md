---
title: Environment and Map Design
date: 2026-11-02
tags: [3d, environment, maps, level-design]
status: researched
---

# Environment and Map Design

How top Roblox games lay out space: plots/bases for tycoons, hub-and-zones for simulators, arenas for shooters, procedural room kits for horror. The common thread is **greybox first, kit second, polish last** (Roblox's own Environmental Art curriculum order) and landmark readability for players who arrive on a small phone screen.

## Layout patterns by genre

| Pattern | Games | Notes |
|---|---|---|
| Plot / base per player | [[Grow a Garden]], [[Steal An Egg]], [[Break and Steal an Egg]], [[Steal a Brainrot]], [[Throw Food For Animals]] | Each player gets a plot on a shared map; you see neighbors' plots (the social/steal hook, see [[Steal and Collect Tycoon Formula]]). Bases are mostly Part-built and duplicated from a template. |
| Hub + zones | [[Pet Simulator 99]], [[Adopt Me]], [[Fisch]], [[Fish It]], [[Sols RNG]] | Central spawn hub with shops, portals to progressively harder zones or biomes; each zone has a color/material identity. |
| Island chain | [[Blox Fruits]] | Open sea with themed islands (inspired by One Piece), landmarks for quest hubs. |
| Town / life sim | [[Brookhaven RP]], [[Dress To Impress]] | Large town map with enterable buildings; Dress To Impress centers on runway and showroom spaces. |
| Arena | [[Rivals]], [[The Strongest Battlegrounds]], [[Jujutsu Shenanigans]], [[Blade Ball]], [[Murder Mystery 2]] | Compact maps with clear sightlines; Rivals shipped 30 maps at launch per a stats site and later added Experimental Maps. |
| Procedural rooms | [[Doors]] | 100 randomly generated, pre-determined rooms assembled from kits; floors (The Hotel, The Mines) share systems but change materials. |
| Survival wilderness | [[99 Nights in the Forest]], [[Evade]] | Large streamed terrain, campfire safe hub, escalating danger. |
| Lane maps | [[Tower Defense Simulator]], [[Anime Adventures]] | Fixed lanes with clear build slots. |
| Asymmetric horror | [[Violence District]], [[Forsaken]], [[Dandys World]] | Looping layouts with loops/pallets/generators style objectives (unverified), elevators for floor transitions in Dandy's World. |

## Design rules

1. **Greybox with Parts first**, test movement and sightlines, then swap in meshes (Roblox curriculum chapters 1-5).
2. **Landmarks:** one tall/colored silhouette per zone so players self-orient; vary skyline height and color.
3. **Readable paths:** lighting, floor material changes and prop clusters guide the eye. Doors uses light pools to pull players toward exits.
4. **Modular kits:** wall/floor/door pieces on a grid with shared trim sheet, see [[Materials Textures and PBR]].
5. **Terrain vs Parts:** Terrain for organic ground and water (Terrain Editor: sculpt, paint, heightmap import, up to 62 custom materials); Parts/meshes for structures. Terrain greatly reduces instance count for outdoor biomes.
6. **Streaming-friendly:** keep models grouped, avoid giant single models, use Improved ModelStreamingBehavior, see [[Performance Budgets and Optimization]].
7. **Plots as templates:** clone a plot template per player; keep it light because 10-20 plots render at once in a server.
8. **Mobile first:** big, high-contrast landmarks; fewer tiny props; wider doorways.
9. **Atmosphere per zone:** change Atmosphere/Sky or ColorCorrection per biome ([[Lighting and Atmosphere]]).

## Procedural room pipeline (Doors-like)

Build rooms as self-contained models with fixed door anchors, tag props with spawn slots, generate the next room when the player opens a door, destroy rooms behind. Keep each room under a per-room triangle budget.

## References

- [Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art) — official tutorial · greybox to optimize
- [Roblox art docs index](https://create.roblox.com/docs/art.md) — official · art section map
- [Curriculum overview](https://create.roblox.com/docs/tutorials/curriculums/curriculum-overview) — official · tutorial paths
- [Terrain](https://create.roblox.com/docs/parts/terrain) — official · terrain overview
- [Terrain Editor](https://create.roblox.com/docs/studio/terrain-editor) — official · tools
- [Create an environment with terrain](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-an-environment-with-terrain) — official tutorial
- [Custom terrain materials](https://create.roblox.com/docs/parts/custom-terrain-materials) — official · up to 62 materials
- [Instance streaming](https://create.roblox.com/docs/workspace/streaming) — official
- [Content streaming recommendations](https://create.roblox.com/docs/optimization/content-streaming) — official · radius defaults
- [Doors (Wikipedia)](https://en.wikipedia.org/wiki/Doors_(game)) — encyclopedia · The Hotel, The Mines
- [Roblox games list (Wikipedia, 99 Nights / Dandy's entries)](https://en.wikipedia.org/wiki/Dandy%27s_World) — encyclopedia · settings
- [Grow a Garden (Wikipedia)](https://en.wikipedia.org/wiki/Grow_a_Garden) — encyclopedia · plot gameplay
- [Steal a Brainrot (Wikipedia)](https://en.wikipedia.org/wiki/Steal_a_Brainrot) — encyclopedia · conveyor and base steal
- [Rivals news (rowatcher)](https://rowatcher.com/news/rivals-how-roblox-s-top-shooter-built-a-nearly-million-player-empire) — stats site · maps and modes
- [Rivals Season 3 (rowatcher)](https://rowatcher.com/news/rivals-season-3-can-roblox-s-top-shooter-sustain-300k-concurrent-players) — stats site · map updates
- [Rivals guides (games.gg)](https://games.gg/rivals/guides/) — guide site · Labor of Love maps
- [Map design skill (game-dev-skills)](https://skills.sh/taozhuo/game-dev-skills/map-design) — community skill · map design checklist
- [Low-Poly FPS Lobby](https://builtbybit.com/resources/low-poly-fps-lobby.94206/) — marketplace · lobby example
- [Fiverr Roblox map builders listing](https://fiverr.com/roblox_lua_dev/build-immersive-roblox-maps-dungeons-lobbies-arenas-and-rpg-environments) — service listing · what maps/lobbies/arenas clients commission
- [Kenney City Kit and Mini kits](https://kenney.nl/assets) — CC0 kits · modular layout study
- [Quaternius Modular Streets / Dungeons packs](https://quaternius.com) — CC0 kits · modular environment study
- [Low poly modular street pack](https://opengameart.org/content/lowpoly-modular-street-pack) — OpenGameArt · modular street
- [Medieval village pack](https://opengameart.org/content/lowpoly-medieval-village-pack) — OpenGameArt · village kit
- [Adam W environment breakdown](https://adamw3d.artstation.com/projects/gR0OGP) — ArtStation · environment art example

Links: [[3D Assets MOC]] · [[00 Home]]
