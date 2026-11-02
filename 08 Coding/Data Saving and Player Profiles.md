---
title: Data Saving and Player Profiles
date: 2026-11-02
tags: [coding, persistence, data-stores]
status: researched
---

# Data Saving and Player Profiles

Persistent profiles need explicit ownership, failure handling and recovery. This note summarizes official documentation checked on 2026-11-02 and proposes acceptance tests; no profile module was installed or run in Studio. Use it alongside [[Networking and Remotes]], [[Security and Anti-Exploit]] and [[Release and Rollback Runbook]].

## Choose the storage boundary

| Need | Starting decision |
|---|---|
| Inventory, currency, progression | Server-owned persistent profile in DataStoreService |
| Temporary, frequently changing coordination | Investigate MemoryStore instead of treating persistence as a live event bus |
| UI balance display | Replicate selected server state; the client display does not own the saved balance |
| A profile library | Review maintenance, ownership, migration/export access and actual guarantees before adoption |

Data stores are shared across places and servers within an experience. Access from experience scripts is server-side. Studio API access can touch the same data as the live experience: use a separate published test experience. Calls can fail; catching an error is only the beginning of handling it. [Data stores](https://create.roblox.com/docs/cloud-services/data-stores).

## Shape and write the profile

Use stable player identifiers and a small number of stores. Keep values that must change together in one record when feasible. Buffer gameplay changes in server memory; stagger recurring saves. Retry transient failures with capped backoff and jitter, preserving request order per key. An unsuccessful response can leave the write outcome unknown. Prefer UpdateAsync when the result depends on existing state or other servers can write; SetAsync replaces without first reconciling that state. Review library escape routes before choosing a wrapper, including any proposed ProfileStore integration; this note has not audited that library. [Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices).

UpdateAsync's transform cannot yield, and returning nil cancels the update. Keep external effects outside the transform. Do not confuse an atomic update of one key with an implemented transaction spanning two players. [Data stores](https://create.roblox.com/docs/cloud-services/data-stores).

## Session ownership and failure states

Roblox's sample acquires a session lock atomically while loading through UpdateAsync. Each later operation checks ownership; expiry permits another server to take over, and the former owner must stop writing. Regular saves refresh the lock; final saving releases it. Merely adding a lock field without those checks does not reproduce this behavior. The sample explicitly requires extensive testing before use. [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing).

Distinguish **new profile**, **load failed**, **another session owns profile**, and **loaded successfully**. Failed-load defaults must never overwrite existing saved progress. For purchases, Roblox's sample checks receipt identity, applies the award and records that identity in persistent player data before acknowledging success. [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing).

## Limits, migration and recovery

Request queues, per-key throughput and experience/server budgets are separate constraints. Measure serialized profile size and request pressure before growth reaches limits; use the owning limits page instead of copying an undated requests-per-minute constant. [Errors and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits).

Recommended project contract: store a schema version, make upgrades repeatable, preserve unknown fields intentionally, and define whether older server code may read the new shape. Test on copies before rollout. These are design recommendations, not a supplied migration implementation.

Standard-store versioning is not a backup of every write: Roblox describes hourly version behavior and expiring older versions. Its snapshot API can preserve data before storage-logic changes. Record the snapshot/version, restore scope and compatibility with the rollback build; rehearse recovery outside production. [Versioning, listing and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching).

## Proposed acceptance tests — not executed

| Scenario | Evidence to collect |
|---|---|
| Failed initial read | Player receives clear state; existing progress remains unchanged |
| Rapid rejoin or teleport | Second session cannot overwrite an active owner's changes |
| Lock expires; old server resumes | Former owner cannot save stale memory |
| Retry after an ambiguous write | No duplicated reward or older-state overwrite |
| Same receipt delivered again | Exactly one durable award |
| Shutdown during throttling | Record completed saves and unresolved failures |
| Migration then rollback | Old/new fixtures and recovery revision behave as specified |

Record actual results in [[Playtest Record]] and [[Evidence Record]]. Ordered leaderboards, cross-player trades and a specific third-party profile library still need separate focused research and implementation tests.

## Mentioned in

- [[Anime Adventures]]
- [[Fish It]]
- [[Pet Simulator 99]]
- [[What Every Roblox Game Needs]]

## References
- [Data stores](https://create.roblox.com/docs/cloud-services/data-stores) — official documentation · access, update semantics and test isolation.
- [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing) — official reference design · ownership, load failures and durable receipt handling.
- [Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) — official guidance · record layout, retries and library evaluation.
- [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) — official reference · current service constraints.
- [Versioning, listing and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) — official documentation · versions, snapshots and recovery limits.

Links: [[Coding MOC]] · [[00 Home]]
