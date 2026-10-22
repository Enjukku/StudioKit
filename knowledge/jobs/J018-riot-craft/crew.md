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
| 2-3 wave 2 (brief v2) | wf_65d4684d-d9b | makers + reviewers + repairs: character-rigger, art-director, environment-designer, film-director, vfx-designer, sound-designer, ui-ux-designer, marketing, progression-designer | opus · high | 2026-10-22 | done 17.59 M tokens (52 agents): pass art-director, ui-ux-designer, progression-designer; 6 roles fix-first with one blocking measuring-recipe finding each | the roles' books (ownership: `stage2-brief-v2.md`) |
| 2-3 wave 2 round 3-4 | wf_2fe45f27-9e5 | lead decision: focused repair + review for 6 roles; one shared flash counter | opus · high | 2026-10-22 | done 2.12 M tokens: environment-designer, marketing pass; film-director fixed in the shared counter; vfx, rigger, sound one more edge case each |
| 2-3 wave 2 final | wf_974de974-390 | lead decision: last repair vfx-designer, character-rigger, sound-designer (screening aids with known limits); lead verifies | opus · high | 2026-10-22 | done 0.63 M tokens; lead verified by script (fixed list) and aligned film, marketing and animator books with the shared counter and sync rule | their books |
| 2-3 wave 3 (brief v3) | wf_76213347-ca7 | makers + reviewers + repairs: live-ops-designer, architect, feature-builder (engineering-craft, ui-basics), qa-lead, reviewer, reference-images, orchestration, level-design | opus · high | 2026-10-22 | done 13.09 M tokens (44 agents): 6 pass; reviewer and level-design one text-only blocker each, closed by a final repair (wf_dff63473-240, 0.23 M) | the books in `stage2-brief-v2.md` ownership table |

Pre-J018 revision of every book (the pilot's "old books"): `df13ff4`.
