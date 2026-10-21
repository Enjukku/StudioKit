> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Source: N3 RV-00..18 (pass/fail review), DF-01..08 (AI sequence defects), CC-01..04 (change control), PM-07; N2 CP-01..17 (captures). All OPINION: project acceptance checks, not industry benchmarks.

# Review: judging the captured sequence

PASS needs evidence in the current build or an explicit owner decision. FAIL includes an unresolved critical UNKNOWN at a stage that depends on it. NOT APPLICABLE needs a reason (N3 RV-00). Label every check: gate-verified / MCP-verified / owner-confirmed / not verified (`AGENTS.md` §3).

## 1. Four passes, separately (N3 PM-07)
1. **Continuity:** positions, travel direction, eyelines, props, light direction, action phase at each cut, against the continuity ledger.
2. **Emotional readability:** per shot, say in one sentence what the player should now know or feel, then watch the clip and write what it actually gives. Watch once silent (does the picture tell it?) and once with sound.
3. **Sound-picture:** each cue against its planned time (`shotlist.py log-diff`), its relationship (warning, sync, delay), dialogue intelligibility.
4. **Interaction:** every ending into immediate play, on the target devices.

Record each defect with build, device, viewport, shot id, observed event, expected behaviour and a capture. Separate a creative disagreement from a reproducible fault.

## 1b. Planning stage (before any Roblox capture)
The animatic can pass: beat purpose, shot purpose, geography (screen direction across cuts), camera movement reasons, timing evidence (`shotlist.py diff` no drift), storyboard continuity, the phone proxy below, and the owner's timing. Every runtime row (performance on a device, loading, completion, skip, interruption, multiplayer, UI on layouts, avatar range) is "held: needs Roblox" until step 7 (J015 G2 gaps G7).

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

A script can flag missing ids, absent cues and inconsistent records (`shotlist.py check`, `log-diff`). It cannot say whether a performance moves anyone or a cut is right (N3 DF-00).

## 4. Captures to take (N2 CP-01..15)
Normal finish; skip during each major cue; repeated skip; skip while loading; missing or denied audio; missing streamed actor; fast distant cut; low graphics quality; resized and portrait viewport; large text; reduced motion; touch and gamepad; respawn mid-scene; two clients; late join. Record them with Studio MCP (`studio-mcp` skill), or ask the studio-operator for multi-client runs; every capture names its `studio_id`, build and device. Phone results need a phone: a desktop or emulator capture is not phone proof.

## 5. Change control (N3 CC-01..04)
- Present the current sequence, its intended effect, the strongest open issue and one proposed revision; keep the approved baseline.
- After a timing or staging change, list the affected animation, sound, VFX, subtitle and gameplay cues (`shotlist.py diff` shows the shots whose windows moved).
- A camera change can invalidate a performance review even when no animation file changed: recheck the assembled result, not each asset alone.
- Approval belongs to one revision; a new revision needs its own.
