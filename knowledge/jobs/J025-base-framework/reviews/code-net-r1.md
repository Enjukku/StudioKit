---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: Net code rev 1 (J025-R-Net), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\src\Net\` + `src/Types/init.luau`, `src/Helpers/RateLimit.luau`, the gate's transport step (`tools/gate.py:83-130`). Repo uncommitted (rule 7): revision = the sha256 below. Depth: **deep** (the only client-to-server surface). Round 1. Code read before `evidence/Net.md`; contract `contracts/Net.md` (frozen) + CC-7..CC-9.

Goal questions: (1) Can a modified client reach a handler with bad data, or change anything through a denied call (N1, N2, Q7)? (2) Can one client flood the log, the heap, a queue or server time (N5, N8, the performance budget)? (3) Does any per-player state outlive the player (N6, Q5, G10, T-10)? (4) Is the post-generation patch deterministic, anchor-checked and loud on a Blink change (Net-T16)?

## Files reviewed (sha256)

| File | sha256 |
| --- | --- |
| src/Net/init.luau | 778b4a742e9b054ab64e2d86c83eb7d4ba62976a360f4a21745dfde383c48a46 |
| src/Net/tools/patch-generated.luau | 7f6834107c767d44716bdbf025120584a161f7de61aa3eca3fd37cea12fb808a |
| src/Net/tools/schema-lint.luau | 19e0727df41da3052f96920c901cc1fbb36364fdb451b7f35db4fa1d72d4b21a |
| src/Net/framework.blink | 12f22c8ce6c696de5420b761147ead5020c4e69d8a4a2a49919e0668b3ad1798 |
| src/Net/Generated/Server.luau | db9a6a815ee918c78eb4d051e973b481d9039e6d8a1525eda2818f5bc332604b |
| src/Net/Generated/Client.luau | e6b3d03128a833f6d4b51f110bc0bb183f4a1d0411649e83f86e0b7d150ae553 |
| src/Types/init.luau | 1819b417812ba82fc4d0e5da2a4a38713764adc62389ccd159b4101d1d7b5c61 |
| src/Helpers/RateLimit.luau | dd819c6e7aa011d08da3926021964ef3093a4d44258e86e918f580ffb56379f0 |

Hashes equal the brief and the B7b evidence; unchanged after the gate run.

## Runs (2026-10-24)

- `python tools/gate.py` (live repo): **RESULT: FAIL** on `types` only: 11 errors, all in `tests/acceptance/Net/Harness.luau` and `NonFinite.spec.luau` (QA's Q2 protected tests, in progress; `@lune/` requires and table.insert overloads). Not counted against Net. transport PASS (regenerated + patched + linted, output current), format, lint, rules PASS, specs **349/349**, build PASS, copy-tool 9/9. `src/Admin` produced no failure in this run.
- Scratch probes (copy of the repo in the session scratchpad, `src/Net/Probe.spec.luau` on the spec's own harness: Blink 0.18.9 output of `test/sample.blink`, patched, on the fake engine, wired to a real Net). Lune lane, 2-3 runs each:

| Probe | Result |
| --- | --- |
| A: one reliable packet of n one-byte `StateHydrate` events, Net `rate 2 burst 4` | n=1,000: 2.0-2.7 ms; n=20,000: 35-37 ms; n=65,535: **104-112 ms per packet**, 4 handled, 65,531 `rate`, `blocked` 0, `bad_packet` 0; a second identical packet costs the same and is not blocked |
| D: same 65,535-event packet, raw listener without Net | 80-82 ms (Blink decode + `task.spawn` per event); Net's check adds ~25-30 ms |
| B: one packet of 65,535 unknown event indexes (byte 250) | **6.5-7.5 ms per packet**, no reject, no strike (the dispatcher skips unknown indexes) |
| C: `StateSync.Fire(p)` after `PlayerRemoving` for 100 players (T-10) | current patch: FireClient to departed players **100**, staying player 1; with the step proposed in F2: **0**, staying player 1 |

## Findings (most harmful first)

```text
<spec>
artifact: roblox-game-framework src/Net @ init 778b4a74, patch 7f683410, Generated/Server db9a6a81 (rev 1)
reviewer: reviewer
looked_at_first: [src/Net/init.luau, Generated/Server.luau, tools/patch-generated.luau, tools/schema-lint.luau, framework.blink, Types, RateLimit, gate.py transport step, contracts/Net.md]
findings:
  - id: F1
    class: blocking
    where: "Generated/Server.luau:347-375 (reliable loop: one task.spawn per decoded event, :354/:367), :388-392 (unreliable loop skips unknown indexes); init.luau:200-233 (strikes come only from decode rejects); tools/patch-generated.luau (no bound per packet)"
    observed: "Harm area 2/5 (server cost). A modified client fires BLINK_RELIABLE_REMOTE with a 65,535-byte buffer, every byte = the StateHydrate index (an event every game registers). Blink decodes 65,535 events and task.spawns Net's listener for each; Net denies 65,531 as `rate`. Nothing raises, so guard.reject is never called and the sender is never blocked. Lune: 104-112 ms of server time per packet (Blink 80 ms + Net 25-30 ms), repeatable every packet. Same shape with any registered client event or function (a function also writes one denied Reply per call into the sender's send buffer), and with unknown index bytes: 6.5-7.5 ms per packet, no reject. The engine's ~500 requests/s cap counts packets, not events, so the per-event Net rate does not bound the work."
    expected: "Brief intent: a modified client must not slow the server. Net.md budget: a flood keeps heartbeat avg <= 18 ms, max <= 25 ms; one such packet exceeds the 25 ms max on the Lune screen. N-10 still holds (block, no kick)."
    evidence: "High. Code read (D) + Lune probes A, B, D (T, screen lane, not engine). Engine per-event cost and the client upload cap per second: not verified."
    smallest_fix: "Bound events per client before the spawn: the patched dispatcher asks the guard once per loop iteration (not once per packet) and raises `error(\"flood\", 0)` when refused, so the guarded decode turns it into one counted reject + strike; Net's allow spends one credit from a per-player event allowance (RateLimit.allowance, PROPOSAL 600/s burst 600, far above a real client's per-frame batch) and keeps the 10 s block. One mechanism covers per-packet, sustained and unknown-index floods. Contract text change (Guarded decode step 2, budget row) = a CC entry by the lead."
    protect: "Normal batches (<= the allowance) decode and arrive exactly as today; allow-before-decode order; fixed reject kinds; N-10 no kick; G6 accepted loss of the rest of the sender's own packet; accepted-call overhead <= 20 us."
    retest: "Transport rows: one 65,535-event packet -> listener calls <= burst, 1 reject, Lune cost <= 2 ms; 500 packets x 255 events in 1 s -> sender blocked, listener calls <= allowance; 65,535 unknown indexes -> rejected; planted fault (guard asked once per packet again) turns them red. Engine: Net-T18 variant with a valid-event flood (heartbeat avg/max in budget)."
  - id: F2
    class: blocking
    where: "Generated/Server.luau:301-316 (StepReplication), :401-405/:418-429 (Fire, FireList create PlayersMap[Player] for any Player), :297-299 (the only cleanup, PlayerRemoving)"
    observed: "Harm area 4 (leak per player), T-10. Sequence: a handler yields (Session.update, a DataStore call, task.wait) -> its player leaves -> PlayerRemoving clears PlayersMap -> the handler resumes and calls Remotes.X.Fire(player) (or FireList with that player, or any PlayerRemoving handler that fires after Blink's own handler ran). Fire Loads nil, Saves a new entry: the Player and its BufferSave stay in PlayersMap for the server's life, StepReplication calls FireClient on the departed Player once and iterates the entry every Heartbeat after. Probe C: 100 departed sends -> 100 FireClient calls to departed players. An exploiter repeats it with leave + rejoin (a new Player object each time). Patch step 5 covers function replies only (builder's own note F-B7b-1)."
    expected: "Q5: 1,000 join/leave cycles leave 0 entries in every per-player table; N6; CC-8 intent (no send entry for a player who left)."
    evidence: "Medium-High (slow, unbounded growth over server life). Code read (D) + builder's Net-T21 control + probe C (T). Whether FireClient on a departed Player raises in the engine (which would abort StepReplication for every later player each frame): not verified."
    smallest_fix: "RULING on T-10: a patch step, not a rule for games (a rule cannot be grepped: any Fire after any yield, plus PlayerRemoving handler order). Patch step 6 on the one StepReplication anchor `if Send.Cursor <= 0 then continue end`: append `if Player.Parent ~= Players then PlayersMap[Player] = nil continue end`. A departed entry always has Cursor > 0, so it is dropped on the first Heartbeat; idle entries cost nothing; Fire, FireList, function replies and handler order are all covered. Step 5 may stay (it also skips writing the reply); removing it is the lead's call."
    protect: "Staying players' sends and their order unchanged; anchor found exactly once or exit 1; marker/idempotence check extended to step 6."
    retest: "Spec Net-T22 (Transport): 100 players leave, then StateSync.Fire and FireList to each; after two Heartbeats 0 FireClient calls to departed players, the staying player's message delivered (probe C: unpatched-step control 100, fixed 0); Net-T16 rows for the new anchor (missing -> exit 1, second run no-op); planted fault: step 6 off -> red. Engine ticket: FireClient on a departed Player in Studio (raises or silent)."
  - id: R1
    class: recommendation
    where: "tools/schema-lint.luau:302-311 (array suffix parsed, bound never required), :459-462"
    observed: "Harm area 2. The lint accepts an unbounded client array `T[]` (Blink caps it at 65,535 elements, a u16). Net's walk denies every call over 512 values (init.luau:30, :72-75), so any element count above 511 can never pass: such a field only buys decode work and a `bad_input` denial, which is not a strike. Cost not measured (comparable byte-loop to probe B)."
    expected: "Net.md Schema rules: bounded arrays T[..n]."
    evidence: "Code read (D); cost not measured."
    smallest_fix: "Lint: every array in client data needs `[..n]` (n <= 511) and names event and field, like the map rule."
    protect: "Server-to-client arrays stay unbounded."
    retest: "Lint.spec row: `u8[]` in a From: Client event fails naming event and field; `u8[..64]` passes; framework schema passes."
