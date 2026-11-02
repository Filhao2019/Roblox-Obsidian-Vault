---
title: Cutscenes and Camera Work
date: 2026-11-02
tags: [animation, cutscenes, camera, cinematics]
status: researched
---

# Cutscenes and Camera Work

Cutscenes in top Roblox games are short (2-8 s), skippable beats that sell a reveal: a rare drop, an entity, a boss, an awakening. Keep them brief, never block the loop for long, and let players skip. Specific observations about games below are from general knowledge unless a source is cited; no source was found for them (unverified).

## Cinematic language
- Shot types: wide/establishing (location), medium (action), close-up (emotion or reveal), extreme close-up (detail like an eye or item).
- Angles: low angle makes subjects powerful (bosses), high angle makes them small, Dutch tilt adds unease.
- Rule of thirds: place the subject on a third line; use leading space in the direction they face.
- 180 degree rule: keep the camera on one side of the action axis between cuts so left/right stays consistent.
- Establishing shot first, then push-in to the subject.
- Push-in (dolly) builds tension; pull-out reveals scale.
- Whip pan: very fast rotation with motion blur between two shots hides a cut.
- FOV punch: briefly lower FOV (zoom) on impact then ease back; widen FOV when sprinting.
- Letterbox bars (2.39:1) signal cinematic mode; slide black frames in/out.
- Depth of field: blur background to focus subject (`DepthOfFieldEffect` in Lighting or Camera).

## Roblox camera toolkit
- `workspace.CurrentCamera.CameraType = Enum.CameraType.Scriptable` takes full control (player controls lost). Store the old CameraType/CFrame/FieldOfView to restore.
- Tween `CFrame` and `FieldOfView` with `TweenService` per shot; chain tweens with `Completed:Wait()` (a forum thread covers tweens that jump when not waited properly).
- Camera positions from authored parts (Cam1, Cam2) in a folder, so designers can edit in Studio.
- Bezier paths: evaluate quadratic/cubic Bezier for position and slerp CFrame orientation for smooth fly-throughs; drive with `RunService.RenderStepped` and an easing function.
- Moon Animator camera export: key the camera in MA2, then play back via MA2 data or convert to CFrames (see [[Moon Animator Guide]]).
- Camera shake: Perlin-noise offset applied after the camera update with `RenderPriority.Camera.Value + 1`; modules like EZ Camera Shake exist.
- Skip button: show a "Skip" TextButton, cancel tweens, restore camera, and fire a server RemoteEvent if state matters. Always allow skip for repeated cutscenes.
- Hide HUD and lock movement during the scene; restore after; handle player death mid-scene.
- Cutscenes run on the client; the server only triggers and applies results ([[Networking and Remotes]]).
- Preload animations/assets before the scene (`ContentProvider:PreloadAsync`) to avoid pop-in.

## Cutscenes in top games (observations, mostly unverified)
- [[Sols RNG]]: rare aura rolls play a dramatic reveal with sound, screen effects and a server-wide announcement; higher rarity gets a longer, more elaborate sequence.
- [[Doors]]: entities announce themselves through lighting changes, sound, screen shake and a short jump-scare close-up on death; the camera work is brief and punchy.
- [[Pet Simulator 99]] and other egg games: egg hatch zooms the camera to the egg, shakes it, cracks it, then reveals the pet with a flash and rarity effect; speed-ups skip frames for auto-hatchers ([[Pet Egg and Gacha Systems]]).
- [[Blox Fruits]]: awakening and fruit moves use short camera pushes and screen effects; storyline bosses have intro sequences.
- [[The Strongest Battlegrounds]] / [[Jujutsu Shenanigans]]: ultimates lock the camera and opponent for a stylised cutscene with impact frames and colour inversion ([[Combat and Ability Animations]]).
- Boss intros in [[Anime Adventures]] and [[Tower Defense Simulator]]: short zoom on the boss with a name card.

## Shot list template
1. Establishing wide (1.0 s)
2. Medium of trigger (0.8 s)
3. Close-up reveal with push-in (1.5 s)
4. FOV punch + shake at impact (0.3 s)
5. Pull out and return control (0.5 s)

## References

