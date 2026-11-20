---
title: Audio MOC
date: 2026-11-02
tags: [audio, moc, index]
status: researched
---

# Audio MOC

Map of content for sound effects, music and audio code. Start with the chart-based reference, then the principles, then build. Games referenced come from [[Top Games Chart 2026-11-02]]; an honest limit: audio is thinly documented, so many game entries are marked unverified.

## Notes

| Note | Use it for |
|---|---|
| [[SFX of Top Games]] | Signature sounds and audio identity across the 27 chart games (Doors entity cues, Sols RNG rarity audio, Violence District terror-radius audio, brainrot meme audio) |
| [[What Makes a Sound Satisfying]] | Layering, pitch variation, escalation, sync with VFX, ducking, avoiding fatigue |
| [[UI Sounds]] | Click, hover, purchase, error, notifications, reward and rarity stingers |
| [[Combat and Impact Sounds]] | Hits, swings, guns, explosions, footsteps per material |
| [[Ambience and Music]] | Ambience beds, adaptive and chase music, Roblox music licensing, loudness |
| [[Making SFX]] | Tools, workflows, export, current Roblox upload limits and privacy history |
| [[Sound Sources and Libraries]] | Creator Store, Sonniss, Kenney, Freesound, Pixabay and licence notes |
| [[Audio Implementation in Luau]] | Pooled SoundManager, ducking, footsteps, combo pitch, new Audio API example (untested) |
| [[Audio References]] | Categorized link library |

## Quick start for an agent

1. Read [[What Makes a Sound Satisfying]] (principles) and [[UI Sounds]] (first sounds players hear).
2. Source assets from [[Sound Sources and Libraries]] or make them via [[Making SFX]]; check Roblox upload rules (20 MB, 7 minutes, 48 kHz, monthly free upload limits).
3. Drop in [[Audio Implementation in Luau]] and tune.
4. Add ambience and adaptive music per [[Ambience and Music]]; give players volume and opt-out toggles.
5. Pair with [[VFX MOC]] and [[Animation MOC]] so audio, particles and motion peak together.

## Related areas

[[Games MOC]] · [[UI MOC]] · [[Coding MOC]] · [[Game Design MOC]]

## References

- [Roblox audio overview](https://create.roblox.com/docs/audio) — docs · official entry point
- [Roblox audio assets requirements](https://create.roblox.com/docs/audio/assets) — docs · current upload limits
- [Roblox audio objects](https://create.roblox.com/docs/audio/objects) — docs · wiring model
- [Roblox audio effects](https://create.roblox.com/docs/audio/effects) — docs · effect chain
- [Audio privacy announcement (2022)](https://devforum.roblox.com/t/1701697) — forum · policy history
- [Sonniss GDC game audio](https://sonniss.com/gameaudiogdc/) — library · free pro SFX
- [Lior Tega: FPS gun sound design](https://www.liortega.com/post/first-person-shooter-gun-sound-design) — article · layered design
- [Wikipedia: dynamic music](https://en.wikipedia.org/wiki/Dynamic_music) — encyclopedia · adaptive music


## Visual study

- [[Spatial Audio Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


## Reference implementation brief

- [[VFX and Audio Brief]] — synchronized cue design and audio-specific evidence requirements.


Links: [[00 Home]] · [[Games MOC]]
