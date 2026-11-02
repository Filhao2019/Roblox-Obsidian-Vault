---
title: Audio References
date: 2026-11-02
tags: [audio, references, links]
status: researched
---

# Audio References

Categorized link library for the audio folder. Every link was opened during research or returned by a search; notes after a dash say what each is good for and flag limits. Sites that blocked automated access (403/402) are marked so you can verify manually. Main notes: [[SFX of Top Games]], [[What Makes a Sound Satisfying]], [[UI Sounds]], [[Combat and Impact Sounds]], [[Ambience and Music]], [[Making SFX]], [[Sound Sources and Libraries]], [[Audio Implementation in Luau]].

## References

### Roblox official documentation: concepts and tutorials
- [Audio overview](https://create.roblox.com/docs/audio) — docs · AudioPlayer, emitter, listener, effects map
- [Audio assets](https://create.roblox.com/docs/audio/assets) — docs · formats, 20 MB, 7 min, 48 kHz, upload limits, privacy
- [Audio objects](https://create.roblox.com/docs/audio/objects) — docs · wiring 2D and 3D
- [Audio effects](https://create.roblox.com/docs/audio/effects) — docs · effect list and chaining
- [Add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) — tutorial · UI/background sound
- [Add 3D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) — tutorial · waterfall attenuation example
- [Add text-to-speech](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) — tutorial · generated voice
- [Sound groups](https://create.roblox.com/docs/sound/groups) — docs · mixer groups and ducking
- [Sound objects](https://create.roblox.com/docs/sound/objects) — docs · legacy positional audio, rolloff
- [Dynamic effects](https://create.roblox.com/docs/sound/dynamic-effects) — docs · legacy effect objects
- [Creator Store](https://create.roblox.com/docs/production/creator-store) — docs · free audio
- [Asset privacy](https://create.roblox.com/docs/projects/assets/privacy) — docs · permissions model
- [Account verification](https://create.roblox.com/docs/production/publishing/account-verification) — docs · ID verification for limits
- [Audio Upload License Agreement](https://en.help.roblox.com/hc/en-us/articles/23359485439124-Audio-Upload-License-Agreement) — help · upload terms
- [Licensed music availability](https://en.help.roblox.com/hc/articles/360000927163) — help · licensed catalog (blocked automated fetch; seen in search)
- [Documentation index (llms.txt)](https://create.roblox.com/docs/llms.txt) — docs · all audio class names

### Roblox API reference: audio classes
- [AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer) — API · Asset, Looping, PlaybackSpeed
- [AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter) — API · distance/angle attenuation
- [AudioListener](https://create.roblox.com/docs/reference/engine/classes/AudioListener) — API · virtual microphone
- [AudioDeviceOutput](https://create.roblox.com/docs/reference/engine/classes/AudioDeviceOutput) — API · speakers
- [AudioDeviceInput](https://create.roblox.com/docs/reference/engine/classes/AudioDeviceInput) — API · microphone input (link seen on audio page)
- [AudioTextToSpeech](https://create.roblox.com/docs/reference/engine/classes/AudioTextToSpeech) — API · TTS (link seen on audio page)
- [AudioAnalyzer](https://create.roblox.com/docs/reference/engine/classes/AudioAnalyzer) — API · volume/frequency inspection (link seen on effects page)
- [Wire](https://create.roblox.com/docs/reference/engine/classes/Wire) — API · connection object
- [AudioCompressor](https://create.roblox.com/docs/reference/engine/classes/AudioCompressor) — API · sidechain ducking
- [AudioFader](https://create.roblox.com/docs/reference/engine/classes/AudioFader) — API · volume stage
- [AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer) — API · band gain
- [AudioReverb](https://create.roblox.com/docs/reference/engine/classes/AudioReverb) — API · room effect
- [AudioLimiter](https://create.roblox.com/docs/reference/engine/classes/AudioLimiter) — API · peak ceiling
- [AudioPitchShifter](https://create.roblox.com/docs/reference/engine/classes/AudioPitchShifter) — API · pitch without speed
- [Sound](https://create.roblox.com/docs/reference/engine/classes/Sound) — API · legacy sound
- [SoundGroup](https://create.roblox.com/docs/reference/engine/classes/SoundGroup) — API · group volume
- [SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService) — API · AmbientReverb, listener location
- [Humanoid](https://create.roblox.com/docs/reference/engine/classes/Humanoid) — API · FloorMaterial
- [Material enum](https://create.roblox.com/docs/reference/engine/enums/Material) — API · surfaces for footsteps

### DevForum and Roblox audio policy history
- [Upcoming changes to asset privacy for audio](https://devforum.roblox.com/t/1701697) — forum · March 2022 announcement
- [1-second SFX can't be made public](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394) — forum · staff confirm intended
- [Add newer APM music](https://devforum.roblox.com/t/add-newer-apm-music/279482) — forum · APM catalogue gap
- [Need recommendations for music in my game](https://devforum.roblox.com/t/need-reccomendations-for-music-in-my-game/875258) — forum · licence discussion
- [Monstercat song library module](https://devforum.roblox.com/t/monstercat-song-library-module/4010644) — forum · Monstercat IDs
- [Bloxtunes](https://devforum.roblox.com/t/bloxtunesco-spotify-like-app-for-roblox-music/3784402) — forum · music-app example
- [Progameguides: Roblox privates sounds](https://progameguides.com/roblox/roblox-to-private-millions-of-user-created-sounds-within-its-audio-database/) — news · recap
- [EDM.com: Monstercat x Roblox](https://edm.com/lifestyle/monstercat-announces-roblox-partnership/) — news · 2020 partnership

### Game audio in top Roblox games
- [Doors wiki: Rush](https://doors-game.fandom.com/wiki/Rush) — wiki · far/near audio, re-recording
- [Doors wiki: Soundtracks](https://doors-game.fandom.com/wiki/Soundtracks) — wiki · soundtrack list
- [Destructoid: Doors entities](https://www.destructoid.com/all-doors-entities-guide-how-to-survive/) — guide · entity cues
- [Ginx: Rush](https://www.ginx.tv/en/doors-rush) — guide · static cue
- [Sportskeeda: Doors entities](https://sportskeeda.com/roblox-news/best-entities-roblox-doors) — article · entity list
- [EaseUS Rush soundboard](https://voicechanger.easeus.com/soundboards/sounds/rush-sound-effect-roblox-doors) — soundboard · meme status
- [Earnaldo: Violence District guide](https://earnaldo.com/blog/violence-district-beginner-guide) — guide · sound-driven play
- [Deltias: Violence District](https://deltiasgaming.com/roblox-how-to-play-violence-district) — guide · warning audio
- [ItemLevel: Sol's RNG settings](https://itemlevel.net/sols-rng-best-settings-guide/) — guide · audio toggles
- [Rblxguide: Symphony aura](https://rblxguide.com/games/sols-rng/auras/symphony) — guide · aura music
- [Droidgamers: Celestial](https://www.droidgamers.com/guides/celestial-sols-rng/) — guide · aura music remarks
- [Bloxodes: Sol's RNG](https://bloxodes.com/wiki/sols-rng) — wiki mirror · aura listings
- [MM2 wiki: Default Gun](https://murder-mystery-2.fandom.com/wiki/Default_Gun) — wiki · starter items
- [Bloxodes: MM2 effects](https://bloxodes.com/wiki/murder-mystery-2/effects) — wiki mirror · knife effects
- [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot) — encyclopedia · concert, character licensing
- [Wikipedia: Italian brainrot](https://en.wikipedia.org/wiki/Italian_brainrot) — encyclopedia · AI voice meme
- [VoxBooster: Italian brainrot soundboard](https://voxbooster.com/blog/italian-brainrot-soundboard) — blog · popular phrases
- [VoxBooster: brainrot soundboard](https://voxbooster.com/blog/brainrot-soundboard/) — blog · sound list (seen in search)
- [Fish Audio: brainrot narrator](https://fish.audio/m/4d45631184584ce1b2eda4e06ae14e5f) — AI voice · style reproduction
- [Wikipedia: Dress to Impress](https://en.wikipedia.org/wiki/Dress_to_Impress_(video_game)) — encyclopedia · music collaborations
- [Gameleap: DTI musical theme](https://www.gameleap.com/articles/dress-to-impress-musical-theme-explained-ideas) — guide · outfit theme only
- [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden) — encyclopedia · classical soundtrack
- [Wikipedia: Adopt Me!](https://en.wikipedia.org/wiki/Adopt_Me!) — encyclopedia · no audio detail
- [Wikipedia: Roblox games (Doors article)](https://en.wikipedia.org/wiki/Doors_(Roblox)) — encyclopedia · awards, licensing
- [ElevenLabs: parry sounds](https://elevenlabs.io/sound-effects/parry) — library · parry samples
- [Morphic: parry sound effects](https://morphic.com/resources/sounds/parry-sound-effects) — library · parry samples

### Dead by Daylight audio model (template for horror proximity music)
- [Chase music](https://deadbydaylight.wiki.gg/wiki/Chase_Music) — wiki · layer system
- [Heartbeat](https://deadbydaylight.wiki.gg/wiki/Heartbeat) — wiki · proximity layer
- [Lullaby](https://deadbydaylight.wiki.gg/wiki/Lullaby) — wiki · lullaby layer

### Sound design theory and craft
- [Lior Tega: FPS gun sound design](https://www.liortega.com/post/first-person-shooter-gun-sound-design) — article · five-layer shots
- [Violet Recording: SFX for games](https://violetrecording.com/how-to-design-sound-effects-for-games/) — article · variation, export
- [Wayline: game audio lesson](https://www.wayline.io/learn/game-audio/1) — course · fundamentals
- [Wikipedia: sound design](https://en.wikipedia.org/wiki/Sound_design) — encyclopedia · game sound design
- [Wikipedia: sound effect](https://en.wikipedia.org/wiki/Sound_effect) — encyclopedia · categories
- [Wikipedia: Foley](https://en.wikipedia.org/wiki/Foley_(filmmaking)) — encyclopedia · prop techniques
- [Wikipedia: dynamic music](https://en.wikipedia.org/wiki/Dynamic_music) — encyclopedia · layering vs resequencing
- [Wikipedia: dynamic range compression](https://en.wikipedia.org/wiki/Dynamic_range_compression) — encyclopedia · sidechain
- [Wikipedia: psychoacoustics](https://en.wikipedia.org/wiki/Psychoacoustics) — encyclopedia · masking
- [Wikipedia: Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) — encyclopedia · flyby pitch
- [Wikipedia: loudness](https://en.wikipedia.org/wiki/Loudness) — encyclopedia · LUFS and perception
- [Wikipedia: EBU R 128](https://en.wikipedia.org/wiki/EBU_R_128) — encyclopedia · loudness targets
- [Wikipedia: Vorbis](https://en.wikipedia.org/wiki/Vorbis) — encyclopedia · Ogg format

### GDC talks (game audio)
- [Back 4 Blood: interactive music](https://www.gdcvault.com/play/1029247/Music-Design-Is-Composition-Interactive) — talk · music as composition
- [Hunting with Hits](https://www.gdcvault.com/play/1028797/Hunting-with-Hits-Tempo-Slaying) — talk · hit-driven rhythm
- [Understanding the audio needs of a game](https://www.gdcvault.com/play/1029386/Understanding-the-Audio-Needs-of) — talk · planning
- [The TUNIC audio talk](https://www.gdcvault.com/play/1029369/The-TUNIC-Audio) — talk · small team
- [Sounds as Intended: QA](https://www.gdcvault.com/play/1028854/Audio-Summit-Sounds-as-Intended) — talk · audio QA
- [Dying Light 2 open-world audio](https://www.gdcvault.com/play/1029272/Open-World-Audio-in-Dying) — talk · large-scale systems
- [Dial up the diegetics](https://www.gdcvault.com/play/1034172/Dial-Up-the-Diegetics-Musical) — talk · musical SFX
- [How do you make casual players turn audio on](https://www.gdcvault.com/play/1034493/Audio-Summit-How-Do-You) — talk · casual audience
- [Diablo IV living audio](https://www.gdcvault.com/play/1034343/-Diablo-IV-Audio-Systems) — talk · audio systems
- [Adapting Foley techniques for interactivity](https://www.gdcvault.com/play/1034394/Adapting-Foley-Techniques-for-Interactivity) — talk · foley
- [Developing strong musical identity](https://www.gdcvault.com/play/1034510/Audio-Summit-Developing-Strong-Musical) — talk · identity
- [Avatar ambient sound](https://www.gdcvault.com/play/1034385/Everything-is-Connected-Ambient-Sound) — talk · ambience
- [Destiny 2 music across activities](https://www.gdcvault.com/play/1034383/-Destiny-2-Weaving-Music) — talk · adaptive music
- [Creature vocalizations](https://www.gdcvault.com/play/1034233/Creature-Vocalizations-The-Art-of) — talk · monster sound design
- [GDC 2023 audio listing](https://www.gdcvault.com/browse/gdc-23/?categories=Audio) — index · all 2023 audio talks
- [GDC 2024 audio listing](https://www.gdcvault.com/browse/gdc-24/?categories=Audio) — index · all 2024 audio talks

### Tools
- [jsfxr](https://sfxr.me/) — web tool · retro SFX
- [jsfxr GitHub](https://github.com/chr15m/jsfxr) — repo · library
- [Bfxr](https://www.bfxr.net/) — web tool · SFX plus footsteps
- [ChipTone](https://sfbgames.itch.io/chiptone) — tool · CC0 SFX
- [Vital](https://vital.audio/) — synth · free tier
- [Audacity](https://www.audacityteam.org/) — editor · free
- [Audacity: loudness normalization](https://manual.audacityteam.org/man/loudness_normalization.html) — manual · LUFS
- [Audacity: noise reduction](https://manual.audacityteam.org/man/noise_reduction.html) — manual · cleanup
- [REAPER](https://www.reaper.fm/) — DAW · overview
- [REAPER licensing](https://www.reaper.fm/purchase.php) — pricing · tiers
- [FL Studio](https://www.image-line.com/fl-studio) — DAW · editions
- [ElevenLabs sound effects](https://elevenlabs.io/sound-effects) — AI · text to SFX

### Libraries and licences
- [Sonniss GDC audio](https://sonniss.com/gameaudiogdc/) — library · free bundles
- [Kenney audio](https://kenney.nl/assets/category:Audio) — library · packs
- [Freesound](https://freesound.org/) — library · community sounds
- [Freesound FAQ](https://freesound.org/help/faq/) — help · licences
- [Pixabay licence summary](https://pixabay.com/service/license-summary/) — licence · terms
- [Mixkit licence](https://mixkit.co/license/) — licence · index
- [Zapsplat](https://www.zapsplat.com/) — library · blocked fetch
- [OpenGameArt](https://opengameart.org/) — library · blocked fetch
- [Incompetech](https://incompetech.com/music/royalty-free/) — music · see licence pages
- [FreePD](https://freepd.com/) — music · closed
- [Wikipedia: Creative Commons licences](https://en.wikipedia.org/wiki/Creative_Commons_license) — encyclopedia · BY/NC/SA/ND/CC0
- [Wikipedia: Monstercat](https://en.wikipedia.org/wiki/Monstercat) — encyclopedia · label

Links: [[Audio MOC]] · [[00 Home]]
