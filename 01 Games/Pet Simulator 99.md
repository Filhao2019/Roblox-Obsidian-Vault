---
title: Pet Simulator 99
date: 2026-11-02
tags: [game, pets, gacha, simulator]
status: researched
roblox_url: https://www.roblox.com/games/8737899170
universe_id: 3317771874
studio: BIG Games Pets
genre: Simulation / Incremental Simulator
created: 2022-02-05
---

# Pet Simulator 99

Pet Simulator 99 (PS99) is the successor to Pet Simulator X from BIG Games: break breakables in themed zones, collect diamonds and coins, hatch eggs for pets, and chase ever-rarer pets (Huge, Titanic, Gargantuan) through weekly events and trading. It launched on 1 December 2023 and pushes weekly updates (Saturday 5 pm GMT). Learn from it how to run an egg economy, an event calendar and a collection-as-status loop. See [[Pet Egg and Gacha Systems]] and [[Trading Systems]].

| Stat (snapshot 2026-11-02) | Value |
|---|---|
| Playing | 66,247 |
| Visits | 2,693,333,223 |
| Favorites | 2,221,226 |
| Like ratio | 94.7% |
| Max server size | 10 |

## Core gameplay loop
- Minute to minute: equip a team of pets, auto-target breakables for coins and drops, buy eggs from egg stands, hatch in bulk, equip better pets.
- Session: progress through worlds/zones (e.g. a Fantasy world with five zones added in Update 61), complete zone upgrades, run events or minigames, trade at the plaza.
- Long term: fill the collection, grow huge pets' XP, win raffles/hatch contests, farm eggs while offline (Update 61 farm: eggs grow offline and variant into Golden/Rainbow/Shiny), and maintain collection value in trading.

## Why it went viral
- Franchise carryover: BIG Games' earlier Pet Sim X audience (a "Pet Box" system let X players transfer pets), plus a launch trailer that passed 700K views within a day.
- Peaked above 400K concurrent near launch per one source (RoWatcher gives 250K as its own tracker peak; conflicting).
- Event spectacle: the Pet Games event (Jan 2025) was a Squid-Game-style 50-player minigame set (Glass Bridge, Minefield, Obby, Red Light/Green Light, Color Block, Mingle) with a Frontman-run Titanic raffle.
- Streamer/YouTuber hatching content: huge hatches are inherently clip-worthy.
- A licensed toy line from PhatMojo (sources: Toy Insider, Mammoth Times).

