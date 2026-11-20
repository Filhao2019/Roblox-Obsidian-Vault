---
title: Combat and Ability Animations
date: 2026-11-02
tags: [animation, combat, abilities, ragdoll, guns]
status: researched
---

# Combat and Ability Animations

Combat animation is a gameplay timing contract: wind-up, active (hit) frames and recovery. Animation markers mark the active frames so the server can open a hitbox exactly there. Anime battlegrounds ([[The Strongest Battlegrounds]], [[Jujutsu Shenanigans]]) are essentially animation libraries plus VFX and sound; shooters like [[Rivals]] animate viewmodels; reaction games like [[Blade Ball]] animate a parry; asymmetric horror ([[Forsaken]], [[Violence District]]) animates killer swings and survivor actions.

## M1 combos
- 4-5 punches chained; each clip has start-up, hit marker, recovery and a cancel window for the next input; the last hit is a heavier finisher with knockback.
- Alternate left/right, vary angles (body, high, low) for rhythm; the finisher adds a bigger wind-up and a slower, heavier end pose.
- Chain via a combo index reset by a timer; play the next clip at Action2 with a short fade (0.05 s).
- Add hit-stop (freeze 2-4 frames on both attacker and victim), camera nudge, sound and VFX ([[Combat and Impact Sounds]], [[Combat and Ability VFX]]).
- Variants: downslam, uppercut (jump + M1) as in TSB-style tutorials.
- Server logic: [[Combat Systems]].

## Hit reactions and stuns
- Light hit: small flinch clip (additive-like partial upper body) at Action3.
- Stun: looped dazed pose until stun timer ends; block break and guard-break use a stagger clip.
- Knockback: apply an impulse; clips for airborne flail and get-up.
- Directional hit reactions (front/back/left/right) read better than one generic flinch.

## Ragdoll
Common approach: set Humanoid state to Physics/disable GettingUp, enable BallSocketConstraints on Motor6D replacements, apply `ApplyImpulse` for knockback, give network ownership of the victim to the attacker for the knockback period, then restore joints and play a get-up clip. Pitfalls include upward flings on recovery and knockback working on NPCs but not players because of ownership.

## Dashes
Short directional clip (front/back/left/right) with velocity burst (LinearVelocity, 0.15-0.25 s), afterimage trail VFX, FOV pulse. Side dash and back dash have invincibility frames in many battlegrounds (verify per game).

## Abilities and ultimates
- Standard structure: cast pose, active loop, release, recovery.
- Ultimates in battlegrounds often take control of the camera and both characters in a short cutscene (for example TSB heroes with a cutscene grab ultimate per a guide): lock opponent, tween camera, play synced animations, then return control. See [[Cutscenes and Camera Work]].
- Custom move builders exist (TSB Skill Builder V2 combines animations, sounds, trails and props).
- Impact frames and colour-flash frames are a popular polish trick (Eclipse Animator tutorial exists).

## Guns ([[Rivals]])
- Third-person: character holds gun with an Action-priority upper-body clip, so others see aiming, reload and equip.
- First person: a separate viewmodel (arms + gun) parented to the camera, animated with equip, idle sway, fire recoil, reload, inspect; ADS moves the gun to an aim point.
- Procedural bits: sway from mouse delta, bob from velocity, recoil springs.

## Parry ([[Blade Ball]])
A single, fast, readable block/deflect clip; timing window matters more than the clip. Sword swing, shield pose and flash VFX confirm success. Details of exact implementation are unverified.

## Killer and survivor ([[Forsaken]], [[Violence District]])
Killer: wind-up swing, lunge, attack recovery with long punish; chase run with menacing lean. Survivors: vault/window, hide, heal, generator interaction loops, hit stagger and downed crawl. Use sound and camera cues for tension ([[Round-Based and Horror Systems]]).

## References

