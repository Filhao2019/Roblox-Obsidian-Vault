---
title: Locomotion Walk Run Sprint
date: 2026-11-02
tags: [animation, locomotion, walk, run]
status: researched
---

# Locomotion Walk Run Sprint

Locomotion is the clip set players see most. The default Animate script plays walk/run clips by Humanoid speed; top games replace them to give identity (heavy boss stomp, anime run, runway strut in [[Dress To Impress]]). This note covers cycle construction, speed matching and replacement methods.

## Walk and run cycle poses
A cycle for one step (mirror for the other) is built from four poses:
1. Contact: front foot heel lands, rear foot toe trails, arms opposite to legs, body at mid height.
2. Down (recoil): weight drops onto the front leg, knee bends, body at lowest point.
3. Passing: rear foot swings past the supporting knee, body rising.
4. Up: body at highest point, push-off through the rear toe.
Run cycles add a flight phase (both feet off ground), greater forward lean, higher knee drive and bent elbows. Sprint adds more lean and a shorter, faster cycle. Human gait pairs the left arm with the right leg, which videos highlight as the usual mistake to avoid. Typical lengths: walk about 0.7-1.0 s per two steps, run 0.5-0.7 s (tune by feel).

## Speed matching to WalkSpeed
Foot slide happens when animation stride does not equal movement distance. Approaches:
- Pick a reference speed per clip (for example walk clip authored for 8 studs/s, run for 16) and scale `AdjustSpeed(currentSpeed / referenceSpeed)` each frame, clamped to roughly 0.6-1.5.
- Cross-fade between walk and run by weight based on speed instead of snapping.
- For sprint, play a dedicated sprint clip with a different reference speed.
- Default R15 Humanoid speed is 16; many games override (check yours).

## Replacing default animations
- Official method: set `AnimationId` values on the Animate script (`run.RunAnim`, `walk.WalkAnim`, `swim.Swim`, etc.) from a Script, or copy the generated Animate into StarterCharacterScripts and edit it. DevForum threads disagree on whether server-side edits always apply, so test.
- Better for games: remove the Animate script and drive tracks with your own controller (see [[Animation Implementation in Luau]]). You then handle state changes yourself.
- HumanoidDescription can also specify animation bundle IDs (verify).

## R6 vs R15
- R6: 6 parts, 1 joint per limb; walk cycles are simple and stylised, many battlegrounds games use R6 because hitboxes and moves are easier ([[The Strongest Battlegrounds]]).
- R15: elbows, knees, ankles, spine; more natural but more keys. Walk cycle tutorial in Creator Docs uses R15.
- Animations are not interchangeable between rig types without retargeting.

## Make it feel good
- Add torso twist opposite to hips and head counter-rotation.
- Lean into acceleration with procedural tilt (see [[Animation Implementation in Luau]]).
- Footstep sound via animation markers ([[Audio Implementation in Luau]]).
- Sprint FOV widening reinforces speed.

## References

- [Create character animations](https://create.roblox.com/docs/en-us/tutorials/building/animation/creating-an-animation) — tutorial · R15 walk cycle from scratch
- [Intro to animation curriculum](https://create.roblox.com/docs/en-us/tutorials/curriculums/animator) — tutorial · export and replace run
- [Use animations](https://create.roblox.com/docs/animation/using) — docs · Animate script IDs
- [Play character animations](https://create.roblox.com/docs/en-us/tutorials/use-case-tutorials/animation/play-character-animations) — tutorial · scripted playback
- [Change Default Animations](https://devforum.roblox.com/t/change-default-animations/351811) — forum · replacement caveats
- [Changing Default Animations, easy way?](https://devforum.roblox.com/t/changing-default-animations-is-there-an-easy-way-to-do-it/186503) — forum · copy Animate
- [Replacing default Animate script with a custom one](https://devforum.roblox.com/t/replacing-default-animate-script-with-a-custom-one/2920725) — forum · custom controller
- [Scripting my own Animate script](https://devforum.roblox.com/t/scripting-my-own-type-of-animate-script-instead-of-changing-the-default-one/1901528) — forum · state logic
- [How am I supposed to change default animations?](https://devforum.roblox.com/t/how-am-i-supposed-to-change-default-animations/3851240) — forum · current options
- [Change default animations without forking](https://devforum.roblox.com/t/change-the-default-roblox-animations-without-forking-or-using-humanoiddiscription-system/1795493) — community · resource
- [R6 Animation Help](https://devforum.roblox.com/t/r6-animation-help/1461666) — forum · R6 entries
- [How to Animate WALK CYCLES](https://www.youtube.com/watch?v=kFEhiaKdaiw) — video · theory
- [Advanced R6 Walk Animation Tutorial](https://www.youtube.com/watch?v=hAUEJA7MrN8) — video · R6
- [Custom Walk Animation (Beginner Guide)](https://www.youtube.com/watch?v=NmcezZuoYA8) — video · custom walk
- [Walk Cycle Polish](https://www.youtube.com/watch?v=t7uRzpv4XvU) — video · polish
- [Create a Custom Walk Animation](https://www.youtube.com/watch?v=olHImEJzRBo) — video · load on join
- [Moon Animator Simple Walk Cycle](https://www.youtube.com/watch?v=MPYNxYPLoGU) — video · MA2
- [Walk and Jump Animation](https://www.youtube.com/watch?v=9gi21mVQDB8) — video · speed script in comments
- [R6 Walk cycle Prisma3D](https://www.youtube.com/watch?v=o0zundBj8mU) — video · less bouncy
- [How To Make a Walk Cycle In Roblox (Eclipse)](https://www.youtube.com/watch?v=5jHijSVX7pE) — video · contact poses
- [Walk Cycle With Eclipse Animator (2026)](https://www.youtube.com/watch?v=qzcQTBjgZ74) — video · arm/leg tip
- [Walk Cycle Tutorial: Eclipse Animator (2026)](https://www.youtube.com/watch?v=jgnj9Ul52jo) — video · cycle
- [Dress To Impress walks (Deltias Gaming)](https://deltiasgaming.com/?p=214162) — article · purchasable walks


## Visual study

- [[Animation Poses and Timing Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[Animation MOC]] · [[00 Home]]
