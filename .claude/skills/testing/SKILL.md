---
name: testing
description: Plan, write and run the tests that prove a Roblox change works for players and what they see matches the server - acceptance checks traced to the brief, real content and scale, oracles, planted faults, protected tests, verdicts PASS / FAIL / BLOCKED / NOT RUN. Use for "plan the tests", "is this tested", "does it really work", "prove it", "why did this come back", and before accepting a feature.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. J010. Evidence: owner engineering paper §7, §10, §11 (`knowledge/reference/engineering/paper/part-2.md` P249-P266, `part-3.md` P321-P349; fact-checked in `factcheck-practice.md`), the DestructionSimulator rework study (`knowledge/reference/engineering/rework-study.md`), `code-review` → `references/testing.md` (lanes, fixtures, tool notes). Rebuilt by J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (player-facing rows and their oracles, the conditions players meet it in, test hooks asked for at plan time, what each input can prove, the self-review by stage in §6, core principles in §7); repair rounds 1 and 2 after the stage 3 reviews (J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22).

# Testing: prove it works, on the real thing, where players meet it

The first game's biggest source of rework was tests that passed on toy cases while the real stage, scale or content broke (9 tasks, 45 rounds); its fixes were failing case first, a random-update oracle, old-vs-new tests with planted bugs. This book makes those the default, and adds the other half of "it works": what the player sees and hears tells the truth about what the server decided, under the conditions players really play in.

## 1. When this skill starts
A brief or feature plan exists with behaviour to accept, a craft's work is wired into the game and needs its technical check, or a bug came back. Without a statement of intended behaviour there is nothing to test against: ask for it (`engineering-craft` EC-01). After a context compaction, re-read §3, §6 and §7 of this file before you continue.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Test lanes (gate, merge, nightly, release), fixtures per area, tool status | `code-review` → `references/testing.md` |
| Oracles, planted faults (code and presentation), scoring a suite, engine scenarios, tools by job | `references/methods.md` |
| Player-facing rows: conditions matrix, the row catalogue (PF-01 to PF-16), test hooks to ask for, the measures borrowed from partner books with their false readings | `references/player-facing.md` |
| Three worked trace tables (ground slam, paid egg shop, coin burst) | `references/worked-examples.md` |
| Rework record, cause list, finding format, result card for the owner | `references/records.md` |
| Save, remote and money cases; paid random items | `data-saving`, `networking-security`, `platform-policy` (§A wins over any line here) |
| Performance acceptance | `performance` → `references/measure-loop.md` |
| Driving Studio (ids, play, probes, camera restore) | `studio-mcp` |

