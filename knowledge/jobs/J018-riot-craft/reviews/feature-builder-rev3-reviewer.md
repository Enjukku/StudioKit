---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer feature-builder · claude-opus-5-5 · high · 2026-10-22

# Review: feature-builder books, round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/feature-builder.md (body) + .agents/skills/engineering-craft/ (SKILL.md, references/ engine-first, probes, handoffs, presentation; shared with architect, qa-lead, reviewer) + .agents/skills/ui-basics/ (SKILL.md, references/ facts, ui-effects; evals/ not changed), working tree on top of df13ff4 after repair round 2, 2026-10-22
reviewer: J018 reviewer feature-builder (opus, high)
looked_at_first: [
  reviews feature-builder-rev1 and rev2 (to re-check every earlier finding), then the coverage file (read before the books this round: a deviation from the spec order, said here; every claim in it was checked against the books, not taken from it),
  all eight book files read in full as they are now; git diff df13ff4 of all eight, every removed line walked (C5),
  matrix.md feature-bu column extracted by script (52 ids); principle, apply, check and roblox_fit lines of all 52 findings; universal-principles.md index, engineering lines and applies-to lines of UP-01..UP-20,
  docs mirror: TextLabel.yaml:481-494 (TextFits), Animator.yaml:128-141, 215-234, projects/server-authority/techniques.md:130-146,
  partner books for V4 and V10: platform-policy SKILL.md P-01..P-05 and references/rules.md § A line 11; code-review references/testing.md:16, references/presentation.md PT-19 :42, severity :48-50, S10 :95; testing references/player-facing.md §3 :45, :56; architecture references/presentation-contract.md :33, :43-44, :56, :69-70, :83; animation-craft roblox-playback.md:58 and SKILL.md C-25 :68; vfx-design camera-and-screen.md:117; ui-design review.md §7 :170; sound-design SKILL.md S-133; studio-mcp SKILL.md §5,
  my own V3 runs (scratchpad fbrev3/): the production-build check of P§10 with Rojo 7.7.0 on a synthetic project (default and test project files, a planted leak, a failed build over an old output file); the literals grep extracted verbatim from presentation.md:138 and run with eval on a synthetic Luau tree (string.format, "Word: " .. concatenations, interpolation, legacy waits, a neutral file with GetService, Instance.new, WaitForChild, Event:Wait, task.wait(), a config wait); a widened pattern on the same tree; list_roblox_studios (none connected, as the maker found),
  python tools/sync_harness.py --check (read-only), heading diff against df13ff4, byte offsets of §3/§5/§6/§7,
  grep of proposals/*.md for every row aimed at these books or at the builder (V11),
  ui-basics/evals/briefs.md E-03 (tiny text) for C7, plus the sell-button feature used in round 2
  ]
findings:
  - {id: R1, class: recommendation, check: "C8 V3 (screening aid known limits)",
     where: "engineering-craft/references/presentation.md:138 (literals grep), :150 (§11 caught and missed lists)",
     expected: "Common Luau ways of building player text are caught, or listed as misses next to the grep.",
     observed: "Run verbatim, the grep misses label.Text = string.format(\"Need %d more coins\", n), notify(string.format(\"Need %d more coins\", n)) (a format code right after the first word: the space group allows only letters, digits and '{') and toast(\"Cooldown: \" .. t .. \"s\") (punctuation after the capitalised word before '..'). string.format is a common form in AI-written Luau; neither is in §11. Not blocking: §11 says a clean grep is not proof and SR-06 / U-S05 require the code read.",
     evidence: "scratchpad fbrev3/tree/src/Screen.client.luau: 10 hits, lines 4, 5, 7 absent (line 17, a wait on a local number, is a listed miss). This pattern caught 4, 5 and 7 with no hit on the neutral file (GetService, Instance.new, WaitForChild, FindFirstChild, Event:Wait, task.wait(), task.wait(cfg.holdSeconds), ('%s'):format): grep -rnE \"TweenInfo\\.new|EasingStyle\\.|Color3\\.|BrickColor\\.|\\.Text\\s*=\\s*[\\\"'\\`]|[\\\"'\\`][A-Z][a-z]+[:!?.,]?( [A-Za-z0-9{%]+)+|[\\\"'\\`][A-Z][a-z]+[:!?.,]? [\\\"'\\`]\\s*\\.\\.|(^|[^.A-Za-z_])(task\\.)?(wait|delay)\\(\\s*[0-9.]\" src",
     smallest_fix: "Use the widened pattern (re-run it on the d12 tree), or add 'string.format(\"Word %d ...\")' and '\"Word: \" ..' to the §11 miss list."}
  - {id: R2, class: recommendation, check: "C4 (engine claim), C7 (E-03)",
     where: "ui-basics/SKILL.md:71 (U-S03 'a TextScaled label always fits'), :72 (U-S04 'since a scaled label always reports a fit')",
     expected: "Engine claims backed by a docs line or a probe. TextLabel.yaml:481-494: TextFits 'reflects the combined effect of TextWrapped, TextTruncate, and TextScaled' and is false 'when the text is too large and is therefore clipped or truncated'.",
     observed: "The book states that a TextScaled label always fits. The docs do not say so, and U-04 itself prescribes TextScaled with a UITextSizeConstraint (MinTextSize >= 9), the case where the text cannot shrink further and can clip on the smallest phone. That is exactly eval E-03 ('Text is unreadable on small phones'). An agent that reads the sentence as an exclusion filters TextScaled labels out of the S read and gets 0 with no error for the clipped labels the eval is about. The U-S04 conclusion (TextScaled text does not grow with PreferredTextSize, so a code read) stays right for another reason (facts.md:113).",
     evidence: "Docs lines quoted; ui-basics/SKILL.md:40 (U-04); evals/briefs.md E-03. No Studio was connected to probe it.",
     smallest_fix: "U-S03: replace 'a TextScaled label always fits' with 'TextScaled labels count too: one held at its UITextSizeConstraint minimum can clip (TextFits false)'; U-S04: 'reading text grows (no TextScaled on it: code read, since TextScaled ignores PreferredTextSize, facts.md)'. Optionally one probe row in probes.md §4: a TextScaled label with MinTextSize 9 in a box too small for it reads TextFits false."}
  - {id: R3, class: recommendation, check: "C8 V3 (what gives a wrong number with no error), C4 (source modes)",
     where: "engineering-craft/references/presentation.md:134 (§10 Production build row), :154 (§11), :87 (§9 Test build only)",
     expected: "The check cannot read an old build, leaves no build file in the repo, and says what to do in the source modes that have no project file.",
     observed: "(a) The row writes prod.rbxlx in the repo root and greps it. If the build fails (a renamed project file), Rojo prints an error but the grep reads the previous prod.rbxlx and prints its old count; the line SR-18 relies on is then stale. (b) The output file stays in the repo root (SR-18 also says temporary files removed). (c) studio-mcp §5 allows files mode through Studio Script Sync and a `studio` mode: neither has a project file, so the 'test project file' route and this check do not apply; §11's Studio read before a publish is the only guard and the book does not say so for those modes.",
     evidence: "My run (Rojo 7.7.0, scratchpad fbrev3/proj): default build 0, test build 4 (positive control), planted leak (hook script copied into src/server) 1: the recipe is right. Then 'rojo build default.project.jsn -o prod.rbxlx': rojo exit 1, and 'grep -c TestHook prod.rbxlx' printed 1 with exit 0 from the old file. studio-mcp SKILL.md:49-52; game-profile.md:27.",
     smallest_fix: "Row: 'rm -f \"$TMP/prod.rbxlx\" && rojo build default.project.json -o \"$TMP/prod.rbxlx\" && grep -c TestHook \"$TMP/prod.rbxlx\"' (a scratch path; the same for the test build). §9 or §11 one line: 'Script Sync or studio source mode: the hooks are synced only into the test place (game profile place ids); the Studio read of §11 runs before every publish.'"}
  - {id: R4, class: recommendation, check: "C7 (correctness of the hit-stop recipe), C4",
     where: "engineering-craft/references/presentation.md:52 (§4 'AdjustSpeed(0) on the attacker's and target's tracks'; 'every other speed change on it ... goes through the owner')",
     expected: "The tracks the stop pauses are named, and the rule 'every speed change goes through the owner' is one the builder can keep.",
     observed: "'The attacker's and target's tracks' can be read as every playing track of both characters. The default character Animate script re-speeds its own locomotion track on every Running event, outside the owner, so a paused walk or run track resumes mid-stop and the owner's base for it is wrong. The library line says the stop freezes the attacker's and target's animation; the clean reading is the action clip and the hit-reaction clip the game itself plays.",
     evidence: "The default Animate script's speed calls are engine knowledge, not in the docs mirror (grep of the mirror for the script finds only server-authority/techniques.md:130-146, which shows AdjustSpeed called every frame on a walk track by game code). Not probed: no Studio.",
     smallest_fix: "P§4: 'AdjustSpeed(0) on the attack clip and the hit-reaction clip the game plays (tracks the owner holds; never the default Animate script's locomotion tracks, which that script re-speeds)'; same words in the engine-first.md hit-stop row."}
  - {id: R5, class: recommendation, check: "C8 V10 (for the lead: not this maker's files)",
     where: "animation-craft/references/roblox-playback.md:58 ('then the previous speed restored'), animation-craft/SKILL.md:68 C-25 ('restores the speed after the stop'), vfx-design/references/camera-and-screen.md:117 ('restore after the stop'); code-review/references/presentation.md:42 PT-19 (Studio gate only, no test-build check)",
     expected: "Partner books agree with the builder's hit-stop owner (P§4) and test-build rule (P§9), which the architect's presentation-contract.md:69 and the qa-lead's player-facing.md:56 already follow.",
     observed: "Four partner lines still carry the old saved-speed restore or only the Studio gate. The builder's proposals file has the exact replacement rows (proposals/feature-builder.md rows for roblox-playback.md §9, vfx-design camera-and-screen.md, code-review PT-19 / S10); reviewer proposal rows 20-21 ask the same.",
     evidence: "Lines quoted; grep of the four files.",
     smallest_fix: "The lead routes those proposal rows to the animator, vfx-designer and reviewer makers before G3, so an animator or VFX designer reading its own book does not brief a builder with the freezing rule."}
keep: [
  the feedback stack sheet tied to the architect's P-rows (P§1) and the skeleton -> presentation -> worst-case order with the §1 conditions and a check per step (EC §1, §3; role steps 4, 6, 7),
  the hit-stop owner: stop-until time, base speed as last set through the owner, restore on interruption, the overlap and speed-change offline test, the latency default and the predicted stop as its own contract row (P§4, SR-17, sword example), matching presentation-contract.md:69-70, :83,
  the test-build-only hooks with the IsStudio gate as second guard, the production-build row and its §11 false readings (my Rojo run: 0 / 4 / leak 1), the qa-lead row in the partner table,
  'one run, one setting' with the start line and cleared attributes (P§9, §11, SR-18),
  the comfort module with five settings and the Clarity override (P§5, P§6, SR-12, SR-14),
  paid reveals through the policy module, fail closed, server-sent effective odds (P§8, SR-15, egg example), in line with platform-policy P-01, P-02 and U-15's P-03 clause,
  the §5 rule 6 predicted-row exception, the §6 self-review with named inputs and a six-still budget, the EC-17..EC-25 one-line pointers,
  U-S03 / U-S04 numbers-first UI checks with the still budget (light-check rule), U-S06 contrast by text tone,
  the engine-first rows and the open probes, including the replication and Device Simulator probes; every old rule kept, moved or replaced (diff walked)
  ]
verdict: pass
lesson: {type: process, cause: "each round's sample tree for the literals grep was built from the misses the last reviewer named, so every round found new common forms (single quotes, interpolation, Title Case to helpers, legacy waits, now string.format and 'Word: ' ..)", layer: book recipe, what_happened: "three rounds widened one regex", proposed_change: "a screening grep is tested on a fixed fixture of the ways Luau code builds text, timing and colour (literal, interpolation, concatenation with punctuation, string.format, helper calls, legacy and task waits, stored aliases) written once before the first run"}
</spec>
```

## Round 2 findings
| Id | Status | Where it is now |
| --- | --- | --- |
| F1 hooks publish with the game | fixed | P§9 :87-88 (test build only, IsStudio second guard), P§10 :134 production-build row, §11 :154, SR-18, EC-24, role Write scope :66, role qa-lead row :51; agrees with code-review testing.md:16 and player-facing.md:56. My Rojo run confirms the check (R3 hardens it) |
| F2 qa-lead row 31, architect row 25 | fixed | coverage table d answers both; P§10 :138 has `BrickColor\.`; P§4 :52-54 clients, replication question, predicted row; probes.md §4 :105; engine-first.md :35; H§14 :231 |
| R1 grep misses | fixed | P§10 :138 widened pattern, §11 :150 lists (R1 above: two more forms) |
| R2 §5 rule vs predicted stop | fixed | EC §5 :76 exception; P§2 :28, P§4 :54 |
| R3 base speed | fixed | P§4 :52 'the speed the game last set ... through the owner', SR-17, sword example (R4 above: which tracks) |
| R4 up to 40 stills | fixed | ui-basics §6 :65 budget, U-S03, U-S04 numbers reads (R2 above: one wrong engine note) |
| R5 restricted player | fixed | U-15 :51 P-03 clause |
| R6 saved hook attributes | fixed | P§9 :90, §11 :153, SR-18 |
| R7 role steps unconditioned | fixed | role :34, :36, :37 |

## Result per check
| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass (52 rows checked, 0 failed) | 52 of 52 matrix ids in table a; every landed-in location opened against the finding's principle, apply and check lines; partial rejections (MD-05, PP-09, SD-16) and role splits (GD-06, PP-11, WL-29) sound. |
| C2 core principles | pass | EC §7 covers the 10 principles the master tags for feature-builder (UP-01, 02, 07, 08, 13, 15, 16, 17, 19, 20) plus 4, 6, 12, 14, 18, each with its own example and check; no contradiction with the master's engineering lines. |
| C3 self-review | pass | SR-01..SR-19 and U-S01..U-S13 name their inputs and run with Studio MCP reads, the debug log, grep, offline tests, Rojo and look_check contrast; still budgets stated. R2 corrects one note inside U-S03. |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules, the job card or the binding skills. One engine note unsupported by the docs (R2) and one ambiguous track scope (R4), both recommendations. Script Sync / studio mode gap for the build check (R3). |
| C5 nothing lost | pass | Every removed line walked: kept, moved (EC-06 facts to luau-current.md), sharpened or replaced by something at least as good; matches table c. |
| C6 fixed rules | pass | Only the 8 listed books (plus the job's own files) changed for this role; frontmatter byte-identical to df13ff4; SKILL.md 127 and 83 lines; descriptions 376 and 394 characters; headings only extended or appended; J018 phrase in all 8 files and the role comment; no library ids, transcript lines, Riot names or tips section; evals/ unchanged. sync_harness --check shows the generated copies stale: the lead's sync before commit. |
| C7 better work | yes | See below. |
| C8 brief v2/v3 | pass | V1 pass (inputs and still budgets named); V2 pass (look_check contrast, rojo build, grep: real modes); V3 my runs: production-build check right (0 / 4 / leak 1), stale-file reading (R3), grep misses two common forms (R1); V4 pass (P-01, P-02, P-03, § A); V6 pass; V7 pass (§6 at 16.2-21.8 KB, §1 re-read line); V8 pass (sheet, partner asks, self-review); V10 pass for these books (R5 is partner books, for the lead); V11 pass (every row answered); V12/V13 pass. |

**Better work (C7).** Typical job "add a Sell button that turns the backpack into coins", and eval E-03 "text is unreadable on small phones". With the old books the agent builds a safe server sale and a scaled screen and stops: no press timing, no pending, no refusal text, a label per coin, screenshots at four sizes as the only check, hooks and debug log not even named. With the new books it writes the feedback stack, plays a skeleton first, fires the press cue in the input frame, pays out only on the server's result, says "Backpack empty" at the control, merges "+N" labels, keeps the counter true, reads every tween and string from tables, proves it with the Reject, DelayMs and Rate hooks in a test build that never ships, and checks the screen with numbers (bounds and TextFits for every state and size) before a few stills. That is clearly better work, and every blocking defect of rounds 1 and 2 (frozen hit-stop, direct PolicyService, missing comfort settings, hooks in the published place, unanswered partner rows) is gone. Weak spots left, all recommendations: the literals grep still misses string.format text and "Word: " .. (R1); the U-S03 note that a TextScaled label always fits works against E-03 (R2); the production-build check can read a stale file and has no route for Script Sync or studio mode (R3); "the attacker's and target's tracks" should name the action and hit-reaction clips (R4); four partner lines still carry the old restore and gate rules until the lead routes the filed proposals (R5). The engineering-craft SKILL.md is still about twice its old length with the self-review ending near 22 KB; the §1 re-read line makes that acceptable, but it is the next place to cut.
