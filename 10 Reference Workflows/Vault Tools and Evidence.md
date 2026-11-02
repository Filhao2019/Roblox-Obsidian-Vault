---
title: Vault Tools and Evidence
date: 2026-11-02
tags: [tools, evidence, reference-workflow]
status: researched
---

# Vault Tools and Evidence

Use the bundled local search and checker to find references and keep the library navigable. Use [[Troubleshooting Index]] for symptom-based starting points and [[Evidence and Quality Review]] to distinguish a researched idea from a tested result.

## Search and read

From this vault's root folder, run:

```shell
python _tools/vault.py search "mobile UI"
python _tools/vault.py search "data saving" --json
python _tools/vault.py read "Reference Driven Roblox Workflow" --heading "1. Define the decision"
```

Search shows the note's existing status. A result marked `stub` identifies a gap, not a researched implementation. `untested` code still needs execution in Studio. The tool uses local text ranking, not image understanding; open any selected images or clips before making visual claims. No model, API key or network connection is required.

## Validate the library

```shell
python _tools/vault.py check
python -m unittest discover -s _tools -p test_vault.py
```

The checker covers required note properties, unresolved or ambiguous wikilink/file-embed targets, media path containment, byte lengths and SHA-256 hashes. It exits unsuccessfully when it finds errors. The repository's GitHub Actions workflow runs these checks and regression tests on pushes and pull requests.

The checker does not verify external websites, heading anchors, Roblox API currency, snippet compilation, security or gameplay correctness. Passing it means those structural checks passed, not that every note is true or every system works. Original chart data and incomplete coding notes retain their existing evidence limits.

## Attribution and implementation scope

The search, check and evidence-workflow ideas were informed by inspecting LihFolk Vault V2. The tools and notes in this release were independently written for our repository. No LihFolk executable code, plugin hooks, gameplay modules, scene-reset scripts or asset-pack files were imported.

## References

- [LihFolk Vault V2 tools guide](https://github.com/lihfolk-cy/v2-vault/blob/43ba05dbad93e9ff4e4b06633d10260ca59f0602/LihFolk%20Vault%20V2/_tools/README.md) — upstream primary source · organizational inspiration.
- [[Media Attribution and Reuse]] — offline media provenance and checksums.
- [[Reference Workflows MOC]] — existing build briefs.

Links: [[Reference Workflows MOC]] · [[00 Home]]
