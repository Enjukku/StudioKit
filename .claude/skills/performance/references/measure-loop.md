> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. J010. Evidence: the first game's measured practice (`knowledge/reference/engineering/rework/` git-b §4, logs §6, old-agents HB1-HB7, records §7), the owner engineering paper §6 (P237-P239, fact-checked), `references/measure.md` for tools and targets.

# The measure-change-measure loop

For problems that stay hard even for expert teams: physics, destruction, explosions, crowds, phone performance. In the first game, 4 tasks lost 25 rounds by changing code before measuring the real place, and the fixes that held all came from same-recipe before/after tables.

## 1. Before any change
| Step | What | Why (first game) |
| --- | --- | --- |
| Recipe | Write the scenario so anyone can replay it: place version, scene, player count, camera position, seed, quality level, warm-up time, run length, the stress (for example "3 collapses, then 60 s idle") | one recipe gave a standing building in one run and a pancake in the next; a fixed recipe made runs comparable |
| Budget first | Write the pass line before you measure: frame p95, worst frame, memory, network, Part count. No game budget → `references/budgets.md` as PROPOSAL. The studio's test default (owner J010-D2): p95 ≤ 16.7 ms and worst frame ≤ 50 ms after the stress, server and client | a pre-set budget turned the lag hunt into one checkpoint (p95 23.6 → 0.77 ms) |
| Labels | `debug.profilebegin/profileend` around our systems (F-08); a per-frame cost ledger before any fix | the ledger found the real costs; the review's ranked guesses did not |
| Baseline | Run the recipe 3+ times on the current code; record median, worst and spread | a pre-existing cost is then not blamed on the change |

## 2. Hygiene (or the numbers mean nothing)
- One Studio instance, one driver, Studio in the foreground, no other agent's work on the machine during the run.
- No `LogService` scans, Output floods or screenshots during a timed run (they added 140-1,800 ms frames).
- Play Solo runs server and client in one process: report it as such; use a local server with clients when the question is server vs client.
- Alternate the arms in one session (A, B, A, B) instead of A all morning and B after lunch; report ratios as well as times.
- Treat differences inside the run-to-run spread (the first game used about 2 ms) as noise.
- A probe or counter needs a positive control: a case where you know the answer.
- A run with zero samples is invalid, not a pass.

## 3. The change
- One change at a time, the one the capture names (`references/fixes.md`).
- New behaviour ships behind a default-off switch whose off state is identical to the old behaviour (golden hash, byte-identical packets); switch it on only after the Studio A/B passes. No switched feature shipped as a regression in the first game.
- A speed-up claimed as "behaviour-identical" needs an old-vs-new differential test with planted bugs.
- Measure a candidate fix before it becomes the default, even inside the same task (one cache made things 4.6× slower and was caught this way).
- Offline (CLI) speed-ups are hints, not results: in the first game 2-3.8× CLI gains were invisible in Studio.

## 4. After
- Same recipe, same machine, 3+ runs. Report the table below. Run the behaviour tests: a faster build that changed gameplay fails.
- If a target is still missed, sweep one stressor (piece count, player count, effect count) and save the capture where it first fails; that is the project's real limit (P238).
- Third failed round on the same symptom: stop and return to the architect (`engineering-craft` EC-12).

| Metric | Before (median / worst / spread) | After | Budget | Where measured |
| --- | --- | --- | --- | --- |

## 5. Phones
Without a physical baseline phone, phone performance is **BLOCKED** or **not verified**, never passed. The device emulator changes the screen only (`references/measure.md`). Studio numbers on a PC compare two builds fairly; they do not prove phone speed. Say which one you have.
