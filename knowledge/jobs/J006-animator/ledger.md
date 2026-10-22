---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J006-animator
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Ledger: J006-animator

| id | from | to | ask | inside | stage | status | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J006-T01 | lead | extractor (Sonnet high) | Riot ep4 + core animation + first-game animator → `knowledge/reference/animation/03-*.md` | yes | build | done | knowledge/reference/animation/03-riot-first-game.md (359 lines) | 2026-10-21 |
| J006-T02 | lead | fact-checker A (Sonnet high, researcher) | Roblox runtime animation claims with no J005 verdict | yes | build | done | knowledge/reference/animation/fact-check-roblox-runtime.md (RA01-RA47) | 2026-10-21 |
| J006-T03 | lead | fact-checker B (Sonnet high, researcher) | technique and scale facts (TweenService, CFrame, constraints, flipbooks, wind, many copies) + docs-map rows | yes | build | done | knowledge/reference/animation/fact-check-techniques.md (84 rows, TC01-TC30, SD01-SD12) | 2026-10-21 |
| J006-T04 | lead | fact-checker C (Sonnet high, researcher) | Blender animation claims with no J005 verdict + AI motion tools + science numbers | yes | build | done (AI motion tools and science numbers left out: the skills state no tool versions; the paper's acceptance gate is kept as OPINION) | knowledge/reference/animation/fact-check-blender-keying.md (KB01-KB26, run on 5.1.2) | 2026-10-21 |
| J006-T05 | lead | tool builder (Opus medium) | `tools/anim/clip_check.py` + `tools/tests/test_clip_check.py` | yes | build | done (20 tests; Blender layer run on 5.1.2) | tools/anim/clip_check.py |
| J006-T06 | lead | animator (Opus high) | G2 teddy: `T06-g2-brief.md` | yes | proof | cancelled (owner J006-D2: no testing now) | partial work in output/anim/teddy/ (gitignored), not reviewed |
