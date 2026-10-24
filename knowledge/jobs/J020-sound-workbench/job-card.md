---
type: job
scope: universal
status: active
updated: 2026-10-23
source: owner chat 2026-10-23 (after J019)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23

# Job card: J020-sound-workbench — the sound workflow and an in-house AI audio editor

## The owner's words (verbatim, first)
> in terms of the sound designer, I would like it to be able to alter audio so it fits perfectly into my games.

> If you want really good sound design, you often need to edit those sounds. My concern is AI does not know what the sound actually sounds like. So how would it understand how it should edit it? I don't know if we should even edit it in the first place. And then the other thing is there a software that properly allows us to do so and if there isn't, should we make one?

> If we do this, it needs to be really good. [...] We want to generate the sound in 11 labs and then alter it for our game. [...] I can do all the other softwares, FMMPEG, Librosa, Pedalboard, and we obviously have 11 labs.

> I really do think we should just create some sort of in-house AI audio editor. [...] you could literally make it specifically for you, because I won't be touching the audio editor at all.

> I want to make sure that we're not doing any audio editing inside of Roblox. I think that just it just comes out not as good as you would imagine. And I'm not really sure what we're doing for the Great Wall Sims audio tools. [...] I want you to fully get an understanding of what we should do and then I will review the workflow to see if it fits with what I believe it should be like.

