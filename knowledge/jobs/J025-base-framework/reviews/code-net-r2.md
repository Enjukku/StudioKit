---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: Net code rev 2 (J025-R-Net-r2, selective recheck), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\src\Net\` (repo uncommitted, rule 7: revision = sha256). Depth: **deep**, round 2, selective (V-17: the round-1 sequences re-traced, harm order walked on the changed lines only). Code read before `evidence/Net.md` "Repair round 1".

Goal questions: (1) F1: does one packet of valid or unknown events now stop at a bound, and does a sustained flood block the sender (N1 step 0, budget row)? (2) F2: can any send entry of a departed player survive one Heartbeat (Q5, N6, T-10)? (3) R1 / CC-15: does the lint refuse every client array Net's walk can never accept? (4) CC-17: negative target ids decode, NaN/inf/out-of-range do not, and a fractional id cannot act?

## Files (sha256, equal to the brief; unchanged after the gate run)

| File | sha256 |
| --- | --- |
| src/Net/init.luau | 18bbd1c50db70cc7075923caf65aac59a86d58c2aff6056cb3c83ebb83787831 |
| src/Net/tools/patch-generated.luau | 248faf4277ff82e0c0cc5abfe31ed3a6c00447daa7272da0fbbca383c547641f |
| src/Net/tools/schema-lint.luau | 2941dcdf88d10c9784df0da3e38742f947930dad3a0a4a0203678654bf4b6ba0 |
| src/Net/framework.blink | ddf5d9a94f60df446016a1519f0a6bfc1257a1cb140ca6dd9603400b9eac7e75 |
| src/Net/Generated/Server.luau | e5066c66e4ca8b1e45b08379e791a673a6e40b976443caade9ef3cf8de7327f4 |
| src/Net/Generated/Client.luau (unchanged) | e6b3d03128a833f6d4b51f110bc0bb183f4a1d0411649e83f86e0b7d150ae553 |
| src/Helpers/RateLimit.luau (unchanged) | dd819c6e7aa011d08da3926021964ef3093a4d44258e86e918f580ffb56379f0 |

## Runs (2026-10-24)

- `python tools/gate.py` (live repo): **RESULT: FAIL** on `specs` only, 481 passed, 1 failed: `tests/acceptance/Net/Planted.spec.luau:43` **P27** "patch step 5 removed ... Leave L1 turned red: the planted fault survived". Cause: step 6 (CC-14) now drops a departed player's entry at the next Heartbeat, so removing step 5 no longer turns Leave L1 red; the plant is obsolete, not a Net defect (QA's update with CC-14, like X1/P09 for CC-17; X1/P09 did not fail in this run, QA files changed 08:52-08:53). transport PASS (regenerated + patched + linted, current), format, lint, rules, types (0 errors), build, copy-tool PASS.
- Lint probe (scratch schema, deleted after): `event Paint { From: Client, ..., Data: u8(0..255)[..64][..64] }` → `schema-lint ... arrays bounded` exit 0.

## Per item

| Item | Result | Where | Re-traced sequence |
| --- | --- | --- | --- |
| F1 | **closed** | `Generated/Server.luau:348-352`, `:393-397` (patch `patch-generated.luau:45-47`, `:111`); `init.luau:207-216`, `:218-246`, `:37-40`, `:62` | One reliable packet of 65,535 `StateHydrate` bytes: each loop iteration asks `allow` before `Read(1)`; credit 601 is refused → `error("flood", 0)` → pcall → `reject` → `flood` +1, one strike. Listener spawns ≤ 600. Unknown index bytes spend a credit each too (check precedes the index read), reliable and unreliable. Sustained: once the allowance is empty every packet's first iteration raises → 20 strikes in 1 s → `allow` false for 10 s → each packet ~3 µs (blocked, no strike). Gate: Net-T23 x3 PASS; builder's planted fault (check once per packet) turns them red; Q6 1.2-1.7 ms per 65,535-event packet (Lune, was 104-112). Function replies per denied call are bounded by the same allowance. N-10 kept (no kick) |
| F2 | **closed** | `Generated/Server.luau:306-309` (patch `:48-50`, `:128`, marker check `:157`) | Handler yields → player leaves → Blink's PlayerRemoving clears → `Fire`/`FireList`/reply recreates `PlayersMap[Player]` with Cursor > 0 → next StepReplication: `Player.Parent ~= Players` → entry set nil (assigning nil to the current key during traversal is allowed) → no `FireClient` to the departed Player. `Players` is the module's local (`:17`). Idle staying entries skip at `:303`. Net-T22 PASS (unpatched control 100, patched 0); anchor once-or-exit-1 and marker idempotence cover step 6 |
| R1 | **closed** for its sequence | `schema-lint.luau:471-479`, `:307-321` | `u8[]`, `[n..]`, `[..512]`, `[600]` in client data each fail naming the field (Lint Net-T19 PASS). Gap in the same rule: R2-2 below |
| CC-17 | **closed** | `framework.blink:31-38`; `Generated/Server.luau:192-193` | -2 and -(2^53-1) decode; NaN (`not (NaN >= x)` raises), ±inf, ±(2^53+2) raise inside the guarded decode → `bad_packet`; -2.5 decodes and Admin refuses it (`src/Admin/init.luau:143`, `:168`: finite and `math.floor(v) == v`, then presence) |

## Ruling on the maker's open weakness (sender already out of Players)

`init.luau:208-209` returns `true` with no credit for a sender whose `Parent ~= Players`, so that packet is not bounded by the event allowance; every event in it is then decoded, spawned and denied `closing` (`init.luau:129-130`).
- Can the engine deliver it? The docs do not say for remotes. They do say: `PlayerRemoving` fires right before the removal (`_api-reference/classes/Players.yaml:1613-1619`); with `Deferred` signals (the recommended behaviour, `scripting/events/deferred.md:11`) handlers for events still pending run after an ancestry change (`deferred.md:86`, `:104-106`). So an `OnServerEvent` queued before the disconnect may resume with `Parent == nil`. Not verified for remotes: a Studio probe closes it.
- Size: bounded by the packets the client sent before it left (the ~500 req/s cap, `remote.md:370-411`), one time per leave; each costs up to the round-1 probe A/D figure (~80-100 ms Lune per 65,535-event packet). The attacker pays a full rejoin per repeat.
- **Not blocking** (one-shot per session, reach not verified). Recommendation R2-1 below, because the 1-line fix loses nothing.

```text
<spec>
artifact: roblox-game-framework src/Net @ init 18bbd1c5, patch 248faf42, lint 2941dcdf, blink ddf5d9a9, Generated/Server e5066c66 (rev 2)
reviewer: reviewer
looked_at_first: [src/Net/init.luau, Generated/Server.luau:280-500, tools/patch-generated.luau, tools/schema-lint.luau (array rule), framework.blink, src/Admin/init.luau:143-168, gate run]
findings:
  - id: R2-1
    class: recommendation
    where: "src/Net/init.luau:208-209"
    observed: "Harm area 5. Sequence: a client sends k reliable packets of 65,535 valid events and disconnects; under Deferred signals OnServerEvent for those packets can resume after removal (Parent nil) -> allow returns true for every event -> Blink decodes and task.spawns up to 65,535 events per packet, each denied closing. ~80-100 ms per packet (round-1 probe A/D, Lune), once per leave."
    expected: "CC-13 intent: no packet decodes more than the event allowance; N6: no state for a departed player."
    evidence: "Non-blocking. Code read (D); engine reach per deferred.md:86, :104-106 + Players.yaml:1613-1619, not verified for remotes."
    smallest_fix: "allow returns false for a sender out of Players. reject already creates no state for them (init.luau:227) and every event of such a sender is denied closing or its reply dropped (patch step 5), so nothing is lost; the cost is one `flood` count and at most one sampled line per 10 s."
    protect: "No strikes or allowance entries for a departed player (_debugCounts 0); staying players unaffected."
    retest: "Transport row: sender with Parent nil, one 65,535-event packet -> 0 listener calls, flood +1, _debugCounts {rate 0, rejects 0}. Engine: 1-client Studio probe, fire 5 big packets then Kick from the client side; read whether Net sees Parent nil."
  - id: R2-2
    class: recommendation
    where: "src/Net/tools/schema-lint.luau:471-479 (each array checked alone; no total per message)"
    observed: "Harm area 2/5 and author trap. `Data: u8(0..255)[..64][..64]` (a plausible 64x64 grid) passes the lint (probe, exit 0), but a full grid is 4,161 walked values: Net denies every full call bad_input (init.luau:79-80), and the decode of up to 4,160 elements per event (byte-bounded) is bought before the denial, the R1 sequence again through nesting; same for sums, e.g. (u8[..300], u8[..300])."
    expected: "CC-15 intent (lint header :8-9): no client shape Net's walk can never accept."
    evidence: "Non-blocking (same class as R1; cost not measured). Code read (D) + lint probe (T, scratch)."
    smallest_fix: "Lint computes the most values a message can carry (array: 1 + upper x inner; struct/tuple: sum, +1 per table) and fails over 512, naming the message."
    protect: "Server-to-client shapes untouched; flat [..511] still passes; framework schema passes."
    retest: "Lint rows: u8[..64][..64] fails, u8[..16][..16] passes, (u8[..300], u8[..300]) fails."
