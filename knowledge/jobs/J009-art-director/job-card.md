---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent art-director)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J009 — Build the art-director agent

| Field | Value |
| --- | --- |
| Job id | J009-art-director (J006 is kept for the animator; J008 is the environment designer) |
| Size | L (new role, 2 skill books, a 1,695-line paper with 80 dated sources to extract and fact-check, first-game sources, a look-check script with tests, two real tests with reference images) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J009-D5). Steps 2-5 done 2026-10-21: 5 notes + 2 fact-checks in `knowledge/reference/art-direction/`; tool `tools/art/look_check.py` (20 tests); skills art-direction, art-review; role art-director; art-bible template direction record; evals. Gate PASS. Step 6 done 2026-10-21: hidden evals 29/30 (T10), blind UI review T09 (0 false claims; grades egg B- / anime B+ vs owner C- / B-, J009-D6), grader T11 (`grades-g2.md`); 19 skill gaps fixed + calibration (grade scale, finish as finding); tool v1.1.0 UI options (T12, 27 tests). Gate PASS. G2 sent to owner 2026-10-21; test A waits for a concept. **Job closed 2026-10-21 (G3, J009-D19).** Follow-ups: the vfx-design gaps (N17, owner: drop); J003 preproduction hand-off pointer (N13); a fresh hidden eval set for later regrades (N16) |
| Depends on | `reference-images` skill + `tools/art/art_refs.py` (exist); `templates/skill/art-bible.md` (exists); J003 game-designer (G2 sent) for the direction test |

## Owner's words (2026-10-21, excerpts)
- "It makes every game look like one game, and look great."
- "It works with the game designer from the first concept to set the visual direction: style, shape language, color, lighting, mood and the player fantasy in pictures."
- "It writes and owns each game's art bible ... It proposes which images become anchors; I approve every lock and every anchor."
- "It reviews the work of every visual agent ... for visual hierarchy, readability, silhouettes, color, values, lighting, scale and style match, so everything feels like one world. It also checks that motion and sound fit the same world."
- "It gives clear direction in the brief format (rules/messages.md): what to fix and why, in priority order, without doing the specialist's craft for them."
- "It cannot look at the game the way a human does, so build it measurable checks ... a grayscale value test, a silhouette test, palette extraction, and a thumbnail-size test ... but only the ones the research shows are useful."
- "Use it as strong evidence, but not as gospel. Check claims that matter, and drop what you cannot back up. Deadlock (Valve) and League of Legends (Riot) are my top references for art direction."
- "Keep the lessons that hold for any game, and remove anything specific to that game."
- "Model: Opus, high effort."

