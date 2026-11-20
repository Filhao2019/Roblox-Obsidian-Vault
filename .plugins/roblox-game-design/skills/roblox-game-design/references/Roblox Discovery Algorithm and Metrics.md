---
title: Roblox Discovery Algorithm and Metrics
date: 2026-11-02
tags: [game-design, discovery, analytics, payouts, ads]
status: researched
---

# Roblox Discovery Algorithm and Metrics

How Roblox decides which experiences to show, which metrics matter, and how money flows (Creator Rewards, DevEx, ads). Everything here is from official docs unless labeled. Pair with [[Thumbnails Icons and Titles]], [[Retention and Progression Systems]], [[Monetization Patterns]] and [[What Makes a Roblox Game Go Viral]].

## Discovery surfaces

From the Discovery doc ([Discovery](https://create.roblox.com/docs/discovery)):

- **Recommended for You (Home):** personalized two-stage system — *retrieval* (selects a candidate subset using engagement, retention, monetization, friend plays, similar experiences, variety) then *ranking*.
- **Other Home sorts:** Continue Playing, Friends, Sponsored, Curated sorts, Standout Games, Live Events.
- **Game details page:** events, groups, passes/subscriptions, similar games.
- **Search:** semantic search for natural-language queries.
- **Discover:** top charts and trending sorts (the chart in [[Top Games Chart 2026-11-02]] comes from "Top Playing Now").
- **Notifications:** milestones, high scores, friend activity.

## Ranking signals (Recommended for You)

Per the docs, measured on users who joined organically through that sort ([Discovery](https://create.roblox.com/docs/discovery)):

| Priority | Signal |
|---|---|
| Most important | Play-through rate; first-play bounce rate (negative; <60 s and 61–180 s); play days per user (D1, D2–7, D8–28); playtime per user (capped at 60 min/user/game/day) |
| Important | Intentional co-play days; qualified play sessions; spend days per user; Robux spent per user |

Not counted: engagement of users acquired via ads, curation, friends, search or social media in the ranking stage ([Recommendation](https://create.roblox.com/docs/en-us/production/recommendation.md)). Running ads does not affect Recommended ranking ([Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager)).

**Reduced exposure:** high first-play bounce; metadata implying monetary giveaways; metadata/content mismatch; non-unique place files; missing custom thumbnail; stronger competitors. A banner appears in the Creator Dashboard when exposure is reduced. Four factors move impressions: your changes, Roblox algorithm changes, total traffic (seasonality), competitor performance ([Discovery](https://create.roblox.com/docs/discovery), [DevForum: Boost your discovery](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042)). The Home recommendations update rolled out the week of August 20, 2026 with metric fluctuations expected as it settled (same DevForum post). Experiences without maturity info are unplayable ([Content maturity](https://create.roblox.com/docs/en-us/production/promotion/content-maturity)); older docs treated no guidelines like Ages 13+ ([Experience guidelines](https://create.roblox.com/docs/production/promotion/experience-guidelines)).

**Strong in both retention and monetization -> more distribution;** strong in only one still gets impressions but less (DevForum post).

## Metrics glossary

| Metric | Meaning | Where |
|---|---|---|
| Impressions | Times your tile was shown | Acquisition ([Acquisition](https://create.roblox.com/docs/en-us/production/analytics/acquisition)) |
| Play-through rate / Qualified play-through rate | Share of new users who engaged after an impression | Acquisition > Home Recommendations |
| Average session time | Total play time / sessions per day | Engagement ([Engagement](https://create.roblox.com/docs/production/analytics/engagement)) |
| New-user first-session retention | % still playing X minutes after joining | Engagement |
| D1/D7/D30 retention | Return on day 1/7/30 after first play; cohorts by first play date | Retention ([Retention](https://create.roblox.com/docs/en-us/production/analytics/retention.md)) |
| Payer conversion, ARPPU | Monetization | Monetization / Analytics Dashboard |
| Benchmarks | Comparison to similar experiences; do not affect the algorithm | Analytics Dashboard |

APIs: the Analytics Query API exposes metrics like average session length ([Metrics](https://create.roblox.com/docs/en-us/cloud/guides/analytics/metrics)). Sales data lives in the dashboard ([Sales data](https://create.roblox.com/docs/production/analytics/sales-data)). Third-party analytics are allowed with caveats ([Third-party analytics](https://create.roblox.com/docs/production/analytics/third-party-analytics)).

## Improving each signal

| Signal | Levers |
|---|---|
| Play-through rate | Thumbnails, icon, title, description accuracy ([Acquisition](https://create.roblox.com/docs/en-us/production/analytics/acquisition)); thumbnail personalization (+8.5% avg) |
| First-play bounce | Fast onboarding, stable loading ([[Onboarding and First Session]]) |
| Play days | Daily rewards, appointments, offline income ([[Retention and Progression Systems]]) |
| Playtime | Long loops, parties, group goals; cap awareness (60 minutes counted) |
| Co-play | Friend join, trading, parties ([[Social Features and Multiplayer Hooks]]) |
| Spend days / Robux per user | Healthy economy, shop placement ([[Monetization Patterns]]) |

Roblox staff advice: low retention -> fix core gameplay, first session and reasons to return; high retention -> add optional, valued monetization; keep monetization fair ([DevForum](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042)).

## Experiments and Configs

Experiments run A/B tests to measure causal impact; Configs adjust values live without restarting servers ([Analytics essentials](https://create.roblox.com/docs/production/game-design/analytics-essentials)). Use them for tutorial steps, starter cash, hint timings and prices ([Onboarding](https://create.roblox.com/docs/en-us/production/game-design/onboarding.md)).

## Curation: Standout Games and events

- Standout Games is a curated Home sort; no hard requirements; judged on novelty, unique mechanics or visual style; "copy or reskin" games are a hard sell; nominate through a survey ([Standout Games](https://create.roblox.com/docs/creator-programs/standout-games)).
- Experience events: Notify Me, trending eligibility (start within 7 days, 1,000+ RSVPs, public), off-platform featuring submissions ≥7 days ahead ([Experience events](https://create.roblox.com/docs/production/promotion/experience-events)).

## Creator Rewards (replaced Engagement-Based Payouts, July 24, 2025)

- **Daily Engagement Reward:** 5 Robux per Active Spender (spent ≥ $9.99 in 60 days) who plays ≥10 minutes, counted for their first three experiences each day.
- **Audience Expansion Reward:** 35% share of a new/returning user's first $100 of qualifying purchases in 60 days; needs ≥10 minutes that day and 100+ DAU average for 60 days; ID-verified creator.
- Paid as Earned Robux with a 60-day hold; bot/alt behavior forfeits rewards ([Creator Rewards](https://create.roblox.com/docs/creator-rewards), [Engagement-Based Payouts](https://create.roblox.com/docs/production/monetization/engagement-based-payouts)). Coverage: ([Tubefilter](https://www.tubefilter.com/?p=186987), [Obby.fun guide](https://www.obby.fun/blog/roblox-creator-rewards-guide)).
- Design implication: you are paid more for retaining *spenders* and for bringing *new/returning* users; invite links (Share Links) matter.

## DevEx

- Robux you earn can be cashed out via DevEx (see [Monetize experiences](https://create.roblox.com/docs/en-us/monetize-experiences.md)). Multiple secondary sources report $0.0038 per earned Robux since September 2025 and a 30,000 Robux minimum; one mentions a higher U.S. 18+ rate. These conflict across sources, so confirm on the official DevEx page ([Axeetech](https://axeetech.com/roblox-devex-rates/), [Rolearn](https://rolearn.dev/guidance/roblox-devex-requirements-2026), [RoWatcher](https://rowatcher.com/news/roblox-devex-math-what-you-actually-take-home-in-2026), [Creation.dev](https://www.creation.dev/learn/roblox-developer-exchange-explained); all unverified).
- Example: 1,000 Robux spent -> 700 to the developer (70%) -> about $2.66 at $0.0038 (RoWatcher, unverified).

## Ads Manager and sponsored experiences

([Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager), [Sponsoring experiences](https://create.roblox.com/docs/production/promotion/sponsoring-experiences), [Advertise](https://create.roblox.com/docs/production/promotion/advertise), [User ads](https://create.roblox.com/docs/production/promotion/user-advertisements))
- Campaigns show on Home (Sponsored) and Search; goals: Plays, Earnings (limited), Engagement; auto-bidding with budget (daily/lifetime) and duration; audiences All, New (never played or 180+ days), Recent (30 days, ≥10,000 players), Lapsed (30–180 days, ≥20,000), plus advanced targeting; up to 10 thumbnails.
- Operations: moderation within 24 h; learning phase first 24 h; wait 3–5 days for engagement campaigns; reporting delays up to 48 h; attribution up to 30 days; fraud review 14 days after end.
- Requirements: user 13+, verified email; card payments 18+; Robux->ad credits conversion is permanent.
- API: Open Cloud Ads API exists (test status) ([Advertising guide](https://create.roblox.com/docs/cloud/guides/advertising), [DevForum test post](https://devforum.roblox.com/t/test-ads-manager-api-now-on-open-cloud/4766543)); creators on DevForum reported low CTR and targeting problems (anecdotal).
- Rule of thumb: ads work if your D1 and session time are already good; otherwise you buy churn. Ads' users are not counted for Recommended ranking.

## Platform context (2026)

- Q3 2026: revenue about $1.57B (+16%), bookings about $1.70B (-12%), average DAU 138M (-9% y/y), payers 30M (-16%), 64% of DAU age-checked; Q4 bookings guidance $1.89–2.00B ([Quartr](https://quartr.com/events/roblox-rblx-q3-2026_ozGBemPh), [Gaming.net](https://gaming.net/roblox-q3-revenue-rises-16-as-bookings-fall-12-to-1-7-billion), [WN Hub](https://wnhub.io/news/finance/item-52549), [Digg](https://digg.com/gaming/bde5e8sy)). Filings: [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068253/rblx-20260930.htm), [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm), [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026028904/rblx-20260331.htm), [Q3 supplemental deck](https://s27.q4cdn.com/984876518/files/content_files/Q3_26-Supplemental-Materials.pdf) (the deck could not be text-extracted; figures here come from press summaries and conflict on hours engaged).
- Age checks and maturity labels increasingly gate audiences ([Content maturity](https://create.roblox.com/docs/en-us/production/promotion/content-maturity)); see [[What Every Roblox Game Needs]].

## Analytics routine

- Daily: CCU, D1, avg session, crashes.
- Weekly: Acquisition > Home Recommendations (QPTR vs benchmark), retention cohorts, payer conversion.
- After each update: compare cohorts, thumbnail performance, funnel.

## References

- [Discovery (Creator Docs)](https://create.roblox.com/docs/discovery) — official docs · surfaces and ranking signals
- [Recommendation (Creator Docs)](https://create.roblox.com/docs/en-us/production/recommendation.md) — official docs · what counts in ranking
- [Acquisition analytics (Creator Docs)](https://create.roblox.com/docs/en-us/production/analytics/acquisition) — official docs · impressions, QPTR
- [Engagement analytics (Creator Docs)](https://create.roblox.com/docs/production/analytics/engagement) — official docs · session time
- [Retention analytics (Creator Docs)](https://create.roblox.com/docs/en-us/production/analytics/retention.md) — official docs · cohorts
- [Analytics Dashboard / Sales data (Creator Docs)](https://create.roblox.com/docs/production/analytics/sales-data) — official docs · sales
- [Analytics metrics API (Creator Docs)](https://create.roblox.com/docs/en-us/cloud/guides/analytics/metrics) — official docs · query metrics
- [Third-party analytics (Creator Docs)](https://create.roblox.com/docs/production/analytics/third-party-analytics) — official docs · external analytics
- [Analytics essentials (Creator Docs)](https://create.roblox.com/docs/production/game-design/analytics-essentials) — official docs · Experiments, Configs
- [Creator Rewards (Creator Docs)](https://create.roblox.com/docs/creator-rewards) — official docs · payouts
- [Engagement-Based Payouts (Creator Docs)](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) — official docs · deprecated
- [Standout Games (Creator Docs)](https://create.roblox.com/docs/creator-programs/standout-games) — official docs · curation
- [Experience events (Creator Docs)](https://create.roblox.com/docs/production/promotion/experience-events) — official docs · events
- [Ads Manager (Creator Docs)](https://create.roblox.com/docs/production/promotion/ads-manager) — official docs · campaigns
- [Sponsoring experiences (Creator Docs)](https://create.roblox.com/docs/production/promotion/sponsoring-experiences) — official docs · sponsored setup
- [Advertise (Creator Docs)](https://create.roblox.com/docs/production/promotion/advertise) — official docs · advertising overview
- [User advertisements (Creator Docs)](https://create.roblox.com/docs/production/promotion/user-advertisements) — official docs · ad budgets
- [Advertising API (Creator Docs)](https://create.roblox.com/docs/cloud/guides/advertising) — official docs · Open Cloud ads
- [Ads Manager API test (DevForum)](https://devforum.roblox.com/t/test-ads-manager-api-now-on-open-cloud/4766543) — forum · API announcement and feedback
- [Boost your discovery (DevForum)](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042) — Roblox staff post · August 2026 update
- [Content maturity (Creator Docs)](https://create.roblox.com/docs/en-us/production/promotion/content-maturity) — official docs · labels
- [Experience guidelines (Creator Docs)](https://create.roblox.com/docs/production/promotion/experience-guidelines) — official docs · older guidelines
- [Creator Rewards (Tubefilter)](https://www.tubefilter.com/?p=186987) — press · payout summary
- [Creator Rewards guide (Obby.fun)](https://www.obby.fun/blog/roblox-creator-rewards-guide) — blog · guide (secondary)
- [DevEx rates (Axeetech)](https://axeetech.com/roblox-devex-rates/) — blog · DevEx (unverified)
- [DevEx requirements 2026 (Rolearn)](https://rolearn.dev/guidance/roblox-devex-requirements-2026) — blog · DevEx (unverified)
- [DevEx math (RoWatcher)](https://rowatcher.com/news/roblox-devex-math-what-you-actually-take-home-in-2026) — blog · DevEx (unverified)
- [Roblox Developer Exchange explained (Creation.dev)](https://www.creation.dev/learn/roblox-developer-exchange-explained) — blog · DevEx (may be outdated)
- [Monetize experiences (Creator Docs)](https://create.roblox.com/docs/en-us/monetize-experiences.md) — official docs · 70% share
- [Roblox Q3 2026 (Quartr)](https://quartr.com/events/roblox-rblx-q3-2026_ozGBemPh) — investor summary
- [Q3 results (Gaming.net)](https://gaming.net/roblox-q3-revenue-rises-16-as-bookings-fall-12-to-1-7-billion) — press
- [Q3 results (WN Hub)](https://wnhub.io/news/finance/item-52549) — press
- [Q3 results (Digg)](https://digg.com/gaming/bde5e8sy) — aggregator
- [Roblox 10-Q Q3 2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068253/rblx-20260930.htm) — filing · metric definitions
- [Roblox 10-Q Q2 2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm) — filing
- [Roblox 10-Q Q1 2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026028904/rblx-20260331.htm) — filing
- [Q3 2026 supplemental materials (Roblox IR)](https://s27.q4cdn.com/984876518/files/content_files/Q3_26-Supplemental-Materials.pdf) — investor deck · not text-extractable here

Links: [[Game Design MOC]] · [[00 Home]]