- [M1 combat like The Strongest Battlegrounds](https://www.youtube.com/watch?v=am6kv3dBos4) — video · M1 system
- [M1 Combat in Roblox Studio 2024](https://www.youtube.com/watch?v=TCJ2HgaQb7k) — video · M1
- [How To Make an M1 System](https://www.youtube.com/watch?v=8sdPq9mDLfE) — video · M1
- [Combat System M1 Combo + Downslam + Uppercut](https://www.youtube.com/watch?v=FNBT99Ra54A) — video · combo variants
- [Add M1 Combat to a Tool](https://www.youtube.com/watch?v=ZhLvaXFOgt4) — video · tool M1
- [Combat System: M1s](https://www.youtube.com/watch?v=sw1TiHiqiIs) — video · M1
- [Combat System: Stun](https://www.youtube.com/watch?v=izjD5vDg-aI) — video · stun
- [Advanced Combat System Part 1](https://www.youtube.com/watch?v=CG_kfH4QJ7w) — video · combat
- [Combat System in Roblox Studio](https://www.youtube.com/watch?v=AX3rWUj5gRo) — video · combat
- [ADVANCED COMBAT System Full Tutorial](https://www.youtube.com/watch?v=r-c1aCp5RNg) — video · combat
- [How to Animate IMPACT FRAMES](https://www.youtube.com/watch?v=549Bk_To56g) — video · impact frames
- [Knockback while ragdolled](https://devforum.roblox.com/t/any-ideas-how-i-can-apply-a-knockback-while-ragdolled/3417740) — forum · impulses
- [Knockback Ragdoll](https://devforum.roblox.com/t/how-do-i-make-a-knockback-ragdoll/1667243) — forum · basics
- [Ragdoll when hit by tool](https://devforum.roblox.com/t/how-to-make-ragdoll-when-got-hit-by-tool/4107541) — forum · tool hit
- [R6 Ragdoll and Knockback](https://devforum.roblox.com/t/r6-ragdoll-and-knockback-after-enemy-character-is-hit/2490075) — forum · R6
- [Knockback ragdoll for a combat system](https://devforum.roblox.com/t/how-would-i-make-a-knockback-ragdoll-for-a-combat-system/2049791) — forum · combat
- [Knockback script landing on back](https://devforum.roblox.com/t/how-to-make-a-knockback-script-consistently-make-you-land-on-your-back/2533030) — forum · landing
- [Proper knockback for a combat system](https://devforum.roblox.com/t/how-to-make-proper-knockback-for-a-combat-system/3936670) — forum · knockback
- [Knockback and Ragdoll Bug](https://devforum.roblox.com/t/knockback-and-ragdoll-bug/3045303) — forum · bugs
- [Knockback + Ragdoll extra upward fling](https://devforum.roblox.com/t/knockback-ragdoll-extra-upward-fling/3985033) — forum · recovery fling
- [Ragdoll knockback only for NPCs](https://devforum.roblox.com/t/ragdoll-knockback-only-working-for-npcs-and-not-players/3432025) — forum · ownership
- [FPS Tools Using ViewModels](https://devforum.roblox.com/t/fps-tools-using-viewmodels-tutorial-with-working-adsr6r15-compatible/1000436) — tutorial · ADS viewmodel
- [The First Person Element Of A First Person Shooter](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) — tutorial · viewmodel
- [Animating fps viewmodel arms](https://devforum.roblox.com/t/animating-fps-viewmodel-arms/1122319) — forum · third vs first person
- [Where to start with gun animations](https://devforum.roblox.com/t/where-to-start-with-gun-animations-and-stuff/1762787) — forum · start
- [My First Gun System (viewmodel)](https://devforum.roblox.com/t/my-first-gun-system-with-settings-tutorial-viewmodel/1941354) — tutorial · gun system
- [FPS using ViewModels (improved)](https://devforum.roblox.com/t/fps-using-viewmodels-the-improved-version-parts-2-out-of-3/1129877) — tutorial · viewmodel
- [How to Make a Gun ViewModel](https://www.youtube.com/watch?v=ZWy_bkw1pL4) — video · viewmodel
- [FE Gun Kit Viewmodel (DoomsDev)](https://www.youtube.com/watch?v=etATAnYhQaM) — video · FPS kit
- [Create your own FPS (FE Gun Kit)](https://www.youtube.com/watch?v=dV_6xYO2vy4) — video · FPS kit
- [Double Mag Reload Animation](https://www.youtube.com/watch?v=HqzW8OD8s-c) — video · reload
- [Skill Builder V2 in TSB](https://allthings.how/skill-builder-v2-in-the-strongest-battlegrounds-how-it-works/) — article · custom move builder
- [TSB The Strongest Hero guide](https://sportskeeda.com/roblox-news/the-strongest-battlegrounds-the-strongest-hero-guide) — article · cutscene grab ult
- [Animation events](https://create.roblox.com/docs/animation/events) — docs · hit markers

Links: [[Animation MOC]] · [[00 Home]]
