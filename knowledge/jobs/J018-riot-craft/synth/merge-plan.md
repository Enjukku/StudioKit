---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b synthesizer working memory: knowledge/jobs/J018-riot-craft/synth/all-index.md and bundles"
supersedes: []
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# J018 stage 1b merge plan and coverage record

Output folder: `knowledge/reference/craft/riot/`. If context is compacted: re-read this file, then continue from the progress log (last line = next step).

## 1. Topic plan

| File | Prefix | Holds | Folded in |
| --- | --- | --- | --- |
| value-contrast.md | VC | value structure, contrast for focus, value bands, form shading | — |
| visual-hierarchy.md | VH | what reads first, restraint, noise, detail clumping and rest, read order | — |
| shape-silhouette.md | SS | silhouette, shape language, simplification, gesture, motifs | — |
| character-design.md | CD | character core, identity anchors, anatomy, faces, design for motion | — |
| exaggeration.md | EX | pushing poses and forms past real, safe extremes | — |
| weight-timing.md | WT | anticipation, spacing, impact, landing, build-ups, mass | — |
| rhythm.md | RH | cadence, offsets, holds, beginning-middle-end, motion in stills | — |
| light-colour.md | LC | light direction, temperature, palette roles, reserved colours, colour meaning | — |
| composition-focus.md | CF | framing, focal point, eye path, depth groups, camera, crops | — |
| materials-detail.md | MD | surfaces, edges, wear, detail density, grounding | — |
| world-level-readability.md | WL | gameplay readability of worlds and levels, scale, wayfinding, storytelling props | new-environmental-storytelling |
| vfx-reads-timing.md | VR | effect reads, energy look, particle behaviour | — |
| sound.md | SD | sound jobs, mixing, layering, identity, sync | — |
| ui-ux.md | UI | UX before UI, motion goals, UI ecosystem | — |
| game-design-fun.md | GD | fun types, feedback, fairness, maps as boards, cosmetics vs gameplay | — |
| references-ideation.md | RI | research, reference, options, hooks, acting out | — |
| critique-feedback.md | CR | asking for and giving notes, judging in game, paint-overs | — |
| style-identity.md | SI | one style, audience, theme fit, tone, variants and tiers | — |
| process-iteration.md | PI | ADDED: stage order, gates, timebox, closing doors, not precious, when done | new-timebox, new-stage-gates, new-production-gates, new-decisiveness |
| pipeline-production.md | PP | ADDED: budgets, rig-ready building, UVs, kits, files, effect cost, asset kits | pipeline-tech, new-performance-budget, new-asset-kit |
| cross-craft.md | CC | ADDED: one vision across crafts, hand-offs, building for the next craft, crew split | new-cross-craft-handoff, new-cross-craft-cohesion, new-crew-split |

Placement rule: a finding goes where a maker would look first; the other topics go in "also:". Merge rule: same idea → one finding with all sources; different checkable rules stay separate.

## 2. Mapping (all 649 extract IDs)

All rows carry their final library ID(s); the note names the merge partners (and, where useful, why the finding moved topic).

