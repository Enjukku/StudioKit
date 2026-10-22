> Author: J018 maker reviewer · claude-opus-5-5 · high · 2026-10-22; built also from the owner's Riot transcripts (J018). Part of `code-review`. The finding format is `rules/messages.md` §6; the review file is `templates/jobs/review.md`; this page says how I fill them.

# Review method: inputs, reading orders, findings, rounds

## 1. What each input can prove
A review is only as good as its inputs. Every check in my review names the input it used and gets a label: gate-verified, MCP-verified, owner-confirmed or not verified. I never pass a check its input cannot show.

| Input | Can prove | Cannot prove | Label when it is all I have |
| --- | --- | --- | --- |
| Brief, plan, invariant cards, acceptance cases, spec rows (B) | what the change must do and must not touch | that the code does it | (intent, not a check) |
| The diff alone | what changed | missing behaviour, callers, what the change breaks elsewhere | not verified |
| The full files and callers at the candidate revision, read (D) | data flow, branches, who writes a fact, what is missing on a path | timing on screen, engine behaviour the docs do not state, replication order, cost | not verified for runtime claims |
| A screening pattern (G, `references/presentation.md` §5) | where to look | anything (a miss is not a pass) | (pointer only) |
| Docs mirror line or `_api-reference` entry | the API exists and what Roblox documents | undocumented behaviour (sleep, ordering, timing): needs a probe | gate-verified for existence only |
| The gate or test logs on the candidate revision (T) | analyzer clean; the tested pure logic and migrations behave as asserted | engine behaviour, replication, anything the tests do not drive; a log from another revision proves nothing | gate-verified |
| A builder's Studio run, single client (S) | what one run showed in Studio | two players, latency, phones, leaks over time | MCP-verified (that run only) |
| A two-client or 8-client Studio scenario (S) | races between players, bystander views, join and leave order | real devices, published-only behaviour | MCP-verified |
| A physical phone run (S) | phone cost and feel on that device | other devices | MCP-verified or owner-confirmed, as recorded |
| A published-game run (teleports, real stores) | published-only behaviour | (none of the above limits) | as recorded |
| The owner at the gate | feel at normal speed, taste | correctness | owner-confirmed |
I have no Studio tools. S comes from the builder's hand-back or a ticket to the qa-lead or performance-engineer. A claim about timing, physics, performance or feel without S is "not verified", and the item it supports is not done (`engineering-craft` EC-10).

## 2. Reading orders
The eye gets used to code it has read in one order. I read every change in two orders, and the second one finds what the first one missed.

1. **Intent first.** Brief, invariants, acceptance cases (normal, boundary, failure), non-goals, the contract's event names and the spec rows for anything players see or hear. I write 2-4 **goal questions**, each naming an invariant: "Can a sale the server denies ever show '+N'?", "Can two requests in one frame grant twice?". Not "is this right?".
2. **Look before the claims.** The diff and the changed files at the candidate revision, before the builder's manifest and hand-back (`rules/company.md` §7). Then the manifest; its claims are claims (`rules/messages.md` §7).
3. **Pass 1, file order, shallow.** Every changed file, against all 8 harm areas, writing candidates only: no proving yet. A change of 12 files gets 12 shallow reads before the first deep one.
4. **Pass 2, trace order** (standard and deep depth; a quick review stops after pass 1 and the tests). For each player-facing path: input → attempt cue → request (transport) → handler in the `networking-security` N-02 order → owner module or data layer (`data-saving` D-05) → result (done, denied, unavailable) → client outcome layer → cleanup. Then the failure sweep on the same path: denied, unavailable, player leaves mid-action, character respawns, model streamed out, request repeated, retry after a lost answer, a second player on the same object. Missing behaviour lives here: a path with no branch for one of these is a candidate.
5. **Fresh eyes before writing.** Re-read each kept candidate from the code with the hand-back closed, and once more from the caller's side. A long review (deep depth, many files) ends with one more pass over the harm order from the top, on the same frozen revision.

