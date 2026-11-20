---
title: Moon Animator Guide
date: 2026-11-02
tags: [animation, moon-animator, eclipse-animator, tools, ik, face]
status: researched
---

# Moon Animator Guide

Roblox animation tooling has three layers: the built-in Animation Editor (rigs with Humanoid/Animator), community plugins like Moon Animator 2 (MA2) and the newer Eclipse Animator, and external tools (see [[Blender and Other Animation Tools]]). MA2 is the long-standing plugin for non-humanoid objects, camera tracks and cinematic sequences; the built-in editor is best for character clips that must be uploaded as Animation assets.

## Moon Animator 2 workflow
1. Install from the Creator Store (plugin page asset 4725618216 per search snippet; verify in Studio). If the camera will not animate, disable other camera plugins, as a video comment advises.
2. Insert a rig with the character inserter (R6/R15), or select your own rig made of Motor6Ds or welded parts. MA2 can animate arbitrary Parts, Models, lights and properties, not only humanoids.
3. Create an animation, set FPS/length, and key poses on the timeline by moving/rotating parts with Studio tools.
4. Edit easing per keyframe (styles and directions), scrub, loop-test.
5. Camera track: add the camera, key positions and FOV, preview from the camera.
6. Use "Easy Weld" and object tracks for props.
7. Export: per a Nilo article, Export Rig moves rigs between projects and Export All creates playable KeyframeSequences in Studio. Then publish the KeyframeSequence to Roblox as an Animation asset (right-click, Save to Roblox) to get an ID for play on the Animator.
8. For in-game playback of MA2-only data (non-rig objects), a DevForum module reads MA2 data at runtime ("Frame animation function built around Moon Animator 2").

Tips from tutorial titles/descriptions: keybinds are listed in the basics videos; select keyframes and press Delete to remove them; keep prop welds correct; export early; keep rigs named consistently.

## Eclipse Animator (the "Eclipse animator" the user asked about)
Eclipse Animator exists: it is a third-party keyframe animation plugin for Roblox Studio found through the Creator Store, with a wave of 2026 YouTube tutorials (walk cycles, impact frames, beginner guides). One guide credits the author as `@riftkuro` and lists a Creator Store asset ID; pricing is inconsistent across sources (several say free, one says paid), so check the store page (unverified). Features per the Roonby guide: keyframe timeline, Graph Editor (easing modifiers, cycles, noise), head-control option, facial animation, camera preview and FOV, effects, green-screen, onion skin, Blender animation import. A Discord listing marks features such as unparented animation and IK as coming soon, but it may be out of date. A community MCP project (Eclipse Animator MCP) lets AI agents read, write, enhance and preview animations stored in the rig's AnimSaves folder, and can import animation packs or video-based motion via MediaPipe; it requires your own copy of the plugin and works with Motor6D and AnimationConstraint rigs, not Bone rigs.

## Built-in Animation Editor
- Open via Clip Editor in the Avatar tab; pick a rig; create and name the animation; add tracks per joint; key poses; set easing; preview; Save to Roblox.
- Events (markers): add named markers on the timeline and connect with `GetMarkerReachedSignal` ([[Animation Implementation in Luau]]).
- Animation Graph Editor blends clips in graphs.
- Priority is set per animation in the editor and can be overridden by script.

## Curve Editor
Curve animations use tangents (handles) to shape interpolation before and after keys, and the docs say bounce and elastic styles are not standard for curves; a generate-interpolation workaround exists. Opening the Curve Editor converts quaternions to Euler tracks irreversibly, so duplicate your clip first.

## IK
`IKControl` solves chains between a ChainRoot and an EndEffector toward a Target, with Type, Weight, SmoothTime and Pole. Uses: foot placement on slopes, hands reaching tools, head/eye look-at, climbing hand placement. Parent it to the Humanoid or animator-owned model and drive Target from scripts.

## Face animation
Dynamic heads use `FaceControls` with FACS values from 0 to 1, keyframed in the Animation Editor via per-pose tracks or the Face Animation Editor sliders. Marketplace heads must include 17 base FACS poses. Face capture from a webcam (beta) generates keyframes. Useful for emotes and cutscene dialogue ([[Emotes and Social Animations]]).

## Choosing a tool
| Need | Pick |
|---|---|
| Humanoid clips for gameplay | Built-in editor or Eclipse |
| Props, camera, cinematic scenes | Moon Animator 2 |
| Realistic motion / retargets | Blender, Mixamo, capture |
| Faces | Face Animation Editor |