## 3. Steps
1. **Collect the sources of truth before any test.** The brief or behaviour contract; the architect's invariants, failure cases and presentation contract (its check seeds become rows); the feature contract's state names and event ids; when the change is visible, the partners' sheets that hold its truths (list: `player-facing.md` §3). Name each with its revision. A missing fact is a question to the briefer, never a guess. *Check:* every source is listed with its revision before the first row.
2. **Trace table first.** One row per behaviour, rule and failure case in the brief, per binding rule the change touches (validation, server authority, saves, paid random items), and per player-facing truth the change carries (`references/player-facing.md` §2: the PF-rows that apply, or "n/a" with the reason). Each row: the check, its lane, its data, its oracle, its conditions, its input. A behaviour with no row is untested; a test with no row is extra (`rules/anti-overengineering.md` 11). *Check:* QS-01 to QS-05.
3. **Ask for the test hooks now, not at acceptance.** From the rows, list the hooks the builder must deliver with the candidate by the builder's hook names (`references/player-facing.md` §3: `Reject`, `DelayMs`, `Trigger`, `Rate`, `DebugShape`, `Reduced`, `Clarity`, `Viewer`, `FxLog`, `Outcome` or `Seed` to force a result or roll, `Set` for test state), and the captures you need from the studio-operator or the owner (two clients, device). Send them as a ticket against the plan or the feature contract. *Check:* QS-06.
4. **Pick the data and the conditions.** At least one check per behaviour uses the real content table, the real layout or the scale the brief names (T-03). Each player-facing row names the conditions it runs under, chosen by risk from the conditions matrix (`player-facing.md` §1): game camera, smallest phone viewport, busiest moment, lowest and highest graphics quality, two clients, added latency, reduced motion, grayscale, sound off. *Check:* QS-07, QS-08.
5. **Pick the oracle** for each row (T-04, T-15): an exact expected value from the brief, an independent model, a property over random sequences, old-vs-new equality, or for what players see the gameplay data itself (server value, server shape, server timer, server result in the log). Never your eye as the oracle for a truth. *Check:* QS-09, QS-10.
6. **Write and run** the tests. Each must be able to fail: run the planted-fault check with code faults and presentation faults (T-05, `methods.md` §2). *Check:* QS-11, QS-12.
7. **Protect the acceptance set** (T-06) and run it on the exact candidate revision: offline Luau, Studio scenarios (3+ runs for physics), the conditions each row names. *Check:* QS-13 to QS-16.
8. **Report** with the verdict words and the input each result rests on (T-07, T-20), findings as problems with evidence (`references/records.md` §3), the could-not-check list, the result card for the owner, a rework record for every repair round, and one named weakness of your own test set. *Check:* QS-17 to QS-21.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| T-01 | **Tests come from the brief, not from the code.** Expected results are written from the stated behaviour before or apart from the implementation; the builder adds tests but never changes those expected results. Code and tests written from one wrong assumption agree with each other | `code-review` testing.md; P307, P311 |
| T-02 | **Failing case first for every bug.** Reproduce it as a test that fails on the old code, keep that failed result, fix, keep the test. In the first game a bug with a pre-fix failing spec closed in one more round | P322 (Wube, 2021); study old-agents FB5 |
| T-03 | **Real content, real scale, real conditions.** A check on a three-piece toy is not evidence for a 20,000-piece stage, and a check in an empty scene on a desktop window is not evidence for a phone in the busiest fight. Run at least one check on the shipped content table or layout, at the scale and player count the brief names, on the owner's reported scene when there is one, and under the conditions its row names (§3 step 4) | study A05, A14, A21, B05, B20, B21, C02 (old-agents GP4) |
| T-04 | **An oracle that knows more than the code.** Hand-written cases catch what the writer imagined. For rules over many states (support, economy, inventory), add many random action sequences checked against an invariant or an independent simple model; for a "behaviour-identical" change, an old-vs-new differential test. The random-update oracle ended a six-round task (45-52 missed cases per 240 updates before, 0 in 384 after) | study A05 (3ddcecc8b); git-b §4 differential lanes |
| T-05 | **A suite must be able to fail.** Plant faults one at a time (drop a check, grant twice, skip a cleanup, off-by-one at the boundary, a success layer on a rejected request, a ring sized from its own constant) and confirm the suite catches each; a planted fault that survives is a missing test. The correct build must pass every test: a failure there is a false alarm. Keep unseeded controls | P344, P346; `code-review` testing.md |
| T-06 | **Protected acceptance.** The acceptance tests and their expected results live where the builder cannot write (outside its folder or worktree). If they are not protected, say "visible to the builder" in the result. One agent must not invent the fault, pick its trigger and grade its own detection | P282, P337, P346 |
| T-07 | **Verdict words, bound to the revision and the input.** PASS, FAIL, BLOCKED (could not run: missing device, service, access, second client), NOT RUN (not attempted), RUNNER FAILED (the tool broke, not the product). Each result names the revision, runtime (Studio build, Luau version), scenario, conditions, seed, expected and observed, the raw log or capture path, and its label (gate-verified, MCP-verified, owner-confirmed, not verified). "Tested" without that is NOT RUN. A pass earned by an older revision does not carry over | P151, P251, P277, P312; `AGENTS.md` §3 |
| T-08 | **One shared check per repeated symptom.** A symptom seen twice gets one check that runs for every layout or feature, in the gate; never a third one-off tool. "Nothing falls at load" was fixed three times with three tools in the first game | study C16, C25, C26, S1 |
| T-09 | **Choose the test boundary that holds the failure.** Pure rules: offline Luau with injected fakes. Engine behaviour (physics, replication, streaming, input, sleep, rendering at a quality level): a Studio scenario; a fake cannot prove it. Do not mock everything: a test may use other tested subsystems when that is where the bug lives | P369 (Wube); P265; `engineering-craft` EC-04 |
| T-10 | **Lifecycles, concurrency and repetition are sequences.** Respawn, reset, reopen ×20 with connection and instance counts back to baseline; two players on one reward; leave mid-save; rejoin before the save finishes; a frequent event at its real rate (100 at one per second) and its burst rate. Write the sequence as the test name | `code-review` testing.md; `architecture` R-11 |
| T-11 | **Engine proof is separate from tools.** A test framework, a build tool (Rojo `build`), a runner (Studio, Open Cloud Luau Execution) and engine proof are four different things: a build that succeeds is not a test that passed; Luau Execution runs no physics and no auto-running scripts | P256, P265; factcheck-practice correction 5 |
| T-12 | **Report first attempt apart from repairs.** For acceptance and for agent scoring: did the first handed-in candidate pass the frozen checks; how many repair rounds; what was blocked or skipped. Do not let a pre-submission repair loop be called "first try" | P136, P332, P333, P338 |
| T-13 | **Test where players meet it.** A presentation row passes only under the conditions players have: game camera, the smallest supported phone viewport, the busiest expected moment with every player's effects and the HUD on, lowest and highest graphics quality, two clients when other players matter. An empty scene on a desktop window proves only that the code runs | J018 |
| T-14 | **Feedback follows the real outcome.** The small attempt cue comes on the input; the big layer, the reward sound and the celebration come only on the server's confirmation. Every request type gets a rejected-request row (the builder's reject hook): no outcome event, cue, layer or balance change. Under added latency a pending state shows and no success shows before the confirmation | J018 |
| T-15 | **The picture's truth comes from the gameplay data.** Drawn danger edge = the server's hit shape from warning to last tick; countdown = the server timer; counter = the server value at rest; tier shown = tier rolled. The oracle is the data field the effect reads, never a size judged by eye | J018 |
| T-16 | **Paid random items are tested as a policy area.** Identical windup for every result up to the result frame, no higher tier's layer on a lower result, and every `platform-policy` §A rule (odds before purchase, modifiers, restricted players) as its own row; a gap is a blocking finding (PF-06) | J018; `platform-policy` |
| T-17 | **Every player can read it.** With reduced motion on, sound off and in grayscale, every warning, outcome and tier keeps a second channel that exists in data and fires; the composite flash count on the busiest scene and every pulse or blink rate stay within the PF-07 caps. A comfort, flash or pulse fault blocks release (PF-07) | J018 |
| T-18 | **One code for meaning, tested as data.** Colours, cue ids, motion rows and tells live in shared tables; logic holds no hard-coded hue or asset id; the same event plays the same tell every time (two captures identical up to contact) | J018 |
| T-19 | **Variation never touches meaning.** Random ranges may move decoration only; footprint, contact time, team colour, tier and deadline stay identical. Test the range where it lives (`methods.md` §1, range row): an engine range on a layer the effect spec marks semantic is a property read on the candidate (no spread, no envelope, no random start); a range the game's code rolls runs at its lowest and highest end offline. A `Seed` run repeats a server roll and never reaches a particle range | J018 |
| T-20 | **Say what each input can prove** (`player-facing.md` §5). A check whose input cannot show it is "not verified", never PASS; every report ends with a could-not-check list | J018 |

