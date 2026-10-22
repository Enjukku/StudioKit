> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Source: N3 RV-00..18 (pass/fail review), DF-01..08 (AI sequence defects), CC-01..04 (change control), PM-07; N2 CP-01..17 (captures). All OPINION: project acceptance checks, not industry benchmarks. Revised by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1b points to the plan and build lines; §3 new defects; §6 self-review lines by stage; §7 light checks and image budget). Repair 3: R-10 points to the studio's flash counter; B-06 spread; §7 cut order completed.

# Review: judging the captured sequence

PASS needs evidence in the current build or an explicit owner decision. FAIL includes an unresolved critical UNKNOWN at a stage that depends on it. NOT APPLICABLE needs a reason (N3 RV-00). Label every check: gate-verified / MCP-verified / owner-confirmed / not verified (`AGENTS.md` §3).

## 1. Four passes, separately (N3 PM-07)
1. **Continuity:** positions, travel direction, eyelines, props, light direction, action phase at each cut, against the continuity ledger.
2. **Emotional readability:** per shot, say in one sentence what the player should now know or feel, then watch the clip and write what it actually gives. Watch once silent (does the picture tell it?) and once with sound.
3. **Sound-picture:** each cue against its planned time (`shotlist.py log-diff`), its relationship (warning, sync, delay), dialogue intelligibility.
4. **Interaction:** every ending into immediate play, on the target devices.

You see stills and logs, so each pass runs as §6 lines: continuity = B-02 and P-08 on the captures; readability = each shot's first-second read (P-03) written beside its R-09 capture, then R-09's numbers, R-10 for sound off; sound-picture = R-04 (audible sync and intelligibility: the owner on the device capture); interaction = R-02, R-05, R-07. Watching at normal speed is the owner's part at the gate.

Record each defect with build, device, viewport, shot id, observed event, expected behaviour and a capture. Separate a creative disagreement from a reproducible fault.

## 1b. Planning stage (before any Roblox capture)
The animatic can pass: beat purpose, shot purpose, geography (screen direction across cuts), camera movement reasons, timing evidence (`shotlist.py diff` no drift), storyboard continuity, the phone proxy below, and the owner's timing. Every runtime row (performance on a device, loading, completion, skip, interruption, multiplayer, UI on layouts, avatar range) is "held: needs Roblox" until step 11 (`film-craft` §3) (J015 G2 gaps G7).

The plan and build lines (§6 P and B) run here; the phone proxy is B-03, B-04 and B-06.

**Phone proxy (offline, before a phone exists):** for each key frame, check the key subjects (player, threat, goal, exit) stay inside the narrowest supported display at the fixed vertical FOV (4:3 inside 16:9 when the game profile gives no narrower one); record each key subject's screen height; measure subject vs surround value with `tools/art/look_check.py value` on the frame. Label results "not verified (measured offline)"; only a phone capture is phone proof (J015 G2 gaps G8).

## 2. Pass / fail table (N3 RV-01..18)
| Check | Pass evidence | Fail |
| --- | --- | --- |
| Beat purpose | owner-approved before/after knowledge and emotional intent | the sequence exists only to look cinematic |
| Shot purpose | every shot states its new information or performance change | redundant coverage with no defended purpose |
| Geography | captures keep intended relationships and screen direction | an unintended reversal makes the action ambiguous |
| Performance | intended action and reaction visible in the final framing | key acting hidden, cropped or ambiguous |
| Camera movement | each move has a documented revealing or relational purpose | decorative motion that weakens the beat |
| Timing evidence | final shot and cue times match the capture | placeholder values presented as measured |
| Sound relationship | cues happen as intended in playback | accidental desync or masked dialogue |
| Storyboard continuity | accepted panels match current ids and the ledger | beautiful but contradictory panels still marked approved |
| Previs agreement | runtime deviations documented and reviewed | Blender approval treated as runtime proof |
| Avatar variation | supported avatar range keeps the essential action | works only for one avatar |
| UI readability | subtitles and skip checked on target layouts | text, controls or bars cover essential action |
| Loading | required content present before it is needed | a reveal points at missing or late content |
| Completion | game state and camera ownership restored | player stuck or camera still owned |
| Skip | approved exit state reached, cues and temporary effects cleaned | skip only hides UI while the scene keeps acting |
| Interruption | death, respawn, leaving or a newer scene handled as specified | an abandoned scene leaves state behind |
| Multiplayer | local presentation and shared consequences agree with design | one client's cinematic changes another player's state |
| Device performance | target-device captures meet owner-approved budgets | emulator or desktop capture used as phone proof |
| Owner approval | current revision and open risks explicitly accepted | approval belongs to an older revision |