## References

- [Moon Animator 2 Basics - Official Tutorial](https://www.youtube.com/watch?v=q8tGNMo_jHg) — video · install, R6 rig
- [Introduction to Moon Animator 2 (2026 Basics Guide)](https://www.youtube.com/watch?v=BDJbGU0X5Us) — video · recent basics
- [Moon Animator 2 Beginners Guide](https://www.youtube.com/watch?v=dFPuaH_C_Hs) — video · basics
- [Moon Animator Basics](https://www.youtube.com/watch?v=Uuz_aETFQS8) — video · keybinds, easing, camera
- [Basic Moon Animator Tutorial](https://www.youtube.com/watch?v=TLIoHPl2Ips) — video · basics
- [How to Use Moon Animator 2 (old)](https://www.youtube.com/watch?v=ih1bz41mHEE) — video · older
- [How to use Moon Animator 2](https://www.youtube.com/watch?v=5n3EKo5OBi8) — video · walkthrough
- [Moon Animator 2 For COMPLETE NOOBS](https://www.youtube.com/watch?v=_W3MD44MRZc) — video · beginner
- [The Basics of Moon Animator 2](https://www.youtube.com/watch?v=Fp-dIUb1Hps) — video · basics
- [Moon Animator 2 Beginner Tutorial](https://www.youtube.com/watch?v=f97UqEea0iw) — video · beginner
- [Moon Animator Simple Walk Cycle](https://www.youtube.com/watch?v=MPYNxYPLoGU) — video · walk
- [Export Moon Animator animation to Roblox (Nilo)](https://nilo.io/articles/export-moon-animator-animation-roblox) — article · Export Rig / Export All
- [Moon Animator 2 (DevForum)](https://devforum.roblox.com/t/moon-animator-2/1653708) — community · release thread
- [Frame animation function built around Moon Animator 2](https://devforum.roblox.com/t/frame-animation-function-built-around-moon-animator-2/4214289) — community · runtime
- [Eclipse Animator Full Guide (Roonby)](https://roonby.com/2026/10/17/eclipse-animator-full-guide-how-to-install-and-use-it-in-roblox-studio/amp/) — article · features
- [Eclipse Animator MCP (Glama)](https://glama.ai/mcp/servers/VuxSussy/Eclipse-Animator-MCP) — third-party · AI bridge
- [Eclipse Animator Discord listing](https://discord.com/servers/eclipse-animator-1453567930234048707) — community · status
- [Eclipse Animator - Beginner's Guide (2026)](https://www.youtube.com/watch?v=3pL2B30uU4c) — video · basics
- [I Tried Animating in Roblox Studio (Eclipse)](https://www.youtube.com/watch?v=Pk_ETEMVRlg) — video · first look
- [How to install Eclipse Animator](https://www.youtube.com/watch?v=WHxJbD4lQak) — video · install
- [Walk Cycle Tutorial: Eclipse Animator (2026)](https://www.youtube.com/watch?v=jgnj9Ul52jo) — video · walk
- [Animation Editor](https://create.roblox.com/docs/en-us/animation/editor) — docs · built-in editor
- [Animation Graph Editor](https://create.roblox.com/docs/animation/graph-editor) — docs · graphs
- [Animation events](https://create.roblox.com/docs/animation/events) — docs · markers
- [Curve Editor](https://create.roblox.com/docs/animation/curve-editor.md) — docs · tangents
- [CurveAnimation](https://create.roblox.com/docs/en-us/reference/engine/classes/CurveAnimation) — API · asset type
- [IKControl (Italian page)](https://create.roblox.com/docs/it-it/reference/engine/classes/IKControl) — API · properties
- [IKControl (Japanese page)](https://create.roblox.com/docs/ja-jp/reference/engine/classes/IKControl) — API · methods
- [Facial Animation](https://create.roblox.com/docs/avatar/dynamic-heads) — docs · dynamic heads
- [Animate heads](https://create.roblox.com/docs/avatar/dynamic-heads/animating-dynamic-heads) — docs · face editor
- [FACS poses reference](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference.md) — docs · 17 poses
- [FaceControls](https://create.roblox.com/docs/reference/engine/classes/FaceControls.md) — API · properties
- [Animation capture](https://create.roblox.com/docs/en-us/animation/capture) — docs · face capture

Links: [[Animation MOC]] · [[00 Home]]
