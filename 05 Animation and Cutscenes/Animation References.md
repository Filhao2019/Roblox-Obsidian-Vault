---
title: Animation References
date: 2026-11-02
tags: [animation, references, links]
status: researched
---

# Animation References

The master link library for the animation folder: Creator Docs, DevForum threads, YouTube tutorials and tool pages, grouped by topic. Every URL here was opened or returned by a search on 2026-11-02. Video titles and ages were only seen in search snippets, so skim before trusting step-by-step details; many tutorials are years old. Per-topic notes carry their own smaller reference lists.

## Official Creator Docs

- [Animation in Roblox](https://create.roblox.com/docs/building-and-visuals/animation) — docs · overview of animation systems
- [Animation Editor](https://create.roblox.com/docs/en-us/animation/editor) — docs · timeline, poses, interpolation
- [Animation Editor (building-and-visuals path)](https://create.roblox.com/docs/building-and-visuals/animation/animation-editor) — docs · same editor, newer URL layout
- [Use animations](https://create.roblox.com/docs/animation/using) — docs · replace default Animate IDs, swim/run/jump slots
- [Use animations (building-and-visuals path)](https://create.roblox.com/docs/building-and-visuals/animation/using-animations) — docs · playing tracks from scripts
- [Animation events](https://create.roblox.com/docs/animation/events) — docs · markers and GetMarkerReachedSignal
- [Animation Graph Editor](https://create.roblox.com/docs/animation/graph-editor) — docs · blending graphs
- [Curve Editor](https://create.roblox.com/docs/animation/curve-editor.md) — docs · tangents, curve animations
- [CurveAnimation class](https://create.roblox.com/docs/en-us/reference/engine/classes/CurveAnimation) — API · curve-based animation asset
- [AnimationTrack](https://create.roblox.com/docs/reference/engine/classes/AnimationTrack) — API · Play, AdjustWeight, AdjustSpeed, Priority
- [KeyframeMarker](https://create.roblox.com/docs/reference/engine/classes/KeyframeMarker) — API · marker instance
- [AnimationPriority enum](https://create.roblox.com/docs/en-us/reference/engine/enums/AnimationPriority) — API · Idle 0, Movement 1, Action 2-5, Core 1000
- [Animation capture](https://create.roblox.com/docs/en-us/animation/capture) — docs · face and body capture
- [Live Animation Creator](https://create.roblox.com/docs/building-and-visuals/animation/live-animation-creator) — docs · video to R15 keyframes
- [IKControl (Italian page)](https://create.roblox.com/docs/it-it/reference/engine/classes/IKControl) — API · IK properties and example
- [IKControl (Japanese page)](https://create.roblox.com/docs/ja-jp/reference/engine/classes/IKControl) — API · IK methods list
- [Facial Animation (dynamic heads)](https://create.roblox.com/docs/avatar/dynamic-heads) — docs · FACS overview
- [Animate heads](https://create.roblox.com/docs/avatar/dynamic-heads/animating-dynamic-heads) — docs · face animation editor
- [FACS poses reference](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference.md) — docs · the 17 required poses
- [FaceControls](https://create.roblox.com/docs/reference/engine/classes/FaceControls.md) — API · FACS properties
- [Facial animation (art)](https://create.roblox.com/docs/art/characters/facial-animation) — docs · authoring faces
- [Intro to animation curriculum](https://create.roblox.com/docs/en-us/tutorials/curriculums/animator) — tutorial · first animation, replace run
- [Create character animations](https://create.roblox.com/docs/en-us/tutorials/building/animation/creating-an-animation) — tutorial · full R15 walk cycle
- [Create character animations (use-case path)](https://create.roblox.com/docs/en-us/tutorials/use-case-tutorials/animation/create-an-animation) — tutorial · same walk-cycle lesson
- [Play character animations](https://create.roblox.com/docs/en-us/tutorials/use-case-tutorials/animation/play-character-animations) — tutorial · scripted playback
- [Scripting avatar animations](https://create.roblox.com/docs/tutorials/building/animation/scripting-avatar-animations) — tutorial · Animate script editing

## DevForum — principles and tips

- [Jespone's guide to animations](https://devforum.roblox.com/t/jespones-guide-to-animations/225752) — community · principles applied to Roblox
- [How to Make a Squash and Stretch Animation](https://devforum.roblox.com/t/how-to-make-a-squash-and-stretch-animaiton/3959076) — forum · squash without deformation
- [Does 3D animation follow the 12 principles?](https://devforum.roblox.com/t/does-3d-animation-follow-the-12-principles-of-2d-animation/364997) — forum · rigid rigs and principles
- [Learning animating](https://devforum.roblox.com/t/learning-animating/1988679) — forum · learning path
- [Squash-n-stretch without many bones](https://devforum.roblox.com/t/is-there-a-better-way-to-replicate-squash-n-stretch-animations-other-than-using-an-excessive-amount-of-bones/1792276) — forum · bone tricks
- [Tips for animating?](https://devforum.roblox.com/t/tips-for-animating/2453194) — forum · general advice
- [Animation Easing Styles](https://devforum.roblox.com/t/animation-easing-styles/25374) — forum · pose easing history
- [PoseEasingDirection reference](https://robloxapi.github.io/ref/enum/PoseEasingDirection.html) — API mirror · easing directions
- [Animation Priority problems](https://devforum.roblox.com/t/animation-priority-problems/1710269) — forum · Core priority pitfalls
- [Help on Animation scripting](https://devforum.roblox.com/t/help-on-animation-scripting/1577864) — forum · idle overriding movement
- [Tool Idle Animation](https://devforum.roblox.com/t/tool-idle-animation/1339180) — forum · tool hold priorities

## DevForum — replacing default animations

- [Change Default Animations](https://devforum.roblox.com/t/change-default-animations/351811) — forum · server vs client Animate
- [Replacing default Animate script with a custom one](https://devforum.roblox.com/t/replacing-default-animate-script-with-a-custom-one/2920725) — forum · custom controller
- [Scripting my own Animate script](https://devforum.roblox.com/t/scripting-my-own-type-of-animate-script-instead-of-changing-the-default-one/1901528) — forum · own state machine
- [Making a custom fall animation](https://devforum.roblox.com/t/making-a-custom-fall-animation/2014712) — forum · fall priority and weight
- [Change default animations without forking](https://devforum.roblox.com/t/change-the-default-roblox-animations-without-forking-or-using-humanoiddiscription-system/1795493) — community · resource
- [How am I supposed to change default animations?](https://devforum.roblox.com/t/how-am-i-supposed-to-change-default-animations/3851240) — forum · current state
- [Changing Default Animations, easy way?](https://devforum.roblox.com/t/changing-default-animations-is-there-an-easy-way-to-do-it/186503) — forum · copy Animate to StarterCharacterScripts
- [Swimming animation glitch](https://devforum.roblox.com/t/swimming-animation-glitch/1590334) — forum · swim state
- [R6 Animation Help](https://devforum.roblox.com/t/r6-animation-help/1461666) — forum · R6 animate entries
- [Idle Animation Not Working](https://devforum.roblox.com/t/idle-animation-not-working/3924907) — forum · idle debugging

## DevForum — cutscenes and camera

- [How to Create Camera Cutscenes](https://devforum.roblox.com/t/how-to-create-camera-cutscenes/1629318) — tutorial · Scriptable + TweenService
- [Help on making a cutscene intro](https://devforum.roblox.com/t/help-on-making-a-cutscene-intro/457786) — forum · intro cutscene
- [How do you make cutscenes?](https://devforum.roblox.com/t/how-do-you-make-cutscenes/975405) — forum · approaches
- [How do I make cutscenes?](https://devforum.roblox.com/t/how-do-i-make-cutscenes/1748208) — forum · approaches
- [CutsceneService](https://devforum.roblox.com/t/cutsceneservice/3283407) — community · module
- [How do I skip a cutscene?](https://devforum.roblox.com/t/how-do-i-skip-a-cutscene/1192583) — forum · skip handling
- [Cutscene on part touch](https://devforum.roblox.com/t/cutscene-on-part-touch/2622789) — forum · triggers
- [Camera moving on cutscene](https://devforum.roblox.com/t/camera-moving-on-cutscene/3305345) — forum · camera issues
- [Need help with Camera Tween](https://devforum.roblox.com/t/need-help-with-camera-tween/1719268) — forum · tween troubleshooting
- [Cutscene Instantly Jumps to the Next Tween Position](https://devforum.roblox.com/t/cutscene-instantly-jumps-to-the-next-tween-position/815219) — forum · Completed waits
- [Story Cutscene management](https://devforum.roblox.com/t/story-cutscene-management/619569) — forum · structure
- [Cutscene Loading Screen](https://devforum.roblox.com/t/cutscene-loading-screen/811214) — forum · preloading
- [CameraShakeUpdated](https://devforum.roblox.com/t/camerashakeupdated-simple-camerascreen-shaking-module/3621709) — community · shake module
- [A basic camera shake module](https://devforum.roblox.com/t/a-basic-camera-shake-module/1264840) — community · shake module
- [Simple Shake](https://devforum.roblox.com/t/simple-shake-easy-camera-shake-module/4457496) — community · Perlin shake
- [EZ Camera Shake V2](https://devforum.roblox.com/t/ez-camera-shake-v2-a-refresh-of-a-popular-preferred-module-for-applying-camera-shake-effects/4671745) — community · shake regions
- [EZ Camera Shake ported to Roblox](https://devforum.roblox.com/t/ez-camera-shake-ported-to-roblox/98482) — community · the original
- [CameraShaker (Judash399)](https://devforum.roblox.com/t/camerashaker-another-lightweight-camera-shaking-module/3602088) — community · lightweight shaker
- [Help with Camera Shake Module](https://devforum.roblox.com/t/help-with-camera-shake-module/2418949) — forum · render priority fix
- [Easiest way to produce a CameraShake](https://devforum.roblox.com/t/found-the-easiest-way-to-produce-a-camerashake-effect-any-alternatives/3277122) — forum · Humanoid.CameraOffset approach
- [Setting up a camera shake](https://devforum.roblox.com/t/setting-up-a-camera-shake/2577628) — forum · setup
- [Help with EZ Camera Shake](https://devforum.roblox.com/t/help-with-ez-camera-shake/3579065) — forum · troubleshooting

## DevForum — movement, combat, tools

- [Creating a Wall Climbing System (wall switching)](https://devforum.roblox.com/t/creating-a-wall-climbing-system-with-wall-switching/3645787) — tutorial · raycast climbing
- [Making a "Wall Climbing" System](https://devforum.roblox.com/t/making-a-wall-climbing-system/502101) — forum · basics
- [Creating an advanced ledge climbing system](https://devforum.roblox.com/t/creating-an-advanced-ledge-climbing-system/2166426) — forum · ledge grab
- [Wall climbing like in Deepwoken](https://devforum.roblox.com/t/wall-climbing-system-like-in-deepwoken/2217744) — forum · RPG climbing
- [Building a climbing system](https://devforum.roblox.com/t/building-a-climbing-system/2391851) — forum · climbing
- [Parkour System Problem](https://devforum.roblox.com/t/parkour-system-problem/1511313) — forum · vault, wall run snippets
- [Knockback while ragdolled](https://devforum.roblox.com/t/any-ideas-how-i-can-apply-a-knockback-while-ragdolled/3417740) — forum · impulses
- [Knockback Ragdoll](https://devforum.roblox.com/t/how-do-i-make-a-knockback-ragdoll/1667243) — forum · basics
- [R6 Ragdoll and Knockback](https://devforum.roblox.com/t/r6-ragdoll-and-knockback-after-enemy-character-is-hit/2490075) — forum · R6
- [Knockback ragdoll for a combat system](https://devforum.roblox.com/t/how-would-i-make-a-knockback-ragdoll-for-a-combat-system/2049791) — forum · combat
- [Proper knockback for a combat system](https://devforum.roblox.com/t/how-to-make-proper-knockback-for-a-combat-system/3936670) — forum · knockback
- [Ragdoll knockback only working for NPCs](https://devforum.roblox.com/t/ragdoll-knockback-only-working-for-npcs-and-not-players/3432025) — forum · network ownership
- [FPS Tools Using ViewModels](https://devforum.roblox.com/t/fps-tools-using-viewmodels-tutorial-with-working-adsr6r15-compatible/1000436) — tutorial · viewmodel ADS
- [The First Person Element Of A First Person Shooter](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) — tutorial · viewmodel arms
- [Animating fps viewmodel arms](https://devforum.roblox.com/t/animating-fps-viewmodel-arms/1122319) — forum · arm animation
- [Where to start with gun animations](https://devforum.roblox.com/t/where-to-start-with-gun-animations-and-stuff/1762787) — forum · gun animation start
- [My First Gun System (viewmodel)](https://devforum.roblox.com/t/my-first-gun-system-with-settings-tutorial-viewmodel/1941354) — tutorial · gun system
- [Is it possible to change default sit animation on driver seat](https://devforum.roblox.com/t/is-it-possible-to-change-default-sit-animation-on-driver-seat/1912784) — forum · seats
- [Animatable vehicle seat](https://devforum.roblox.com/t/animatable-vehicle-seat/3323239) — forum · vehicles
- [How to change sitting animation](https://devforum.roblox.com/t/how-to-change-sitting-animation/1555722) — forum · sit
- [Trying to make a more smooth fishing rod cast](https://devforum.roblox.com/t/trying-to-make-a-more-smooth-fishing-rod-cast/2431891) — forum · cast arc
- [Fishing Rod Bending Animation](https://devforum.roblox.com/t/fishing-rod-bending-animation/2907289) — forum · skinned rod
- [How Do I Make Fishing Rod Like Fisch?](https://devforum.roblox.com/t/how-do-i-make-fishing-rod-like-fisch/3640179) — forum · Fisch style
- [Animating a character for a Fishing activity](https://devforum.roblox.com/t/how-would-i-go-about-animating-a-character-for-a-fishing-activity/309606) — forum · hold pose
- [How do I make a custom holding animation?](https://devforum.roblox.com/t/how-do-i-make-a-custom-holding-animation/1879888) — forum · tool hold
- [Tool grip not paired with animation](https://devforum.roblox.com/t/tool-grip-not-paired-with-animation/2863895) — forum · grip C0
- [How to make player hold tool with both hands](https://devforum.roblox.com/t/how-to-make-player-hold-tool-with-both-hands/1632084) — forum · two-handed
- [Animated tool's grip by plugin](https://devforum.roblox.com/t/animated-tools-grip-by-plugin/4822055) — community · grip plugin
- [Mixamo animations](https://devforum.roblox.com/t/mixamo-animations/3093038) — forum · Mixamo pipeline
- [How can I import Mixamo animations into roblox?](https://devforum.roblox.com/t/how-can-i-import-mixamo-animations-into-roblox/3090345) — forum · Mixamo import
- [Moon Animator 2](https://devforum.roblox.com/t/moon-animator-2/1653708) — community · plugin release thread
- [Frame animation function built around Moon Animator 2](https://devforum.roblox.com/t/frame-animation-function-built-around-moon-animator-2/4214289) — community · runtime playback of MA2 data

## YouTube — Moon Animator

- [Moon Animator 2 Basics - Official Tutorial](https://www.youtube.com/watch?v=q8tGNMo_jHg) — video · install, R6 rig, first keyframes
- [Introduction to Moon Animator 2 (2026 Basics Guide)](https://www.youtube.com/watch?v=BDJbGU0X5Us) — video · recent basics
- [Moon Animator 2 Beginners Guide](https://www.youtube.com/watch?v=dFPuaH_C_Hs) — video · basics
- [Moon Animator Basics](https://www.youtube.com/watch?v=Uuz_aETFQS8) — video · rigs, keybinds, easing, camera
- [Basic Moon Animator Tutorial](https://www.youtube.com/watch?v=TLIoHPl2Ips) — video · basics
- [How to Use Moon Animator 2 (old)](https://www.youtube.com/watch?v=ih1bz41mHEE) — video · older walkthrough
- [How to use Moon Animator 2](https://www.youtube.com/watch?v=5n3EKo5OBi8) — video · walkthrough
- [Moon Animator 2 For COMPLETE NOOBS](https://www.youtube.com/watch?v=_W3MD44MRZc) — video · beginner
- [The Basics of Moon Animator 2](https://www.youtube.com/watch?v=Fp-dIUb1Hps) — video · basics
- [Moon Animator 2 Beginner Tutorial](https://www.youtube.com/watch?v=f97UqEea0iw) — video · beginner
- [Export Moon Animator animation to Roblox (Nilo)](https://nilo.io/articles/export-moon-animator-animation-roblox) — article · Export Rig and Export All

## YouTube — Eclipse Animator

- [How To Make A Walk Cycle In Roblox (Eclipse Animator)](https://www.youtube.com/watch?v=5jHijSVX7pE) — video · contact poses
- [How To Make a Walk Cycle With Eclipse Animator (2026)](https://www.youtube.com/watch?v=qzcQTBjgZ74) — video · walk cycle
- [Roblox Walk Cycle Animation Tutorial: Eclipse Animator (2026)](https://www.youtube.com/watch?v=jgnj9Ul52jo) — video · walk cycle
- [Eclipse Animator - Beginner's Guide (2026)](https://www.youtube.com/watch?v=3pL2B30uU4c) — video · basics
- [I Tried Animating in Roblox Studio for the First Time (Eclipse)](https://www.youtube.com/watch?v=Pk_ETEMVRlg) — video · first impressions
- [How to Animate IMPACT FRAMES](https://www.youtube.com/watch?v=549Bk_To56g) — video · impact frames in Eclipse
- [How to install Eclipse Animator](https://www.youtube.com/watch?v=WHxJbD4lQak) — video · install
- [DAY 1: Learning Animate in Eclipse Animator](https://www.youtube.com/shorts/OLsHJBgH8HQ) — short · series start
- [Eclipse Animator Full Guide (Roonby)](https://roonby.com/2026/10/17/eclipse-animator-full-guide-how-to-install-and-use-it-in-roblox-studio/amp/) — article · features overview
- [Eclipse Animator MCP (Glama)](https://glama.ai/mcp/servers/VuxSussy/Eclipse-Animator-MCP) — third-party · AI to Eclipse bridge
- [Eclipse Animator Discord listing](https://discord.com/servers/eclipse-animator-1453567930234048707) — community · server page

## YouTube — walk, idle, crouch, climb

- [How to Animate WALK CYCLES](https://www.youtube.com/watch?v=kFEhiaKdaiw) — video · walk theory
- [Advanced R6 Walk Animation Tutorial](https://www.youtube.com/watch?v=hAUEJA7MrN8) — video · R6 walk
- [Custom Walk Animation (Beginner Guide)](https://www.youtube.com/watch?v=NmcezZuoYA8) — video · custom walk
- [Walking Animation (Walk Cycle Polish)](https://www.youtube.com/watch?v=t7uRzpv4XvU) — video · polish
- [Create a Custom Walk Animation](https://www.youtube.com/watch?v=olHImEJzRBo) — video · load for players
- [Moon Animator Simple Walk Cycle](https://www.youtube.com/watch?v=MPYNxYPLoGU) — video · MA2 walk
- [Walk and Jump Animation in Roblox](https://www.youtube.com/watch?v=9gi21mVQDB8) — video · walk and jump
- [R6 Walk cycle Tutorial Prisma3D](https://www.youtube.com/watch?v=o0zundBj8mU) — video · R6 walk
- [Breathing Idle (Moon Suite)](https://www.youtube.com/watch?v=L0WrqRMptsw) — video · breathing
- [Idle Animation for Beginners](https://www.youtube.com/watch?v=726DR6i-TU0) — video · idle
- [Create Custom Idle Animation](https://www.youtube.com/watch?v=TQEcjaqNsp8) — video · idle
- [Idle Animation in Roblox Studio (2025)](https://www.youtube.com/watch?v=9kej5WGAh44) — video · idle
- [Simple Idle Animation (Blender)](https://www.youtube.com/watch?v=zuezZCaxsCU) — video · Blender idle
- [Breathing NPC](https://www.youtube.com/watch?v=OYRfqLudXe0) — video · breathing NPC
- [Animate a character breathing](https://www.youtube.com/watch?v=ydHj4o_8TKA) — video · easing tips
- [Idle and Idle Moving animation with a tool](https://www.youtube.com/watch?v=BfYWlHRS55g) — video · tool idle
- [Custom Idle Animation in Roblox Studio](https://www.youtube.com/watch?v=Qm9tuFEkpB0) — video · idle
- [C to Crouch Script](https://www.youtube.com/watch?v=1KwempvbNxM) — video · crouch
- [How to make Crouch Animation](https://www.youtube.com/watch?v=wpWIhWCSRzI) — video · crouch
- [Crouch animation in Roblox Studio](https://www.youtube.com/watch?v=WEhBxoyfZoE) — video · crouch
- [C to Crouch System](https://www.youtube.com/watch?v=q7JMHe7epqY) — video · toggle
- [Crouch, Sprint and Crawl](https://www.youtube.com/watch?v=7KuoiVEDeog) — video · stance set
- [Crouch Animation tutorial (R15)](https://www.youtube.com/watch?v=HQ0COjyLXX8) — video · R15
- [Crouch animation (Fast)](https://www.youtube.com/watch?v=erLoNoLccic) — video · quick
- [Crouch/Crawl Script Tutorial](https://www.youtube.com/watch?v=EF9FMP06cWY) — video · crawl
- [Crouch script in Roblox](https://www.youtube.com/watch?v=ItVexZKClMI) — video · crouch
- [Crouch Button (PC and Mobile)](https://www.youtube.com/watch?v=WnzlLYu4n1Q) — video · mobile input
- [How to Make Wall Climbing](https://www.youtube.com/watch?v=cjVJZMCmdQs) — video · wall climb
- [Advanced Climbing System](https://www.youtube.com/watch?v=71qZXj_h3Do) — video · climbing
- [How to Wall-Climb](https://www.youtube.com/watch?v=RwHrB9tofPo) — video · wall climb

## YouTube — principles, combat, guns, fishing

- [FLIPACLIP Lesson 03 Squash and Stretch, Anticipation](https://www.youtube.com/watch?v=eD8DhrXxYJs) — video · principles
- [How to Animate Squash and Stretch](https://www.youtube.com/watch?v=r17Csq0V6ok) — video · principle
- [12 Principles: Squash and Stretch](https://www.youtube.com/watch?v=jhoHv71M66Y) — video · principle
- [Squash and Stretch for Beginners](https://www.youtube.com/watch?v=67yzmKdDF5w) — video · principle
- [M1 combat like The Strongest Battlegrounds](https://www.youtube.com/watch?v=am6kv3dBos4) — video · M1 system
- [M1 Combat in Roblox Studio 2024](https://www.youtube.com/watch?v=TCJ2HgaQb7k) — video · M1
- [How To Make an M1 System](https://www.youtube.com/watch?v=8sdPq9mDLfE) — video · M1
- [Combat System M1 Combo + Downslam + Uppercut](https://www.youtube.com/watch?v=FNBT99Ra54A) — video · combo finishers
- [Add M1 Combat to a Tool](https://www.youtube.com/watch?v=ZhLvaXFOgt4) — video · tool M1
- [Combat System: M1s](https://www.youtube.com/watch?v=sw1TiHiqiIs) — video · M1
- [Combat System: Stun](https://www.youtube.com/watch?v=izjD5vDg-aI) — video · stun
- [Advanced Combat System Part 1](https://www.youtube.com/watch?v=CG_kfH4QJ7w) — video · combat
- [Combat System in Roblox Studio](https://www.youtube.com/watch?v=AX3rWUj5gRo) — video · combat
- [ADVANCED COMBAT System Full Tutorial](https://www.youtube.com/watch?v=r-c1aCp5RNg) — video · combat
- [How to Make a Gun ViewModel](https://www.youtube.com/watch?v=ZWy_bkw1pL4) — video · viewmodel
- [FE Gun Kit Viewmodel (DoomsDev)](https://www.youtube.com/watch?v=etATAnYhQaM) — video · FPS kit
- [FE Gun Kit Viewmodel, create your own FPS](https://www.youtube.com/watch?v=dV_6xYO2vy4) — video · FPS kit
- [Double Mag Reload Animation](https://www.youtube.com/watch?v=HqzW8OD8s-c) — video · reload anim
- [Creating a Fishing Rod System (old)](https://www.youtube.com/watch?v=wr_uPT8Vn7M) — video · rod system
- [Fisch Tutorial: How to cast your rod](https://www.youtube.com/watch?v=NrPdbFZf_RM) — video · Fisch cast
- [Perfect casting in Fisch](https://www.youtube.com/watch?v=uOm_rNnj4Lw) — video · Fisch gameplay
- [How To Cast A Fishing Rod](https://www.youtube.com/watch?v=h9cUCzI2DJ8) — video · cast
- [Fishing rod guide, Steal an Egg](https://www.youtube.com/watch?v=DMo7kFVYZ0s) — video · game reference

## YouTube — Blender, Mixamo, cutscenes

- [Import Blender Animations Into Roblox R6 AND R15 Rigs (2026)](https://www.youtube.com/watch?v=X140xvLc_Rs) — video · add-on pair
- [How To Make Roblox Animation In Blender](https://www.youtube.com/watch?v=SFVrOP50hy0) — video · export/import
- [Mixamo Animations Into Roblox Using Blender 2.79](https://www.youtube.com/watch?v=WmASW9cgnLE) — video · Mixamo
- [Roblox Animation in Blender: Full Beginner Guide (2026)](https://www.youtube.com/watch?v=eg6COxaPCyo) — video · beginner
- [Animate Roblox Characters in Blender (2026)](https://www.youtube.com/watch?v=WI6adMt2aUY) — video · beginner
- [Animate Rigs in Blender for Roblox Studio](https://www.youtube.com/watch?v=y8bfOqLtvwc) — video · rig
- [Import Roblox Characters into Blender (2026)](https://www.youtube.com/watch?v=8lG-tkyAGoQ) — video · import rig
- [Roblox Blender Animation Guide 2025](https://www.youtube.com/watch?v=SI3P10yJcTY) — video · plugin link
- [Animating Avatar In Blender 2024](https://www.youtube.com/watch?v=HtvHrEFCTL0) — video · avatar
- [Cascadeur to Roblox](https://www.youtube.com/watch?v=WQRzvZGmJjo) — video · Cascadeur
- [Cascadeur Roblox animation tutorial page](https://cascadeur.com/tutor/robloxanimation) — vendor · Cascadeur export
- [Animate Your Roblox Avatar with Mixamo (2025)](https://www.youtube.com/watch?v=5fA4OeWIo6Y) — video · Mixamo
- [Export Mixamo Animations into Roblox Studio](https://www.youtube.com/watch?v=rplF-mKRX2A) — video · Mixamo
- [Mixamo animation tutorial (Blender 2.8-2.9+)](https://www.youtube.com/watch?v=vNQ2F96BRPc) — video · Mixamo
- [Custom NPC with Mixamo animation](https://www.youtube.com/watch?v=fZyjs5YgISY) — video · NPC
- [Roblox Studio + Mixamo Tutorial](https://www.youtube.com/watch?v=TNxh-uXNkWE) — video · Mixamo
- [Roblox studio Mixamo animations](https://www.youtube.com/watch?v=Vjp_zKj3uk8) — video · Mixamo
- [Transfer Mixamo Animations to Rigify](https://www.youtube.com/watch?v=nIYrwC85w9k) — video · retarget
- [Roblox Cutscene Script Tutorial](https://www.youtube.com/watch?v=A3JFj7ugqKg) — video · script cutscene
- [How to Make a Cutscene in Roblox Studio (Easy)](https://www.youtube.com/watch?v=XMlc5d7OKj4) — video · easy
- [Camera Manipulation (Spectate and Cutscenes) #32](https://www.youtube.com/watch?v=FhCNvyuZ-mE) — video · advanced scripting
- [Cutscene Camera (Camera Interpolation)](https://www.youtube.com/watch?v=DQ0FbFJ0IU8) — video · interpolation
- [Menu/Intro Camera Scene](https://www.youtube.com/watch?v=Js6BJDHsNy4) — video · menu camera
- [Easy Cutscene in Roblox Studio](https://www.youtube.com/watch?v=EzsMjxL6hAU) — video · easy
- [Cutscene in Roblox Studio 2026](https://www.youtube.com/watch?v=HEZgUK4-C18) — video · animation + camera
- [CUTSCENE in ROBLOX STUDIO Easy](https://www.youtube.com/watch?v=Qkkydch_Kdg) — video · easy
- [Como Fazer Cutscene no Roblox Studio](https://www.youtube.com/watch?v=e6uBJ5o0-CE) — video · Portuguese
- [Code a Cutscene with different Camera Angles](https://www.youtube.com/watch?v=-f5zy0U9vD8) — video · angles

## Game context pages

- [Dress To Impress guide (SteelSeries)](https://steelseries.com/blog/how-to-play-dress-to-impress) — article · runway flow
- [10 Best Poses in Dress to Impress (Beebom)](https://beebom.com/best-poses-dress-to-impress/) — article · pose list
- [Pose 28 (Know Your Meme)](https://knowyourmeme.com/memes/pose-28-in-dress-to-impress-roblox-game) — article · pose meme
- [DTI Equip Walks (Deltias Gaming)](https://deltiasgaming.com/?p=214162) — article · walk animations
- [Skill Builder V2 in TSB (allthings.how)](https://allthings.how/skill-builder-v2-in-the-strongest-battlegrounds-how-it-works/) — article · custom moves
- [TSB The Strongest Hero guide (Sportskeeda)](https://sportskeeda.com/roblox-news/the-strongest-battlegrounds-the-strongest-hero-guide) — article · cutscene grab ult


## Visual study

- [[Animation Poses and Timing Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[Animation MOC]] · [[00 Home]]
