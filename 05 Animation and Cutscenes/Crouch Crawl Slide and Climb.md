---
title: Crouch Crawl Slide and Climb
date: 2026-11-02
tags: [animation, movement, parkour, climbing]
status: researched
---

# Crouch Crawl Slide and Climb

Stance and traversal animations are state-driven: a script decides the state (crouching, sliding, climbing), changes WalkSpeed/HipHeight/collision as needed, and plays the matching looped or one-shot clip. Survival and chase games like [[Evade]], [[Forsaken]], [[Violence District]], [[99 Nights in the Forest]] and [[Doors]] use crouching and hiding as core mechanics.

## Crouch
- Crouch idle and crouch walk are two loops (low hip, bent knees, forward torso). Blend by speed like walk/run.
- Lower WalkSpeed (for example to 8) and reduce hitbox height with HipHeight or by changing the Humanoid state; restore on stand-up.
- Toggle with C/Ctrl and a mobile button; the DevForum and video tutorials cover the LocalScript in StarterCharacterScripts.
- Stand-up check: raycast upward so the player can't stand inside low ceilings.
- Priority Action for the pose with Movement-level walk blending (or full-body custom clips).

## Crawl / prone
Lower still than crouch, arms alternating, legs dragging. Needs a head clearance fix since the character is physically upright (use HipHeight changes); many games fake it with a lowered camera offset and animations.

## Slide
- Triggered by crouch while sprinting: apply a short forward impulse (LinearVelocity or AssemblyLinearVelocity), play a slide pose (one leg forward, leaning back), decay speed over 0.6-1.0 s, then exit to crouch or run.
- Add dust/spark VFX, camera dip and a whoosh sound.
- Slide jump boosts are common in movement shooters like [[Rivals]] (verify details in-game).

## Vault
Short one-shot: raycast forward at waist and above to find a low obstacle, move the character over via tween or velocity while playing a hand-plant vault clip; disable collisions briefly. Parkour system snippets on the DevForum show ledge climb, vault and wall run scripts together.

## Ledge climb
- Two raycasts (head level and above head) detect a grabbable ledge; snap the character to hang position, play a hang loop, then a climb-up clip that ends standing on top; anchor or weld during the motion.
- Use Motor6D-free approach: tween the HumanoidRootPart CFrame with animation while Humanoid is in a Physics/PlatformStand state.

## Wall run and wall climb
- Raycast sideways for walls; apply forward velocity along the wall plane and reduce gravity via a VectorForce; play a side-lean run loop on the wall side.
- Wall climbing (Deepwoken-style) anchors the character to a wall normal and moves with WASD along it; guides cover mobile support and wall switching.

## Ladder / truss climb
Roblox Humanoid has a built-in Climbing state; the Animate script has a `climb` slot (`climb.ClimbAnim`) that plays at speed proportional to climb velocity. Replace that ID for custom ladder clips; use `AdjustSpeed(0)` when stationary so hands stop moving (the default does this).

## Tips
- Keep all of these as separate priority layers: stance loops Movement, one-shots Action2.
- Always clean up state on death/respawn.
- Mobile needs buttons for crouch and slide.

## References

- [C to Crouch Script](https://www.youtube.com/watch?v=1KwempvbNxM) — video · LocalScript crouch
- [How to make Crouch Animation](https://www.youtube.com/watch?v=wpWIhWCSRzI) — video · crouch clip
- [Crouch animation in Roblox Studio](https://www.youtube.com/watch?v=WEhBxoyfZoE) — video · crouch clip
- [C to Crouch System](https://www.youtube.com/watch?v=q7JMHe7epqY) — video · toggle
- [Crouch, Sprint and Crawl](https://www.youtube.com/watch?v=7KuoiVEDeog) — video · stance set
- [Crouch Animation tutorial (R15)](https://www.youtube.com/watch?v=HQ0COjyLXX8) — video · R15
- [Crouch animation (Fast)](https://www.youtube.com/watch?v=erLoNoLccic) — video · quick
- [Crouch/Crawl Script Tutorial](https://www.youtube.com/watch?v=EF9FMP06cWY) — video · crawl
- [Crouch script in Roblox](https://www.youtube.com/watch?v=ItVexZKClMI) — video · crouch
- [Crouch Button (PC and Mobile)](https://www.youtube.com/watch?v=WnzlLYu4n1Q) — video · mobile
- [Creating a Wall Climbing System (wall switching)](https://devforum.roblox.com/t/creating-a-wall-climbing-system-with-wall-switching/3645787) — tutorial · raycast climbing
- [Making a Wall Climbing System](https://devforum.roblox.com/t/making-a-wall-climbing-system/502101) — forum · basics
- [Creating an advanced ledge climbing system](https://devforum.roblox.com/t/creating-an-advanced-ledge-climbing-system/2166426) — forum · ledge
- [Wall climbing like in Deepwoken](https://devforum.roblox.com/t/wall-climbing-system-like-in-deepwoken/2217744) — forum · RPG climb
- [Building a climbing system](https://devforum.roblox.com/t/building-a-climbing-system/2391851) — forum · climbing
- [Parkour System Problem](https://devforum.roblox.com/t/parkour-system-problem/1511313) — forum · vault, wall run code
- [How to Make Wall Climbing](https://www.youtube.com/watch?v=cjVJZMCmdQs) — video · wall climb
- [Advanced Climbing System](https://www.youtube.com/watch?v=71qZXj_h3Do) — video · climbing
- [How to Wall-Climb](https://www.youtube.com/watch?v=RwHrB9tofPo) — video · wall climb
- [Use animations](https://create.roblox.com/docs/animation/using) — docs · Animate climb slot

Links: [[Animation MOC]] · [[00 Home]]
