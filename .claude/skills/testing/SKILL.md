---
name: testing
description: Plan, write and run the tests that prove a Roblox change works for players - acceptance checks traced to the brief, real content and scale, oracles, planted faults, protected tests, verdicts PASS / FAIL / BLOCKED / NOT RUN. Use for "plan the tests", "is this tested", "does it really work", "prove it", "why did this come back", and before accepting a feature.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. J010. Evidence: owner engineering paper §7, §10, §11 (`knowledge/reference/engineering/paper/part-2.md` P249-P266, `part-3.md` P321-P349; fact-checked in `factcheck-practice.md`), the DestructionSimulator rework study (`knowledge/reference/engineering/rework-study.md`), `code-review` → `references/testing.md` (lanes, fixtures, tool notes).

# Testing: prove it works, on the real thing

The first game's biggest source of rework was tests that passed on toy cases while the real stage, scale or content broke (9 tasks, 45 rounds). Its best habits were the fixes: failing case first, a random-update oracle, old-vs-new tests with planted bugs. This book makes those the default.

## 1. When this skill starts
A brief or feature plan exists with behaviour to accept, or a bug came back. Without a statement of intended behaviour there is nothing to test against: ask for it (`engineering-craft` EC-01).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Test lanes (gate, merge, nightly, release), fixtures per area, tool status | `code-review` → `references/testing.md` |
| Oracles, planted faults, scoring a suite, Studio and multi-client scenarios, tools by job | `references/methods.md` |
| Rework record, cause list, result card for the owner | `references/records.md` |
| Save, remote and money cases | `data-saving`, `networking-security`, `platform-policy` |
| Performance acceptance | `performance` → `references/measure-loop.md` |

## 3. Steps
1. **Trace table first.** One row per behaviour, rule and failure case in the brief (and per binding rule the change touches: validation, server authority, saves): the check that proves it, its lane, its data. A behaviour with no row is untested; a test with no row is extra (`rules/anti-overengineering.md` 11).
2. **Pick the data.** At least one check per behaviour uses the real content table, the real layout or the scale the brief names (T-03).
3. **Pick the oracle** for each row (T-04): an exact expected value from the brief, an independent model, a property over random sequences, or old-vs-new equality.
4. **Write and run** the tests. Each must be able to fail: run the planted-fault check (T-05).
5. **Protect the acceptance set** (T-06) and run it on the exact candidate revision.
6. **Report** with the verdict words (T-07), the result card for the owner (`references/records.md`), and a rework record for every repair round.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| T-01 | **Tests come from the brief, not from the code.** Expected results are written from the stated behaviour before or apart from the implementation; the builder adds tests but never changes those expected results. Code and tests written from one wrong assumption agree with each other | `code-review` testing.md; P307, P311 |
| T-02 | **Failing case first for every bug.** Reproduce it as a test that fails on the old code, keep that failed result, fix, keep the test. In the first game a bug with a pre-fix failing spec closed in one more round | P322 (Wube, 2021); study old-agents FB5 |
| T-03 | **Real content and real scale.** A check on a three-piece toy is not evidence for a 20,000-piece stage. Run at least one check on the shipped content table or layout, at the scale and player count the brief names, and on the owner's reported scene when there is one | study A05, A14, A21, B05, B20, B21, C02 (old-agents GP4) |
| T-04 | **An oracle that knows more than the code.** Hand-written cases catch what the writer imagined. For rules over many states (support, economy, inventory), add many random action sequences checked against an invariant or an independent simple model; for a "behaviour-identical" change, an old-vs-new differential test. The random-update oracle ended a six-round task (45-52 missed cases per 240 updates before, 0 in 384 after) | study A05 (3ddcecc8b); git-b §4 differential lanes |
| T-05 | **A suite must be able to fail.** Plant faults one at a time (drop a check, grant twice, skip a cleanup, off-by-one at the boundary) and confirm the suite catches each; a planted fault that survives is a missing test. The correct build must pass every test: a failure there is a false alarm. Keep unseeded controls | P344, P346; `code-review` testing.md |
| T-06 | **Protected acceptance.** The acceptance tests and their expected results live where the builder cannot write (outside its folder or worktree). If they are not protected, say "visible to the builder" in the result. One agent must not invent the fault, pick its trigger and grade its own detection | P282, P337, P346 |
| T-07 | **Verdict words, bound to the revision.** PASS, FAIL, BLOCKED (could not run: missing device, service, access), NOT RUN (not attempted), RUNNER FAILED (the tool broke, not the product). Each result names the revision, runtime (Studio build, Luau version), scenario, seed, expected and observed, and the raw log path. "Tested" without that is NOT RUN. A pass earned by an older revision does not carry over | P151, P251, P277, P312 |
| T-08 | **One shared check per repeated symptom.** A symptom seen twice gets one check that runs for every layout or feature, in the gate; never a third one-off tool. "Nothing falls at load" was fixed three times with three tools in the first game | study C16, C25, C26, S1 |
| T-09 | **Choose the test boundary that holds the failure.** Pure rules: offline Luau with injected fakes. Engine behaviour (physics, replication, streaming, input, sleep): a Studio scenario; a fake cannot prove it. Do not mock everything: a test may use other tested subsystems when that is where the bug lives | P369 (Wube); P265; `engineering-craft` EC-04 |
| T-10 | **Lifecycles and concurrency are sequences.** Respawn, reset, reopen ×20 with connection and instance counts back to baseline; two players on one reward; leave mid-save; rejoin before the save finishes. Write the sequence as the test name | `code-review` testing.md; `architecture` R-11 |
| T-11 | **Engine proof is separate from tools.** A test framework, a build tool (Rojo `build`), a runner (Studio, Open Cloud Luau Execution) and engine proof are four different things: a build that succeeds is not a test that passed; Luau Execution runs no physics and no auto-running scripts | P256, P265; factcheck-practice correction 5 |
| T-12 | **Report first attempt apart from repairs.** For acceptance and for agent scoring: did the first handed-in candidate pass the frozen checks; how many repair rounds; what was blocked or skipped. Do not let a pre-submission repair loop be called "first try" | P136, P332, P333, P338 |

## 5. Rules (final check)
- No behaviour accepted on a test that has never failed against a planted fault.
- No accepted change whose checks ran on a different revision.
- No edit to protected acceptance tests by the builder; a wrong acceptance test is reported to the briefer.
- Phone performance without a physical phone is BLOCKED, never PASS.
- Teleport and published-only behaviour is NOT RUN in Studio until a published test.

## 6. Self-check before returning
- [ ] Trace table covers every behaviour, failure case and touched binding rule.
- [ ] At least one check per behaviour on real content or real scale.
- [ ] Planted-fault check run: caught x of n; correct build passes all.
- [ ] Every result has a verdict word, revision, runtime and log path.
- [ ] Result card and rework records written.

Project overlay: if `knowledge/overlays/testing.md` exists, read it after this file; it wins for this game.
