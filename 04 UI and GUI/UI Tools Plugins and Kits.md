---
title: UI Tools Plugins and Kits
date: 2026-11-02
tags: [ui, tools, plugins, frameworks]
status: researched
---

# UI Tools Plugins and Kits

Design tools, Studio plugins and code frameworks for building Roblox UI. Pair with [[UI Implementation in Luau]] and [[Project Architecture and Frameworks]]. Plugin names below come from DevForum threads; prices, availability and compatibility change, so check each listing before relying on it.

## Design workflow (Figma / Photopea / Photoshop)
1. Sketch the screen as simple boxes first; block layout before detail ([UI design guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916)).
2. Design in Figma, using a font close to a Roblox built-in (Montserrat to Gotham pairing suggested there).
3. Export icons as white-on-transparent PNGs, recolour in Studio with `ImageColor3`.
4. Rebuild gradients, corners and glows natively with UIGradient / UICorner / UIStroke rather than baking them into images ([prototype and import guide](https://devforum.roblox.com/t/ui-design-guide/2975811)).
5. Photopea (browser) or Photoshop for icon cleanup and spritesheets; keep images power-of-two-friendly `(unverified)` best practice.
6. Read pixel values from the design with the properties panel rather than dragging.

## Studio plugins
| Plugin | Purpose | Note |
|---|---|---|
| AutoScale Lite / AutoScale Plus | Convert Offset to Scale | Users report problems inside ScrollingFrames ([thread](https://devforum.roblox.com/t/plugin-autoscale-plus-for-guis/601773)) |
| Offset to Scale | Same idea, lighter | [thread](https://devforum.roblox.com/t/plugin-offset-to-scale/2563623) |
| UI Tools (all-in-one) | Scaling options, unit conversion, UIScale handling | Described as paid; verify ([thread](https://devforum.roblox.com/t/ui-tools-the-all-in-one-interface-design-solution/2166473)) |
| ezVisualz | Preset UIGradient/UIStroke animations | Wally-installable ([thread](https://devforum.roblox.com/t/ezvisualz-uigradient-and-uistroke-effects-made-easy/2470313)) |
| FFusion | Converts Guis into Fusion code | ([thread](https://devforum.roblox.com/t/ffusion-convert-your-roblox-guis-into-fusion-components-free/4810694)) |

Not verified in this pass: "Interface Tools" as a separate plugin (the closest match found was UI Tools) and "UI Labs" — I did not find a source; confirm on the Creator Store before recommending them.

## Frameworks
- **Fusion** (Elttob): declarative, reactive state with tween and spring objects ([docs 0.1](https://elttob.uk/Fusion/0.1/), [@rbxts/fusion README](https://cdn.jsdelivr.net/npm/@rbxts/fusion@0.2.0/README.md)). Check current version on GitHub; a fork by raphtalia is described as incompatible ([fork](https://github.com/raphtalia/fusion)). A Japanese walkthrough exists ([zenn.dev](https://zenn.dev/landel_tech/articles/b4d2df33bb7480)).
- **Vide**: SolidJS-style reactive Luau library with `source`, `derive`, `effect`, `create`, `spring`; fully typed ([centau/vide](https://github.com/centau/vide), [littensy/vide](https://github.com/littensy/vide), [BarakChamo copy](https://github.com/BarakChamo/vide), [@rbxts/vide README](https://cdn.jsdelivr.net/npm/@rbxts/vide@0.6.1/README.md)).
- **React Lua**: Roblox's translation of React 17 to Luau ([roblox/react-lua](https://github.com/roblox/react-lua)); community fork [jsdotlua/react-lua](https://docsearch.algolia.com/mcp/docs/repo/jsdotlua/react-lua). For roblox-ts: [@rbxts/react by littensy](https://github.com/littensy/rbxts-react), [wad4444 version](https://github.com/wad4444/rbxts-react), [nrbx-ts wiki](https://github.com/nrbx-ts/rbxts-react/wiki), [npm package](https://classic.yarnpkg.com/en/package/@rbxts/react), [roblox-ts](https://classic.yarnpkg.com/en/package/roblox-ts). Requires roblox-ts 3.0+ per READMEs.
- **Plain Instance.new + modules** (as in [[UI Implementation in Luau]]) is enough for most simulators; adopt a framework when state-driven lists get complex.

## Kits and free assets
Creator Store UI packs, DevForum community resources and free icon sets exist; always check licence and Roblox asset moderation before use. I did not verify specific kit names in this pass, so none are listed. See [[Free and Paid Asset Sources]] for asset sourcing and [[Color Typography and Iconography]] for icon rules.

## Number and notification modules
FormatNumber ([thread](https://devforum.roblox.com/t/311-formatnumber-a-module-for-formatting-numbers/527979)), N2Abbreviate ([thread](https://devforum.roblox.com/t/open-source-n2abbreviate-advanced-number-abbreviate-module-very-simple-to-use/1832958)), Apprise ([thread](https://devforum.roblox.com/t/apprise-notification-system/1381697)), BlurUI ([thread](https://devforum.roblox.com/t/blurui-blur-your-uis/1276408)).

## References
- [The Ultimate UI Design Guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916) — DevForum tutorial · Figma workflow
- [UI Design Guide](https://devforum.roblox.com/t/ui-design-guide/2975811) — DevForum tutorial · prototype to Studio
- [AutoScale Plus for GUIs](https://devforum.roblox.com/t/plugin-autoscale-plus-for-guis/601773) — plugin thread
- [Offset to Scale plugin](https://devforum.roblox.com/t/plugin-offset-to-scale/2563623) — plugin thread
- [UI Tools all-in-one](https://devforum.roblox.com/t/ui-tools-the-all-in-one-interface-design-solution/2166473) — plugin thread
- [ezVisualz](https://devforum.roblox.com/t/ezvisualz-uigradient-and-uistroke-effects-made-easy/2470313) — resource thread
- [FFusion](https://devforum.roblox.com/t/ffusion-convert-your-roblox-guis-into-fusion-components-free/4810694) — plugin thread
- [Fusion 0.1 docs](https://elttob.uk/Fusion/0.1/) — library docs
- [raphtalia/fusion](https://github.com/raphtalia/fusion) — GitHub fork
- [@rbxts/fusion README](https://cdn.jsdelivr.net/npm/@rbxts/fusion@0.2.0/README.md) — package readme
- [Fusion walkthrough (zenn.dev)](https://zenn.dev/landel_tech/articles/b4d2df33bb7480) — blog (Japanese)
- [centau/vide](https://github.com/centau/vide) — GitHub library
- [littensy/vide](https://github.com/littensy/vide) — GitHub fork
- [BarakChamo/vide](https://github.com/BarakChamo/vide) — GitHub copy
- [@rbxts/vide README](https://cdn.jsdelivr.net/npm/@rbxts/vide@0.6.1/README.md) — package readme
- [Vide docs index](https://docsearch.algolia.com/mcp/docs/repo/centau/vide) — docs index
- [roblox/react-lua](https://github.com/roblox/react-lua) — GitHub library
- [jsdotlua/react-lua docs index](https://docsearch.algolia.com/mcp/docs/repo/jsdotlua/react-lua) — docs index
- [littensy/rbxts-react](https://github.com/littensy/rbxts-react) — GitHub bindings
- [wad4444/rbxts-react](https://github.com/wad4444/rbxts-react) — GitHub bindings
- [nrbx-ts rbxts-react wiki](https://github.com/nrbx-ts/rbxts-react/wiki) — GitHub wiki
- [@rbxts/react on npm mirror](https://classic.yarnpkg.com/en/package/@rbxts/react) — package page
- [roblox-ts on npm mirror](https://classic.yarnpkg.com/en/package/roblox-ts) — package page
- [FormatNumber](https://devforum.roblox.com/t/311-formatnumber-a-module-for-formatting-numbers/527979) — resource thread
- [N2Abbreviate](https://devforum.roblox.com/t/open-source-n2abbreviate-advanced-number-abbreviate-module-very-simple-to-use/1832958) — resource thread
- [Apprise](https://devforum.roblox.com/t/apprise-notification-system/1381697) — resource thread
- [BlurUI](https://devforum.roblox.com/t/blurui-blur-your-uis/1276408) — resource thread

Links: [[UI MOC]] · [[00 Home]]
