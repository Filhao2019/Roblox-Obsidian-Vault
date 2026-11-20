---
title: Roblox UI Patterns from the Top 30
date: 2026-11-19
tags: [ui, visual-reference, roblox, design-workflow]
status: researched
---

# Roblox UI Patterns from the Top 30

Pick references by what the player is trying to do. The [[Roblox Top 30 UI Study 2026-11-19]] has a linked capture, approximate footprint and palette for each of the 30 games in the November 19 chart snapshot.

## Choose references by player task

| Player task | Compare these screens | Adapt for your own game |
| --- | --- | --- |
| Read the match state while aiming or moving | [[Roblox Top 30 UI Study 2026-11-19#8. RIVALS\|RIVALS]] · [[Roblox Top 30 UI Study 2026-11-19#6. 99 Nights in the Forest\|99 Nights in the Forest]] · [[Roblox Top 30 UI Study 2026-11-19#22. Dandy's World\|Dandy's World]] · [[Roblox Top 30 UI Study 2026-11-19#28. Forsaken\|Forsaken]] | Give the one shared objective or clock a stable position. Move local resources and tools to edges, and test them over the brightest and darkest backgrounds. |
| Browse, equip or compare items | [[Roblox Top 30 UI Study 2026-11-19#2. Adopt Me!\|Adopt Me!]] · [[Roblox Top 30 UI Study 2026-11-19#5. Brookhaven RP\|Brookhaven RP]] · [[Roblox Top 30 UI Study 2026-11-19#18. Catalog Avatar Creator\|Catalog Avatar Creator]] | Give categories and items distinct zones. Preserve a preview area for the avatar or object. Design selected, locked and empty states before polishing thumbnails. |
| Choose a class, raid or activity | [[Roblox Top 30 UI Study 2026-11-19#23. Attack on Titan Revolution\|Attack on Titan Revolution]] · [[Roblox Top 30 UI Study 2026-11-19#12. Anime Crusaders X\|Anime Crusaders X]] · [[Roblox Top 30 UI Study 2026-11-19#13. Hyper Realistic Ragdoll\|Hyper Realistic Ragdoll]] | Put the selected item's requirements, reward or next unlock beside its action. Group advanced details below the first decision. |
| Follow or claim a quest | [[Roblox Top 30 UI Study 2026-11-19#10. Fish It!\|Fish It!]] · [[Roblox Top 30 UI Study 2026-11-19#15. Pet Simulator 99!\|Pet Simulator 99!]] · [[Roblox Top 30 UI Study 2026-11-19#17. Tap Simulator REBORN\|Tap Simulator REBORN]] · [[Roblox Top 30 UI Study 2026-11-19#29. Ant Evolution\|Ant Evolution]] | Make the current count, target and reward scan together. Show claimability as a separate state and keep longer lists in a dedicated panel. |
| React to a short-lived state | [[Roblox Top 30 UI Study 2026-11-19#11. Murder Mystery 2\|Murder Mystery 2]] · [[Roblox Top 30 UI Study 2026-11-19#16. Fisch\|Fisch]] · [[Roblox Top 30 UI Study 2026-11-19#20. Sol's RNG\|Sol's RNG]] · [[Roblox Top 30 UI Study 2026-11-19#25. Evade\|Evade]] | Use a temporary banner, target or result for the event. Give it one priority message, and let it yield its space when the event ends. |
| Learn a control or interact with a prop | [[Roblox Top 30 UI Study 2026-11-19#7. Break and Steal an Egg\|Break and Steal an Egg]] · [[Roblox Top 30 UI Study 2026-11-19#13. Hyper Realistic Ragdoll\|Hyper Realistic Ragdoll]] · [[Roblox Top 30 UI Study 2026-11-19#26. MALAM SAMA OPAH\|MALAM SAMA OPAH]] | Pair a short verb with the input glyph and put the prompt close to the relevant action. Remove coaching once the player learns it. |

## Translate the evidence into a brief

1. **Name the player decision.** “Choose a class before entering the queue” is specific enough to design and test. List the information that makes the choice possible.
2. **Open two or three captures from the table.** Cite the game, screen and capture. Pick one layout relationship and one useful state transition. If you only have a still, label the timing as an implementation proposal.
3. **Set original visual roles.** Describe the reading surface, primary action, quiet actions and warning state. Choose typography and materials from the game's world. Specify a label, shape or icon anywhere a color carries meaning.
4. **Set a responsive size budget in the prototype.** Start with the content and available screen space. Record the rendered footprint, text size and hit area at your actual desktop and phone viewports. Compare with the capture's proportions to understand density. Use the Creator Hub size guidance to choose constraints and anchoring. [Position and size UI objects](https://create.roblox.com/docs/ui/position-and-size) · [Size modifiers and constraints](https://create.roblox.com/docs/ui/size-modifiers)
5. **Check the full interaction.** Capture default, focused or selected, disabled or locked, and error or success where applicable. Test touch reach, gamepad focus, long labels, and bright and dark backgrounds. Open the screen with no prior explanation and state what the next action is. [Roblox accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility)

## Pre-game lobby example

For a pre-game class shop, use the raid screen's separation of choices and details, and the catalog screen's unobstructed preview. Keep the class name, cost, unlock requirement and current action together. On a narrow screen, trial a scrollable list that opens a class detail view with a visible back control. The quest board can borrow Dandy's World’s clear objective count and Fish It!'s aligned rewards, with locked, in-progress and claimable states visible in the prototype. Use your game's own fonts, icons and materials.

**Review prompt for Claude or Codex.** “Open the relevant captures from this note. For each capture, point to the specific layout or state you are adapting. Design an original screen for the stated player task. Show what changes on phone, how an unavailable action is communicated, and where the player returns after closing it. Call out any behavior inferred from a still.”

## References

- [[Roblox Top 30 UI Study 2026-11-19]] — source frames, approximate measurements and per-game observations.
- [[UI Design Principles for Roblox]] · [[Mobile Console and Responsive UI]] · [[UI Build Brief]] — existing vault notes for the prototype and review.
- [Roblox Creator Hub overview of UI](https://create.roblox.com/docs/ui/position-and-size) — anchoring, scale and offset.

Links: [[UI MOC]] · [[00 Home]]
