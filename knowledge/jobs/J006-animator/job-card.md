---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent animator)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Job card: J006 Build the animator agent

## The owner's words (verbatim, first)
> Build the animator role (J006), universal, built congruently with the character-rigger (rig-pipeline). The material is [path to the research paper] and the Riot extracts. Animation is open-ended: base it on principles, not one fixed recipe. "C:\Users\Firew\Downloads\Animator_Research_Paper (2).txt""C:\Users\Firew\Downloads\charcter and gameplay animations ep4.txt"

Second message (2026-10-21): the full owner brief, kept word for word in `brief.md` (scope: everything that moves - characters, creatures, pets, held items, props and mechanisms, vehicles and mounts, buildings, ambient loops at scale; technique chosen per object; principles and worked examples, not one recipe). Then: "Use what you learn from both documents to go ahead and create our workflow animator."

Earlier owner words that bind this role: "Opus for animating ... on high" (2026-10-20, roster). "Read BOTH papers for BOTH agents ... Use them as strong evidence, but not as gospel. Check claims that matter, especially numbers, Blender facts and Roblox facts, and drop what you cannot back up." (J005, 2026-10-20). "Always be light check." (J005-D8).

| Field | Value |
| --- | --- |
| Job id | J006-animator (number reserved since J005) |
| Title | Build the animator agent |
| Size | L (new role, 2 skill books, a 2,056-line paper and a 1,100-line transcript, Roblox and Blender facts after the model cutoff, a real test in Blender + Studio) |
| Type (recipe) | other: `/build-agent` (kit role build, not a game job) |
| Job lead (agent) | lead (orchestrator) |
| Direction leads | none (one craft; the rig-pipeline workflow is already owner-approved, J005-D1) |
| Integrator | lead |
| Studio place (`studio_id`) | the rig test place "Place2" (J005-D6); id read with `list_roblox_studios` at G2 |
| Code file owners | none (no game code); `tools/anim/` owned by the tool builder if digest item 4 is approved |
| Linked jobs | J005 (closed): the animator fills the `rig-pipeline` S1, K2, S6, S7 keys; no shared interface changes |
| Status | closed 2026-10-21 (J006-D2): animator in the kit; G2 teddy test stopped before it returned, G3 not run (owner: commit now, test later in real games) |

## Goal and feeling
One `animator` agent that makes players read every action at a glance, believe its weight and feel who does it. It works from principles (weight, timing, spacing, silhouette, character, gameplay read), not one recipe: each choice is made from the character, the camera, the gameplay window and the rig, and the reason is written. It works inside `rig-pipeline` exactly where the rigger expects it (S1 motion needs, K2 plan sign-off, S6 rig acceptance, S7 animate and export, the timing list for VFX, sound and UI), keys and exports clips in Blender (Python + Blender MCP), imports and plays them in Roblox, and checks its own clips light-first (numbers for every clip, images only on a fail plus a few key frames).

