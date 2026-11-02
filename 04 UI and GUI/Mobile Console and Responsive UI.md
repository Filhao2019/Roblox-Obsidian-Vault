---
title: Mobile Console and Responsive UI
date: 2026-11-02
tags: [ui, mobile, console, responsive]
status: researched
---

# Mobile Console and Responsive UI

Make one UI work on phone, tablet, desktop and gamepad. Code helper: [[UI Implementation in Luau]]. Design context: [[UI Design Principles for Roblox]].

## Scale vs Offset
- **Scale** = fraction of the parent; **Offset** = fixed pixels. Use Scale for layout and large panels, Offset for tiny fixed things such as stroke thickness or icon padding. Docs: [position and size](https://create.roblox.com/docs/en-us/ui/position-and-size.md).
- `UIAspectRatioConstraint` locks width:height so a Scale-sized object does not stretch; default 1:1 is ideal for square icons. When a layout (e.g. UIListLayout) and the constraint both control an object, the constraint wins on size ([reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UIAspectRatioConstraint.md)).
- `UIScale` multiplies the parent's AbsoluteSize and scales children including UIStroke and UICorner ([size modifiers](https://create.roblox.com/docs/en-us/ui/size-modifiers)). Typical trick: design at 1920x1080 and set UIScale = min(viewportX/1920, viewportY/1080).
- `UITextSizeConstraint` keeps TextScaled text between limits ([reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UITextSizeConstraint.md)).
- Plugins can convert Offset to Scale ([AutoScale Plus](https://devforum.roblox.com/t/plugin-autoscale-plus-for-guis/601773), [Offset to Scale](https://devforum.roblox.com/t/plugin-offset-to-scale/2563623)); see [[UI Tools Plugins and Kits]]. Reports say conversion can misbehave inside ScrollingFrames.

## Safe areas
`ScreenGui.ScreenInsets` offers None, DeviceSafeInsets (avoids cutouts), CoreUISafeInsets (avoids cutouts and top-bar core UI; for buttons and status) and TopbarSafeInsets (dynamic remaining top bar space) ([ScreenInsets](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md), [mirror](https://robloxapi.github.io/ref/enum/ScreenInsets.html)). Default to CoreUISafeInsets for HUD; use None only for background art.

## Touch
- Minimum interactive size about 44x44 px with spacing (community heuristic; Apple/Google figures cited are 44 pt/48 dp) ([RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement)).
- Roblox default mobile controls take the bottom-left and bottom-right; keep custom buttons clear of those zones ([docs](https://create.roblox.com/docs/en-us/ui/position-and-size.md)).
- Prefer bottom sheets, icons with short labels, and shallow menus.
- Show only vital info during active gameplay; move the rest into menus.
- Detect device with `UserInputService` and swap layouts (touch vs keyboard vs gamepad).

## Gamepad / console
- Set `SelectionGroup = true` on containers to control navigation; `SelectionBehavior` Escape vs Stop decides whether focus can leave the group. Manual `NextSelectionUp/Down/Left/Right` for grids, then set `GuiService.SelectedObject` ([GuiObject](https://create.roblox.com/docs/en-us/reference/engine/classes/GuiObject)).
- `GuiBase2d.SelectionChanged` lets you restyle the focused item ([GuiBase2d](https://create.roblox.com/docs/reference/engine/classes/GuiBase2d)).
- Show a clear focus ring (UIStroke highlight) and gamepad glyph hints; TV-safe margins for text.

## Test matrix
Phone portrait/landscape (small), tablet, 1080p desktop, ultra-wide, console with controller. Use Studio's device emulator. Re-check HUD of [[Rivals]] style shooters where mobile buttons overlap.

## References
- [Position and size UI objects](https://create.roblox.com/docs/en-us/ui/position-and-size.md) — official docs · Scale/Offset, thumb zones
- [Position and size (alt path)](https://create.roblox.com/docs/ui/position-and-size.md) — official docs · same page
- [Size modifiers and constraints](https://create.roblox.com/docs/en-us/ui/size-modifiers) — official docs · UIScale, constraints
- [UIAspectRatioConstraint](https://create.roblox.com/docs/en-us/reference/engine/classes/UIAspectRatioConstraint.md) — official docs · aspect ratio
- [UITextSizeConstraint](https://create.roblox.com/docs/en-us/reference/engine/classes/UITextSizeConstraint.md) — official docs · text limits
- [ScreenInsets enum](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md) — official docs · modes
- [ScreenInsets (non-md path)](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets) — official docs · same enum
- [ScreenInsets (robloxapi)](https://robloxapi.github.io/ref/enum/ScreenInsets.html) — API mirror · enum
- [GuiObject reference](https://create.roblox.com/docs/en-us/reference/engine/classes/GuiObject) — official docs · selection properties
- [GuiBase2d reference](https://create.roblox.com/docs/reference/engine/classes/GuiBase2d) — official docs · SelectionChanged
- [Mobile-first design for Roblox engagement](https://rolearn.dev/insights/mobile-first-design-roblox-engagement) — article · touch guidance
- [Roblox UI/UX skill notes](https://skills.sh/taozhuo/game-dev-skills/ui-ux) — community page · heuristic sizes
- [How to make UI scaling](https://devforum.roblox.com/t/how-to-make-ui-scaling/1069492) — DevForum · scaling basics
- [UI Scaling issue help](https://devforum.roblox.com/t/ui-scaling-issue-help-please/3654432/1) — DevForum · common mistakes
- [AutoScale Plus for GUIs](https://devforum.roblox.com/t/plugin-autoscale-plus-for-guis/601773) — plugin thread · offset to scale
- [Offset to Scale plugin](https://devforum.roblox.com/t/plugin-offset-to-scale/2563623) — plugin thread · conversion

Links: [[UI MOC]] · [[00 Home]]
