---
title: Swim and Other Movement
date: 2026-11-02
tags: [animation, swim, sit, vehicles, fishing, carrying, tools]
status: researched
---

# Swim and Other Movement

Everything that is not walk, jump or combat: swimming, sitting, vehicles, fishing, carrying and holding tools. The theme is that these are mostly hold poses plus a few transitions, layered at Action priority over the base locomotion, animating only the joints that matter.

## Swim
The Animate script has `swim.Swim` and `swimidle.SwimIdle` slots; set their `AnimationId` to custom clips (Creator Docs tutorial). Swimming triggers when the Humanoid enters the Swimming state in Terrain water. Custom water logic (non-terrain water parts) means disabling the default swim and playing your own clip when inside a volume. Swim loops should have a horizontal torso, alternating arm strokes and a flutter kick.

## Sit
- Seats set the Humanoid to Seated and play the `sit` clip. Replace via the Animate `sit.SitAnim` ID.
- Different animations per seat: detect `Seat.Occupant` changes, then load and play your own looped Action-priority clip (the DevForum covers driver seats and per-seat clips).
- Custom clips that play only briefly usually lack Looped or sufficient priority.

## Ride and vehicles
Driving poses are Action-priority loops with arms on a wheel; steering can be procedural by rotating Motor6D C0 of arms toward steering input. Pets and mounts in [[Adopt Me]] and [[Brookhaven RP]] use seat-based mounting (specific implementations unverified).

## Fishing cast ([[Fisch]], [[Fish It]])
- States: equip hold, cast wind-up, throw, wait (loop), bite (shake), reel (loop), catch (lift pose).
- Hold the wait pose with a looped Action clip or `AdjustSpeed(0)` on a frame.
- Lure flight is a scripted arc: Bezier path or projectile math, plus a RopeConstraint or beam for the line.
- Rod bending: skinned rod mesh with bones animated alongside the character, noting Moon Animator does not support skinned meshes.
- Spawn splash VFX and a bobber bob on land ([[VFX of Top Games]]).
- See also [[Fishing Systems]].

## Carrying objects (steal games)
In [[Steal a Brainrot]], [[Steal An Egg]] and [[Break and Steal an Egg]] the player carries a stolen item. Common approach (inferred; exact methods unverified): attach the model to the character via a weld or Motor6D at the hands or over the head/back, and play a two-arm carry pose at Action priority that overrides only arms; reduce WalkSpeed while carrying and add a slight forward lean. Drop and throw one-shots use higher priority. See [[Steal and Base Systems]].

## Tool holding
- Roblox plays a default tool hold when a Tool is equipped (arm raised). Replace with a looped Action clip played on `Equipped` and stopped on `Unequipped`.
- Grip mismatch between animation and tool usually comes from different Motor6D C0 values between the animation rig and the equipped weld; match them or use a grip editor plugin.
- Two-handed holds need arm animations plus a grip that fits both hands.
- To disable the default hold, some creators unset `RequiresHandle` or stop the default track, with side effects.

## References