## 5. Rules (final check)
- No behaviour accepted on a test that has never failed against a planted fault.
- No accepted change whose checks ran on a different revision.
- No edit to protected acceptance tests by the builder; a wrong acceptance test is reported to the briefer.
- No presentation truth passed by eye: a drawn area, countdown, counter or tier is checked against its data field or the server log.
- No PASS on a check whose input cannot show it (T-20).
- A rejected request that shows a success layer, a paid reveal whose windup differs by tier, a reduced mode that drops a warning, or a flash count or pulse rate over the PF-07 caps blocks acceptance.
- Phone performance without a physical phone is BLOCKED, never PASS. Sound sync without a device capture is "not verified".
- Teleport and published-only behaviour is NOT RUN in Studio until a published test.
- Test hooks ship only in the test build: the production build carries none (`code-review` testing.md).

## 6. Self-review before hand-back (each line names its input)
Mark each line PASS, FAIL, n/a (with the reason) or not verified. Inputs: **TT** your trace table and plan; **D** data tables and the feature contract; **T** test results and logs; **C** Studio MCP captures and probe output; **F** a frame folder at a known rate; **Dev** a capture on the target device (owner or studio-operator); **O** the owner at a named gate.
**Image budget (light checks, owner J005-D8):** numbers and logs for every row; stills only for a failing or borderline reading and at most 4 key stills per player-facing row (the conditions that matter most: busiest moment, smallest phone, lowest quality, reduced); frame folders only for rows that need timing. Report the stills and folders made and looked at.

