---
title: Thumbnails Icons and Titles
date: 2026-11-02
tags: [game-design, thumbnails, icons, titles, ctr]
status: researched
---

# Thumbnails Icons and Titles

The icon, thumbnails and title are your ad on the Home page, in search and in Sponsored placements. Roblox measures their effect as **qualified play-through rate** (the share of new users who engage after seeing an impression) and requires a custom thumbnail for Home recommendation impressions ([Acquisition](https://create.roblox.com/docs/en-us/production/analytics/acquisition), [Discovery](https://create.roblox.com/docs/discovery)). Chart context: [[Top Games Chart 2026-11-02]]. Related: [[Roblox Discovery Algorithm and Metrics]], [[Live Ops and Update Cadence]], [[What Makes a Roblox Game Go Viral]].

## Official rules and numbers

- Up to **10** images or videos on the details page; thumbnails are 16:9, ideally 1920x1080; formats .jpg, .gif, .png, .tga, .bmp; non-16:9 images are stretched ([Thumbnails](https://create.roblox.com/docs/production/promotion/thumbnails)).
- Videos: 3 uploads per month quota, not supported on Xbox, PlayStation or VR; prohibited: misrepresented gameplay, real-world footage, voice-over, lyrical music, ads ([Thumbnails](https://create.roblox.com/docs/production/promotion/thumbnails)).
- Keep essential text away from the bottom edge where player-count metadata can cover it (same page).
- **Home page thumbnail personalization:** activate 2–5 thumbnails (min. 2); Roblox shows each to random user segments then gives more impressions to the winner per segment. Roblox reports an average +8.5% qualified play-through rate in testing and up to +50% for some games. Keep multiple active; test several new thumbnails with each major update; results appear in a Thumbnail Performance table after a few hours (impressions, qualified plays, avg playtime, QPTR, winning segment) ([Thumbnails](https://create.roblox.com/docs/production/promotion/thumbnails)).
- Metadata that is mismatched, implies monetary giveaways, or copies other experiences is less recommended ([Discovery](https://create.roblox.com/docs/discovery)). A DevForum commenter warned that editing a description once dropped a game from search (single anecdote) ([DevForum](https://devforum.roblox.com/t/make-your-game-populargood/3024181)).
- Event pages can carry their own thumbnail, and up to 5 experience-event thumbnails exist ([Experience events](https://create.roblox.com/docs/production/promotion/experience-events), [Discovery](https://create.roblox.com/docs/discovery)).
- Ads Manager takes up to 10 thumbnails per campaign at 16:9 and offers AI variants ([Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager)).
- Free camera for capturing screenshots: Left Shift + P during a solo playtest ([Thumbnails](https://create.roblox.com/docs/production/promotion/thumbnails)).

## Patterns seen on the chart (2026-11-02)

Observed from the Top Playing Now screenshots and titles in the chart note:

| Pattern | Examples | Why it works |
|---|---|---|
| **Bold character / pet close-up** | Egg and pet characters for [[Steal An Egg]] / [[Break and Steal an Egg]]; meme figures for [[Steal a Brainrot]] | One focal subject, readable at small size |
| **Huge numbers in the art** | Income values like "$997,151,167/s" | Signals idle-income fantasy and scale |
| **Event emoji in the title** | 🎃 on many titles in Halloween week | Calendar relevance, standout glyph in a list |
| **Bracketed update tags** | [UPD 21], [WEEK 2 x BUTCHER] | Tells returning players there is news; refresh reason |
| **Rarity / mutation glow** | Rainbow/gold items | Instant value cue |
| **High-saturation backgrounds, warm colors** | Orange/red/yellow | Contrast against Roblox's dark UI |
| **Text hooks of 1–3 words** | "NEW", "RARE", "x2" | Readable in a tile |
| **Faces with emotion** | Stylized shocked/excited characters | Click magnet (informal advice) |

Informal design advice from one analyst blog (opinion, based on developer reports): one focal point, visible emotion, tiles ~150x150 px so text under ~40 px source size disappears, no more than five elements, and a hook of about three words ([RoWatcher thumbnail guide](https://rowatcher.com/news/the-roblox-thumbnail-is-a-conversion-ad-stop-designing-it-like-art)). The same site claims 20–40% CTR gains from high-contrast single-subject art (informal, unverified) and discusses A/B methodology ([RoWatcher A/B testing](https://rowatcher.com/news/roblox-thumbnail-a-b-testing-what-the-data-actually-shows)).

## Titles

- Core title: the genre promise ("Steal a ..."), then a modifier.
- Prefix/suffix tags that mark freshness: [UPD 21], [NEW], 🎃, 🎄. They are a standard CTR lever but must be updated or removed (stale "[UPD 14]" looks dead).
- A DevForum poster recommends updating the game name to signal new content, e.g., adding a bracketed theme ([DevForum](https://devforum.roblox.com/t/make-your-game-populargood/3024181)). Check current Roblox naming rules for the Name field before relying on emojis (verify in Studio/Creator Dashboard).
- Title + icon + thumbnail must tell the same story; mismatch hurts bounce rate (a ranking input) ([Discovery](https://create.roblox.com/docs/discovery)).
- Avoid claims of free Robux/giveaways and avoid lookalike names of other games (non-unique penalty).

## Icon vs thumbnail

- **Icon:** square, tiny, appears in lists and on the Home grid; make one subject, high contrast, no text or max one word.
- **Thumbnail:** 16:9, appears on the details page and Home carousel; show the best moment of the actual game (what players will experience).
- **Video thumbnail:** short, no voice-over, curated highlights with UI text allowed.

## A/B testing workflow

1. Create 3–5 candidate thumbnails varying one variable (subject, color, text, number).
2. Activate 2–5 for **personalization**; Roblox optimizes by segment ([Thumbnails](https://create.roblox.com/docs/production/promotion/thumbnails)).
3. Wait for statistically meaningful impressions; track QPTR, average playtime and winning segment, not just clicks.
4. Judge QPTR with Acquisition analytics > Home Recommendations ([Acquisition](https://create.roblox.com/docs/en-us/production/analytics/acquisition)).
5. Replace the loser with a new variant at each major update; leave unchanged until the next update (Roblox's recommendation).
6. Use paid campaigns to test creatives: Ads Manager allows 10 thumbnails and says engagement campaigns need 3–5 days before judging ([Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager)).

## Production checklist

- [ ] 16:9, 1920x1080, key content in the top two-thirds.
- [ ] One focal subject readable in a 150-px tile.
- [ ] Number/rarity/event cue present.
- [ ] Not misleading; matches first minute of gameplay.
- [ ] 3+ variants live for personalization.
- [ ] Event version ready for each holiday (Halloween, Christmas, summer).
- [ ] Localized text avoided or minimized.
- [ ] Update tag in title matches the current patch.

## References

- [Thumbnails (Creator Docs)](https://create.roblox.com/docs/production/promotion/thumbnails) — official docs · specs, personalization, +8.5% QPTR
- [Discovery (Creator Docs)](https://create.roblox.com/docs/discovery) — official docs · custom thumbnail required, metadata penalties
- [Acquisition analytics (Creator Docs)](https://create.roblox.com/docs/en-us/production/analytics/acquisition) — official docs · play-through metrics
- [Experience events (Creator Docs)](https://create.roblox.com/docs/production/promotion/experience-events) — official docs · event thumbnails
- [Ads Manager (Creator Docs)](https://create.roblox.com/docs/production/promotion/ads-manager) — official docs · creative limits and testing windows
- [Make your game popular/good (DevForum)](https://devforum.roblox.com/t/make-your-game-populargood/3024181) — forum · icon, name tag tips
- [Roblox thumbnail is a conversion ad (RoWatcher)](https://rowatcher.com/news/the-roblox-thumbnail-is-a-conversion-ad-stop-designing-it-like-art) — blog · design rules (opinion)
- [Roblox thumbnail A/B testing (RoWatcher)](https://rowatcher.com/news/roblox-thumbnail-a-b-testing-what-the-data-actually-shows) — blog · testing method (unverified)
- [Roblox thumbnail size guide (Moda)](https://moda.app/resources/sizes/roblox-thumbnail) — blog · sizes (secondary)

Links: [[Game Design MOC]] · [[00 Home]]
