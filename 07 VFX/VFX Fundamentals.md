---
title: VFX Fundamentals
date: 2026-11-02
tags: [vfx, fundamentals, particleemitter, beam, trail, postprocessing]
status: researched
---

# VFX Fundamentals

The building blocks of Roblox effects and the design rules that make them read well: the ParticleEmitter, Beam, Trail, Attachment, light, Highlight and post-processing classes, plus timing (anticipation, impact, dissipation), shape language, colour for effects and readability. Property names come from the official Roblox docs; behavioural notes marked (unverified) come from community posts or general VFX practice. Applied examples live in [[Combat and Ability VFX]], [[Reward and Rarity VFX]] and [[Environmental and Weather VFX]]; code is in [[VFX Implementation in Luau]].

## ParticleEmitter

A ParticleEmitter emits customizable 2D camera-facing particles. It must sit in a BasePart (particles spawn inside its volume/shape) or an Attachment (particles spawn at that point). It emits automatically while `Enabled` with a non-zero `Rate`, or on demand via `Emit(count)` (default count 16). Steady-state particle count is about `Rate x Lifetime`.

| Property | Type | What it does / practical tip |
|---|---|---|
| `Rate` | number | particles per second; 0 for burst-only emitters |
| `Lifetime` | NumberRange | seconds per particle; shorter feels snappier |
| `Speed` | NumberRange | initial velocity in studs/s |
| `SpreadAngle` | Vector2 | cone of emission; 360 for omni bursts |
| `Size` | NumberSequence | grow/shrink over life; start small, bloom, fade |
| `Transparency` | NumberSequence | fade in and out; always end at 1 |
| `Color` | ColorSequence | shift hot to cool (white-yellow to orange to dark red) |
| `LightEmission` | number | 1 = additive glow, 0 = normal blending |
| `LightInfluence` | number | how much world lighting tints the particle; 0 for glows |
| `Squash` | NumberSequence | stretches particle along its shape; used for streaks |
| `Rotation` / `RotSpeed` | NumberRange | initial and spinning rotation |
| `Drag`, `Acceleration` | number / Vector3 | slow-down and gravity-like forces |
| `Orientation` | enum | face camera, or align to velocity for sparks |
| `FlipbookLayout`, `FlipbookMode` | enum | animate a texture sheet, see [[VFX Textures and Flipbooks]] |
| `ZOffset` | number | draw-order nudge toward/away from camera; sort glow behind core |
| `LockedToPart` | bool | particles follow the part (auras) vs. stay in world (trails of smoke) |
| `TimeScale` | number | slow-motion for a single emitter, e.g. at hit-stop |
| `Shape`, `ShapeStyle` | enums | volume vs. surface emission on parts |

Community note: flipbook playback in Studio loops while in play it may behave differently for one-shot use; test behaviour in a running game (unverified, see the DevForum thread in the references).

### Burst vs. stream

- **Burst:** `Rate = 0` and call `Emit(n)` from code or on a trigger. Hit sparks, coin pops, level-up fireworks.
- **Stream:** `Enabled = true` with Rate. Fire, smoke, auras. Disable then destroy after the particles' lifetimes finish.

## Attachments

Attachments are invisible position markers inside parts. Emitters, Beams, Trails and lights all use them, which lets one invisible template part carry several effect points (hand, feet, weapon tip). Beams require two **different** attachments; Trails require two attachments on the same moving part.

## Beams

