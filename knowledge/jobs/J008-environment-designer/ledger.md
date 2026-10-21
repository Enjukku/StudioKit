---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J008
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Ledger: J008-environment-designer

| id | from | to | ask | inside | status | hops | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J008-T01 | lead | extractor (Sonnet high) | paper lines 1-255 (rules, cases, guidance, scale, lighting, atmosphere) → notes | yes | done | 1 | knowledge/reference/environment/01-place-guidance-scale-light.md | 2026-10-21 |
| J008-T02 | lead | extractor (Sonnet high) | paper lines 256-434 (ambience, ambient life, dressing, terrain, art cohesion) → notes | yes | done | 1 | knowledge/reference/environment/02-ambience-life-dressing-terrain.md | 2026-10-21 |
| J008-T03 | lead | extractor (Sonnet high) | paper lines 435-762 (kits, Blender↔Studio, performance, review, process, defects, don'ts, open questions) + source register 763-1469 → notes | yes | done | 1 | knowledge/reference/environment/03-pipeline-performance-review.md, 00-source-register.md | 2026-10-21 |
| J008-T04 | lead | extractor (Sonnet high) | DestructionSimulator stage sources (read-only) → universal lessons | yes | done | 1 | knowledge/reference/environment/04-first-game-stages.md | 2026-10-21 |
| J008-T05 | lead | fact-checker (Sonnet high) | Roblox lighting, atmosphere, sky, post effects, terrain claims | yes | done | 1 | knowledge/reference/environment/fact-check-lighting.md | 2026-10-21 |
| J008-T06 | lead | fact-checker (Sonnet high) | Roblox audio and ambience claims | yes | done | 1 | knowledge/reference/environment/fact-check-audio.md | 2026-10-21 |
| J008-T07 | lead | fact-checker (Sonnet high) | performance, streaming, scale, Blender→Studio import claims | yes | done | 1 | knowledge/reference/environment/fact-check-performance-import.md | 2026-10-21 |
| J008-T08 | lead | tool builder (Opus medium) | scene audit + ambience-map check + offline tests | yes | done (incl. T08b: multi-volume zones, global audio) | 1 | tools/env/, tools/tests/test_env_*.py | 2026-10-21 |
| J008-T09 | lead | researcher (Sonnet high) | Roblox look-dev from the docs (lighting, atmosphere/haze, sky/skybox, clouds, post, local lights, materials/water, time of day, zone/state changes, Roblox showcase case studies) → craft reference | yes (J008-D7) | done | 1 | knowledge/reference/environment/05-roblox-look-dev.md | 2026-10-21 |
| J008-T10 | lead | environment-designer (Opus high) | hidden eval: answer hidden-eval-prompts.md H1-H8 from the skills only | yes | done | 1 | knowledge/jobs/J008-environment-designer/hidden-answers.md | 2026-10-21 |
| J008-T11 | lead | grader (Sonnet high) | grade hidden-answers.md against hidden-cases.md (H1-H3) and paper DF01-DF05 (H4-H8) | yes | done (6/8; H1-H3 clean signal 1/3; H4-H8 lookup-assisted) | 1 | knowledge/jobs/J008-environment-designer/grades-hidden.md | 2026-10-21 |
