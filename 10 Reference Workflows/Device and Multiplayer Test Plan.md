---
title: Device and Multiplayer Test Plan
date: 2026-11-02
tags: [qa, devices, multiplayer, reference-workflow]
status: researched
---

# Device and Multiplayer Test Plan

Plan reproducible checks and record what actually ran using [[Playtest Record]]. These documents supply no test runner and do not open Studio, modify settings, connect accounts or run a game. Select only scenarios relevant to the feature and the separately authorized test environment.

## Describe the environment

Record the build/source revision, place or test environment, rig, input method, viewport, client count and test mode. Identify an actual device versus an emulator. An emulated phone layout is evidence about that emulation, not a measurement of a physical phone's performance.

Roblox documents separate client/server, multi-client and device-simulation modes. Record the mode actually used rather than treating a server-only run as evidence of player input and UI behavior. Verify available features in current Studio documentation.

## Pick targeted scenarios

| Area | Example question to adapt |
|---|---|
| First use | Can the player reach and complete the intended action? |
| Input and layout | Are touch targets, focus, safe areas and text usable at the selected size? |
| UI states | Are loading, empty, error, locked and pending states understandable? |
| Lifecycle | What happens on respawn, reopening a screen or leaving during an action? |
| Multiplayer | What happens when two clients act on the same object or value? |
| Repeated actions | Does rapid or duplicate input produce the intended result? |
| Rejoin, if persistent | Does the observed saved state match the accepted action? |
| Network conditions | What behavior is expected under delayed or failed responses? |
| Performance | What was measured, on which device and under what load? |

Use disposable test data and a suitable test environment for destructive, persistence or purchase-related scenarios. Leave scenarios requiring real transactions or live-state changes pending until a separate authorized procedure exists. Do not include reusable commands against live data in this worksheet.

## Write a useful result

Each scenario needs setup, steps, expected result, actual result, evidence and pass/fail/pending. Missing access is pending, not a pass. If a failure is fixed, record the retest revision and outcome while preserving the original failure. Link significant results from [[Evidence Record]].

## References

- [AshExplained mobile testing](https://github.com/AshExplained/roblox-skills/blob/a3a7b940f0899d4a69c1a7df625996bdfc917388/roblox-mobile-playtest/SKILL.md) — upstream primary source · device/input evidence inspiration; no tools or skill dependency imported.
- [Roblox Studio testing modes](https://create.roblox.com/docs/studio/testing-modes) — official documentation · testing environments and simulation, reviewed 2026-11-02.
- [[Mobile Console and Responsive UI]] — vault reference · layout and input considerations.
- [[Playtest Record]] — worksheet · execution evidence.

Links: [[Reference Workflows MOC]] · [[UI MOC]] · [[00 Home]]
