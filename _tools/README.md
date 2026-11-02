# Vault tools

Original, Python-standard-library tools for this repository. Python 3.10 or later; no pip packages, telemetry, shell hooks or plugin installation. Search and read commands only read local files. Check reads notes and the media manifest; it returns a nonzero exit code when validation fails. No command executes the Luau examples in notes.

Run from the vault root:

```shell
python _tools/vault.py search "mobile UI"
python _tools/vault.py search "data saving" --json -k 5
python _tools/vault.py read "UI Layout and Motion Visual Study"
python _tools/vault.py read "Reference Driven Roblox Workflow" --heading "1. Define the decision"
python _tools/vault.py check
python -m unittest discover -s _tools -p test_vault.py
```

Search weights titles, headings, tags and body terms and returns short summaries, paths, headings and the existing status. A highly ranked stub is still a stub. Ranking is a simple lexical heuristic; no retrieval benchmark or token savings are claimed. Supply alternate terms when a query has no match. Section reading uses an exact title or vault-relative path and exact heading; ambiguous titles are rejected.

Validation checks note properties, unique wikilink/file-embed targets and the existing media manifest's paths, sizes and SHA-256 values. Markdown examples in fenced blocks and inline code are ignored for link checking. Templates may have placeholder titles/dates. Root administrative documents are exempt from note metadata. External URLs, heading anchors, runtime code behavior, API freshness and security are not checked. Existing source stubs remain visible.

CI uses official GitHub Actions pinned to verified commits, read-only repository permission and no retained checkout credentials. Python tests create isolated temporary fixtures. They exercise ranking/status, section boundaries, broken links/embeds, template examples, metadata errors, tampered media and path containment. CI does not install upstream code or download/run a Luau compiler.

Organizational inspiration: [LihFolk Vault V2](https://github.com/lihfolk-cy/v2-vault/tree/43ba05dbad93e9ff4e4b06633d10260ca59f0602). This implementation is independently written for this vault; no upstream scripts, hooks, skills or assets are bundled.
