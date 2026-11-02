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
