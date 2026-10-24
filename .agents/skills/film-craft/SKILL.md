---
name: film-craft
description: The how for a Roblox cinematic - beat sheet, options, shot list with camera, lengths and markers (tools/film/shotlist.py), Roblox assembly (camera, cues, skip, endings), capture review; boards and an animatic only when the owner asks. Use for "storyboard this", "time the cutscene", "put the cutscene in the game", "the cues are late", "skip breaks it". Read film-direction first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J015 from the owner's research paper (`knowledge/reference/film/01..03`), the first game's opening-film records (`04`) and three fact-checks (`fact-check-roblox-runtime.md`, `fact-check-blender-images.md`, `fact-check-craft-sources.md`, all 2026-10-21). Rebuilt by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (options, blocking and value passes; the self-review lines; the image budget). Evidence stays out of the body: the notes above (ids N1..N4, FR = Roblox fact-check, FB = Blender/images fact-check, cited in the references). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): outside method.; revised by orchestrator · claude-opus-5-5 · default · 2026-10-24 (J024, owner J023-D7: no strips, boards or animatic as passes)

# Film craft: from plan to a proven cutscene

## 1. When this skill starts
`film-direction` has produced (or is producing with you) the beat contract, the camera mode and the shot design. Before step 1 you need: the owner's brief; the game's art bible (`knowledge/design/art-bible.md`, or the kit template for a test); the game profile (devices, play camera, narrowest display, test place). Missing facts that change the result: state an assumption and continue. **After a context compaction**, re-read §3, §5 and §6 and `references/review.md` §6 before you continue.

You see stills and numbers. Timing is judged from the shot list, the animatic's marker export and the playback log at a known rate; feel at normal speed is the owner's call on the playable animatic at the gate. Every check follows the light-check rule: numbers for every case, images only where a number fails and for a few key frames (`references/review.md` §7).

## 2. Read this file when
| You need | Open |
| --- | --- |
| The self-review lines per stage, with their input and budget; the pass/fail table; captures; change control | `references/review.md` (§6 lines, §7 budget) |
| Options thumbnails, blocking stills, black-fill and subject masks, ranking bright regions, the value strip, contact sheets, the frame export for the flash count (the counter: `vfx-craft/references/measure.md` §6) | `references/blender-previs.md` §7 |
| The shot list file, its fields and the tool commands | `references/shot-list-format.md`; fields for people: `templates/film/shot-list.md` |
| Beat sheet and gameplay state sheet | `templates/jobs/beat-sheet.md` |
| Storyboard panels with ChatGPT, their review, when Blender stills take over | `references/storyboards.md`; brief: `templates/film/storyboard-brief.md`; tool: `reference-images` skill |
| Blender previs: version, camera spec, lens → Roblox FOV, markers, frame rates, review artifacts, camera export | `references/blender-previs.md` §1-6 |
| What to brief each craft, fixed vs open, an example brief | `references/handoff-briefs.md` |
| Roblox: which runtime, camera, cues and clocks, effects, streaming, UI and input, endings and teardown | `references/roblox-assembly.md` |
| Driving Studio for checks and captures | `studio-mcp` skill (you, or the studio-operator for multi-client runs) |
| Phone performance measurement | `performance` skill |
| Value, silhouette and small-size measures of key frames | `tools/art/look_check.py` (`value`, `silhouette`, `thumb`, `palette`) |
| Play camera, supported displays, cinematic rate | `knowledge/design/game-profile.md` |

## 3. Steps
**In a studio job (J024, owner J023-D7) steps 5-8 and 10 are not passes:** no blocking strip, value strip, boards, animatic or blocking check-in is handed to anyone or waits for a review. You plan every shot's camera, length and the marker list in the beat sheet and the shot list (steps 2-4), with the value and light plan per beat; a quick blocking still, a value read or the 4:3-centre read inside your own run is a measured self-check; the B lines run on the Roblox captures (step 12). Steps 5-8 run as passes only when the owner asks for boards or an animatic. Size the passes at step 1 and record them with the budget. A short in-play camera moment (one authored look, a few seconds) runs text options, one blocking key frame with its B-03, B-04 and B-06 numbers, the animatic with its cue markers and the Roblox lines. Option sheets, the value strip, light variants, boards and two edit takes are for a moment with a key beat worth them; a skipped pass is n/a with its reason in the self-review.

