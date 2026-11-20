---
title: Sound Sources and Libraries
date: 2026-11-02
tags: [audio, sources, licensing, libraries]
status: researched
---

# Sound Sources and Libraries

Where to get sounds legally for a Roblox game, with licence notes. Rule zero: Roblox requires that you hold the rights to anything you upload ([audio assets](https://create.roblox.com/docs/audio/assets)), so the licence must allow commercial use, modification and embedding in a distributed game. This is not legal advice; read each licence before use. Related: [[Making SFX]], [[Ambience and Music]], [[Free and Paid Asset Sources]].

## Comparison

| Source | Cost | Commercial game use | Attribution | Key caveat |
|---|---|---|---|---|
| Roblox Creator Store audio | Free | Yes, inside Roblox | Per asset | Roblox-uploaded/licensed catalog stays public; user uploads follow privacy rules |
| Sonniss GDC bundles | Free | Yes | None | No reselling or redistribution as SFX; AI/ML training prohibited |
| Kenney | Free | Check each pack page | Check pack | Site listing did not show licence text when fetched |
| Freesound | Free | Depends on per-sound licence | CC-BY needs credit | Avoid CC-BY-NC for monetised games |
| Pixabay | Free | Yes | Not required | No standalone redistribution |
| Mixkit | Free | Per its SFX licence | Check | Licence is separate per item type |
| Zapsplat | Free/paid | Yes under its licence | Free tier needs credit (verify) | Site blocked automated fetch; verify terms |
| OpenGameArt | Free | Per asset (CC0, CC-BY, GPL...) | Varies | Site blocked automated fetch; verify per asset |
| ChipTone / jsfxr output | Free | Yes (CC0 / Unlicense library) | None | Synthetic style |
| ElevenLabs | Free personal; paid commercial | Paid plans | Free plan requires credit on library pages | No use to build competing products |

## Roblox Creator Store audio

- Free-to-use sound effects and music tracks live in the Creator Store and Toolbox ([audio overview](https://create.roblox.com/docs/audio), [Creator Store docs](https://create.roblox.com/docs/production/creator-store), [Toolbox](https://create.roblox.com/docs/projects/assets/toolbox)).
- Since March 2022, third-party user audio is private by default; Roblox's licensed catalog and audio from partners (APM, Monstercat, Pro Sound Effects, Nettwerk, Position Music) remained usable ([DevForum](https://devforum.roblox.com/t/1701697)).
- Only use IDs you found in the Toolbox or documented by the owner. Do not copy IDs from other games; many are private and will fail silently. Use the Audio Discovery plugin (announced 2022) to find audio that needs replacing.
- Community modules listing licensed tracks exist, such as nearly 100 Monstercat tracks ([DevForum](https://devforum.roblox.com/t/monstercat-song-library-module/4010644); safety claim by the author, unverified). History of APM/Monstercat deals: [[Ambience and Music]].

## Sonniss GDC game audio bundles

Annual free bundles 2015-2024 (no 2025 bundle; a 2026 page exists), ranging from 9 GB to 48 GB per year. The licence is royalty-free, commercial, no attribution, unlimited projects, editing allowed; you may not resell or redistribute the sounds as SFX or sample packs, and use for AI/ML training is prohibited ([Sonniss GDC audio](https://sonniss.com/gameaudiogdc/)). Great for Foley, impacts, ambiences. Downloads are huge: use selectively and convert to mono/48 kHz before upload.

## Kenney

Kenney publishes packs including Interface Sounds, UI Audio, Impact Sounds, Digital Audio, Sci-fi Sounds, RPG Audio, Casino Audio, Music Jingles and voiceover packs ([Kenney audio](https://kenney.nl/assets/category:Audio)). The category page did not show the licence; check each pack page before use (Kenney's assets are widely known as CC0, unverified here).

## Freesound

A collaborative database run by Universitat Pompeu Fabra with roughly 738,000 sounds at the time of fetch ([Freesound](https://freesound.org/)). Licences per sound: **CC0** (use freely), **CC-BY** (credit creator, name, link, licence), **CC-BY-NC** (no commercial use, avoid for monetised games), and legacy Sampling+ ([Freesound FAQ](https://freesound.org/help/faq/)). Remix rules: a CC-BY source cannot be relicensed CC0. In-game credits: put a credits panel and link the attribution list. Background on licence elements: [Wikipedia: Creative Commons licenses](https://en.wikipedia.org/wiki/Creative_Commons_license).

## Pixabay

The Pixabay content licence allows free use without attribution and modification; it prohibits selling content standalone with no creative effort, misleading use, and using it as part of a trademark ([Pixabay licence summary](https://pixabay.com/service/license-summary/)). Note that Roblox uploads must still be your rights to upload; derivative creative use inside a game is generally the intent, but confirm terms (unverified for Roblox specifically).

## Mixkit, Zapsplat, OpenGameArt, others

- **Mixkit**: has a dedicated Sound Effects Free License separate from other item types ([Mixkit licence](https://mixkit.co/license/)).
- **Zapsplat** and **OpenGameArt**: both are major libraries ([Zapsplat](https://www.zapsplat.com/), [OpenGameArt](https://opengameart.org/)) but both returned 403 to automated fetching, so licence details here are unverified. OpenGameArt hosts assets under multiple licences (CC0, CC-BY, CC-BY-SA, GPL); filter to CC0/CC-BY.
- **Incompetech** (royalty-free music) has separate licence and FAQ pages; check them for attribution rules ([Incompetech](https://incompetech.com/music/royalty-free/)).
- **FreePD** (public domain music) permanently closed in 2025 ([FreePD](https://freepd.com/)).
- **BBC sound effects archive** has a restricted licensing page; automated access was blocked, so check it directly before use.
- **ElevenLabs** library pages and generator: free plan requires attribution on library clips; paid plans do not and allow commercial projects; royalty-free but no competing products ([parry page](https://elevenlabs.io/sound-effects/parry), [SFX tool](https://elevenlabs.io/sound-effects)).
- Generic parry library sample from another vendor: [Morphic parry sound effects](https://morphic.com/resources/sounds/parry-sound-effects) (seen in search results; licence unverified).

## Licence quick rules

1. Prefer CC0 and explicit "commercial use, no attribution" licences.
2. Keep a spreadsheet: file, source URL, licence, attribution text, date.
3. Avoid NC, ND and ShareAlike sources for game audio ([Wikipedia: CC licences](https://en.wikipedia.org/wiki/Creative_Commons_license)).
4. Never rip audio from other games, songs or YouTube; Roblox moderation and copyright checks apply ([audio assets](https://create.roblox.com/docs/audio/assets)). Real example: a Roblox game that used another game's soundtrack without permission had to relicense ([Wikipedia](https://en.wikipedia.org/wiki/Doors_(Roblox))).
5. Meme audio is risky: the Tung Tung Tung Sahur character was pulled from [[Steal a Brainrot]] over a licensing dispute and later restored ([Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot)).

## References

- [Roblox: audio overview](https://create.roblox.com/docs/audio) — docs · Creator Store audio
- [Roblox: audio assets](https://create.roblox.com/docs/audio/assets) — docs · rights requirement
- [Roblox: Creator Store](https://create.roblox.com/docs/production/creator-store) — docs · store overview
- [Roblox: Toolbox](https://create.roblox.com/docs/projects/assets/toolbox) — docs · finding assets (link seen on audio assets page)
- [DevForum: audio privacy announcement](https://devforum.roblox.com/t/1701697) — forum · partners' audio stays public
- [DevForum: Monstercat module](https://devforum.roblox.com/t/monstercat-song-library-module/4010644) — forum · track list
- [Sonniss GDC game audio](https://sonniss.com/gameaudiogdc/) — library · licence and sizes
- [Kenney audio](https://kenney.nl/assets/category:Audio) — library · packs list
- [Freesound](https://freesound.org/) — library · home
- [Freesound FAQ](https://freesound.org/help/faq/) — help · licences and attribution
- [Wikipedia: Creative Commons licence](https://en.wikipedia.org/wiki/Creative_Commons_license) — encyclopedia · licence elements
- [Pixabay licence summary](https://pixabay.com/service/license-summary/) — licence · allowed and prohibited
- [Mixkit licence](https://mixkit.co/license/) — licence index · per-type licences
- [Zapsplat](https://www.zapsplat.com/) — library · seen but blocked, verify terms
- [OpenGameArt](https://opengameart.org/) — library · seen but blocked, verify terms
- [Incompetech](https://incompetech.com/music/royalty-free/) — music library · see licence pages
- [FreePD](https://freepd.com/) — music library · closed 2025
- [Morphic parry sounds](https://morphic.com/resources/sounds/parry-sound-effects) — library · seen in search results
- [ElevenLabs sound effects](https://elevenlabs.io/sound-effects) — AI tool · commercial terms
- [ElevenLabs parry page](https://elevenlabs.io/sound-effects/parry) — library page · attribution rule
- [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot) — encyclopedia · meme licensing dispute
- [Wikipedia: Roblox games (Doors article)](https://en.wikipedia.org/wiki/Doors_(Roblox)) — encyclopedia · Notoriety soundtrack case

Links: [[Audio MOC]] · [[00 Home]]
