---
title: Emotes and Social Animations
date: 2026-11-02
tags: [animation, emotes, dance, social, roleplay]
status: researched
---

# Emotes and Social Animations

Emotes are social currency: they drive screenshots, short-form videos and monetization (emote packs, walks, poses). Roblox ships default emotes (`/e dance`, wave, point, cheer, laugh) via the Humanoid emote system; games add custom wheels. Roleplay games ([[Brookhaven RP]], [[Adopt Me]]) and fashion ([[Dress To Impress]]) lean on them.

## Core design
- Emote clips are Action-priority, often looped dances or one-shot gestures; cancel on movement for gestures, keep dances running until the player moves.
- Wheel or grid UI with favorites; mobile-friendly large buttons ([[Mobile Console and Responsive UI]]).
- Sync dances: players near each other can join or mirror (social hook, [[Social Features and Multiplayer Hooks]]).
- Sell packs, rarity-tiered emotes and limited event emotes ([[Monetization Patterns]]).

## Dress To Impress poses and walks
[[Dress To Impress]] has a runway where players cycle through poses and use purchasable walks; guides describe walking the centre line, pausing, cycling two or three poses, a half-turn and a final pose facing judges. "Pose 28" became a meme, showing how a single stance can go viral. Walk animations are separate purchases per a guide (prices may have changed).
Design takeaways: poses are static or low-motion loops built to show off outfits, so they favour clean silhouettes, hip and shoulder offsets and hand placement.

## Roleplay animations
Sit, lie down, hug, hold hands, carry, drive and job-specific actions (chef, doctor). Implement as seat/proximity prompts that play synced clips for two characters (align with a welded pivot) and Action3 priority.

## Authoring
- Dance loops follow the beat: author in multiples of the music BPM; mirror left/right halves.
- Use Moon Animator or the built-in editor ([[Moon Animator Guide]]), or Mixamo/Blender retargets ([[Blender and Other Animation Tools]]).
- Face animation (dynamic heads) adds expression to emotes.

## References

- [Dress To Impress guide (SteelSeries)](https://steelseries.com/blog/how-to-play-dress-to-impress) — article · runway routine
- [10 Best Poses in Dress to Impress](https://beebom.com/best-poses-dress-to-impress/) — article · pose list
- [Pose 28 (Know Your Meme)](https://knowyourmeme.com/memes/pose-28-in-dress-to-impress-roblox-game) — article · viral pose
- [Dress To Impress: Equip Walks](https://deltiasgaming.com/?p=214162) — article · walk animations and costs
- [Animate heads](https://create.roblox.com/docs/avatar/dynamic-heads/animating-dynamic-heads) — docs · face emotes
- [Use animations](https://create.roblox.com/docs/animation/using) — docs · playing clips
- [Animation capture](https://create.roblox.com/docs/en-us/animation/capture) — docs · mocap emotes
- [Roblox Animation in Blender: Full Beginner Guide (2026)](https://www.youtube.com/watch?v=eg6COxaPCyo) — video · dance authoring
- [Animate Your Roblox Avatar with Mixamo (2025)](https://www.youtube.com/watch?v=5fA4OeWIo6Y) — video · Mixamo dances
- [Moon Animator 2 Beginners Guide](https://www.youtube.com/watch?v=dFPuaH_C_Hs) — video · authoring
- [Jespone's guide to animations](https://devforum.roblox.com/t/jespones-guide-to-animations/225752) — community · personality and secondary action
- [Mixamo animations](https://devforum.roblox.com/t/mixamo-animations/3093038) — forum · Mixamo pipeline

Links: [[Animation MOC]] · [[00 Home]]