## 3. Common AI sequence defects (N3 DF-01..08)
| Defect | Inspect | Revision hypothesis |
| --- | --- | --- |
| Same size, centred subject in every shot | ordered shot records and thumbnails side by side | change emphasis only where the story information changes |
| Arbitrary movement | read each move's reason without watching | remove moves whose changing view reveals nothing needed |
| Emotion named but not visible | find the action or reaction that carries it | stage a readable change of intention or attention |
| Cuts reverse geography by accident | eyeline and screen-direction ledger entries | reblock, add an orienting view, or change the cut |
| Repeated information | state the new information per beat | merge redundant beats; note the emotional cost |
| Sound and picture disagree by accident | cue intent vs captured playback | fix cue timing or document an intended offset |
| Boards look coherent but previs cannot join them | spatial relationships across shots | revise panel geometry rather than force an impossible move |
| Final frame strands the player | run each ending into play | reframe and restore the play state |
| Every shot lit evenly; nothing leads the eye | B-06 ranks and the luminance strip | calm the surround, put the brightest area on the subject |
| Metronomic cuts (every shot the same length) | B-10 shot lengths | cut on events; let decisions hold and surprises cut short |
| Smoke, sparks and glow added before the frame worked | B-08 clean frame | remove effects, fix blocking and value, add effects back last |
| One polished option and two sketches | P-04 finish | bring all options to the same low finish, then pick |
| Peaks of picture, flash and sound on different frames | B-11 and R-04 | key all three from one marker |

A script can flag missing ids, absent cues and inconsistent records (`shotlist.py check`, `log-diff`). It cannot say whether a performance moves anyone or a cut is right (N3 DF-00).

## 4. Captures to take (N2 CP-01..15)
Normal finish; skip during each major cue; repeated skip; skip while loading; missing or denied audio; missing streamed actor; fast distant cut; low graphics quality; resized and portrait viewport; large text; reduced motion; touch and gamepad; respawn mid-scene; two clients; late join. Record them with Studio MCP (`studio-mcp` skill), or ask the studio-operator for multi-client runs; every capture names its `studio_id`, build and device. Phone results need a phone: a desktop or emulator capture is not phone proof.

## 5. Change control (N3 CC-01..04)
- Present the current sequence, its intended effect, the strongest open issue and one proposed revision; keep the approved baseline.
- After a timing or staging change, list the affected animation, sound, VFX, subtitle and gameplay cues (`shotlist.py diff` shows the shots whose windows moved).
- A camera change can invalidate a performance review even when no animation file changed: recheck the assembled result, not each asset alone.
- Approval belongs to one revision; a new revision needs its own.


## 6. Self-review lines by stage
Run the lines of the stage you hand on; re-run earlier B lines when a later stage changes the picture. Each line is PASS, MEASURED (a number with no tolerance from a source), not verified (the input cannot show it) or n/a, with its evidence path. Inputs: **doc** = the job's documents; **num** = tool numbers for every case; **img N** = at most N images looked at (plus any frame whose number fails); **owner** = the owner at the named gate. Commands and their traps: `references/blender-previs.md` §7 and `references/shot-list-format.md` §2.

