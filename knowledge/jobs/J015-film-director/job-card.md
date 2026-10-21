---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent film-director)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J015 — Build the film-director agent

| Field | Value |
| --- | --- |
| Job id | J015-film-director (opened as J013 on 2026-10-21; renamed the same day because J013-analyst and J014-live-ops-designer, opened by other chats at the same time, used the same number; ticket ids T01-T08 and decision ids D1-D7 keep their numbers under J015) |
| Size | L (new role, 2 skill books, a 1,931-line paper with ~60 dated sources (Roblox, Blender 5.2 and ChatGPT Images facts after the model cutoff) to extract and fact-check, a read-only earlier-game source to distil, 3 templates, a shot-list format with a small tool and tests, an art-bible family, a real test with ChatGPT boards, Blender previs and a Roblox playback check) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J015-D7). Steps 2-5 done 2026-10-21: 4 notes + 3 fact-checks in `knowledge/reference/film/` (Roblox 33 rows, Blender/images 23 rows with 10 probes, craft sources 47 rows); tool `tools/film/shotlist.py` (47 tests); skills film-direction, film-craft; templates beat sheet (extended), shot list, storyboard brief, shotlist.example.json; art-bible family `storyboard`; role `film-director`; evals E1-E5 + hidden H1-H4; roster row. Step 6: G2 test run (J015-T09, planning half: hybrid boss reveal, 4 shots, 175 frames at 30/1, 8 images, animatic, check + diff clean); 19 gaps found (18 agent + 1 lead) and fixed (J015-T10 tool; skills, templates, game profile). G2 decision waits for the owner (`digest-g2.md`); Roblox step waits for a separate Studio |
| Depends on | `reference-images` skill + `tools/art/art_refs.py` + `templates/skill/art-bible.md` (exist); Blender MCP (connected); Studio MCP; `vfx-design`/`vfx-craft`, `sound-design`, `environment-design`, `ui-design`, `art-direction`, `engineering-craft` skills (exist); animator role (planned, J006, not built) |

## Owner's words (2026-10-21, excerpts)
- "It directs every cinematic moment in a game, like a movie director: opening films, story cutscenes, boss introductions, reveals, endings, and short in-game camera moments."
- "It decides what each shot shows, the shot size and angle, the lens, how the camera moves, how long each shot lasts, where it cuts, how characters are staged and act, and how light, color, sound and music carry the emotion."
- "It plans before anything is animated: a beat sheet, a shot list with timings, storyboards made with ChatGPT through the kit's reference-images skill ... and a previs or animatic in Blender."
- "It hands each shot's needs to the animator ..., the environment designer ..., VFX, sound ... and UI ..., in the brief format (rules/messages.md)."
- "It assembles and checks the final cutscene in Roblox: camera control, cues on time, smooth return of control to the player, skipping, and performance on phones."
- "It reviews its own work from captured clips before I see it."
- "A shot list format a script can read, so the cutscene timings stay the same in the plan, the previs and Roblox. Only build a script if the research shows it is useful."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially Roblox camera and cutscene facts, and drop what you cannot back up."
- "This agent replaces cutscene-director in the roster. Model: Opus, high effort."

