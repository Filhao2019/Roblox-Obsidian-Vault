---
title: Free and Paid Asset Sources
date: 2026-11-02
tags: [3d, assets, licenses, security]
status: researched
---

# Free and Paid Asset Sources

Where to get models, textures and kits, what each license allows, and how to avoid backdoored free models. Licenses change: always re-read the asset page and keep a record (name, author, URL, license, date) for every third-party asset. This note is not legal advice. Ready-made link lists live in [[3D Asset References]].

## License cheat sheet

| Source | Typical license | Commercial in a Roblox game? | Attribution | Notes |
|---|---|---|---|---|
| Quaternius | CC0 | Yes | Not required | 83 packs listed; FBX/OBJ/glTF/Blend; some Patreon-only models (e.g. a Cop SUV in the cars pack) |
| Kenney | CC0 (per OpenGameArt listings; the asset index page itself shows no license text, so check each pack) | Yes | Appreciated | Kits like Nature Kit, Fantasy Town Kit, Castle Kit, City Kits |
| Poly Pizza | CC0 and CC-BY per model | Yes | Required for CC-BY | Check each model page; some models are Google Poly CC-BY |
| Poly Haven | CC0 | Yes | Not required | Models, HDRIs, textures; site logos/renders are not CC0 |
| ambientCG | CC0 | Yes | Not required | PBR surfaces, HDRIs |
| OpenGameArt | Mixed (CC0, CC-BY, GPL...) | Depends | Depends | Read each entry |
| BlenderKit | Royalty Free or CC0 | Yes, no resale of the asset itself | Not required | Cannot resell the model as a model or pack |
| Sketchfab | Per-model Creative Commons or standard | Only if license allows | CC-BY needs credit | Filter to downloadable; CC-BY-NC or ND are not suitable for commercial games |
| Fab (Epic) | Seller license, often engine-restricted | Check listing | Per listing | Many listings are Unreal/Unity focused; check that the license permits other engines |
| Synty Store | Seat-based proprietary | Seat count applies | Not required | Advertised for Unity/Unreal/Godot; a listing shows 5 seats per copy, no Roblox mention found: confirm with Synty before using in Roblox |
| Unity Asset Store | Unity-specific EULA | Usually Unity-only | n/a | Do not assume Roblox use is permitted |
| Roblox Creator Store | Per creator, Roblox terms | Yes inside Roblox per terms | n/a | Free models may carry scripts: see warning |
| itch.io, BuiltByBit, CGTrader, TurboSquid | Seller EULA | Check | Check | Read for engine/platform restrictions, resale bans |

## Roblox-specific

- Creator Store assets sold or shared must comply with the Community Rules, Terms of Use and IP guidelines. Seller accounts run through Stripe in supported countries.
- Marketplace policy pages cover avatar items separately from general Creator Store assets.
- Models you upload from external sources must be ones you have rights to; fan art of memes or franchises can be moderated (Steal a Brainrot removed a character after a licensing dispute).

## Backdoor warning (free models)

Free Toolbox/Creator Store models can hide scripts that give an attacker server access. Roblox says its moderation does not guarantee removal of all malicious scripts. Defenses:

1. **Sandbox inserted models:** set SandboxedInstance to Experimental on Workspace, set the model's Sandboxed property, and grant only needed Capabilities. Be careful with Network, DataStore, AssetRequire, CapabilityControl and LoadString. Roblox plans to auto-sandbox Creator Store assets later.
2. **Delete all Scripts** from free meshes; import only the mesh, not the packaged scripts.
3. **Search for red flags:** `require(<asset id>)`, `HttpService`/`HttpGet`, `getfenv`, `loadstring`, obfuscated strings, code hidden far off-screen with whitespace.
4. **Use scanners:** community plugins such as ShieldScan (heuristic; always review manually).
5. **Prefer own meshes or license-clear packs** (Quaternius, Kenney) imported as plain FBX/glTF, which carry no scripts.

See also [[Security and Anti-Exploit]].

## References

- [Third-party vulnerabilities (backdoors)](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) — official · sandboxing, capabilities
- [Creator Store publishing](https://create.roblox.com/docs/production/publishing/creator-store) — official · store overview
- [Publishing assets](https://create.roblox.com/docs/production/publishing/publishing-assets) — official · compliance, seller accounts
- [Selling on the Creator Store](https://create.roblox.com/docs/production/publishing/selling-on-the-creator-store) — official · selling
- [Creator Store marketplace page](https://create.roblox.com/docs/production/publishing/creator-marketplace) — official · marketplace
- [Marketplace overview](https://create.roblox.com/docs/marketplace.md) — official · policy index
- [Assets overview](https://create.roblox.com/docs/en-us/assets.md) — official · asset types
- [ShieldScan anti-backdoor scanner](https://devforum.roblox.com/t/shieldscan-anti-backdoor-scanner-for-roblox-studio/4736119) — DevForum · plugin
- [How to remove backdoors from your game](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game) — DevForum · cleanup guide
- [Backdooring Explained (Chapter 2)](https://devforum.roblox.com/t/backdooring-explained-chapter-2/998413) — DevForum · require-based backdoors
- [Is this some virus?](https://devforum.roblox.com/t/is-this-some-virus/4026622) — DevForum · example report
- [How to prevent Roblox game backdoors](https://www.creation.dev/learn/how-to-prevent-roblox-game-backdoors) — third-party guide · checklist
- [ClearlyDev marketplace thread](https://devforum.roblox.com/t/clearlydev-%E2%80%93-buy-sell-high-quality-roblox-creations/3968558) — DevForum · third-party marketplace
- [KitsBlox terms](https://kitsblox.com/terms) — seller marketplace · example terms
- [KitsBlox licenses](https://kitsblox.com/licenses) — seller marketplace · Roblox-only licensing example
- [Quaternius home](https://quaternius.com) — CC0 library
- [Quaternius Ultimate Platformer Pack](https://quaternius.itch.io/ultimate-platformer-pack) — itch.io · CC0 statement
- [Quaternius licensing guide](https://licenseorg.com/guide/3d-assets/quaternius) — third-party guide · CC0 summary
- [Quaternius profile (Game World Observer)](https://gameworldobserver.com/2023/01/20/free-game-assets-tutorials-quaternius-indie-developers) — news · catalog size
- [Kenney assets](https://kenney.nl/assets) — CC0 library
- [Kenney Nature Kit (OpenGameArt)](https://opengameart.org/content/nature-kit) — listing · CC0
- [Kenney Fantasy Town Kit (OpenGameArt)](https://opengameart.org/content/fantasy-town-kit) — listing · attribution optional
- [Poly Pizza upload guidelines](https://poly.pizza/docs/uploading) — site docs · CC0/CC-BY
- [Poly Pizza overview (GameFromScratch)](https://gamefromscratch.com/poly-pizza-a-replacement-to-google-poly/) — article · Google Poly replacement
- [Poly Haven license](https://polyhaven.com/license) — license page · CC0
- [ambientCG](https://ambientcg.com/) — site · CC0
- [BlenderKit licenses](https://www.blendkit.com/docs/licenses/) — license page · Royalty Free vs CC0
- [Synty POLYGON Dungeon Pack](https://syntystore.com/products/polygon-dungeon-pack) — store · 5-seat license
- [Free 3D model sites guide (Cinevva)](https://app.cinevva.com/de/guides/free-3d-model-sites) — guide · site roundup (third-party)
- [Best low-poly model sites (DEV Community)](https://dev.to/dook/the-5-best-sites-for-free-low-poly-3d-models-for-unity-44lb) — article · site roundup

Links: [[3D Assets MOC]] · [[00 Home]]
