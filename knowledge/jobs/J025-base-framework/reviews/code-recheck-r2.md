---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: Session, Screens, Analytics repair rev 2 (J025-R-recheck2), by reviewer

Selective recheck, round 2 (`rules/company.md` §7). Depth: deep for Session (saves, purchases), standard for Screens and Analytics. Code read at the candidate before `evidence/*.md` "Repair round 1". Repo uncommitted (rule 7); revision = sha256.

| File | sha256 (first 16) |
| --- | --- |
| src/Session/init.luau | 089fd470e25ea0fb (Data.luau 9b66b8417044aa74 unchanged; vendor ProfileStore 799263dc0d281f36 unpatched) |
| src/Screens/init.luau | a3da6bedb37e234c |
| src/Analytics/init.luau | e53bdc0846dc313b |

Goal questions: (1) Can a same-server rejoin still load a record this server has not finished writing (S1, S2, F1)? (2) Does a present rejoined player reach `ready` (S9, F2/T-8)? (3) Can a leave during load leave a lock or a `ready` closed entry (S2, N1)? (4) Every open closable once, never two copies (Sc3, Sc5)? (5) No non-finite custom value sent (An3, T-1)?

## Runs (2026-10-24)

| Run | Last lines | Label |
| --- | --- | --- |
| `python tools/gate.py` (once) | `PASS transport` (src/Net regenerated, no Net failure) · `PASS types 0 errors` · `PASS specs 34 files, 287 passed, 0 failed` · `SKIP engine 11 Jest specs, Studio lane only` · `gate: 19.7s` · `RESULT: PASS` | gate-verified |
| `lune run tools/spec/run.luau src/Session tests/acceptance/Session src/Screens src/Analytics` | `specs: 16 files, 125 passed, 0 failed` (R1-F1, R1-F2, R1-N1, QA Rejoin A26-A31, Sc3/Sc5 F1, An-T3 F2) | gate-verified |
| Scratch copy, probe P1 (below) on the candidate | `FAIL ... P1 ...: expected 143, got 142` | Lune probe (FakeWorld, real vendor); scratch deleted |
| Same scratch, data-compare clear sketch (below) | P1 PASS; `specs: 15 files, 97 passed, 0 failed`; probe P2 (steal, then rejoin A) `expected "ready", got "degraded"`, mark left 1 | Lune probe; scratch deleted |
| Candidate, probe P2 | P2 PASS (`ready after 0.1 s`, marks 0) | Lune probe |

## Earlier findings (by the problem)

| Finding | State | Where | Sequence re-traced |
| --- | --- | --- | --- |
| Session F1 lost save | **closed** (for the sequence reviewed) | init.luau:187-195 (timer armed, then wait while `releasing[userId]`), :288-296 (mark set before `EndSession`, cleared on OnAfterSave) | Leave save fails 10 s, rejoin at +12: load waits at :193 until the release lands (vendor :924), then loads 43. R1-F1 and Rejoin F1 (500 and 304 classes) green. Hang: vendor per-key queue (:353-378) holds the rejoin's call anyway; CC-6 row degraded at 120 s green. |
| Session F2 / T-8 | **closed** | init.luau:203-207 | Stolen job result → nil while `loading` → 1 s → a fresh call takes the session → `ready`. Exits: timer/leave through `Cancel` and the :204 guard, `IsClosing`, `ok == false`. A3/S-T2 (degraded at 120 s) green. "Another session tried to load" nil (vendor :1593-1596) now retries instead of degrading at once: needs the same user loading on two servers with the player present in both; not a sequence. |
| Session N1 | **closed** | init.luau:232-236 | Yielding migration + leave: `onLeave` closes (no `ready` → no mark), load resumes, `EndSession` with raw `profile.Data` (Data.load works on a copy), onEnd already disconnected → no kick; timer during migration: `degrade` ended it, the second `EndSession` is a no-op (IsActive false). R1-N1 green. |
| Screens F1 | **closed** | init.luau:139-142 (remove only with an index), :225 (`byId` before build), :235-239 (closed after build: clean late adds, destroy root, return) | A: close inside build → no list removal, Hud untouched, root destroyed, nothing inserted. B: second open while build yields → closes the first (Sc5, newer wins) → first build resumes into the closed branch → one copy. Invariant: every not-closed entry is `byId[its id]` (an older open is closed before a newer one registers), so closeEntry's `byId[id] = nil` never drops a newer entry. |
| Analytics F2 | **closed** | init.luau:248 | NaN, ±inf return before `admit` (no budget used); -2.5 sent. An-T3 green. |

