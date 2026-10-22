---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 wave 1 hand-backs and reviews (animator, modeler, game-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-22

# Stage 2 brief v2: what wave 1 taught, and what changes for waves 2 and 3

J018-D3: no blind test; the lead reads wave 1 and fixes the brief before the other roles run. Wave 1 result: animator pass after 2 repair rounds; game-designer pass after 2; modeler fix-first after 2, then one lead-decided repair round 3 (three measuring commands gave wrong numbers on real inputs). The reviewers judged all three rebuilt agents to make clearly better work than the old books.

## Causes found in wave 1 (from the agents' `lesson` fields and the reviews)
| # | Cause | Layer | Seen in | Brief change (v2 rule) |
| --- | --- | --- | --- | --- |
| 1 | Self-review lines written for senses the agent does not have ("a fresh viewer names it", "pick between timing takes" while the agent sees stills only) and new option or take stages with no image budget, against the light-check rule (J005-D8) | brief | animator rev1 F3 | V1 |
| 2 | Checks named a tool mode that does not exist, or a mode that fails or gives wrong numbers on the real input (in-scene Studio captures cannot be masked; HSV saturation marks near-black pixels; whole-frame resize shrinks the model) | brief, tools | animator, modeler rev1-rev3 | V2, V3 |
| 3 | A library `apply` line copied into a book contradicted a binding shared skill (paid random odds "static, behind Details" vs platform-policy rules) | library, brief | game-designer rev1 F1 | V4; library GD-35 fixed by the lead |
| 4 | Coverage rows written from a keyword; checkable findings landed as standards only, found one review round at a time | maker self-check | all three | V5 |
| 5 | Worked examples not re-read after a rule they use was repaired | maker self-check | animator rev2 | V5 |
| 6 | One rule copied into 6-10 places, which will drift | maker | animator rev3 | V6 |
| 7 | SKILL.md grew so steps and self-check fell outside the part that survives compaction (first 5,000 tokens) | maker | animator rev1 F6 | V7 |
| 8 | Design-side roles got craft advice they cannot carry out; the useful form was templates they fill and review checklists run on named captures | brief | game-designer lesson | V8 |
| 9 | Windows text-mode writes turned LF files into CRLF; scratch files from parallel makers collided | tooling | modeler, animator lessons | V9 |

## v2 rules added to the maker brief (and checked by the reviewer)
- **V1 Input and budget per check.** Every self-review line names its input: sample numbers, at most N key frames as stills, Studio MCP captures, a device capture, or a partner or the owner at a named check-in. The agent sees stills: feel at normal speed is judged by the owner on a playable preview at the gate. Every option, take or bracket stage states its image budget under the light-check rule (numbers for every case, images only on failure and for a few key cases).
- **V2 Real tool modes only.** A book names only modes listed in `tool-modes.md` (or the tool's own docstring). A measure the tools lack is a manual check plus a proposal row for the tool. No long code in SKILL tables; short commands live in `references/`.
- **V3 Run every command once on the real input type.** Before a check names a command or tool mode, run it on a synthetic sample of the input the agent will really give it (flat-background render, black-fill, full game-camera frame with a small subject, in-scene capture with sky and ground, a sampled clip JSON): it runs, writes every file the check names, and gives the right answer. Ask what makes it give a wrong number with no error. Record each run in the coverage file.
- **V4 Binding skills win.** Before a library line about money, paid random items, ads, chat, player data, saves, remotes or younger players lands, diff it against the binding shared skill (`platform-policy/references/rules.md`, `data-saving`, `networking-security`). Where they differ, the shared skill wins and the maker adds a proposal row for the library (the lead fixes the master first).
- **V5 Prove coverage before hand-back.** Script a pass over the coverage table: every row whose library finding has a runnable `check:` names the self-review line that carries it; open every landed-in location and confirm the rule and its check are there; re-read every worked example that uses a rule you changed.
- **V6 One rule, one place.** A rule lives in one place; other places point to it.
- **V7 Compaction.** Each SKILL.md keeps its steps, rules and self-check in roughly the first 5,000 tokens (about 18 KB); depth goes to `references/`. If the "Core principles for this craft" section falls later, the skill's first section says to re-read it after a compaction.
- **V8 Design and engineering roles.** Turn craft findings into what the role owns: the sheets and templates it fills, the briefs it writes for crafts (what to ask each craft for, and when), the review checklists it runs on named captures or tests. No craft advice the role cannot carry out.
- **V9 Files.** Write with LF line endings (`open(p, 'w', encoding='utf-8', newline='')`); scratch files carry the role name.
- **V10 Partner consistency.** Read the rebuilt books of your partner roles from earlier waves (read-only) and keep hand-offs consistent: the same event and marker names, the same sync rule (sound 0 to about 40 ms after the contact frame, never more than one frame early), the attempt cue at once and the big layer on the confirmed outcome, the same timing-list fields. A conflict is a proposal row, not a silent change.
- **V11 Proposals from earlier waves.** Each maker gets the proposal rows other roles wrote against its books; it adopts what is right (and says so in the coverage file) or declines with a reason.

## Book ownership for waves 2 and 3 (no two makers edit the same file)
| Wave | Role or shared skill | Books it owns |
| --- | --- | --- |
| 2 | character-rigger | role file body, `rigging-design`, `rigging-craft`, `rig-pipeline` (shared with animator and modeler: the rigger maker owns it this job) |
| 2 | art-director | role file body, `art-direction`, `art-review` |
| 2 | environment-designer | role file body, `environment-design`, `environment-craft` |
| 2 | film-director | role file body, `film-direction`, `film-craft` |
| 2 | vfx-designer | role file body, `vfx-design`, `vfx-craft` |
| 2 | sound-designer | role file body, `sound-design` |
| 2 | ui-ux-designer | role file body, `ui-design`, `ui-figma`, `ui-style-cartoon`, `ui-style-anime`, `ui-style-pixel`, `ui-style-stud` |
| 2 | marketing | role file body, `marketing-design`, `marketing-craft` |
| 2 | progression-designer | role file body, `progression-design`, `progression-craft` |
| 3 | live-ops-designer | role file body, `live-ops-design`, `live-ops-craft` |
| 3 | architect | role file body, `architecture` |
| 3 | feature-builder | role file body, `engineering-craft` (shared by four engineering roles: the feature-builder maker owns it), `ui-basics` |
| 3 | qa-lead | role file body, `testing` |
| 3 | reviewer | role file body, `code-review` |
| 3 | reference-images (shared) | `reference-images` |
| 3 | orchestration (the lead's book) | `orchestration` SKILL.md and references except `references/job-types.md` (job recipes: proposals only, J018-D2 point 4) |
| 3 | level-design (shared) | `level-design` |

Not in scope (proposals only, shown at G3): `platform-policy`, `ste-writing`, `studio-mcp`, `performance`, `data-saving`, `networking-security`, `analytics`, the analyst and trend-scout books, templates, tools, `.agents/workflows/jobs/`, `rules/`, job recipes.

## v3 (from wave 2, 2026-10-22)
Wave 2 result: art-director, ui-ux-designer and progression-designer passed; character-rigger, environment-designer, film-director, vfx-designer, sound-designer and marketing each ended round 3 with one blocking finding of one class: a measuring recipe written into the books gave a wrong number with no error in a common real case (cap faces read from a shared vertex group; palette roles compared under the wrong light; a flash counter that misses flicker after an eased rise and lets a lasting dim cancel later flashes, copied into three books; a loudness window stretched by trailing silence). The lead ran one focused repair round with the reviewers' tested fixes and moved the flash counter into one place (`vfx-craft/references/measure.md` §6).

| Rule | Text |
| --- | --- |
| V12 | Run each command on the exact input form the book names in the same step (how parts are attached, the rotation mode it recommends, the frame size of the render recipe it points to, the light the capture is taken under, files as delivered with padding or silence). Write each tool's silent thresholds next to the command. |
| V13 | A measure that needs more than a few lines of code is not written into a book: it becomes a manual or visual check plus a proposal row for a tested kit tool. A measure another role's book already carries is used by pointing to it, never copied. |

G3 proposal to carry: move the hand-written measures (flash count, chroma peak, detail density, cap exposure, trimmed loudness compare, palette-as-rendered) into tested kit tools, with fixtures from the review runs.

## v3 addendum (lead decision after wave 2 round 4, 2026-10-22)
Round 4 showed a loop: each adversarial review round finds a rarer edge case in a hand-written measuring heuristic (two lights flashing in turn, a reverb tail under the noise floor, a socket on a blocky parent). Each case is real; the right home for these measures is a tested kit tool (G3 proposal; `tools/` changes only with the owner's yes). Decision: the vfx-designer, character-rigger and sound-designer get one last repair with the round-4 tested fixes and no further review round; the lead verifies the repair. Film-director needs no new text (its finding is fixed in the vfx-owned shared counter).

| Rule | Text |
| --- | --- |
| V14 | Every measuring recipe in a book is a labelled screening aid: next to it, its known false readings, and the rule that a failing or borderline reading is checked by eye on the stills (or by ear) before any fix note goes out. |
| Review severity | A rare edge case in a labelled screening aid that lists its known limits is a recommendation (add it to the known limits). It is blocking only when the recipe gives a wrong number with no error in a common case the book itself prescribes, or when the book trusts the number without the eye check. |
