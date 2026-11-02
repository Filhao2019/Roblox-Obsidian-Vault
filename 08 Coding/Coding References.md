---
title: Coding References
date: 2026-11-02
tags: [coding, research]
status: researched
---

# Coding References

Start with the owning Roblox documentation and distinguish API research from working code. The sources below were opened during this batch on 2026-11-02. This is a curated reading route, not a library recommendation or a Studio test result.

| Task | Vault guide | Official starting point |
|---|---|---|
| Persistent player state | [[Data Saving and Player Profiles]] | [Data stores](https://create.roblox.com/docs/cloud-services/data-stores) |
| Locking and purchase recovery | [[Data Saving and Player Profiles]] | [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing) |
| Cross-boundary communication | [[Networking and Remotes]] | [Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote) |
| Validate player requests | [[Security and Anti-Exploit]] | [Client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary) |
| Review imported content | [[Third Party Asset Intake Review]] | [Third-party vulnerabilities](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) |

## Use the route

1. Read the owning source and record the review date and affected API.
2. Write one behavior and its invariants using [[Feature Build Contract]].
3. Implement in the actual project's chosen source workflow.
4. Test the success, failure and concurrency paths using [[Playtest Record]].
5. Keep actual results in [[Evidence Record]]; researched guidance alone does not justify a verified implementation label.

## Gaps retained

[[Open Source Libraries]] is still a stub; no specific persistence, networking or framework package was reviewed in this batch. Genre systems that remain stubs require separate research. The historical game chart is not API evidence, and a third-party code example is not proof of production readiness.

## References

- [Roblox data stores](https://create.roblox.com/docs/cloud-services/data-stores) — official guide · persistence entry point.
- [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing) — official guide · advanced player data workflow.
- [Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote) — official guide · communication models.
- [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary) — official guide · request validation.
- [Third-party vulnerabilities](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) — official guide · imported content review.

## Mentioned in

- (none yet)


Links: [[Coding MOC]] · [[00 Home]]
