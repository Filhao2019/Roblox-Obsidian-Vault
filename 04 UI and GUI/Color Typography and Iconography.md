---
title: Color Typography and Iconography
date: 2026-11-02
tags: [ui, color, fonts, icons]
status: researched
---

# Color Typography and Iconography

Reusable colour ladders, font choices and icon sources. Visual rules: [[UI Design Principles for Roblox]]. Hex values below are a **community-convention starting palette I composed**, not sampled from any game; tune them in Studio.

## Rarity colour standard
Most top games converge on this ladder, but exact tier names and counts differ per game (guides for [[Blox Fruits]] disagree on tier count; [[Steal a Brainrot]] runs Common up through Secret/God tiers).

| Tier | Colour name | Approx hex | Stroke (darker) | Extra |
|---|---|---|---|---|
| Common | Grey | `#B8BCC4` | `#4A4F59` | none |
| Uncommon | Green | `#5BD65B` | `#1F6B2A` | none |
| Rare | Blue | `#3FA0FF` | `#1B4A9C` | soft glow |
| Epic | Purple | `#B05CFF` | `#52209B` | glow + sparkle |
| Legendary | Gold/orange | `#FFB82E` | `#9A5A00` | shine sweep |
| Mythic | Red/pink | `#FF4D6D` | `#8A1230` | pulsing glow |
| Secret / Divine | Rainbow or white-gold | animated gradient | `#FFFFFF`/dark | full-screen moment |

Special variants: shiny/neon/mega usually use animated rainbow or cyan-magenta gradients (see Adopt Me Neon art, [Neon Hawk](https://adoptme.fandom.com/wiki/File:Neon_Hawk.png)). A Sols RNG rarity article lists its tiers by odds rather than colour ([guide](https://itemlevel.net/sols-rng-how-to-get-rarest-auras-complete-guide/)).

## UI colour roles
| Role | Suggested | Notes |
|---|---|---|
| Primary action | Green `#3DDC4E` to `#1FA83A` gradient | Buy, confirm |
| Danger/close | Red `#FF4040` to `#C41E1E` | Close X, delete |
| Premium | Gold `#FFD23F` | Robux items |
| Panel | Navy/purple `#2B2D5B` or white `#FFFFFF` | Match theme |
| Outline | Near-black `#101018` | 2-4 px |
| Text | White with dark stroke | Never grey-on-colour |

## Fonts available in Studio
Studio cannot load custom font files, so pick from the built-in set ([Font datatype](https://create.roblox.com/docs/en-us/reference/engine/datatypes/Font.md), [Font enum](https://create.roblox.com/docs/reference/engine/enums/Font.md)).
- **Builder Sans** (Enum members BuilderSans, Medium, Bold, ExtraBold) — clean UI body font; its enum entries point to a Builder font licence.
- **Fredoka One** — rounded, chunky display font; single regular weight per the legacy reference ([developer ref](https://developer.roblox.com/api-reference/datatype/Font)).
- **Gotham family** and **Montserrat** — modern geometric; GothamMedium was removed and maps to Montserrat per the enum page.
- **Others** in the list include Bangers, Luckiest Guy, Cartoon-style faces, SourceSans, Arimo (replacement for Arial) — check the list for the current set rather than assuming ([developer enum](https://developer.roblox.com/api-reference/enum/Font)).
- Prefer the `Font` datatype (`Font.new`, `Font.fromName`) over legacy `Enum.Font` for new work.
- Use `UITextSizeConstraint` with `TextScaled` to keep text between a min and max size; avoid MinTextSize below ~9 ([reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UITextSizeConstraint.md)).
- Pairing: display font for numbers/headings, Builder Sans/Gotham for descriptions. Figma tip: design in Montserrat, use Gotham in Studio ([guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916)).

## Iconography
- Style: bold silhouettes with thick dark outline and a highlight, 1:1 aspect, centred in a rounded square. Keep one angle of light across the set.
- Make icons white in the source, then recolour via `ImageColor3` ([guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916)).
- Enforce squareness with `UIAspectRatioConstraint` ([reference](https://create.roblox.com/docs/en-us/reference/engine/classes/UIAspectRatioConstraint.md)).
- Sources: draw in Figma/Photopea ([[UI Tools Plugins and Kits]]), render 3D items into icons using a ViewportFrame ([[Inventory Trading and Collection UI]]), or use licensed packs from the Creator Store (check licence before shipping) `(unverified)` individual packs. AI-generated icon workflows exist but review the asset policy.
- Upload at 256 or 512 px squares; atlas small icons into spritesheets to cut load `(unverified)`.

## References
- [Font datatype](https://create.roblox.com/docs/en-us/reference/engine/datatypes/Font.md) — official docs · font families and weights
- [Font datatype (older)](https://create.roblox.com/docs/reference/engine/datatypes/Font.md) — official docs · same, alt path
- [Font enum](https://create.roblox.com/docs/reference/engine/enums/Font.md) — official docs · legacy enum list
- [Font datatype (developer.roblox.com)](https://developer.roblox.com/api-reference/datatype/Font) — legacy docs · weights per family
- [Font enum (developer.roblox.com)](https://developer.roblox.com/api-reference/enum/Font) — legacy docs · members
- [UITextSizeConstraint](https://create.roblox.com/docs/en-us/reference/engine/classes/UITextSizeConstraint.md) — official docs · text clamps
- [UITextSizeConstraint (robloxapi)](https://robloxapi.github.io/ref-temp/class/UITextSizeConstraint.html) — API mirror · properties
- [TextService (ja-jp)](https://create.roblox.com/docs/ja-jp/reference/engine/classes/TextService) — official docs (Japanese) · text measuring
- [UIAspectRatioConstraint](https://create.roblox.com/docs/en-us/reference/engine/classes/UIAspectRatioConstraint.md) — official docs · square icons
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — official docs · stroke/gradient
- [The Ultimate UI Design Guide](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916) — DevForum · font pairing and icon recolour
- [Neon Hawk file](https://adoptme.fandom.com/wiki/File:Neon_Hawk.png) — wiki · variant glow
- [Rarest auras in Sols RNG](https://itemlevel.net/sols-rng-how-to-get-rarest-auras-complete-guide/) — guide · rarity tiers
- [Steal a Brainrot rarities](https://allthings.how/steal-a-brainrot-brainrots-rarities-and-prices-full-list/) — guide · tier names
- [All fruits in Blox Fruits (esports.net)](https://www.esports.net/news/gaming/all-fruits-in-blox-fruits) — guide · tier names
- [Ranks (Pet Simulator 99)](https://pet-simulator.fandom.com/wiki/Ranks_(Pet_Simulator_99)) — wiki · rank badges

Links: [[UI MOC]] · [[00 Home]]