| extract ID | library ID(s) | note |
| --- | --- | --- |
| R00a-F01 | GD-01 | merged with R00b-F27 |
| R00a-F02 | WL-01 | merged with R02-F23, R09-F04 |
| R00a-F03 | GD-02 | merged with R06-F02 |
| R00a-F04 | SI-01 | merged with R01-F22 |
| R00a-F05 | VH-01 | merged with R13-F07 |
| R00a-F06 | VC-01 | single |
| R00a-F07 | VC-04 | merged with R08-F22, R11-F26 |
| R00a-F08 | SS-05 | merged with R12-F11, R01-F13, R11-F22 |
| R00a-F09 | VH-10 | single |
| R00a-F10 | LC-01 | merged with R02-F11, R09-F03 |
| R00a-F11 | VH-05 | merged with R02-F22, R00b-F11, R09-F45 |
| R00a-F12 | WL-25 | single |
| R00a-F13 | RI-01 | merged with R11-F10 |
| R00a-F14 | RI-03 | merged with R08-F26, R06-F03 |
| R00a-F15 | SI-03 | merged with R13-F02 |
| R00a-F16 | CF-02 | merged with R11-F12, R04-F06 |
| R00a-F17 | GD-09 | single |
| R00a-F18 | RI-05 | merged with R01-F01, R05-F05, R09-F28 |
| R00a-F19 | RI-16 | merged with R11-F01, R12-F03 |
| R00a-F20 | RI-18 | merged with R12-F04, R05-F06 |
| R00a-F21 | PI-01 | merged with R03-F04 |
| R00a-F22 | SS-01 | merged with R05-F15, R10-F11, R05-F32 |
| R00a-F23 | PI-03 | single |
| R00a-F24 | CR-02 | merged with R11-F30 |
| R00a-F25 | CR-07 | merged with R08-F19 |
| R00a-F26 | CR-14 | single |
| R00a-F27 | CD-03 | single |
| R00a-F28 | SI-02 | merged with R05-F33 |
| R00a-F29 | SI-05 | merged with R08-F17 |
| R00a-F30 | CD-07 | single |
| R00a-F31 | CD-08 | merged with R13-F20, R13-F25 |
| R00a-F32 | SS-04 | merged with R11-F15, R01-F52, R03-F09 |
| R00a-F33 | PI-04 | merged with R09-F12 |
| R00a-F34 | PP-01 | merged with R13-F28 |
| R00a-F35 | PP-03 | merged with R02-F29 |
| R00a-F36 | MD-06 | single |
| R00a-F37 | CD-10 | merged with R01-F39 |
| R00a-F38 | CD-11 | single |
| R00a-F39 | CD-12 | merged with R11-F25, R01-F33, R03-F39 |
| R00b-F01 | WL-06 | single |
| R00b-F02 | PP-26 | merged with R09-F34 |
| R00b-F03 | CR-05 | merged with R03-F35, R13-F08 |
| R00b-F04 | WL-04 | single |
| R00b-F05 | WL-03 | single |
| R00b-F06 | CF-08 | merged with R13-F11, R13-F12 |
| R00b-F07 | WL-07 | merged with R09-F22 |
| R00b-F08 | LC-12 | merged with R02-F03 |
| R00b-F09 | MD-07 | single |
| R00b-F10 | CF-13 | single |
| R00b-F11 | VH-05 | merged with R02-F22, R00a-F11, R09-F45 |
| R00b-F12 | WL-22 | merged with R02-F32, R09-F23, R13-F15 |
| R00b-F13 | RI-10 | merged with R02-F18, R03-F27, R00c-F16, R06-F31 |
| R00b-F14 | WL-21 | merged with R02-F27, R13-F17 |
| R00b-F15 | PP-24 | merged with R09-F37 |
| R00b-F16 | CR-03 | merged with R00d-F35 |
| R00b-F17 | WL-24 | single |
| R00b-F18 | MD-09 | merged with R11-F20 |
| R00b-F19 | PI-09 | merged with R04-F19, R08-F24, R07-F30 |
| R00b-F20 | PP-28 | merged with R00b-F23 |
| R00b-F21 | PP-18 | single |
| R00b-F22 | PP-19 | single |
| R00b-F23 | PP-28 | merged with R00b-F20 |
| R00b-F24 | PP-29 | merged with R09-F07 |
| R00b-F25 | PP-30 | single |
| R00b-F26 | MD-05 | merged with R02-F04, R02-F15 |
| R00b-F27 | GD-01 | merged with R00a-F01 |
| R00b-F28 | WT-01 | merged with R04-F21 |
| R00b-F29 | WT-02 | single |
| R00b-F30 | WT-03 | single |
| R00b-F31 | CD-09 | merged with R04-F23 |
| R00b-F32 | RI-24 | merged with R06-F22, R04-F30 |
| R00b-F33 | SS-10 | merged with R08-F10 |
| R00b-F34 | WT-07 | single |
| R00b-F35 | WT-08 | single |
| R00b-F36 | EX-02 | single |
| R00b-F37 | WT-09 | single |
| R00b-F38 | EX-06 | single |
| R00b-F39 | PP-20 | single |
| R00b-F40 | RI-25 | single |
| R00b-F41 | CR-16 | single |
| R00c-F01 | VR-08 | merged with R06-F26 |
| R00c-F02 | VR-01 | merged with R06-F01 |
| R00c-F03 | VR-18 | merged with R06-F30 |
| R00c-F04 | VR-02 | merged with R00c-F06, R00c-F07 |
| R00c-F05 | VR-03 | merged with R12-F31 |
| R00c-F06 | VR-02 | merged with R00c-F04, R00c-F07 |
| R00c-F07 | VR-02 | merged with R00c-F04, R00c-F06 |
| R00c-F08 | VH-02 | single |
| R00c-F09 | VR-05 | single |
| R00c-F10 | LC-02 | merged with R06-F18 |
| R00c-F11 | LC-19 | single |
| R00c-F12 | LC-20 | single |
| R00c-F13 | WT-11 | single |
| R00c-F14 | WT-12 | merged with R06-F14, R07-F19 |
| R00c-F15 | WT-13 | merged with R06-F24 |
| R00c-F16 | RI-10 | merged with R00b-F13, R02-F18, R03-F27, R06-F31 |
| R00c-F17 | SD-02 | single |
| R00c-F18 | SD-01 | merged with R07-F01 |
| R00c-F19 | SD-27 | single |
| R00c-F20 | SD-08 | merged with R07-F08 |
| R00c-F21 | SD-07 | merged with R07-F13 |
| R00c-F22 | WT-23 | single |
| R00c-F23 | SD-09 | single |
| R00c-F24 | SD-10 | single |
| R00c-F25 | SD-11 | merged with R07-F11 |
| R00c-F26 | SD-13 | merged with R07-F14 |
| R00c-F27 | SD-06 | single |
| R00c-F28 | SD-30 | merged with R07-F10 |
| R00c-F29 | SD-22 | single |
| R00c-F30 | SD-28 | merged with R07-F29 |
| R00c-F31 | SD-29 | merged with R07-F07, R07-F28 |
| R00c-F32 | SD-33 | single |
| R00d-F01 | UI-01 | merged with R00d-F12 |
| R00d-F02 | UI-02 | single |
| R00d-F03 | UI-03 | single |
| R00d-F04 | UI-04 | single |
| R00d-F05 | UI-05 | single |
| R00d-F06 | UI-06 | single |
| R00d-F07 | UI-07 | single |
| R00d-F08 | UI-09 | single |
| R00d-F09 | UI-10 | single |
| R00d-F10 | UI-08 | single |
| R00d-F11 | UI-11 | single |
| R00d-F12 | UI-01 | merged with R00d-F01 |
| R00d-F13 | UI-12 | single |
| R00d-F14 | UI-13 | single |
| R00d-F15 | UI-14 | single |
| R00d-F16 | UI-15 | single |
| R00d-F17 | UI-16 | single |
| R00d-F18 | CR-15 | single |
| R00d-F19 | RI-15 | single |
| R00d-F20 | CR-10 | merged with R05-F17 |
| R00d-F21 | GD-03 | single |
| R00d-F22 | GD-04 | merged with R00d-F23 |
| R00d-F23 | GD-04 | merged with R00d-F22 |
| R00d-F24 | CC-01 | merged with R03-F46 |
| R00d-F25 | GD-05 | single |
| R00d-F26 | GD-06 | single |
| R00d-F27 | GD-07 | single |
| R00d-F28 | GD-10 | single |
| R00d-F29 | GD-11 | single |
| R00d-F30 | GD-12 | single |
| R00d-F31 | GD-13 | single |
| R00d-F32 | GD-14 | single |
| R00d-F33 | GD-15 | merged with R09-F02 |
| R00d-F34 | CR-11 | merged with R10-F22 |
| R00d-F35 | CR-03 | merged with R00b-F16 |
| R01-F01 | RI-05 | merged with R00a-F18, R05-F05, R09-F28 |
| R01-F02 | PP-17 | single |
| R01-F03 | PP-12 | merged with R03-F37, R03-F38 |
| R01-F04 | PP-14 | merged with R12-F17 |
| R01-F05 | CD-05 | single |
| R01-F06 | VC-03 | merged with R13-F10, R01-F34 |
| R01-F07 | VC-08 | merged with R03-F41, R03-F33, R01-F35; restated for Roblox third-person camera |
| R01-F08 | VH-06 | merged with R06-F12 |
| R01-F09 | PP-09 | merged with R13-F22 |
| R01-F10 | CD-01 | merged with R11-F04, R03-F07 |
| R01-F11 | VH-04 | merged with R11-F06 |
| R01-F12 | EX-01 | merged with R11-F16 |
| R01-F13 | SS-05 | merged with R12-F11, R11-F22, R00a-F08 |
| R01-F14 | CC-03 | merged with R03-F12 |
| R01-F15 | PP-15 | merged with R11-F05 |
| R01-F16 | CR-01 | merged with R03-F45, R06-F07, R03-F11 |
| R01-F17 | RI-06 | merged with R01-F36 |
| R01-F18 | CD-13 | merged with R11-F23 |
| R01-F19 | SS-16 | single |
| R01-F20 | EX-04 | single |
| R01-F21 | MD-11 | merged with R12-F34 |
| R01-F22 | SI-01 | merged with R00a-F04 |
| R01-F23 | CF-16 | merged with R05-F36 |
| R01-F24 | CD-15 | single |
| R01-F25 | SS-17 | merged with R12-F09 |
| R01-F26 | MD-01 | merged with R13-F13, R03-F22, R02-F06 |
| R01-F27 | PP-16 | single |
| R01-F28 | MD-02 | merged with R10-F24, R02-F20, R02-F21 |
| R01-F29 | CD-16 | single |
| R01-F30 | SI-11 | single |
| R01-F31 | CD-04 | merged with R08-F03, R10-F04, R11-F19, R03-F16, R12-F07 |
| R01-F32 | GD-20 | single |
| R01-F33 | CD-12 | merged with R00a-F39, R11-F25, R03-F39 |
| R01-F34 | VC-03 | merged with R01-F06, R13-F10 |
| R01-F35 | VC-08 | merged with R01-F07, R03-F41, R03-F33; restated for Roblox third-person camera |
| R01-F36 | RI-06 | merged with R01-F17 |
| R01-F37 | LC-06 | single |
| R01-F38 | LC-05 | single |
| R01-F39 | CD-10 | merged with R00a-F37 |
| R01-F40 | CD-29 | single |
| R01-F41 | PP-13 | single |
| R01-F42 | CD-17 | single |
| R01-F43 | WT-24 | single |
| R01-F44 | GD-16 | merged with R12-F06 |
| R01-F45 | SI-12 | single |
| R01-F46 | CC-05 | merged with R05-F13 |
| R01-F47 | RI-27 | single |
| R01-F48 | SI-13 | merged with R05-F39 |
| R01-F49 | CD-18 | single |
| R01-F50 | CF-09 | merged with R12-F12 |
| R01-F51 | SS-03 | single |
| R01-F52 | SS-04 | merged with R00a-F32, R11-F15, R03-F09 |
| R01-F53 | SS-18 | merged with R12-F16 |
| R02-F01 | CF-01 | merged with R10-F07, R09-F30, R05-F24 |
| R02-F02 | LC-09 | single |
| R02-F03 | LC-12 | merged with R00b-F08 |
| R02-F04 | MD-05 | merged with R00b-F26, R02-F15 |
| R02-F05 | MD-03 | merged with R13-F24, R10-F13 |
| R02-F06 | MD-01 | merged with R13-F13, R01-F26, R03-F22 |
| R02-F07 | LC-10 | merged with R03-F03, R03-F43; restated for Roblox camera |
| R02-F08 | PP-05 | merged with R03-F40 |
| R02-F09 | PI-11 | merged with R03-F20 |
| R02-F10 | WL-23 | single |
| R02-F11 | LC-01 | merged with R09-F03, R00a-F10 |
| R02-F12 | SI-07 | merged with R02-F28 |
| R02-F13 | MD-10 | merged with R13-F35 |
| R02-F14 | VC-09 | merged with R03-F06, R12-F33 |
| R02-F15 | MD-05 | merged with R02-F04, R00b-F26 |
| R02-F16 | PI-06 | merged with R03-F10, R04-F40 |
| R02-F17 | MD-08 | single |
| R02-F18 | RI-10 | merged with R00b-F13, R03-F27, R00c-F16, R06-F31 |
| R02-F19 | GD-32 | single |
| R02-F20 | MD-02 | merged with R01-F28, R10-F24, R02-F21 |
| R02-F21 | MD-02 | merged with R01-F28, R10-F24, R02-F20 |
| R02-F22 | VH-05 | merged with R00a-F11, R00b-F11, R09-F45 |
| R02-F23 | WL-01 | merged with R00a-F02, R09-F04 |
| R02-F24 | LC-08 | merged with R13-F29 |
| R02-F25 | GD-31 | single |
| R02-F26 | SD-23 | merged with R09-F20 |
| R02-F27 | WL-21 | merged with R00b-F14, R13-F17 |
| R02-F28 | SI-07 | merged with R02-F12 |
| R02-F29 | PP-03 | merged with R00a-F35 |
| R02-F30 | PP-06 | merged with R13-F38 |
| R02-F31 | MD-15 | single |
| R02-F32 | WL-22 | merged with R00b-F12, R09-F23, R13-F15 |
| R02-F33 | PP-04 | single |
| R02-F34 | VC-05 | merged with R13-F31, R09-F32 |
| R02-F35 | CF-12 | single |
| R02-F36 | MD-16 | single |
| R02-F37 | SS-06 | merged with R05-F26 |
| R02-F38 | WL-27 | single |
| R02-F39 | PP-10 | single |
| R03-F01 | MD-04 | single |
| R03-F02 | RI-11 | merged with R03-F13 |
| R03-F03 | LC-10 | merged with R02-F07, R03-F43; restated for Roblox camera |
| R03-F04 | PI-01 | merged with R00a-F21 |
| R03-F05 | PP-02 | single |
| R03-F06 | VC-09 | merged with R02-F14, R12-F33 |
| R03-F07 | CD-01 | merged with R01-F10, R11-F04 |
| R03-F08 | WL-28 | merged with R12-F32 |
| R03-F09 | SS-04 | merged with R00a-F32, R11-F15, R01-F52 |
| R03-F10 | PI-06 | merged with R02-F16, R04-F40 |
| R03-F11 | CR-01 | merged with R01-F16, R03-F45, R06-F07 |
| R03-F12 | CC-03 | merged with R01-F14 |
| R03-F13 | RI-11 | merged with R03-F02 |
| R03-F14 | CD-22 | merged with R08-F31 |
| R03-F15 | CD-23 | single |
| R03-F16 | CD-04 | merged with R08-F03, R10-F04, R11-F19, R01-F31, R12-F07 |
| R03-F17 | SI-06 | single |
| R03-F18 | PI-10 | single |
| R03-F19 | PI-12 | merged with R08-F30, R04-F45 |
| R03-F20 | PI-11 | merged with R02-F09 |
| R03-F21 | VC-13 | merged with R03-F31 |
| R03-F22 | MD-01 | merged with R13-F13, R01-F26, R02-F06 |
| R03-F23 | RI-14 | single |
| R03-F24 | VC-11 | single |
| R03-F25 | VC-10 | single |
| R03-F26 | MD-14 | single |
| R03-F27 | RI-10 | merged with R00b-F13, R02-F18, R00c-F16, R06-F31 |
| R03-F28 | SS-12 | single |
| R03-F29 | CD-27 | single |
| R03-F30 | SI-08 | single |
| R03-F31 | VC-13 | merged with R03-F21 |
| R03-F32 | CD-28 | single |
| R03-F33 | VC-08 | merged with R01-F07, R03-F41, R01-F35; restated for Roblox third-person camera |
| R03-F34 | LC-07 | merged with R13-F06 |
| R03-F35 | CR-05 | merged with R00b-F03, R13-F08 |
| R03-F36 | RI-13 | single |
| R03-F37 | PP-12 | merged with R01-F03, R03-F38 |
| R03-F38 | PP-12 | merged with R01-F03, R03-F37 |
| R03-F39 | CD-12 | merged with R00a-F39, R11-F25, R01-F33 |
| R03-F40 | PP-05 | merged with R02-F08 |
| R03-F41 | VC-08 | merged with R01-F07, R03-F33, R01-F35; restated for Roblox third-person camera |
| R03-F42 | LC-25 | single |
| R03-F43 | LC-10 | merged with R02-F07, R03-F03; restated for Roblox camera |
| R03-F44 | VC-12 | single |
| R03-F45 | CR-01 | merged with R01-F16, R06-F07, R03-F11 |
| R03-F46 | CC-01 | merged with R00d-F24 |
| R04-F01 | WT-04 | merged with R04-F39 |
| R04-F02 | WT-05 | single |
| R04-F03 | WT-06 | single |
| R04-F04 | WT-17 | single |
| R04-F05 | WT-18 | single |
| R04-F06 | CF-02 | merged with R00a-F16, R11-F12 |
| R04-F07 | CC-02 | merged with R07-F05 |
| R04-F08 | PP-21 | single |
| R04-F09 | WT-14 | single |
| R04-F10 | WT-15 | single |
| R04-F11 | WT-16 | merged with R04-F36 |
| R04-F12 | RH-04 | single |
| R04-F13 | EX-05 | merged with R04-F22 |
| R04-F14 | EX-07 | single |
| R04-F15 | RH-01 | single |
| R04-F16 | WT-22 | merged with R04-F31, R04-F38 |
| R04-F17 | EX-08 | single |
| R04-F18 | EX-09 | single |
| R04-F19 | PI-09 | merged with R00b-F19, R08-F24, R07-F30 |
| R04-F20 | WT-21 | merged with R04-F35 |
| R04-F21 | WT-01 | merged with R00b-F28 |
| R04-F22 | EX-05 | merged with R04-F13 |
| R04-F23 | CD-09 | merged with R00b-F31 |
| R04-F24 | SS-11 | single |
| R04-F25 | RH-02 | single |
| R04-F26 | EX-10 | merged with R04-F37 |
| R04-F27 | PP-22 | single |
| R04-F28 | WT-19 | single |
| R04-F29 | WT-20 | single |
| R04-F30 | RI-24 | merged with R00b-F32, R06-F22 |
| R04-F31 | WT-22 | merged with R04-F16, R04-F38 |
| R04-F32 | SS-15 | merged with R11-F14 |
| R04-F33 | PI-07 | merged with R08-F14 |
| R04-F34 | WT-10 | single |
| R04-F35 | WT-21 | merged with R04-F20 |
| R04-F36 | WT-16 | merged with R04-F11 |
| R04-F37 | EX-10 | merged with R04-F26 |
| R04-F38 | WT-22 | merged with R04-F16, R04-F31 |
| R04-F39 | WT-04 | merged with R04-F01 |
| R04-F40 | PI-06 | merged with R02-F16, R03-F10 |
| R04-F41 | WT-25 | single |
| R04-F42 | CD-24 | single |
| R04-F43 | RI-26 | single |
| R04-F44 | PP-23 | single |
| R04-F45 | PI-12 | merged with R03-F19, R08-F30 |
| R05-F01 | RI-04 | single |
| R05-F02 | SI-14 | single |
| R05-F03 | RI-07 | single |
| R05-F04 | LC-04 | merged with R12-F23 |
| R05-F05 | RI-05 | merged with R01-F01, R00a-F18, R09-F28 |
| R05-F06 | RI-18 | merged with R00a-F20, R12-F04 |
| R05-F07 | SS-19 | single |
| R05-F08 | RI-19 | merged with R10-F03, R13-F03 |
| R05-F09 | EX-03 | single |
| R05-F10 | CF-17 | single |
| R05-F11 | CF-06 | merged with R08-F15 |
| R05-F12 | CD-25 | single |
| R05-F13 | CC-05 | merged with R01-F46 |
| R05-F14 | CR-06 | merged with R13-F34 |
| R05-F15 | SS-01 | merged with R10-F11, R00a-F22, R05-F32 |
| R05-F16 | CF-04 | merged with R10-F02, R08-F05 |
| R05-F17 | CR-10 | merged with R00d-F20 |
| R05-F18 | LC-17 | merged with R05-F38 |
| R05-F19 | LC-15 | single |
| R05-F20 | LC-23 | merged with R12-F36 |
| R05-F21 | LC-24 | single |
| R05-F22 | LC-14 | single |
| R05-F23 | PP-31 | single |
| R05-F24 | CF-01 | merged with R10-F07, R09-F30, R02-F01 |
| R05-F25 | WL-26 | single |
| R05-F26 | SS-06 | merged with R02-F37 |
| R05-F27 | PP-32 | merged with R05-F37 |
| R05-F28 | PP-33 | single |
| R05-F29 | VC-17 | single |
| R05-F30 | SI-15 | single |
| R05-F31 | CF-15 | merged with R08-F21 |
| R05-F32 | SS-01 | merged with R05-F15, R10-F11, R00a-F22 |
| R05-F33 | SI-02 | merged with R00a-F28 |
| R05-F34 | SI-16 | single |
| R05-F35 | CR-12 | single |
| R05-F36 | CF-16 | merged with R01-F23 |
| R05-F37 | PP-32 | merged with R05-F27 |
| R05-F38 | LC-17 | merged with R05-F18 |
| R05-F39 | SI-13 | merged with R01-F48 |
| R06-F01 | VR-01 | merged with R00c-F02 |
| R06-F02 | GD-02 | merged with R00a-F03 |
| R06-F03 | RI-03 | merged with R00a-F14, R08-F26 |
| R06-F04 | PP-25 | merged with R09-F29 |
| R06-F05 | VR-06 | single |
| R06-F06 | VR-07 | single |
| R06-F07 | CR-01 | merged with R01-F16, R03-F45, R03-F11 |
| R06-F08 | PI-08 | single |
| R06-F09 | VR-10 | single |
| R06-F10 | LC-03 | merged with R06-F29 |
| R06-F11 | VR-11 | single |
| R06-F12 | VH-06 | merged with R01-F08 |
| R06-F13 | VR-12 | single |
| R06-F14 | WT-12 | merged with R07-F19, R00c-F14 |
| R06-F15 | VC-07 | merged with R12-F25 |
| R06-F16 | VR-04 | single |
| R06-F17 | CF-10 | single |
| R06-F18 | LC-02 | merged with R00c-F10 |
| R06-F19 | VR-13 | single |
| R06-F20 | RH-03 | single |
| R06-F21 | VR-09 | single |
| R06-F22 | RI-24 | merged with R00b-F32, R04-F30 |
| R06-F23 | CF-11 | single |
| R06-F24 | WT-13 | merged with R00c-F15 |
| R06-F25 | VR-17 | single |
| R06-F26 | VR-08 | merged with R00c-F01 |
| R06-F27 | VR-14 | single |
| R06-F28 | VR-15 | single |
| R06-F29 | LC-03 | merged with R06-F10 |
| R06-F30 | VR-18 | merged with R00c-F03 |
| R06-F31 | RI-10 | merged with R00b-F13, R02-F18, R03-F27, R00c-F16 |
| R07-F01 | SD-01 | merged with R00c-F18 |
| R07-F02 | SD-04 | single |
| R07-F03 | SD-21 | merged with R07-F32 |
| R07-F04 | SD-05 | single |
| R07-F05 | CC-02 | merged with R04-F07 |
| R07-F06 | SD-24 | single |
| R07-F07 | SD-29 | merged with R00c-F31, R07-F28 |
| R07-F08 | SD-08 | merged with R00c-F20 |
| R07-F09 | SD-17 | single |
| R07-F10 | SD-30 | merged with R00c-F28 |
| R07-F11 | SD-11 | merged with R00c-F25 |
| R07-F12 | SD-12 | single |
| R07-F13 | SD-07 | merged with R00c-F21 |
| R07-F14 | SD-13 | merged with R00c-F26 |
| R07-F15 | SD-14 | single |
| R07-F16 | SD-15 | merged with R07-F17 |
| R07-F17 | SD-15 | merged with R07-F16 |
| R07-F18 | SD-16 | single |
| R07-F19 | WT-12 | merged with R06-F14, R00c-F14 |
| R07-F20 | SD-20 | single |
| R07-F21 | SD-19 | single |
| R07-F22 | SD-18 | single |
| R07-F23 | SD-03 | single |
| R07-F24 | SD-26 | single |
| R07-F25 | SD-25 | single |
| R07-F26 | SD-31 | single |
| R07-F27 | SD-32 | single |
| R07-F28 | SD-29 | merged with R07-F07, R00c-F31 |
| R07-F29 | SD-28 | merged with R00c-F30 |
| R07-F30 | PI-09 | merged with R00b-F19, R04-F19, R08-F24 |
| R07-F31 | CC-06 | single |
| R07-F32 | SD-21 | merged with R07-F03 |
| R08-F01 | GD-18 | single |
| R08-F02 | SI-09 | single |
| R08-F03 | CD-04 | merged with R10-F04, R11-F19, R03-F16, R01-F31, R12-F07 |
| R08-F04 | CD-19 | single |
| R08-F05 | CF-04 | merged with R10-F02, R05-F16 |
| R08-F06 | RI-08 | merged with R13-F14 |
| R08-F07 | RI-12 | single |
| R08-F08 | RI-21 | merged with R12-F18, R08-F32 |
| R08-F09 | VH-07 | merged with R13-F01 |
| R08-F10 | SS-10 | merged with R00b-F33 |
| R08-F11 | CD-02 | single |
| R08-F12 | RI-20 | single |
| R08-F13 | PI-05 | single |
| R08-F14 | PI-07 | merged with R04-F33 |
| R08-F15 | CF-06 | merged with R05-F11 |
| R08-F16 | CF-18 | single |
| R08-F17 | SI-05 | merged with R00a-F29 |
| R08-F18 | LC-11 | merged with R13-F04 |
| R08-F19 | CR-07 | merged with R00a-F25 |
| R08-F20 | SS-02 | merged with R12-F20 |
| R08-F21 | CF-15 | merged with R05-F31 |
| R08-F22 | VC-04 | merged with R00a-F07, R11-F26 |
| R08-F23 | CF-05 | single |
| R08-F24 | PI-09 | merged with R00b-F19, R04-F19, R07-F30 |
| R08-F25 | RI-02 | merged with R12-F22 |
| R08-F26 | RI-03 | merged with R00a-F14, R06-F03 |
| R08-F27 | PI-02 | merged with R13-F30, R10-F26 |
| R08-F28 | VH-08 | single |
| R08-F29 | CD-06 | single |
| R08-F30 | PI-12 | merged with R03-F19, R04-F45 |
| R08-F31 | CD-22 | merged with R03-F14 |
| R08-F32 | RI-21 | merged with R08-F08, R12-F18 |
| R09-F01 | GD-23 | single |
| R09-F02 | GD-15 | merged with R00d-F33 |
| R09-F03 | LC-01 | merged with R02-F11, R00a-F10 |
| R09-F04 | WL-01 | merged with R00a-F02, R02-F23 |
| R09-F05 | GD-24 | single |
| R09-F06 | WL-08 | single |
| R09-F07 | PP-29 | merged with R00b-F24 |
| R09-F08 | WL-11 | single |
| R09-F09 | WL-12 | merged with R09-F38 |
| R09-F10 | GD-25 | single |
| R09-F11 | WL-09 | single |
| R09-F12 | PI-04 | merged with R00a-F33 |
| R09-F13 | GD-26 | single |
| R09-F14 | WL-14 | single |
| R09-F15 | GD-29 | single |
| R09-F16 | GD-30 | single |
| R09-F17 | GD-28 | single |
| R09-F18 | PP-27 | merged with R09-F36 |
| R09-F19 | WL-18 | single |
| R09-F20 | SD-23 | merged with R02-F26 |
| R09-F21 | WL-17 | single |
| R09-F22 | WL-07 | merged with R00b-F07 |
| R09-F23 | WL-22 | merged with R00b-F12, R02-F32, R13-F15 |
| R09-F24 | WL-10 | single |
| R09-F25 | WL-15 | single |
| R09-F26 | GD-27 | single |
| R09-F27 | WL-16 | single |
| R09-F28 | RI-05 | merged with R01-F01, R00a-F18, R05-F05 |
| R09-F29 | PP-25 | merged with R06-F04 |
| R09-F30 | CF-01 | merged with R10-F07, R02-F01, R05-F24 |
| R09-F31 | CF-14 | single |
| R09-F32 | VC-05 | merged with R02-F34, R13-F31 |
| R09-F33 | WL-13 | single |
| R09-F34 | PP-26 | merged with R00b-F02 |
| R09-F35 | LC-16 | single |
| R09-F36 | PP-27 | merged with R09-F18 |
| R09-F37 | PP-24 | merged with R00b-F15 |
| R09-F38 | WL-12 | merged with R09-F09 |
| R09-F39 | PP-11 | single |
| R09-F40 | CR-09 | merged with R11-F13 |
| R09-F41 | MD-17 | single |
| R09-F42 | LC-18 | single |
| R09-F43 | MD-13 | merged with R13-F23, R13-F27, R13-F33 |
| R09-F44 | WL-19 | single |
| R09-F45 | VH-05 | merged with R02-F22, R00a-F11, R00b-F11 |
| R09-F46 | WL-20 | single |
| R09-F47 | GD-33 | merged with R13-F39 |
| R09-F48 | VC-06 | single |
| R09-F49 | VR-16 | single |
| R09-F50 | WL-05 | single |
| R09-F51 | CR-13 | single |
| R10-F01 | RI-09 | single |
| R10-F02 | CF-04 | merged with R05-F16, R08-F05 |
| R10-F03 | RI-19 | merged with R13-F03, R05-F08 |
| R10-F04 | CD-04 | merged with R08-F03, R11-F19, R03-F16, R01-F31, R12-F07 |
| R10-F05 | RH-05 | single |
| R10-F06 | SI-20 | single |
| R10-F07 | CF-01 | merged with R09-F30, R02-F01, R05-F24 |
| R10-F08 | CF-07 | single |
| R10-F09 | CD-14 | single |
| R10-F10 | SI-19 | single |
| R10-F11 | SS-01 | merged with R05-F15, R00a-F22, R05-F32 |
| R10-F12 | VC-02 | merged with R13-F19 |
| R10-F13 | MD-03 | merged with R13-F24, R02-F05 |
| R10-F14 | LC-13 | single |
| R10-F15 | GD-08 | single |
| R10-F16 | PI-14 | single |
| R10-F17 | VH-09 | single |
| R10-F18 | SI-18 | single |
| R10-F19 | CF-19 | single |
| R10-F20 | LC-22 | merged with R11-F28 |
| R10-F21 | CR-08 | single |
| R10-F22 | CR-11 | merged with R00d-F34 |
| R10-F23 | RI-29 | single |
| R10-F24 | MD-02 | merged with R01-F28, R02-F20, R02-F21 |
| R10-F25 | CF-20 | single |
| R10-F26 | PI-02 | merged with R08-F27, R13-F30 |
| R10-F27 | RI-23 | merged with R11-F02, R11-F27 |
| R11-F01 | RI-16 | merged with R00a-F19, R12-F03 |
| R11-F02 | RI-23 | merged with R11-F27, R10-F27 |
| R11-F03 | RI-17 | single |
| R11-F04 | CD-01 | merged with R01-F10, R03-F07 |
| R11-F05 | PP-15 | merged with R01-F15 |
| R11-F06 | VH-04 | merged with R01-F11 |
| R11-F07 | SS-14 | single |
| R11-F08 | SS-13 | single |
| R11-F09 | GD-21 | single |
| R11-F10 | RI-01 | merged with R00a-F13 |
| R11-F11 | GD-22 | single |
| R11-F12 | CF-02 | merged with R00a-F16, R04-F06 |
| R11-F13 | CR-09 | merged with R09-F40 |
| R11-F14 | SS-15 | merged with R04-F32 |
| R11-F15 | SS-04 | merged with R00a-F32, R01-F52, R03-F09 |
| R11-F16 | EX-01 | merged with R01-F12 |
| R11-F17 | CD-21 | single |
| R11-F18 | SI-10 | single |
| R11-F19 | CD-04 | merged with R08-F03, R10-F04, R03-F16, R01-F31, R12-F07 |
| R11-F20 | MD-09 | merged with R00b-F18 |
| R11-F21 | RI-22 | single |
| R11-F22 | SS-05 | merged with R12-F11, R01-F13, R00a-F08 |
| R11-F23 | CD-13 | merged with R01-F18 |
| R11-F24 | PI-13 | single |
| R11-F25 | CD-12 | merged with R00a-F39, R01-F33, R03-F39 |
| R11-F26 | VC-04 | merged with R00a-F07, R08-F22 |
| R11-F27 | RI-23 | merged with R11-F02, R10-F27 |
| R11-F28 | LC-22 | merged with R10-F20 |
| R11-F29 | LC-21 | single |
| R11-F30 | CR-02 | merged with R00a-F24 |
| R11-F31 | GD-19 | single |
| R12-F01 | SI-17 | single |
| R12-F02 | CC-04 | single |
| R12-F03 | RI-16 | merged with R00a-F19, R11-F01 |
| R12-F04 | RI-18 | merged with R00a-F20, R05-F06 |
| R12-F05 | RI-28 | single |
| R12-F06 | GD-16 | merged with R01-F44 |
| R12-F07 | CD-04 | merged with R08-F03, R10-F04, R11-F19, R03-F16, R01-F31 |
| R12-F08 | SS-09 | single |
| R12-F09 | SS-17 | merged with R01-F25 |
| R12-F10 | SS-08 | single |
| R12-F11 | SS-05 | merged with R01-F13, R11-F22, R00a-F08 |
| R12-F12 | CF-09 | merged with R01-F50 |
| R12-F13 | CF-03 | single |
| R12-F14 | MD-12 | merged with R12-F15 |
| R12-F15 | MD-12 | merged with R12-F14 |
| R12-F16 | SS-18 | merged with R01-F53 |
| R12-F17 | PP-14 | merged with R01-F04 |
| R12-F18 | RI-21 | merged with R08-F08, R08-F32 |
| R12-F19 | VH-11 | merged with R12-F27 |
| R12-F20 | SS-02 | merged with R08-F20 |
| R12-F21 | VH-03 | merged with R13-F37 |
| R12-F22 | RI-02 | merged with R08-F25 |
| R12-F23 | LC-04 | merged with R05-F04 |
| R12-F24 | CD-20 | single |
| R12-F25 | VC-07 | merged with R06-F15 |
| R12-F26 | VC-16 | single |
| R12-F27 | VH-11 | merged with R12-F19 |
| R12-F28 | VC-15 | single |
| R12-F29 | VC-14 | single |
| R12-F30 | RI-30 | single |
| R12-F31 | VR-03 | merged with R00c-F05 |
| R12-F32 | WL-28 | merged with R03-F08 |
| R12-F33 | VC-09 | merged with R03-F06, R02-F14 |
| R12-F34 | MD-11 | merged with R01-F21 |
| R12-F35 | WL-02 | single |
| R12-F36 | LC-23 | merged with R05-F20 |
| R12-F37 | GD-17 | single |
| R13-F01 | VH-07 | merged with R08-F09 |
| R13-F02 | SI-03 | merged with R00a-F15 |
| R13-F03 | RI-19 | merged with R10-F03, R05-F08 |
| R13-F04 | LC-11 | merged with R08-F18 |
| R13-F05 | PI-15 | single |
| R13-F06 | LC-07 | merged with R03-F34 |
| R13-F07 | VH-01 | merged with R00a-F05 |
| R13-F08 | CR-05 | merged with R00b-F03, R03-F35 |
| R13-F09 | SS-07 | single |
| R13-F10 | VC-03 | merged with R01-F06, R01-F34 |
| R13-F11 | CF-08 | merged with R00b-F06, R13-F12 |
| R13-F12 | CF-08 | merged with R00b-F06, R13-F11 |
| R13-F13 | MD-01 | merged with R01-F26, R03-F22, R02-F06 |
| R13-F14 | RI-08 | merged with R08-F06 |
| R13-F15 | WL-22 | merged with R00b-F12, R02-F32, R09-F23 |
| R13-F16 | SI-04 | single |
| R13-F17 | WL-21 | merged with R00b-F14, R02-F27 |
| R13-F18 | SS-20 | single |
| R13-F19 | VC-02 | merged with R10-F12 |
| R13-F20 | CD-08 | merged with R00a-F31, R13-F25 |
| R13-F21 | PP-07 | single |
| R13-F22 | PP-09 | merged with R01-F09 |
| R13-F23 | MD-13 | merged with R13-F27, R13-F33, R09-F43 |
| R13-F24 | MD-03 | merged with R10-F13, R02-F05 |
| R13-F25 | CD-08 | merged with R00a-F31, R13-F20 |
| R13-F26 | PP-08 | single |
| R13-F27 | MD-13 | merged with R13-F23, R13-F33, R09-F43 |
| R13-F28 | PP-01 | merged with R00a-F34 |
| R13-F29 | LC-08 | merged with R02-F24 |
| R13-F30 | PI-02 | merged with R08-F27, R10-F26 |
| R13-F31 | VC-05 | merged with R02-F34, R09-F32 |
| R13-F32 | CR-04 | single |
| R13-F33 | MD-13 | merged with R13-F23, R13-F27, R09-F43 |
| R13-F34 | CR-06 | merged with R05-F14 |
| R13-F35 | MD-10 | merged with R02-F13 |
| R13-F36 | CD-26 | single |
| R13-F37 | VH-03 | merged with R12-F21 |
| R13-F38 | PP-06 | merged with R02-F30 |
| R13-F39 | GD-33 | merged with R09-F47 |