## Progression and retention
- Rarity ladder: Normal, Golden, Rainbow, Huge, Titanic, Gargantuan; numbers scale into the billions/quintillions.
- Weekly update with new limited pets, plus roughly biweekly named events (Pet Games, St. Patrick's, Summer Block Party, Halloween Haunted, Autumn, Winter Wonderland).
- Time Trials (Update 61): points from speed, improvement, daily streaks, up to 10 runs per day, redeemable for chests with Huge/Titanic pets.
- Hourly hatch contests, Traveling Merchant, farm sprinklers, Combine-o-Matic (merge items into Huge/Gargantuan), clan battles with prize tiers.
- Power creep deliberately devalues old pets so players keep engaging (RoWatcher notes a 40% drop for some pets after one update).

## Monetization
Patterns only:
- Game passes that sell luck: reported 200% luck for 275 Robux, Ultra Lucky 800, Magic Eggs 1,200, Huge Hunter 3,250; bundled about 8,075 Robux (RoWatcher). This is monetization on the core random event.
- Exclusive-shop eggs at around 400 Robux, rotating weekly "Forever Pack" bundles that scale price with progression.
- Limited event pets that become permanently unobtainable, which fuels trading and FOMO.
- Critics call it pay-to-win/predatory toward minors (RoWatcher, Spanish-language video essay in search). Design cautiously.

## Art direction and 3D assets
- Bright, rounded, toy-like pet models, readable at tiny scale, with colour variants (Golden gold shading, Rainbow gradient, Shiny sparkle) layered on the same mesh; zone themes change scenery, from grass to neon cities to fantasy forests. See [[Art Styles of Top Games]] and [[Characters Pets and Creatures]].

## UI and GUI
- Dense side-panel HUD: currency counters (coins, diamonds) top corner, egg purchase button over each egg with price and hatch counter (1/3/8 hatches), inventory grid with pet cards showing rarity colour and power number, quest/gift widgets, trading plaza UI with 60-second auction board. A Hotbar added in Update 61 helps mobile and console. BIG Games also says the PS99 UI was cleaned up compared with older titles (VGC/Pocket Tactics). See [[UI Breakdown of Top Games]] and [[Inventory Trading and Collection UI]].

## Animation
- Egg hatch: egg pops open, pets burst out of the shell and bounce toward the screen in a row for multi-hatch; rarer pets get a longer reveal; Gargantuan hatches trigger a server-wide cutscene (RoWatcher) (exact camera moves unverified). Pets follow with a bobbing idle and attack lunges. See [[Animation MOC]].

## SFX and music
- Rising-pitch break/collect tick sounds, a coin-cascade on drops, escalating fanfare on rarer hatches, and cheerful looping zone music (unverified details). See [[SFX of Top Games]].

## VFX
- Confetti and sparkle on hatches, rarity-coloured glow, rainbow shimmer shaders for Rainbow pets, screen-wide announcement banners for Titanic+ (unverified details). See [[VFX of Top Games]] and [[Reward and Rarity VFX]].

## Systems and code worth studying
- Weighted egg tables with luck stacking, pity-free RNG, trade escrow and an auction board, server-wide announcements for ultra rares, offline farm growth timers (store timestamps, compute on join). See [[Pet Egg and Gacha Systems]], [[Trading Systems]] and [[Data Saving and Player Profiles]].

## Lessons to steal (patterns, not content)
- Layer variants (Golden/Rainbow/Shiny) over one asset set to multiply the collection cheaply.
- A weekly ship day plus named events makes retention predictable.
- Let skill content (time trials, obstacle courses) mint rare pets so non-payers feel earnings.
- Offline growth plus mandatory online collect gives return triggers.
- Server-wide cutscenes for top rarities turn pulls into social status.
- Think twice before selling luck directly; it is what draws the criticism.

## References
- [Pet Simulator 99 on Roblox](https://www.roblox.com/games/8737899170) — official game page · stats, description
- [Pet Games update (Destructoid)](https://destructoid.com/pet-simulator-99-pet-games-update-patch-notes-new-minigames-new-event-and-more) — news · event structure, raffles
- [Update 61 Grow Rainbow Pets (BIG Games)](https://www.biggames.io/post/pet-simulator-99-update-61) — developer post · farm, Time Trials, hotbar
- [Update 10 Backrooms and limited Huge pets (Sportskeeda)](https://sportskeeda.com/roblox-news/news-pet-simulator-99-update-10-backrooms-limited-huge-pets) — news · event example
- [Update 13 Summer Obby World (Sportskeeda)](https://www.sportskeeda.com/roblox-news/news-pet-simulator-99-update-13-summer-obby-world-new-eggs) — news · obby world
- [Pet Simulator 99 patch notes (Ginx)](https://www.ginx.tv/en/pet-simulator-99-patch-notes) — news · cadence
- [Release date (Pocket Tactics)](https://www.pockettactics.com/pet-simulator-99/release-date) — news · launch facts
- [Release date and everything we know (VGC)](https://www.videogameschronicle.com/guide/pet-simulator-99-release-date-and-everything-we-know-so-far/) — news · launch features
- [BIG Games announces trailer (Progame Guides)](https://progameguides.com/roblox/big-games-announces-trailer-for-new-pet-sim-experience-roblox/) — news · trailer
- [Inside BIG Games (RoWatcher)](https://rowatcher.com/news/inside-big-games-how-pet-simulator-became-a-100m-roblox-empire) — analysis · studio history, revenue estimates
- [Pet Sim 99 monetization machine (RoWatcher)](https://rowatcher.com/news/pet-simulator-99-inside-roblox-s-most-aggressive-monetization-machine) — analysis · pass pricing, power creep
- [PS99 stats (RoWatcher)](https://rowatcher.com/games/3317771874) — tracker · update list, peaks
- [Pet Simulator 99 (Roblox Wiki)](https://roblox.fandom.com/wiki/BIG_Games_Pets/Pet_Simulator_99) — wiki · overview (seen in search)
- [PhatMojo toys (Toy Insider)](https://thetoyinsider.com/phatmojo-new-pet-simulator-toys-follow-new-game-launch/) — trade news · merch
- [PhatMojo (Mammoth Times)](https://business.mammothtimes.com/mammothtimes/news/read/43777771/phatmojo) — trade news · merch
- [Video essay on monetization (VideoHighlight, Spanish)](https://videohighlight.com/v/eMOLxs9NrTQ) — video summary · criticism

Note: I did not find a BIG Games / Preston public talk. Hatch animation details are inferred; verify in-game.

Links: [[Games MOC]] · [[Top Games Chart 2026-11-02]] · [[00 Home]]
