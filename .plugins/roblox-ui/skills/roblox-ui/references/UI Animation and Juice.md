---
title: UI Animation and Juice
date: 2026-11-02
tags: [ui, animation, tween, juice]
status: researched
---

# UI Animation and Juice

The feel layer: tweens, springs, count-ups, shine sweeps. Implementation: [[UI Implementation in Luau]]. World-space animation lives in [[Animation Principles for Roblox]] and effects in [[Reward and Rarity VFX]].

## Easing cheat sheet
Roblox easing styles include Back (slightly overshoots then settles), Bounce (bounces after reaching target) and Elastic (rubber-band overshoot) per the docs ([EasingStyle](https://create.roblox.com/docs/en-us/reference/engine/enums/EasingStyle.md)). Graphs on that page show the In direction; Out reverses it.

| Moment | Style / Direction | Time |
|---|---|---|
| Popup open | Back Out | 0.25-0.35 s |
| Popup close | Quad In | 0.15-0.2 s |
| Button hover | Quad Out | 0.1 s |
| Button press | Quad Out, scale 0.92 | 0.06 s |
| Release | Back Out to 1.05 then 1 | 0.15 s |
| Reward pop | Elastic Out | 0.5-0.8 s |
| Count-up | Quart Out | 0.4-0.8 s |
| Slide-in toast | Quint Out | 0.3 s |

## Recipes
- **Hover/press scale:** add a `UIScale` child and tween it; do not tween Size (breaks layouts).
- **Number count-up:** tween a `NumberValue` and write formatted text on Changed ([[HUD and Currency Displays]]).
- **Shine sweep:** a white diagonal `UIGradient` with a transparency sequence, tween `Offset` from (-1,0) to (1,0) on a loop ([gradient animation tutorial](https://devforum.roblox.com/t/uigradient-animation/2637300), [4 UIGradient animations](https://devforum.roblox.com/t/4-uigradient-animations-including-rainbow/557922)).
- **Rainbow / rotating border:** put a UIGradient inside a white UIStroke and tween its `Rotation` ([forum](https://devforum.roblox.com/t/how-to-add-a-uigradient-into-a-gui-border/1783385)).
- **Idle wobble:** low-amplitude sine on Rotation for call-to-action buttons.
- **Particles in UI:** there is no UI particle emitter; fake it with pooled ImageLabels, or animate gradient offsets; for 3D use a ViewportFrame (no particles inside it per the release notes: [post](https://devforum.roblox.com/t/viewportframe-release/206476)). A request for a successor tech is discussed in [CameraView Frame](https://devforum.roblox.com/t/cameraview-frame/4614500).
- **Springs:** libraries give physically based motion — Fusion exposes tween and spring objects, Vide has `spring()` ([Fusion docs](https://elttob.uk/Fusion/0.1/), [Vide](https://github.com/centau/vide)). See [[UI Tools Plugins and Kits]].
- **ViewportFrame pets:** slowly rotate the model on Heartbeat, bob on a sine.

## Signature moments
[[Pet Simulator 99]] egg rattle then pop; [[Sols RNG]] roll build-up scaled to rarity; [[Fisch]] reel bar following the fish; [[Steal a Brainrot]] ticking cash numbers; [[Dress To Impress]] runway star ratings.

## Performance
Limit looping tweens to visible UI; stop them when the frame is hidden. Pool toast objects. Prefer `UIScale`/`Position`/`Transparency` tweens; avoid per-frame text re-layout.

## References
- [EasingStyle (Creator Docs)](https://create.roblox.com/docs/en-us/reference/engine/enums/EasingStyle.md) — official docs · Back/Bounce/Elastic descriptions
- [EasingStyle (Creator Docs, alt)](https://create.roblox.com/docs/reference/engine/enums/EasingStyle.md) — official docs · same enum
- [EasingStyle (legacy)](https://developer.roblox.com/en-us/api-reference/enum/EasingStyle) — legacy docs · enum values
- [Understanding easing styles](https://devforum.roblox.com/t/understanding-easing-styles/937281) — DevForum · visual explanation
- [Custom tweening](https://devforum.roblox.com/t/custom-tweening/3897708) — DevForum · own tween functions
- [UIGradient animation](https://devforum.roblox.com/t/uigradient-animation/2637300) — DevForum tutorial · offset tweens
- [4 UIGradient Animations (Including Rainbow!)](https://devforum.roblox.com/t/4-uigradient-animations-including-rainbow/557922) — DevForum tutorial · shine/hover/rainbow
- [ezVisualz](https://devforum.roblox.com/t/ezvisualz-uigradient-and-uistroke-effects-made-easy/2470313) — DevForum resource · gradient/stroke effect presets
- [ezVisualz page 3](https://devforum.roblox.com/t/ezvisualz-uigradient-and-uistroke-effects-made-easy/2470313?page=3) — DevForum · usage Q&A
- [Interface Tween Help](https://devforum.roblox.com/t/interface-tween-help/1819020) — DevForum · bouncy clicks with Fusion tween
- [Fusion 0.1 docs](https://elttob.uk/Fusion/0.1/) — library docs · tween/spring state
- [centau/vide](https://github.com/centau/vide) — library · spring() and reactive UI
- [ViewportFrame Release](https://devforum.roblox.com/t/viewportframe-release/206476) — DevForum · limits of 3D in UI
- [CameraView Frame](https://devforum.roblox.com/t/cameraview-frame/4614500) — DevForum proposal · successor ideas
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — official docs · UIGradient Offset/Rotation


## Visual study

- [[UI Layout and Motion Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[UI MOC]] · [[00 Home]]
