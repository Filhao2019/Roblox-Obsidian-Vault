---
title: Feature Triage and Build Contract
date: 2026-11-02
tags: [planning, feature-contract, reference-workflow]
status: researched
---

# Feature Triage and Build Contract

Describe one complete player-visible behavior before implementation. This original guide and [[Feature Build Contract]] are planning documents; filling them does not authorize code edits, publishing, account actions or tool installation.

## Choose one complete slice

State what the player does, what changes, and how the result becomes visible. For example: request one supply item, receive an authoritative result, and see the updated inventory. Keep unrelated shop redesigns and progression changes outside this slice. Include persistence only when the feature requires it.

For a bug, record expected versus actual behavior and reproducible steps. A suspected cause remains a hypothesis until evidence supports it. For a new feature, state the player benefit and the smallest observable outcome.

## Make ownership and failure behavior explicit

Record the client presentation, server-owned state, request/response fields, and who validates eligibility. Describe duplicate requests, unavailable data, interrupted actions and reconnect behavior where relevant. This is a contract to research and implement, not a supplied networking or persistence system.

Use [[UI Build Brief]] for screens and [[Style and Environment Brief]] for world changes. Keep current source locations and revision identifiers beside behavioral descriptions; recheck those pointers when implementation starts.

## Triage without automatic actions

Use a project-local work state such as draft, needs information, ready, in progress or awaiting verification. Keep this separate from the vault's note-level research status. Ready means the behavior and checks are specified; it does not mean implemented, tested or authorized for deployment.

Record dependencies, unresolved decisions, work already authorized and actions needing a separate decision. Respect existing authorization instead of adding a new approval step for every routine edit. This document does not create issues, change labels, dispatch agents or edit project instructions.

## Completion evidence

Write a check as a concrete action and expected result. Record actual results with [[Evidence Record]] and use [[Playtest Record]] for runtime scenarios. Leave unexecuted checks pending. A successful document check does not verify game behavior.

## References

- [AshExplained build brief](https://github.com/AshExplained/roblox-skills/blob/a3a7b940f0899d4a69c1a7df625996bdfc917388/roblox-triage/BUILD-BRIEF.md) — upstream primary source · behavioral contracts and explicit authority inspired this independently written guide; no setup or skill instructions are imported.
- [[Evidence and Quality Review]] — vault method · evidence labels and acceptance.
- [[Feature Build Contract]] — worksheet · project-local feature specification.

Links: [[Reference Workflows MOC]] · [[Coding MOC]] · [[00 Home]]
