---
title: Grow a Garden
date: 2026-11-02
tags: [game, simulator, farming, tycoon]
status: researched
roblox_url: https://www.roblox.com/games/126884695634066
universe_id: 7436755782
studio: The Garden Game (Splitting Point Studios / Do Big Studios with original creator BMWLux)
genre: Simulation / Tycoon
created: 2025-03-25
---

# Grow a Garden

A chill farming simulator: buy seeds from a global shop that restocks every five minutes, plant them, wait, harvest, sell, and keep crops growing offline. A teenager built the first version in days; Splitting Point Studios (Janzen "Jandel" Madsen) joined at ~500 CCU and turned it into a weekly-update live service. In 2025 it broke Roblox's records repeatedly (about 8.9M concurrent in May, 16M+ in June, reported 21.6M on 2025-06-21, beating Fortnite's earlier 15.2M peak) and made mainstream news. In late 2026 it has cooled to about 18K playing but 36B visits and 11.5M favorites. Learn from it: a relaxed, global-timer loop plus weekly spectacle events.

| Stat (2026-11-02) | Value |
|---|---|
| Playing | 17,930 |
| Visits | 36.0B |
| Favorites | 11.47M |
| Like ratio | 89.9% |
| Max server size | 4 |

## Core gameplay loop
- **Minute-to-minute:** equip a seed, click a plot, wait for growth, harvest fruit, sell for Sheckles (in-game money), buy more expensive seeds and gear; global shop restocks on a five-minute clock so players keep returning.
- **Session loop:** hunt rare seeds at restock, tend crops while weather/mutations roll, use pets and tools, trade or gift to friends, expand the garden.
- **Long-term loop:** mutation hunting, pets, events (weekly), prestige-like resets (unverified), "flex" crops. Plants continue growing offline.

## Why it went viral
- Lowest-possible friction: no enemies, no combat, no time pressure; simple to explain to anyone.
- Global restock timer creates coordinated "rare seed incoming" moments and Discord/YouTube restock streams.
- Weekly updates by an experienced studio (Splitting Point) with ever-bigger events: Jandel storms, laser storms, black holes, disco.
- Cheap, social, mobile-friendly; used as hangout (veterans gift newcomers).
- Media: record CCU coverage (esports.gg, Insider Gaming, PocketGamer.biz), AP wire story on the teenage creator, Fortune, GamesBeat interview with Madsen. Bloomberg/BBC/Forbes/Wired coverage was not located in this research (unverified).
- Timing: rose during summer 2025 holidays and while GTA 6 was delayed (journalist speculation).
- Won Best New Experience at the Roblox Innovation Awards (per GamesBeat).

## Progression and retention
- Seeds by rarity, gear, pets, cosmetics, then mutations: Gold x20, Rainbow x50, Frozen x10, Sundried x85, Aurora x90, Voidtouched x135, Cosmic and Abyssal x240, Plasma x5 etc.; mutations stack and the wiki cites combined multipliers above 200,000x.
- Weather system: Rain, Thunderstorm, Frost, Night, Blood Moon, Meteor Shower, Bee Swarm, Volcano, Disco, Jandel Storm, Sheckle Rain, Lazer Storm, Tornado, Black Hole, etc.; weather applies to all servers and triggers mutations.
- Offline growth; return rewards; limited seasonal crops and cosmetics.

## Monetization
- Robux seeds/gear, restock skips, pet eggs, instant-grow, game passes, limited events (patterns only). Free play works but is slower.
- "Admin abuse"-style events encourage spending on boosters at peak (unverified).

## Art direction and 3D assets
- Minecraft-like blocky, bright, low-poly cartoon: green grass plots, brown tilled squares, simple fences; each crop is a chunky model with glossy rim. Mutation overlays tint crops (gold shiny, rainbow cycling, brown dried, blue-purple pulsing aurora, black voidtouched particles). Soft classical background music. → [[Art Styles of Top Games]]

## UI and GUI
- Bottom hotbar of seed/gear tools with count badges, Sheckles counter at top-left or top-center, timer-based seed shop UI with stock counts and "restock in mm:ss", rarity text colors (grey-green-blue-purple-gold; unverified exact). Bright rounded panels. → [[UI Breakdown of Top Games]]

## Animation
- Plant growth tween (scale up), harvest pop, pets idle/follow, weather event cutscenes (Jandel NPC with laser beams, giant Jandel in Jandel Storm). → [[Animation MOC]]

