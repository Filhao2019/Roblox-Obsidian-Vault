---
title: Third Party Asset Intake Review
date: 2026-11-02
tags: [asset-review, security, reference-workflow]
status: researched
---

# Third Party Asset Intake Review

Document the provenance and permissions of one third-party asset before a separate decision to use it. This original review guide and [[Asset Intake Record]] perform no download, installation, insertion, execution or deletion. A completed checklist is not a guarantee that an asset is safe.

## Identify the execution boundary

| Material | What the review needs to distinguish |
|---|---|
| Visual or audio content | License, origin, file type and any attached behavior |
| In-game model or package | Script descendants, dependencies and game capabilities |
| Studio plugin | Editor permissions, file/network access and installation behavior |
| AI skill or external tool | Instructions, scripts, dependencies, persistence and host-tool permissions |

A text prompt can direct an agent to use powerful tools. A model with decorative geometry can also contain scripts. Review the actual contents rather than relying on the advertised category.

## Record before taking action

Use an existing inert source listing or review copy when available. Do not install an unknown plugin or execute unknown code just to inspect it. If contents cannot be inspected without running them, record that limitation and stop the review at that boundary.

Record the source, creator, exact revision or asset version, license, intended use and all executable content. Trace dependencies and network destinations. Explain sensitive operations in context: a network API name alone proves neither maliciousness nor safety. Unknown or changing dependencies remain unresolved.

An ordinary folder named quarantine does not restrict script execution. Roblox documents separate sandbox/capability controls; availability and required settings need checking against current official documentation. This note supplies no automatic configuration procedure.

## Decision and evidence

Use decisions such as rejected, unresolved/held out, or candidate for limited use after review. State exactly what was inspected, what remains unknown, and any separately performed isolation or runtime checks. Review only the intended scope: a model review does not certify a plugin, skill pack or Studio bridge.

Keep sensitive source code, credentials, account details and full private logs in the project. A reusable public record should contain only redacted examples and references.

## References

- [AshExplained asset audit](https://github.com/AshExplained/roblox-skills/blob/a3a7b940f0899d4a69c1a7df625996bdfc917388/roblox-creator-store-security-audit/SKILL.md) — upstream primary source · inventory and evidence inspiration; this guide is independently written and imports no execution steps.
- [Roblox third-party vulnerabilities](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) — official documentation · third-party scripts and sandboxing, reviewed 2026-11-02.
- [Roblox Script capabilities](https://create.roblox.com/docs/scripting/capabilities) — official documentation · actual execution restrictions; described as experimental/client beta when reviewed 2026-11-02.
- [[Asset Intake Record]] — worksheet · scope, findings and unresolved risks.

Links: [[Reference Workflows MOC]] · [[Free and Paid Asset Sources]] · [[00 Home]]
