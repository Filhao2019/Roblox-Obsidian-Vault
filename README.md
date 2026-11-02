# Roblox-Obsidian-Vault

An [Obsidian](https://obsidian.md) vault of references for building Roblox games with AI. It studies what the most-played Roblox games do — game design, 3D assets, UI/GUI, animation and cutscenes, SFX, VFX and code — and links every claim back to its source.

## How to use it

1. Clone the repo and open the folder as a vault in Obsidian (*Open folder as vault*).
2. Start at `00 Home.md`.
3. Point your AI agent (Claude Code, Codex, Cursor…) at the folder. `AGENTS.md` / `CLAUDE.md` tell it how to read and extend the vault.

## What's inside

| Folder | Contents |
|---|---|
| `01 Games/` | Profiles of the top 20 "Top Playing Now" games + 7 chart staples, and a dated chart snapshot |
| `02 Game Design/` | Virality, gameplay loops, retention, monetization, thumbnails, discovery, launch checklist |
| `03 3D Assets and Models/` | Low → high fidelity tiers, art styles, when to use each, Blender → Studio, budgets, sources |
| `04 UI and GUI/` | UI breakdown of every top game, principles, patterns, Luau UI components |
| `05 Animation and Cutscenes/` | Locomotion, idle/breathing, jump, crouch, combat, emotes, Moon Animator, cameras |
| `06 SFX and Audio/` | Game sounds, satisfying-sound design, tools, libraries, audio code |
| `07 VFX/` | Effects of top games, particles/beams/trails, VFX packs, textures, VFX code |
| `08 Coding/` | Architecture, data, networking, security, genre systems, open-source libraries |

## Data

Game stats come from Roblox's public APIs (`explore-api` chart sorts and `games.roblox.com`), snapshot **2026-11-02**. Raw data lives in `_Data/`.

## Notes

- References are links to their original sources; text is paraphrased. Game names and assets belong to their owners — study patterns, don't copy content.
- Luau code marked `status: untested` hasn't been run in Studio yet.

MIT License.

## Visual reference library — v1.1.0

Open `09 Visual References/Visual References MOC.md` for five study boards containing 21 local images and 9 local MP4 clips (50.4 MB). Examples cover environment art, PBR materials, UI, animation, particles, beams and spatial audio. Each includes a source link and study prompt. Obsidian plays local videos inline; other Markdown viewers may require opening the file.

Roblox documentation media is **CC BY 4.0**, separately from the vault text's MIT license. See `09 Visual References/Media Attribution and Reuse.md`, `_Media/ROBLOX-CC-BY-4.0.txt` and `_Data/visual-media-2026-11-02.json` for attribution and checksums. Use `_Templates/Visual Reference Template.md` to add your own references.

## Reference workflows — v1.2.0

Start at `10 Reference Workflows/Reference Workflows MOC.md` for five original build briefs, a selection worksheet, and a workflow for converting inspected references into Roblox tasks. `Roblox AI External Library.md` credits [izzyfrm/roblox-ai](https://github.com/izzyfrm/roblox-ai) and links its 12 categories at a reviewed revision. External images remain online and are not included or relicensed here. The reviewed upstream repository contains no plugin package; this update adds reference workflows, not a software installation.
