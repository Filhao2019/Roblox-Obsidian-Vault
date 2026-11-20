---
title: Blender and Other Animation Tools
date: 2026-11-02
tags: [animation, blender, mixamo, mocap, ai, cascadeur]
status: researched
---

# Blender and Other Animation Tools

When the built-in editor is too slow, creators animate in Blender, retarget Mixamo clips, use Cascadeur physics-assisted posing, or capture motion from video. The common thread: get the motion onto a Roblox rig (R6/R15 Motor6D joints) and end with a KeyframeSequence uploaded as an Animation asset.

## Blender
- Use a Blender rig exporter/animation importer pair: a Blender add-on plus a Roblox Studio plugin. A Creator Store listing "Blender rig exporter/animation importer" is referenced in a video description. Newer 2025-2026 videos show an add-on (about v2.4.1 on GitHub) covering R6 and R15 plus a matching Studio plugin.
- Typical flow: export the Roblox rig from Studio with the plugin; text is copied to the clipboard; import into Blender with the add-on; animate; export the animation; paste into Studio's import prompt; save as KeyframeSequence; publish.
- Match FPS: Blender defaults to 24 FPS; set it to your target to avoid timing drift.
- Moon Animator or Eclipse can import the result to avoid re-exporting each time (tip from a comment).
- Only animate joints Roblox supports: rotation on the bones that map to Motor6Ds; no scale or shape keys in clips.

## Mixamo retargeting
Mixamo provides free humanoid animations. A typical workflow: export the Roblox rig, upload to Mixamo or use a Mixamo skeleton, download FBX, retarget in Blender to the Roblox rig (a retargeting add-on may help but may not support standard R15), then export. Forum replies warn it is not a one-click import and that plugins can be outdated. Check licensing and Roblox content rules before shipping. Roblox's own importer can also bring in rigged FBX characters with animations (verify in docs).

## Cascadeur
Physics-assisted keyframe tool with an official Roblox export tutorial page and a "Cascadeur to Roblox" video. Good for acrobatic combat moves and realistic weight.

## Roblox animation capture
Animation Editor can generate keyframes from a webcam (face) or from an uploaded video of one person (body, R15). The Live Animation Creator page lists limits such as a single continuous shot under 15 seconds from a stable camera; the main capture page cites 60-second face recordings. Treat output as a first draft to clean.

## AI and procedural tools
- AI-driven helpers like an Eclipse Animator MCP can enhance poses, apply animation packs and convert video to keyframes via body tracking ([[Moon Animator Guide]]).
- Procedural animation in Luau (lean, IK, springs) complements clips ([[Animation Implementation in Luau]]).
- Always review AI-generated clips for joint limits, foot sliding and looping.

## Export checklist
1. Rig naming matches Motor6D/Bone names.
2. Frame rate consistent.
3. Looping flag and priority set.
4. Markers added for footsteps and hits.
5. Published under the right group or creator so playback works in your experience.

## References

- [Import Blender Animations Into Roblox R6 AND R15 Rigs (2026)](https://www.youtube.com/watch?v=X140xvLc_Rs) — video · add-on pair
- [How To Make Roblox Animation In Blender](https://www.youtube.com/watch?v=SFVrOP50hy0) — video · export/import
- [Roblox Animation in Blender: Full Beginner Guide (2026)](https://www.youtube.com/watch?v=eg6COxaPCyo) — video · FPS tip
- [Animate Roblox Characters in Blender (2026)](https://www.youtube.com/watch?v=WI6adMt2aUY) — video · beginner
- [Animate Rigs in Blender for Roblox Studio](https://www.youtube.com/watch?v=y8bfOqLtvwc) — video · rigs
- [Import Roblox Characters into Blender (2026)](https://www.youtube.com/watch?v=8lG-tkyAGoQ) — video · import rig
- [Roblox Blender Animation Guide 2025](https://www.youtube.com/watch?v=SI3P10yJcTY) — video · plugin link
- [Animating Avatar In Blender 2024](https://www.youtube.com/watch?v=HtvHrEFCTL0) — video · avatar
- [Simple Idle Animation (Blender)](https://www.youtube.com/watch?v=zuezZCaxsCU) — video · example
- [Cascadeur to Roblox](https://www.youtube.com/watch?v=WQRzvZGmJjo) — video · export
- [Cascadeur Roblox animation tutorial page](https://cascadeur.com/tutor/robloxanimation) — vendor · workflow
- [Mixamo Animations Into Roblox Using Blender 2.79](https://www.youtube.com/watch?v=WmASW9cgnLE) — video · Mixamo
- [Animate Your Roblox Avatar with Mixamo (2025)](https://www.youtube.com/watch?v=5fA4OeWIo6Y) — video · Mixamo
- [Export Mixamo Animations into Roblox Studio](https://www.youtube.com/watch?v=rplF-mKRX2A) — video · Mixamo
- [Mixamo tutorial (Blender 2.8-2.9+)](https://www.youtube.com/watch?v=vNQ2F96BRPc) — video · Mixamo
- [Custom NPC with Mixamo animation](https://www.youtube.com/watch?v=fZyjs5YgISY) — video · NPC
- [Roblox Studio + Mixamo Tutorial](https://www.youtube.com/watch?v=TNxh-uXNkWE) — video · Mixamo
- [Roblox studio Mixamo animations](https://www.youtube.com/watch?v=Vjp_zKj3uk8) — video · Mixamo
- [Transfer Mixamo Animations to Rigify](https://www.youtube.com/watch?v=nIYrwC85w9k) — video · retarget
- [Mixamo animations (DevForum)](https://devforum.roblox.com/t/mixamo-animations/3093038) — forum · pipeline
- [How can I import Mixamo animations into roblox?](https://devforum.roblox.com/t/how-can-i-import-mixamo-animations-into-roblox/3090345) — forum · import
- [Animation capture](https://create.roblox.com/docs/en-us/animation/capture) — docs · capture
- [Live Animation Creator](https://create.roblox.com/docs/building-and-visuals/animation/live-animation-creator) — docs · video limits
- [Eclipse Animator MCP (Glama)](https://glama.ai/mcp/servers/VuxSussy/Eclipse-Animator-MCP) — third-party · AI bridge
- [Create character animations](https://create.roblox.com/docs/en-us/tutorials/building/animation/creating-an-animation) — tutorial · built-in route

Links: [[Animation MOC]] · [[00 Home]]
