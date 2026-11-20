---
title: Brainrot and Simulator UI Patterns
date: 2026-11-20
tags: [ui, brainrot, simulator, hud, billboard, rarity, mutation]
status: untested
---

# Brainrot and Simulator UI Patterns

The 2025–26 brainrot and steal/grow wave includes [[Steal a Brainrot]], [[Grow a Garden]], [[Steal An Egg]], Escape Tsunami for Brainrots and Plants vs Brainrots ([[Brainrot Games Roundup]]). These games share one UI kit, built around a single number: **income per second**. Every screen element either shows that number, raises it or protects it. This note lists the recurring pieces, gives a suggested rarity and mutation colour ladder, and includes typed Luau for the most-copied element, the overhead unit tag. Most layout and colour details below are inferred from game mechanics, not measured from screenshots, and are marked (unverified). The Luau has not been run in Studio.

## The kit

| Element | What it does | Seen in |
|---|---|---|
| Cash pill + `$X/s` readout | Top or left-centre counter. The per-second rate under the total is the main stat | All of them (placement unverified) |
| Overhead unit tag (BillboardGui) | Shows name, rarity, mutation and `$/s` above every placed unit, so players shop other bases by reading tags | Steal a Brainrot, Escape Tsunami, Plants vs Brainrots (inferred from mechanics) |
| Conveyor / spawn belt | Units ride past with a price tag. Buying is a walk-up prompt. Pity timers guarantee a Legendary every ~5 min and a Mythic every ~15 min | Steal a Brainrot |
| Base lock button + countdown | A big timer on the base door: 60 s, plus 10 s per rebirth in Steal a Brainrot. The countdown is the stealing window for everyone else | Steal a Brainrot |
| Shop restock countdown | `Restock in 4:32` on the seed and gear shops (~5 min) and the egg shop (~30 min). A Robux button skips the wait | Grow a Garden |
| Carry / steal alert | A screen-edge flash and a sound for the owner, plus a slow-walk debuff for the thief | Steal a Brainrot, Steal An Egg |
| Index / collection book | A grid of silhouettes per rarity and per mutation. Completing a set gives a multiplier or a base cosmetic | Steal a Brainrot, Grow a Garden |
| Event banner | `ADMIN ABUSE` / weather / limited-mode banner at the top centre, with a timer. Drives live concurrency | Grow a Garden, Steal a Brainrot, Escape Tsunami |
| Rebirth panel | Cost bar, the next permanent multiplier and the slots or floors it unlocks | Steal a Brainrot |
| Upgrade button with cost | A wide green button with cash cost, repeated per stat (speed, carry, plot) | Steal An Egg treadmill |

## Rarity ladder

The games disagree on tier names and counts, and no source documents their exact colours. Use this original ladder, tuned to the vault's rarity table in [[Color Typography and Iconography]]:

| Tier | Fill | Treatment |
|---|---|---|
| Common | `#B0B0B0` | flat |
| Uncommon | `#55D45A` | flat |
| Rare | `#3D8BFF` | flat |
| Epic | `#A64DFF` | flat |
| Legendary | `#FFB020` | gradient + shine sweep |
| Mythic | `#FF3B5C` | gradient + shine sweep |
| God / Divine | `#FFF27A` → `#FFFFFF` | animated gradient |
| Secret | `#111111` with rainbow stroke | animated rainbow `UIGradient` |

Reported orders, low to high:
- **Steal a Brainrot:** Common, Rare, Epic, Legendary, Mythic, Brainrot God, Secret, OG.
- **Escape Tsunami:** Common, Uncommon, Rare, Epic, Legendary, Mythical, Cosmic, Secret, Celestial. Another source adds Divine and Infinity.

## Mutations as tags

- A mutation is a multiplier word above the name, in its own colour, plus a material swap and particles on the model ([[Voxel and Brainrot Model Style]]).
- Escape Tsunami's reported ladder: Gold 1.25×, Diamond 1.5×, Bloodrot 2×, Candy 4×, Lava 6×, Galaxy 7×, Yin Yang 7.5×, Rainbow 10×.
- Grow a Garden separates exclusive variants (Gold ~20×, Rainbow ~50×) from weather mutations that stack additively (Wet, Chilled, Shocked, Celestial). Values differ between versions.
- **UI rule:** show at most one mutation word plus a `+N` chip for stacked traits. A tag with five words is unreadable at 30 studs.

## Typography and style

- Fonts are disputed even for Steal a Brainrot. A Fonts In Use entry credits Comic Sans for purchase text and Source Sans / Montserrat for names, but a commenter there says the purchase font is Builder Sans.
- The safe choice for originals is a rounded display face such as Fredoka One or Luckiest Guy, with a 2–3 px black `UIStroke` ([[Stud UI Figma Guide]], [[Cartoony UI Figma Guide]]).
- High saturation, black outlines and green for money. Never put long text on the HUD: numbers and icons only.

## Example: overhead unit tag (Luau)

The tag is a BillboardGui sized in studs, so it shrinks with distance like the unit. `MaxDistance` stops 50 bases' worth of tags from drawing at once.

