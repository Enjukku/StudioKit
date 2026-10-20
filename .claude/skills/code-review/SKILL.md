---
name: code-review
description: Review Roblox Luau changes - especially code AI agents wrote - for the things that hurt players most, in order - lost or duplicated data, exploitable requests, money and policy mistakes, leaks and yields, performance at scale, structure, outdated Luau and over-building. Also sets which tests a change needs and when a test result counts. Use before merging any change, for "review this", "is this safe", "why did this break", and after a builder agent hands back code. Reports findings with evidence; does not rewrite the change.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 6. Evidence: owner research papers (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-20, A-23; `roblox-operations-2026-10.md`), the kit's engineering skills and the Roblox docs mirror.

# Code review: find what would hurt players, prove it, rank it

## 1. When this skill starts
A change is ready to merge, a builder handed back code, or something broke. The reviewer needs the brief or feature plan (intent), the diff, and the test results. Without the intent, ask for it: a diff alone cannot show missing behaviour.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Which tests the change needs; when a result counts; fixtures | `references/testing.md` |
| Current Luau and outdated habits | `references/luau-current.md` |
| The rules each area must keep | `data-saving`, `networking-security`, `platform-policy`, `performance`, `ui-basics`, `architecture` skills |

## 3. Steps
1. **Read the intent**: brief, invariants, owned files, non-goals. Note what the change must not touch.
2. **Check scope**: files changed vs files owned; unasked refactors or new dependencies are findings.
3. **Walk the harm order** (§4 table), each area against its skill.
4. **Check the tests** against `references/testing.md`: right lane, failure cases from the brief, result counts.
5. **Prove each finding**: file:line, the input or sequence, the wrong outcome. Re-read the code to confirm before reporting; drop what you cannot show.
6. **Report** findings, most harmful first, each with a fix direction (not a rewrite). Say what you did not check.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| V-01 | **Harm order:** (1) saved data lost, corrupted or duplicated; (2) a client can gain rewards, items, permission or damage; (3) money and policy (receipts, odds, prices, filtering); (4) leaks, yields, lifetimes, races after waits; (5) performance at peak; (6) structure (owners, contracts, locality); (7) outdated or invented APIs; (8) over-building. Style is the tools' job | A-23 (fix by harm and blast radius) |
| V-02 | **Adversarial questions** for every change: where is authority duplicated? which callback can outlive its owner? what happens after a yield (player left, character respawned, round ended)? can a retry repeat a side effect? does a config or data change bypass validation? what does the worst client input do? | A-20 |
| V-03 | **Intent over diff.** Missing behaviour (a failure path, a cleanup, a check) is the most common defect in generated code and never shows in a diff: compare against the brief's invariants and failure cases | A-20; `architecture` R-01 |
| V-04 | **APIs must exist.** Every engine call, property and enum in the change is checked against `_api-reference/` (and its deprecation notes); invented or deprecated APIs are findings | `AGENTS.md` §0 (docs mirror first) |
| V-05 | **Tests must be able to fail.** Expected results come from the brief, not from the code; zero tests or skipped tests are a fail; spot-check one test against a deliberately wrong version | `references/testing.md` |
| V-06 | **Evidence or nothing.** Each finding: file:line, a concrete failure scenario (input → wrong outcome), severity. "Might be a problem" without a scenario is not reported | ours |
| V-07 | **Concurrency is reviewed as sequences:** two servers, two players, leave mid-save, respawn mid-ability, duplicate requests. Write the sequence in the finding | `data-saving` D-04, D-11; `networking-security` N-02 |
| V-08 | **Lifetimes:** every `Connect`, `task.spawn/delay`, tween and `Instance.new` has a cleanup owner; the reviewer names the owner or reports the leak | `architecture` R-11 |
| V-09 | **Scope discipline:** changes outside the owned files, unrequested renames, new packages or layers are findings, even if they work | `rules/packages.md`; `architecture` R-09 |
| V-10 | **Report what was not checked** (no Studio run, no device test, teleport untestable in Studio) with the labels gate-verified / MCP-verified / owner-confirmed / not verified | `AGENTS.md` §3 |
| V-11 | **Over-building is a finding, nitpicks are not.** Apply the reviewer checks in `rules/anti-overengineering.md` (unplanned files, one-caller abstractions, defensive code around our own code, out-of-scope edits, extra tests, stubs). Do not report style or "could be nicer" items: chasing every gap is itself over-engineering. Depth follows risk (quick / standard / deep); after 3 rounds on one approach, escalate to the lead instead of another round; later rounds review only the new diff; findings in untouched code are tagged pre-existing follow-ups | `rules/anti-overengineering.md` 18-20; claude.dev/blog/solving-code-review-at-anthropic (2026-10-15) |

## 5. Rules (final check)
- Changes touching purchases, currency, saves, trades or client-callable methods always get this review before merge.
- A finding without a failure scenario is not reported.
- The reviewer does not rewrite the change; it reports, and the builder fixes.

## 6. Self-check before returning
- [ ] Intent read; scope compared with owned files.
- [ ] All 8 harm areas walked; skipped ones named with the reason.
- [ ] Every finding has file:line, scenario and severity, and was re-checked in the code.
- [ ] Test lane and test quality judged.
- [ ] Unchecked items listed with verification labels.

Project overlay: if `knowledge/overlays/code-review.md` exists, read it after this file; it wins for this game.
