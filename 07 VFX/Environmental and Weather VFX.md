---
title: Environmental and Weather VFX
date: 2026-11-02
tags: [vfx, research]
status: researched
---

# Environmental and Weather VFX

Build atmosphere from a small number of visual jobs: distant mood, local movement, and readable landmarks. This research was reviewed 2026-11-02. The suggested scene recipes below are design exercises; no weather controller or device benchmark was implemented.

## Choose the right layer

| Goal | Candidate | Important distinction |
|---|---|---|
| Obscure the far distance or change mood | Atmosphere | Affects the overall scene, not individual rain streaks |
| Dust, sparks, snow or drifting motes | ParticleEmitter | Local visible particles need controlled density and lifetime |
| A connection or continuous sheet between points | Beam | Requires two attachments; appearance depends on viewpoint |
| Light on nearby surfaces | A local light source | Bright-looking particles alone do not light geometry |

The effects overview distinguishes particles, beams, trails and local lights. [Roblox effects](https://create.roblox.com/docs/effects). Atmosphere exposes density, offset, haze and color controls; density can conceal distant objects, so visibility is a gameplay concern. [Atmospheric effects](https://create.roblox.com/docs/environment/atmosphere).

## Illustrated comparison: a beam is a surface

![[beams-Default-Beam.png|800]]

![[beams-Texture-Applied.png|800]]

Official default/textured beam examples, not screenshots of weather or a profiled game. Roblox Corporation and creator-docs contributors; CC BY 4.0; unchanged. See [[Particles and Beams Visual Study]] for pinned source media and [[Media Attribution and Reuse]] for attribution and hashes.

A beam draws its texture between attachments. Width, curvature, texture repetition and camera-facing behavior shape the result. Inspect it from several angles and at low/high graphics settings. [Beams](https://create.roblox.com/docs/effects/beams).

## Original scene recipes to prototype

- **Dusty hallway:** sparse motes near a light cone and a restrained distant haze. Keep the exit silhouette visible. Avoid covering the entire corridor in dense particles just to imply age.
- **Rainy courtyard:** local rain coverage around the active play space, a separate splash cue, and a sheltered indoor state. Decide whether roofs stop rain before adding distant scenery effects.
- **Snow:** compare slower flakes with faster travel, then examine camera motion and bright backgrounds. Choose a density from actual readability and performance checks.
- **Fireflies:** use sparse, short-lived accents away from critical targets; ensure they cannot be confused with interaction markers.

These are original production starting points, not documented implementations of [[Grow a Garden]] or [[Doors]].

## Lifecycle and acceptance

For particles, disabling emission does not instantly remove existing particles; `Clear()` removes them. Choose explicitly between a natural fade and an immediate cut when changing zones. [Particle emitters](https://create.roblox.com/docs/effects/particle-emitters).

Proposed checks: enter/leave shelter repeatedly; respawn and teleport between zones; overlap weather transitions; inspect low graphics and a real phone; compare frame time with effects enabled/disabled; confirm objectives remain legible. Record actual results in [[Playtest Record]]. No device test has been run for these recipes.

## Mentioned in

- [[Grow a Garden]]
- [[Jump Fall and Land]]
- [[VFX Fundamentals]]
- [[VFX of Top Games]]


## References

- [Effects](https://create.roblox.com/docs/effects) — official overview · object choices.
- [Atmospheric effects](https://create.roblox.com/docs/environment/atmosphere) — official guide · distance and mood.
- [Beams](https://create.roblox.com/docs/effects/beams) — official illustrated guide · attachments and viewing angles.
- [Particle emitters](https://create.roblox.com/docs/effects/particle-emitters) — official guide · lifecycle.
- [[Media Attribution and Reuse]] — local media provenance.

Links: [[VFX MOC]] · [[00 Home]]