## Goal
One `film-director` agent that turns a story beat into a sequence the player understands and feels: it names the change in feeling and knowledge first, then plans every shot (size, angle, lens/FOV, move, length, cut, staging, acting, light, sound) with a reason, proves the plan in boards and a timed Blender animatic, briefs each craft, assembles and checks the Roblox playback (camera ownership, cues on time, skip, every exit back to play, phones), and reviews its own captures before the owner sees them. One shot list, with stable shot ids and one timing convention, is the truth for the plan, the previs and Roblox.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Film_Director_Research_2026.txt` (outside git; owner wrote it) | 15 rules; 8 scene studies (Jaws, Yojimbo, Fatal Attraction, Feast, Spider-Verse, God of War x2, Half-Life: Alyx) + Piper, Arcane, Raiders oner; shots, lenses, movement, staging, editing, structure, light/colour, acting, sound; game cinematics, skip/replay/comfort, multiplayer contract; boards, Blender 5.2 previs (camera maths, FPS and frame-interval maths, evaluated export), ChatGPT boards; Roblox runtime (Camera, FOV mode, BindToRenderStep, animation markers and graphs, server time vs mixer time, AudioPlayer scheduling, streaming and frustum streaming, preload, ScreenInsets, input contexts, VideoFrame, Moon Animator); terminal-path contract; shot vocabulary; method; hand-off table; AI defect table; shot-list template; filled 5-shot boss reveal; storyboard brief template; pass/fail review; don'ts; open questions; source register F01-F12, A01-A10, G01-G10, B01-B17, R01-R29 | 1,931 lines, 141 KB | high: VERIFIED / EXPERIENCE / OPINION on every claim; it invents no shot lengths or lens moods (all UNKNOWN). It ran no Blender, no Roblox test and watched no clips. Roblox, Blender 5.2 and ChatGPT Images 2.5 facts are after the model cutoff → live check |
| DestructionSimulator (read-only): `knowledge/design/story-opening-cutscene.md`, `story-film-plan.md`, `story-film-sound.md`; logs `2026-10-11-story-cast-refs.md`, `2026-10-12-opening-film-rigs.md`; decisions D-147, D-148, D-149, D-153, D-155, D-160, D-180, D-181, D-183..D-186 | The first game's opening film: scene list, video-vs-live split, Blender-still boards (chosen over AI boards for consistency), 24 fps 1080p VideoFrame plan, sound plan, rig and face lessons, owner corrections | ~45 KB notes | medium: real owner decisions and corrections; game-specific content to strip; film never reached animatic |
| Kit: `reference-images`, `art_refs.py`, `art-bible.md` template, `templates/jobs/beat-sheet.md`, `vfx-design` §3 cutscene row, `sound-design`, `ui-design`, `environment-design`, local Roblox docs mirror (incl. `resources/modules/event-sequencer.md`) | The pipeline and neighbour rules the agent works inside | — | owner-approved |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/film/` + fact-check tables (Roblox runtime; Blender 5.2 + ChatGPT Images; film/game craft sources) + earlier-game lessons note | The cutscene playback runtime as shipping game code (digest item 3: engineering follow-up) |
| Skills (names: digest item 4): design (what and why: shots, moves, cuts, staging, acting, light, sound, player control, review) and craft (how: beat sheet → shot list → boards → Blender previs → briefs → Roblox assembly → capture review) | Animating final clips, building sets, making VFX or sounds, final UI (the crafts do; this agent briefs and reviews) |
| Templates: beat sheet (replaces or extends `templates/jobs/beat-sheet.md`), shot list, storyboard image brief | A real game's cutscene |
| Shot-list data format + `tools/film/shotlist.py` + offline tests, if fact-checks keep the case (digest item 2) | Camera-pose export from Blender to Roblox CFrames beyond what the G2 test needs |
| Art-bible template: `storyboard` family + lock; `reference-images` role row | The animator role (J006) |
| Role file `film-director`; roster row replaces cutscene-director; pointer lines in `vfx-design` (cutscene row) and roles that name a cutscene director | Player studies, analytics instrumentation |
| Hand-off briefs: animator (planned), environment designer, VFX, sound, UI, engineering, game designer, art director | |
| Eval briefs + hidden cases; 1 real test (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×3 (paper §1-10 craft and game cinematics; §11-13 previs, Roblox runtime, method + templates + register; DestructionSimulator film records → universal lessons) | Sonnet | high (J004, J009, J012 precedent) | dense notes per part |
| fact-checkers ×3 (Roblox runtime R01-R29: local docs mirror first, then live docs and DevForum; Blender 5.2 B01-B14 against the connected Blender + manual, ChatGPT Images B15-B17; film/game craft F, A, G sources: spot-check quotes, dates, scope) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| tool builder (shot-list tool + tests) | Opus | medium | script + tests |
| lead (merge, skills, templates, role, family, hand-offs, evals, review) | Opus | high | 2 skills, 3 templates, role, family, hand-offs, evals, roster |
| film-director test (new agent) | Opus | high | G2 package |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time. Wave 1: 3 extractors. Wave 2: 3 fact-checkers (they read the extract notes and the paper's register). Tool builder after the fact-checks confirm the timing facts the format rests on. The lead writes the skills and templates. The new agent runs the G2 test as a subagent with `art_refs.py`, Blender MCP and Studio MCP.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 3 extract + 3 fact-check + 1 tool + 1 test + 1 grader = 9 | |
| Models / effort | Sonnet high ×7; Opus medium ×1; Opus high ×1 + lead | |
| Image generations | G2 test: about 5-8 ChatGPT board panels (5 shots + retries) | |

## Acceptance checks
- [ ] Every Roblox camera, cutscene, timing, audio, streaming, UI and input fact in a skill has a source, a date and a fact-check verdict (confirmed / corrected / unverified-kept-with-label / dropped); dropped claims listed with the reason.
- [ ] No invented numbers: no ideal cutscene length, shot length per mood, skip delay, lens-to-emotion map, camera speed limit or phone budget. Angle and move effects are stated as conditional ("can", "when"), as the paper does.
- [ ] Every shot in a plan has a job (new information or a performance change) and a stated emotion change; every move has a reason; the review checks both.
- [ ] One shot list per sequence is the timing truth: stable shot ids, one interval convention `[start, next-start)`, a rational frame rate; boards, previs and Roblox use the same ids (tool check, if built).
- [ ] Every exit is specified and tested as its own ending: finish, skip, repeated skip, failure/missing asset, death/respawn, disconnect, late join (where the scene is shared). Visuals never grant rewards or decide outcomes.
- [ ] Storyboards go through `reference-images` with the new family; each panel is reviewed for continuity (screen direction, eyeline, prop hand, light direction) before use.
- [ ] Earlier-game lessons note keeps only universal lessons; no game names, characters or stage content in kit files.
- [ ] 3 templates exist and each is used in the G2 test.
- [ ] Hand-off briefs follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "You may begin." |
| G2 first real test | | |
| G3 final approval | | |
