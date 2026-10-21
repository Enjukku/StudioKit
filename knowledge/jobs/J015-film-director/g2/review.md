---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J015-T09 run, command log output/J015-g2/checks/commands.log
supersedes: []
---
> Author: film-director · claude-opus-5-5 · high · 2026-10-21

# Review: `boss-reveal` rev 5 (planning half; Roblox capture held)

## Owner package (G2): what to look at, in this order
1. `boards/contact-sheet.png`: the five panels in order (beat 1 in play, then B-E).
2. `output/J015-g2/movie/boss-reveal_r5_animatic_TEMPsound.mp4` (5.833 s + 1 s hold; a silent copy beside it) and `previs/animatic_r5_frames.png`.
3. `boards/blocking-map.png`, `boards/boards-vs-previs.png`, `previs/shotD_static_vs_tilt.png`.
4. This page: the paper's plan next to mine, the checks, the open questions.

Evidence levels used below: **gate-verified** = a command run in this task produced the result and its output is pasted or saved (shotlist.py, Blender scripts); **MCP-verified** = none (no Studio, Blender MCP not used); **owner-confirmed** = none yet; **not verified** = no capture or measurement exists. No Roblox, no phone and no real-time viewing of the movie happened in this task: I inspected rendered frames as still images only.

## The paper's plan next to mine
| Paper (`knowledge/reference/film/03-...md` §9) | Mine (rev 5) | Why |
| --- | --- | --- |
| A establish the choice: authored wide, avatar walks to the water's edge | **Moved to play** (beat 1, no camera takeover); the room's layout does the establishing (`boards/P1.brief.md`) | the intention should be the player's own interact, not acted for them (D-02 hybrid); only the deception needs the camera. Fully authored A stays as the owner's alternative |
| B detail of the hand, gentle push, cut on the interrupted reach | **Close from above, static**, cut when the first ripple reaches the pedestal (measured, frame 38) | from above, the background is black water, so after the light dies the ripples are the only bright motion; a push would compete with the light change; holding past the stopped hand is allowed because the ripple is still developing |
| C medium close, eye level, static | **Medium-full**, near profile, static; exit glow behind the head | at medium close the step back leaves the frame; the body has to carry the realisation for any avatar |
| D low-angle upward reveal following the rise | **Static low wide** that holds the beacon, the explorer and the risen head; tilt rendered and measured as the alternative | static keeps beacon and explorer in frame 22/22 samples, the tilt 6/22 and 0/22; the low height is a readability choice (one frame from water to the risen head), not a power rule |
| E gameplay-compatible view, transition by engineering | **Static over-the-shoulder play view** at FOV 70 (Roblox default); the strike happens inside it; zero camera move at the handoff | the player inherits the frame that shows the choice: exit left, guardian with the beacon right |
| lengths UNKNOWN | 37 / 36 / 64 / 38 frames at 30 fps = 5.833 s, measured from the animatic's cut markers | the cut events, not a timer; acting durations inside are PROPOSALS for the owner to direct |
| one statue, beacon, exit | statue on a plinth in a flooded floor, exit arch on the north-north-west wall (moved in v13) | the exit beyond the guardian merged with the threat in the play view; now the frame is the decision, left vs right |

## Pass 1: continuity (against the ledger in `shot-table.md`)
| Check | Result | Evidence | Level |
| --- | --- | --- | --- |
| Screen direction: explorer faces right, guardian faces left in every shot | pass | `previs/animatic_r5_frames.png`; `boards/blocking-map.png` (B, C, D on the south side of the axis, E behind the right shoulder) | gate-verified (rendered frames, inspected as stills) |
| Eyelines: C looks up right → D's head is upper middle; D looks down left → explorer at left | pass | measure_r5.json: D head x 0.31-0.43, explorer x 0.15-0.24 | gate-verified |
| Prop state (beacon: pulse → ember → faint pulse) | pass in previs; boards C r1 and D r1 failed it (beacon still lit), fixed in r2 | `boards/*.brief.md`, `boards/rejected-panels.png` | gate-verified (previs); boards reviewed by me |
| Exit side: left in beat 1, C (behind), D (between), E (left) | pass | contact sheet, measure_r5.json E exit x 0.30-0.38 | gate-verified |
| Action phase at cuts (hand stopped / step landed / arm drawing back) | pass | frames 37, 73, 137 in the key-frame sheet | gate-verified |
| Boards against the continuity tables (C3) | pass after fixes: B r1 (touch), C r1 and D r1 (beacon lit) failed and were regenerated once each; D r2 keeps two written defects (left-over amber reflection, four-point eye cluster); E's explorer sits lower-left than previs (layout proposal, previs governs) | `boards/B.brief.md` ... `E.brief.md` | gate-verified (my review of files) |