## Goal
One `art-director` agent that sets each game's visual direction with the game designer, writes and keeps the art bible (locks and proposed anchors, owner-approved), and reviews every visual craft so the game reads clearly and looks like one world. It measures what a model cannot see reliably (values, silhouettes, palette, small sizes) with deterministic scripts, interprets the numbers against the art bible, and directs specialists with ranked, sourced briefs that leave the craft to them.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Art_Director_Research_Paper.txt` (outside git) | 15 rules; Deadlock, TF2, Dota 2, League of Legends in depth; 7 short cases (Overwatch, Hades, Splatoon 3, Mario Wonder, Fortnite Ch4, Sea of Thieves, Hearthstone) + Luca, Gurney, Mateu-Mestre; numeric evidence ledger; concept → direction; art bible template + filled example; readability; hierarchy; shape, color, value (luminance math, contrast scopes, palette, silhouette, thumbnail, clutter); lighting; cohesion across crafts; consistency across makers and AI anchors; feedback template; platform; evolving a style; marketing; 14-step process; capture contract; 15-row pass/fail checklist; don'ts; open questions; source register (V01-V11 Valve, R01-R20 Riot, C01-C14 other studios, A01-A17 accessibility/AI/tools, P01-P18 Roblox) | 1,695 lines, 162 KB | high: VERIFIED / EXPERIENCE / OPINION tags on every claim, dated sources. The paper states it ran no image generation, scene, player study or screenshot measurement. Sources dated 2026-07 to 2026-10 are after the model cutoff → live check |
| DestructionSimulator `.claude/agents/art-director.md`, `.agents/skills/art-fundamentals/` (+ `references/expert-workflows.md`), `knowledge/design/art-bible.md`, `knowledge/design/ui-style.md`, art rows of `knowledge/design/decisions.md`, `content/art/anchors/` (read-only) | First-game art director role (squint + greyscale tests, ranked findings, could-not-check list), art fundamentals from owner-supplied Riot "So You Wanna Make Games??" transcripts, a filled art bible, anchor practice, owner art rulings (for example D-056 pickups must read as collectibles, not rubble) | ~500 lines + images | medium-high: owner practice and owner material; brick style, stages, game names → drop |
| Kit: `reference-images` skill, `tools/art/art_refs.py`, `templates/skill/art-bible.md`, `vfx-design`, `ui-design`, `sound-design`, `rig-pipeline` | The pipeline the art director owns the style of, and the specialist books it reviews against | — | owner-approved |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/art-direction/` + fact-check tables (Valve/Riot and other studio claims; accessibility, vision-model and tool numbers; Roblox rendering facts against the local docs mirror) | Making final assets of any craft (models, UI, VFX, animation, sound) |
| Skills `art-direction` (design) and `art-review` (craft), brief.md | Changing `reference-images` or `art_refs.py` beyond pointer lines to the new books |
| Look-check script `tools/art/look_check.py` + offline tests (scope: digest item 3) | Approving locks or anchors (owner only) |
| Role file `art-director`; the art-bible template gains the fields the research backs (semantic color roles, permitted variation, review states), owner approves | The marketing agent (planned); the environment-designer agent (J008) |
| Hand-off briefs to game designer, modeler, rigger, animator, VFX, UI, environment designer, marketing (planned), `rules/messages.md` format | A game's real art bible (each game writes its own) |
| Eval briefs + hidden cases; 2 real tests (G2) | Player studies, device benchmarks |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×5 (paper §1 cases; §2-5; §6-10; §11-14 + checklist + don'ts; first-game sources) | Sonnet | high (J004-D2, J005-D4 precedent; digest item 6) | dense notes per part |
| fact-checkers ×2 (Valve + Riot + other studio claims, web; accessibility, AI, tool and Roblox claims, web + local docs mirror) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| tool builder (look-check script + offline tests) | Opus | medium | `tools/art/look_check.py`, `tools/tests/test_look_check.py` |
| lead (merge, skills, role, template fields, hand-offs, evals, review) | Opus | high | 2 skills, role, hand-offs, evals, roster |
| art-director test A: direction (new) | Opus | high (owner) | 2-3 visual directions as reference images + first art-bible draft |
| art-director test B: cross-craft review (new) | Opus | high (owner) | look-check outputs, ranked findings, briefs to specialists |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time (company limit). Wave 1: 3 paper extractors. Wave 2: last paper extractor + first-game extractor + tool builder (the tool needs only the paper's method sections, already read by the lead). Wave 3: 2 fact-checkers. The lead writes the skills (it needs the paper, the first-game history and the specialist books together). The new art director runs both tests as a subagent with `art_refs.py`, the look-check tool and (for test B) Studio MCP captures.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 5 extract + 2 fact-check + 1 tool + 2 tests + 1 grader = 11 | 13 runs: 5 extract, 2 fact-check, 1 tool (+2 fix pushes), 1 tool update (T12), 2 tests, 1 grader; Sonnet high x8, Opus medium x2, Opus high x2 + lead |
| Models / effort | Sonnet high ×8; Opus medium ×1; Opus high ×2 + lead | |
| Image generations | test A: about 6-10 ChatGPT images (2-3 directions × 2-3 subjects, retries); test B: 0-2 | 0 so far (test A not run) |

## Acceptance checks
- [ ] Every Valve, Riot or other-studio claim in a skill has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-EXPERIENCE-or-OPINION / dropped); fan interpretations are never labelled as a studio rule; dropped claims listed with the reason.
- [ ] No invented thresholds: palette size, DeltaE tolerance, silhouette pixel size, world-art contrast and review counts stay PROPOSAL or per-project owner decisions; only scoped standards (WCAG / Xbox for UI text) are stated as numbers, with their scope.
- [ ] Nothing specific to DestructionSimulator in kit files (grep for brick style terms, stage names, D-ids = 0 hits outside source tables).
- [ ] Each look check returns a measurement + saved diagnostic image, never a quality score or a pass without a project tolerance; unknown or missing capture = NOT REVIEWED.
- [ ] Look-check script: offline tests pass (known luminance values, WCAG ratio examples, CIEDE2000 reference pairs, synthetic silhouettes and IoU, resampling recorded).
- [ ] Review output separates observation, interpretation and decision; findings ranked; each finding names evidence, the player consequence, the acceptance condition and the owner of the fix, never the technique.
- [ ] Art bible: locks and anchors are proposals until the owner approves each; versioned; permitted variation recorded.
- [ ] Hand-off briefs to the 8 roles follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.
- [ ] G2: test A directions shown next to Deadlock / League reference notes; test B review shown with its captures and measurements.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "Okay, I believe you can get started now." |
| G2 first real tests (direction + review) | | |
| G3 final approval | 2026-10-21 | "For now, the agent is just done." (J009-D19) |
