---
title: Animation Principles for Roblox
date: 2026-11-02
tags: [animation, principles, priority]
status: researched
---

# Animation Principles for Roblox

The classic 12 principles still apply to Roblox, but the rigs are rigid blocks with Motor6D joints (or AnimationConstraints) and no vertex deformation, so you convey weight and energy through timing, posing, arcs and exaggeration of whole limbs rather than squishing meshes. Forum veterans agree 3D animation follows the principles only partly because of this rigidity. Small mobile screens add a second rule: poses must read as a silhouette at thumbnail size.

## The 12 principles applied to R6 and R15

| Principle | Roblox application |
|---|---|
| Squash and stretch | No mesh deformation, so fake it: crouch the torso and bend knees before a jump (squash), extend limbs at the apex (stretch). Exaggerate the whole motion. Some creators add bones to faces for deformation, which costs skinning time. |
| Anticipation | A wind-up frame before every attack, jump, dash and cast. The squash before a jump is the anticipation. Battlegrounds like [[The Strongest Battlegrounds]] keep M1 wind-ups very short but visible so opponents can react. |
| Staging | Pose silhouettes: arms away from the torso, weapon extended, so the action reads from a third-person camera at distance. |
| Straight ahead / pose to pose | Roblox editors are pose-to-pose: block keys, then add breakdowns. |
| Follow-through and overlapping action | Offset timing: torso leads, head and arms lag 2-4 frames, tool or cape lags more. Add extra keys after the stop. |
| Slow in, slow out | Use Cubic or Sine easing rather than Linear. Linear looks robotic. |
| Arcs | Hands, feet and weapon tips should move on curves. Add breakdown poses between extremes to bend the path. |
| Secondary action | Head tilt, finger motion, hair or accessory sway during the main action. |
| Timing | Fast hits (2-6 frames of impact) feel punchy; slow movement feels heavy. Keep gameplay timing authoritative: the hit frame must match server timing. |
| Exaggeration | Push poses 20-30 percent further than realistic for a readable game clip. |
| Solid drawing | Keep limb rotations consistent in 3D; avoid flipping Euler angles. |
| Appeal | Strong silhouette and clear character personality. |

## Frame rates and spacing
- Roblox plays animations at 60 FPS in the editor timeline; many clips use few keyframes with easing between them (verify the current editor FPS setting).
- Keep distance between extreme keys closer near the ends of a move (slow out) and wider mid-move.
- Hit frames: hold a pose for 1-3 extra frames at impact (hit-stop feel) rather than easing straight through.

## Easing styles
Pose easing in KeyframeSequences is a style (Linear, Constant, Elastic, Cubic, Bounce, plus others) combined with a direction (In, Out, InOut). Curve animations edited in the Curve Editor use tangents instead, and the docs say bounce and elastic are not available as standard curve interpolations. See [[Moon Animator Guide]] for the Curve Editor.

## Animation priority
`Enum.AnimationPriority` values: Idle 0, Movement 1, Action 2, Action2 3, Action3 4, Action4 5, Core 1000. Higher overrides lower on the same joint; equal priority blends by weight. The default Animate script plays idle at Idle, walk and run at Movement, and jump/fall at Action in practice. Core is described in the DevForum as the lowest effective layer despite its numeric value, so confirm in your own test before relying on it (unverified). Practical rules:
- Looping hold poses (tool hold, fishing wait, carrying) use Action so they beat walk legs, but animate only the joints you need (arms) so the walk shows through on legs.
- Attacks use Action2 or higher so they beat hold poses.
- Emotes and stuns use Action3-4 to override combat holds.
- Reserve Action4 for cutscene-like scripted overrides.

## Blending and weight
- Each playing track has weight; `Play(fadeTime, weight, speed)` and `AdjustWeight` blend tracks of equal priority.
- Use fade times of about 0.1-0.2s for locomotion, 0.05s for attacks, 0.25-0.4s for idle changes.
- Upper-body only clips (arms and torso) over a lower-body walk give "run and shoot" for free.

## Looping cleanly
- First and last keyframes must match pose and easing; duplicate the first key at the end.
- Match limb phase: a walk loop is two steps; the second half mirrors the first.
- Remove drift in the root: Roblox animations drive joints, movement comes from the Humanoid.
- Preview the loop with the editor loop toggle and watch for a stutter at the seam.

## Smooth vs stiff
Smooth animations have overlap, arcs and non-uniform timing; stiff ones are all keys on the same frames with Linear easing, symmetric limbs and no secondary motion. Add a 1-2 frame offset between body parts, use Cubic or Sine easing, and add a small breathing motion to the torso even in holds.

## Mobile readability
- Push poses wider so silhouettes survive 6-inch screens.
- Keep key action beats at least 4-6 frames long.
- Pair visuals with sound and VFX ([[Combat and Ability VFX]], [[Combat and Impact Sounds]]).

## References

- [Jespone's guide to animations](https://devforum.roblox.com/t/jespones-guide-to-animations/225752) — community · principles in Roblox
- [Does 3D animation follow the 12 principles?](https://devforum.roblox.com/t/does-3d-animation-follow-the-12-principles-of-2d-animation/364997) — forum · rigid-rig limits
- [How to Make a Squash and Stretch Animation](https://devforum.roblox.com/t/how-to-make-a-squash-and-stretch-animaiton/3959076) — forum · no-deformation workaround
- [Better way to do squash-n-stretch than many bones](https://devforum.roblox.com/t/is-there-a-better-way-to-replicate-squash-n-stretch-animations-other-than-using-an-excessive-amount-of-bones/1792276) — forum · bone cost
- [Learning animating](https://devforum.roblox.com/t/learning-animating/1988679) — forum · learning path
- [Tips for animating?](https://devforum.roblox.com/t/tips-for-animating/2453194) — forum · tips
- [Animation Easing Styles](https://devforum.roblox.com/t/animation-easing-styles/25374) — forum · pose easing
- [PoseEasingDirection reference](https://robloxapi.github.io/ref/enum/PoseEasingDirection.html) — API mirror · directions
- [AnimationPriority enum](https://create.roblox.com/docs/en-us/reference/engine/enums/AnimationPriority) — docs · values
- [Animation Priority problems](https://devforum.roblox.com/t/animation-priority-problems/1710269) — forum · Core caveats
- [Help on Animation scripting](https://devforum.roblox.com/t/help-on-animation-scripting/1577864) — forum · arms-only fix
- [Tool Idle Animation](https://devforum.roblox.com/t/tool-idle-animation/1339180) — forum · tool priority
- [Curve Editor](https://create.roblox.com/docs/animation/curve-editor.md) — docs · tangents, no bounce
- [AnimationTrack](https://create.roblox.com/docs/reference/engine/classes/AnimationTrack) — API · weight and fade
- [Animation Editor](https://create.roblox.com/docs/en-us/animation/editor) — docs · interpolation
- [FLIPACLIP Lesson 03](https://www.youtube.com/watch?v=eD8DhrXxYJs) — video · squash, anticipation, arcs
- [How to Animate Squash and Stretch](https://www.youtube.com/watch?v=r17Csq0V6ok) — video · principle
- [12 Principles of Animation: Squash and Stretch](https://www.youtube.com/watch?v=jhoHv71M66Y) — video · principle
- [Squash and Stretch for Beginners](https://www.youtube.com/watch?v=67yzmKdDF5w) — video · examples

Links: [[Animation MOC]] · [[00 Home]]