- [Use animations](https://create.roblox.com/docs/animation/using) — docs · swim and swimidle slots
- [Swimming animation glitch](https://devforum.roblox.com/t/swimming-animation-glitch/1590334) — forum · swim state issues
- [Is it possible to change default sit animation on driver seat](https://devforum.roblox.com/t/is-it-possible-to-change-default-sit-animation-on-driver-seat/1912784) — forum · driver seat
- [Animatable vehicle seat](https://devforum.roblox.com/t/animatable-vehicle-seat/3323239) — forum · vehicle seats
- [How to change sitting animation](https://devforum.roblox.com/t/how-to-change-sitting-animation/1555722) — forum · sit replace
- [How to make a sit animation with a model](https://devforum.roblox.com/t/how-to-make-a-sit-animation-with-a-model/1375934) — forum · sit with model
- [Seat is breaking my animations on server](https://devforum.roblox.com/t/seat-is-breaking-my-animations-on-server-including-the-default-one/2691902) — forum · seat pitfalls
- [Specific seat animation](https://devforum.roblox.com/t/specific-seat-animation/195288) — forum · per-seat
- [Different Sit Animation For Every Seat](https://devforum.roblox.com/t/different-sit-animation-for-every-seat/481145) — forum · per-seat
- [Help with Seat animation](https://devforum.roblox.com/t/help-with-seat-animation/1200571) — forum · seat looping
- [More sit animation selection](https://devforum.roblox.com/t/more-sit-animation-selection/2781385) — community · sit choices
- [Sitting animation](https://devforum.roblox.com/t/sitting-animation/1168125) — forum · basics
- [Trying to make a more smooth fishing rod cast](https://devforum.roblox.com/t/trying-to-make-a-more-smooth-fishing-rod-cast/2431891) — forum · Bezier cast
- [Fishing Rod Bending Animation](https://devforum.roblox.com/t/fishing-rod-bending-animation/2907289) — forum · skinned rod
- [How Do I Make Fishing Rod Like Fisch?](https://devforum.roblox.com/t/how-do-i-make-fishing-rod-like-fisch/3640179) — forum · Fisch-like
- [Animating a character for a Fishing activity](https://devforum.roblox.com/t/how-would-i-go-about-animating-a-character-for-a-fishing-activity/309606) — forum · hold frame
- [I Need Help With My Fishing Rod](https://devforum.roblox.com/t/i-need-help-with-my-fishing-rod/754464) — forum · physics cast
- [Creating a Fishing Rod System (old)](https://www.youtube.com/watch?v=wr_uPT8Vn7M) — video · rod system
- [Fisch Tutorial: cast your rod](https://www.youtube.com/watch?v=NrPdbFZf_RM) — video · game reference
- [Perfect casting in Fisch](https://www.youtube.com/watch?v=uOm_rNnj4Lw) — video · game reference
- [How To Cast A Fishing Rod](https://www.youtube.com/watch?v=h9cUCzI2DJ8) — video · cast
- [Fishing rod guide, Steal an Egg](https://www.youtube.com/watch?v=DMo7kFVYZ0s) — video · game reference
- [How do I make a custom holding animation?](https://devforum.roblox.com/t/how-do-i-make-a-custom-holding-animation/1879888) — forum · tool hold
- [Tool grip not paired with animation](https://devforum.roblox.com/t/tool-grip-not-paired-with-animation/2863895) — forum · grip C0
- [How do I remove the holding animation for a tool?](https://devforum.roblox.com/t/how-do-i-remove-the-holding-animation-for-a-tool/2132676) — forum · disable default
- [Hold tool with both hands](https://devforum.roblox.com/t/how-to-make-player-hold-tool-with-both-hands/1632084) — forum · two-handed
- [Apply an animation while holding a tool](https://devforum.roblox.com/t/how-would-i-apply-an-animation-to-a-player-while-they-are-holding-a-tool/640186) — forum · layering
- [Change the grip of a tool while animating](https://devforum.roblox.com/t/how-do-i-change-the-grip-of-a-tool-while-its-animating/932545) — forum · dynamic grip
- [Tool not play the holding animation](https://devforum.roblox.com/t/make-a-certain-tool-not-play-the-roblox-holding-animation/2959896) — forum · skip hold
- [Tool Grip messes up tool Animation](https://devforum.roblox.com/t/tool-grip-seems-to-mess-up-tool-animation/3128090) — forum · grip issue
- [Animate a dummy holding an object](https://devforum.roblox.com/t/how-do-i-animate-a-dummy-holding-an-object/940979) — forum · authoring
- [Animated tool's grip by plugin](https://devforum.roblox.com/t/animated-tools-grip-by-plugin/4822055) — community · grip plugin

Links: [[Animation MOC]] · [[00 Home]]
