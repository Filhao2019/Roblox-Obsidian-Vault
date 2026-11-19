---
title: Figma Workflow for Roblox UI
date: 2026-11-19
tags: [ui, figma, workflow, ai-agent, mcp]
status: researched
---

# Figma Workflow for Roblox UI

How to design Roblox UI in Figma, move it into Studio without losing responsiveness, and drive Figma with an AI agent through the official Figma MCP server. The style briefs [[Cartoony UI Figma Guide]] and [[Stud UI Figma Guide]] say *what* to draw; this note says *how* to set up the file, export it and verify it. Plugin lists and older tips live in [[UI Tools Plugins and Kits]]; layout rules in [[Mobile Console and Responsive UI]].

## 1. Set up the Figma file

- **Frames.** One 1920 × 1080 desktop reference frame per screen, plus a phone-landscape frame. The desktop frame is a reference canvas, not a promise that pixel sizes fit every device.
- **Structure.** Page → one frame per screen → named containers (`Header`, `Content`, `Footer`, `LeftButtons`). No loose absolute-positioned layers except true overlays such as badges.
- **Auto layout** wherever content can grow (lists, grids, buttons with labels). It maps to `UIListLayout`, `UIGridLayout` and `UIPadding`. Resize the frame in Figma to test it before handoff.
- **Components and variants** for every repeated element: button `Default / Hover / Pressed / Disabled`, card rarity, toggle on/off. Use component properties for label text, icon swap and boolean layers.
- **Variables as design tokens.** Colour, number (spacing, radius, stroke width, extrusion offset, font size) and string variables in collections. Use modes for Desktop/Mobile or theme variants. Alias semantic tokens (`button/primary/face`) to primitives (`green/500`). Modes per collection depend on the Figma plan.
- **Layer names** are semantic and match the Roblox instance names you want (`ShopButton`, `FrontFace`, `BackExtrusion`, `StudTexture`). `Group 5` produces poor agent and importer output.
- **Live text.** Keep text as text layers, never outlined, so font, size and localization stay editable.
- **Guides.** Draw a safe-area margin: keep about 36 px at the top clear if the ScreenGui keeps default insets (unverified exact value), and keep the lower phone corners free for the thumbstick and jump button.
- **Annotations** (Dev Mode) for behaviour the visuals cannot show: tween timings, toggle states, what a button opens.

## 2. Translate Figma to Roblox

| Figma | Roblox | Rule |
|---|---|---|
| Frame size/position | `UDim2` Scale | Panels and layout: divide by the 1920 × 1080 parent. |
| Icons, strokes, radius, text size | `UDim2` Offset / pixels | Keep pixel precision where stretching distorts art. |
| Fixed aspect art | `UIAspectRatioConstraint` | Every card, icon and button whose art must not stretch. |
| Global size knob | `UIScale` | Multiplies a subtree; good for a "UI size" setting. |
| Min/max size | `UISizeConstraint` | Stops panels becoming tiny on phones or huge on 4K. |
| Centre / right alignment | `AnchorPoint` | Write the anchor in the layer name or an annotation. |
| Auto layout | `UIListLayout` / `UIGridLayout` + `UIPadding` | Layer order becomes `LayoutOrder`. |
| Corner radius | `UICorner` | Native, crisp, scales. |
| Stroke | `UIStroke` | Pixel thickness by default; `StrokeSizingMode` ScaledSize ties text strokes to font size. Two strokes on one text object give text outline + box border. Do not tween `Thickness` on text. |
| Gradient fill | `UIGradient` | Colour/transparency sequences, `Rotation`, `Offset`. A `UIGradient` under a `UIStroke` gives a gradient outline. |
| Safe area | `ScreenGui.ScreenInsets` | `CoreUISafeInsets` keeps UI below the top bar; check `GuiService:GetInsetArea` (search result; confirm on the reference page). |

