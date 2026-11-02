---
title: HUD and Currency Displays
date: 2026-11-02
tags: [ui, hud, currency]
status: researched
---

# HUD and Currency Displays

How top games place and format currencies, health, hotbars and minimaps. See per-game notes in [[UI Breakdown of Top Games]] and animation recipes in [[UI Animation and Juice]]; code in [[UI Implementation in Luau]].

## Layout zones
| Zone | Typical content | Notes |
|---|---|---|
| Top-left | Core Roblox menu and chat | Reserved by the engine; keep clear |
| Top-center / top-left under topbar | Primary currency stack (coins, gems) | Pill-shaped, icon at left, number right |
| Left edge column | Round shortcut buttons (Shop, Pets, Index, Settings) | 5-7 buttons, stacked vertically |
| Bottom-center | Hotbar (tools, skills, towers) | Slots with keybind numbers |
| Bottom corners | Mobile thumbstick and jump | Avoid placing UI here ([position and size](https://create.roblox.com/docs/en-us/ui/position-and-size.md)) |
| Right edge | Timers, event banners, boosts | Vertical stack of small chips |
| Center | Transient prompts, rewards | Never persistent |

## Currency pill anatomy
Icon (square, ~32-40 px) overlapping the left end of a rounded bar, number in a display font with 2-3 px stroke, optional "+" button that opens the matching shop ([[Shop and Monetization UI]]). Gains pop a floating "+1.2K" that flies toward the counter. Passive-income games like [[Steal a Brainrot]] also show a per-second rate under the total.

## Number formatting
Use suffixes: 1.2K, 3.4M, 5.6B, 7.8T, then Qa, Qi, Sx, Sp, Oc, No, Dc. Many community modules exist (FormatNumber, N2Abbreviate, NumberFormatter, UltiNum — see references); an original implementation is in [[UI Implementation in Luau]]. Keep decimals at 1-2 and trim trailing zeros. For idle/incremental games like [[Pet Simulator 99]] and [[Sols RNG]], numbers can exceed Luau double precision in practice only past 1e308, so a suffix table up to Dc is enough for most designs.

## Count-up
Tween the displayed value toward the true value over 0.25-0.6 s with Quad/Quart Out. Never block updates: if a new gain arrives mid-tween, retarget.

## Health, stamina, cooldowns
- Bars: rounded track, filled gradient, thick dark stroke; colour shifts green to red at low values.
- Cooldowns: radial or bottom-up dark overlay on the ability button with a seconds label; used in [[Jujutsu Shenanigans]], [[The Strongest Battlegrounds]], [[Forsaken]].
- Combat HUDs ([[Rivals]], [[Blade Ball]]) keep everything small and edge-aligned.

## Minimal HUDs
Horror titles ([[Doors]], [[99 Nights in the Forest]], [[Violence District]]) hide the HUD until needed. Roblox's default hotbar cannot be restyled directly; devs either hide the CoreGui backpack and build their own or accept the default ([custom hotbar thread](https://devforum.roblox.com/t/how-to-make-custom-hotbar/1661208), [style change thread](https://devforum.roblox.com/t/how-to-change-hotbar-style/2866003)).

## Rules of thumb
1. One currency visible always; show at most 3 on mobile.
2. Format on the client; replicate raw numbers.
3. Respect `ScreenInsets` so notched phones don't clip counters ([ScreenInsets](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md)).
4. Animate changes; never snap.

## References
- [FormatNumber module](https://devforum.roblox.com/t/311-formatnumber-a-module-for-formatting-numbers/527979) — DevForum resource · compact notation with configurable suffixes
- [FormatNumber universal system](https://devforum.roblox.com/t/formatnumber-%E2%80%93-universal-number-formatting-system-for-roblox/3974899) — DevForum resource · newer large-number formatter
- [Number Abbreviation](https://devforum.roblox.com/t/number-abbreviation/914140) — DevForum resource · suffix table approach
- [How do I shorten these numbers?](https://devforum.roblox.com/t/how-do-i-shorten-this-numbers/741957) — DevForum support · basics
- [Integer Formatter](https://devforum.roblox.com/t/integer-formatter/1196162) — DevForum · comma formatting
- [N2Abbreviate](https://devforum.roblox.com/t/open-source-n2abbreviate-advanced-number-abbreviate-module-very-simple-to-use/1832958) — DevForum open source · abbreviation module
- [UltiNum extended number module](https://devforum.roblox.com/t/ultinum-v10-extended-number-module/1548983) — DevForum · beyond double range
- [NumberFormatter open source](https://devforum.roblox.com/t/open-source-numberformatter-%E2%80%93-auto-format-large-numbers-in-ui-leaderstats/3774942) — DevForum · leaderstats formatting
- [Convert 1k, 1M, 1b to number](https://devforum.roblox.com/t/convert-1k-1m-1b-to-number/1505551) — DevForum · parsing suffixes back
- [How to make custom hotbar?](https://devforum.roblox.com/t/how-to-make-custom-hotbar/1661208) — DevForum · custom backpack UI
- [How to change hotbar style](https://devforum.roblox.com/t/how-to-change-hotbar-style/2866003) — DevForum · default hotbar limits
- [Custom Hotbar/HUD tool help](https://devforum.roblox.com/t/custom-hotbarhud-tool-help/261637) — DevForum · hiding CoreGui backpack
- [Position and size UI objects](https://create.roblox.com/docs/en-us/ui/position-and-size.md) — official docs · mobile control zones
- [ScreenInsets enum](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md) — official docs · safe areas
- [Steal a Brainrot rarities and prices](https://allthings.how/steal-a-brainrot-brainrots-rarities-and-prices-full-list/) — guide · cash per second examples

Links: [[UI MOC]] · [[00 Home]]