## 3. Progress log

| Step | State |
| --- | --- |
| 1. all-index read, topic plan and draft mapping | done 2026-10-21 |
| 2. value-contrast.md VC-01..VC-17 (17 findings, 31 extract IDs) | done |
| 3. visual-hierarchy.md VH-01..VH-11 (11 findings, 20 extract IDs) | done |
| 4. shape-silhouette.md SS-01..SS-20 | done |
| 5. character-design.md CD-01..CD-29 | done |
| 6. exaggeration.md EX-01..EX-10, weight-timing.md WT-01..WT-25, rhythm.md RH-01..RH-05; R07-F05 moved to CC (timing contract with R04-F07), R07-F13 to SD | done |
| 7. light-colour.md LC-01..LC-25; R01-F22 to SI, R06-F16 to VR | done |
| 8. composition-focus.md CF-01..CF-20; R00b-F07 to WL | done |
| 9. materials-detail.md MD-01..MD-17; R03-F02 to RI, R02-F29 to PP, R09-F19 to WL | done |
| 10. world-level-readability.md WL-01..WL-28; R06-F05 and R06-F06 to VR; R01-F36 to RI; R03-F45, R03-F11 to CR | done |
| 11. vfx-reads-timing.md VR-01..VR-18 | done |
| 12. sound.md SD-01..SD-33 | done |
| 13. ui-ux.md UI-01..UI-16 | done |
| 14. game-design-fun.md GD-01..GD-33; R09-F02 merged here (was PI draft) | done |
| 15. references-ideation.md RI-01..RI-30 | done |
| 16. critique-feedback.md CR-01..CR-16; R01-F46 to CC | done |
| 17. process-iteration.md PI-01..PI-15 (added topic) | done |
| 18. pipeline-production.md PP-01..PP-33 (added topic) | done |
| 19. cross-craft.md CC-01..CC-06 (added topic) | done |
| 20. style-identity.md SI-01..SI-20; all 21 topic files written | done |
| 21. universal-principles.md UP-01..UP-18 (master, J018-D1); every "rests on" ID exists | done |
| 22. README.md (sources, topics, conventions, full index generated from the topic files) | done |
| 23. Final check by script: 649 mapping rows, 649 unique IDs, 0 dropped, every library ID in the mapping exists, every finding's sources equal its mapping rows, all fields present, roles in vocabulary, all cited docs paths exist | done 2026-10-21 |

## 4. Result summary

| Item | Value |
| --- | --- |
| Extract findings mapped | 649 of 649 |
| Dropped | 0 (every extract finding had a teachable point; weak ones were merged into stronger findings) |
| Library findings | 427 in 21 topic files (VC 17, VH 11, SS 20, CD 29, EX 10, WT 25, RH 5, LC 25, CF 20, MD 17, WL 28, VR 18, SD 33, UI 16, GD 33, RI 30, CR 16, SI 20, PI 15, PP 33, CC 6) |
| Universal principles | 18 (UP-01..UP-18) |
| Added topics | process-iteration (PI), pipeline-production (PP), cross-craft (CC) |