**Plan**
- [ ] QS-01 (TT) Every behaviour, failure case and touched binding rule has a row; every source of truth is named with its revision (§3 step 1).
- [ ] QS-02 (TT, D) Every request type that changes state has a rejected-request row (PF-02), an outcome row per result tier (PF-03) and an attempt-cue row (PF-01) when it has a press or input.
- [ ] QS-03 (TT, D) Every visible truth has its data row: danger edge to hit shape (PF-04), countdown to server timer, counter to server value (PF-05), tier shown to tier rolled (PF-06); each names the data field.
- [ ] QS-04 (TT, D) Every state in the UI state list, every hazard rule, every event in the sound event list and every timing-list event the game reacts to is reached by a scenario (PF-11, PF-12, PF-14).
- [ ] QS-05 (TT) Paid random items, sold cosmetics, comfort settings, frequent events, effects other players see and new colours or cues have their PF-rows or a written n/a (PF-06, PF-13, PF-07, PF-10, PF-16, PF-08 with the code scan).
- [ ] QS-06 (TT) The hook and capture list went to the builder and the lead at plan time, with the row each hook serves.
- [ ] QS-07 (TT) At least one check per behaviour on real content, layout or scale.
- [ ] QS-08 (TT) Each player-facing row names its conditions from the matrix and why those (the busiest moment and the smallest phone at least once per feature with a visible part).

**Oracles and faults**
- [ ] QS-09 (TT) Each row's oracle knows more than the code: brief value, model, invariant, old-vs-new, or the data field or server log; no expected value copied from the implementation.
- [ ] QS-10 (TT) Every image measure is marked as a screening aid with its known false readings (`player-facing.md` §4); a failing or borderline reading was checked by eye on the named stills before the finding went out.
- [ ] QS-11 (T) Planted-fault result: caught x of n, false alarms y; the list holds at least one presentation fault per player-facing row group run.
- [ ] QS-12 (D, C, T) Random ranges, by where they live (T-19, `methods.md` §1 range row): every layer the effect spec marks semantic read on the candidate with no range, no envelope and `FlipbookStartRandom` false; every range the code rolls run offline at its lowest and highest end; meaning identical. A `Seed` run alone is not this check.

**Run**
- [ ] QS-13 (T, C) Every result names revision, runtime, scenario, conditions, seed, expected, observed, log or capture path and label.
- [ ] QS-14 (C, T) Rejected requests: no outcome event in the filtered log, no balance change, the refusal cue present, and one still at the refusal (an unlogged branch is invisible to the log); under added latency a pending state, no early success.
- [ ] QS-15 (C, T, F) Repetition: 100 at one per second and the burst rate; live copies within the cap, one label and one cue per merge window, the final count exact, counts back to baseline.
- [ ] QS-16 (C, F, D) Reduced motion, sound off and grayscale captures taken on the busiest scene; the flash count run with the studio counter on that folder; every pulse, blink and countdown rate read from the spec or the server timer, both against the PF-07 caps; a rate read only from the spec is labelled D, and its on-screen rate stays not verified until the box reading on a folder; every warning's second channel fired in the log.

**Report**
- [ ] QS-17 (T) Verdict words only; first attempt apart from repairs; BLOCKED and NOT RUN each with the reason and the input that would close it.
- [ ] QS-18 (TT) Could-not-check list: the step, the missing input, the capture or test that closes it (two clients, device sync and feel PF-15, published game).
- [ ] QS-19 (T) Each finding is one problem with evidence, the goal it breaks, its layer and the smallest fix direction as what must hold (never code), then the rows to retest (`records.md` §3); a wrong test went to the briefer.
- [ ] QS-20 (T) Result card and rework records written; each claim on the card points to its row.
- [ ] QS-21 (TT) One named weakness of this test set (a condition not run, an oracle that is only a screening aid) with its next step, or why there is none; the stop criteria met (§7 row 18).