Pick one Scale/Offset convention per project and write it down. Community threads disagree; the hybrid rule above is the one Roblox's own tips thread describes.

## 3. Export assets

- **Native first.** Simple corners, strokes and gradients are rebuilt with `UICorner`, `UIStroke` and `UIGradient`, not baked. They stay editable and resolution-independent.
- **Bake only what Roblox cannot draw**: halftones, stud textures, sunbursts, bevels, scalloped edges, heavy blur or layered soft shadows. Export those layers alone, never the text or the clickable control.
- **PNG, not SVG.** `ImageLabel` needs an uploaded raster image. SVG is only useful for editing or importers that convert shapes.
- **Size.** Export at 1×–2× the final on-screen size. Keep each image ≤ 1024 px on its long side as a safe convention (unverified as a hard UI limit; the official 1024 figure is for 3D textures). Crop tight: transparent padding shifts positions.
- **9-slice** for frames that resize: export a small source (≈ 64–128 px) with a flat centre, set `ScaleType = Slice`, set `SliceCenter` in source pixels and tune `SliceScale`. The Studio 9-Slice Editor shows edge offsets, which differ from the `SliceCenter` numbers. Keep drop shadows in a separate image so they are not sliced wrongly.
- **Moderation.** Every uploaded image is moderated; patterned textures sometimes get false positives and can be appealed.
- **Fonts.** Studio cannot upload font files. Design with families Roblox ships (Builder Sans, Montserrat as the Gotham stand-in, Luckiest Guy for cartoony titles) and re-check the [Font datatype](https://create.roblox.com/docs/reference/engine/datatypes/Font) list. Anything else must be baked, losing editability and localization.

## 4. Importer plugins (all third-party)

Treat imports as a first draft. Imported UI is usually Offset-heavy and needs a Scale pass, effects are approximated and fonts only survive if Roblox ships them.

- **UILint** — Figma + Studio plugin pair, imports the hierarchy and uploads images; free tier with limits; closed-source service needing an account.
- **FigBloxUI** — ZIP (no login), Code and Live modes, Offset/Scaled toggle. Licence and pricing unconfirmed.
- **Figma Importer Assistant v2** — free; "opportunistic" mode converts text, strokes, colours and auto layout.
- **Kekui** — free plugin accompanying Kek's importing masterclass, with Ultra Scale and 9-slice helpers.
- **Figblox** — open-source codegen to Luau (search result; licence unverified). Others seen only in search: Bloxporter (paid), Framewisp, GuiForge (unverified maturity).

After any import, audit: Scale vs Offset, `AnchorPoint`, aspect constraints, `ZIndex` / `LayoutOrder`, and that decorative images do not block clicks. Review third-party plugins with [[Third Party Asset Intake Review]] before installing.

## 5. Driving Figma with an AI agent (Figma MCP)

**Servers.** Remote (`https://mcp.figma.com/mcp`, no desktop app, broadest features, recommended) or desktop (through the Figma desktop app, needs a Dev or Full seat).

**Read tools.** `get_design_context` (structured design, web-oriented by default), `get_metadata` (light outline of IDs, names, sizes — use on big files first), `get_variable_defs` (tokens used), `get_screenshot`, `search_design_system`, `get_code_connect_map`, `get_figjam`.

**Write tools.** `use_figma` (runs Plugin API JavaScript: pages, frames, components, variants, variables, styles, text, images), `create_new_file`, `upload_assets`, `generate_figma_design`, `html_to_figma`, `generate_diagram`.

**Rules an agent should follow:**

1. Load Figma's `figma-use` skill before any `use_figma` call. Start every file task with `create_session` and reuse the session ID.
2. Read before writing: `search_design_system` and `get_variable_defs`, then reuse existing components and tokens instead of inventing new ones.
3. Create variables and collections first, then frames that bind to them.
4. Build in small steps — one component or section per call. Large selections slow down, truncate or fail.
5. Use auto layout. Inside auto layout, writing `x`/`y` does nothing; set `FILL` sizing only after the node is parented to an auto-layout frame (search result; verify).
6. Name every layer for its Roblox instance.
7. **Verify visually after every write**: `get_screenshot` of the frame, `get_metadata` for structure, `get_variable_defs` for bindings. A successful tool return is not visual proof.
8. When reading for Studio, ask explicitly for Luau/Roblox output: "Scale for layout, Offset for icons and strokes, `UIAspectRatioConstraint` on art, `UIStroke`/`UIGradient`/`UICorner` natively." `get_design_context` defaults to React + Tailwind and must be translated.
9. Brief the agent like a teammate: which file and node, which tokens to reuse, where code goes, and the acceptance check.

**Limits and failure modes.** Starter plans and View/Collab seats get about six read calls a month; Dev/Full seats follow REST Tier 1 per-minute limits; write tools are exempt from read limits (Figma may change these). Missing fonts, oversized context, sizing set before parenting, unnamed layers and no Code Connect mapping (so the agent guesses components) are the usual causes of bad output. Code Connect targets mainstream frameworks; Luau support is unconfirmed, so keep a written mapping of Figma components to your Luau UI kit instead (unverified).

## 6. Agent checklist

- [ ] Tokens defined as variables (colour, radius, stroke, extrusion, spacing, font size).
- [ ] One master component per control, with state variants.
- [ ] Layer names match planned Roblox instances.
- [ ] Desktop and phone frames both checked by resizing.
- [ ] Only non-native decoration exported, as tight PNGs ≤ 1024 px; frames that resize use 9-slice.
- [ ] Fonts exist in Roblox's list.
- [ ] After import or rebuild: Scale/Offset audit, safe insets, touch targets, screenshots on desktop and phone ([[Device and Multiplayer Test Plan]]).

## Videos

- [The Greatest Cartoony UI Tutorial on Roblox (w/ Figma)](https://www.youtube.com/watch?v=z16zs2v-FNI) — Kek · YouTube · layered cartoony panels and cards; basis of [[Cartoony UI Figma Guide]]
- [The Greatest Stud UI Tutorial on Roblox (w/ Figma)](https://www.youtube.com/watch?v=gnIKtS3nUqo) — Kek · YouTube · stud-texture HUD buttons; basis of [[Stud UI Figma Guide]]
- [Simple Tutorial for Cartoony UI using FIGMA (Roblox)](https://www.youtube.com/watch?v=HTkaJZnojuw) — Shiro · YouTube · short beginner walkthrough
- [How To Make Simulator UI Buttons In Figma | Roblox UI Tutorial](https://www.youtube.com/watch?v=k69tudey-vs) — voidryxUI · YouTube · simulator-style buttons
- [How to Design Custom Roblox Shop UI (Figma to Studio)](https://www.youtube.com/watch?v=F8w-vTQ71fE) — MrCrabDev · YouTube · shop design plus Studio import
- [How To Make Your GUIs Look "Good"](https://www.youtube.com/watch?v=4rF3BdMYmjY) — Stuffy Dev · YouTube · native UICorner/UIStroke/UIGradient without Figma
- [FigBloxUI — Figma to Roblox UI in Seconds](https://www.youtube.com/watch?v=JbFUMvAtGug) — Ananchai.m · YouTube · FigBloxUI import demo
- [How to Import UI from Figma to Roblox Studio (2026 Integrated Experience)](https://www.youtube.com/watch?v=5Kia4YuAVCI) — YouTube · import walkthrough (creator unverified)
- [How To Import Uis With Bloxporter!](https://www.youtube.com/watch?v=zil8NfIcofM) — YouTube · paid Bloxporter workflow (creator unverified)
- [A Guide to Auto Layout: Best Practices, Tips & Tricks](https://www.youtube.com/watch?v=1odqpkfkDL8) — YouTube · auto layout habits (Figma channel unverified)
- [Getting started with the Figma MCP server](https://www.youtube.com/watch?v=brTAdHVCwSw) — YouTube · MCP setup and code-to-canvas (Figma channel unverified)
- [How to Choose and Set Up the Remote or Desktop Figma MCP Server](https://www.youtube.com/watch?v=c2z5Bg52yCg) — YouTube · remote vs desktop server (unverified)
- [Figma webinar: From Claude Code to Figma and Back Again](https://www.figma.com/webinars/claude-code-cs/) — Figma webinar · round-trip agent workflow (search result)

## References

- [UI 9-slice design](https://create.roblox.com/docs/ui/9-slice) — official docs · ScaleType Slice, SliceCenter, 9-Slice Editor
- [Size modifiers and constraints](https://create.roblox.com/docs/ui/size-modifiers) — official docs · UIScale, UIAspectRatioConstraint, UISizeConstraint
- [UI appearance modifiers](https://create.roblox.com/docs/ui/appearance-modifiers.md) — official docs · UIStroke, UIGradient, UICorner
- [ImageLabel reference](https://create.roblox.com/docs/reference/engine/classes/ImageLabel) — API reference · Image, ScaleType, SliceScale
- [ScreenGui.ScreenInsets](https://create.roblox.com/docs/reference/engine/classes/ScreenGui/ScreenInsets) — API reference · safe-area insets
- [Font datatype](https://create.roblox.com/docs/reference/engine/datatypes/Font) — API reference · font families Roblox ships
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) — official docs · the 1024 × 1024 texture ceiling (3D)
- [Designing UI - Tips and Best Practices](https://devforum.roblox.com/t/designing-ui-tips-and-best-practices/3074034) — DevForum · Scale vs Offset, aspect ratio, safe area, mobile controls
- [Importing UI from Figma with proper scaling](https://devforum.roblox.com/t/importing-ui-from-figma-with-proper-scaling/2995956) — DevForum · the scaling problem after import
- [Roblox UI Importing Masterclass (w/ Free Plugin)](https://devforum.roblox.com/t/extremely-detailed-roblox-ui-importing-masterclass-w-free-plugin/4619363) — DevForum · Kek's course outline and Kekui plugin
- [Figma Importer Assistant v2](https://devforum.roblox.com/t/v2-release-figma-importer-assistant-a-free-and-faster-way-to-create-your-ui/2961561) — DevForum · free importer
- [UILint v2: Import Figma UI into Roblox Studio](https://devforum.roblox.com/t/plugin-uilint-v2-import-figma-ui-into-roblox-studio/4765869) — DevForum · plugin thread (search result)
- [Introducing Builder Font + Deprecating Gotham and Arial](https://devforum.roblox.com/t/introducing-builder-font-deprecating-gotham-and-arial/2868222) — DevForum announcement · font changes
- [UILint: Figma to Roblox](https://uilint.dev/figma-to-roblox) — vendor docs · Figma-to-Roblox mapping table
- [FigBloxUI Getting Started](https://figbloxui.dev/getting-started/) — vendor docs · import modes and moderation notes
- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559) — Figma help center · remote vs desktop
- [Tools and example prompts](https://help.figma.com/hc/en-us/articles/42495147242903) — Figma help center · tool list and prompts
- [Figma skills for MCP](https://help.figma.com/hc/en-us/articles/39166810751895) — Figma help center · figma-use and other skills
- [Figma MCP server docs](https://developers.figma.com/docs/figma-mcp-server/) — developer docs · official reference and rate limits
- [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) — Figma GitHub · setup, best practices, rules template
- [Guide to variables in Figma](https://help.figma.com/hc/en-us/articles/15145852043927-Guide-to-variables-in-Figma) — Figma help center · variables, collections, modes (search result)

Links: [[UI MOC]] · [[UI Tools Plugins and Kits]] · [[Cartoony UI Figma Guide]] · [[Stud UI Figma Guide]] · [[00 Home]]
