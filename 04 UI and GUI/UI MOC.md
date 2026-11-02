---
title: UI MOC
date: 2026-11-02
tags: [ui, moc, index]
status: researched
---

# UI MOC

Map of content for `04 UI and GUI/`: how the top Roblox games build interfaces, the patterns behind them, and original Luau code to reproduce them. Start with [[UI Breakdown of Top Games]] for evidence, then [[UI Design Principles for Roblox]] for the why.

## Notes
- [[UI Breakdown of Top Games]] — per-game HUD, buttons, palette, fonts, menus, signature moments (all 27 chart games)
- [[UI Design Principles for Roblox]] — strokes, gradients, hierarchy, consistency, contrast
- [[HUD and Currency Displays]] — layout zones, currency pills, number suffixes, cooldowns
- [[Shop and Monetization UI]] — store layouts, offers, MarketplaceService hooks
- [[Inventory Trading and Collection UI]] — grids, trade windows, index books, ViewportFrame previews
- [[Notifications Popups and Rewards]] — toasts, modals, blur, reward reveals
- [[Color Typography and Iconography]] — rarity colour table, fonts, icon rules
- [[UI Animation and Juice]] — easing, springs, count-up, shine sweeps
- [[Mobile Console and Responsive UI]] — Scale vs Offset, constraints, safe areas, gamepad
- [[UI Implementation in Luau]] — typed, untested components (button, counter, popup, toasts, shop grid, rarity frame, responsive, pet preview)
- [[UI Tools Plugins and Kits]] — Figma workflow, plugins, Fusion / Vide / React Lua
- [[UI References]] — categorized link library

## Related areas
[[Game Design MOC]] · [[Games MOC]] · [[UI Sounds]] · [[Reward and Rarity VFX]] · [[Animation Implementation in Luau]] · [[Audio Implementation in Luau]]

## Read order for an agent building a UI
1. [[UI Breakdown of Top Games]] (find the closest reference game)
2. [[UI Design Principles for Roblox]]
3. Relevant pattern note (HUD, shop, inventory, popups)
4. [[Mobile Console and Responsive UI]] before building
5. [[UI Implementation in Luau]] to scaffold, [[UI Animation and Juice]] to polish

## Honest limits
The research pass could not open screenshots, so visual specifics in the breakdown are largely marked `(unverified)`. See the gaps list inside [[UI References]].

## References
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — official docs · UIStroke/UIGradient/UICorner
- [Size modifiers and constraints](https://create.roblox.com/docs/en-us/ui/size-modifiers) — official docs · UIScale and constraints
- [Position and size UI objects](https://create.roblox.com/docs/en-us/ui/position-and-size.md) — official docs · layout and mobile zones
- [The Ultimate UI Design Guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916) — DevForum tutorial · design workflow
- [UI Design Guide](https://devforum.roblox.com/t/ui-design-guide/2975811) — DevForum tutorial · Figma to Studio
- [UIGridLayout reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UIGridLayout.md) — official docs · grid layouts for shops and inventories

Links: [[00 Home]]
