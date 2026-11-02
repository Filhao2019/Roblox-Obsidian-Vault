---
title: Combat and Impact Sounds
date: 2026-11-02
tags: [audio, combat, impact, footsteps, sfx]
status: researched
---

# Combat and Impact Sounds

Combat audio has three jobs: confirm that input registered, communicate outcome (hit, block, parry, kill), and carry information about enemies you cannot see. This note covers swings, hits, guns, explosions and footsteps per material, with the Roblox-specific implementation points. Genre examples are in [[SFX of Top Games]]; the visual and animation halves are [[Combat and Ability VFX]] and [[Combat and Ability Animations]]; server logic is [[Combat Systems]].

## Hits and swings

- **Swing / whoosh**: played at animation start (not at damage time). A thin-stick or cloth whoosh is the classic foley source ([Wikipedia: Foley](https://en.wikipedia.org/wiki/Foley_(filmmaking))). Pitch up for fast attacks, down for heavy.
- **Hit**: transient (click) + body (thump) + material layer (flesh, metal, wood). Tiering by damage: light, heavy, critical, each larger rather than just louder ([[What Makes a Sound Satisfying]]).
- **Hit marker / confirm** (shooters such as [[Rivals]]): short bright tick, separate sounds for body, headshot and kill; must play with zero latency on the shooter's client (predict, then reconcile). Observed pattern (unverified for individual games).
- **Block and parry** ([[Blade Ball]], [[The Strongest Battlegrounds]]): metallic clang with a bright tail; pitch can rise with the ball speed or combo to build tension. Generic clang references exist, e.g. [ElevenLabs parry page](https://elevenlabs.io/sound-effects/parry), but no source documents the game's own file.
- **Hit-stop**: freeze 40-100 ms on heavy hits and align the transient to the first frozen frame. Drop and restore animation speed in code, see [[Animation Implementation in Luau]].
- **Ultimates / abilities** ([[Jujutsu Shenanigans]], [[The Strongest Battlegrounds]]): charge-up riser, release boom, tail with low-pass decay; brief ducking of everything else ([[Audio Implementation in Luau]]).

## Guns

A layered shot design (transient, body, sub, mechanical, tail) is the practitioner standard ([Lior Tega](https://www.liortega.com/post/first-person-shooter-gun-sound-design)).

- Close shot loud and full range, distance shot low-passed with long tail: swap by distance or crossfade using `AudioEmitter` attenuation plus an [AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer).
- Limit overlapping instances (pool, see code) so full-auto fire does not distort.
- Dry-fire click, reload start/mid/end and equip sounds tell nearby players what you are doing.
- For survival horror ([[Violence District]], [[Forsaken]], [[Doors]]) the quietest sounds matter: footsteps, doors, breathing.

## Explosions

Combine a punchy transient, a sub-bass thump, debris crackle and a long reverb tail. Duck ambience and music for about a second, and add a brief low-pass on the master to simulate ear ringing (use [AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer) or a SoundGroup effect). The Doppler principle (a source sounds higher approaching, lower receding) can be faked with pitch for flybys ([Wikipedia: Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect)).

## Footsteps by material

Footsteps give position, speed and surface. Use `Humanoid.FloorMaterial` (an `Enum.Material`) to choose the set ([Humanoid](https://create.roblox.com/docs/reference/engine/classes/Humanoid)); the enum has 45 members from Plastic and Wood to Grass, Sand, Snow, Metal and Water ([Material enum](https://create.roblox.com/docs/reference/engine/enums/Material)). Group them into 8-10 buckets:

| Bucket | Materials (examples) |
|---|---|
| Hard/stone | Concrete, Pavement, Asphalt, Brick, Cobblestone, Rock, Slate, Granite, Basalt, Marble, CeramicTiles |
| Wood | Wood, WoodPlanks |
| Metal | Metal, DiamondPlate, CorrodedMetal, Foil |
| Soft earth | Grass, LeafyGrass, Ground, Mud, Pebble |
| Sand/snow | Sand, Sandstone, Snow, Salt |
| Ice/glass | Ice, Glacier, Glass |
| Fabric | Carpet, Fabric, Leather |
| Plastic/default | Plastic, SmoothPlastic, Neon, Rubber |
| Water | Water |

Rules: step interval follows walk speed (faster = shorter interval); crouch is quieter and sprint louder; 4+ variants per bucket with pitch jitter; separate landing sound with intensity from fall speed. Foley pits and prop ideas (shoes on surfaces, cornstarch pouch for snow) are described in [Wikipedia: Foley](https://en.wikipedia.org/wiki/Foley_(filmmaking)); Bfxr even bundles a footstep generator ([Bfxr](https://www.bfxr.net/)). Code: footstep controller in [[Audio Implementation in Luau]].

For horror, make footsteps part of the gameplay: [[Doors]]' Figure tracks footsteps and heartbeat ([Destructoid](https://www.destructoid.com/all-doors-entities-guide-how-to-survive/)), so loudness is a design lever.

## Threat cues and proximity layers

Asymmetric games use proximity music layers: the dead-by-daylight style terror radius splits into zones that each add a layer, replaced by chase music during a chase ([DBD wiki: chase music](https://deadbydaylight.wiki.gg/wiki/Chase_Music)). [[Violence District]] guides tell survivors to stop repairing when that audio gets loud ([Earnaldo](https://earnaldo.com/blog/violence-district-beginner-guide)). Implement with distance-driven volume on 3-4 looping stems ([[Ambience and Music]]).

## Implementation notes

- Play local-player feedback on the client; replicate others' sounds via remote events or by creating sounds on the server for positional ones ([[Networking and Remotes]]).
- 3D sounds: AudioPlayer + AudioEmitter + Wire with a distance attenuation curve ([3D tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio), [AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter)). Legacy: RollOff min/max distance on Sound ([Sound objects](https://create.roblox.com/docs/sound/objects)).
- Cap voices and prioritise by distance so a battle with dozens of players stays readable (important for [[Tower Defense Simulator]]).

## References

- [Lior Tega: FPS gun sound design](https://www.liortega.com/post/first-person-shooter-gun-sound-design) — article · gun layers
- [Wikipedia: Foley](https://en.wikipedia.org/wiki/Foley_(filmmaking)) — encyclopedia · footstep and whoosh sources
- [Wikipedia: Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) — encyclopedia · flyby pitch
- [Destructoid: Doors entities](https://www.destructoid.com/all-doors-entities-guide-how-to-survive/) — guide · footstep-tracking Figure
- [DBD wiki: chase music](https://deadbydaylight.wiki.gg/wiki/Chase_Music) — wiki · proximity layers
- [Earnaldo: Violence District guide](https://earnaldo.com/blog/violence-district-beginner-guide) — guide · terror radius audio
- [ElevenLabs: parry sounds](https://elevenlabs.io/sound-effects/parry) — library page · parry references
- [Roblox: Humanoid](https://create.roblox.com/docs/reference/engine/classes/Humanoid) — docs · FloorMaterial, Running
- [Roblox: Material enum](https://create.roblox.com/docs/reference/engine/enums/Material) — docs · material list
- [Roblox: AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter) — docs · distance attenuation
- [Roblox: add 3D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) — tutorial · wiring and attenuation
- [Roblox: AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer) — docs · distance low-pass
- [Roblox: Sound objects](https://create.roblox.com/docs/sound/objects) — docs · rolloff
- [Bfxr](https://www.bfxr.net/) — tool · includes footstep generator

Links: [[Audio MOC]] · [[00 Home]]