## SFX and music
- Soft classical background; event themes: Disco weather plays a novelty song, Jandel Storm uses an "Ode to Joy" soundtrack (per Ginx); coin-pop harvest sounds and shop chimes. → [[SFX of Top Games]]

## VFX
- Weather particles: rain, lightning strikes, frost shivers, red blood moon sky, meteors, bees, volcano eruption, golden sky for Sheckle Rain, tornado, purple void sky; crop-level mutation particles (water drips, ice shell, ash, falling currency, star sparkles). → [[Environmental and Weather VFX]] · [[VFX of Top Games]]

## Systems and code worth studying
- Server-global shop restock with seeded RNG, plant growth timers computed from timestamps (offline growth), crop value = base x size x mutation multipliers, server-wide weather scheduler, pet system, trade. → [[Pet Egg and Gacha Systems]] · [[Coding MOC]]

## Lessons to steal (patterns, not content)
- A global timer (restock) is the best "come back" device for a relaxed game.
- Timestamp-based growth gives offline progress for free.
- Layered multiplier mutations create endless build-your-own-jackpot stories.
- Weekly, loud events get media and creator coverage without changing the core loop.
- Make partnerships (original dev retains a share) to scale a hit with a pro live-ops team.
- Keep the first minute trivial; progression depth lives in the shop.

## References
- [Grow a Garden on Roblox](https://www.roblox.com/games/126884695634066) — official page
- [How Grow a Garden took off (GamesBeat interview with Janzen Madsen)](https://gamesbeat.com/janzen-madsen-interview/) — interview · growth timeline, weekly updates
- [Roblox video game Grow a Garden viral summer hit (Fortune)](https://fortune.com/2025/07/30/roblox-video-game-grow-a-garden-viral-summer-hit/) — news · mechanics, 21.6M record
- [Grow a Garden hits 11M concurrent (Insider Gaming)](https://insider-gaming.com/roblox-grow-a-garden-hits-incredible-record-of-11m-concurrent-players/) — news · record
- [Grow a Garden shatters record again (Insider Gaming)](https://insider-gaming.com/roblox-grow-a-garden-shatters-all-time-player-record-for-second-week-in-a-row/) — news · record
- [Grow a Garden beats Steam (PocketGamer.biz)](http://www.pocketgamer.biz/roblox-game-grow-a-garden-beats-steam-with-record-concurrent-user-high-of-89m/) — trade press · 8.9M record
- [Grow a Garden breaks Blox Fruits record (esports.gg)](https://esports.gg/news/roblox/grow-a-garden-breaks-blox-fruits-record-for-most-concurrent-users-on-roblox/) — news
- [Roblox breaks mega player records (TBreak)](https://tbreak.com/roblox-breaks-mega-player-records-beats-fortnite/) — news · contains a 47M claim that other sources do not support (unverified)
- [Notebookcheck: 5 million concurrent](https://www.notebookcheck.net/Unbelievable-record-Free-Roblox-game-hits-5-million-concurrent-players-more-than-any-game-on-Steam.1023197.0.html) — news
- [Millions flocking to grow virtual gardens (AP via News4Jax)](https://www.news4jax.com/business/2025/07/30/millions-are-flocking-to-grow-virtual-gardens-in-viral-roblox-game-created-by-teenager/) — wire story · teen creator
- [Roblox Grow a Garden teenager (Boston Globe/AP)](https://www.bostonglobe.com/2025/07/30/wires/roblox-grow-a-garden-teenager/) — wire story
- [A teen allegedly created the viral game (Ypulse)](https://www.ypulse.com/newsfeed/2025/06/12/a-teen-allegedly-created-the-viral-grow-a-garden-game-on-roblox-and-young-gamers-are-loving-it/) — trend press
- [Grow a Garden mutations (Pocket Tactics)](https://www.pockettactics.com/grow-a-garden-mutations) — guide · multipliers and looks
- [All weather events (Ginx)](https://www.ginx.tv/en/weather-events-grow-a-garden) — guide · weather visual/audio table
- [Weather events guide (Deltias Gaming)](https://deltiasgaming.com/?p=203882) — guide
- [Weather event mutation planner (AverGames)](https://avergames.com/games/grow-a-garden/weather-event-mutation-planner/) — tool
- [Grow a Garden gameplay guide (NoPing)](https://noping.com/blog/grow-a-garden-gameplay-guide) — guide

Links: [[Games MOC]] · [[Top Games Chart 2026-11-02]] · [[00 Home]]