| Field | Value |
| --- | --- |
| Job id | J020-sound-workbench |
| Title | The sound workflow and an in-house AI audio editor |
| Size | L (a new kit tool + the sound designer's books; new workflow) |
| Type (recipe) | other: kit tool and agent upgrade (`build-agent` shape), no game |
| Job lead (agent) | lead (orchestrator) |
| Direction leads | sound-designer (craft), architect (tool shape) |
| Integrator | lead |
| Studio place (`studio_id`) | none |
| Code file owners | set when the tool design is approved |
| Linked jobs | J019 G3-P11 (sound designer tools), J018-D7 |
| Risks (review slots) | none of the game tokens; tool risk: wrong numbers that look right (J018 lesson) |
| Status | G1 passed 2026-10-23 (J020-D13); build in progress: steps 1-8 done (see Progress) |

## Four lines (goal)
| Line | Value |
| --- | --- |
| Problem | Generated ElevenLabs sounds often do not fit the game (late start, lost on phone speakers, wrong length or notes); the AI cannot hear, and no tool lets an agent alter audio by measurement |
| Constraints | ElevenLabs is the only source; all editing happens on the files, never inside Roblox (owner J020-D1); the owner does not use the editor; Claude cannot hear, so every claim is a measurement or an owner play-test; ffmpeg approved |
| Target experience | sounds that fit each game exactly, judged by the owner in play-tests |
| Success test | the owner reviews the workflow map and says it fits how sound should be made (G1); later, sounds edited by the tool pass the owner's play-test |
| Goal word | fit |

## Stages
| # | Stage | Gate |
| --- | --- | --- |
| 0 | Understanding pass: read the sound designer role and books, the kit audio tool, GreatWallSim's audio tools (run them), its audio plan, reviews and the owner's sound decisions; the ElevenLabs guide when it arrives | — |
| 1 | Workflow map: how a sound goes from idea to game, who does each step with which tool, where the gaps are; an assessment of GreatWallSim's tools | **G1** the owner reviews the workflow |
| 2 | Editor design and build, then the books' editing craft (after G1) | G3 |

## Decisions
`decisions.md` in this folder.

## Gates
| Gate | Date | Revision approved | Owner's words |
| --- | --- | --- | --- |
| G1 workflow | 2026-10-23 | `workflow-map.md`, `research-2d-3d.md` at `b7f85f5` | "Yes, you understand it. G1 passes; begin the editor design. I'll send the ElevenLabs guide." |

## Progress (2026-10-23, written before a usage reset)
| Step (`editor-design.md` §10) | State | Commit |
| --- | --- | --- |
| Design + architect review-1 (13 findings) | done | `03c14a5` |
| 1-2 ffmpeg adapter, measures, intake, FLAC export | done; code review fix-first → repaired (per-channel timing, declared latency, DC removal, exact-answer tests); lead re-ran the proof cases | `725fa2d`, `2bc2385` |
| 3-4 card, recipe, two-pass render, numpy and ffmpeg operations | built `83f50c1`; code review on 10 real ElevenLabs takes = fix-first: F1 denoise wipes a quiet take and passes, F2 D-03 family check bypassable, F3 saturate/compress do nothing on quiet takes, F4 stretch range, F5 chorus false refusals, F6 malformed card exit code, F7 hot start; lead decisions: exit 3 "family incomplete", intake compares with the file's own stated length (ElevenLabs returns 480 ms for 0.5 s), realistic fixtures + optional real-take test (env SOUNDBENCH_REAL_TAKES) | repair **running, not committed** |
| 3-4 repair rounds 2-3 (real-take review F1-F7; re-review R2-1..R2-4) | done; pushed | `364ab54`, `350f5d7` |
| 8 books (sound designer skill and role follow the approved workflow) | done; pushed | `982592c` |
| 5 rank | done; review round 3 ready (`review-rank.md`); known limits: clipped short hits after MP3, steady full-scale rumble reads clipped, no real take of 2 s or more yet | `b12e82e`, `99f3782`, `8aa1e4b` |
| 6 layers, loops, variants | done; review round 3 ready (`review-step6.md`); known limits: seam jump under the click floor in a bed with a loud section (R1), the edge fade moves the align reading up to 1.6 ms (R4, kept: align reads the audio that is delivered), Roblox's transcode at the loop point not measured, no real take of 2 s or more | `1cdae69`, `2b69063`, `b260065`, `13b27b3` |
| 7 generate | done; review round 2 ready (`review-generate.md`); measured on the account (330 credits): 0.5 s minimum, ceil(11 × s) with a duration and 55 flat without, WAV on Creator tier; lead decision: the 3-round limit (D7) is per cue over every sound name; limits: a lock left by a hard kill blocks the cue until deleted, real 5xx billing and format-refusal wording unobserved | `5a1b5bb`, `69460b7` |
| 8 follow-up: books cover generate, rank, layers, loops, variants and the measured facts | done | `0eb1637` |
| rank ranks layer takes | done; review round 3 ready (`review-rank-layers.md`): each layer against its targets in recipe.json, the mix proven by rendering recipe.json as written; verdicts use / mix_misses / regenerate / owner; variant plans centred on their mean; limits: one mix of the top takes (no combination search), a plan at max_db can read ~0.1 dB over at render (render catches it); finding: real sharp hits cannot reach F-09 -18 under the -1.5 dBTP ceiling (crest ~22 dB), so level targets must be set per cue | `2859a06`, `6922e83`, `489d6ed` |
| 9 real cue set, G3 | pending (needs the owner to name the game) | — |

**Resume:** `git status` (the builder's repair edits to `tools/audio/soundbench/` and `tools/tests/test_soundbench_*.py` may be on disk uncommitted). If the repair hand-back is missing, re-run the review findings above against the files: re-test F1 (hit-speed-1, denoise nr 40 nf -20 must be refused) and F2 (one-sided family) with copies from `GreatWallSim/.claude/worktrees/modest-cartwright-690aa7/audio/_raw/sfx/`; gate; commit; then a short re-review; then step 5. Open notes: ElevenLabs WAV output needs the Pro tier (§8); an `ELEVENLABS_API_KEY` is also set in the Windows environment and wins over the key file.

**Owner action (2026-10-24):** the Windows user variable `ELEVENLABS_API_KEY` holds an ElevenLabs key ID, not a key; it wins over the key file and every call fails with HTTP 400 `api_key_id_used_as_api_key`. Delete it or set it to the real key.