A Beam draws a textured ribbon between `Attachment0` and `Attachment1`. Key properties from the docs: `Width0`/`Width1` (studs at each end), `CurveSize0`/`CurveSize1` (how far Bezier control points extend along each attachment's axis to curve the beam), `TextureMode` (Wrap/Static repeat by length divided by `TextureLength`; Stretch repeats the texture TextureLength times across the beam), `FaceCamera` (always face the camera, essential for thin lasers). Also typically used: `TextureSpeed` to scroll the texture, `LightEmission`, `Transparency` as a NumberSequence, `Color` as a ColorSequence. Uses: lasers, tethers, lightning, kamehameha-style beams, waterfalls and force fields.

## Trails

A Trail leaves a ribbon behind two moving attachments. Docs list uses such as sword swings, projectiles and footprints. Set `Lifetime` (how long segments live), `Transparency` and `Color` sequences, `LightEmission` and `Texture`. Short lifetimes (0.2 to 0.5 s) read as speed; long ones read as magic.

## Lights

`PointLight`, `SpotLight`, `SurfaceLight` add real lighting. A brief high-Brightness PointLight flash on impact helps sell contact; keep Range small, ramp Brightness down over 0.1 to 0.3 s and avoid many simultaneous shadowed lights.

## Highlight

Highlight draws an outline and fill on an Adornee. Properties: `Adornee`, `DepthMode` (AlwaysOnTop or Occluded), `Enabled`, `FillColor`, `FillTransparency`, `OutlineColor`, `OutlineTransparency`. Uses: hit flash, rarity outlines, interactable hints, x-ray. The engine limits the number of active highlights (a commonly cited figure is 31; unverified), so prefer a few well-chosen ones.

## Post-processing

Children of `Lighting` apply to everyone; children of the camera apply to one player (good for menu blur or per-player ultimates). Types: BloomEffect (glow on bright pixels), BlurEffect, ColorCorrectionEffect (tint, contrast, saturation, brightness; e.g. red tint at low health), DepthOfFieldEffect, SunRaysEffect and ColorGradingEffect. Some effects are reduced at low graphics quality, so test with different settings. For fog, sky and haze see [[Environmental and Weather VFX]] and [[Lighting and Atmosphere]].

## Timing: anticipation, impact, dissipation

Every effect has three beats:

1. **Anticipation** (0.1 to 0.5 s): a gather, charge or telegraph. It makes the hit feel bigger and gives opponents a fair read. Skipping it makes an effect feel cheap; sources note anticipation turns a "hit" into a "slam".
2. **Impact** (1 to 3 frames of peak): maximum size/brightness, white flash, hit-stop, camera shake. Hit-stop of roughly 30 to 80 ms (2 to 5 frames) is a commonly cited range for weight.
3. **Dissipation** (0.3 to 1.5 s): smoke, embers and glow fade; a long soft tail makes an effect feel physical.

Rule of thumb: fast in, slow out. Scale peak brightness and duration with importance; a common coin pop should never look like a mythic reveal ([[Reward and Rarity VFX]]).

## Shape language

- Circles and rings: radiating force, shockwaves, magic circles.
- Triangles, spikes and streaks: speed, danger, fire.
- Soft round puffs: smoke, dust, friendly sparkle.
- Vertical columns: celebration, summoning, rarity pillars.
- Spirals: magic, wind, charging.
Combine a hard silhouette (sharp slash arc) with soft support (smoke, dust) so effects have both read and richness.

## Colour for effects

- Use value contrast first, hue second: effects must stand out from a bright map and a dark map.
- Hot-to-cool gradients (white, yellow, orange, red, dark smoke) feel like fire; the reverse feels like ice or magic.
- Reserve one hue per faction/element (blue vs. red orbs in Jujutsu-style fighters) so players read ownership instantly ([[VFX of Top Games]]).
- Rarity ladders: grey/white, green, blue, purple, gold, then rainbow or black/white inversion for the top ([[Reward and Rarity VFX]]).
- Additive blending (`LightEmission = 1`) lightens everything beneath it, so it cannot make dark smoke; use normal blending for smoke and soot.

## Readability and performance

- Keep the player character and enemies readable: lower Transparency and size near the screen centre in PvP.
- Limit overdraw: many large, overlapping, semi-transparent particles are expensive, especially on phones. Cap `Rate x Lifetime` and size; use fewer, bigger layered sprites rather than hundreds of tiny ones.
- Reuse templates, clean up with Debris, avoid per-frame instance creation ([[Code Performance and Optimization]], [[Performance Budgets and Optimization]]).
- Offer reduced-effects and reduced-shake settings.
- Check colour-blind safety on team colours.

## References

- [ParticleEmitter class reference](https://create.roblox.com/docs/en-us/reference/engine/classes/ParticleEmitter) — official API · properties, Emit default, Rate x Lifetime
- [Particle emitters (Creator Docs)](https://create.roblox.com/docs/effects/particle-emitters.md) — official guide · Studio workflow
- [Beams (Creator Docs)](https://create.roblox.com/docs/effects/beams.md) — official guide · attachments, curve, width, texture mode
- [Effects overview (Creator Docs)](https://create.roblox.com/docs/en-us/effects) — official docs · lights, particles, beams, trails, highlights
- [Highlight class reference (German)](https://create.roblox.com/docs/de-de/reference/engine/classes/Highlight) — official API · Highlight property list
- [Post-processing effects (Creator Docs)](https://create.roblox.com/docs/environment/post-processing-effects.md) — official guide · Bloom, Blur, ColorCorrection, DoF, SunRays
- [PostEffect class (legacy API reference)](https://developer.roblox.com/api-reference/class/PostEffect) — official API · parenting and quality notes
- [PostEffect class (Japanese)](https://create.roblox.com/docs/ja-jp/reference/engine/classes/PostEffect) — official API · same class, localised
- [Intro to VFX art curriculum](https://create.roblox.com/docs/tutorials/curriculums/artist.md) — official curriculum · beginner path
- [Intro to VFX art: next steps](https://create.roblox.com/docs/tutorials/curriculums/artist/next-steps.md) — official curriculum · what to learn after emitters
- [Particles' Flipbook Release (DevForum)](https://devforum.roblox.com/t/particles’-flipbook-release/2029388) — announcement · Grid2x2/4x4/8x8, size limits
- [Particle flipbook loops in Studio, one-shot in game (DevForum)](https://devforum.roblox.com/t/particle-flipbook-will-emit-1-at-time-when-its-completed-but-in-studio-it-goes-on-loop/3023343) — community thread · playback caveat
- [I want to get started with VFX (DevForum)](https://devforum.roblox.com/t/i-want-to-get-started-with-vfx/1438924) — community thread · beginner advice
- [How to create VFX? (DevForum)](https://devforum.roblox.com/t/how-to-create-vfx/4029502) — community thread · beginner workflow
- [Explosion VFX help (DevForum)](https://devforum.roblox.com/t/explosion-vfx-help/4079170) — community thread · layering an explosion
- [The Soul of Effects: What is Timing in VFX? (VFX Apprentice)](https://www.vfxapprentice.com/blog/the-soul-of-effects-what-is-timing-in-vfx) — article · timing theory
- [Game Feel & Juice lesson (Wayline)](https://www.wayline.io/learn/game-feel/1) — tutorial · juice in small doses
- [Where does game feel come from (EastonDev)](https://eastondev.com/blog/en/posts/dev/20260521-game-feedback-feel/) — article · flash, shake, text, sound, particles together
- [Hit stop, flash, shake and sound primer (uhiyama-lab)](https://uhiyama-lab.com/en/notes/unity/unity-game-feel-hit-feedback/) — article · hit-stop and impact feedback (Unity-based, principles transfer)
- [Pixel-art combat FX: hitstop, smear frames, impact timing (GamineAI)](https://gamineai.com/blog/pixel-art-combat-fx-hitstop-smear-frames-impact-timing-2026) — article · impact timing
- [20 free combat feel and juice resources (GamineAI)](https://gamineai.com/resources/20-free-combat-feel-and-juice-resources-hitstop-screenshake-vfx-timing-2026-edition) — resource list · hit-stop and shake resources


## Visual study

- [[Particles and Beams Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[VFX MOC]] · [[00 Home]]
