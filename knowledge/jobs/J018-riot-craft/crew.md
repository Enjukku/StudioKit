---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J018-riot-craft
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Crew: J018-riot-craft

All J018 stages run as workflow calls (no agent ids; sideways work goes through files). One row per call.

| Stage | Workflow run | Agents | Model · effort | Started | Status | Writes |
| --- | --- | --- | --- | --- | --- | --- |
| 1a wave 1 | wf_a1ddb5fc-07d | readers R00a, R00b, R00c, R00d, R01-R05 (9) | opus · medium | 2026-10-21 | done: 369 findings, 1.10 M tokens | `extracts/<key>.md` |
| 1a wave 2 | wf_6580b0f7-656 | readers R06-R13 (8) | opus · medium | 2026-10-21 | done: 280 findings, 0.98 M tokens | `extracts/<key>.md` |
| 1b | wf_f297505c-22c | synthesizer (1) | opus · high | 2026-10-21 | done: 427 findings, UP-01..18, 0.77 M tokens | `knowledge/reference/craft/riot/`, `synth/merge-plan.md` |
| 1c | wf_9be64666-08b | DestructionSimulator cross-checker (1) | opus · high (J018-D4) | 2026-10-21 | done: 16 findings + UP-19, UP-20, 32 sharpened checks, 0.50 M tokens | library additions + cross-check table in `knowledge/reference/craft/riot/` |
| 2-3 wave 1 | wf_ab890fff-a1c | makers + reviewers + repairs: animator, modeler, game-designer (18 agents) | opus · high | 2026-10-22 | done 5.85 M tokens: animator pass (rev3), game-designer pass (rev3), modeler fix-first after 2 repairs | the roles' books, `coverage/<role>.md`, `proposals/<role>.md`, `reviews/<role>-rev<N>-reviewer.md` |
| 2-3 wave 1 modeler round 3 | wf_defb0d44-38e | lead decision: repair round 3 + review round 4 | opus · high | 2026-10-22 | done 0.42 M tokens: modeler pass (rev4); recommendations F4, F5 of rev3 open (G3 note) | modeler books |

Pre-J018 revision of every book (the pilot's "old books"): `df13ff4`.