```lua
--!strict
-- UnitTag: overhead name / rarity / mutation / income tag for a placed unit.
local UnitTag = {}

local RARITY: { [string]: Color3 } = {
	Common = Color3.fromHex("B0B0B0"), Uncommon = Color3.fromHex("55D45A"), Rare = Color3.fromHex("3D8BFF"),
	Epic = Color3.fromHex("A64DFF"), Legendary = Color3.fromHex("FFB020"), Mythic = Color3.fromHex("FF3B5C"),
	God = Color3.fromHex("FFF27A"), Secret = Color3.fromHex("FFFFFF"),
}
local MUTATION: { [string]: Color3 } = {
	Gold = Color3.fromHex("FFD34D"), Diamond = Color3.fromHex("7FE7FF"), Rainbow = Color3.fromHex("FF7AF0"),
}
local SUFFIX = { "", "K", "M", "B", "T", "Qa", "Qi" }

-- 1500 -> "1.5K", 2000000 -> "2M". The 999.95 threshold stops "1000K" after rounding.
function UnitTag.short(n: number): string
	local i = 1
	while n >= 999.95 and i < #SUFFIX do
		n /= 1000
		i += 1
	end
	if i == 1 then
		return tostring(math.floor(n))
	end
	return (string.format("%.1f", n):gsub("%.0$", "")) .. SUFFIX[i]
end

local function line(parent: Instance, text: string, color: Color3, order: number, height: number): TextLabel
	local label = Instance.new("TextLabel")
	label.BackgroundTransparency = 1
	label.Size = UDim2.fromScale(1, height)
	label.FontFace = Font.fromEnum(Enum.Font.FredokaOne)
	label.TextScaled = true
	label.Text = text
	label.TextColor3 = color
	label.LayoutOrder = order
	local stroke = Instance.new("UIStroke")
	stroke.Thickness = 2
	stroke.Parent = label
	label.Parent = parent
	return label
end

function UnitTag.attach(part: BasePart, name: string, rarity: string, mutation: string?, perSecond: number): BillboardGui
	local gui = Instance.new("BillboardGui")
	gui.Name = "UnitTag"
	gui.Size = UDim2.fromScale(6, 2.6) -- scale = studs on a BillboardGui
	gui.StudsOffsetWorldSpace = Vector3.new(0, part.Size.Y / 2 + 1.8, 0)
	gui.MaxDistance = 60
	gui.Adornee = part
	local list = Instance.new("UIListLayout")
	list.SortOrder = Enum.SortOrder.LayoutOrder
	list.HorizontalAlignment = Enum.HorizontalAlignment.Center
	list.VerticalAlignment = Enum.VerticalAlignment.Bottom
	list.Parent = gui
	if mutation then
		line(gui, mutation, MUTATION[mutation] or Color3.new(1, 1, 1), 1, 0.22)
	end
	line(gui, name, Color3.new(1, 1, 1), 2, 0.3)
	local tier = line(gui, rarity, RARITY[rarity] or Color3.new(1, 1, 1), 3, 0.22)
	if rarity == "Secret" or rarity == "God" then
		local gradient = Instance.new("UIGradient") -- spin it from a client RenderStepped loop
		gradient.Color = ColorSequence.new({
			ColorSequenceKeypoint.new(0, Color3.fromHex("FF4D4D")), ColorSequenceKeypoint.new(0.5, Color3.fromHex("4DFFB8")),
			ColorSequenceKeypoint.new(1, Color3.fromHex("8A4DFF")),
		})
		gradient.Parent = tier
	end
	line(gui, "$" .. UnitTag.short(perSecond) .. "/s", Color3.fromHex("7CFF6B"), 4, 0.22)
	gui.Parent = part
	return gui
end

-- self-check: runs once when the module is first required
assert(UnitTag.short(999) == "999" and UnitTag.short(1500) == "1.5K", "short: small values")
assert(UnitTag.short(2e6) == "2M" and UnitTag.short(999950) == "1M", "short: rounding across suffixes")

return UnitTag
```

Usage, server-side when a unit is placed: `UnitTag.attach(unit.PrimaryPart, "Pickle Pancake", "Epic", "Gold", 1500)`. The tag shows Gold, Pickle Pancake, Epic and `$1.5K/s`.

## Build order for an agent

1. Cash pill with `$/s` (count-up tween, [[UI Animation and Juice]]).
2. Overhead unit tag (above).
3. Conveyor price tag: the same tag plus a `$cost` line and a ProximityPrompt.
4. Base lock button and countdown on a SurfaceGui at the base door.
5. Shop restock timer and event banner.
6. Index book ([[Inventory Trading and Collection UI]]).

## Common mistakes

- `AlwaysOnTop` tags. Players see every unit on the map through walls, and the screen fills with text.
- Tags sized in pixels (`Offset`), so they stay huge at distance. Size them in studs (scale).
- Showing the total instead of the rate. Players compare `$/s` when they decide what to steal.
- Mutation colours that clash with rarity colours. Keep mutations on a separate line, never tint the rarity word.

## References

- [Steal a Brainrot (Roblox) — Efficient stealing, events, and rebirths](https://allthings.how/steal-a-brainrot-roblox-efficient-stealing-events-and-rebirths) — guide blog · base lock timer, pity spawns, rebirths
- [Steal a Brainrot brainrots, rarities, and prices (full list)](https://allthings.how/steal-a-brainrot-brainrots-rarities-and-prices-full-list/) — guide blog · rarity ladder and income ranges
- [Steal a Brainrot video game (Fonts In Use)](https://fontsinuse.com/uses/73361/steal-a-brainrot-video-game) — typography site · font claims, disputed in comments
- [Escape Tsunami for Brainrots: mutation multipliers explained](https://allthings.how/escape-tsunami-for-brainrots-mutation-multipliers-explained/) — guide blog · mutation ladder and multipliers
- [Grow a Garden shop stock guide](https://avergames.com/games/grow-a-garden/shop-stock-guide/) — fan guide · restock timers
- [All Grow a Garden crop mutations and multipliers](https://www.pockettactics.com/grow-a-garden-mutations) — guide · variant vs weather mutations
- [Steal an Egg beginner guide](https://allthings.how/steal-an-egg-beginner-guide-biomes-speed-and-pets-explained/) — guide blog · treadmill upgrade button, carry loop

Links: [[UI MOC]] · [[00 Home]]
