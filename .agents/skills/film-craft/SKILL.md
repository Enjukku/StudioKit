---
name: film-craft
description: The how for a Roblox cinematic - beat sheet, shot list (tools/film/shotlist.py), storyboards, timed Blender animatic, Roblox assembly (camera, cues, skip, endings), capture review. Use for "storyboard this", "make the animatic", "time the cutscene", "put the cutscene in the game", "the cues are late", "skip breaks it". Read film-direction first (what and why).
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J015 from the owner's research paper (`knowledge/reference/film/01..03`), the first game's opening-film records (`04`) and three fact-checks (`fact-check-roblox-runtime.md`, `fact-check-blender-images.md`, `fact-check-craft-sources.md`, all 2026-10-21). Note ids: N1..N4 as in `film-direction`; FR = Roblox fact-check, FB = Blender/images fact-check.

# Film craft: from plan to a proven cutscene

## 1. When this skill starts
`film-direction` has produced (or is producing with you) the beat contract, the camera mode and the shot design. Before step 1 you need: the owner's brief; the game's art bible (`knowledge/design/art-bible.md`, or the kit template for a test); the game profile (devices, camera style, test place). Missing facts that change the result: state an assumption and continue.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The shot list file, its fields and the tool commands | `references/shot-list-format.md`; fields for people: `templates/film/shot-list.md` |
| Beat sheet and gameplay state sheet | `templates/jobs/beat-sheet.md` |
| Storyboard panels with ChatGPT, their review, when Blender stills take over | `references/storyboards.md`; brief: `templates/film/storyboard-brief.md`; tool: `reference-images` skill |
| Blender previs: version, camera spec, lens → Roblox FOV, markers, frame rates, review artifacts, camera export | `references/blender-previs.md` |
| What to brief each craft, fixed vs open, an example brief | `references/handoff-briefs.md` |
| Roblox: which runtime, camera, cues and clocks, effects, streaming, UI and input, endings and teardown | `references/roblox-assembly.md` |
| Judging captures: four passes, pass/fail table, AI defects, change control | `references/review.md` |
| Driving Studio for checks and captures | `studio-mcp` skill (you, or the studio-operator for multi-client runs) |
| Phone performance measurement | `performance` skill |
| Value contrast and small-size reads of key frames | `tools/art/look_check.py` (`value`, `thumb`; `art-review` skill) |
| Play camera, supported displays, cinematic rate | `knowledge/design/game-profile.md` |