- [How to Create Camera Cutscenes](https://devforum.roblox.com/t/how-to-create-camera-cutscenes/1629318) — tutorial · Scriptable + TweenService
- [Help on making a cutscene intro](https://devforum.roblox.com/t/help-on-making-a-cutscene-intro/457786) — forum · intro
- [How do you make cutscenes?](https://devforum.roblox.com/t/how-do-you-make-cutscenes/975405) — forum · approaches
- [How do I make cutscenes?](https://devforum.roblox.com/t/how-do-i-make-cutscenes/1748208) — forum · approaches
- [CutsceneService](https://devforum.roblox.com/t/cutsceneservice/3283407) — community · module
- [How do I skip a cutscene?](https://devforum.roblox.com/t/how-do-i-skip-a-cutscene/1192583) — forum · skip
- [Cutscene on part touch](https://devforum.roblox.com/t/cutscene-on-part-touch/2622789) — forum · triggers
- [Camera moving on cutscene](https://devforum.roblox.com/t/camera-moving-on-cutscene/3305345) — forum · issues
- [Need help with Camera Tween](https://devforum.roblox.com/t/need-help-with-camera-tween/1719268) — forum · tweens
- [Cutscene Instantly Jumps to the Next Tween Position](https://devforum.roblox.com/t/cutscene-instantly-jumps-to-the-next-tween-position/815219) — forum · waiting on tweens
- [Story Cutscene management](https://devforum.roblox.com/t/story-cutscene-management/619569) — forum · structure
- [Cutscene Loading Screen](https://devforum.roblox.com/t/cutscene-loading-screen/811214) — forum · preloading
- [CameraShakeUpdated](https://devforum.roblox.com/t/camerashakeupdated-simple-camerascreen-shaking-module/3621709) — community · shake
- [A basic camera shake module](https://devforum.roblox.com/t/a-basic-camera-shake-module/1264840) — community · shake
- [Simple Shake](https://devforum.roblox.com/t/simple-shake-easy-camera-shake-module/4457496) — community · Perlin
- [EZ Camera Shake V2](https://devforum.roblox.com/t/ez-camera-shake-v2-a-refresh-of-a-popular-preferred-module-for-applying-camera-shake-effects/4671745) — community · regions
- [EZ Camera Shake ported to Roblox](https://devforum.roblox.com/t/ez-camera-shake-ported-to-roblox/98482) — community · original
- [CameraShaker](https://devforum.roblox.com/t/camerashaker-another-lightweight-camera-shaking-module/3602088) — community · lightweight
- [Help with Camera Shake Module](https://devforum.roblox.com/t/help-with-camera-shake-module/2418949) — forum · render priority
- [Easiest way to produce a CameraShake](https://devforum.roblox.com/t/found-the-easiest-way-to-produce-a-camerashake-effect-any-alternatives/3277122) — forum · alternatives
- [Roblox Cutscene Script Tutorial](https://www.youtube.com/watch?v=A3JFj7ugqKg) — video · script
- [How to Make a Cutscene in Roblox Studio (Easy)](https://www.youtube.com/watch?v=XMlc5d7OKj4) — video · easy
- [Camera Manipulation (Spectate and Cutscenes) #32](https://www.youtube.com/watch?v=FhCNvyuZ-mE) — video · advanced
- [Cutscene Camera (Camera Interpolation)](https://www.youtube.com/watch?v=DQ0FbFJ0IU8) — video · interpolation
- [Menu/Intro Camera Scene](https://www.youtube.com/watch?v=Js6BJDHsNy4) — video · menu camera
- [Easy Cutscene in Roblox Studio](https://www.youtube.com/watch?v=EzsMjxL6hAU) — video · easy
- [Cutscene in Roblox Studio 2026](https://www.youtube.com/watch?v=HEZgUK4-C18) — video · animation + camera
- [CUTSCENE in ROBLOX STUDIO Easy](https://www.youtube.com/watch?v=Qkkydch_Kdg) — video · easy
- [Code a Cutscene with different Camera Angles](https://www.youtube.com/watch?v=-f5zy0U9vD8) — video · angles
- [Moon Animator Basics](https://www.youtube.com/watch?v=Uuz_aETFQS8) — video · camera track

Links: [[Animation MOC]] · [[00 Home]]
