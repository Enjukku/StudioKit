---
name: engineering-craft
description: How engineers build Roblox features right the first time - behaviour contract before code, read the real code and docs, engine features before custom systems, Studio probes, current Luau, tests at scale, hand-offs. Use for any code task, "build this feature", "fix this bug", "is there a Roblox feature for this", "why does the engine do that", and before code goes to review.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. J010. Evidence: owner engineering paper (`knowledge/reference/engineering/paper/part-1..3.md`, P-ids; fact-checked in `factcheck-engine.md`, `factcheck-practice.md`), the DestructionSimulator rework study (`knowledge/reference/engineering/rework-study.md`; row ids such as A01, B08 point into `rework/`), the Roblox docs mirror (paths relative to `knowledge/external/roblox-creator-docs/`).

# Engineering craft: build it right the first time

Most rework in the first game was not hard physics. It was process: tests on toy cases (45 of 159 rounds), no measurement before building (25), "done" without a real check (10), and guesses about the engine (5 tasks). This book is the habits that prevent those, plus the loop for problems that stay hard even for expert teams.

## 1. When this skill starts
Any task that writes or changes Luau, content tables that code reads, or place settings. For a new system or a refactor, the architect's plan (`architecture` skill) comes first; for a small, exact change, start at §3 step 1 and keep every step short.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Which Roblox feature already does the job, its docs page, what custom work is fair | `references/engine-first.md` |
| How to write a Studio probe; engine behaviours that surprised the first game | `references/probes.md` |
| The hand-off briefs between the engineering roles and to the other crafts | `references/handoffs.md` |
| Outdated Luau habits and language status | `code-review` → `references/luau-current.md` |
| Test lanes, verdicts, oracles, planted-fault checks | `testing` skill |
| Measuring before and after (hard problems, performance) | `performance` → `references/measure-loop.md` |
| Remotes, saves, money, policy | `networking-security`, `data-saving`, `platform-policy` |

