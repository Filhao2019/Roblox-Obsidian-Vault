---
title: Jump Fall and Land
date: 2026-11-02
tags: [animation, jump, fall, landing]
status: researched
---

# Jump Fall and Land

Vertical movement is where weight reads best. A jump needs anticipation, launch and apex; a fall is a loop; a landing is a short squash that recovers into idle or run. Obby-style games like [[Dont Splash]] and runners depend on responsive jump feel, so keep clips short.

## Jump
- Anticipation: 2-4 frame crouch (squash). For responsiveness, many games skip long anticipation and start the clip at the launch pose.
- Launch: legs extend, arms swing up, torso stretches.
- Apex: brief hold with limbs spread; use a slow-out ease.
- The Humanoid state `Jumping` triggers the Animate jump clip; airtime is physics, not animation.

## Fall loop
- Looping pose with arms slightly up, legs relaxed, small flutter to avoid static look.
- Fade in slowly (0.2-0.3 s) so short hops don't flash the fall pose; the default Animate script handles `Freefall`.
- Forum advice for custom fall: set the priority to Movement/Action and tune weight and fade.
- Terminal-velocity falls can switch to a stronger "falling fast" clip based on vertical speed.

## Landing and squash
- Detect with Humanoid state `Landed` or a Ground raycast; play a non-looping landing clip: knees bend, torso drops, arms balance, then recover over 0.2-0.3 s.
- Scale squash depth by fall speed (soft landing vs heavy impact); add camera dip and dust VFX ([[Environmental and Weather VFX]]).
- Roll landings for parkour games cancel velocity penalties.

## Double jump
- Second jump clip: flip or spin that overrides the fall loop at higher priority; the apex pose should differ clearly from the first jump so the double reads.
- Trigger through `UserInputService.JumpRequest` and an air-jump counter; play an air-burst VFX and a distinct sound.
- Reset the counter on `Landed`.

## R6 vs R15
R6 jump clips are limbs up/down; R15 can add knee and spine bend for crisper squash. Both use the same states.

## References

- [Making a custom fall animation](https://devforum.roblox.com/t/making-a-custom-fall-animation/2014712) — forum · fall priority, weight, fade
- [Use animations](https://create.roblox.com/docs/animation/using) — docs · jump/fall Animate entries
- [Walk and Jump Animation in Roblox](https://www.youtube.com/watch?v=9gi21mVQDB8) — video · walk and jump
- [Change Default Animations](https://devforum.roblox.com/t/change-default-animations/351811) — forum · jump ID replacement
- [Replacing default Animate script with a custom one](https://devforum.roblox.com/t/replacing-default-animate-script-with-a-custom-one/2920725) — forum · custom states
- [How am I supposed to change default animations?](https://devforum.roblox.com/t/how-am-i-supposed-to-change-default-animations/3851240) — forum · manual state handling
- [Intro to animation curriculum](https://create.roblox.com/docs/en-us/tutorials/curriculums/animator) — tutorial · replace default clips
- [How to Make a Squash and Stretch Animation](https://devforum.roblox.com/t/how-to-make-a-squash-and-stretch-animaiton/3959076) — forum · jump squash
- [Jespone's guide to animations](https://devforum.roblox.com/t/jespones-guide-to-animations/225752) — community · jump example
- [AnimationTrack](https://create.roblox.com/docs/reference/engine/classes/AnimationTrack) — API · Stopped and Ended events
- [Scripting avatar animations](https://create.roblox.com/docs/tutorials/building/animation/scripting-avatar-animations) — tutorial · Animate script
- [Squash and Stretch for Beginners](https://www.youtube.com/watch?v=67yzmKdDF5w) — video · principle

Links: [[Animation MOC]] · [[00 Home]]
