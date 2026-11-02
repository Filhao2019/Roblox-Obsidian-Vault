---
title: Release and Rollback Runbook
date: 2026-11-02
tags: [release-planning, recovery, reference-workflow]
status: researched
---

# Release and Rollback Runbook

Record release readiness and recovery questions before a separate publishing decision. This original guide and [[Release Record]] contain no publishing, rollback, account, purchase or data-mutation commands. Completing the record does not deploy a build or authorize changes.

## Identify the candidate

Record the exact source revision or saved candidate, intended environment, changed behavior and known issues. Link the completed [[Feature Build Contract]] and relevant [[Playtest Record]] results. A checked plan is insufficient without evidence that the required checks actually ran.

## Plan recovery before release

Identify the last known working candidate and its recovery location. Record who owns recovery and how the availability of the backup was checked. Never put credentials, private recovery locations or production logs into this public reference vault.

Ask whether the candidate changes stored data, grants, configuration, assets or external dependencies. A code rollback must not be assumed to undo earlier saved-data changes. Record compatibility and a separately researched/tested migration or recovery procedure when needed. If that procedure is unknown, preserve the gap rather than claiming rollback is ready.

## State the decision criteria

| Question | Evidence to record |
|---|---|
| What must work? | Small smoke-test route and relevant devices/players |
| What blocks release? | Required failures or pending checks |
| What would trigger recovery? | Concrete symptoms, thresholds and responsible owner |
| What can be restored? | Candidate/configuration/data scope and known limitations |
| What should be watched? | Errors, failed saves/grants and relevant player reports |

Choose thresholds for the particular project; this guide does not invent a universal acceptable error rate or performance target. Describe monitoring ownership without creating scheduled jobs or sending notifications.

## Record the actual outcome

Separate planned actions from actions already performed. After a separately authorized release, record the actual revision/environment, smoke-test result and remaining issues. Record any recovery as another observed event with its result. A published build still needs the checks appropriate to its changes.

## References

- [AshExplained release operations](https://github.com/AshExplained/roblox-skills/blob/a3a7b940f0899d4a69c1a7df625996bdfc917388/roblox-release-operations/SKILL.md) — upstream primary source · readiness/recovery questions inspired this independently written planning guide.
- [[What Every Roblox Game Needs]] — vault reference · broad readiness questions.
- [[Evidence and Quality Review]] — method · actual versus pending evidence.
- [[Release Record]] — worksheet · candidate, recovery and outcome.

Links: [[Reference Workflows MOC]] · [[Game Design MOC]] · [[00 Home]]
