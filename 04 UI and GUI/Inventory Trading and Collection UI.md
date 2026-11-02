---
title: Inventory Trading and Collection UI
date: 2026-11-02
tags: [ui, inventory, trading, index]
status: researched
---

# Inventory Trading and Collection UI

Patterns for grids of owned things, trade windows, and discovery books. Games: [[Adopt Me]], [[Pet Simulator 99]], [[Blox Fruits]], [[Steal a Brainrot]], [[Murder Mystery 2]], [[Sols RNG]]. Backend: [[Trading Systems]].

## Inventory grid
- `ScrollingFrame` + `UIGridLayout` with fixed square cells; use `AutomaticCanvasSize` so the canvas grows with content ([UIGridLayout](https://create.roblox.com/docs/en-us/reference/engine/classes/UIGridLayout.md)).
- Card = rarity-coloured background, item icon or ViewportFrame, quantity badge bottom-right, equipped tick top-left, new-item dot.
- Sort/filter bar above: rarity, newest, favourites, search box.
- Selection opens a side or bottom detail panel (name, stats, actions: equip, lock, sell, trade).
- Multi-select/mass-delete with a confirm popup; lock icon prevents accidental sells.

## 3D previews
Pets and fruits are often shown as 3D via ViewportFrame so no per-item icon is needed ([release post](https://devforum.roblox.com/t/viewportframe-release/206476), [pictures of models thread](https://devforum.roblox.com/t/getting-pictures-of-models/264570)). Limits: fixed lighting, no particles inside; cache a snapshot or reuse one viewport for the detail panel. Code in [[UI Implementation in Luau]].

## Collection index
A book/codex of every possible item with undiscovered entries shown as dark silhouettes and a progress counter (x/total). Completing pages grants rewards. `UIPageLayout` gives page-turn behaviour with `Next()`/`Previous()` ([UIPageLayout](https://create.roblox.com/docs/en-us/reference/engine/classes/UIPageLayout.md)).

## Variant badges
Adopt Me uses age/variant treatments: Neon pets glow on certain body parts, Mega Neons cycle rainbow colours ([Neon Hawk](https://adoptme.fandom.com/wiki/File:Neon_Hawk.png), [Mega Neon Goat](https://adoptme.fandom.com/wiki/File:Mega_Neon_Goat.png)). In UI, mirror this with an animated gradient border (see [[UI Animation and Juice]]). PS99 has Golden/Rainbow/Shiny transforms per its update post ([update 61](https://www.biggames.io/post/pet-simulator-99-update-61)).

## Trade window
1. Two halves: "Your offer" and "Their offer", each a small grid.
2. Add items from your inventory panel by click/drag.
3. Both players press Accept; any change resets acceptance; a short countdown before final confirm prevents scams.
4. Show value hints cautiously: community value lists exist for Blox Fruits ([value list](https://www.sportskeeda.com/roblox-news/blox-fruits-value-list)) but in-game values are player-driven.

## Gamepad
Use `SelectionGroup` and the `NextSelection*` properties so grids are navigable with a controller ([GuiObject reference](https://create.roblox.com/docs/en-us/reference/engine/classes/GuiObject)); see [[Mobile Console and Responsive UI]].

## Pitfalls
- Don't rebuild all cards on every change; pool and update.
- Rarity colour must be readable on the card background ([[Color Typography and Iconography]]).
- Handle 1000+ items with virtualised lists if needed `(unverified)` best practice.

## References
- [UIGridLayout reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UIGridLayout.md) — official docs · cell layout
- [UIPageLayout reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UIPageLayout.md) — official docs · paging
- [GuiObject reference](https://create.roblox.com/docs/en-us/reference/engine/classes/GuiObject) — official docs · selection properties
- [GuiObject LayoutOrder](https://create.roblox.com/docs/reference/engine/classes/GuiObject/LayoutOrder) — official docs · sorting items
- [ViewportFrame Release](https://devforum.roblox.com/t/viewportframe-release/206476) — DevForum announcement · 3D in GUI
- [Getting pictures of models](https://devforum.roblox.com/t/getting-pictures-of-models/264570) — DevForum · pet-picker previews
- [Inventory [NEED HELP]](https://devforum.roblox.com/t/inventory-need-help/1687198/29) — DevForum · custom inventory discussion
- [Neon Hawk file](https://adoptme.fandom.com/wiki/File:Neon_Hawk.png) — wiki · neon visual
- [Mega Neon Goat file](https://adoptme.fandom.com/wiki/File:Mega_Neon_Goat.png) — wiki · mega visual
- [Adopt Me Bunny](https://adoptme.fandom.com/wiki/Bunny) — wiki · pet card info
- [Adopt Me Punk Pony](https://adoptme.fandom.com/wiki/Punk_Pony) — wiki · pet card info
- [10 rarest pets in Adopt Me](https://esports.gg/news/roblox/10-rarest-pets-adopt-me/) — guide · trade-driven rarity
- [PS99 update 61](https://www.biggames.io/post/pet-simulator-99-update-61) — studio post · pet variants
- [Blox Fruits value list](https://www.sportskeeda.com/roblox-news/blox-fruits-value-list) — guide · trade values
- [All brainrots database](https://rblxguide.com/games/steal-a-brainrot/brainrots) — database · index-style listing

Links: [[UI MOC]] · [[00 Home]]