## 3. Steps
1. **Write the behaviour contract** (EC-01). If a design answer is missing, return `needs-decision` with options; do not invent the owner's answer.
2. **Read the real code** you will touch and its callers, then the docs mirror page for **every engine system** you touch (EC-02). List them under "Docs read" in the hand-back.
3. **Engine gate** (EC-03): name the built-in feature for each part. If the design relies on engine behaviour the docs do not state, **probe it** in Studio first (EC-04).
4. **Plan the smallest change**: the files, why each one, what stays untouched (`rules/anti-overengineering.md`).
5. **Write the failing case first**, on the real content, data and scale the brief names (EC-09).
6. **Build.** Strict types, clear names, failures explicit (EC-06, EC-07). For hard-by-nature work, use the loop in EC-05.
7. **Check the exact code**: analyzer, tests, and the Studio run the claim needs (EC-10). Record each check as PASS, FAIL, BLOCKED or NOT RUN.
8. **Hand back** with the change manifest (EC-13) in the `rules/messages.md` §3 shape.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| EC-01 | **Behaviour contract before code.** Nine fields: existing behaviour; intended change; examples with expected outcomes (one normal, one boundary, one old behaviour that must stay); engine APIs involved; files and callers affected; allowed scope; non-goals; acceptance checks; open design questions. "Make it production ready" is not a contract. A vague brief cost 3-6 rounds per task in the first game | P302, P139; study C06, C11, C12 |
| EC-02 | **Read before writing, docs for every engine system.** Read the implementation and its callers, not file names or a summary. Grep the docs mirror and `_api-reference/classes/<Class>.yaml` for every class, property and enum you use. Missing docs pointers in a brief caused the lighting rework (invented `Bloom` class) | P140, P141; study B08, records SR4 |
| EC-03 | **Engine features first.** Custom game rules are fine; custom **infrastructure** needs a reason. Before you replace an engine mechanism, answer in the hand-back: which built-in you evaluated (docs page), what concrete requirement it failed (with evidence: a probe, a measurement or a docs line), how the replacement will be measured. The first game rebuilt shadows, motion and resting and later deleted or reversed all three | P116, P201; study B09, A07, records SR1; `references/engine-first.md` |
| EC-04 | **Probe what the docs do not say.** When your design depends on engine behaviour the docs leave out (sleep, replication timing, spawn order, stepping, query bounds), run a short Studio probe (`execute_luau` or a play-test, under 30 lines, one question) before you build on it, and cite its output. Every probe the first game ran overruled a guess | old-agents GP3; study A11, A17, B17, E7; `references/probes.md` |
| EC-05 | **Hard-by-nature loop** (physics, destruction, explosions, phone performance). These need measuring and tuning even for expert teams. (1) Reproduce with a fixed recipe and record the baseline. (2) Change one thing. (3) Measure the same recipe again, 3+ runs, report the spread. (4) Ship new behaviour behind a default-off switch whose off state is byte-identical to the old behaviour, then A/B in Studio before you switch it on. Offline speed-ups were invisible in Studio in the first game; the Studio soak found the real lag cause | study B02, L04, EG9; old-agents HB1; `performance` → `references/measure-loop.md` |
| EC-06 | **Current Luau.** `--!strict` in shared and server code (`AGENTS.md` §2); new client modules too where the API types allow. `unknown` plus refinement (type test, `assert`, equality) over `:: any` or casts; `export type` the public shapes; generics only to keep an input-output relation. Tables: `table.clone` is shallow (keeps the metatable), `table.freeze` is shallow and errors on a frozen table, `table.clear` keeps capacity, `table.create(n)` reserves array space only. Iteration: array part in order, the rest in no order; never mutate keys you are not visiting; collect and sort keys when order matters. `const` stops reassignment, not mutation (compiles in Studio, probe 2026-10-21); `if local` is Studio beta, do not ship; the non-type `export` keyword was rolled back (2026-08-26). Native code: server `Script`s, numeric work, measured with and without. More rows: `code-review` → `luau-current.md` | P175-P195; factcheck-engine §3-4 and lead addendum |
| EC-07 | **Clear code shape.** The direct solution with the right data structure; built-ins with the needed meaning (`table.find`, `string.find(s, x, 1, true)`) over hand-written loops. Names carry domain meaning and units (`cooldownSeconds`, `maxStudsPerSecond`). Absence and failure are explicit at the interface (done / denied / unavailable, `architecture` R-13). Never hide an unexpected error behind a plausible default. There is no universal function length: keep a reader from jumping back and forth, and split only where a name explains a real step | P145, P146, P157-P159, P169, P196 |
| EC-08 | **Validate at boundaries, trust inside.** Client requests, saved data on load, HTTP, failing services get full checks (`networking-security` N-02 order: type, NaN/inf, range, rate, ownership, state). Inside our own code, no defensive checks for states our types and owners rule out | `rules/anti-overengineering.md` 9-10 |
| EC-09 | **Tests on the real thing.** The failing case first (in the first game, a spec that failed before the fix closed the bug in one more round). Then test with the real content table, the real layout or the scale the brief names, not only a toy case: toy-case tests were the biggest single cause of rework. A symptom seen twice gets one shared check, not a second one-off tool | study A05, A14, B05, C16, old-agents FB5, GP4; `testing` skill |
| EC-10 | **Done means checked, on the exact code.** Run the analyzer and the tests on the revision you hand in and read the output. A claim about performance, physics, feel or engine behaviour needs Studio evidence (MCP-verified) or it is `not verified`, and that item is not `done`. 15 hand-ins in the first game said "Not Studio-verified" honestly and were merged anyway | P147, P151; study A16, B13, C01; `AGENTS.md` §3 |
| EC-11 | **Stop when the API cannot do it.** If the documented API cannot meet the contract, stop that part and return: the unsupported assumption, the probe or docs line that proves it, the smallest alternatives, the player-facing trade-off. Never quietly build a nearby behaviour | P314, P150 |
| EC-12 | **Third patch, stop.** The same symptom patched a third time means the approach is wrong: stop and return to the architect with the three attempts and what each measured. In the first game this ended two long patch chains in one design | old-agents FB11, HB8; records B26 |
| EC-13 | **Change manifest** in every code hand-back: requirement ids covered; files changed; public behaviour or API shape changed; dependencies added; test commands with their results; environment (Studio build, Luau version); performance-sensitive paths touched; open questions; what is generated or temporary. The reviewer reads intent from it | P313, P152 |
| EC-14 | **Placement is download size and security.** Server-only code and data in ServerScriptService or ServerStorage; everything under Workspace and ReplicatedStorage replicates to every client. The first game's rule text sent 5.2 MB of stage data and 1.56 MB of server code to every client, and 32k invisible collider Parts replicated | study R02, EG4, EG5; `performance` F-06 |
| EC-15 | **One source for shared lists.** A list that two places need is derived from one config table, never typed twice; shared registries have one named owner and others ask through a ticket | study C24, C23 |
| EC-16 | **Technical choices are yours; only design forks go to the owner.** Budgets, limits, caps, fallbacks and test design are engineering calls: write them as `PROPOSAL` values and list them in `knowledge/design/open-questions.md` (`AGENTS.md` §0), do not ask them. Ask the owner only where the answer changes what players see or do and no owner decision already answers it, each with a default. The owner wants one recommendation, not option menus, for technical choices (`rules/owner-profile.md`) | J010 architect scores: 2 of 3 tasks lost on misrouted questions |

## 5. Rules (final check)
- No custom replacement of an engine mechanism without the EC-03 answer in the hand-back.
- No engine assumption the design depends on without a docs line or a probe result.
- No performance, physics or feel claim marked `done` without Studio evidence.
- No edit to hidden or protected tests, expected results or acceptance fixtures; a wrong test is reported, not worked around.
- No work outside the brief's files; extra problems go in the hand-back as follow-ups.

## 6. Self-check before returning
- [ ] Behaviour contract written; design gaps returned as `needs-decision`, not guessed.
- [ ] "Docs read" lists a mirror path for every engine system touched; probes cited.
- [ ] Failing case first; tests use the real content or scale the brief names.
- [ ] Analyzer and tests run on the handed-in revision; every check labelled PASS / FAIL / BLOCKED / NOT RUN.
- [ ] Change manifest complete; temporary files removed.

Project overlay: if `knowledge/overlays/engineering-craft.md` exists, read it after this file; it wins for this game.