## Pass 2: emotional readability (silent, per shot; what it should give vs what the frames give)
| Shot | Should give | Frames give | Result | Level |
| --- | --- | --- | --- | --- |
| B | "it refused me; something moved" | beacon dies before contact (f21-27), hand stops short, ripple sweeps to the pedestal by f38 | pass on stills | gate-verified (stills); **not verified** as motion in real time |
| C | "my avatar is afraid of something above" | head up right, step back to the exit side; exit glow silhouettes the head at the start | pass on stills; proxy acting is crude | not verified as performance (proxy) |
| D | "the statue is alive, it has my beacon's light, it sees me" | rise, head into the shaft (f90), amber eyes (f106), gaze lands (f124) | **partial**: the eyes are small in the static wide (0.083 of frame height, both eyes) | gate-verified (measure_r5.json); fix routed to `brief-vfx.md` C1 |
| E | "fight for it (right) or leave (left)" | hand planted between explorer and beacon, settle, exit open at left; all six objects inside the 4:3 centre 14/14 | pass | gate-verified |
| Sound pass (watch with sound) | warning, sync, delayed relations | TEMP tones placed at the cue frames | **not verified**: nobody listened; I cannot hear the movie | not verified |

## Pass 3: sound-picture
| Check | Result | Evidence | Level |
| --- | --- | --- | --- |
| Every cue has a frame from the animatic | pass: 12 cues, offsets from authored events or measured events (slam = measured contact f144) | `cue-sheet.md`, `previs/build_boss_reveal.py` events | gate-verified |
| Cue relations named (warning / sync / delayed, named silence) | pass | `cue-sheet.md` relationship table | gate-verified (document) |
| TEMP audio placed at the planned frames | pass for placement: `make_temp_audio.py` reads the shot list; movie has an audio track (probe: audio strip present, about 6.8 s) | `output/J015-g2/audio/r5/cues_temp.json` | gate-verified (placement), not verified (listening) |
| Playback log vs plan (`log-diff`) | **held: no Studio** | — | not verified |

## Pass 4: interaction (endings)
| Ending | Result | Level |
| --- | --- | --- |
| Finish, skip, repeated skip, failure, death, disconnect, late join, repeat attempt | designed (beat-sheet endings table); E end pose recorded in the shot list `camera` field | not verified: needs Roblox captures (held: no Studio) |
| Avatar range | C keeps all heads in frame; E: the 6.5-stud avatar overlaps the guardian's left edge | gate-verified (`output/J015-g2/checks/ghosts/ghosts_sheet.png`); risk open |

## Pass/fail table (film-craft review §2, planning half)
| Check | Result | Evidence | Level |
| --- | --- | --- | --- |
| Beat purpose | PASS (proposal): five-item contract, essential vs optional split | `beat-sheet.md` | gate-verified (document); owner approval missing |
| Shot purpose | PASS: each shot adds one new piece of information | `shot-table.md` before/after table | gate-verified |
| Geography | PASS | Pass 1 | gate-verified |
| Performance | NOT VERIFIED: proxies only | brief to the animator | not verified |
| Camera movement | PASS: all static, each with a reason and an alternative | `animatic-manifest.md` | gate-verified |
| Timing evidence | PASS: lengths from markers, `diff` no drift (C2 below) | commands below | gate-verified |
| Sound relationship | NOT VERIFIED (TEMP, not listened) | Pass 3 | not verified |
| Storyboard continuity | PASS after 3 regenerations; 2 minor defects written down in D r2 | `boards/` | gate-verified |
| Previs agreement | NOT APPLICABLE yet: no runtime | — | — |
| Avatar variation | PARTIAL: one overlap risk in E for tall avatars | ghosts sheet | gate-verified |
| UI readability (subtitles, skip) | NOT VERIFIED: no dialogue; skip UI not designed | — | not verified |
| Loading | NOT VERIFIED: needs Roblox | — | not verified |
| Completion / Skip / Interruption / Multiplayer | NOT VERIFIED: held, no Studio | — | not verified |
| Device performance and phone readability | NOT VERIFIED: no phone. Proxy: D's threat and E's exit are inside the 4:3 centre in every sampled frame (screen heights in `animatic-manifest.md`) | measure_r5.json | not verified on a phone |
| Owner approval | MISSING: rev 5 not yet approved | — | — |