## 3. Steps
1. **Restate and check readiness.** Restate goal, feeling, fixed, open, checks. List every character, set, prop, rig feature (face kit, eye target, mouth shapes, limb range) and sound the shot design needs; mark each ready / partial / missing; missing items become tickets now (N4 X-01, R-04..R-09). *Check: readiness table in the job folder.*
2. **Beat sheet** from `templates/jobs/beat-sheet.md`: beat contract, beats as state changes, gameplay state sheet, endings table. Owner approves the beat contract (G1 for M/L jobs). *Check: owner decision id recorded.*
3. **Shot list file** at `stage: plan` (`references/shot-list-format.md`): every shot with the 10 fields, purpose, continuity; cues with ids; lengths UNKNOWN or event-bounded. `shotlist.py check` passes; `table` and the continuity ledger go to the job folder. *Check: exit 0; open items listed.*
4. **Colour strip and boards** (`references/storyboards.md`): blocking map; if the cast or set is missing, block a greybox first (step 5's proxies and cameras) and attach each shot's greybox still as the layout input; then one panel per shot through `reference-images` (`storyboard` family), each reviewed against its brief and the ledger, then a contact sheet in shot order. For an L job this is the cheap first sample (G2). *Check: every panel passed the continuity table or was revised openly.*
5. **Blender previs** (`references/blender-previs.md`): proxies at true scale, landmarks, cameras `CAM_<id>` with the recorded camera spec, actor paths, temp sound. First animatic (lengths still UNKNOWN): push rate and properties only (`shotlist.py blender --props-only`), author a `shot:<id>` marker at each cut and a `cue:<id>` marker at each cue event, time the shots, export and `diff --write` (check first that the scene's end frame is the last cut you intend). After that, push normally (`shotlist.py blender`). Cuts sit on events; acting durations inside a shot are PROPOSALS until the owner directs timing; measure what geometry decides (contact, arrival, line of sight). Review silent, then with sound; change one thing at a time (reveal order, a cut point, distance, move vs static, a sound entrance). Owner directs timing on the animatic; then `stage: locked`. *Check: `check` passes with no UNKNOWN; `diff` shows no drift; the animatic file names the shot-list revision.*
6. **Brief the crafts** (`references/handoff-briefs.md`): animator (acting per shot), character rigger (what the acting needs), environment designer (sets, landmarks, light per beat), VFX (cue, function, occlusion limits), sound (`shotlist.py cues` + relationships), UI (bars, subtitles, skip), engineering (data module, endings, readiness list). One ledger ticket per brief. *Check: every brief has fixed values with sources and runnable checks.*
7. **Assemble in Roblox** (`references/roblox-assembly.md`): choose the runtime; `shotlist.py luau` for the data; engineering builds or extends the player against the contract (J015-D7); the director checks camera ownership, FOV mode, cues, readiness and every ending in Studio itself (Studio MCP, `studio-mcp` skill; one driver per Studio instance), or through the studio-operator for multi-client and device runs. *Check: `log-diff` of a playback log against the plan; every ending captured.*
8. **Review** (`references/review.md`): at the planning stage, the rows an animatic can pass, plus the phone proxy (safe frame at the narrowest display, key-subject screen size and value contrast on key frames with `tools/art/look_check.py`); after the Roblox step, the captures: four passes (continuity, emotional readability, sound-picture, interaction), the pass/fail table, the AI defect table, real phones for phone claims. Fix or ticket every FAIL before the owner sees it. *Check: each row labelled with its evidence level.*
9. **Owner package (G3):** the captured sequence next to the approved animatic and boards, the shot-list table, what was checked and how (gate / MCP / owner / not verified), open risks, one recommendation per open decision. Record the owner's words. *Check: approval names the revision.*

## 4. Craft core (what separates great work from weak work)
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | **One timing truth.** Plan, boards, previs, data module and playback log all carry the same shot ids and revision; timings move only through the shot list file and `diff --write` | O: N3 PM-03, DN-07; tool J015-T08 |
| C-02 | **Half-open intervals and exact rates.** A shot is `[start, next-start)`; frames 1-31 at 30 fps are 31 frames = 31/30 s, not 1 s; 29.97 is 30000/1001, kept as a fraction; one frame at 30 fps is 100/3 ms, at 60 fps 50/3 ms | V (derived): N2 BL-30..34; FB |
| C-03 | **Cheapest artifact that answers the question:** boards for intent and screen direction; timed greybox playblast for staging, cuts, occlusion and movement; a few lit frames for contrast and atmosphere. One beautiful render answers none of these well | O: N2 BL-36 |
| C-04 | **Compare like with like:** A/B edits at the same rate, crop, display size and audio revision; one directing change at a time; one silent viewing and one with sound | O: N2 BL-37, BL-38 |
| C-05 | **A camera spec survives software:** projection, pose, target, focal length + sensor + fit + output aspect, derived vertical and horizontal angles, timing. "40 mm" alone cannot be rebuilt in Roblox; Roblox takes a vertical angle | V: N2 BL-07..13; FR FC-22..24 |
| C-06 | **Separate controls for path and interest point;** watch roll and screen direction across the whole move; animate the target when attention shifts; avoid a target passing over the camera (Track To roll is unstable there) | V: N2 BL-15, BL-16 (B07); O: BL-17 |
| C-07 | **Export evaluated poses, not raw keys,** when constraints or parents shape the camera; state units, basis, handedness, origin; test the conversion with an axis-and-landmark scene before trusting it | V: N2 BL-21 (B09); O: BL-22, BL-23 |
| C-08 | **Blender approves staging, not runtime.** Loading, device performance, camera behaviour, UI layout and sync are proven only by Roblox captures; deviations are documented and reviewed | O: N2 BL-38, N3 PM-07, RV-09 |
| C-09 | **Readiness before boards:** the first game's boards never started because cast, set and face kit were missing; check on day one, ticket what is missing, start boards with shots whose assets exist | N4 X-01, P-07 (owner decision), P-10 |
| C-10 | **Test the acting against the rig** in a render before a beat locks; the owner cut a beat the character's proportions could not show | N4 R-09 (owner decision), R-01..R-08 |
| C-11 | **One cue sheet keyed to shot ids** for director and sound designer; markers for pose-linked details, the scene timeline for cuts, subtitles and music; temp tracks labelled | O: N1 SN-06; N2 RT-24; FR FC-27 |
| C-12 | **One camera owner, one render-step binding, one teardown** that runs for every ending; spare cameras never parented directly to Workspace | FR FC-20, FC-25; O: N2 TC-01..07 |
| C-13 | **Local audio on the local clock:** schedule `AudioPlayer` from the client on `SoundService:GetMixerTime()`; keep the action ids to cancel on skip; never send mixer time across the network | FR FC-32, FC-33 |
| C-14 | **Prepare distant sets before the cut** (prefetch with a timeout, server-held foci released on every ending); a returned preload is not proof; fallback shot ready | FR FC-39..41; O: N2 RT-49..51 |
| C-15 | **Phone proof comes from a phone.** Desktop or emulator captures do not count; the docs give no universal budget, so the owner sets one | FR FC-38; O: N3 RV-17 |
| C-16 | **Reduced motion is ours to honour:** read `GuiService.ReducedMotionEnabled` and switch to the calmer camera version; Roblox does not apply it to scripted cameras | FR FC-44 |
| C-17 | **Label every check:** gate-verified, MCP-verified, owner-confirmed, not verified. A number from a script you wrote in this task (Blender projections, frame measurements) is "not verified (measured offline: <script path>)", never gate-verified. Never claim a clip was seen, played or timed without a capture or log in this task | `AGENTS.md` §3; J015 G2 gaps G6 |
| C-18 | **Light and dark must separate the subjects in the handoff frame.** A greybox lit for mood can hide the player, the threat or the exit; measure subject vs surround value on key frames (`look_check.py value`) and fix light or staging before the owner sees it | J015 G2 gaps (lead review: shot E too dark to read) |

## 5. Rules (final check)
- No invented numbers (lengths, speeds, tolerances, budgets): measure, or ask the owner; tolerances in `check` and `log-diff` need a source.
- Server authority: no reward, progression, boss result, teleport or trade depends on a cinematic finishing (FR FC-49).
- Code lives where the game profile says (default files mode): the director writes data and contracts, never game code through Studio MCP; the player code is engineering's (J015-D7).
- Images through `reference-images` only, with the art bible's locks; no franchise characters, logos or brands; no attachment whose source forbids AI use.
- Video uploads, voice and music licences, and any spend are owner actions.
- Never open or save a `.blend` the owner has open; work on copies or new files; save explicitly after a push.
- Generated files (`.luau` from the tool, `.claude/` copies) are never edited by hand.
- Platform rules for story content: `platform-policy`; flash and shake safety: `vfx-design`.

## 6. Self-check before returning
- [ ] Readiness table done; missing assets ticketed.
- [ ] Beat sheet approved; shot list file at the right stage; `shotlist.py check` exit 0.
- [ ] Boards reviewed panel by panel and as a sequence; contact sheet saved with briefs and the shot-list revision.
- [ ] Animatic timed; `diff` no drift; owner timing decision recorded.
- [ ] Every craft brief: fixed values with sources, open craft, runnable checks, skills named.
- [ ] Roblox: one camera owner, FOV mode set, cues from the data module, readiness checks, every ending captured with teardown evidence.
- [ ] Review: four passes, pass/fail table filled with evidence levels; phone claims from a phone.
- [ ] Owner package: captures next to the plan, what was and was not checked, one recommendation per open decision.

Project overlay: if `knowledge/overlays/film-craft.md` exists, read it after this file; it wins for this game.
