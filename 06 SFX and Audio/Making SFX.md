---
title: Making SFX
date: 2026-11-02
tags: [audio, sfx, tools, workflow, upload]
status: researched
---

# Making SFX

How to produce Roblox-ready sound effects yourself: pick a tool, build or record, edit and normalise, export, then upload within Roblox's current limits. Combine with [[What Makes a Sound Satisfying]] for design and [[Sound Sources and Libraries]] for ready-made material.

## Pick a tool

| Tool | Best for | Notes |
|---|---|---|
| [jsfxr](https://sfxr.me/) | Instant retro blips, coins, clicks, hits | Browser; presets Pickup/coin, Laser, Explosion, Powerup, Hit/hurt, Jump, Click, Blip/select; free tier exports WAV and JSON, Pro adds MP3/OGG ([jsfxr](https://sfxr.me/)); library under the Unlicense ([GitHub](https://github.com/chr15m/jsfxr)) |
| [Bfxr](https://www.bfxr.net/) | Same plus mutate/randomise; includes Footsteppr | Open source, WAV export |
| [ChipTone](https://sfbgames.itch.io/chiptone) | Chiptune SFX with more control | Output released under CC0 |
| [Vital](https://vital.audio/) | Synth-designed whooshes, risers, magical sparkles, UI tones | Free Basic tier with full synth, 75 presets, 25 wavetables |
| [Audacity](https://www.audacityteam.org/) | Free editing, noise reduction, normalising | Open source; version 4.0.1 on the site |
| [REAPER](https://www.reaper.fm/) | Full DAW for layering and batch render | 60-day evaluation; discounted licence $60 if under $20k yearly revenue, else $225 ([licensing](https://www.reaper.fm/purchase.php)); render reports include loudness ([REAPER](https://www.reaper.fm/)) |
| [FL Studio](https://www.image-line.com/fl-studio) | Music and synthesised SFX | Lifetime free updates per edition |
| [ElevenLabs SFX](https://elevenlabs.io/sound-effects) | Text-to-SFX prototyping | Max 30 s; free plan is personal use only, paid plans allow commercial use |

## Workflows

### 1. Synth SFX in 5 minutes (UI, pickups)
1. Open jsfxr, choose a preset (Pickup/coin, Blip/select), press Mutate until it feels right.
2. Export WAV, trim silence, normalise (below), save as mono for positional use.
3. Make 4 variants for repeated sounds.

### 2. Layered hero sound (ability, explosion, rarity stinger)
1. Sketch the timeline: charge, transient, body, tail.
2. Layer: synth riser (Vital) + foley impact + noise burst + sub. See [[What Makes a Sound Satisfying]].
3. EQ each layer into its lane; use a limiter on the bus.
4. Render the final file at 48 kHz or lower WAV.

### 3. Foley at home
Foley recreates sounds with props: fabric rubbing for movement, a thin stick for whooshes, cornstarch in a leather pouch for snow, frozen lettuce for bone cracks, cellophane for fire ([Wikipedia: Foley](https://en.wikipedia.org/wiki/Foley_(filmmaking))). Record with a phone in a quiet closet, then clean with Audacity noise reduction: sample a noise-only section as profile, apply the lowest reduction that sounds clean, and do click removal before and compression after ([Audacity manual: noise reduction](https://manual.audacityteam.org/man/noise_reduction.html)).

### 4. AI-generated SFX
ElevenLabs generates effects from text prompts; four options per prompt, up to 30 seconds, and the licence restricts building competing products ([ElevenLabs](https://elevenlabs.io/sound-effects)). Its library pages for common sounds require attribution on the free plan ([parry example](https://elevenlabs.io/sound-effects/parry)). Treat AI audio as a draft layer: edit, layer and check the platform's terms before shipping. The Roblox docs also cover AudioTextToSpeech for generated voice ([text-to-speech tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech), [AudioTextToSpeech](https://create.roblox.com/docs/reference/engine/classes/AudioTextToSpeech)).

## Edit, normalise, export

1. Trim start so the transient is at 0 ms; fade tail out (2-10 ms) to avoid clicks.
2. Remove DC/noise, optional EQ high-pass at 20-40 Hz on non-bass sounds.
3. Normalise: peak to about -1 dBFS for short SFX, or loudness-normalise longer assets; Audacity's Loudness Normalization uses a LUFS target (default -23 LUFS, EBU R128) and is meant as the final step ([Audacity manual](https://manual.audacityteam.org/man/loudness_normalization.html), [EBU R128](https://en.wikipedia.org/wiki/EBU_R_128)).
4. Export WAV at a consistent sample rate; mono for 3D sounds. Practitioner advice: uncompressed WAV, matched levels, consistent naming ([Violet Recording](https://violetrecording.com/how-to-design-sound-effects-for-games/)).
5. Test in-game at real volume.

## Roblox upload limits (verified 2026-11-02)

From the current audio assets page ([Roblox docs](https://create.roblox.com/docs/audio/assets)):

- Formats: `.mp3`, `.ogg`, `.wav`, `.flac`; single track or stream.
- Size under **20 MB**; length under **7 minutes**.
- Sample rate **48 kHz or lower**; mono or stereo (also 3.0/5.1 surround).
- Free uploads per 30 days: **2,000** for ID-verified accounts, **100** unverified; the older daily import limit was replaced by this monthly limit. ([Account verification](https://create.roblox.com/docs/production/publishing/account-verification))
- You must hold the rights; the Audio Upload License Agreement applies ([agreement](https://en.help.roblox.com/hc/en-us/articles/23359485439124-Audio-Upload-License-Agreement)).
- Audio goes through moderation before reuse; the Studio importer can reject corrupt files, often caused by outdated tools producing bad headers, so re-export from a current tool.
- Privacy: newly imported audio is usable only by you at first; grant permission to specific friends and experiences ([asset privacy](https://create.roblox.com/docs/projects/assets/privacy)).

Historical changes since 2022: in March 2022 new audio became private by default, existing audio over 6 seconds was privatised, and uploads were made free with monthly limits of 10 (100 with ID verification) ([DevForum announcement](https://devforum.roblox.com/t/1701697)); staff confirmed even 1-second SFX could not be made public ([DevForum](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394)). Verify the numbers again before publishing; they have changed more than once.

Ogg Vorbis is a free lossy format useful for smaller music files ([Wikipedia: Vorbis](https://en.wikipedia.org/wiki/Vorbis)).

## Learning more

- Sound design overview and workflow: [Wikipedia: sound design](https://en.wikipedia.org/wiki/Sound_design), [sound effect](https://en.wikipedia.org/wiki/Sound_effect).
- Gun layers and timing: [Lior Tega](https://www.liortega.com/post/first-person-shooter-gun-sound-design).
- Middleware context: Wwise and FMOD are used in AAA (see [Wikipedia: sound design](https://en.wikipedia.org/wiki/Sound_design) on middleware); Roblox games use the built-in engine, so learn the concepts (events, parameters, buses) and apply them in [[Audio Implementation in Luau]].
- Talk: [The TUNIC audio talk (GDC 2023)](https://www.gdcvault.com/play/1029369/The-TUNIC-Audio), [Understanding the audio needs of a game (GDC 2023)](https://www.gdcvault.com/play/1029386/Understanding-the-Audio-Needs-of).

## References

- [jsfxr](https://sfxr.me/) — tool · retro SFX generator
- [jsfxr on GitHub](https://github.com/chr15m/jsfxr) — repo · library and Unlicense
- [Bfxr](https://www.bfxr.net/) — tool · SFX generator with Footsteppr
- [ChipTone](https://sfbgames.itch.io/chiptone) — tool · CC0 chiptune SFX
- [Vital](https://vital.audio/) — tool · free synth
- [Audacity](https://www.audacityteam.org/) — tool · free editor
- [REAPER](https://www.reaper.fm/) — tool · DAW
- [REAPER licensing](https://www.reaper.fm/purchase.php) — pricing page · licence tiers
- [FL Studio](https://www.image-line.com/fl-studio) — tool · DAW
- [ElevenLabs sound effects](https://elevenlabs.io/sound-effects) — AI tool · text to SFX
- [ElevenLabs parry page](https://elevenlabs.io/sound-effects/parry) — library page · attribution terms
- [Audacity manual: noise reduction](https://manual.audacityteam.org/man/noise_reduction.html) — manual · cleanup steps
- [Audacity manual: loudness normalization](https://manual.audacityteam.org/man/loudness_normalization.html) — manual · LUFS
- [Wikipedia: Foley](https://en.wikipedia.org/wiki/Foley_(filmmaking)) — encyclopedia · prop ideas
- [Wikipedia: sound effect](https://en.wikipedia.org/wiki/Sound_effect) — encyclopedia · categories
- [Wikipedia: sound design](https://en.wikipedia.org/wiki/Sound_design) — encyclopedia · workflow
- [Wikipedia: EBU R 128](https://en.wikipedia.org/wiki/EBU_R_128) — encyclopedia · loudness targets
- [Wikipedia: Vorbis](https://en.wikipedia.org/wiki/Vorbis) — encyclopedia · Ogg Vorbis
- [Violet Recording](https://violetrecording.com/how-to-design-sound-effects-for-games/) — article · export advice
- [Lior Tega](https://www.liortega.com/post/first-person-shooter-gun-sound-design) — article · layered design
- [Roblox: audio assets](https://create.roblox.com/docs/audio/assets) — docs · upload requirements
- [Roblox: Audio Upload License Agreement](https://en.help.roblox.com/hc/en-us/articles/23359485439124-Audio-Upload-License-Agreement) — help · terms
- [Roblox: account verification](https://create.roblox.com/docs/production/publishing/account-verification) — docs · ID verification
- [Roblox: asset privacy](https://create.roblox.com/docs/projects/assets/privacy) — docs · permissions
- [Roblox: add text-to-speech](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) — tutorial · TTS
- [Roblox: AudioTextToSpeech](https://create.roblox.com/docs/reference/engine/classes/AudioTextToSpeech) — docs · class
- [DevForum: audio privacy announcement](https://devforum.roblox.com/t/1701697) — forum · 2022 changes
- [DevForum: 1-second SFX](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394) — forum · staff reply
- [GDC: TUNIC audio talk](https://www.gdcvault.com/play/1029369/The-TUNIC-Audio) — talk page · small-team audio
- [GDC: Understanding the audio needs of a game](https://www.gdcvault.com/play/1029386/Understanding-the-Audio-Needs-of) — talk page · planning

Links: [[Audio MOC]] · [[00 Home]]
