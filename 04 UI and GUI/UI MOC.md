---
title: UI MOC
date: 2026-11-02
tags: [ui, moc, index]
status: researched
---

# UI MOC

Map of content for `04 UI and GUI/`. Start with [[Roblox Top 30 UI Study 2026-11-19]] and [[Roblox Top 50 UI Study Ranks 31-50 2026-11-19]] for gameplay captures and [[Roblox UI Patterns from the Top 30]] to turn the observations into an original interface.

## Notes
- [[Roblox Top 30 UI Study 2026-11-19]] — 30 linked gameplay screens, with layout, proportional size, color and a design takeaway per game
- [[Roblox UI Patterns from the Top 30]] — comparisons by player task, a brief workflow and a Hollow Grand example
- [[Roblox Top 50 UI Study Ranks 31-50 2026-11-19]] — 20 more chart games (ranks 31–50 and next titles), same per-screen format
- [[Figma Workflow for Roblox UI]] — Figma file setup, Figma-to-Roblox translation table, asset export, importers, AI agent + Figma MCP rules, videos
- [[Cartoony UI Figma Guide]] — layered-stroke cartoony menus, rarity cards, halftones (Kek tutorial brief)
- [[Stud UI Figma Guide]] — tactile stud-texture HUD buttons, currency counter, toggles (Kek tutorial brief)
- [[UI Breakdown of Top Games]] — per-game HUD, buttons, palette, fonts, menus, signature moments (all 27 chart games)
- [[UI Design Principles for Roblox]] — strokes, gradients, hierarchy, consistency, contrast
- [[HUD and Currency Displays]] — layout zones, currency pills, number suffixes, cooldowns
- [[Shop and Monetization UI]] — store layouts, offers, MarketplaceService hooks
- [[Inventory Trading and Collection UI]] — grids, trade windows, index books, ViewportFrame previews
- [[Notifications Popups and Rewards]] — toasts, modals, blur, reward reveals
- [[Color Typography and Iconography]] — rarity colour table, fonts, icon rules
- [[UI Animation and Juice]] — easing, springs, count-up, shine sweeps
- [[Mobile Console and Responsive UI]] — Scale vs Offset, constraints, safe areas, gamepad
- [[Device and Multiplayer Test Plan]] · [[Playtest Record]] — actual device/emulator, input and scenario evidence; blank checks stay pending
- [[UI Implementation in Luau]] — typed, untested components (button, counter, popup, toasts, shop grid, rarity frame, responsive, pet preview)
- [[UI Tools Plugins and Kits]] — Figma workflow, plugins, Fusion / Vide / React Lua
- [[UI References]] — categorized link library

## Related areas
[[Game Design MOC]] · [[Games MOC]] · [[UI Sounds]] · [[Reward and Rarity VFX]] · [[Animation Implementation in Luau]] · [[Audio Implementation in Luau]]

## Read order for an agent building a UI
1. [[Roblox UI Patterns from the Top 30]], [[Roblox Top 30 UI Study 2026-11-19]] and [[Roblox Top 50 UI Study Ranks 31-50 2026-11-19]] (pick and open references by player task)
2. [[Figma Workflow for Roblox UI]] plus a style brief ([[Cartoony UI Figma Guide]] or [[Stud UI Figma Guide]]) when designing in Figma
3. [[UI Design Principles for Roblox]]
4. Relevant pattern note (HUD, shop, inventory, popups)
5. [[Mobile Console and Responsive UI]] before building
6. [[UI Implementation in Luau]] to scaffold, [[UI Animation and Juice]] to polish

## Honest limits
The November 2 breakdown has visual details marked `(unverified)`. The November 19 study records what was visible in published gameplay captures and gives approximate frame proportions. See [[UI References]] for older source gaps.

## References
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — official docs · UIStroke/UIGradient/UICorner
- [Size modifiers and constraints](https://create.roblox.com/docs/en-us/ui/size-modifiers) — official docs · UIScale and constraints
- [Position and size UI objects](https://create.roblox.com/docs/en-us/ui/position-and-size.md) — official docs · layout and mobile zones
- [The Ultimate UI Design Guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916) — DevForum tutorial · design workflow
- [UI Design Guide](https://devforum.roblox.com/t/ui-design-guide/2975811) — DevForum tutorial · Figma to Studio
- [UIGridLayout reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UIGridLayout.md) — official docs · grid layouts for shops and inventories


## Visual study

- [[UI Layout and Motion Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


## Reference implementation brief

- [[UI Build Brief]] — original task frame, deliverables and acceptance checks.
- [[Roblox AI External Library]] — broader online visual categories.


Links: [[00 Home]]