### P. Plan (before boards and the animatic)
| ID | Look for | Input |
| --- | --- | --- |
| P-01 | The beat contract has problem, constraints, premise (one sentence), hook, target experience, sell list (2-4), the five items, budget and stop criteria; the owner's decision id is recorded | doc: beat sheet |
| P-02 | The camera mode has a one-line reason the interruption is worth it | doc |
| P-03 | Every shot row has purpose, first-second read, read order (at most three reads), value key, emotion change, transition reason, and for a camera height chosen for status its intended feeling; no two consecutive shots share size and centred subject without a reason | doc: shot table + picture plan |
| P-04 | A research board (our approved images first, real-world reference, one outside-games source); 2-3 approaches for the key beat, each with its own hook, one non-obvious, at equal finish (same camera height, size, proxies, render look), at phone size; for a single still, 4-5 small framings on one sheet; the pick names its goal question and why each other option lost; sheets counted against the budget | doc + img 3 (one sheet per approach) |
| P-05 | Every beat has a changing event, a carried question and something that resists the character; the intensity line rises to one climax; no beat duplicates another's information | doc: beat sheet |
| P-06 | One row per ending with view, state and first safe action; skip keeps the essential information; every outcome sequence starts on a server-confirmed event; a paid random reveal follows the game-designer's reveal rules | doc: endings table |
| P-07 | Stage dates: blocking strip, then value strip, then colour strip, boards, effects; nothing later polished while an earlier stage is open | doc: job folder dates |
| P-08 | Continuity ledger: positions, travel direction, eyelines, light direction, props, action phase at each cut | doc |
| P-09 | One conventions table for the sequence (story colours, light directions such as "villains underlit", camera grammar, the motion material of title cards and graphic transitions) that matches earlier cutscenes of the game and the art bible | doc |
| P-10 | Every acting row has belief, stimulus, decision, subtext, 2-4 adjectives with their pose change, the key poses, the pushed moments, the end pose; each physical beat tested on the rig and face kit | doc: performance sheets + rig render |
| P-11 | Every craft brief has fixed values with sources, the craft left open, runnable checks and skills; each cue names its job and emotion; VFX and sound got the marker list, the stage names and the sync rule; the environment designer got the value plan and the story facts the place must show; the animator was asked for the signature key pose of any still | doc: briefs |
| P-12 | Platform limits at the top of the beat list; no number without a measurement, owner decision or PROPOSAL label | doc |

