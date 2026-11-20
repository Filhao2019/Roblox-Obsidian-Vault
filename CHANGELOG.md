# Changelog

## v2.5.0 — Brainrot Games and Voxel Models — 2026-11-20

- Added Brainrot Games Roundup, comparing Steal a Brainrot, Grow a Garden, Steal An Egg, Escape Tsunami for Brainrots and Plants vs Brainrots. It covers their loops, rarity × mutation systems, timers and lessons.
- Expanded the Steal a Brainrot profile from a stub to a full profile.
- Added Brainrot and Simulator UI Patterns. It covers the income-per-second HUD, conveyor, base lock and restock timers, and an original rarity and mutation colour ladder, with a typed Luau overhead unit tag and number abbreviator (untested in Studio).
- Added Voxel and Brainrot Model Style, which compares the voxel, Part-built and low-poly routes. It covers style rules, a tool chooser and the pipeline into Roblox. Its Blender 5.1 script turns a voxel grid into one merged, palette-textured GLB. The script ran headless and its self-check passed; the GLB has not yet been imported into Studio. The original example model (render + GLB) is in `_Media/Voxel/`.
- New plugin `voxel-models` bundles these notes with LihFolk's voxel deep dive.
- `build_plugins.py` now copies the Roblox CC BY licence only next to Roblox docs media.

## v2.4.0 — Claude Code plugins — 2026-11-20

- The repo is now a Claude Code plugin marketplace (`roblox-obsidian-vault`) with ten topic plugins, each holding one skill and copies of its notes: `cartoony-ui`, `horror-ui`, `roblox-ui`, `roblox-top-games`, `roblox-game-design`, `roblox-3d-models`, `roblox-animation`, `roblox-audio`, `roblox-vfx` and `roblox-coding`.
- `_tools/build_plugins.py` generates `.plugins/` and `.claude-plugin/marketplace.json` from the notes. Images embedded by notes are copied; videos are not.
- CI rebuilds the plugins and fails if the committed copies are out of date. `vault.py` skips `.plugins/`.

## v2.3.0 — UI and Model Reference Boards — 2026-11-20

- Added five visual boards with 1135 in-game screenshots collected from Fandom wikis: cartoony UI (282, led by Pet Simulator 99), horror UI (209, led by Forsaken), Fisch islands and props (180), towns, islands and buildings (315) and horror rooms and props (149).
- Each image has a caption and a link to its wiki file page. Sources, sizes and checksums are in `_Data/reference-media-2026-11-20.json`.
- Images are hotlinked from Fandom and not redistributed. A few non-Roblox games (Brawl Stars, Clash Royale, Dead by Daylight, Phasmophobia, Sea of Thieves, Animal Crossing, Genshin Impact) are included as style anchors.
- Linked the boards from the Visual References, UI and 3D MOCs and from the Fisch and Pet Simulator 99 profiles.

## v2.2.0 — Top 50 UI and Figma Workflow — 2026-11-19

- Added a companion study covering 20 more experiences from the November 19 Top Playing Now chart (ranks 31–50 plus the next uncovered titles). Entries with only store art are labelled so they are not used as HUD references.
- Added a Figma workflow guide: file setup with auto layout, components and variables; a Figma-to-Roblox translation table; asset export and 9-slice rules; third-party importers; rules for AI agents using the Figma MCP server; 13 videos.
- Added two agent-ready style briefs from Kek's Figma tutorials: cartoony layered-stroke menus and stud-texture HUD buttons.
- Linked the new notes from the UI MOC, UI References, UI Tools and the Visual References MOC.

## v2.1.0 — Roblox UI Reference Study — 2026-11-19

- Added a dated study of 30 experiences from Roblox's Top Playing Now chart. Each entry links an inspected gameplay capture or clip and records its layout, approximate screen footprint, color and a design takeaway.
- Added a UI patterns guide organized by player task, with a workflow for adapting references and an example for a pre-game class shop and quest board.
- Linked the new notes from the UI and visual reference indexes. The gameplay evidence is hosted at its original sources.

