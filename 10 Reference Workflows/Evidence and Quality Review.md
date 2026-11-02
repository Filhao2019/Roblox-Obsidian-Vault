---
title: Evidence and Quality Review
date: 2026-11-02
tags: [evidence, quality, reference-workflow]
status: researched
---

# Evidence and Quality Review

Use an explicit evidence record to decide whether a reference-informed change is ready. These are original review guidelines for this vault, informed by the usefulness of LihFolk's evidence/rubric approach. No fixed numerical score guarantees quality.

## Label the evidence

| Label | What it means |
|---|---|
| Source-backed | The linked source directly supports the claim; record its revision or review date |
| Observed | A screenshot, clip, log or inspected file shows the stated behavior; say exactly what was inspected |
| Tested | A documented procedure was executed with the stated result and environment |
| Hypothesis | A plausible explanation or design choice that still needs checking |
| Pending | The required check has not been performed |

Keep the existing note-level statuses: `stub`, `researched`, `untested`, `verified`. A successful structural check is insufficient to mark code runtime-verified. Record changing API, policy or price claims with current authoritative sources before relying on them.

## Review against the task

1. Define observable acceptance criteria before building: required behavior, visual readability, controls and constraints.
2. Record a result per criterion as pass, fail or pending, with a file, screenshot, log, measurement or actual test result.
3. Separate mechanical checks from visual judgment. For a visual criterion, name the reference and describe the comparison; use human or independent review when needed.
4. Fix the demonstrated failure and repeat the affected check. Keep significant failed attempts and the reason for the final choice.
5. State remaining gaps. A pending required test remains pending regardless of how polished the result looks.

Use [[Evidence Record]] for the log and the relevant brief in [[Reference Workflows MOC]] for task-specific checks. Keep project-local evidence in the project; do not publish private paths, logs or user information into this public reference repository.

## References

- [LihFolk quality guide](https://github.com/lihfolk-cy/v2-vault/blob/43ba05dbad93e9ff4e4b06633d10260ca59f0602/skills/quality-score/SKILL.md) — upstream primary source · evidence and rubric inspiration; this note is independently written.
- [[Reference Selection Sheet]] — selected source observations.

Links: [[Reference Workflows MOC]] · [[Vault Tools and Evidence]] · [[00 Home]]
