---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied research paper 'Operating a Roblox Experience in 2026' (ChatGPT, 2026-10-20); file kept outside git at C:\\Users\\Firew\\Downloads\\Roblox_Engineering_Operations_2026.docx"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Paraphrased digest (paper sections in brackets). The paper labels every claim Fact / Common practice / Opinion; that label is kept here. Spot-checked 2026-10-20 against the docs mirror: `StudioTestService:ExecuteMultiplayerTestAsync`, `DataModel.ServerRestartScheduled`, `ConfigSnapshot.UpdateAvailable/Refresh`, `Stats.MemoryTrackingEnabled`, `Players` ban fields all exist; the mirror's update page still says delayed restart ≤ 60 min (the paper cites the newer 4 h staff update). Budgets are the paper's **proposals**, not Roblox limits.

# Operating a Roblox game in 2026: digest

## 1. Testing toolchain [§1, §5]
| Item | Label | Detail |
| --- | --- | --- |
| Official test framework | Fact | `roblox/jest` + `roblox/jest-globals` 3.20.1 (2026-08-30) on Wally; runs in Studio and Open Cloud Luau Execution. TestEZ archived 2024-09-14; `jsdotlua/jest-lua` is a separate older fork |
| Outside the engine | Fact | Lune 0.11.0 (2026-10-11), limited Roblox API: good for pure logic (migrations, reward math, state transitions), not replication, physics or rendering. run-in-roblox 0.3.0 is a 2020 bridge into installed Studio |
| Server tests in CI | Fact | Open Cloud Luau Execution: headless server per task, ≤ 5 min per task, ≤ 10 concurrent per place, run against an explicit place version. Roblox's CI sample is "not battle-tested" |
| CI contract | Opinion | build the production place and a separate instrumented test place from the same revision; run the test place by version; require a structured result (tests found, run, failed, skipped); zero tests, timeouts or missing results fail; retry infrastructure errors, never failing assertions; publish only the production artifact |
| Multi-client tests | Fact | `StudioTestService` (2025-12, multiplayer 2026-05): `ExecuteMultiplayerTestAsync`, up to 8 simulated clients, Plugin security, needs a Studio machine. **Teleports cannot be tested in Studio** |
| Multi-client suite | Opinion | short two-client cases: simultaneous claims, leave during save, respawn during an ability, late join, stale client action; an 8-client churn case nightly; pass = expected server and client state, not a screenshot |
| Save fixtures | Opinion | separate test universe; fixtures for new account, each old schema, missing / extra / malformed fields, duplicate item ids, huge valid balance, partial migration, **unknown future schema**; mixed writers (old server + new save, new server + old save, lock lost, rejoin before final save); the agent that changes a migration must not also edit its expected outputs |
| Leaks | Opinion | three separate signals: our own counted connections and tasks return to zero after 100 create-destroy cycles; `InstanceCount`, LuaHeap and total memory plateau at idle checkpoints; Scene Analysis for causes. One clean signal does not excuse another |
| Tool pins | Fact / Opinion | Rojo 7.7.1 (2026-10-02), Wally 0.3.2 (2023; 0.4 is alpha), Luau-LSP 1.70.1 (2026-09-27; set `strictDatamodelTypes`), Lune 0.11.0, jest 3.20.1. Record the Studio build per run |
| Test lanes | Opinion | every commit: static checks + Lune fixtures (≈ 1 min). Merge: Luau Execution Jest suite + Studio two-client scenario. Nightly: 8-client churn and memory checkpoints. Release candidate: physical phone + PC, published teleport/save/rejoin route |

## 2. Releases and recovery [§2, §5.3]
| Item | Label | Detail |
| --- | --- | --- |
| Old servers keep running | Fact | publishing does not move players; Server Management restarts only outdated servers; restart does not block invites, teleports or profile joins. Delay up to 4 h (staff 2026-02-12; mirror page still says 60 min) |
| Restart notice | Fact | `game.ServerRestartScheduled` (2026-06-18) fires on delayed restarts (reason DeveloperUpdate or RobloxMaintenance, restart time); Open Cloud `restartServers`. A chance to save, not a guarantee |
| Configs | Fact | ConfigService is server-only; publishes in ~15-60 s (or gradual over 15 min); an existing snapshot does **not** change by itself: watch `UpdateAvailable`, call `Refresh`; `SetTestingValue` is session-only; restoring history stages a value that must be published |
| Experience Betas | Fact | stay public and searchable but drop Home recommendations; not a private test branch (one game lost recommendations for days by enabling it by mistake) |
| Experiments | Fact | 14-60 days, control + 2 variants, one per key; enrolment on `GetValue`; Early Harm Detection (2026-10-01) needs 10,000+ enrolled before it flags, so no flag in a small game means "not enough data", not "safe" |
| Mixed writers | Opinion | a session lock does not stop an old server misreading a new save; finish moving servers (or fence old writers) before an incompatible save change |
| Rollback is three jobs | Fact / Opinion | place version restore creates a version that must be published plus a server restart (player data untouched); data store versions are hourly (not per write), kept 30 days; daily snapshot; `GetVersionAtTimeAsync`; Data Stores Batch Processor CLI (at-least-once, so idempotent jobs). Order: stop dangerous writes → roll back code or config → repair data for affected keys only |
| Incidents | Fact | Tower Defense Simulator 2024: migration picked the store with the latest `UpdatedTime`, so stale data that was rewritten won (lesson: choose by version rule, not timestamp). Plane Crazy 2024: restored data while bad writes continued. Midnight Racing 2025: a platform regression, not the game's publish |
| First hours | Opinion | watch together: outdated-server count, new-version errors and performance, data store status codes, successful operations; add counters for refused future-schema saves, migration done, lock lost, receipt failures. Real-time performance alerts with webhooks are live (2026-07) |