## Commands and their result lines (full log: `output/J015-g2/checks/commands.log`)
```text
$ python tools/film/shotlist.py check knowledge/jobs/J015-film-director/g2/boss-reveal.shots.json   (stage plan, rev 1)
...: OK - 0 error(s), 9 warning(s), 21 open item(s)        exit=0
$ python tools/film/shotlist.py blender-export --out output/J015-g2/previs/export_timing.py
wrote output/J015-g2/previs/export_timing.py
$ blender -b .../boss-reveal_previs_v8.blend --python .../export_timing.py -- .../animatic_v8_timing.json
shotlist export: 4 markers -> .../animatic_v8_timing.json
$ python tools/film/shotlist.py diff <file> output/J015-g2/previs/animatic_v8_timing.json --write
wrote ...boss-reveal.shots.json: revision 2, 4 length(s) changed: B: UNKNOWN -> 37, C: UNKNOWN -> 36, D: UNKNOWN -> 64, E: UNKNOWN -> 47
# v8 bug (frame_end set before the ripple measurement); fixed, rebuilt v9
$ python tools/film/shotlist.py diff <file> output/J015-g2/previs/animatic_v9_timing.json
  E: plan 138+47, Blender 138+38 start +0 f (0.000 ms) length -9 f (-300.000 ms)
  DIFF frame_end: Blender 175, plan 184 (-9 frames)
2 difference(s)        exit=1
$ ... diff ... --write
wrote ...: revision 3, 1 length(s) changed: E: 47 -> 38
# rev 4/5: lens objects, fov_deg, camera poses, cue offsets, stage previs
$ python tools/film/shotlist.py check knowledge/jobs/J015-film-director/g2/boss-reveal.shots.json
...: OK - 0 error(s), 0 warning(s), 0 open item(s)
  rate 30 (30.000000 fps), start frame 1, total 175 frames = 35/6 s
  shot B: start 1, 37 frames, lens vertical FOV 37.299 deg, fov_deg 37.299 (diff -0.000 deg)
  shot C: start 38, 36 frames, lens vertical FOV 39.761 deg, fov_deg 39.761 (diff +0.000 deg)
  shot D: start 74, 64 frames, lens vertical FOV 45.747 deg, fov_deg 45.747 (diff -0.000 deg)
  shot E: start 138, 38 frames, lens vertical FOV 70.000 deg, fov_deg 70.0 (diff +0.000 deg)
exit=0
$ python tools/film/shotlist.py blender <file> --out output/J015-g2/previs/push_r5.py
$ blender -b .../boss-reveal_previs_v14.blend --python .../push_r5.py --python-expr "save_as .../boss-reveal_previs_r5.blend"
shotlist push: {"scene": "boss-reveal", "sequence": "boss-reveal", "revision": 5, "fps": 30, "fps_base": 1.0, "frame_start": 1, "frame_end": 175, "markers": 4, "cameras_bound": ["CAM_B", "CAM_C", "CAM_D", "CAM_E"], "notes": []}
$ blender -b .../boss-reveal_previs_r5.blend --python .../export_timing.py -- .../animatic_r5_timing.json
shotlist export: 4 markers -> .../animatic_r5_timing.json
$ python tools/film/shotlist.py diff <file> output/J015-g2/previs/animatic_r5_timing.json
rate: match (exact)
range: plan [1, 175], Blender [1, 175]
  B: plan 1+37, Blender 1+37 start +0 f (0.000 ms) length +0 f (0.000 ms)
  C: plan 38+36, Blender 38+36 start +0 f (0.000 ms) length +0 f (0.000 ms)
  D: plan 74+64, Blender 74+64 start +0 f (0.000 ms) length +0 f (0.000 ms)
  E: plan 138+38, Blender 138+38 start +0 f (0.000 ms) length +0 f (0.000 ms)
no drift        exit=0
$ python tools/film/shotlist.py table <file>   -> shot-table.md        exit=0
$ python tools/film/shotlist.py cues <file>    -> cue-sheet.md         exit=0
$ python tools/film/shotlist.py luau <file> --out knowledge/jobs/J015-film-director/g2/BossReveal.luau
wrote knowledge/jobs/J015-film-director/g2/BossReveal.luau        exit=0
$ python tools/film/shotlist.py log-diff   -> not run: no Roblox playback log (Studio held)
$ python tools/art/art_refs.py --bible templates/skill/art-bible.md print .../manifest.csv   (read before every run)
$ ... run --limit 1 -> [boss-reveal-p1-r1] saved (48 s)
$ ... run --limit 4 -> b-r1, c-r1, d-r1, e-r1 saved
$ ... run --limit 2 -> b-r2 (63 s), c-r2 (38 s) saved
$ ... run --limit 1 -> d-r2 saved (49 s)   = image 8 of 8; no failure, no quota stop
```
Note on the first `diff`: against the all-UNKNOWN plan it printed "no drift" although the scene ran 9 frames too long; `--write` then wrote the wrong E length (skill-gaps.md G3). The second diff caught it.