## v2.0.0 — v2: LihFolk V2 Import and Visual Boards — 2026-11-02

- Imported 1,360 notes and images from LihFolk Vault V2 (CC BY 4.0, pinned commit) into `11 LihFolk V2/`, unchanged and credited in `ABOUT THIS IMPORT.md`. This adds sections the vault lacked: anti-exploit, physics and vehicles, level design, accessibility, player QoL, thumbnails and CTR, engine reference cards, an API atlas, a bug-symptom table (`SYMPTOMS.md`) and a topic router (`ROUTER.md`).
- Security review: no exfiltration, credential access or prompt-injection instructions found. Excluded the upstream Claude plugin hook (runs a script on every edit), multi-agent council commands (high token use), Obsidian plugin, tools, rig files and benchmarks.
- Added 16 visual boards: 407 UI, 599 high-fidelity model, 200 thumbnail and 100 VFX references plus a 100-video animation library. Images are **remote embeds** from their original hosts rather than bundled files, a change from earlier releases; they need internet access and Roblox CDN links can expire.
- `_tools/vault.py check` searches the imported folder but does not hold it to this vault's metadata and link rules.

## v1.4.0 — Research and Practical Workflows — 2026-11-02

- Expanded seven stubs: persistence, networking, security, coding references, flipbooks, environmental VFX and DOORS. Added a source-scoped Pressure reference and a research coverage map.
- Embedded three existing offline images and one existing clip directly in the new VFX guidance; linked official online thumbnails in the horror profiles. No third-party game media was bundled.
- Updated coverage/status navigation; retained historical chart data and separated research, original exercises and untested implementation.

- Added four original, passive Markdown guides and four blank worksheets for feature contracts, third-party asset intake, device/multiplayer test evidence and release recovery planning.
- Linked the additions from Home, the workflow hub, troubleshooting and relevant area maps. Existing evidence conventions, runtime limitations and coding-stub statuses are preserved.
- Credited AshExplained's reviewed planning ideas at a pinned revision. No upstream skills, setup blocks, scripts, dependencies, remote embeds, automatic actions or agent-configuration changes are included.

## v1.3.0 — 2026-11-02

- Added original Python-standard-library local search, exact note/section reading and structured JSON search results with evidence status preserved.
- Added a vault checker for note metadata, wiki/file-embed targets, media path containment and SHA-256 integrity; regression tests cover errors as well as successful checks.
- Added GitHub Actions validation using pinned official actions and read-only repository permissions.
- Added an original troubleshooting index, evidence review guidelines and project evidence template, linked from Home and area maps.
- Added the missing researched status to the dated chart note; existing chart data and incomplete system notes are preserved.
- Credited LihFolk's tooling ideas without importing its code, hooks, gameplay modules, plugin or separately restricted assets. Existing 21 images and 9 videos remain included.

## v1.2.0 — 2026-11-02

- Added a pinned guide and machine-readable catalog of izzyfrm/roblox-ai's 12 visual reference collections, with independently counted files and explicit review limits.
- Added five original build briefs for environments, UI, animation/cutscenes, VFX/audio and branding/thumbnails.
- Added a reference selection worksheet and a workflow connecting inspected media to implementation and acceptance evidence.
- Linked the additions from Home, visual references and relevant area maps.
- Credited the upstream organizational inspiration without importing mixed-rights images, copied prompts or an unverified plugin package. The existing 21 offline images and 9 videos are preserved.

## v1.1.0 — 2026-11-02

- Added five visual study boards containing 21 offline images and 9 offline demonstration videos from Roblox Creator Documentation.
- Added a visual reference hub, observation workflow and reusable capture template.
- Linked visual boards from Home, area MOCs, reference libraries and relevant topic notes.
- Included per-asset provenance, pinned upstream revision, SHA-256 checksums, CC BY 4.0 license and attribution.
- Preserved the existing game research and dated chart snapshot. Studio implementation and device performance are not verified by this update.
