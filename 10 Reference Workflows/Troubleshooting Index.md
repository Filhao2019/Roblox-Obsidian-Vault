---
title: Troubleshooting Index
date: 2026-11-02
tags: [troubleshooting, evidence, reference-workflow]
status: researched
---

# Troubleshooting Index

Start from a symptom, then inspect the linked material and reproduce the issue. These are original navigation suggestions, not confirmed diagnoses or completed fixes. Linked stubs and untested notes keep their status.

| Symptom or question | Suggested inspection | Start with |
|---|---|---|
| Phone UI clipped, crowded or hard to reach | Compare the current layout at the target viewport and input method | [[Mobile Console and Responsive UI]] · [[UI Layout and Motion Visual Study]] |
| UI motion feels abrupt or text appears too quickly | Inspect the sequence and record actual timing | [[UI Animation and Juice]] · [[UI Layout and Motion Visual Study]] |
| Walk cycle looks stiff or feet appear to slide | Compare key poses and contact against an inspected clip | [[Animation Poses and Timing Visual Study]] |
| Effects obscure a target or linger after use | Compare contrast, duration, repeated triggers and cleanup | [[Particles and Beams Visual Study]] · [[VFX and Audio Brief]] |
| Ambience sounds wrong as the player moves | Listen along a repeatable route and record source placement | [[Spatial Audio Visual Study]] |
| Room looks cluttered or direction is unclear | Review player-height views, major shapes and route | [[Style and Environment Brief]] |
| Player progress fails to save | Gather load/save errors and reproduction steps before changing persistence | [[Data Saving and Player Profiles]] — researched guidance, runtime checks pending |
| Currency changes or remote requests seem exploitable | Review client/server responsibility and actual request validation | [[Security and Anti-Exploit]] · [[Networking and Remotes]] — researched guidance, runtime checks pending |
| Search returns an incomplete answer | Read the returned status and narrow the query | [[Vault Tools and Evidence]] |
| Feature touches several systems or scope is unclear | Specify one observable outcome, authority and failure cases | [[Feature Triage and Build Contract]] · [[Feature Build Contract]] |
| Third-party asset or skill needs review | Record provenance, executable content, permissions and unknowns without running it | [[Third Party Asset Intake Review]] · [[Asset Intake Record]] |
| Behavior differs across devices or players | Record actual inputs, test mode, client count and reproduction evidence | [[Device and Multiplayer Test Plan]] · [[Playtest Record]] |
| Release recovery is unclear | Identify exact candidates, backups, data compatibility and recovery gaps | [[Release and Rollback Runbook]] · [[Release Record]] |
| Checker reports a missing embed or altered file | Inspect the exact path and compare with the integrity manifest | [[Media Attribution and Reuse]] |

## Add a confirmed fix

Record the reproduction, expected/actual behavior, logs or screenshots, confirmed cause, changed files and verification result using [[Evidence Record]]. Keep hypotheses separate from causes demonstrated by a test. Do not mark a coding stub researched merely because this index links it.

## References

- [[Reference Driven Roblox Workflow]] — observation and acceptance process.
- [[Evidence and Quality Review]] — evidence labels and review criteria.

Links: [[Reference Workflows MOC]] · [[Vault Tools and Evidence]] · [[00 Home]]