keep:
  - "N1 order exactly as the contract: in Players -> Session status (+ beforeReady) -> rate -> walk -> xpcall handler; rate before the walk so a flood is cheap per event"
  - "Guard: allow before decode, pcall'd decode, fixed reject kinds (no attacker text as a Stats key), one decode line per 10 s server-wide, no strike state for a player not in Players"
  - "Walk: math.isfinite on numbers and keys, Vector3/Vector2, the CFrame 12-component sum (f32 components keep the sum finite), depth 8, 512 values, UTF-8 on strings and string keys"
  - "answer: closed registration -> closing, xpcall, isReply shape check (outcome + reason <= 32 bytes) -> exactly one Reply"
  - "Patch: exact anchors found once or exit 1, queue-branch and function-reply counts must match, final 'no unguarded dispatcher' check, marker idempotence with a partial-patch check; gate restores generated files after the compare"
  - "Unpatched controls in the transport specs (each guarded row proves the same packet hurts without the patch)"
weakest_part: "F1's size comes from the Lune lane (no native codegen, Lune scheduler); the engine per-event cost and how many 64 KB packets per second a client can upload are unmeasured, so the real heartbeat hit may be smaller or larger."
could_not_check:
  - {step: "F1 engine size", missing_input: "Studio heartbeat during a valid-event flood (one 64 KB StateHydrate packet per frame) and the client's reliable upload cap", closes_it: "Net-T18 variant in the 1-client multi-client lane", who: "qa-lead / studio-operator"}
  - {step: "F2 engine consequence", missing_input: "FireClient on a departed Player: raises or silent", closes_it: "a 1-client Studio probe: Fire after leave, read Output", who: "studio-operator"}
  - {step: "Net-T12, T13 engine, T15, T18", missing_input: "engine runs (written, not run)", closes_it: "engine batch T-4", who: "studio-operator"}
  - {step: "tests can fail (protected set)", missing_input: "QA Q2 planted-fault result for Net (in progress; its files do not type-check yet)", closes_it: "Q2 hand-back", who: "qa-lead"}