## 3. Performance budgets [§3] (all thresholds are the paper's Opinion: starting gates, dated 2026-10-20)
| Metric | Floor phone (Galaxy A13 4 GB / iPhone SE 2, 30 FPS) | Target (Galaxy A54 / iPhone 13 / Iris Xe laptop, 60 FPS) |
| --- | --- | --- |
| Frame interval | p95 ≤ 35 ms, p99 ≤ 50 ms, ≤ 1 hitch > 100 ms per 10 min | p95 ≤ 18 ms, p99 ≤ 25 ms, ≤ 3 hitches > 50 ms per 10 min |
| Client CPU and GPU (each) | p95 ≤ 25 ms | p95 ≤ 12 ms, p99 ≤ 16 ms |
| Our scripts | - | client p95 ≤ 3 ms; server p95 ≤ 4 ms |
| Client memory | ≤ 1,000 MB steady, ≤ 1,200 MB peak | ≤ 1,500 MB steady, ≤ 1,800 MB peak |
| Server | work p95 ≤ 12 ms, ≥ 59 FPS; physics p95 ≤ 3 ms; memory ≤ 3,000 MB and < 50 % of allocation | |
| Remotes | client → server ≤ 30 events/s and ≤ 5 KB/s per player; server → client ≤ 10 KB/s per player | |
| Network total | receive p95 ≤ 30 KB/s, send ≤ 10 KB/s; investigate > 50 KB/s for 5 s | |
| Join | cold p50 ≤ 5 s, p95 ≤ 10 s (constrained network ≤ 15 s) | |
| Leak gate | memory at the same checkpoint rises ≤ 5 % (or 50 MB) over 20 cycles; any steady climb blocks release | |
| Review triggers | > 50 moving replicated assemblies near a client; streaming pause p95 ≤ 250 ms | |
Method (Opinion): 15 min warm-up, three 10-min scripted routes (spawn, crowded hub, combat, map edge, respawn, shop, chat); record device, OS, build, quality level, heat, battery; per-frame distributions, never averaged percentiles; ≥ 100 joins for a join p95. Facts: P10 FPS on the dashboard is the slow end; Peter McNeill's 2024 Roblox demo budgeted 300k triangles / 300 draw calls for the map + 200k / 200 for dynamic content; UnreliableRemoteEvent limit is 1,000 bytes since 2025-03-12.

## 4. Exploit resistance [§4]
| Item | Label | Detail |
| --- | --- | --- |
| Test priority by damage (economy game) | Opinion | 1 durable asset corruption (replayed claims, overlapping trades, save failure mid-trade); 2 arbitrary reward or permission (bad types, NaN, wrong ancestry, forbidden ops); 3 contact-driven rewards on client-owned parts; 4 movement and combat advantage; 5 hidden state delivered to clients early; 6 innocent players punished by a detector. Shooters move 4 and 5 up |
| Test rules | Opinion | owned private test place only, synthetic data, no exploit code; stop if a test touches production data or real players |
| Prevalence | Fact | no reliable public data on how common each attack is or how accurate detectors are; do not judge a detector by ban counts |
| Ban API | Fact | `Players.BanningEnabled` set in Studio; ≤ 50 ids; device block (2026-06-04) is Windows/macOS only, 24 h, needs the player online; a website unban does **not** clear a device block: use `UnbanAsync` in the game. Rehearse unbans before enforcing |
| Alternatives | Fact | Server Authority (live 2026-07-09); Chickynoid (open-source character simulation, invasive) |

## How it maps to the kit
- J001 step 6 (architecture + code review): §1 test lanes and fixtures, §2 release and rollback, mixed-writer rule.
- Revise approved skills: `performance` (proposed budgets table, method, P10 note); `data-saving` (future-schema fixtures, mixed writers, TDS lesson, rollback order, Batch Processor); `networking-security` (damage-ranked test list, ban rehearsal, device-block unban); `analytics` (Configs refresh behaviour, Early Harm floor); `studio-mcp` (StudioTestService for multi-client, teleports not testable in Studio).