keep:
  - "Round-1 keep list (N1 order, guard shape, walk, answer, patch anchors and idempotence, unpatched controls) still holds on the changed lines"
  - "Per-event allow before the index read in both loops, count-checked against GuardedConnect and in the marker check: unknown indexes and function calls spend the same credit"
  - "Blocked sender returns before strike accounting (no block extension, ~3 us per packet)"
  - "Step 6 placed after the Cursor check: idle entries cost nothing; one anchor, exit 1 if moved"
  - "CC-17 range keeps NaN/inf/2^53 outside Blink; integer and presence stay Admin's"
weakest_part: "R2-1's reach rests on deferred-signal semantics read across from instance events; no engine run shows a remote resuming after removal."
could_not_check:
  - {step: "R2-1 engine reach", missing_input: "a remote resuming after the sender's removal (Parent nil)", closes_it: "1-client Studio probe in the throwaway place", who: "studio-operator"}
  - {step: "F1 engine size", missing_input: "Studio heartbeat during a valid-event flood", closes_it: "Net-T18 valid-event variant (engine batch)", who: "qa-lead / studio-operator"}
  - {step: "tests can fail (protected set) on this hash", missing_input: "QA Q2b planted-fault result; P27 now obsolete after CC-14", closes_it: "Q2b hand-back with P27 retargeted or retired", who: "qa-lead"}
  - {step: "contract text", missing_input: "contracts/Net.md:32, :36 still describe a per-packet allow (CC-13, CC-14 live only in build-log)", closes_it: "lead folds CC-13..CC-15, CC-17 into Net.md", who: "orchestrator"}
verdict: ready for the next review (no blocking findings) on init 18bbd1c5, patch 248faf42, lint 2941dcdf, blink ddf5d9a9, Generated/Server e5066c66
</spec>
```

## Harm order on the changed lines

| Area | Result |
| --- | --- |
| 1 Saved data | n/a (Net writes nothing) |
| 2 Exploitable requests | F1, CC-17 closed; no new path to a handler; R2-2 (lint gap) |
| 3 Money, policy | n/a |
| 4 Leaks, races | `events` allowance reset on leave (`init.luau:253`), no take for a departed sender; step 6 closes F2; no new per-player table |
| 5 Performance | Blocked packet 0.4 → ~3 µs (builder Q6), 1,000-packet flood 3.1-3.6 ms, inside the 18/25 ms budget (Lune); R2-1 |
| 6 Structure | One mechanism (allowance in the dispatcher) for per-packet, sustained and unknown-index floods; no second way |
| 7 APIs | No new engine calls (`Player.Parent`, `error`, `RateLimit.allowance` existing) |
| 8 Over-building | None |