## References (material)
| Source | What | Size | State in the kit | Trust |
| --- | --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Animator_Research_Paper (2).txt` (byte-identical to `Animator_Research_Paper.txt`, checked with `cmp`) | 15 operating rules; great animation and the twelve principles as conditional tools; the body and species motion families; motion profile; game vs film timing; stylization; sets and loops; combat timing contract; face and secondary; cutscenes; Blender 5.x Python/MCP workflow; Roblox runtime and phone cost; AI motion tools; hand-offs; review checklist; 15 gates; 26-action timing library; source register | 2,056 lines, 180 KB | already extracted in J005 (`knowledge/reference/animation/01-*.md`, `02-*.md`, complete per section, with claim table CL and limits table LM). Partly fact-checked in J005 (Roblox rows in `knowledge/reference/rigging/fact-check-roblox.md`, Blender rows in `fact-check-blender.md`); AI-tool, science and many runtime claims not yet checked | high: evidence tags on every claim; it says it watched no video and ran no benchmark (AP:79, AP:1148) |
| `C:\Users\Firew\Downloads\charcter and gameplay animations ep4.txt` | Riot senior animator (Lana Bachynski): a K/DA Akali weight shift between two key poses in Maya, about 3 h, with her reasons | 1,100 lines, 69 KB | already read line by line in J016: `knowledge/jobs/J016-orchestration/riot/E-anim-vfx-sound.md` §A (A1-A10) and the per-role row in `riot-extracts.md` §4 | high for principles (an expert's stated reasons); low for numbers (a compressed live demo, no frame counts) |
| "The Riot extracts": `knowledge/jobs/J016-orchestration/riot-extracts.md` + `riot/A-core.md` §3.5 (Riot core series, character animation R:2896-3420: Garen pose, Teemo ball bounce, state machines, 3-5 tries) | Riot practice across 14 talks; the animator row and cross-craft timing spine | 97 + 651 lines | in a job folder, not yet in `knowledge/reference/animation/` | high for principles and order of work; no sign-off chain (riot-extracts.md:13) |
| First game, read-only: `DestructionSimulator/.claude/agents/animator.md`, `.agents/skills/animation/` | The earlier animator: animation cards, state tables, checklist | 30 + 89 lines | not read into the kit yet | medium: owner-used, game-specific parts to strip |
| Kit: `rig-pipeline`, `rigging-design` (`references/motion-needs.md`), `rigging-craft`, `templates/rig/`, `tools/rig/roblox_fbx.py`, the J005 teddy rig (`output/rigs/teddy/s5/`, Blender side PASS, control manifest, Roblox import not run) | The workflow and the rig the animator receives | — | owner-approved (J005-D1, D7-D10) | high |

## Scope
| In | Out |
| --- | --- |
| Move the Riot animation lessons and the first-game animator lessons into `knowledge/reference/animation/03-*.md` (paraphrased, universal) | New research beyond checking the material's claims |
| Fact-check the animation claims J005 did not check (Roblox runtime, Blender keying and export, AI motion tools, science and industry numbers) | Game code (animation controllers, state machine scripts): engineering builds them from the animator's set spec |
| Skills `animation-design` (principles, how to read what must move, technique choice per object, feel and read, sets and state planning, timing list format, review) and `animation-craft` (Blender keying by Python/MCP, export, Roblox import, Animator playback, priorities and blending, markers, code-driven motion specs, ambient loops at scale, light self-check); a worked example per kind: characters/creatures/pets, held items, props and mechanisms, vehicles and mounts, buildings, ambient decoration | Rigs, cuts and geometry (rigger, modeler) |
| Docs-map rows for the animator in `knowledge/reference/roblox/docs-map.md` (animation, Bones, Motor6D, AnimationConstraint, TweenService, Animator and priorities, constraints, flipbooks, at least) | Cutscene camera motion (film-director); UI motion (ui-ux-designer); the code of code-driven motion (a builder writes it from the animator's motion spec) |
| Templates in `templates/anim/` that fit the rig sheet: motion profile (S1), clip card, set and transition table, timing list | Cutscene direction (film-director); effects and sounds (VFX, sound) |
| Role file `animator` with a `tools:` line (Blender + Studio, J017 O8); roster row; pointer edits where kit files say "planned (J006)" | Changing the rig-pipeline stages or the rigger's skills beyond pointer lines |
| Optional small clip-check script (digest item 4) | |
| Eval briefs + hidden cases; first real test on the teddy rig (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractor ×1 (Riot ep4 + core animation + first-game animator → note 03; gap read of ep4 against extract §A) | Sonnet | high (J005-D4 precedent) | `knowledge/reference/animation/03-riot-first-game.md` |
| fact-checker ×2 (A: Roblox runtime + Blender rows with no J005 verdict, mirror first; B: AI motion tools + science/industry numbers, web, dated) | Sonnet | high | `knowledge/reference/animation/fact-check-*.md` |
| tool builder (only if item 4 = a) | Opus | medium | `tools/anim/` + offline tests |
| lead (skills, templates, role, evals, pointers) | Opus | high | 2 skills, templates, role, evals |
| animator (new, G2 test) | Opus | high | G2 clips + self-check record |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents by hand, max 3 at a time. Wave 1: extractor + 2 fact-checkers in parallel. Then the lead writes the skills (it needs all sources together). Tool builder after the skills fix what the check measures. G2: the new animator runs as its own agent type on the teddy rig with Blender MCP and Studio MCP.

## Budget (tokens)
No earlier build job recorded tokens, so these are estimates.

| Stage | Estimate | Actual |
| --- | --- | --- |
| extract + fact-check (3 Sonnet) | 0.6 M | |
| skills, templates, role, evals (lead) | 0.5 M | |
| tool (if approved) | 0.2 M | |
| G2 test + grader | 0.7 M | |
| total | 2.0 M | |

## Acceptance checks
- [ ] Principles, not a recipe: every timing, spacing or pose rule in the skills says when it applies and what to read to choose; the 26-action timing library is labelled "starting ranges to test", never targets; no clip has a required frame count unless a gameplay window fixes it.
- [ ] Every number, Blender fact and Roblox fact in a skill has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-label / dropped); dropped claims listed with the reason.
- [ ] Congruent with `rig-pipeline`: the animator writes only its own sheet keys (§B, K2 sign-off, §H), uses `templates/rig/fix-note.md` for rig notes, follows the §4a light check budget, owns the §5 timing list in the format `animation-design` defines, and never works around a missing degree of freedom.
- [ ] Gameplay windows come from the gameplay owner; markers are presentation, never damage authority.
- [ ] Nothing game-specific in kit files (grep for first-game names = 0 outside source tables).
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.
- [ ] G2: S6 rig acceptance on the teddy, then at least an idle loop, a walk loop and one action with a timing list, exported and imported to Roblox and played on the intended Animator (import click by the owner, J005-D6); shown next to the material's reference (the Riot weight-shift principles and the paper's filled profile).

## Gates
| Gate | Date | Revision approved | Owner's words |
| --- | --- | --- | --- |
| G1 brief | 2026-10-21 | job-card.md + brief.md 2026-10-21 | "Use what you learn from both documents to go ahead and create our workflow animator." (J006-D1; digest defaults apply) |
| G2 first real test | 2026-10-21 | not run (J006-T06 stopped) | "Okay, don't do the testing right now." (J006-D2) |
| G3 final | 2026-10-21 | build as committed | "If you're done, just go ahead and commit and push." (J006-D2) |

## Close-out
Metrics in `evidence.md` §4. Filed into the vault (`orchestration` skill §9): [ ] decisions [ ] precedents [ ] vocabulary [ ] systems [ ] tried-and-failed [ ] taste log [ ] catalogs [ ] lesson drafts [ ] removed from `knowledge/jobs/active.md`