1. **Restate and check readiness.** Restate goal, feeling, premise, fixed, open, checks, the budget (options, passes, images) and the stop criteria. List every character, set, prop, rig feature (face kit, eye target, mouth shapes, limb range) and sound the shot design needs; mark each ready / partial / missing; missing items become tickets now. *Check: readiness table in the job folder.*
2. **Beat sheet** from `templates/jobs/beat-sheet.md`: the beat contract with problem, premise, hook, target experience and sell list; beats as state changes with a rising intensity line; gameplay state sheet; endings table. Owner approves the beat contract (G1 for M/L jobs). *Check: P-01, P-05, P-06; owner decision id recorded.*
3. **Options pass (thumbnails).** A narrow research board: our game's approved images first, then real-world reference, one outside-games source chosen from the target-experience sentence with the method taken (D-23). Then 2-3 clearly different approaches for the key beat, each with a one-line hook, one non-obvious; each made as a strip of rough greybox stills from proxy cameras (one still per shot), shaded and black-fill, tiled into one contact sheet per approach at phone size, all at the same low finish (`references/blender-previs.md` §7). Budget: at most 3 contact sheets; other beats get text options only. Pick with a goal question against the sell list; record the reasons each other option lost; show the owner the sheets with one recommendation (the direction stage's "approaches"). *Check: P-04.*
4. **Shot list file** at `stage: plan` (`references/shot-list-format.md`): every shot with the 10 fields, purpose, continuity; cues with ids; lengths UNKNOWN or event-bounded. In `shot-table.md`, beside the printed table: the before/after table, the continuity ledger and a **picture plan** (per shot: first-second read, read order, value key, brightest area, overlay zones). `shotlist.py check` passes. *Check: exit 0; P-03, P-08, P-09.*
5. **Blocking pass.** The overhead blocking map (entrances, exits, threats, positions per beat, the action axis, each camera's side). Proxies at true scale with a player-sized reference and the smallest and tallest supported avatar; actors' marks and paths per beat; then cameras `CAM_<id>` on the approved blocking. Render each shot's key frame: shaded, black-fill per group and a subject mask from the same pass, plus the delivery-frame overlay. Measure (B-01..B-05) and tile one blocking strip. Show the strip at the check-in your recipe names before the camera and light are polished. *Check: B-01..B-05.*
6. **Value pass.** Test 2-3 light variants of the key beat on the greybox and choose (budget: the variants' key frames as one strip). Then for every key frame: `look_check.py value` (subject/ring ratio, the subject's rank by p95 among the named bright regions, the picture-area spread against the beat's planned intensity) and one grayscale strip of the luminance images in shot order. Only then the colour strip, one vignette per beat on the approved values. Re-run the same lines on the animatic key frames and on the Roblox captures. *Check: B-06..B-09, B-17, B-18.*
7. **Storyboards** (`references/storyboards.md`): one panel per shot through `reference-images` (`storyboard` family), each built on its blocking still as the layout input, reviewed against its brief, the ledger and its first-second read at small size; then a contact sheet in shot order. Only when the owner asks for boards (J024). *Check: B-15.*
8. **Timed animatic** (`references/blender-previs.md`): the greybox or real set, cameras, actor paths, temp sound and temp effect marks from the first cut. First animatic (lengths still UNKNOWN): push rate and properties only (`shotlist.py blender --props-only`), author a `shot:<id>` marker at each cut and a `cue:<id>` marker at each cue event, time the shots, export and `diff --write` (check first that the scene's end frame is the last cut you intend); after that, push normally (`shotlist.py blender`). Cuts sit on events; measure what geometry decides; acting durations stay PROPOSALS. Mark tell, build, beat, peak and result on the key beats; read the shot lengths and beat gaps; on the key beat make two edit takes on the same shots. Review silent, then with sound; change one thing at a time. When the owner asked for an animatic, the owner directs timing on it; otherwise timing is judged on the Roblox capture at G3. Then `stage: locked`. *Check: B-10, B-11, B-16; `check` passes with no UNKNOWN; `diff` shows no drift.*
9. **Brief the crafts** (`references/handoff-briefs.md`): animator (the acting brief and performance sheet per shot; the signature key pose for any still), character rigger (what the acting needs), environment designer (sets, landmarks, the value and light plan per beat), VFX (cue, function, attention priority, occlusion limits), sound (`shotlist.py cues`, each cue's job and emotion, the sync rule), UI (bars, subtitles, skip, protected areas), engineering (data module, endings, readiness list, the confirmed-outcome trigger). One ledger ticket per brief. *Check: P-10, P-11.*
10. **Check the key poses on the captures** (J024: no blocking check-in before polish; the animator builds the final clip once). In your integrated review, at the shot cameras: each key pose's black-fill reads its beat, the line of action is clear, the pushed moments keep their balance, the end pose matches the next shot. One note per problem, with the frame and the intended read. *Check: R-08.*
11. **Assemble in Roblox** (`references/roblox-assembly.md`): choose the runtime; `shotlist.py luau` for the data; engineering builds or extends the player against the contract; check camera ownership, FOV mode, cues, readiness and every ending in Studio yourself (Studio MCP, `studio-mcp` skill; one driver per Studio instance), or through the studio-operator for multi-client and device runs. *Check: R-02..R-06, R-14.*
12. **Review** (`references/review.md`): the §1 four passes (continuity, readability per shot, sound-picture, interaction), each run as its §6 lines; the B lines on the captured key frames, the R lines on the playback, the §2 pass/fail table, the AI defect table, real phones for phone claims. One named problem per pass, the worst first. Fix or ticket every FAIL before the owner sees it. *Check: each line labelled with its evidence level.*
13. **Owner package (G3):** the captured sequence next to the approved beat sheet and shot list (and boards or animatic, if the owner asked for them), the shot-list table; the moment pitched as the player's experience in one or two sentences; what was checked and how (gate / MCP / owner / not verified); the could-not-check list; at least one named weakness with its next step; one recommendation per open decision. Record the owner's words. *Check: R-13; approval names the revision.*

## 4. Craft core (what separates great work from weak work)
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | **One timing truth.** Plan, boards, previs, data module and playback log all carry the same shot ids and revision; timings move only through the shot list file and `diff --write` | O; tool J015-T08 |
| C-02 | **Half-open intervals and exact rates.** A shot is `[start, next-start)`; frames 1-31 at 30 fps are 31 frames = 31/30 s, not 1 s; 29.97 is 30000/1001, kept as a fraction; one frame at 30 fps is 100/3 ms, at 60 fps 50/3 ms | V (derived) |
| C-03 | **Cheapest artifact that answers the question:** greybox thumbnails for options; boards for intent and screen direction; a timed greybox animatic for staging, cuts, occlusion and movement; a few lit frames for contrast and atmosphere. One beautiful render answers none of these well | O |
| C-04 | **Compare like with like:** A/B edits at the same rate, crop, display size and audio revision; one directing change at a time; one silent viewing and one with sound | O |
| C-05 | **A camera spec survives software:** projection, pose, target, focal length + sensor + fit + output aspect, derived vertical and horizontal angles, timing. "40 mm" alone cannot be rebuilt in Roblox; Roblox takes a vertical angle | V |
| C-06 | **Separate controls for path and interest point;** watch roll and screen direction across the whole move; animate the target when attention shifts; avoid a target passing over the camera | V/O |
| C-07 | **Export evaluated poses, not raw keys,** when constraints or parents shape the camera; state units, basis, handedness, origin; test the conversion with an axis-and-landmark scene first | V/O |
| C-08 | **Blender approves staging, not runtime.** Loading, device performance, camera behaviour, UI layout and sync are proven only by Roblox captures; deviations are documented and reviewed | O |
| C-09 | **Readiness before boards:** check cast, set and face kit on day one, ticket what is missing, start with shots whose assets exist; block a greybox where they do not | owner decision |
| C-10 | **Test the acting against the rig** in a render before a beat locks | owner decision |
| C-11 | **One cue sheet keyed to shot ids** for director and sound designer; markers for pose-linked details, the scene timeline for cuts, subtitles and music; temp tracks labelled | O/V |
| C-12 | **One camera owner, one render-step binding, one teardown** that runs for every ending; spare cameras never parented directly to Workspace | V/O |
| C-13 | **Local audio on the local clock:** schedule `AudioPlayer` from the client on `SoundService:GetMixerTime()`; keep the action ids to cancel on skip; never send mixer time across the network | V |
| C-14 | **Prepare distant sets before the cut** (prefetch with a timeout, server-held foci released on every ending); a returned preload is not proof; fallback shot ready | V/O |
| C-15 | **Phone proof comes from a phone.** Desktop or emulator captures do not count; the docs give no universal budget, so the owner sets one | V/O |
| C-16 | **Reduced motion is ours to honour:** read `GuiService.ReducedMotionEnabled` and switch to the calmer camera version; Roblox does not apply it to scripted cameras | V |
| C-17 | **Label every check:** gate-verified, MCP-verified, owner-confirmed, not verified. A number from a script you wrote in this task is "not verified (measured offline: <script path>)", never gate-verified. Never claim a clip was seen, played or timed without a capture or log in this task | `AGENTS.md` §3 |
| C-18 | **Light and dark must separate the subjects in the handoff frame.** A greybox lit for mood can hide the player, the threat or the exit; measure subject vs surround on key frames and fix light or staging before the owner sees it | J015 lead review |
| C-19 | **Options and blocking are greybox stills, small and at equal finish.** A polished option wins for the wrong reason; a ChatGPT board comes after the pick, on the blocking still | O |
| C-20 | **Measure the picture, not the overlay.** Masks come from the same render pass as the frame (occlusion kept); bars and UI are kept out of a spread measure; every bright region that might out-shine the subject is named, then ranked by its p95 on exact masks or tight boxes, never by a box median; a cast check compares like poses at one camera | O |
| C-21 | **Stills ship as layers.** Foreground, midground, background, lights and effects in named, switchable collections; the clean frame passes before effects are added | O |

## 5. Rules (final check)
- No invented numbers (lengths, speeds, tolerances, budgets): measure, or ask the owner; tolerances in `check`, `log-diff` and `look_check.py` need a source. A starting value in these books is a PROPOSAL a check may change.
- Server authority: no reward, progression, boss result, teleport or trade depends on a cinematic finishing; an outcome sequence starts on the confirmed result.
- Code lives where the game profile says (default files mode): the director writes data and contracts, never game code through Studio MCP; the player code is engineering's.
- Images through `reference-images` only, with the art bible's locks; no franchise characters, logos or brands; no attachment whose source forbids AI use.
- Video uploads, voice and music licences, and any spend are owner actions.
- Never open or save a `.blend` the owner has open; work on copies or new files; save explicitly after a push.
- Generated files (`.luau` from the tool, `.claude/` copies) are never edited by hand.
- Platform rules for story content: `platform-policy`; flash and shake safety: `vfx-design`.

## 6. Self-check before returning
The lines, their inputs and the image budget: `references/review.md` §6-7. Report each as PASS, MEASURED, not verified or n/a, with evidence.
- [ ] Readiness table done; missing assets ticketed; budget and stop criteria stated.
- [ ] Beat sheet approved; options contact sheets and the recorded pick (P-04).
- [ ] Shot list file at the right stage; `shotlist.py check` exit 0; picture plan per shot.
- [ ] B-01..B-09, B-17, B-18 measured on the Roblox key frames (strips only when the owner asked for them).
- [ ] (Only when the owner asked for boards) boards reviewed panel by panel and as a sequence; contact sheet saved with briefs and the shot-list revision.
- [ ] Shot lengths and beat parts in the shot list; (only when the owner asked for an animatic) animatic timed; rhythm read; two edit takes of the key beat and the owner's pick recorded; `diff` no drift; owner timing decision recorded.
- [ ] Every craft brief: fixed values with sources, open craft, runnable checks, skills named; marker list and sync rule sent.
- [ ] Roblox: one camera owner, FOV mode set, cues from the data module, readiness checks, every ending captured with teardown evidence; `log-diff` with no planned id missing.
- [ ] Review: the four passes, run as the §6 lines, and the §2 table filled with evidence levels; phone claims from a phone; images looked at counted against the brief's cap.
- [ ] Owner package: captures next to the plan, the pitch, what was and was not checked, one named weakness, one recommendation per open decision.

Project overlay: if `knowledge/overlays/film-craft.md` exists, read it after this file; it wins for this game.
