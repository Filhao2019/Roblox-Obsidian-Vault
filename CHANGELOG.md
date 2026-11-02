# Changelog

## v2.0.0 — v2: LihFolk V2 Import and Visual Boards — 2026-11-02

- Imported 1,360 notes and images from LihFolk Vault V2 (CC BY 4.0, pinned commit) into `11 LihFolk V2/`, unchanged and credited in `ABOUT THIS IMPORT.md`. This adds sections the vault lacked: anti-exploit, physics and vehicles, level design, accessibility, player QoL, thumbnails and CTR, engine reference cards, an API atlas, a bug-symptom table (`SYMPTOMS.md`) and a topic router (`ROUTER.md`).
- Security review: no exfiltration, credential access or prompt-injection instructions found. Excluded the upstream Claude plugin hook (runs a script on every edit), multi-agent council commands (high token use), Obsidian plugin, tools, rig files and benchmarks.
- Added 16 visual boards: 407 UI, 599 high-fidelity model, 200 thumbnail and 100 VFX references plus a 100-video animation library. Images are **remote embeds** from their original hosts rather than bundled files, a change from earlier releases; they need internet access and Roblox CDN links can expire.
- `_tools/vault.py check` searches the imported folder but does not hold it to this vault's metadata and link rules.

## v1.4.0 — Research and Practical Workflows — 2026-11-02

- Expanded seven stubs: persistence, networking, security, coding references, flipbooks, environmental VFX and DOORS. Added a source-scoped Pressure reference and a research coverage map.
- Embedded three existing offline images and one existing clip directly in the new VFX guidance; linked official online thumbnails in the horror profiles. No third-party game media was bundled.
- Updated coverage/status navigation; retained historical chart data and separated research, original exercises and untested implementation.

- Added four original, passive Markdown guides and four blank worksheets for feature contracts, third-party asset intake, device/multiplayer test evidence and release recovery planning.
- Linked the additions from Home, the workflow hub, troubleshooting and relevant area maps. Existing evidence conventions, runtime limitations and coding-stub statuses are preserved.
- Credited AshExplained's reviewed planning ideas at a pinned revision. No upstream skills, setup blocks, scripts, dependencies, remote embeds, automatic actions or agent-configuration changes are included.

## v1.3.0 — 2026-11-02

- Added original Python-standard-library local search, exact note/section reading and structured JSON search results with evidence status preserved.
- Added a vault checker for note metadata, wiki/file-embed targets, media path containment and SHA-256 integrity; regression tests cover errors as well as successful checks.
- Added GitHub Actions validation using pinned official actions and read-only repository permissions.
- Added an original troubleshooting index, evidence review guidelines and project evidence template, linked from Home and area maps.
- Added the missing researched status to the dated chart note; existing chart data and incomplete system notes are preserved.
- Credited LihFolk's tooling ideas without importing its code, hooks, gameplay modules, plugin or separately restricted assets. Existing 21 images and 9 videos remain included.

## v1.2.0 — 2026-11-02

- Added a pinned guide and machine-readable catalog of izzyfrm/roblox-ai's 12 visual reference collections, with independently counted files and explicit review limits.
- Added five original build briefs for environments, UI, animation/cutscenes, VFX/audio and branding/thumbnails.
- Added a reference selection worksheet and a workflow connecting inspected media to implementation and acceptance evidence.
- Linked the additions from Home, visual references and relevant area maps.
- Credited the upstream organizational inspiration without importing mixed-rights images, copied prompts or an unverified plugin package. The existing 21 offline images and 9 videos are preserved.

## v1.1.0 — 2026-11-02

- Added five visual study boards containing 21 offline images and 9 offline demonstration videos from Roblox Creator Documentation.
- Added a visual reference hub, observation workflow and reusable capture template.
- Linked visual boards from Home, area MOCs, reference libraries and relevant topic notes.
- Included per-asset provenance, pinned upstream revision, SHA-256 checksums, CC BY 4.0 license and attribution.
- Preserved the existing game research and dated chart snapshot. Studio implementation and device performance are not verified by this update.
