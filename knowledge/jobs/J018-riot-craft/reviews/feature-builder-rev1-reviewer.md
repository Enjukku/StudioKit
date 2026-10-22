---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer feature-builder · claude-opus-5-5 · high · 2026-10-22

# Review: feature-builder books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/feature-builder.md (body) + .agents/skills/engineering-craft/ (SKILL.md, references/ incl. new presentation.md; shared with architect, qa-lead, reviewer) + .agents/skills/ui-basics/ (SKILL.md, references/; evals/ not changed), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer feature-builder (opus, high)
looked_at_first: [
  all eight book files read in full as they are now, then git diff df13ff4 for each (every removed line walked),
  knowledge/reference/craft/riot/matrix.md feature-bu column (script: 52 ids) and the principle, apply, check and roblox_fit lines of all 52 findings; universal-principles.md (index, applies-to lines, engineering lines of UP-01..UP-20),
  roblox-creator-docs: animation/events.md:10-14, 45-75; AnimationTrack.yaml:318-324; ParticleEmitter.yaml:502-511, 962-968; effects/highlighting.md:35-37; ColorCorrectionEffect.yaml:20-28; GuiService.yaml:222-268; Workspace.yaml:1522-1530; Camera.yaml:1252-1314; NetworkSettings.yaml:119-296 (security lines); studio/network-simulator.md; ui/list-flex-layouts.md:14-16,
  partner books for V4 and V10: platform-policy SKILL.md P-01, P-02 and references/rules.md § A; architecture/references/presentation-contract.md §2-§4; code-review/references/presentation.md PT-08, S6; testing/references/player-facing.md §3; vfx-craft/references/measure.md §1; animation-craft/references/roblox-playback.md §9; roles animator, vfx-designer, reviewer, qa-lead; sound-design S-133, R-40, R-44, roblox-audio.md §G; studio-mcp C-04, C-05,
  my own V3 runs (scratchpad fbrev/): look_check.py contrast on a synthetic 1280 x 720 in-scene capture (white text on a 60 %-transparent navy panel; dark text on a 60 %-transparent light panel over sky and grass); the literals grep of presentation.md §10 copied verbatim and run on a synthetic Luau tree (motion helper, screen script, data and token modules); a Python model of the §4 hit-stop save-and-restore; list_roblox_studios (no instance, as the maker found),
  proposals/*.md rows that target these books (grep),
  ui-basics/evals/briefs.md E-01 (shop) for C7
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C1 (VR-19, VR-23), C8 V10",
     where: "engineering-craft/references/presentation.md:65 (§6 comfort module), :59 (§5 toned value); engineering-craft/SKILL.md:64 (EC-21), :97 (SR-12)",
     expected: "VR-23 apply: separate player controls for shake strength (incl. off), reduce flashes and reduce screen effects; VR-19 apply: a local clarity setting (all, reduced, essential) that changes only the local screen and never hides threats. The architect's rebuilt contract that P§6 cites as 'its contract' (architecture/references/presentation-contract.md:48-57) lists five settings: reduced motion, shake, flashes, screen effects, effect clarity.",
     observed: "The comfort module 'answers reducedMotion(), shakeScale(), reduceFlashes()'. No accessor for screen effects (full-screen tints, vignettes, FOV punches) and no clarity setting; P§5 tones other players' effects by a fixed spec value (PROPOSAL 0.5) with no player setting. SR-12 and SR-14 test only the Reduced and Viewer overrides.",
     evidence: "presentation.md:65 vs presentation-contract.md:50-56; riot/vfx-reads-timing.md VR-19 and VR-23 apply lines. A builder who codes the module from P§6 ships three of the five settings the architect's plan and the library require.",
     smallest_fix: "P§6: the module answers the five settings of presentation-contract.md §4 (add screenEffects() and clarity()); P§5: the toned value comes from the spec times the clarity setting, threats and pickups never toned; SR-14: the reduced override also covers the screen-effects branch; SR-12: with clarity = essential, others' non-threat effects tone further and threats stay full."}
  - {id: F2, class: blocking, check: "C4 / C7 correctness, C8 V10 and V11 (proposals/reviewer.md row 20)",
     where: "engineering-craft/references/presentation.md:52 (§4 hit-stop: 'then the previous values restored'); engine-first.md:35 (Hit-stop row: 'then restore')",
     expected: "A hit-stop always ends: restore to the track's base speed held by one owner per track (a stop-until time), and restore on interruption (death, unequip, destroy, a new clip). The reviewer's rebuilt book rates 'a hit-stop that can stay paused' High (code-review/references/presentation.md:31 PT-08, :47).",
     observed: "Save the current speed at pause and restore it at the end. Two overlapping stops on one track save 1 and then 0.",
     evidence: "My model of the text: stop A at 0 ms (100 ms), stop B at 50 ms (100 ms): 0 A speed 0; 50 B speed 0; 100 A ends speed 1 (B's stop already broken); 150 B ends speed 0: the track stays frozen. Multi-hit and fast melee hit this every time; ParticleEmitter.TimeScale has the same pattern. proposals/reviewer.md:20 asked for this change and coverage table d has no row for it.",
     smallest_fix: "P§4: 'one hit-stop owner per track and per emitter keeps a stop-until time; each new stop extends it; when it passes, set the base speed (1 or the clip's own speed) and TimeScale 1; also restore on death, unequip, destroy and a new clip.' Same words in the engine-first.md Hit-stop row (or point to P§4). Add an offline test case to SR-15's neighbour list or a new line in SR-09: two overlapping stops end with speed 1. Answer reviewer row 20 in coverage table d."}
  - {id: F3, class: blocking, check: "C8 V4 (binding platform-policy), C1 GD-35",
     where: "engineering-craft/references/presentation.md:78 ('The server checks PolicyService ... first'), :80 ('odds panel is built from the same probability table and modifier function'), :147 (egg example 'The server checks PolicyService'); engineering-craft/SKILL.md:100 (SR-15 'shown odds come from the server's table and modifier function'); engine-first.md:44",
     expected: "platform-policy SKILL.md:31 P-02: features ask the one policy module, never PolicyService directly; the module calls GetPolicyInfoForPlayerAsync in pcall with retry and fails closed (paid random treated as restricted). P-01 (:30): the server sends each player their effective odds; the UI never computes its own copy.",
     observed: "P§8 and the egg example tell the builder to check PolicyService itself (no pcall, no fail-closed); P§8 and SR-15 let the client build the odds from the table and modifier function, i.e. compute its own copy. The coverage file says V4 was diffed against rules.md § A only; the conflict is with the SKILL.md patterns. (P§9 :96 already says 'through the game's own policy module, never PolicyService itself', so the books disagree with themselves.)",
     evidence: "Quoted lines above. A builder following P§8 writes a direct PolicyService call; on a failed call the generator stays open to a restricted player, which P-02 forbids.",
     smallest_fix: "P§8 :78 and :147: 'the server asks the game's policy module (platform-policy P-02: fail closed) ...'; P§8 :80 and SR-15: 'the odds panel shows the effective odds the server sends, built on the server from the same table and modifier function the roll uses (P-01)'; engine-first.md:44 Fair-custom-work cell: 'the policy module (P-02) and the restricted path'."}
  - {id: F4, class: blocking, check: "C8 V11",
     where: "knowledge/jobs/J018-riot-craft/coverage/feature-builder.md table d (proposal rows); engineering-craft/references/handoffs.md:78-90 (§3 builder → reviewer)",
     expected: "Every other role's proposal row aimed at these books is adopted or declined with a reason.",
     observed: "proposals/reviewer.md rows 20 (hit-stop restore, F2) and 23 (builder → reviewer brief refs: presentation contract revision, feedback stack sheet, debug log of the hook runs, stand-ins) have no row in table d; handoffs §3 still lists only plan, manifest and test log.",
     evidence: "grep of proposals/*.md for engineering-craft, ui-basics, feature-builder: architect 19, 20; qa-lead 22; reviewer 20, 23; sound-designer 22; ui-ux-designer 26, 27. Table d answers all but reviewer 20 and 23.",
     smallest_fix: "Add both rows to table d. Row 23: add to handoffs §3 `refs`: '<presentation contract revision>, <feedback stack sheet>, <debug log of the Reject, DelayMs, Viewer, Reduced, DebugShape, Rate runs>' (or decline with a reason)."}
  - {id: R1, class: recommendation, check: "C8 V7, V6; C7",
     where: "engineering-craft/SKILL.md whole file: §6 runs 18.1-23.3 KB, §7 23.3-28.9 KB (df13ff4: §6 at 11.3 KB, file 11.8 KB)",
     expected: "Steps, rules and self-check in about the first 5,000 tokens (about 18 KB); one rule, one place.",
     observed: "The self-review starts at the cut and ends 5 KB after it; §1 :13 does say to re-read §3, §6 and §7 after a compaction (so this is not blocking). The attempt-and-outcome rule is stated in role :14, :36; EC §3 steps 1 and 8, EC-17, §5 rule 6, SR-08, §7 rows 1 and 19; P§2; U-14, U-S07, ui-basics §5; ui-effects §A; handoffs §11. EC-17..EC-25 each restate a P section the next column already points to.",
     evidence: "byte offsets measured with Python on the file.",
     smallest_fix: "Make EC-17..EC-25 one-line pointers (rule name + 'presentation.md §n'), shorten the header line (909 B) to the J018 phrase and the evidence sources, and move the SR-06/SR-08/SR-10 recipe detail to P§10 (keep the one-line look-for). Target: §6 ends near 19 KB."}
  - {id: R2, class: recommendation, check: "C7 (VR-22 'freeze on the best pose'), C8 V10",
     where: "engineering-craft/references/presentation.md:52, :145 (sword example); role :46 (animator: 'the hit-stop freeze frame')",
     expected: "The book names the trade-off it creates: a hit-stop started on the server's confirmed result arrives one round trip after the contact marker, so on a real connection the frozen pose is not the animator's freeze frame (animation-craft roblox-playback.md:58 asks the animator to check that it is).",
     observed: "Hit-stop only on the confirmed hit, with no word on latency. In Play Solo the delay is near 0, so the animator's check passes in Studio and fails for players.",
     evidence: "GD-34 (big layer on confirmed result) and VR-22 (freeze on the best pose) pull apart under latency; nothing in P§2 prediction rules covers hit-stop.",
     smallest_fix: "One line in P§4: 'Under latency the confirmed stop lands after the contact pose: test with DelayMs 150; where the spec allows, the attacker's own client may start the stop on contact_candidate and end it at once on a denial (P§2 prediction rule); otherwise agree with the animator a hold or a shorter stop.' Add DelayMs 150 to the sword example's checks."}
  - {id: R3, class: recommendation, check: "C8 V3 (screening aid known limits)",
     where: "engineering-craft/references/presentation.md:128 (literals grep), :140 (§11 known false readings); SKILL.md:91 SR-06; ui-basics SKILL.md:73 U-S05",
     expected: "The grep's known misses listed next to it, or the pattern widened, for the common modern-Luau forms.",
     observed: "Verbatim run on my sample tree: missed label.Text = 'Not enough coins' (single quotes), label.Text = `Need {n} more coins` (interpolated string: the book's own refusal text written the current-Luau way), task.wait(0.28) and task.delay(0.35, ...) (durations: EC-18 bans them, the grep never looks), and '\"Need \" .. n .. \" more coins\"'. None is in §11. §11 does say a clean grep is not proof, so not blocking.",
     evidence: "scratchpad fbrev/tree: 10 hits, these 5 lines absent. A widened pattern I tested caught all but the concatenation: grep -rnE \"TweenInfo\\.new|EasingStyle\\.|Color3\\.|\\.Text\\s*=\\s*[\\\"'\\`]|[\\\"'\\`][A-Z][a-z]+( [a-z0-9{]+)+|task\\.(wait|delay)\\(\\s*[0-9.]\" src",
     smallest_fix: "Use the widened pattern (or add the four misses to §11), and add to SR-06: 'a clean result still needs the code read of the screen's tween, text and timer paths'."}
  - {id: R4, class: recommendation, check: "C8 V3; C3",
     where: "ui-basics/SKILL.md:74 (U-S06: 'its background box must sit directly behind the text on the brightest backdrop'); proposals/feature-builder.md row 'ui-design review.md §6' (same words)",
     expected: "The weakest backdrop: the brightest for light text, the darkest for dark text.",
     observed: "'Brightest' unconditionally. Dark text on a light translucent panel then gets a false PASS.",
     evidence: "look_check.py contrast on my sample (dark #1E1E1E text, 60 %-transparent light panel over sky and dark grass): bg box on the brightest part 13.27 PASS; on the darkest part 3.76 FAIL (wcag-text). White text on the sky part: 3.09 FAIL, as the maker found.",
     smallest_fix: "U-S06 and the proposal row: 'on the weakest backdrop the screen meets (the brightest for light text, the darkest for dark text)'."}
  - {id: R5, class: recommendation, check: "C4 (engine omission)",
     where: "ui-basics/SKILL.md:51 U-15 ('only that control shakes (a Position offset tween)'); ui-basics/references/ui-effects.md:32 (§B refusal shake: 'the layout and the other controls stay still'); presentation.md:75",
     expected: "A control that is a direct child of a UIListLayout or UIGridLayout ignores its own Position: ui/list-flex-layouts.md:14-16 ('overrides or influences the Position, Rotation and/or Size of all sibling UI objects ... changes ... will not have the normal effect').",
     observed: "The shake recipe gives no exception; in a button row, tab bar or menu list the shake silently does not play (message, icon and sound still do).",
     evidence: "docs lines above; ui-basics/references/facts.md:13 already says the layout controls siblings' position.",
     smallest_fix: "U-15 and §B: 'tween the Position offset of the control's inner content frame (a control laid out by a UIListLayout or UIGridLayout ignores its own Position)'."}
  - {id: R6, class: recommendation, check: "C7",
     where: "engineering-craft/SKILL.md:13 (§1 'Steps 6, 8 and 9 apply when the change has something players see or hear; a pure rule or data change skips them')",
     expected: "The worst-case pass's lifecycle and scale parts (respawn, reset and reopen 20 times; most players; rejected request and slow server) apply to every change; only its presentation parts are optional.",
     observed: "A save, remote or money change with nothing visible skips step 9, so SR-17 (connections back to baseline, late answers dropped) is never run for it.",
     evidence: "SR-17 :102 has no presentation condition; the §6 preamble limits only SR-06..SR-16 to visible changes.",
     smallest_fix: "§1: 'Steps 6 and 8 apply when ...; step 9 always runs, its burst, viewer and quality parts only when players see or hear the change.'"}
  - {id: R7, class: recommendation, check: "C3",
     where: "engineering-craft/SKILL.md §6; presentation.md:53 (one root, one scale factor), :46 (footsteps), :61 (camera channels)",
     expected: "A self-review line for each checkable finding the builder carries.",
     observed: "VR-17 (change the root scale once: all layers stay aligned), SD-23 (every floor material in the place has a footstep row) and VR-21 (a frequent effect at its real rate never moves the camera) have rules but no SR line.",
     evidence: "library check lines of VR-17, SD-23, VR-21; coverage table a cites no SR line for VR-17 or SD-23.",
     smallest_fix: "SR-10: add 'no cam line during the rate run'; SR-16: add 'scale factor ×2 once: one still, layers aligned (after the probes.md §4 ScaleTo probe)'; SR-07: add 'every FloorMaterial used in the place has a footstep row (S read of materials vs the table)'."}
  - {id: R8, class: recommendation, check: "C8 V10",
     where: "presentation.md:89 (Rate hook), :105 (live line)",
     expected: "The animator's role (roles/animator.md:67) asks for a rate trigger for frequent clips that logs the playing-track count.",
     observed: "Rate logs the live-copy count of effects and cues only.",
     evidence: "role line quoted; maker's own proposal row to roblox-playback.md §10 mentions 'live lines for playing tracks', but P§9 does not define them.",
     smallest_fix: "P§9: 'live' ids include `track:<clip-id>` (count of playing tracks from Animator:GetPlayingAnimationTracks)."}
  - {id: R9, class: recommendation, check: "C5",
     where: "ui-basics/references/ui-effects.md:17 (Currency change, Sound cell)",
     expected: "Old df13ff4 :14 'tick on gain, clink on spend' kept or its removal reasoned.",
     observed: "Now 'tick on the first arrivals, one closing sound'; the spend sound is gone and table c says only 'sharpened'.",
     evidence: "git diff df13ff4 of ui-effects.md.",
     smallest_fix: "'tick on the first arrivals and one closing sound on gains; a soft clink on spend; on the confirmed update'."}
  - {id: R10, class: recommendation, check: "C2",
     where: "engineering-craft/SKILL.md:112 (§7 row 2)",
     expected: "Master UP-02 engineering line: 'profile on a phone-class device with the expected player count'.",
     observed: "Row 2 says 'phone viewport', which the emulator gives without phone CPU, GPU or memory (probes.md:38).",
     evidence: "universal-principles.md:80.",
     smallest_fix: "Row 2: add 'phone cost is a phone-class profile (performance), never the viewport emulator'."}
  - {id: R11, class: recommendation, check: "C8 V10 (for the lead; not this maker's file)",
     where: "testing/references/player-facing.md:54",
     expected: "Agrees with presentation.md §9, which now has Outcome / Seed and Set.",
     observed: "'not in the builder's set yet (proposal filed)'.",
     evidence: "presentation.md:95-96.",
     smallest_fix: "The qa-lead maker updates the row to the builder's names."}
keep: [
  the feedback stack sheet in the contract (P§1) and its tie to the architect's P-rows,
  the skeleton → presentation → worst-case order with a check per step (§3),
  attribute-driven Studio-only test hooks and the debug log line format shared with sound, VFX, UI, QA and review (P§9),
  the §6 self-review with named inputs and the known false readings (P§11),
  the partner table in the role file (what to ask, and when),
  refusals at the control, true counters, honest reveal windup tests (EC-22, EC-23, SR-11, SR-15),
  the new engine-first rows and the open probes (§4), all checked against the docs mirror,
  every old rule kept or moved (walked the diff: only R9 lost without a reason)
  ]
verdict: fix-first
</spec>
```

## Result per check
| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (3 of 52 rows) | 52 of 52 matrix ids have a row; opened every landed-in location. VR-19 and VR-23 lose the clarity and screen-effects controls (F1); VR-22's restore recipe freezes tracks (F2). MD-05, PP-09, SD-16 partial rejections are sound. GD-35 lands but conflicts with P-01/P-02 (F3). |
| C2 core principles | pass | `engineering-craft` §7 covers all 10 principles the master tags for feature-builder (UP-01, 02, 07, 08, 13, 15, 16, 17, 19, 20) plus 4, 6, 12, 14, 18; each has an example and a check; the 5 left out are untagged in the master. No contradiction. R10 small. |
| C3 self-review | pass with gaps | SR-01..SR-19 and U-S01..U-S13 name their input and run with Studio MCP, grep, offline tests. R7 (three missing lines), R4 (wrong box rule for dark text). |
| C4 kit rules and engine | pass with gaps | 20 engine claims checked in the mirror: all correct. R5 (shake under layouts omitted). The hit-stop restore (F2) is a logic error, not an engine claim. |
| C5 nothing lost | pass | Every removed line walked; kept, moved or sharpened; the J016 extracts pointer removed per the job card. R9 one small loss. |
| C6 fixed rules | pass | Frontmatter byte-identical (diff); SKILL.md 127 and 83 lines; descriptions 376 and 394 chars unchanged; no renumbering (§7 and probes §4 appended); J018 phrase in all 8 changed files and the role comment; no Riot names or library ids in bodies; no tips section; evals/ unchanged. |
| C7 better work | yes, after F1-F3 | See below. |
| C8 brief v2/v3 | fail (V4, V11) | V1 pass (inputs and still budgets); V2 pass (only `look_check.py contrast`, a real mode); V3 my runs: contrast right for light text, wrong box rule for dark (R4); literals grep misses common forms (R3); V4 fail (F3); V6 recommendation (R1); V7 recommendation (R1); V8 pass (sheet, partner asks, self-review); V10 fail via F1, F2 (R8, R11 small); V11 fail (F4); V12/V13 pass (one-line grep, no copied measuring code). |

**Better work (C7, brief E-01 shop screen).** With the old books the agent would build a correct, safe purchase path and a scaled screen, and stop there: nothing about press feedback timing, pending, refusals, counters or the partners' tables. With the new books it writes a feedback stack, plays a skeleton first, wires the press cue before the request, shows "Need 40 more coins" at the button, keeps affordability on the true balance, reads every tween and string from tables and proves it with the reject and delay hooks. That is clearly better work. The weak spots: the hit-stop recipe can freeze a track (F2) and ignores latency (R2); paid reveals bypass the policy module (F3); the comfort module misses two settings (F1); the engineering-craft SKILL.md is twice as long, with the attempt/outcome rule in about ten places (R1); the grep and contrast screens have unlisted false passes (R3, R4).
