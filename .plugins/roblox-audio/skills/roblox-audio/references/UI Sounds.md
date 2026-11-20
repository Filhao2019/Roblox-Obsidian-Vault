---
title: UI Sounds
date: 2026-11-02
tags: [audio, ui, sfx, rewards]
status: researched
---

# UI Sounds

UI audio confirms input, signals state change and delivers reward moments. On Roblox, the most-played games treat UI sound as a reward system: tiny clicks everywhere, a richer purchase cue, and escalating stingers for rare reveals (see [[SFX of Top Games]]). This note gives a taxonomy, design rules and a Roblox implementation path. Visual counterparts live in [[Notifications Popups and Rewards]] and [[UI Animation and Juice]].

## Taxonomy and design rules

| Event | Character | Length | Notes |
|---|---|---|---|
| Click / press | Soft, dry transient, no tail | 30-80 ms | Highest-frequency sound in the game: keep it quiet and varied slightly |
| Hover | Quieter, higher, airy tick | 20-60 ms | PC only; skip on touch. Rate-limit so rapid hovers do not machine-gun |
| Open / close panel | Short whoosh pair; close is the pitched-down or reversed open | 100-250 ms | Match panel tween duration, see [[UI Animation and Juice]] |
| Tab / toggle | Two-state click, on is brighter than off | 50-100 ms | Pitch communicates state |
| Purchase success | Coin/register layer + bright chime | 300-800 ms | Should feel richer than any click; ties to [[Shop and Monetization UI]] |
| Error / denied | Low, short, dull double-thud; never harsh | 150-300 ms | Falling pitch reads as negative ([Violet Recording](https://violetrecording.com/how-to-design-sound-effects-for-games/)) |
| Notification | Distinct from clicks; two-note motif | 300-600 ms | Brand-defining; keep consistent |
| Reward reveal | Build-up riser, hit on reveal, sparkle tail | 1-4 s | Matches the animation beats |
| Rarity stinger | Longer and richer per tier | 1-10 s | See below |
| Currency tick | Very short pitched tick; combo pitch climb | 30-60 ms | See [[What Makes a Sound Satisfying]] |

Principles:

1. **Hierarchy of loudness**: errors and purchases above clicks; never louder than gameplay warnings.
2. **Rising = good, falling = bad** ([Violet Recording](https://violetrecording.com/how-to-design-sound-effects-for-games/)).
3. **Consistency**: UI sounds come from one family (same synth or material) so the interface feels designed. Kenney's UI and interface packs show such a family ([Kenney audio](https://kenney.nl/assets/category:Audio)).
4. **Always provide a toggle**. [[Sols RNG]] exposes separate switches for background music, UI SFX, other players' aura SFX and server rare-drop SFX ([ItemLevel](https://itemlevel.net/sols-rng-best-settings-guide/)).
5. **Casual audiences play muted** — do not hide critical information only in audio ([GDC 2024: casual players and audio](https://www.gdcvault.com/play/1034493/Audio-Summit-How-Do-You)).
6. **Check the device**: phones have weak low end, so keep UI cues in the mid/high range.

## Rarity stingers

The loop used by gacha-style games ([[Pet Simulator 99]], [[Anime Adventures]], [[Fisch]], [[Sols RNG]]): each tier adds time, layers and frequency range rather than only volume.

- Common: single short pop.
- Uncommon-Rare: pop + chime.
- Epic: riser + hit + sparkle tail.
- Legendary/Mythic: unique musical phrase (a mini-theme), bass drop, crowd/choir pad. Sols RNG gives auras their own soundtracks ([Rblxguide: Symphony](https://rblxguide.com/games/sols-rng/auras/symphony)).
- Broadcast tier: server-wide announcement sound, which players must be able to disable.

Duck music during the stinger and restore after (code in [[Audio Implementation in Luau]]); pair with [[Reward and Rarity VFX]].

## Implementation on Roblox

- UI sounds are 2D: parent to `SoundService` or play through an AudioPlayer wired to an AudioDeviceOutput ([audio objects](https://create.roblox.com/docs/audio/objects), [2D tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio)). Legacy `Sound` objects parented to SoundService or Workspace play identically regardless of listener ([Sound objects](https://create.roblox.com/docs/sound/objects)).
- `SoundService:PlayLocalSound` is a quick one-off call for client UI ([SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService)).
- Put UI on its own SoundGroup so the settings menu can scale it ([Sound groups](https://create.roblox.com/docs/sound/groups)).
- Pool and pitch-jitter hover/click sounds; hook to `MouseEnter`/`Activated`. Full module: [[Audio Implementation in Luau]]; UI-side wiring in [[UI Implementation in Luau]].
- Preload the sound assets used in the first 30 seconds (onboarding feel: [[Onboarding and First Session]]).

## Making UI sounds quickly

Synthesis tools generate a coherent family in minutes: [jsfxr](https://sfxr.me/) (pickup/coin, blip/select, click presets), [Bfxr](https://www.bfxr.net/) and [ChipTone](https://sfbgames.itch.io/chiptone) (CC0 output). See [[Making SFX]] and [[Sound Sources and Libraries]].

## References

- [Violet Recording: designing sound effects for games](https://violetrecording.com/how-to-design-sound-effects-for-games/) — article · rising vs falling, variants
- [Kenney audio packs](https://kenney.nl/assets/category:Audio) — asset site · Interface Sounds, UI Audio, Digital Audio packs (license per pack)
- [ItemLevel: Sol's RNG settings](https://itemlevel.net/sols-rng-best-settings-guide/) — guide · audio opt-outs
- [Rblxguide: Symphony aura](https://rblxguide.com/games/sols-rng/auras/symphony) — guide · per-aura music
- [GDC: casual players and audio](https://www.gdcvault.com/play/1034493/Audio-Summit-How-Do-You) — talk page · muted players
- [Roblox: audio objects](https://create.roblox.com/docs/audio/objects) — docs · wiring
- [Roblox: add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) — tutorial · 2D playback
- [Roblox: Sound objects](https://create.roblox.com/docs/sound/objects) — docs · 2D vs positional by parent
- [Roblox: SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService) — docs · PlayLocalSound
- [Roblox: sound groups](https://create.roblox.com/docs/sound/groups) — docs · group volume
- [jsfxr](https://sfxr.me/) — tool · retro UI sounds
- [Bfxr](https://www.bfxr.net/) — tool · synthesised SFX
- [ChipTone](https://sfbgames.itch.io/chiptone) — tool · CC0 output

Links: [[Audio MOC]] · [[00 Home]]
