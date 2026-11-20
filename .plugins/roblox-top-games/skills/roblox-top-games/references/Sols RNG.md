---
title: Sols RNG
date: 2026-11-02
tags: [game, rng, incremental, simulator]
status: researched
roblox_url: https://www.roblox.com/games/15532962292
universe_id: 5361032378
studio: Sol's Studio
genre: Simulation / Incremental Simulator (RNG)
created: 2023-12-03
---

# Sols RNG

A luck game: press Roll, receive an "aura" (a cosmetic glow/effect around your avatar) with odds from roughly 1 in 2 to billions, and use potions, gear and the server's rotating biome to bias future rolls. The roll itself is the whole interaction; the game spends its budget on presentation of rare outcomes (cutscenes, server-wide announcements) and on a deep luck-math meta layer. It has run as a live-service for ~3 years with numbered "Eons". Learn from it: rarity spectacle, the gambler's dopamine loop, and a community-facing math layer (luck calculators).

| Stat (2026-11-02) | Value |
|---|---|
| Playing | 41,579 |
| Visits | 2.27B |
| Favorites | 1.03M |
| Like ratio | 91.4% |
| Max server size | 20 |

## Core gameplay loop
- **Minute-to-minute:** click Roll (or auto-roll), see the aura, equip it. Total luck combines base luck, bonus rolls, special luck and VIP (per a fan wiki). Potions give temporary luck/speed; gear (45 listed) is crafted from auras and potions.
- **Session loop:** wait for or trigger a biome (23 listed), roll aggressively during its boosted window, craft, complete quests (e.g. the Halloween "Jack the Pumpkin" bounty quests).
- **Long-term loop:** chase named auras (514 per one wiki; 11 rarity tiers from Basic to Transcendent) and the multi-billion-to-one trophies; new "Eon" content adds auras and biomes.

## Why it went viral
- The universal appeal of "rolling for rare"; every rare roll is a shareable clip.
- Server-wide announcements make rare rolls social events: others in the server see the notification.
- Biome events (rare spawn odds like 1 in 30,000 Glitched) create "everyone drop what you're doing" moments.
- Regular Eon updates and free private servers (the description advertises them) reduce lag and farm friction.
- Reported to be among the highest-earning Simulation experiences (RoWatcher estimate; modelled, treat as rough).

## Progression and retention
- Aura rarity ladder with named tiers up to Transcendent; era/Eon system; biome-exclusive auras (e.g. Glitch, a Challenged-tier aura at roughly 1 in 12.2M in the Glitched biome per one guide).
- Biomes: Windy, Snowy, Rainy (frequent), Sandstorm, Hell, Starfall, Heaven, Corruption, Lost Forest, Glitched, Dreamspace, Cyberspace, Singularity; spawn odds from 1/500 per second to 1/3.5M (per Bloxodes).
- Codes (potion chests) and daily/weekly seasonal events (Halloween 2026: Eon 1-31 added 17 auras and brought back Graveyard and Pumpkin Moon biomes).

## Monetization
- VIP and Robux luck products, auto-roll style conveniences, potions; free private servers as a retention perk.
- Probability products are the center of gravity (patterns only; see [[Monetization Patterns]]).

## Art direction and 3D assets
- Simple low-fidelity island hub with a minimal avatar, because the aura VFX is the art. Biomes retint the whole world: snowy turns the map white, rainy adds gray fog, Starfall a dark blue sky with falling stars, Heaven a golden sky, Hell red energy, Glitched shows error textures and scrambled trees, Dreamspace is pastel, Lost Forest has giant green trees and rising lights, Cyberspace is a digital grid. → [[Art Styles of Top Games]]

## UI and GUI
- Central Roll button, current aura card with name and rarity ("1 in X") text, inventory of auras, gear/potion tabs, luck stat display. Rarity text color follows tier (unverified exact palette). → [[UI Breakdown of Top Games]]

## Animation
- Rare auras take over the screen: the game plays a cutscene when you roll a high-tier aura (camera push-in, vignette, name reveal) and may announce it server-wide (general pattern; details unverified). → [[Cutscenes and Camera Work]]

## SFX and music
- Different stingers per rarity tier and a tension build before the reveal; each biome has its own ambience and music (unverified details; the Bloxodes biome page lists no audio). → [[SFX of Top Games]]

## VFX
- Auras are particle/mesh effects that surround the character: swirling light, glitch shatters, lightning, flame, etc. Higher tiers add screen-wide effects, lighting changes and sky tint. → [[Reward and Rarity VFX]] · [[VFX of Top Games]]

## Systems and code worth studying
- Weighted random with luck multipliers and biome-conditional tables; server-side roll resolution with server-wide events; global biome timer shared across the server; offline-safe aura inventory; calculator-friendly math (the wiki publishes a rolls-to-aura calculator). → [[Pet Egg and Gacha Systems]] · [[Coding MOC]]

## Lessons to steal (patterns, not content)
- Make the rare outcome a show, not a number: sky tint, cutscene and server broadcast.
- Use time-boxed global biomes to pool all players at the same moment.
- Publish odds clearly; players love computing them and will build content around it.
- Layer modifiers (potions, gear, VIP, biome) so there is always a new reason to roll.
- Version content as numbered Eons for clear live-ops cadence.
- Keep the hub tiny and cheap; invest in effects only where the dopamine lives.

## References
- [Sol's RNG on Roblox](https://www.roblox.com/games/15532962292) — official page · description, feature list
- [Sol's RNG Wiki (RBLXGuide)](https://rblxguide.com/games/sols-rng) — fan wiki mirror · auras, tiers, gear, Halloween 2026 update
- [Sol's RNG biomes (Bloxodes)](https://bloxodes.com/wiki/sols-rng/biomes) — fan wiki · biome visuals and odds
- [Sol's RNG auras (Bloxodes)](https://bloxodes.com/wiki/sols-rng/auras) — fan wiki · aura list
- [Glitch aura (RBLXGuide)](https://rblxguide.com/games/sols-rng/auras/glitch) — fan wiki · rarity example
- [Fault aura (RBLXGuide)](https://rblxguide.com/games/sols-rng/auras/fault) — fan wiki · biome aura example
- [Sol's RNG on RoWatcher](https://rowatcher.com/games/5361032378) — tracker · update history, Eon labels
- [Sol's RNG gameplay (Destructoid)](https://destructoid.com/how-to-get-poseidons-aura-in-sols-rng) — news/guide · aura acquisition
- [Sol's RNG codes (Deltias Gaming)](https://deltiasgaming.com/?p=394312) — guide · code cadence
- [Sol's RNG wiki (TechWiser)](https://techwiser.com/roblox-sols-rng-wiki/) — guide
- [All aura showcase (ItemLevel)](https://itemlevel.net/sols-rng-all-aura-showcase) — showcase list

Links: [[Games MOC]] · [[Top Games Chart 2026-11-02]] · [[00 Home]]