### B. Build (blocking strip, value pass, boards, animatic key frames)
| ID | Look for | Input |
| --- | --- | --- |
| B-01 | Every greybox has a player-sized reference and the smallest and tallest avatar; every shot has a key-frame still at its camera; geography matches the overhead map | img 1 (the blocking strip) |
| B-02 | Screen direction and eyelines across each cut match the ledger | img 1 (the same strip) |
| B-03 | No key subject's box (mask or black-fill JSON) intersects the bars, subtitle zone, skip control or, on the handoff frame, the HUD, at the narrowest supported display | num |
| B-04 | Each key subject's height in px at phone size (`look_check.py thumb --size`) is recorded and meets the brief's minimum, or is MEASURED when no minimum has a source | num |
| B-05 | Per-group black-fill: the group outline reads as the beat, one line of action, the source of power visible in threat shots; scale ratios (giant to heroes) from the groups' box heights as planned, the bigger threat measurably bigger | num + img 3 (reveal, turn, handoff) |
| B-06 | The subject's subject/ring ratio and its p5-p95 spread wider than its ring's (both from its `--mask` run: the subject owns the widest value range), and the subject first when the named regions are ranked by each region's **p95**, never by `rank_by_median` (regions, boxes and the rank: `references/blender-previs.md` §7 "Rank the bright regions"); every lamp, sky patch or white prop that looks brighter in the luminance image is named, and in a threat shot the source of power; the dark foreground region ranks below the midground subject; before a planned surprise, the surprise's region ranks low. A planned silhouette (written in the picture plan: subject dark against the brightest area) passes instead when the region ranked first is that backdrop, the subject's box lies inside the backdrop's box (box arithmetic), and the subject's p50 is below its ring's, with the subject/ring ratio recorded | num |
| B-07 | Picture-area p5-p95 spread per key frame (a box on the picture, bars excluded; with no bars, read the `whole` distribution: a box over 98 % of the frame is refused) rises with the beat's planned intensity, calm beats measurably narrower than the climax; the far band's spread is narrower than the near band's | num |
| B-08 | The clean frame (effects hidden) passes B-05 and B-06; with effects on, the subject still ranks first | num |
| B-09 | One motivated key direction per shot, matching the ledger and the conventions table (for example the villain lit from below); a rim where a figure meets a similar-value background; on the key beat, 2-3 light variants measured and the choice recorded | num + img 1 (variant strip) |
| B-10 | Shot lengths (`shotlist.py check` output) and beat gaps are not all equal; every long hold has something developing; one climax. The tool gives no cadence warning: read the numbers | num |
| B-11 | Key beats have tell, build, beat, peak and result frames labelled from the marker export; each result starts after its cause; the build rises; one peak frame shared by the picture event, the VFX mark and the sound cue; a giant's beats and camera moves are slower than the cast's; camera moves ease in and out unless the shot wants mechanical motion (the camera f-curve interpolation read by Python) | num |
| B-12 | Cast, palette and place match the game: each cast member in the scene is the released in-game model and rig (its file or Roblox asset ids equal the asset record's lineage and the rig sheet's revision; in Studio, read back through the MCP); a silhouette compare, where wanted, renders the cutscene rig in the anchor's pose at the anchor's camera and compares that pair (`silhouette --compare`; an acting pose at a shot camera against a sheet pose measures the pose, not the cast); `palette --roles` against the art bible's colour roles; the planned story facts are visible in the set | doc + num + img 1 |
| B-13 | In crowd shots no two neighbouring extras share pose and frame; nothing that carries meaning (a uniform, a team colour) varies | img 1 |
| B-14 | Stills: inside every planned crop with calm room for the title; the featured thing the largest readable element; 2-3 flow lines through the focal point; foreground, midground, background, lights and effects in named switchable groups; the pose matches the clip's key frame (`silhouette --compare` of two black-fills, both rendered from the still's camera) | num + img 1 |
| B-15 | Boards: the §3 storyboard checks pass, each panel's first-second read holds at small size, and approval is asked for staging and order, not finish | img: the contact sheet |
| B-16 | `shotlist.py diff` shows no drift; the animatic manifest names the shot-list, board and audio revisions; temp sound and effect marks were in from the first cut; the key beat has two edit takes on the same shots and the owner's pick is recorded; the owner watched the playable animatic, timed it, and heard the key event solo and in the full mix | num + owner (G2) |
| B-17 | Balance: dark and bright masses sit where planned on the reveal frame and on every still (manual, on the luminance image: no tool mode yet) | img: the value strip |
| B-18 | Flow: the main lines of the key frame (set lines, cast shadows, gaze, motion paths) point to the primary; during a build motion converges on it (the actor and emitter paths read from the Blender data move toward the focus, or 2-3 frames of the build where no path data exists); after the peak the region ranked first by p95 changes from the cause to the result (the B-06 rank on the frame before and the frame after the peak); small accents are smaller and lower in contrast than the focus | num + img: the value strip (+ 2-3 build frames where no path data) |