## 3. Proving and writing a finding
- **Prove or drop.** For each candidate: file:line, the input or sequence, the wrong outcome for players. Then try to make it safe: is there a guard elsewhere (the transport's rate limit, the data layer's check), an engine guarantee (a docs line), a type that rules it out? A candidate that survives is a finding; one that does not is dropped. A candidate only a run can settle becomes a ticket (`references/presentation.md` §4, `rules/messages.md` §2) and a could-not-check line, never a finding.
- **One problem per finding.** If two problems share a line, they are two findings. Name the harm area (the layer) and the invariant or rule it breaks (the goal).
- **The `rules/messages.md` §6 fields, filled this way:** `where` = file:line at the candidate revision; `expected` = the rule or invariant with its source (brief line, skill row); `observed` = the sequence → wrong outcome for players; `evidence` = severity (Critical, High, Medium; `SKILL.md` §4 V-12), the proof and its label; `smallest_fix` = the fix direction, then "protect:" what the fix must not break (from the keep list), then "retest:" the sequence or test name that shows it fixed.
- **Show, do not rewrite.** When words are ambiguous, the fix direction may carry a sketch of at most 3 lines. Never a rewrite and never an edit of the change.
- **Plain and direct.** No "might", "consider", softened praise or style. A finding is a problem with proof; a question is marked as a question.
- **One recommended fix.** When several fixes would work, name the smallest one and why; never a menu.
- **Do not reopen closed doors.** A fix direction never brings back an approach recorded in `knowledge/design/tried-and-failed.md` or rejected in the job's decision log without saying so and why.
- **Conflicts go up.** When my finding contradicts another reviewer's (qa-lead, performance-engineer, a craft lead), I state both and send the conflict to the lead (or the architect for an approach), never an averaged note.

## 4. Re-review rounds
1. Review only the new diff and what it touches; the frozen keep list stays protected.
2. Map every earlier finding: fixed, not fixed, or disputed (the builder's evidence, re-read at its revision). A builder's proof that a finding was wrong withdraws it, in writing; I do not defend it.
3. Re-check the **problem**, not the suggested change: re-trace each finding's sequence in the new code (or read the retest's log). A fix that made the suggested change but still lets the sequence happen is "not fixed".
4. Walk the harm order once on the new diff around each fix: fixes often add a yield, a second writer, a new connection or a success layer in the wrong branch.
5. A new idea that is not a defect (a better structure, a nicer name) after the gate is a follow-up, not a finding.
6. Round 3 on one approach: stop and escalate to the lead and the architect with the three rounds' findings (`rules/anti-overengineering.md` 20).

## 5. Closing the review
- **Keep list:** what works and must keep working (a correct validation order, a well-owned cleanup, a test that fails on the planted fault). It joins the candidate's protected list.
- **Could-not-check list:** one line per check I could not run: the step, the missing input, the capture or test that would close it, and who can supply it. Empty only with the reason ("pure logic, every row gate-verified").
- **Honest recap:** the weakest part of this review in one line (an area I could only skim, an input I lacked, a file I read only in the diff).
- **Done when:** every harm area was walked (or skipped with the reason), every candidate proved or dropped, the could-not-check list written. A round that finds nothing new ends the loop. A clean change gets "no blocking findings" and its keep list, never an invented finding.

## 6. Symptom review ("why did this break")
1. Start from the observed symptom and where it was seen (report, Output log, capture, analytics), at the revision that showed it.
2. Write the sequence that reproduces it, in player words, then in code (input → path → wrong state).
3. Find the cause by layer (harm area): the first line where the state goes wrong, not the line where it shows.
4. Name the test that should have caught it and why it did not (no such case, a toy case, a test copied from the code).
5. The finding carries the root cause, the failing case to add first (`testing` T-02) and the smallest fix direction. A third patch for the same symptom goes to the architect (`engineering-craft` EC-12).

## 7. Plan check (before code, for deep changes)
When the brief sends me the architect's plan before the build (money, saves, remotes, paid random, trades), I review the plan, which costs one exchange instead of a rework round:
- every invariant card has an owner, a clock, a failure response and a test (`architecture` R-01, R-04);
- the requests are intents, the server computes outcomes, grants have ids (`networking-security` N-02, N-03; `data-saving` D-11);
- each player-facing moment names its attempt cue, its confirmed event, its pending and denied states and its reduced variant (`references/presentation.md` PT-01, PT-09);
- paid random: one odds table, effective odds, the restricted path (`platform-policy` P-01 to P-03).
Findings use the same format, with `where` = the plan's section; the build then starts from the corrected plan.
