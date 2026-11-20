---
title: Idle and Breathing
date: 2026-11-02
tags: [animation, idle, breathing]
status: researched
---

# Idle and Breathing

An idle is what players watch while reading menus, waiting for rounds and standing at shops, so a living idle makes a character feel alive. The default idle has two clips the Animate script picks between by weight. Good idles are short loops with tiny motion; variations and fidgets prevent staring at a repeating loop.

## Breathing idle
- Chest/torso rises 1-2 degrees and shoulders lift slightly on the inhale; head counter-moves slightly (overlap).
- Loop 2.5-4 s with Sine or Cubic easing; keep the first and last key identical.
- Offset head and arms 2-3 frames behind the torso for follow-through.
- Weight shift: slowly move hips a few degrees side to side so feet stay planted.

## Variations and fidgets
- Default Animate uses an idle with weight 9 and a second variation with weight 1, so the variation appears occasionally.
- Fidgets: look around, stretch, adjust sleeve/tool, scratch head. Make them non-looping Idle-priority clips played after N seconds of standing still, then return to the base loop.
- Per-class idles: heavy fighters wide stance, mage staff lean, killers menacing slow sway ([[Forsaken]], [[Violence District]]).
- Tool idles: hold animations at Action priority animating only arms; leave legs for locomotion (see [[Swim and Other Movement]]).

## Common mistakes
- Custom idle at Action priority overrides walking legs; use Idle or animate arms only.
- Idle not looping or wrong priority: check track `Looped` and `Priority` in the editor and in code.
- Idle breaking after respawn: reapply in `CharacterAdded`.

## Game examples
- [[Dandys World]] and other cartoon games use bouncy exaggerated idles for character appeal.
- [[Dress To Impress]] shows poses as idles in showcase moments (see [[Emotes and Social Animations]]).
- [[Adopt Me]]-style pet idles are small breathing and ear motion on rigs (unverified specifics).

## References

- [Breathing Idle (Moon Suite)](https://www.youtube.com/watch?v=L0WrqRMptsw) — video · breathing in MA
- [Idle Animation for Beginners](https://www.youtube.com/watch?v=726DR6i-TU0) — video · idle basics
- [Create Custom Idle Animation](https://www.youtube.com/watch?v=TQEcjaqNsp8) — video · load into players
- [Idle Animation in Roblox Studio (2025)](https://www.youtube.com/watch?v=9kej5WGAh44) — video · editor workflow
- [Simple Idle Animation (Blender)](https://www.youtube.com/watch?v=zuezZCaxsCU) — video · Blender
- [Breathing NPC](https://www.youtube.com/watch?v=OYRfqLudXe0) — video · simplest breathing
- [Animate a character breathing](https://www.youtube.com/watch?v=ydHj4o_8TKA) — video · easing tweak
- [Idle and Idle Moving animation with a tool](https://www.youtube.com/watch?v=BfYWlHRS55g) — video · tool idles
- [Custom Idle Animation in Roblox Studio](https://www.youtube.com/watch?v=Qm9tuFEkpB0) — video · custom idle
- [Idle Animation Not Working](https://devforum.roblox.com/t/idle-animation-not-working/3924907) — forum · debugging
- [Tool Idle Animation](https://devforum.roblox.com/t/tool-idle-animation/1339180) — forum · tool priority
- [Help on Animation scripting](https://devforum.roblox.com/t/help-on-animation-scripting/1577864) — forum · overlap fix
- [AnimationPriority enum](https://create.roblox.com/docs/en-us/reference/engine/enums/AnimationPriority) — docs · values
- [Use animations](https://create.roblox.com/docs/animation/using) — docs · Animate idle slots
- [Jespone's guide to animations](https://devforum.roblox.com/t/jespones-guide-to-animations/225752) — community · secondary action

Links: [[Animation MOC]] · [[00 Home]]