### R. Roblox (captures and playback)
| ID | Look for | Input |
| --- | --- | --- |
| R-01 | Captures come from Studio through the MCP at the target viewport; every phone claim comes from a device capture | doc |
| R-02 | Camera ownership, `CameraType`, `CameraSubject`, FOV and FOV mode restored after every ending (state read back through the MCP) | num |
| R-03 | `FieldOfViewMode` is `Vertical` and each shot's FOV matches the shot list | num |
| R-04 | `shotlist.py log-diff` without `--tol-ms` (its tolerance is symmetric and passes early cues; a sourced `--tol-ms` may judge cut times only): "planned, not logged" is empty (animation markers appear as "logged, not planned": expected); each sound cue with `sync: locked` minus its picture event, both from the log, read with its sign against the sync rule (`film-direction/references/beats-and-timing.md` §4); a planned lead or delay (a J cut, a warning before a reveal) has its offset written in the cue's `note` and is read with the same window around that offset. Logged times are scheduled times; audible sync is not verified without a device capture | num |
| R-05 | Skip, repeated skip, replay and a repeat trigger each give one result: no replayed cues, no repeated rewards; a sequence that plays every round stays short over repeated triggers | num + img 1 per ending |
| R-06 | Readiness: a missing actor or late set takes the fallback; nothing waits on an empty mark | num |
| R-07 | The handoff capture at the game camera on the phone viewport names the threat, the goal and the first safe action, with the HUD on | img 1 |
| R-08 | Animator blocking check-in: at the shot cameras, each key pose's black-fill reads its beat with one line of action; pushed poses keep their centre of gravity over the support; a comic beat reads from the whole body; eyes close through fast turns and widen on a shock where the face kit allows; a jump apex in a key shot has a pose; end poses match the next shot | img: the animator's key-pose strip |
| R-09 | Captured key frames re-run B-06 and B-07 with everything on (effects, other players, HUD), each region's box from the MCP projection or drawn by hand and recorded (`references/blender-previs.md` §7), each box checked against the capture you look at: it holds its region and no brighter patch; each sell-list item is pointed to in a named captured key frame (a missing item fails); `palette --roles` against the art bible | num + img: one capture per shot at its key moment |
| R-10 | Grayscale and reduced-motion captures of the reveal and handoff frames still name every essential fact; flashes: on the animatic rendered at the shot-list rate, the large-area flash count per rolling second (the studio's one flash counter, `vfx-craft/references/measure.md` §6, run on frames exported as `references/blender-previs.md` §7 "Flash count" says; both counts read as the counter's known-limits note says, never the over-10 % count alone with rain or a pan; not verified (measured offline)) within the `vfx-design` flash rule, with every effect mark on; in Roblox "not verified" without a device recording; each shake, punch or whip is listed with its importance and its reduced version; the play-critical beat reads with sound off | img 4 + num |
| R-11 | After `stage: locked`, no drift without a logged revision; the affected cues listed and the consumers told | num |
| R-12 | Every finding names shot, intended read, observed read, layer and one fix (a visual fix as a marked capture); a weak read is fixed with contrast, not detail; one problem per pass, the worst first; the other layers re-checked after a fix; review questions name the goal; a received note that carries a solution is first restated as the problem behind it; the self-review included a mirrored and a grayscale look | doc |
| R-13 | The hand-back pitches the moment as the player's experience in one or two sentences, lists each stop criterion with its evidence, the budget used, images looked at, the could-not-check list and at least one named weakness with its next step | doc |
| R-14 | In a test build the server rejects the result (engineering's hook): no outcome sequence plays | num (Output log) |

## 7. Light checks and the image budget
- Numbers for every key frame and every run (`look_check.py`, `shotlist.py`); images only where a number fails and for the few frames the §6 lines name (at most: 3 options sheets, 1 blocking strip, 1 value strip, 1 light-variant strip, 3 black-fills, 1 crowd and 1 cast-comparison still, 1 still for marketing, 1 board contact sheet, one capture per shot at its key moment, the handoff and the first playable frame of each ending, 4 access captures).
- **The brief's image cap wins** over these maxima. Cut in this order until it fits: the light-variant strip (numbers only), the option sheets to one combined sheet, the black-fills to the reveal frame, the ending captures to finish and skip; then the per-shot captures become numbers only (R-09 boxes from the MCP projection), keeping the reveal and the handoff frame as images. Still over the cap: keep the reveal, the handoff and the board contact sheet, and drop the other images from the end of the maxima list backward. Every line whose image was cut is "not verified (image budget)" and goes in the could-not-check list.
- Plan-stage images (options, blocking, value strips) are making, not checking; they are counted and reported separately. A cap in a brief counts the images you look at; generated boards and plan-stage renders are reported beside it unless the brief says otherwise.
- The playable animatic and the device capture with sound are for the owner to watch at the gate; you do not inspect their frames one by one.
- Say what each input can prove: a still shows a pose and a composition, not timing; a marker export or playback log at a known rate shows timing; sound sync needs a device capture with audio. A line whose input cannot show it is "not verified", never PASS; end with a could-not-check list.
- Report how many renders were made and how many images were looked at.
