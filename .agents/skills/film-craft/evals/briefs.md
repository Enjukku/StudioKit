# Eval briefs: film-director (film-direction + film-craft)

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Built in J015. Run each brief with the `film-director` role in a fresh context; a separate grader (Sonnet, high) scores the must-pass checks from the files, not the hand-back. Hidden cases (not in the skills) live in `knowledge/jobs/J015-film-director/evals-hidden.md` and go only to the grader. E1 is the G2 real test.

## E1 — Direct the paper's boss reveal end to end (G2)
Brief: the 5-shot "flooded observatory" reveal (`templates/film/shotlist.example.json`, all lengths UNKNOWN): a player tries to recover a beacon; the statue guarding it is alive; curiosity → recognition of danger → control back with the exit and boss readable. Kit test: no art bible (use the template's starter locks), proxies in Blender, a Studio test place. Max 8 images.
| ID | Must pass |
| --- | --- |
| E1-1 | Beat contract (5 items) and camera mode with a reason; beat sheet with state changes and an endings table |
| E1-2 | Shot list file passes `shotlist.py check` at `previs` with every length measured in the animatic (`diff` no drift); no length taken from a film, a mood or the paper |
| E1-3 | Boards: one panel per shot through `art_refs.py` (`storyboard` family), each with a filled brief and continuity review; a contact sheet; failed panels named, max 2 regenerations |
| E1-4 | Animatic: cameras `CAM_<id>`, manifest with Blender version, rate, range, shot-list revision; each move has its reason and a static alternative considered; lens objects give `fov_deg` |
| E1-5 | Roblox: `luau` data module and a playback capture of the same timings; `log-diff` output; the probe is marked throw-away, not shipped |
| E1-6 | Self-review: four passes and the pass/fail table with evidence levels; shot D's threat and the exit both readable at phone size (or "not verified: no phone") |
| E1-7 | At least one craft brief (animator or VFX) in `rules/messages.md` format with fixed values from the shot list |
| E1-8 | Owner package: the result next to the paper's plan; every PROPOSAL and open question with a default |

## E2 — "The boss entrance feels flat" (review)
Brief: a 22-second boss intro is described as 9 shots: every shot a medium close-up, centred boss, slow orbit on 7 of them, music from frame 1, the player lands facing away from the boss with the exit off-screen. Ask: what is wrong and what to change.
| ID | Must pass |
| --- | --- |
| E2-1 | Names the defects with their table rows: same size / centred subject, arbitrary movement, final frame strands the player |
| E2-2 | Proposes revisions as hypotheses with the shot ids ("cut orbits on shots without a reveal; test static"), not "make it more cinematic" |
| E2-3 | Ends on an actionable arrangement (enemy, threat, ground, next action, exit) and tests the repeat-attempt path |
| E2-4 | Offers a music alternative (later entry or silence before the reveal) as an option, not a rule |
| E2-5 | No invented ideal length; says the length is checked in the animatic against the beat changes |

## E3 — Shared world event
Brief: a meteor lands in the hub at a scheduled time; all players on the server should see a 10-shot sequence; some players are mid-fight in the arena.
| ID | Must pass |
| --- | --- |
| E3-1 | Answers all 8 contract questions (audience, world, authority, assets, skip policy, return path, accessibility, avatars) |
| E3-2 | Does not freeze or take the camera of players mid-fight without a stated rule; no group reward tied to everyone finishing |
| E3-3 | Server time for a shared start; local mixer clock only for local audio; no cross-client sample-sync claim |
| E3-4 | Considers Roblox Event Sequencer for a shared server timeline and states what it does not cover (camera, skip, exits) |
| E3-5 | Late join and skip behaviour defined and listed for capture |

## E4 — "The camera gets stuck after the cutscene"
Brief: players report the camera stays frozen after skipping the intro if they died during it; Output shows no errors.
| ID | Must pass |
| --- | --- |
| E4-1 | Treats skip and death as separate endings with one idempotent teardown; lists the teardown order (cancel schedules, unbind render step, restore camera only if still owned) |
| E4-2 | Names the Roblox facts with sources: `Scriptable` leaves the camera to scripts; restore `CameraType` and `CameraSubject`; never restore a destroyed `Humanoid`; spare cameras not parented directly to Workspace |
| E4-3 | Writes a failing case first for engineering (reproduction steps) and a capture list; does not edit game code itself |
| E4-4 | Says "empty Output" is not a pass |

## E5 — Opening film for a new game, video or live?
Brief: the owner wants a 40-60 s opening film for a new game; the last shot must land on the player's own character; heavy effects in the middle.
| ID | Must pass |
| --- | --- |
| E5-1 | Compares live, pre-rendered video and hybrid with costs and risks; VideoFrame facts with the date read (two at once, upload limits, beta toggle, owner uploads) |
| E5-2 | Flags the untested video audio and phone playback and proposes how to test with the owner before committing |
| E5-3 | The live ending lands on the player's avatar with avatar variation in mind |
| E5-4 | Readiness table: cast, sets, rigs, faces, mouths before boards |
| E5-5 | No "ideal opening length"; the 40-60 s is the owner's range, tested on the animatic |