verdict: fix-first (F1, F2) on init 778b4a74, patch 7f683410, Generated/Server db9a6a81
</spec>
```

## Harm areas walked

| Area | Result |
| --- | --- |
| 1 Saved data | Net writes nothing; grants are handlers' via Session (N7). n/a beyond that |
| 2 Exploitable requests | No path found to a handler with bad data: decode bounds (Blink) -> guard -> in Players -> status -> rate -> walk. `check` cannot raise on client input (Session.status `init.luau:305-311` is total; walk is bounded), so Blink's unsampled function-error warn is unreachable. `unknown` args (AdminAction) walked; Color3/UDim2 inside `unknown` are not walked (outside N1's list; handlers type-check). Floods: F1, R1 |
| 3 Money, policy | n/a (no purchases or paid random in Net) |
| 4 Leaks, yields, races | Net tables reset on leave, no new state after leave (`init.luau:123`, `:213`); Blink queues capped and hold <= 256 Player refs until registration; PlayersMap: F2. Handler yield then leave: Net does nothing after the handler; step 5 drops the reply |
| 5 Performance | Accepted/denied per-call costs within budget (builder Q6, Lune); per-client aggregate: F1 |
| 6 Structure | One transport, functions passed in (README rule 2); no second way |
| 7 APIs | `math.isfinite` (`_api-reference/libraries/math.yaml:367`), `utf8.len`, `debug.traceback`, `buffer.*`, `FireClient` (`RemoteEvent.yaml:90`) exist; none deprecated |
| 8 Over-building | None found (Net's `count` duplicates RateLimit's 5-line helper: not worth a finding) |

Patch safety (goal 4): deterministic text edits, each anchor once or exit 1; second run is a no-op with a partial-patch check; Blink pinned in `rokit.toml` (`1Axen/blink@0.18.9`). Schema lint (holes): half-open float ranges are safe (Blink fills the type limit, P1 T2; the walk is the second layer); `unknown` allowed by contract; only R1 found.
