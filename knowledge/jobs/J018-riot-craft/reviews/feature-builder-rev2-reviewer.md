---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer feature-builder · claude-opus-5-5 · high · 2026-10-22

# Review: feature-builder books, round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/feature-builder.md (body) + .agents/skills/engineering-craft/ (SKILL.md, references/ engine-first, probes, handoffs, presentation; shared with architect, qa-lead, reviewer) + .agents/skills/ui-basics/ (SKILL.md, references/ facts, ui-effects; evals/ not changed), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer feature-builder (opus, high)
looked_at_first: [
  all eight book files read in full as they are now; git diff df13ff4 for each, every removed line walked (C5),
  every finding of reviews/feature-builder-rev1-reviewer.md re-checked against the current text (table "Round 1 findings" below),
  matrix.md feature-bu column extracted by script (52 ids) and the principle, apply, check and roblox_fit lines of all 52 findings read; universal-principles.md index and applies-to lines of UP-01..UP-20,
  docs mirror for the claims new since round 1: Animator.yaml:128-140 (fading tracks listed), PolicyService.yaml:66-94, 170-184 (the call can error), ui/list-flex-layouts.md:16, ui/grid-table-layouts.md:40, Workspace.yaml:1524-1528, Camera.yaml:1254-1266, 1306-1312, GuiService.yaml:225, 262, Humanoid.yaml:365-372, NetworkSettings.yaml:173-197, accessibility.md:104-129, 184-208, in-experience-containers.md:93-98, ParticleEmitter.yaml:502-511, 962-968, AnimationTrack.yaml:318-324, Animator.yaml:217-232 (replication), TextLabel.yaml:481 (TextFits),
  partner books for V4 and V10: platform-policy SKILL.md P-01..P-05; architecture/references/presentation-contract.md §2-§5 (predicted layer, comfort service, probe 3, hit-stop line); code-review/references/presentation.md PT-08, PT-09, PT-19, S3, S6; code-review/references/testing.md:16; code-review/references/luau-current.md:42-45; testing SKILL.md:30, :70 and references/player-facing.md §3; roles animator :67, vfx-designer :65, qa-lead :44, reviewer :44; animation-craft roblox-playback.md:58; ui-design review.md S-18, S-33, S-44; studio-mcp C-04, C-05, P-03,
  my own V3 runs (scratchpad fbrev2/): the literals grep extracted verbatim from presentation.md §10 and run with eval on a synthetic Luau tree (single, back-quoted, concatenated, Title Case and upper-case strings, task.wait, legacy wait and delay, TweenInfo, Color3, a message data module); a widened pattern on the same tree; look_check.py contrast (real mode, --help read) on a synthetic 1280 x 720 capture: white text on a 50 %-transparent navy panel spanning bright sand and dark forest,
  python tools/sync_harness.py --check (read-only),
  grep of proposals/*.md for rows that target these books,
  ui-basics/evals/briefs.md E-01 and E-05, and a typical money feature (sell button) for C7
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V10 (qa-lead and reviewer books, rebuilt), C4",
     where: "engineering-craft/references/presentation.md:85 (§9 'They run only in Studio (RunService:IsStudio())'); engineering-craft/SKILL.md:103 (SR-18 'test hooks Studio-only'); role :65 (Write scope 'Studio-only test hooks'); role partner table :41-52 (no qa-lead row)",
     expected: "Hooks ship only in the test build; the published build carries none. code-review/references/testing.md:16 (already at df13ff4): 'publish only the production build, never the test build with its hooks'. testing SKILL.md:70: 'Test hooks ship only in the test build: the production build carries none'. qa-lead role :44 asks the builder for 'a test build with the hooks and a production build without them'. code-review presentation.md PT-19: 'nothing in the production build reads a hook value'.",
     observed: "The builder's books gate the hooks with IsStudio and say nothing about a test build. A builder following P§9 puts the hook script and the two TestHooks folders in the default source tree, so they publish with the game; it cannot deliver the build the qa-lead asks for, and the hooks it ships include Outcome / Seed (force a paid roll's result) and Set (set a balance) on the server, held back only by the gate.",
     evidence: "grep of the eight books for 'test build|production build|publish': no hit on hooks. The four partner lines quoted above. PT-19 itself notes that an attribute set in Studio is saved with the place.",
     smallest_fix: "P§9 first paragraph: 'The hook script and the TestHooks folders live only in the test build (for example a test project file that adds them to the default one); the published build is made without them (code-review testing.md); the IsStudio gate stays as the second guard.' SR-18: 'the production build has no TestHooks folder or hook script; every hook reader is behind IsStudio'. Role Write scope: 'Studio-only test hooks, in the test build only'. Role partner table: a qa-lead row (asks: the PF rows and the hook names at plan, the test and production builds with the candidate)."}
  - {id: F2, class: blocking, check: "C8 V11",
     where: "knowledge/jobs/J018-riot-craft/coverage/feature-builder.md table d (proposal rows)",
     expected: "Every other role's proposal row aimed at these books is adopted or declined with a reason.",
     observed: "Two rows have no answer in table d: (1) proposals/qa-lead.md row 31 (presentation.md §10 literals grep: add BrickColor, or list it in §11; file time 08:51, before the coverage file's last write at 08:57); (2) proposals/architect.md row 25 (presentation.md §4 hit-stop: say which clients run the stop; add the open probe 'AdjustSpeed(0) on a character track replicated from another client: does it hold on the observing client, does the owning client's pause replicate'; tie the predicted attacker-only stop to the contract's 'predicted' layer row). Row 25 was written after the maker's last write (architect.md 09:02), so this is new work for round 2, not an omission in round 1.",
     evidence: "grep of proposals/*.md for engineering-craft, ui-basics, presentation.md: table d answers architect 19, 20; qa-lead 22; reviewer 20, 23; sound-designer 22; ui-ux-designer 26, 27; not qa-lead 31 or architect 25. The probe is real: Animator.yaml:217-232 documents only that animations started on the owning client replicate, not what a local AdjustSpeed does to another client's replicated track; presentation-contract.md:70 lists it as probe 3; probes.md §4 does not carry it, so the target's freeze on an attacker's track rests on undocumented behaviour.",
     smallest_fix: "Answer both rows in table d. Row 31: add 'BrickColor\\.' to the pattern (see R1 for a tested pattern). Row 25: P§4 'the stop runs on the attacker's and the target's clients only (bystanders where the contract row says so)'; add the replication question as a row in probes.md §4; the predicted stop is a contract row with layer 'predicted' (presentation-contract.md §2), never the outcome row."}
  - {id: R1, class: recommendation, check: "C8 V3 (screening aid known limits)",
     where: "engineering-craft/references/presentation.md:132 (literals grep), :144 (§11 known misses)",
     expected: "Common literal forms caught, or listed as misses next to the grep.",
     observed: "Run verbatim on my sample tree, the grep missed notify(\"Not Enough Coins\"), showBanner(\"Daily Reward Claimed\"), setLabel(button, \"Level Up\") (Title Case strings passed to a helper: the string pattern allows only lower-case words after the first), wait(0.3) and delay(0.35, ...) (legacy globals, common in AI-written code), and BrickColor.Red() (qa-lead row 31). None is in §11. §11 says a clean grep is not proof and SR-06 asks for the code read, so not blocking.",
     evidence: "scratchpad fbrev2/src: 11 hits, these 5 lines absent. This pattern caught all of them with no new false hit on game:GetService(\"TweenService\"): grep -rnE \"TweenInfo\\.new|EasingStyle\\.|Color3\\.|BrickColor\\.|\\.Text\\s*=\\s*[\\\"'\\`]|[\\\"'\\`][A-Z][a-z]+( [A-Za-z0-9{]+)+|[\\\"'\\`][A-Z][a-z]+ [\\\"'\\`]\\s*\\.\\.|(^|[^.A-Za-z_])(task\\.)?(wait|delay)\\(\\s*[0-9.]\" src",
     smallest_fix: "Use the widened pattern (re-run it on the maker's d10 tree), or add the three forms to §11."}
  - {id: R2, class: recommendation, check: "C7 (contradiction), C2 (UP-19)",
     where: "engineering-craft/SKILL.md:76 (§5 rule 'No success layer before the server's confirmation'); presentation.md:15 (§1 Outcome response includes the hit-stop tier), :53 (predicted stop on contact_candidate); role :14 ('the big moment waits for the server')",
     expected: "One statement of the exception: a predicted layer only where the spec allows it, small, on the acting player's client, removed in the frame the denial arrives, never money, rewards or paid reveals (P§2; presentation-contract.md:28).",
     observed: "§5 states the rule with no exception, while P§2 and P§4 allow a predicted hit marker and a predicted hit-stop. A builder running §5 as its final check flags its own allowed prediction, or a reviewer reads the predicted stop as an outcome layer before confirmation. Note: the predicted stop entered the books from my own round-1 recommendation R2; on a denial the attacker sees a freeze on a miss for up to one round trip, which is the trade-off the game designer must sign.",
     evidence: "Quoted lines; GD-34 roblox_fit 'a predicted hit that the server rejects never shows the confirmed-hit layer'.",
     smallest_fix: "§5 rule 6: '... except a predicted row the spec allows (presentation.md §2: small, own client, removed on denial; never money, rewards or paid reveals)'. P§4 latency bullet: 'the predicted stop is the game designer's choice, recorded as a predicted row; default: the agreed hold or a shorter confirmed stop'."}
  - {id: R3, class: recommendation, check: "C7 (correctness of the hit-stop recipe)",
     where: "engineering-craft/references/presentation.md:52 ('holds the base speed (the speed the clip was started with; TimeScale 1)')",
     expected: "The base is the speed the game last set for that clip, and every other speed change on the track goes through the owner.",
     observed: "'Started with' is ambiguous when a game plays a clip and then calls AdjustSpeed (attack-speed stats, a slow debuff): the owner restores 1 after each stop, the rest of the swing plays at the wrong speed and its markers fire later than the server's windows. An emitter whose spec sets TimeScale below 1 is restored to 1.",
     evidence: "AnimationTrack.yaml:318-324 (speed is set by AdjustSpeed after Play as well as by Play); the SR-17 offline test in the book uses one base and would not catch it.",
     smallest_fix: "P§4: 'the base is the speed the game last set for that track (other code changes speed only through the owner, which updates the base) and the emitter's spec TimeScale'; SR-17: add 'a speed change during a stop survives the stop'."}
  - {id: R4, class: recommendation, check: "C8 V1 (image budget), C3",
     where: "ui-basics/SKILL.md:65 (C input 'one per state per size: smallest phone, tablet, PC, TV'), :71-72 (U-S03, U-S04)",
     expected: "The light-check rule: numbers for every case, stills only for failures and a few key states.",
     observed: "Ten states at four sizes is up to 40 stills, plus Largest text size; the clipping and safe-area checks need no image.",
     evidence: "TextLabel.TextFits (TextLabel.yaml:481) and GuiBase2d.AbsolutePosition / AbsoluteSize against the inset rectangle give both answers as numbers in one execute_luau read per state and size.",
     smallest_fix: "U-S03 and U-S04: 'S read for every state and size: elements outside the inset rectangle, TextFits = false (count 0); stills: the main state at each size, failures, and the states the UI designer's slot names'."}
  - {id: R5, class: recommendation, check: "C8 V4",
     where: "ui-basics/SKILL.md:51 (U-15 'a disabled control shows why and what unlocks it before it is pressed')",
     expected: "platform-policy P-03: for a restricted player, hide the paid-random control or give a free path; a refusing button only where hiding is not possible.",
     observed: "U-15 is general; a builder applies it to the egg button of a restricted player and shows a disabled button with a reason.",
     evidence: "platform-policy SKILL.md:32 P-03.",
     smallest_fix: "U-15 last clause: '(a paid-random control for a restricted player is hidden or given a free path: platform-policy P-03)'."}
  - {id: R6, class: recommendation, check: "C7 (false reading of the hook recipe)",
     where: "engineering-craft/references/presentation.md:85-99 (§9), :135-146 (§11)",
     expected: "A hook set for one run does not change the next run.",
     observed: "Attributes set in Edit mode (the probes.md §4 network-delay probe is set in Edit; Reduced, Clarity or Viewer set before Play) are saved with the place, so a left DelayMs, Reject or Reduced makes the next play-test read wrong with no error.",
     evidence: "code-review presentation.md PT-19: 'An attribute set in Studio is saved with the place'.",
     smallest_fix: "P§9: 'the hook script prints its active overrides at start; clear every hook attribute after the run'; P§11: the same as a known false reading."}
  - {id: R7, class: recommendation, check: "C7 (consistency inside the books)",
     where: "role :34 (step 4 skeleton pass), :36 (step 6 presentation pass)",
     expected: "engineering-craft §1:13: steps 6 and 8 only when players see or hear the change; step 9 always.",
     observed: "The role states both passes without the condition, so a pure save or remote change reads as needing a Studio skeleton and a presentation pass.",
     evidence: "Quoted lines.",
     smallest_fix: "Role steps 4 and 6: add '(when players see or hear the change: engineering-craft §1)'."}
keep: [
  the feedback stack sheet tied to the architect's P-rows (P§1) and the skeleton → presentation → worst-case order with a check per step (EC §3, §1 conditions),
  the hit-stop owner with stop-until time, interruption restore and the overlap test (P§4, SR-17), matching the reviewer's PT-08 and the architect's contract,
  the comfort module with the five settings and the Clarity override (P§5, P§6, SR-12, SR-14),
  paid reveals through the policy module, fail closed, server-sent effective odds (P§8, SR-15, egg example),
  the attribute-driven test hooks and the debug log format shared with sound, VFX, UI, QA and review (P§9), now with track counts and their fading-track false reading,
  the §6 self-review with named inputs, the one-line EC-17..EC-25 pointers and the §11 false readings,
  U-S06 contrast rule by text tone (my run: brightest backdrop 4.39 FAIL, dark side 15.3 PASS, both right for white text),
  the refusal shake on the inner content frame (U-15, ui-effects §B) and the restored spend sound,
  the engine-first rows and the open probes, every old rule kept or moved (diff walked; EC-06 facts confirmed at luau-current.md:42-45)
  ]
verdict: fix-first
</spec>
```

## Round 1 findings
| Id | Status | Where it is now |
| --- | --- | --- |
| F1 comfort settings | fixed | P§5 :60, P§6 :66-67, P§9 Clarity :94, SR-12, SR-14, EC-21; agrees with presentation-contract.md §4 |
| F2 hit-stop restore | fixed | P§4 :52, engine-first.md hit-stop row, H§14, SR-17, sword example; agrees with code-review PT-08 (R3 is a new, smaller point) |
| F3 policy module, server-sent odds | fixed | P§8 :79-82, egg example, SR-15, EC-23, engine-first.md paid random row; agrees with P-01, P-02 |
| F4 reviewer rows 20, 23 | fixed | table d; handoffs.md §3 refs |
| R1 length | fixed in part, rest declined with a sound reason | §6 at 15.6-20.9 KB, §7 after; §1 says to re-read §3, §6, §7 after a compaction |
| R2 latency of the stop | fixed | P§4 :53, SR-08, role animator row (R2 above tightens the wording) |
| R3 literals grep | fixed | widened pattern and §11 list (R1 above: three more forms) |
| R4 contrast box | fixed | U-S06 (confirmed by my run) |
| R5 shake under layouts | fixed | U-15, ui-effects §A, §B |
| R6 step 9 always | fixed | EC §1 :13 (R7 above: the role does not say it yet) |
| R7 three SR lines | fixed | SR-07, SR-10, SR-16 |
| R8 track counts | fixed | P§9 Rate and live lines, §11 fading tracks |
| R9 spend sound | fixed | ui-effects §A currency row |
| R10 phone-class profile | fixed | EC §7 row 2 |
| R11 qa-lead hook names | fixed by the qa-lead maker | player-facing.md:54-55 (Clarity still missing there: the maker's proposal row covers it) |

## Result per check
| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass (52 rows checked, 0 failed) | 52 of 52 matrix ids have a row; every landed-in location opened against the finding's principle, apply and check lines; the 3 partial rejections (MD-05, PP-09, SD-16) and the role splits (GD-06, PP-11, WL-29) are sound. |
| C2 core principles | pass | EC §7 covers all 10 principles the master tags for feature-builder (UP-01, 02, 07, 08, 13, 15, 16, 17, 19, 20) plus 4, 6, 12, 14, 18, each with an example and a check; no contradiction. R2 tightens the UP-19 exception wording. |
| C3 self-review | pass | SR-01..SR-19 and U-S01..U-S13 name their inputs and run with Studio MCP, grep, offline tests and look_check contrast. R4 (numbers before stills for UI). |
| C4 kit rules and engine | pass with one conflict (F1) | Every new docs line checked in the mirror: correct. F1 conflicts with code-review testing.md:16. The replication of a local pause on another client's track is undocumented and not yet a builder probe (F2). |
| C5 nothing lost | pass | Every removed line walked; the EC-06 table facts are at luau-current.md:42-45; the spend sound is back. |
| C6 fixed rules | pass | Only the 8 listed books and the job's own files changed for this role; role frontmatter byte-identical to df13ff4; SKILL.md 127 and 83 lines; descriptions 376 and 394 characters; headings only extended or appended (§7, probes §4); the J018 phrase in all 8 files and the role comment; no library ids, Riot names or tips section in the bodies; LF endings; evals/ unchanged. sync_harness --check shows the generated copies stale: the lead's sync before commit. |
| C7 better work | yes, after F1 | See below. |
| C8 brief v2/v3 | fail (V10 via F1, V11 via F2) | V1 pass (R4 small); V2 pass (look_check contrast flags match --help); V3 my runs: contrast right, grep misses three common forms (R1); V4 pass (R5 small); V6 pass (one-line pointers); V7 pass (self-review ends near the 5,000-token cut, §1 re-read line); V8 pass; V10 fail (F1); V11 fail (F2); V12/V13 pass. |

**Better work (C7).** Typical job: "add a Sell button that turns the backpack into coins", plus E-05 "every button presses down on click". With the old books the agent would build a safe server sale and a scaled button and stop: no press timing, no pending, no refusal text, a coin label per pickup. With the new books it writes the feedback stack, plays a skeleton first, fires the press cue in the input frame, pays out only on the server's result, says "Backpack empty" at the button, merges "+N" labels, keeps the counter true, reads every tween from the motion table and proves it with the Reject, DelayMs and Rate hooks. That is clearly better work, and the round-1 defects (frozen hit-stop, direct PolicyService, missing comfort settings) are gone. Still weak: the hooks would publish with the game (F1); two partner rows are unanswered, one of them an engine gap in the hit-stop (F2); the grep misses Title Case strings and legacy waits (R1); the predicted stop and the §5 rule disagree (R2); a mid-clip speed change is lost after a stop (R3); UI checks still lean on up to 40 stills (R4).