## Ruling on the maker's open window (early mark clear)

**Proven, not blocking** (recommendation R2-1 below). Probe P1 on the candidate reproduces it.

Why not blocking: the loss is only updates accepted between an in-flight save's transform and the leave (one DataStore round trip), and it needs three things at once: a save in flight at leave, the release's first attempt failing right after that save succeeded, and a same-server rejoin inside the release's back-off. The contract already accepts a larger loss in a wider case (CC-6: a release failing past the steal time loses everything since the last landed save, up to the 300 s autosave).

Smallest fix without patching ProfileStore: none that is complete and small.
- `profile:IsActive()` false at OnAfterSave does not tell the two saves apart: `EndSession` removes the profile from `ActiveSessionCheck` (vendor :1090-1093 → :724 → :693) before either answer, so both fire with IsActive false.
- Clearing only when `lastSaved` deep-equals the data at leave (`final = profile.Data` in `onLeave`; no write lands after leave, so the release writes exactly it) closes P1 (sketch: 6-line `same` + 2 lines; 96 existing specs + P1 green). But a release that lands after another server stole the session answers with that server's data, so the mark never clears: probe P2 (CC-6 60 s steal, player leaves B, rejoins A) → `degraded` at 120 s, connection leaked. It needs a second exit no public vendor field gives (ownership of the answered record).
- Clean fix: a one-line vendor patch with a `PATCHES.md` row (for example, pass `is_ending_session` to `OnAfterSave:Fire`), and clear the mark only on that save. That is the lead's call (brief keeps the vendor unpatched).