## 7. Core principles for this craft
The studio's universal principles (master: `knowledge/reference/craft/riot/universal-principles.md`), stated for my work: trace tables, oracles, scenarios, verdicts and the result card. Principles 3, 4, 5, 9, 10, 11 and 14 are not mine: they judge how a thing reads or is made, which has no test oracle; their data side is tested under 1, 7, 19 and 20. Principles 6 and 12 apply in a limited form.

| # | Principle for my work | Example | My check |
| --- | --- | --- | --- |
| 1 | **The gameplay read comes first.** My first rows prove that the player can know what happened, what threatens them and what they can do; beauty is the crafts' call, but a beautiful layer that hides or contradicts state is a FAIL row | A shield glow that covers the boss's tell: the tell row fails at the busiest moment, whatever the glow looks like | QS-03, QS-08; PF-09 |
| 2 | **Judge it where players meet it.** No player-facing row passes from an empty scene on a desktop window | A ring readable on the test baseplate disappears on the lava stage at lowest quality: that run is the evidence | QS-08, QS-16; T-13 |
| 6 | **Less is more (limited).** The fewest checks that give the strongest proof: one row per behaviour and failure case, one shared check per repeated symptom, no row a craft review already owns | The VFX designer measures footprint and value; I test that the ring sits on the server's hit shape | QS-01; T-08 |
| 7 | **One code for meaning.** The same meaning is one entry in data, played the same way every time; I test the tables and the repeats, not taste | Two captures of the same boss slam: identical tell up to contact; no hue literal in logic | PF-08; T-18 |
| 8 | **Timing tells cause and effect.** The result follows its cause: the outcome event after the server decision, the telegraph removed on the damage frame, cues on the timing list's events | A celebration logged before the purchase receipt is a FAIL, not a timing nit | PF-01, PF-02, PF-04, PF-14 |
| 12 | **Variation, never on meaning (limited).** Decoration may vary; meaning may not. I read every semantic layer for ranges and run both ends of every range the code rolls | Coin bursts vary in rotation and size; the count, the label and the cue never vary; the slam ring's emitter has no size envelope | QS-12; T-19 |
| 13 | **Problem, constraints and target before tests.** The trace table, its sources and the hooks come before the first test | "Make sure the shop works" becomes 14 rows with oracles, conditions and hooks | QS-01, QS-06 |
| 15 | **Cheap stages first; gates freeze decisions.** Hooks and rows at plan time; acceptance frozen with the candidate; a closed row is not reopened without a new brief | The reject hook asked for at the plan costs one line; asked for at acceptance it costs a repair round | QS-06; T-06 |
| 16 | **Critique against the goal, one named problem at a time.** Each finding names the goal it breaks, its layer, its evidence and the smallest fix direction as what must hold; the maker decides how to build it | "Rejected sale shows coin shower (log: `outcome sell` after `reject sell`); fix direction: the coin layer waits for the server's confirmation; retest PF-02" | QS-19; `records.md` §3 |
| 17 | **Build for the next craft and the engine.** Tests, fixtures and hook requests the builder can run and read; repeated checks become shared gate checks or tool proposals | The rate-trigger test lives in the shared acceptance folder and runs for every frequent effect | QS-06; T-08 |
| 18 | **Know when it is done.** Done when every row has a verdict word, the planted faults are caught, the could-not-check list is honest and a repeat run brings no new finding; extra rows past the brief are follow-ups | A fourth repeat of a passing run is not more evidence | QS-17, QS-18, QS-21 |
| 19 | **Feedback follows the real outcome.** A rejected or pending request never shows success; the big layer scales with the confirmed result; nothing celebrates a result worth less than its cost | Sell rejected for a full backpack: refusal at the control, no coins | PF-02, PF-03; T-14 |
| 20 | **Every player can read it.** No meaning on one channel; every intense channel has an off path that keeps the warning; flashes and pulses on the composite within the PF-07 caps | Reduced motion on: the fuse blink becomes a steady glow with a fill countdown, and the log shows it fired | PF-07; T-17 |

Project overlay: if `knowledge/overlays/testing.md` exists, read it after this file; it wins for this game.
