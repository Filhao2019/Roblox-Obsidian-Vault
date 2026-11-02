---
title: Shop and Monetization UI
date: 2026-11-02
tags: [ui, shop, monetization]
status: researched
---

# Shop and Monetization UI

How top games structure stores, offers and purchase prompts. Strategy lives in [[Monetization Patterns]]; this note covers presentation and the Roblox API hooks. Examples reference [[Pet Simulator 99]], [[Sols RNG]], [[Fisch]], [[Adopt Me]] and [[Rivals]].

## Store layout patterns
- **Tabbed shop window:** left or top tabs (Gamepasses, Boosts, Currency, Cosmetics). Grid of cards: icon, name, price chip, buy button.
- **Featured banner:** a large top card for the current offer or limited item, with a countdown timer chip.
- **Currency packs:** 3-6 escalating cards with "Best value" ribbons; middle card enlarged.
- **Gamepass list:** icon + one-line benefit (e.g. 2x luck, auto-hatch, quick roll). Sols RNG sells Quick Roll as a gamepass while Auto Roll is a free group unlock per guides ([guide](https://allthings.how/sol-s-rng-how-to-get-auto-roll-and-quick-roll-in-roblox/)). PS99 keeps a gamepass wiki list ([wiki](https://pet-simulator.fandom.com/wiki/Gamepasses_(Pet_Simulator_99))).
- **Restock shops:** seed/gear/rod shops with a visible refresh timer ([[Grow a Garden]], [[Blox Fruits]] fruit stock).
- **Contextual "+" buttons** on currency pills jump straight to the matching store tab ([[HUD and Currency Displays]]).

## Button & card style
Green primary "Buy" with Robux icon or soft-currency icon, red/orange for limited offers, gold for premium. Strike-through old price and a percentage badge. Keep the price in the display font with a stroke. See [[Color Typography and Iconography]].

## Roblox API
- Developer products and game passes are bought through `MarketplaceService` prompts; handle `ProcessReceipt` on the server ([MarketplaceService docs](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService), [developer products doc](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-products.md)).
- Prompt with the correct ID type; a forum case failed because a game pass ID was used where a product ID was required ([thread](https://devforum.roblox.com/t/how-to-prompt-a-purchase/1037470)).
- Never grant the item on the client; grant on the server after the receipt. See [[Security and Anti-Exploit]].
- `ProximityPrompt` is good for in-world vendors ([docs](https://create.roblox.com/docs/en-us/reference/engine/classes/ProximityPrompt.md)).

## Ethics and policy notes
Show real odds for random rewards (egg and roll odds are listed on wikis such as the [Anchor Egg page](https://pet-simulator.fandom.com/wiki/Anchor_Egg_(Pet_Simulator_99))); avoid fake countdowns. Check Roblox's current rules before shipping paid random items `(unverified)`.

## Checklist
- [ ] Every offer shows what you get and the exact price.
- [ ] Purchase success shows a reward popup ([[Notifications Popups and Rewards]]).
- [ ] Failure/cancel returns to the shop without a dead state.
- [ ] Shop grid generated from data ([[UI Implementation in Luau]]).

## References
- [MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService) — official docs · purchase prompts
- [Developer products (creator-docs)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-products.md) — official docs source · ProcessReceipt
- [MarketplaceService (robloxapi mirror)](https://robloxapi.github.io/ref/class/MarketplaceService) — API mirror · member list
- [ProximityPrompt](https://create.roblox.com/docs/en-us/reference/engine/classes/ProximityPrompt.md) — official docs · vendor interactions
- [How to prompt a purchase?](https://devforum.roblox.com/t/how-to-prompt-a-purchase/1037470) — DevForum · ID pitfalls
- [Gamepasses (Pet Simulator 99)](https://pet-simulator.fandom.com/wiki/Gamepasses_(Pet_Simulator_99)) — wiki · example gamepass lineup
- [Anchor Egg](https://pet-simulator.fandom.com/wiki/Anchor_Egg_(Pet_Simulator_99)) — wiki · odds and cost display
- [Auto roll and quick roll](https://allthings.how/sol-s-rng-how-to-get-auto-roll-and-quick-roll-in-roblox/) — guide · free vs paid convenience
- [Sol's RNG guide](https://sportskeeda.com/roblox-news/sol-s-rng-guide-features-faqs) — guide · features
- [Fisch Rod Progression Guide](https://deltiasgaming.com/roblox-fisch-rod-progression-guide) — guide · upgrade shop structure
- [Blox Fruits value list](https://www.sportskeeda.com/roblox-news/blox-fruits-value-list) — guide · fruit values/prices
- [Blox Fruits fruit values and Robux prices](https://allthings.how/blox-fruits-fruit-values-and-robux-prices/) — guide · store price points
- [Rivals all weapons guide](https://www.sportskeeda.com/roblox-news/roblox-rivals-weapons-guide) — guide · cosmetic-only monetization framing

Links: [[UI MOC]] · [[00 Home]]
