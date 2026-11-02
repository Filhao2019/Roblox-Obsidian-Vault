---
title: UI Design Principles for Roblox
date: 2026-11-02
tags: [ui, gui, principles, design]
status: researched
---

# UI Design Principles for Roblox

Why the interfaces of the top games feel good, distilled into rules an agent can apply. Most of this is convention shared across the chart games in [[UI Breakdown of Top Games]] rather than a documented spec, so treat the rules as strong defaults and verify against a reference game.

## 1. Thick outlines, always
Roblox gives you `UIStroke` for borders and text outlines; the docs note a stroke on text outlines the text and on other GuiObjects draws a border, with pixel `Thickness` and a `LineJoinMode` of Round, Bevel or Miter ([appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers)). Top games use 2-4 px dark strokes on buttons and 2-3 px on text so every element reads on any background. Beware: several strokes with the same ZIndex have undefined render order per the docs.

## 2. Bold saturated gradients
A vertical two-stop `UIGradient` (lighter top, deeper bottom) turns a flat colour into a "gem" button. A gradient *inside* a UIStroke gives gradient outlines; the stroke colour must be white for the gradient to show ([DevForum thread](https://devforum.roblox.com/t/how-to-add-a-uigradient-into-a-gui-border/1783385)).

## 3. Cartoon display fonts
One display face for headings and numbers, one clean face for body copy. Studio cannot load arbitrary font files, so match your design font to the nearest built-in ([UI design guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916)). See [[Color Typography and Iconography]].

## 4. Chunky, rounded shapes
Generous `UICorner` radii (often 8-16 px or full pill) and big hit areas. This also satisfies mobile touch needs: community guidance cites 44x44 px minimums ([RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement)); see [[Mobile Console and Responsive UI]].

## 5. Clear hierarchy
- One primary call-to-action per screen with the most contrast and effects (glow, shine).
- Featured items get a large header region; secondary options are smaller and muted.
- Drop shadow the entire panel to lift it off the world ([UI design guide](https://devforum.roblox.com/t/ui-design-guide/2975811)).

## 6. Rarity colour coding
Players learn one colour ladder (grey, green, blue, purple, gold, red, rainbow) and read value at a glance. Table in [[Color Typography and Iconography]]; use in [[Inventory Trading and Collection UI]].

## 7. Consistency
Same corner radius, stroke width, font, and button states everywhere. Build a small component set once ([[UI Implementation in Luau]]) instead of styling each frame by hand.

## 8. Contrast and legibility
Light text on a dark stroke, never mid-grey on mid-colour. Keep gameplay-critical HUD small and edge-aligned; large menus can dim and blur the world ([[Notifications Popups and Rewards]]).

## 9. Safe areas and scale
Use Scale-based sizing with aspect ratio constraints and respect device cutouts via `ScreenInsets` ([ScreenInsets reference](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md)). Default mobile thumb controls occupy the bottom corners, so avoid important buttons there ([position and size](https://create.roblox.com/docs/en-us/ui/position-and-size.md)).

## 10. Juice is part of clarity
Hover and press scale, count-up numbers and shine sweeps tell the player the UI heard them ([[UI Animation and Juice]]).

## 11. Match the world's tone
Kid-friendly sims go pastel and light; horror titles such as [[Doors]] go dark and minimal. Guides recommend light themes for playful UI rather than defaulting to dark ([UI guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916)).

## Quick checklist
- [ ] Every interactive element has a stroke, a corner, and a pressed state.
- [ ] Currency always visible, formatted with suffixes ([[HUD and Currency Displays]]).
- [ ] No text under 14 px equivalent on mobile.
- [ ] Rarity colours from one shared module.
- [ ] Layout tested at phone, tablet, desktop aspect ratios.

## References
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — official docs · UIStroke, UIGradient, UICorner behaviour
- [The Ultimate UI Design Guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916) — DevForum tutorial · Figma-to-Studio workflow, palettes, glow
- [UI Design Guide](https://devforum.roblox.com/t/ui-design-guide/2975811) — DevForum tutorial · prototype and import gradients/corners
- [How to add a UIGradient into a gui border](https://devforum.roblox.com/t/how-to-add-a-uigradient-into-a-gui-border/1783385) — DevForum · gradient outlines
- [How can I add a gradient outline to a UI](https://devforum.roblox.com/t/how-can-i-add-a-gradient-outline-to-a-ui/3831253) — DevForum · gradient stroke workaround
- [Working method for rounding only certain corners](https://devforum.roblox.com/t/working-method-for-rounding-only-certain-corners-on-a-ui-element-without-using-images-or-any-other-external-program/3189528) — DevForum · partial corners
- [Mobile-first design for Roblox engagement](https://rolearn.dev/insights/mobile-first-design-roblox-engagement) — article · mobile thumb zones and 44 px targets
- [Position and size UI objects](https://create.roblox.com/docs/en-us/ui/position-and-size.md) — official docs · mobile controls zones
- [ScreenInsets enum](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md) — official docs · safe areas
- [Roblox UI/UX skill notes](https://skills.sh/taozhuo/game-dev-skills/ui-ux) — community skill page · heuristic sizes (not official)

Links: [[UI MOC]] · [[00 Home]]
