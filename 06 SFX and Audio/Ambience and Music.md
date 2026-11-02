---
title: Ambience and Music
date: 2026-11-02
tags: [audio, music, ambience, licensing, loudness]
status: researched
---

# Ambience and Music

Ambience beds make a place feel real; music sets pace and emotion; both must stay under gameplay-critical sounds. This note covers ambience layering, adaptive and chase music, lobby music, Roblox music licensing since the 2022 audio privacy change, and loudness targets. Examples from the chart are in [[SFX of Top Games]].

## Ambience beds

- Build a place from 2-4 loops: a **base bed** (wind, room tone), **mid details** (insects, machinery) and **spot one-shots** triggered at random intervals (distant creature, drip). [[99 Nights in the Forest]] and [[Doors]] rely on this for tension (genre pattern, game-specific cues unverified).
- Keep loops low in the mix and seamless; ambience must not draw attention ([Violet Recording](https://violetrecording.com/how-to-design-sound-effects-for-games/)).
- Zones: crossfade beds by region (outdoor, cave, interior). `SoundService.AmbientReverb` switches a global reverb type, and the docs show it changing when the player enters a tagged cave part ([SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService)). With the new API use [AudioReverb](https://create.roblox.com/docs/reference/engine/classes/AudioReverb) and an [AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer) (underwater muffling is the docs' own example, [audio effects](https://create.roblox.com/docs/audio/effects)).
- Positional ambience (a waterfall, a campfire) uses an emitter with a distance curve; the 3D tutorial uses a waterfall at 0.8 volume by 20 studs and silence by 80 ([add 3D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio)).
- Large-scale ambience design talks: [Avatar: Frontiers of Pandora ambient sound (GDC 2024)](https://www.gdcvault.com/play/1034385/Everything-is-Connected-Ambient-Sound), [Dying Light 2 open-world audio (GDC 2023)](https://www.gdcvault.com/play/1029272/Open-World-Audio-in-Dying).

## Adaptive and dynamic music

Adaptive music reacts to game state. Two main techniques ([Wikipedia: dynamic music](https://en.wikipedia.org/wiki/Dynamic_music)):

- **Vertical layering**: stems fade in and out over a shared loop (calm: pad only; danger: add percussion; chase: add lead). Dead Space 2 is cited as mixing four fear layers by enemy distance.
- **Horizontal re-sequencing**: switch between sections on phrase boundaries or with bridges, for bigger changes (enter fight, round start).

Roblox recipe: keep all stems as synchronised looping `Sound`s or `AudioPlayer`s with the same `TimePosition`, and tween each stem's volume ([AudioFader](https://create.roblox.com/docs/reference/engine/classes/AudioFader) or a plain volume tween). Start stems in the same frame; verify drift. Code scaffold in [[Audio Implementation in Luau]].

### Chase music

Horror and asymmetric games ([[Violence District]], [[Forsaken]], [[Evade]]) use proximity layers plus a chase layer. The Dead by Daylight model: the terror radius is split into three zones, each playing a layer; a fourth layer (chase music) replaces the closest during a chase, and the killer hears only chase music ([DBD wiki: chase music](https://deadbydaylight.wiki.gg/wiki/Chase_Music), [heartbeat](https://deadbydaylight.wiki.gg/wiki/Heartbeat), [lullaby](https://deadbydaylight.wiki.gg/wiki/Lullaby)). Violence District guides tell players the radius audio is their early warning ([Earnaldo](https://earnaldo.com/blog/violence-district-beginner-guide)). Talks on interactive horror music: [Back 4 Blood (GDC 2023)](https://www.gdcvault.com/play/1029247/Music-Design-Is-Composition-Interactive).

### Lobby and hub music

Short, friendly, loopable (60-120 s), narrow dynamic range so it never fatigues; swap seasonally. [[Grow a Garden]] uses a classical-music soundtrack according to Wikipedia ([Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden)). [[Dress To Impress]] ties runway rounds to pop music, with 2024 and 2025 artist collaborations ([Wikipedia](https://en.wikipedia.org/wiki/Dress_to_Impress_(video_game))). For [[Sols RNG]] each aura has its own score and players can disable background music ([ItemLevel](https://itemlevel.net/sols-rng-best-settings-guide/)). Always offer a music toggle.

### Stingers

Short musical phrases for events (round win, rare drop). Duck the bed, play the stinger, restore; ensure the stinger is in the same key as the bed or arrives on a quiet moment. See [[UI Sounds]] for rarity stingers.

## Music licensing on Roblox

History and current practice:

- **APM Music (2018 license)**: Roblox signed with APM to give creators a large licensed library; unlicensed music flagged by moderation can be replaced with licensed music ([Roblox help: licensed music](https://en.help.roblox.com/hc/articles/360000927163)). Developers complained that APM tracks after mid-2018 were missing ([DevForum: add newer APM music](https://devforum.roblox.com/t/add-newer-apm-music/279482)).
- **Monstercat (2020)**: reported as giving developers free use of 51 tracks at the time ([EDM.com](https://edm.com/lifestyle/monstercat-announces-roblox-partnership/)); a community module lists nearly 100 tracks from Monstercat's official Roblox account ([DevForum](https://devforum.roblox.com/t/monstercat-song-library-module/4010644); the author's safety claim is unverified). Monstercat is a Vancouver label founded in 2011 ([Wikipedia](https://en.wikipedia.org/wiki/Monstercat)).
- **March 2022 audio privacy**: new audio became private by default and existing audio over 6 seconds was set to private; Roblox's licensed catalog and audio from Roblox partners (APM, Monstercat, Pro Sound Effects, Nettwerk, Position Music) stayed usable; the catalog added over 100,000 songs and SFX ([DevForum announcement](https://devforum.roblox.com/t/1701697)). Press recap: [Progameguides](https://progameguides.com/roblox/roblox-to-private-millions-of-user-created-sounds-within-its-audio-database/). Staff confirmed that short SFX also became non-public by design ([DevForum](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394)).
- **Today**: upload only audio you have rights to; assets are private to you until you grant permission to experiences or friends ([audio assets](https://create.roblox.com/docs/audio/assets), [asset privacy](https://create.roblox.com/docs/projects/assets/privacy)). Free Creator Store audio exists ([Creator Store](https://create.roblox.com/docs/production/creator-store)). Check each track's licence; some licensing terms discussed on the DevForum limit using licensed tracks to build a music library inside an experience or charging per track (quoted second-hand, unverified) ([DevForum](https://devforum.roblox.com/t/need-reccomendations-for-music-in-my-game/875258)).
- **Real-world risk**: Wikipedia records a Roblox game (Notoriety) that originally used another game's soundtrack without permission and later relaunched under a 2024 licensing deal ([Wikipedia](https://en.wikipedia.org/wiki/Doors_(Roblox))). Do not ship ripped music.
- Songs uploaded by ID-verified users can show on a game's details page if they pass moderation and copyright checks ([audio assets](https://create.roblox.com/docs/audio/assets)).
- Music players inside games (Brookhaven-style boomboxes, [[Brookhaven RP]]) need licensed tracks only; community players like [Bloxtunes](https://devforum.roblox.com/t/bloxtunesco-spotify-like-app-for-roblox-music/3784402) show demand.

See [[Sound Sources and Libraries]] for free music sources and [[Making SFX]] for upload specs.

## Loudness

- Broadcast norm: EBU R128 targets -23 LUFS integrated with a -1 dBTP ceiling; streaming platforms target about -14 to -16 LUFS ([Wikipedia: EBU R128](https://en.wikipedia.org/wiki/EBU_R_128)). LUFS follows ITU-R BS.1770 ([Wikipedia: loudness](https://en.wikipedia.org/wiki/Loudness)).
- Roblox has no official game loudness target (unverified); a practical approach: master music around -16 to -18 LUFS, SFX peaks around -3 dBFS, ambience -30 to -24 LUFS short-term, and test against voice chat.
- Audacity can normalise to a LUFS target as a final export step ([Audacity manual](https://manual.audacityteam.org/man/loudness_normalization.html)).
- Add an [AudioLimiter](https://create.roblox.com/docs/reference/engine/classes/AudioLimiter) on the master path to catch spikes.
- Mix with music below dialogue/critical cues; music typically sits 6-12 dB under SFX peaks (rule of thumb, unverified).

## References

- [DBD wiki: chase music](https://deadbydaylight.wiki.gg/wiki/Chase_Music) — wiki · layers model
- [DBD wiki: heartbeat](https://deadbydaylight.wiki.gg/wiki/Heartbeat) — wiki · heartbeat layer
- [DBD wiki: lullaby](https://deadbydaylight.wiki.gg/wiki/Lullaby) — wiki · lullaby layer
- [Wikipedia: dynamic music](https://en.wikipedia.org/wiki/Dynamic_music) — encyclopedia · vertical/horizontal
- [Earnaldo: Violence District](https://earnaldo.com/blog/violence-district-beginner-guide) — guide · radius audio
- [ItemLevel: Sol's RNG settings](https://itemlevel.net/sols-rng-best-settings-guide/) — guide · music toggle
- [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden) — encyclopedia · classical soundtrack
- [Wikipedia: Dress to Impress](https://en.wikipedia.org/wiki/Dress_to_Impress_(video_game)) — encyclopedia · artist tie-ins
- [Wikipedia: Roblox games (Doors article)](https://en.wikipedia.org/wiki/Doors_(Roblox)) — encyclopedia · Notoriety licensing example and awards
- [Violet Recording](https://violetrecording.com/how-to-design-sound-effects-for-games/) — article · ambience guidance
- [Roblox help: licensed music](https://en.help.roblox.com/hc/articles/360000927163) — help · APM licence (seen in search results)
- [DevForum: add newer APM music](https://devforum.roblox.com/t/add-newer-apm-music/279482) — forum · APM gap (seen in search results)
- [DevForum: music recommendations](https://devforum.roblox.com/t/need-reccomendations-for-music-in-my-game/875258) — forum · licence discussion (seen in search results)
- [DevForum: Monstercat module](https://devforum.roblox.com/t/monstercat-song-library-module/4010644) — forum · track list module
- [DevForum: Bloxtunes](https://devforum.roblox.com/t/bloxtunesco-spotify-like-app-for-roblox-music/3784402) — forum · in-game music apps (seen in search results)
- [EDM.com: Monstercat x Roblox](https://edm.com/lifestyle/monstercat-announces-roblox-partnership/) — news · 2020 partnership (seen in search results)
- [Wikipedia: Monstercat](https://en.wikipedia.org/wiki/Monstercat) — encyclopedia · label background
- [DevForum: audio privacy announcement](https://devforum.roblox.com/t/1701697) — forum · March 2022 changes
- [DevForum: 1-second SFX can't be public](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394) — forum · staff confirmation
- [Progameguides: Roblox privates user sounds](https://progameguides.com/roblox/roblox-to-private-millions-of-user-created-sounds-within-its-audio-database/) — news · recap (seen in search results)
- [Roblox: audio assets](https://create.roblox.com/docs/audio/assets) — docs · current upload and privacy rules
- [Roblox: asset privacy](https://create.roblox.com/docs/projects/assets/privacy) — docs · permissions (link seen on audio assets page)
- [Roblox: Creator Store](https://create.roblox.com/docs/production/creator-store) — docs · free audio (link seen on audio page)
- [Roblox: SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService) — docs · AmbientReverb
- [Roblox: audio effects](https://create.roblox.com/docs/audio/effects) — docs · underwater EQ example
- [Roblox: add 3D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) — tutorial · attenuation
- [Roblox: AudioFader](https://create.roblox.com/docs/reference/engine/classes/AudioFader) — docs · stem fades
- [Roblox: AudioReverb](https://create.roblox.com/docs/reference/engine/classes/AudioReverb) — docs · reverb
- [Roblox: AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer) — docs · muffling
- [Roblox: AudioLimiter](https://create.roblox.com/docs/reference/engine/classes/AudioLimiter) — docs · master limiter
- [Wikipedia: EBU R 128](https://en.wikipedia.org/wiki/EBU_R_128) — encyclopedia · LUFS targets
- [Wikipedia: loudness](https://en.wikipedia.org/wiki/Loudness) — encyclopedia · LUFS definition
- [Audacity manual: loudness normalization](https://manual.audacityteam.org/man/loudness_normalization.html) — manual · LUFS workflow
- [GDC: Avatar ambient sound](https://www.gdcvault.com/play/1034385/Everything-is-Connected-Ambient-Sound) — talk page · ambience design
- [GDC: Dying Light 2 open-world audio](https://www.gdcvault.com/play/1029272/Open-World-Audio-in-Dying) — talk page · open-world
- [GDC: Back 4 Blood music](https://www.gdcvault.com/play/1029247/Music-Design-Is-Composition-Interactive) — talk page · interactive music


## Visual study

- [[Spatial Audio Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[Audio MOC]] · [[00 Home]]
