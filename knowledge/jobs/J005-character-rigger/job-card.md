---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent character-rigger, then animator)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J005 — Rig workflow + character-rigger agent

| Field | Value |
| --- | --- |
| Job id | J005-character-rigger |
| Size | L (new role, shared three-role workflow, 3 skill books, two papers to extract and fact-check, first real test in Blender + Studio) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | step 1 approved and G1 approved 2026-10-21 (J005-D1..D5). Step 2 (extract + fact-check) running |
| Next job | J006-animator (own job card, gates; starts after J005 G3) |

## Owner's words (2026-10-20, excerpts)
- "The most important part is the workflow between the agents. Each agent does what it knows best."
- "The rigger turns that into a joint and bone plan, and says which parts must be separate pieces, where the cuts go and why."
- "The modeler does the cutting, seam clean-up and any re-modelling ... It may push back with a better cut or a better way to build the part."
- "The rigger checks the modeler's result, rigs it and tests it. Problems go back to the modeler as one exact note."
- "This loop matters most for Tripo models, which arrive as one merged mesh."
- "First design the workflow and the shared hand-off ... Show it to me before building either agent."
- "Read BOTH papers for BOTH agents ... Use them as strong evidence, but not as gospel. Check claims that matter, especially numbers, Blender facts and Roblox facts, and drop what you cannot back up."
- "Model: Opus, high effort for both agents."

## Goal
A `character-rigger` agent that rigs characters, creatures, pets, weapons, vehicles and moving props in Blender (Python + Blender MCP) for Roblox; plans the rig with the animator and modeler from the start; tells the modeler exactly what to separate and why; decides per region between clean separate parts and skinning for merged Tripo meshes (and when Tripo's own segmentation and auto-rig are good enough); and tests every rig in Blender and Roblox before the animator gets it.

## Material received (outside git)
| File | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\uterd\NewGame\Roblox_Character_Rigger_Research.txt` | Rig quality, Roblox rigid / skinned / mixed, requirements sheet, merged AI mesh → rig (cut, skin, decision table), Tripo segmentation and auto-rig, weights, non-humans, faces, controls and Python, export / import, tests, 16-stage method, 20 don'ts, dated sources R1-R13, T1-T6, B0-B10 | 849 lines, 100 KB | high: VERIFIED / EXPERIENCE / OPINION tags, dated sources; Tripo and Blender 5.2 facts are after the model cutoff → web check |
| `C:\Users\Firew\Downloads\Animator_Research_Paper.txt` | Body inventory and motion profile, rig manifest, Blender slots / channelbags, export, Roblox runtime (importer, AnimationConstraint, priority, replication, throttling, track cap), AI motion tools, cross-craft hand-off, review checklist, 15-gate process, 26-action timing library | 1,300 lines, 180 KB | high, same tags; read for rig needs here, fully in J006 |
| DestructionSimulator `rules/character-rigs.md`, `knowledge/reference/character-part-rigging.md`, D-160 / D-185 / D-186 / F-020, `.claude/agents/animator.md`, `.agents/skills/animation/` (read-only) | First-game owner experience with Tripo rigs (segmented buried-root pieces; skinned limbs webbed and wrinkled; neck mesh creased; face-delete holes) and the earlier animator | 38 + 194 + 81 lines | medium-high: owner decisions with owner's words; numbers in the rigging note are UNVERIFIED starting values |

## Scope
| In | Out |
| --- | --- |
| Shared workflow skill `rig-pipeline` + templates (rig sheet, fix note) | Building the modeler agent (planned hand-off brief + roster row only) |
| Reference notes in `knowledge/reference/rigging/` + fact-check table (Roblox, Blender, Tripo) | Animator skills and role (J006) |
| Skills `rigging-design`, `rigging-craft` (brief.md) | Game code, runtime animation scripts |
| Blender check script for rig audits (`tools/rig/`, pure parts tested offline) | New research beyond checking the papers' claims |
| Role file `character-rigger`, eval briefs, first real test (G2) | Changing other skills beyond pointers |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×5 (rig paper ×2, animation paper ×2 shared with J006, first-game sources ×1) | Sonnet | high (J002-D2, J003-D2 precedent) | dense notes per part |
| fact-checkers ×3 (Roblox, Blender via MCP docs + web, Tripo via web) | Sonnet | high | fact-check table: claim, source, checked against, verdict |
| lead (merge, skills, role, evals, script) | Opus | high | 3 skills, templates, role, evals, roster |
| character-rigger (new, first test) | Opus | high (owner 2026-10-20) | G2 rig + test record |
| modeler stand-in for the test (digest item 2) | Opus | high | geometry for the test asset |
| grader (evals, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents in waves of 3 (company limit). Lead writes the skills (needs both papers and the first-game history together). The test runs the real loop: rigger S2 → stand-in modeler S3 → rigger S4-S5 in Blender (MCP) and Studio (MCP), with real fix notes.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 5 extract + 3 fact-check + 1 rigger test + 1 modeler stand-in + 1 grader = 11 | |
| Models / effort | Sonnet high ×9; Opus high ×2 + lead | |

## Acceptance checks
- [ ] Every number, Blender fact, Roblox fact and Tripo fact in a skill has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-OPINION / dropped); dropped claims listed with the reason.
- [ ] Evidence tags kept; no invented budgets, angles, loop counts or bone caps (rigging paper "Do not do" 4).
- [ ] Nothing specific to DestructionSimulator in kit files (grep: King, golem, villain, D-1xx, D-2xx = 0 hits outside source tables).
- [ ] `rig-pipeline` covers S0-S8, the rig sheet, the fix note, the Tripo route table, and the modeler hand-off; the rigger role names its stages.
- [ ] Rig audit script: influence count ≤ 4, Root weights 0, unweighted deform vertices, protected-region displacement, watertight, triangles; offline tests pass.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and the gate PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.
- [ ] G2: one merged Tripo character goes through S2-S5 for real; one fix-note round is exercised; rig test record with Blender and Roblox evidence; shown next to the first game's final rig.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| Step 1 workflow review | 2026-10-21 | "All right." |
| G1 brief | 2026-10-21 | "All right. And when you do this, set all the Sonnet models to high" |
| G2 first real test | | |
| G3 final approval | | |