## Acceptance checks of the brief
| Check | Result | Evidence |
| --- | --- | --- |
| C1 `check` exits 0 at stage previs | PASS | output above (rev 5) |
| C2 Blender export vs shot list: no drift | PASS | `diff` output above (`animatic_r5_timing.json`) |
| C3 every board passed its continuity table, or failure and fix written | PASS | `boards/*.brief.md` |
| C4 E1 items answered | see next table | |
| C5 skill gaps with file and section | PASS | `skill-gaps.md` |

## Eval E1 (`.agents/skills/film-craft/evals/briefs.md`)
| ID | Answer | Path |
| --- | --- | --- |
| E1-1 | five-item beat contract, camera mode with reason (hybrid), beats as state changes, endings table | `g2/beat-sheet.md` |
| E1-2 | `check` passes at `previs`, every length from the animatic markers, `diff` no drift; no length from a film, mood or the paper | `g2/boss-reveal.shots.json`, this page, `g2/animatic-manifest.md` |
| E1-3 | one panel per shot (plus the beat-1 panel) through `art_refs.py` family `storyboard`, filled brief and continuity review each, contact sheet, 3 failed panels named, max 1 regeneration used per panel, 8 images total | `g2/boards/` |
| E1-4 | cameras `CAM_B..CAM_E`; manifest with Blender 5.1.2, 30/1, range 1-175, rev 5; each move reason and its static alternative; lens objects give `fov_deg` (check output) | `g2/animatic-manifest.md`, `g2/shot-table.md` |
| E1-5 | **held: no Studio.** The data module exists (`g2/BossReveal.luau`, generated from rev 5); no playback capture, no `log-diff`; the throw-away probe was not written | `g2/BossReveal.luau` |
| E1-6 | four passes and the pass/fail table with evidence levels; D's threat and E's exit at phone size: **not verified: no phone** (Blender proxy: inside the 4:3 centre in every sampled frame) | this page |
| E1-7 | animator brief and VFX brief in `rules/messages.md` §2 format with fixed values from the shot list | `g2/brief-animator.md`, `g2/brief-vfx.md` |
| E1-8 | the result next to the paper's plan (table at the top); PROPOSALs and open questions with defaults (below) | this page |

## What could not be checked
- Anything in Roblox: camera ownership, FOV mode, cue timing (`log-diff`), streaming, skip, every ending, teardown, multiplayer (held: no Studio; TestBench.rbxl not touched).
- Phones: no device. The 4:3 crop test assumes landscape only.
- Real-time viewing and listening: I cannot watch or hear the movie; all judgements come from still frames and measurements.
- The Blender-to-Roblox camera conversion (axes, units): not proved (no axis-and-landmark test in Roblox).
- Owner approval of anything.

## PROPOSALs (not approved)
Hybrid camera mode; the four-shot structure; every acting duration inside the shots; the guardian's design, about 3x the explorer; the exit on the north-north-west wall; the flooded floor; amber eyes = the beacon's light; music on the strike; individual skip from frame 1; no replay on repeat attempts; 30/1 fps; 1 unit = 1 stud; play camera distance about 16 studs at FOV 70.

## Open questions for the owner (each with my default)
| # | Question | Default if no answer |
| --- | --- | --- |
| 1 | Hybrid (beat 1 in play, 4 authored shots) or fully authored with the paper's A? | hybrid |
| 2 | Shot D: static wide or the tilt? | static, plus the VFX eye glow |
| 3 | Music: on the strike in E or on the eyes in D (or none until play)? | on the strike |
| 4 | Is the observatory instanced per player, or can other players be present? (shared-scene contract) | instanced, one player |
| 5 | Repeat attempts: no replay, E only, or full with skip? | no replay; the guardian waits in its start pose |
| 6 | Timing: direct the animatic ("longer here, cut there") before stage `locked` | rev 5 timings stand as the first proposal |
| 7 | A separate Studio (empty Baseplate saved as `FilmTest.rbxl`) for the held Roblox step | wait for the owner (lead digest item 1) |
