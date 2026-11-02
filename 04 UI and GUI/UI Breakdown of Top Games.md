---
title: UI Breakdown of Top Games
date: 2026-11-02
tags: [ui, gui, games, breakdown]
status: researched
---

# UI Breakdown of Top Games

A per-game read of how the 27 chart games present their interface: where the HUD pieces sit, how buttons are built, which palette and fonts they lean on, and the one UI moment each game is known for. Companion pattern notes: [[UI Design Principles for Roblox]], [[HUD and Currency Displays]], [[Shop and Monetization UI]], [[Inventory Trading and Collection UI]], [[Color Typography and Iconography]], [[UI Animation and Juice]].

**Confidence warning.** Search tools in this research pass returned guides and wikis that describe mechanics, not pixel-level screenshots. Layout, stroke, radius and hex values below are therefore a mix of (a) what guides state about the mechanic and (b) typical values the genre uses. Anything visual that I could not tie to a source is marked `(unverified)`. Hex codes are *approximate palette anchors*, not sampled pixels. Before copying a look, open the game and eyeball it; see the chart in [[Top Games Chart 2026-11-02]].

**Shared genre conventions** (apply unless a section says otherwise):
- Simulator/tycoon titles: currency stack top-left or top-center, round buttons in a left-edge column (Shop, Inventory, Index, Settings), pop-up windows as rounded frames with a thick dark outline and a red close "X" at the top-right corner.
- Fonts: the Roblox built-in set is small ([Font enum](https://create.roblox.com/docs/reference/engine/enums/Font.md)); top games mostly use a chunky display face (Fredoka One / Luckiest Guy / Bangers class, `(unverified)` per game) for labels and Gotham/Builder Sans for body copy.
- Rarity is colour-coded; see the standard table in [[Color Typography and Iconography]].

---

## 1. [[Steal An Egg]]
- **HUD:** cash readout and egg/pet shortcuts in the steal-and-collect style; base ownership indicators. `(unverified)` — no source found for layout.
- **Buttons / palette:** expected bright saturated gradients with thick outlines like its genre siblings. `(unverified)`
- **Signature moment:** egg purchase/open reveal and stealing from other bases; see [[Steal and Collect Tycoon Formula]].
- **Menus:** shop, inventory/pets, settings (assumed). 

## 2. [[Blox Fruits]]
- **HUD:** health/energy bars, hotbar of skills along the bottom, level and money readouts on a side panel (typical for the game, `(unverified)` in detail).
- **Menus:** fruit stock shop, inventory with rarity-sorted fruits (Common to Mythical per several lists), stats allocation screen.
- **Rarity:** guides list tiers Common up to Mythical; sources disagree on tier count and give no colours, so treat colours as `(unverified)`.
- **Signature moment:** fruit stock refresh and fruit trading values.

## 3. [[Murder Mystery 2]]
- **HUD:** minimal in rounds: role is hidden, a timer and coin counter, knife/gun tool slot. `(unverified)`
- **Menus:** crate/weapon inventory with rarity-coloured items, trade window.
- **Signature moment:** role reveal at round start; coin collection counter during the round.

## 4. [[Brookhaven RP]]
- **HUD:** roleplay tool: left menu icons for houses, vehicles, avatar and music; the default Roblox top bar stays visible. `(unverified)`
- **Menus:** vehicle spawner, house/props lists, avatar editor — list-and-grid layouts rather than flashy currency UI.
- **Style:** low-key, utility-first; fewer gradients than simulators.

## 5. [[Adopt Me]]
- **HUD:** pastel, rounded kid-friendly UI; needs/tasks bars for pets; bucks and event currency counters.
- **Pet tiers:** Fandom wiki pages describe Neon pets glowing on specific body parts and Mega Neons cycling rainbow colours; that glow language carries into the UI as colour-coded age/rarity badges.
- **Menus:** inventory grid with pet cards, trading window (two-sided with confirm step), nursery/Neon Cave.
- **Signature moment:** the Neon / Mega Neon pet creation sequence.

## 6. [[Rivals]]
- **HUD:** FPS crosshair, ammo and weapon wheel/slots, kill feed top-right, round score top-center. `(unverified)`
- **Loadout screen:** guides describe a pre-match loadout of primary, secondary, melee and utility slots (one guide says 3 weapons, another 4 slots; check in game). Mirror Matchups assign loadouts automatically.
- **Style:** darker, competitive, flatter than simulators; skins show rarity colours.

## 7. [[Break and Steal an Egg]]
- **HUD / menus:** same family as Steal An Egg: cash, egg shop, base slots. `(unverified)`

## 8. [[99 Nights in the Forest]]
- **HUD:** survival bars (health, hunger), day counter, inventory hotbar, campfire/fuel indicators. `(unverified)`
- **Style:** darker palette, serif-ish or rounded horror fonts, vignette overlay.

## 9. [[Throw Food For Animals]]
- **HUD / menus:** tycoon money counter, upgrade buttons, animal collection. `(unverified)`

## 10. [[Anime Adventures]]
- **HUD:** tower-defense top bar (wave, cash, base HP), unit hotbar along the bottom with cost badges, speed toggle.
- **Menus:** summon (gacha) banners, unit index with rarity borders, trait rerolls. `(unverified)` on look.

## 11. [[The Strongest Battlegrounds]]
- **HUD:** four-move hotbar with cooldown overlays, ultimate meter, health bar; minimal chrome so combat is visible.
- **Style:** anime-inspired text, bold white outlined fonts. `(unverified)`

## 12. [[Fisch]]
- **Signature moment — reel bar:** guides describe a two-stage flow: cast, wait for a bite, then a minigame where you keep a player-controlled white bar over a moving fish icon while a progress bar fills; rod "Control" stat widens the bar and a perfect catch means the fish never left it ([Sportskeeda](https://www.sportskeeda.com/roblox-news/roblox-fisch-a-beginner-s-guide)).
- **HUD:** hotbar for rod and items, currency in C$, fish catch popup showing rarity.
- **Menus:** merchant shop (e.g. Training Rod listed at 300C$ in a guide), rod progression screens.

## 13. [[Pet Simulator 99]]
- **Signature moment — hatch screen:** eggs are bought (single/triple/auto), pets pop onto a dim stage with rarity-coloured names; rarer pets get extra effects. Wiki pages confirm eggs, costs, and the Golden/Rainbow/Shiny transform system (see references) but not exact pixel layout.
- **HUD:** multi-currency stack (coins, diamonds) at top, area/zone buttons, ranks and rank rewards.
- **Menus:** inventory grid with enchants/ stacking, index/collection book, trading plaza, gamepasses list.
- **Juice:** heavy number pop-ups when breaking objects, big egg rattle before the pop.

## 14. [[Fish It]]
- **HUD / menus:** fishing-simulator flow with sell shop and rod/bait upgrades; layout similar to [[Fisch]]. `(unverified)`

## 15. [[Dont Splash]]
- **HUD:** runner-obby: distance/score, lives or checkpoint indicator. `(unverified)`

## 16. [[Jujutsu Shenanigans]]
- **HUD:** move hotbar with cooldown radial, cursed-energy/ultimate meter, health bar, anime-style bold text. `(unverified)`

## 17. [[Steal a Brainrot]]
- **Signature moment — cash/sec readout:** each brainrot placed on a base earns passive cash per second based on rarity, traits and mutations; guides give examples like a Mythic range of ~1.4K to 16K per second and Secret units into millions ([All Things How](https://allthings.how/steal-a-brainrot-brainrots-rarities-and-prices-full-list/)). Each unit shows its per-second income in a billboard above it, and the base collects into a cash pad.
- **Rarity:** Common to Secret/God tiers with colour banners; mutation overlays (e.g. Lava) tint the model and label.
- **Buttons:** big green "buy/steal" prompts and floating price tags `(unverified)`.

## 18. [[Dandys World]]
- **HUD:** floor/machine progress, team of characters with portraits, skill-check minigame bar for repairing machines. `(unverified)`
- **Style:** hand-drawn, cartoon-ink aesthetic with rounded character cards.

## 19. [[Violence District]]
- **HUD:** asymmetric 1vN horror: generator progress, skill check, killer cooldowns, minimal grungy theme. `(unverified)`

## 20. [[Evade]]
- **HUD:** stamina/sprint, downed-timer, revive prompts, round timer and map vote screen. `(unverified)`

## 21. [[Dress To Impress]]
- **Signature moment — runway & voting:** guides say each round gives a theme and timer; players build an outfit, walk the runway, and others rate it with 1-5 stars. Theme voting may have been replaced by random/prop-driven selection per one guide ([Timesaver](https://timesaver.gg/blog/dress-to-impress-themes)); sources disagree, so verify in game.
- **Menus:** closet with category tabs (tops, shoes, hair, makeup), VIP clothing locks, rank system.
- **Palette:** pink / lilac / white fashion palette, rounded cards, sparkles `(unverified)`.

## 22. [[Sols RNG]]
- **Signature moment — roll UI:** a central Roll button; Auto Roll is a toggle near it (free via group join per guides) and Quick Roll is a gamepass ([All Things How](https://allthings.how/sol-s-rng-how-to-get-auto-roll-and-quick-roll-in-roblox/)). Rolled auras fill the screen with title text and effects scaled to rarity.
- **Menus:** aura storage with filters (Aura Filter, Auto Equip threshold), settings for skipping animations for rare rolls.
- **Palette / style:** dark space theme with bright rarity-coloured text glow `(unverified)`.

## 23. [[Grow a Garden]]
- **HUD:** sheckles counter, seed/gear shop timer with restock countdown, hotbar of seeds/tools. `(unverified)`

## 24. [[Doors]]
- **HUD:** deliberately minimal horror HUD: small item hotbar, flashlight/lighter indicator, door numbers, subtle vignette; hint text at the bottom for guiding messages. `(unverified)` in specifics.
- **Menus:** Knobs/currency shop between runs, closet-style death screen with hints.

## 25. [[Forsaken]]
- **HUD:** survivor/killer ability buttons with cooldown rings, stamina, health, generator progress. `(unverified)`

## 26. [[Tower Defense Simulator]]
- **HUD:** top wave/health/cash bar, tower hotbar at bottom, upgrade panel when a placed tower is selected, speed controls.
- **Menus:** lobby loadout (5 towers), crates/skins; tower cards with rarity-coloured frames. `(unverified)` on colours.

## 27. [[Blade Ball]]
- **HUD:** one large parry/block button on mobile; ball target indicator and speed; spin/crate shop for swords and effects. `(unverified)`

---

## What to copy across all of them
1. A permanent, instantly readable currency stack ([[HUD and Currency Displays]]).
2. Rarity colour as the primary language of value ([[Color Typography and Iconography]]).
3. One signature "moment" screen that is over-animated on purpose ([[UI Animation and Juice]]).
4. Chunky, finger-friendly buttons ([[Mobile Console and Responsive UI]]).

## References

Official / technical
- [Font enum (Creator Docs)](https://create.roblox.com/docs/reference/engine/enums/Font.md) — docs · built-in font list
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — docs · UIStroke/UIGradient/UICorner

Pet Simulator 99
- [Pet Simulator 99 (Roblox Fandom)](https://roblox.fandom.com/wiki/BIG_Games_Pets/Pet_Simulator_99) — wiki stub · game overview
- [Ranks (Pet Simulator 99)](https://pet-simulator.fandom.com/wiki/Ranks_(Pet_Simulator_99)) — wiki · rank system
- [Gamepasses (Pet Simulator 99)](https://pet-simulator.fandom.com/wiki/Gamepasses_(Pet_Simulator_99)) — wiki · gamepass shop items
- [Anchor Egg](https://pet-simulator.fandom.com/wiki/Anchor_Egg_(Pet_Simulator_99)) — wiki · egg odds and cost
- [Backrooms Fear Egg](https://pet-simulator.fandom.com/wiki/Backrooms_Fear_Egg_(Pet_Simulator_99)) — wiki · themed egg
- [Pet Simulator 99 update 61](https://www.biggames.io/post/pet-simulator-99-update-61) — official studio post · egg transform update
- [PS99 eggs (Bloxodes)](https://bloxodes.com/wiki/pet-simulator-99/eggs) — guide · egg list

Steal a Brainrot
- [Brainrots rarities and prices](https://allthings.how/steal-a-brainrot-brainrots-rarities-and-prices-full-list/) — guide · rarity tiers and income
- [All Brainrot Gods and earnings](https://www.sportskeeda.com/roblox-news/steal-a-brainrot-all-brainrot-gods-earnings) — guide · cash/sec numbers
- [Beginners guide 2026](https://rblxguide.com/games/steal-a-brainrot/updates/steal-a-brainrot-beginners-guide-2026) — guide · base loop
- [All Brainrots database](https://rblxguide.com/games/steal-a-brainrot/brainrots) — database · rarity and income
- [Bisonte Giuppitere guide](https://www.sportskeeda.com/roblox-news/steal-brainrot-bisonte-giuppitere-guide) — guide · example unit
- [All brainrots and secrets](https://techwiser.com/all-brainrots-and-secrets-in-steal-a-brainrot-roblox/) — guide · secret tier
- [All brainrots stats](https://findingdulcinea.com/all-brainrots-in-steal-a-brainrot-stats/) — guide · stats list

Fisch
- [Roblox Fisch: a beginner's guide](https://www.sportskeeda.com/roblox-news/roblox-fisch-a-beginner-s-guide) — guide · reel minigame
- [How to Fish in Fisch](https://www.sportskeeda.com/roblox-news/how-fish-fisch) — guide · casting flow
- [How to catch fish in Fisch](https://videogameschronicle.com/guide/fisch-fishing-tips) — guide · minigame tips
- [Fisch Rod Progression Guide](https://deltiasgaming.com/roblox-fisch-rod-progression-guide) — guide · rod stats
- [Go Fishing Roblox guide](https://www.destructoid.com/go-fishing-roblox-guide/) — guide · fishing games
- [Fisch codes and tips](https://www.supercheats.com/fisch-codes-tips) — guide · tips

Sol's RNG
- [Sol's RNG guide, features, FAQs](https://sportskeeda.com/roblox-news/sol-s-rng-guide-features-faqs) — guide · features
- [Sol's RNG full guide](https://allthings.how/sol-s-rng-on-roblox-how-to-play-full-guide/) — guide · roll flow
- [Auto roll and quick roll](https://allthings.how/sol-s-rng-how-to-get-auto-roll-and-quick-roll-in-roblox/) — guide · roll toggles
- [Beginners guide](https://rblxguide.com/games/sols-rng/updates/beginners-guide) — guide · settings
- [Rarest auras](https://itemlevel.net/sols-rng-how-to-get-rarest-auras-complete-guide/) — guide · rarity tiers
- [Sols RNG wiki (Techwiser)](https://techwiser.com/roblox-sols-rng-wiki/) — guide · wiki-style
- [Sols RNG (Bloxodes)](https://bloxodes.com/wiki/sols-rng) — wiki · aura info

Dress To Impress
- [Dress To Impress themes (Timesaver)](https://timesaver.gg/blog/dress-to-impress-themes) — guide · theme/voting changes
- [DTI definitive guide](https://sportskeeda.com/roblox-news/dress-to-impress-a-definitive-guide) — guide · rounds
- [DTI beginners guide](https://rblxguide.com/games/dress-to-impress/updates/beginners-guide) — guide · UI basics
- [DTI theme guide (BlueStacks)](https://www.bluestacks.com/blog/game-guides/roblox/rl-dress-to-impress-theme-guide-outfit-ideas-en.html) — guide · themes
- [How to rank up in DTI](https://esports.gg/news/gaming/how-to-rank-up-in-dress-to-impress-dti/) — guide · ranks
- [How to play DTI (SteelSeries)](https://steelseries.com/de-be/blog/how-to-play-dress-to-impress) — guide · flow
- [All DTI themes](https://dotesports.com/roblox/news/all-themes-in-dress-to-impress-roblox) — guide · themes
- [DTI themes (mobi.gg)](https://mobi.gg/en/tips/dress-to-impress-themes/) — guide · themes

Rivals
- [Best loadout for every weapon](https://allthings.how/roblox-rivals-best-loadout-for-every-weapon/) — guide · loadout slots
- [Rivals all weapons guide](https://www.sportskeeda.com/roblox-news/roblox-rivals-weapons-guide) — guide · weapon categories
- [Rivals game modes](https://www.sportskeeda.com/roblox-news/rivals-game-modes-guide) — guide · modes
- [Rivals Mirror Matchups](https://deltiasgaming.com/?p=310144) — guide · auto loadouts
- [Rivals beginner guide](https://bloxodes.com/articles/rivals-beginner-guide) — guide · basics

Adopt Me and Blox Fruits
- [Mega Neon Goat file](https://adoptme.fandom.com/wiki/File:Mega_Neon_Goat.png) — wiki file · mega neon look
- [Neon Hawk file](https://adoptme.fandom.com/wiki/File:Neon_Hawk.png) — wiki file · neon look
- [Adopt Me Rhino](https://adoptme.fandom.com/wiki/Rhino) — wiki · pet card layout
- [10 rarest pets in Adopt Me](https://esports.gg/news/roblox/10-rarest-pets-adopt-me/) — guide · rarity ranking
- [Blox Fruits Super Fruit Box](https://blox-fruits.fandom.com/wiki/Super_Fruit_Box) — wiki · fruit box
- [All fruits in Blox Fruits](https://dotesports.com/roblox/news/all-fruits-in-blox-fruits) — guide · tiers

Links: [[UI MOC]] · [[00 Home]]