Spec that catches it (P1, Lune, FakeWorld latency 1 s): saved gold 42 → ready → receipt `p-1` (+100: 142; its Save's transform runs, answer due +1 s) → at +0.3 s `update(+1)` = 143 → leave; every UpdateAsync for the key fails for 12 s from leave → rejoin the same server at +13 s → expect status `ready` and gold 143 (candidate: 142). Pair it with P2 (steal past the release, player leaves B, rejoins A → `ready`, marks 0) so a data-compare fix cannot strand the mark.

## New problems in the changed lines

None blocking. One text note:
- **N-T1 (contract text, step 9):** `contracts/Screens.md:56` says close runs `janitor:Destroy()`; code runs `Cleanup()` (init.luau:150, reasoned in evidence/Screens.md:67). Sc3 still holds (each object cleaned once: the closed-branch Cleanup at :236 cleans only adds after the first). Effect of the change: an `Add` after close no longer throws, it waits silently (only open's closed branch cleans it; a caller that adds after close without `alive()` leaks quietly instead of loudly). Contract line should say Cleanup and that adds after close are the caller's (Sc4 `alive()`).

The maker's second named residual (same-server rejoin during a yielding migration → `degraded`) stands: the rejoin's `StartSessionAsync` throws "already loaded in this session" (vendor :1390-1392) → `ok` false → degraded. No data loss, and migrations are pure by contract (S4). Not a finding; worth a contract failure-table line.

```text
<spec>
artifact: roblox-game-framework/src/Session/init.luau@089fd470, src/Screens/init.luau@a3da6bed, src/Analytics/init.luau@e53bdc08 (Data.luau@9b66b841, vendor ProfileStore@799263dc unpatched)
reviewer: reviewer
looked_at_first: [src/Session/init.luau (all), vendor/ProfileStore/init.luau 344-378, 510-650, 709-935, 1080-1190, 1236-1246, 1380-1630, src/Screens/init.luau (all), src/Analytics/init.luau 247-256, Session.spec R1-F1/F2/N1, tests/acceptance/Session/Rejoin.spec.luau, then evidence/Session.md:74-84, evidence/Screens.md:66-69, evidence/Analytics.md:55-57]
findings:
  - {id: R2-1, class: recommendation, where: "src/Session/init.luau:291-294 (mark cleared on any OnAfterSave); vendor :353-378 (FIFO queue), :924 (OnAfterSave per landed save)", expected: "S1/F1: an update accepted before leave survives a same-server rejoin during the release back-off", observed: "a receipt or autosave in flight at leave lands first and clears the mark; the release's next attempt fails; a same-server rejoin loads the record without the last update; the release then writes nothing (probe P1: expected 143, got 142)", evidence: "harm 1, bounded to one DataStore round trip before leave, three coincidences; below the loss CC-6 accepts; D + scratch Lune probe on the candidate", smallest_fix: "no complete small fix without the vendor: data-compare clear closes P1 but strands the mark after a stolen release (P2 degraded); clean: one-line vendor patch + PATCHES.md row so only the release clears the mark (lead's call); else record the window in the contract failure table", protect: "R1-F1, Rejoin A26-A31 (CC-6 degraded at 120 s), S-T14 leak counts, P2", retest: "specs P1 and P2 as written in this file"}
  - {id: N-T1, class: recommendation, where: "contracts/Screens.md:56 vs src/Screens/init.luau:150", expected: "contract and code say the same", observed: "contract says janitor:Destroy(), code Cleanup(); a late Add after close no longer errors", evidence: "code read; no player harm", smallest_fix: "contract text at step 9", retest: "none"}
keep: [F1 mark armed before EndSession and counted in _debugCounts; load timer armed before the release wait; F2 retry bounded by Cancel, IsClosing and pcall failure, late profile still ended; N1 status re-check after Data.load; Screens closed flag as the single guard, byId before build, index-guarded remove; Analytics non-finite check before admit]
weakest_part: "every Session claim is FakeWorld (transform at call time, then latency); real UpdateAsync ordering and same-server rejoin timing are modelled, not measured"
could_not_check: [{step: "F1/F2/R2-1 on the engine", missing_input: "probe place with DataStore faults and a same-server rejoin", closes_it: "S-T17 engine lane", who: "studio-operator"}, {step: "planted faults for the R1 specs", missing_input: "qa-lead pass on 089fd470 (maker reports 3 red-before runs, Screens 3 plants red)", closes_it: "qa-lead planted-fault result", who: "qa-lead"}, {step: "Screens engine spec (yielding build, PlayerGui)", missing_input: "Studio lane", closes_it: "T-4 engine batch", who: "studio-operator"}]
verdict: ready for the next review
</spec>
```

## Verdict per block

| Block | Verdict | Why |
| --- | --- | --- |
| Session | ready | F1, F2, N1 closed; R2-1 is a proven, bounded residual for the lead (vendor patch or contract row), not blocking |
| Screens | ready | F1 closed; N-T1 is contract text |
| Analytics | ready | F2 closed |
| Helpers, Types, Loader, Config, Motion, ContentTests, State, Anim | ready (carried from code-g1-r1) | not re-reviewed |

Harm areas on the changed lines: 1 saves (R2-1; F1, N1 traced); 2 client gain n/a (no client input in the changes); 3 money (receipt confirm unchanged; P1's receipt returns NotProcessedYet and is redelivered as a duplicate → GRANTED, no double grant); 4 races and leaks (mark lifetime, retry loop, closed-branch cleanup traced); 5 performance (per-frame wait only while a mark is set, ≤ 120 s, per rejoining player: n/a at scale); 6 structure (N-T1); 7 APIs (no new engine call); 8 over-building (none: each fix within its finding).
