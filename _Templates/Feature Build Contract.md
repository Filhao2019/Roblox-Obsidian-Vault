---
title: Feature Build Contract
date: 2026-11-02
tags: [template, planning, feature-contract]
status: researched
---

# Feature Build Contract

Copy this blank worksheet into the relevant project and follow [[Feature Triage and Build Contract]]. It records a plan, not an implemented feature or permission to execute actions. Keep private project details outside this public reference library.

## Outcome and scope

- Feature or bug:
- Player outcome:
- Current and desired behavior:
- Source revision and current locations:
- In scope / out of scope:
- Dependencies and unresolved decisions:
- Project work state:
- Existing authorization and any separate decisions required:

## Behavior and ownership

| Area | Contract to define |
|---|---|
| Client and UI | Input, display states and expected feedback |
| Server | Canonical state, eligibility and validation |
| Messages | Request/result fields, rejection and duplicate handling |
| Persistence, if needed | What survives rejoin; load/write failure behavior |
| Lifecycle | Cancellation, disconnect, respawn and cleanup |
| Dependencies | Existing systems, assets and current source references |

## Acceptance

| Scenario | Action | Expected result | Actual result / evidence | Outcome |
|---|---|---|---|---|
| Main behavior | To define | To define | Not run | Pending |
| Relevant failure case | To define | To define | Not run | Pending |

## References

- [[Feature Triage and Build Contract]] — method · scope, ownership and readiness.
- [[UI Build Brief]] — companion brief · interface states.
- [[Evidence Record]] — results · observations and executed checks.

Links: [[Reference Workflows MOC]] · [[00 Home]]
