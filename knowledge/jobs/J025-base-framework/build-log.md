---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# J025 build stage: state log (read this first after a compaction or in a fresh session)

## Resume here (2026-10-24, stopped by the owner before step 8)

| Item | State |
| --- | --- |
| Done (gate-verified, Lune lane) | Steps 1-7 and 9. All 12 blocks built and reviewed ready (reviews/code-final-r3.md); protected acceptance tests PASS: Session 51 specs / 19 plants, Net 37 / 31, Admin 19 / 32; framework gate `python tools/gate.py` RESULT: PASS (488+ specs, 43 s); template + `tools/new_game.py` make a game whose gate passes (ProofGame); kit books written, sync_harness in sync, kb_index lint 0 errors |
| Not run | Step 8 Studio proof (2-client success test, Q6 engine numbers); every `*.engine.spec.luau` (list: `python tools/gate.py` engine lane); (kit `tools/verify.py` now PASS, 2026-10-24: sync 347 in sync, kb_index lint 0 errors, indexes current, 1291 tests) |
| Not verified (engine) | ProfileStore on a real DataStore (S-T17; needs a test universe); Session F1/F2/R2-1 timing on the engine; Net flood heartbeat and packets after PlayerRemoving (R2-1 reach); Anim markers in the framework player; Screens gamepad InputContext; Admin panel, fly and noclip on a real client; State real wire bytes and per-change cost (T-7); Loader client boot and Screens.register WaitForChild PlayerGui; CI on GitHub |
| Next session | 1. Free memory (close the two game Studio windows if the owner agrees: 2 clients need ~5 GB). 2. studio-operator: engine Jest batch on the framework test place (`tools/engine/run_jest.luau`, Edit DM + play-Server lane) + R2-1 probe; fix findings. 3. studio-operator: ProofGame success test with `StudioTestService:ExecuteMultiplayerTestAsync` (2 clients, else 1 + note), admin done for -1 and refused for -2, Q6 numbers. 4. G3 packet (step 10). Open tickets: T-3, T-15, T-16, T-17 below |
| Commits | Framework repo: `a332f75` pushed to `Enjukku/roblox-game-framework` main (owner: "just go ahead and commit"); CI on GitHub not read. Studio Kit: the lead chat commits J023, J024 and J025 together (J025 sends it the path list); package notes moved from `knowledge/reference/packages/` (git-ignored by `Packages/`) to `knowledge/reference/libraries/` |
| Close items | merge `side-session-notes/local_d3c22317…/J025-agent-memory/` into `StudioKit/.claude/agent-memory/<role>/`; probe scratch (Blink/Zap source) kept at `side-session-notes/local_d3c22317…/J025-probe-scratch/` |


Session: build stage, side session of the J024-era lead chat. Inputs: `build-plan.md` (Q1-Q9, steps 1-12), `proposal.md` (L1-L19 as amended, L16 removed), `decisions.md` (J025-G1, J025-D2, CD-1..CD-6).

## Fixed by the lead for every agent

| Item | Value |
| --- | --- |
| Framework repo | `C:\Users\Firew\Downloads\uterd\roblox-game-framework` (clone of private `Enjukku/roblox-game-framework`, empty on 2026-10-24). No commit, no push until the owner says so. |
| Repo layout | `src/<Block>/` code + specs per block; `contracts/<Block>.md`; `vendor/<Package>/` pinned third-party copies with `PATCHES.md`; `tools/` gate, copy tool, lock check, spec runner; `template/` game template (step 7); `CHANGELOG.md`; `.github/workflows/ci.yml` |
| Kit checkout | Touch only `knowledge/jobs/J025-base-framework/` and, at step 9, the book files step 9 lists. Never stage, revert or edit other files (other sessions have uncommitted work). Commit nothing in the kit. |
| Kit gate wiring | Step 2 names "kit copy tool + lock-hash check in `tools/verify.py`". `tools/verify.py` is outside the files this session may touch: the copy tool and the lock check live in the framework repo and run in each game's gate (template). Wiring into the kit's `tools/verify.py` = G3 open item. |
| Studio | Never drive the two open game windows (`NO MORE FOOD` f89548c2..., `Build Dam Save City` a4adc054...). One throwaway probe place, built by `rojo build`, opened with `C:\Users\Firew\AppData\Local\Roblox\Versions\version-7aaa6838d36c4448\RobloxStudioBeta.exe <file>.rbxl`. Machine memory is low (1.3 GB available on 2026-10-24): one probe window at a time, one driver. |
| Open Cloud Luau Execution | No Open Cloud key in `knowledge/design/keys.json` (all blank except ElevenLabs). Probe P2 is blocked; alternative lane: Jest inside Studio driven by MCP (plugin context, `StudioTestService` run/play mode). Owner key = G3 follow-up. |
| CI | GitHub Actions runs only after a push (owner's word). Until then: the same gate script run locally; CI = not verified. |

## Step status

| Step | Status | Evidence / file |
| --- | --- | --- |
| 1 Probes | P2 blocked (no key → Jest-in-Studio lane), P3 pass (roblox/jest 3.20.1; Edit DM via MCP 0.42 s; play-Server lane needs LoadStringEnabled in project; strict needs wally-package-types + negative control), P4 pass (marker ±1 frame; server→client and client→server replicate; LoadAnimation twice = 2 tracks; client reuses track object on replay: connect markers once per track), P5 pass with 1 client (ExecuteMultiplayerTestAsync from MCP Edit; child ids appear; EndTest returns value; 2 clients need the game windows closed: ~1.5 GB per process). P1 offline: Blink 0.18.9 picked (5/5; Zap 0.6.29 fails 3/5: ranged vectors break, `--!nocheck`, non-deterministic); gaps G1-G9 for Net; G6: a bad packet raises an error and drops later events in the batch. P1 runtime in Studio: 38/38 as expected (G1-G4, G6 confirmed; bad-packet flood 1000/s: heartbeat 16.7 → 42.3 ms avg, 5 log lines per bad packet). **Step 1 done.** | `probes/p1-transport/verdict.md`, `probes/p2-5-engine/verdict.md`, `probes/p1-transport/` |
| 2 Repo and gate | done locally (lead re-ran: RESULT: PASS, 3.9 s). 7 checks + transport/engine slots. Copy goes to `<game>/Framework/` (wally wipes Packages/). Open: Blink pin + transport check, engine lane, tests/ root for QA specs, server-only code must not map under ReplicatedStorage (architect/template). CI not verified (no push) | `tools/gate.py`, `README.md` |
| 3 Contracts | **done** — written (12 blocks + README, 139 test rows; groups G1-G4; placement table; Net G6 fix = post-generation patch + schema lint; Session hard tests on a Lune FakeWorld, no ProfileStore patch). Contract review r1: fix-first, 10 blocking (F1-F10 in Session, Net, Admin, Anim); 9 ready. Repair round 1 by the architect closed F1-F10, R1-R7 (r2). r2 found F11 (ProfileStore shutdown release would kick all players as "session moved") + N1-N3: the lead applied the reviewer's exact smallest fixes to Session.md (S12, H-S5, receipt row), Loader.md (ResetOnSpawn, L-T14), Admin.md (Ad4 snap formula), Net.md (N8 queue cap wording) on 2026-10-24 — text taken from reviews/contracts-r2.md, no other change. **Contracts frozen for build.** Lead decisions: client boot failure = error() + visible message, no kick; creator counts as admin only when CreatorType is User. Lead accepted the architect's defaults as PROPOSAL: Admin save view online only; Studio admins = UserId -1 + place creator | framework `contracts/`, `reviews/contracts-r1.md` |
| 4 Blocks | **all 12 built** (Admin last, 2026-10-24); history: B1 Helpers+Types+Analytics, B2 Config+Motion+ContentTests; S2b done (require rule `@game/<Service>/Framework/<Block>` per REQUIRES.md, documented in LuaGlobals.yaml:621-627; placement via tools/placement.json; Blink gate step; tests/acceptance root; engine lane lists *.engine.spec.luau); S2c (Wally packages in Lune) working. Engine specs written, not run (memory 0.5-0.8 GB free). Asked parent session 2026-10-24: may the owner close the two game windows for engine runs + 2-client proof (default: 1 client) | `evidence/<Block>.md` |
| 5 Hard tests | Admin: **PASS** (19 specs, 32/32 plants). Net: **PASS** (37 specs, 31/31 plants, bound to init 9067f189…). Session: **PASS** (51 specs incl. same-server rejoin A26-A31, 19/19 planted faults; bound to src/Session/init.luau 089fd470…; F-Q1 decided as CC-4); QA used FakeWorld (src/Session/test/FakeWorld.luau); Net, Admin: after their builds | tests/acceptance/ |
| 6 Reviews | **done**: every block ready (final recheck code-final-r3.md, gate PASS 488 specs, 2026-10-24). History: G1 round 1 (code-g1-r1.md): ready Helpers, Types, Loader, Config, Motion, ContentTests, State, Anim; fix-first Screens F1 (close inside build removes wrong entry), Analytics F2 (NaN value); repair round 1 done (F1, F2 closed; reviewer recheck pending, batched). Rulings: State cost mostly charm-sync (per-frame budget from T-7), T-6 leave duplicated helper, CC-1..3 accepted; Config.md text N1 and Motion M2 text at step 9. Engine check first at step 8: Screens.register WaitForChild PlayerGui in client init. Session, Net, Admin deep reviews after QA | reviews/code-*.md |
| 7 Template | built: one command (`tools/new_game.py`) makes a game whose gate passes; sample Coins system; Admin wiring pending B8 | template/, evidence/Template.md |
| 8 Proof | **NOT RUN** — owner 2026-10-24 (via the J025 lead chat): "just go ahead and commit we wont be testing rn i need to restart my pc". Was waiting for memory (101 MB available at 2026-10-24 after step 6; kit writer running). Plan: (A) engine Jest batch + R2-1 probe on the framework test place, then (B) the success test on ProofGame (scratchpad/ProofGame) with StudioTestService, 2 clients if ≥ 3 GB free, else 1 client | |
| 9 Kit books | **done** (evidence/kit-books.md). Lead fixes for the kit gate: stray agent memory written under this job folder's .claude/ (cwd effect) moved to the shared notes folder `J025-agent-memory/` (close item: merge into StudioKit/.claude/agent-memory); third-party Blink/Zap source clones moved from probes/p1-transport/scratch/ to notes folder `J025-probe-scratch/`; 28 frontmatter types fixed; kb_index regenerated → lint 0 errors, indexes current. Kit verify.py re-run in background | evidence/kit-books.md |
| 10 G3 packet | not started (after step 8) | |

## Crew (hand-spawned)

| Role | Task | Model · effort | Agent id | Status |
| --- | --- | --- | --- | --- |
| feature-builder | J025-P1 Blink vs Zap probe (offline + runtime harness) | opus · medium | a9c8204f8e5312603 | done |
| studio-operator | J025-P2-5 engine probes (Jest, Anim, multi-client) | sonnet · medium | a12ac4e64486fe379 | done |
| feature-builder | J025-S2 repo + gate skeleton | opus · medium | aa3542cd02457293f | S2b, S2c done (Wally packages load in Lune; Net tools in src/Net/tools/) |
| architect | J025-S3 block contracts | opus · high | a14a2c419b51f2bab | resumed: contract fix round 1 |
| studio-operator | J025-P1-RT Blink runtime in Studio | sonnet · medium | a8d1b880035c29228 | done |
| reviewer | J025-S3-R1 contract review | opus · high | a43e8ce39b3750a4f | done (r1) |
| feature-builder | J025-B1 Helpers, Types, Analytics | opus · medium | a0268be41f3b9f94a | done: Helpers+Types+Analytics, 32 specs, 25/25 planted faults; open: Analytics.custom passes NaN value (lead: add finite check in review round) |
| feature-builder | J025-B2 Config, Motion, ContentTests | opus · medium | a3e9268f02f425ee9 | done: Config 20, Motion 12, ContentTests 15 specs; faults 9/9, 5/5, 6/6 |
| reviewer | J025-S3-R2 contract recheck | opus · high | afc1b6f3d26be1da7 | done (r2) |
| feature-builder | J025-B3 Loader | opus · medium | ae07be8e401f7d70c | done: Loader 15/15 Lune specs, engine specs written not run; whole gate pending other blocks |
| feature-builder | J025-B4 State, Screens | opus · medium | a5fc693895cf35ba2 | done: State 13 + Screens 15 specs, faults 7/7, 10/10; whole gate PASS 7.6 s; State Q6 0.15 ms/change @50 players vs 0.1 ms PROPOSAL budget (re-measure in engine at step 8); per-player wire key "<name>@<UserId>" (charm-sync has no per-player syncer) |
| feature-builder | J025-B5 Anim | opus · medium | a8c26581c12e2e674 | done: Anim 25 specs, 13/13 faults; template ticket: Workspace.PlayerCharacterDestroyBehavior = Enabled via Rojo |
| feature-builder | J025-B6 Session | opus · high | a178b4737f5bcd7e4 | done: Session 42 specs, gate PASS (198 specs), 4 named + 14/14 sweep faults red, ProfileStore unpatched; Q6 update 6.8-8.2 µs |

## Tickets for later steps

| Id | For step | Ticket | From |
| --- | --- | --- | --- |
| T-1 | 6 review | Analytics.custom passes NaN/inf `value`: add a finite check (lead decision) | B1 |
| T-2 | 7 template | Template project sets `Workspace.PlayerCharacterDestroyBehavior = Enabled` via Rojo `$properties` (Anim respawn cleanup) | B5 |
| T-3 | 7 template | L-T12 needs a test entry that waits for PlayerAdded before Loader.start (recipe in Loader.multiclient.engine.spec header) | B3 |
| T-4 | engine batch | Run every `*.engine.spec.luau` in one probe window (Loader, Analytics, Anim lanes 1-2, the rest as they land) | all |
| T-5 | 7 template | How a game's Lune spec requires ContentTests (placement "none"; contract's `@framework/` alias does not exist): template gives a runner alias or relative path | B2 |

## Contract changes after freeze (lead decisions, applied to the contract text at step 9 or by the next contract edit)

| Id | Contract | Change | Reason / evidence |
| --- | --- | --- | --- |
| CC-1 | ContentTests.md | `export type Rows = {}` and `rule(key, row: Row)` with `Row = { read [string]: unknown }`; the five functions unchanged | contract type rejected every real table under the new solver (B2 probes, evidence/ContentTests.md) |
| CC-2 | Motion.md Usage | annotate the rows, then freeze (`local rows: { [string]: Motion.Row } = {...}; return table.freeze(rows)`) | unannotated frozen literal fails type check (evidence/Motion.md Q9) |
| CC-3 | Motion.md Lifecycle | reads `GuiService.ReducedMotionEnabled` at each play instead of a change connection (same truth, nothing to clean) | B2 decision; reviewer to confirm |
| T-6 | 6 review | Sampled-warn helper duplicated in State and Screens (and others): one shared helper in Helpers if a reviewer agrees | B4 |
| T-7 | 8 proof | Re-measure State per-change cost at 2 players in the engine; budget decision with the number | B4 |
| qa-lead | J025-Q1 Session protected hard tests | opus · medium | a3a70810e4dfb7284 | Q1c done: PF1-PF3 red, 19 plants total, 51 acceptance specs ×3 green on 089fd470; Q1b done: A26-A31 (A26 F1, A27 F2 red on 359dbebc as intended); PF1-PF3 plants after fix lands; earlier: 24 Session acceptance specs PASS, 16/16 planted faults, 3 identical runs (test-plans/Session.md) |
| feature-builder | J025-B7 Net | opus · high | a36519dcdb2383e9c | done: Net built, gate PASS incl. transport; 40/40 planted; Lune accepted 2.0 µs, denied 0.2 µs; 1,000-bad flood → 1 log line (Lune); engine rows not run |
| T-8 | 6 review (Session repair) | Leave mid-load + rejoin same server while the first load is throttled → ends `degraded` (ProfileStore hands back the cancelled result, init.luau:1433-1446, 1603-1605). Lead: fix in the Session repair round (retry StartSessionAsync while still loading, bounded by the 120 s timer), not a follow-up | B6 |
| T-10 | 6 Net review | `Remotes.X.Fire(player)` after a yield to a departed player creates a lasting PlayersMap entry (Blink); lead prefers a patch step that drops entries of departed players over a rule for games: reviewer to rule | B7b |
| T-11 | after Admin | install.py also locks the dev tools a game gets (tools/spec, tools/types, jest.config, roblox-std.yml): an edited spec runner could pass tests falsely (lead decision) | S7 Q2 |
| T-12 | 8 proof | run_jest.luau must also scan the game's ServerScriptService.Server and ReplicatedStorage.Client for engine specs | S7 Q3 |
| T-13 | tools | gate types check counts DeprecatedApi warnings in src/ as failures | Admin lesson |
| T-14 | integration ticket | Admin R1 (exempt only when value differs from StarterPlayer default) + R2 (`minRank >= 1`) with specs and plants; PATCHES.md LF-normalised hashes; template Admin wiring (ADMIN-PENDING); T-11; T-12; T-13 | Admin review |
| T-15 | G3 packet | Admin status is cached per join: a player removed from the allow-list or demoted stays admin until they leave (PROPOSAL, owner may want a re-check); text maxLength counts bytes | Admin QA |
| T-16 | G3 packet | jump slider step 1 cannot hit the JumpHeight default 7.2, so the jump exemption lasts until respawn (PROPOSAL: step 0.1 or snap to default); the template's own tools/gate.py is not locked | T-14 |
| T-17 | framework repo | CHANGELOG "Vendored" says ProfileStore has no patches (PATCHES.md lists P-1); contract usage examples still use the `require(Framework.X)` placeholder; no tag yet, so `install.py --ref <tag>` cannot run until the owner allows the first commit + tag | S9 |
| T-9 | G3 packet | ProfileStore warns once per DataStore error, not sampled (init.luau:425); accepted, no patch | B6 |
| reviewer | J025-R-G1 review of 10 non-risky blocks | opus · medium | a46350cd4f91874f7 | done (G1 r1) |
| feature-builder | J025-R-G1-fix1 Screens F1, Analytics F2 | opus · medium | a4b5d366ea6f9749b | done: F1, F2 closed red→green, 3/3 planted; Screens a3da6bed…, Analytics e53bdc08…; recheck pending (batch with next review) |
| CC-4 | Session.md | `Purchased` fires **at most once** (0 when the first confirmation failed and a later server returns it as a duplicate); games never grant or count revenue from this signal | QA F-Q1 (test-plans/Session.md) |
| CC-5 | Session.md | note: the IsActive guard cannot be reached through events with ProfileStore 1.0.3 (OnSessionEnd is synchronous, init.luau:720-726); keep it, held by Writes.spec direct-state spec | QA F-Q2 |
| reviewer | J025-R-Session deep review r1 | opus · high | ae644ab38d24f79c0 | done: fix-first, F1 lost save on same-server rejoin after failed leave save; F2 = T-8; N1 rec |
| feature-builder | J025-R-Session-fix1 F1, F2, N1 | opus · high | a66b70a72726bff14 | done: F1, F2, N1 fixed red→green; init.luau 089fd470…; gate PASS 284 specs; Rejoin A26-A31 green; open window: in-flight autosave clears release mark early |
| CC-6 | Session.md | failure row: a leave save that never answers or fails past the 40 s steal time → next server steals, record = last landed save; after F1 fix a same-server rejoin ends degraded at 120 s; a hung release holds BindToClose until the 30 s kill | review code-session-r1 F-Q3 ruling |
| reviewer | J025-R-recheck2 Session, Screens, Analytics fixes | opus · high | ab30edb57a79ae150 | done (r2): Session, Screens, Analytics ready; R2-1 window proven, not blocking |
| feature-builder | J025-B7b Net follow-ups (CC-7..CC-9, selene std) | opus · high | a6c7113a93605e1ed | done: CC-7..CC-9 + selene std; Net-T21 G10 100→0; Net 33/33; init 778b4a74…, patch 7f683410…, Generated/Server db9a6a81… |
| feature-builder | J025-B8 Admin | opus · high | af2a6756a46726820 | done: Admin 47 specs, 14/14 planted; ~1,515 lines vs 400-600 estimate (Panel 399): reviewer to judge size; engine rows not run |
| CC-7 | README.md Types | `AnswerListen<A...> = ((Player, A...) -> Reply) -> ()` (Blink function On returns nothing) | Net builder Q-1 |
| CC-8 | Net.md | patch step 5: no send-buffer entry for a player who left during a yielding function handler (gap G10) | Net builder Q-3 |
| CC-9 | README.md / Net.md | install.py copies `src/Net/tools/` to the game outside the place tree and skips `src/Net/Generated/` | Net builder Q-2 |
| feature-builder | J025-S7 game template + new_game.py | opus · medium | a606e46d6edad2067 | done: new_game.py → Coinsville in 20 s, game gate PASS; 10/10 planted; success test traced; Admin wiring pending (template/src/admin/Pages.luau:4 ADMIN-PENDING); T-3 not done |
| CC-10 | Screens.md:56 | closeEntry uses `janitor:Cleanup()` not `Destroy()` (a yielding build may still Add after close) | recheck r2 N-T1 |
| feature-builder | J025-R-Session-fix3 R2-1 (ProfileStore patch P-1) | opus · high | a5c9a2bd9b35f5ee0 | done: R2-1 closed; vendor P-1 (1 functional line, OnAfterSave passes is_ending_session); records byte-identical on/off; ProfileStore cfda9e90…, Session 4dee4521…; gate PASS 293; recheck of this diff batched with the Admin review |
| reviewer | J025-R-Net deep review r1 | opus · high | a48fbdd46e277af28 | done (r1): fix-first F1 event flood in one packet (~100 ms/packet Lune, never blocked), F2 departed-player send buffer leak (T-10), R1 unbounded client arrays |
| qa-lead | J025-Q2 Net protected hard tests | opus · medium | a45d76fab18d13553 | Q2c done: 37 specs + 31/31 plants ×3 on init 9067f189…, gate PASS; Q2b done: 37 Net acceptance specs + 30/30 plants PASS ×3 on init 18bbd1c5…, Server e5066c66…; full gate PASS 482 specs; earlier: 37 Net acceptance specs; 33 green, F3-F5 + L4 red as intended (review F1, F2) on 778b4a74; 28/28 plants; plants for CC-13/14 after fix hash |
| CC-11 | Session.md:70, :121 | ProfileStore is vendored **with patch P-1** (PATCHES.md); the never-used fallback text replaced by a pointer to P-1 | Session fix3 |
| CC-12 | Net.md usage | Net.Policy literal writes `beforeReady = false` explicitly (new-solver optional-field issue at call sites) | S7 Q1 |
| feature-builder | J025-R-Net-fix1 F1, F2, R1 | opus · high | a7916049487daaf4f | done: F1 (per-event allowance; 65,535-event packet 107 → 1.2-1.7 ms Lune), F2 step 6, R1 lint, CC-17; init 18bbd1c5…, Server e5066c66… |
| CC-13 | Net.md | per-player **event** allowance (PROPOSAL 600/s, burst 600) checked once per event in the patched dispatcher; empty → `error("flood")` = one reject + one strike | Net review F1 |
| CC-14 | Net.md | patch step 6: StepReplication drops PlayersMap entries of departed players (covers Fire, FireList, replies, any PlayerRemoving order) | Net review F2 (T-10) |
| CC-15 | Net.md lint | client arrays must be bounded `[..n]`, n ≤ 511 | Net review R1 |
| CC-16 | Admin.md | the admin's cloned client gets its transport by an ObjectValue link to the game's generated Blink Client module (`Def.client`), read as `.Framework.AdminAction` | Admin Q1 |
| CC-17 | Net.md schema | AdminAction target range allows negative integers (Studio test players -1, -2); server still checks a present player | Admin Q2 |
| CC-18 | Admin.md | core.info push budget 8 KB (PROPOSAL; 10 players + 100-line log = 5.4 KB) | Admin Q3 |
| CC-19 | README placement, Admin.md | all of Admin incl. client source sits in ServerScriptService (never replicates; cloned to admins only); group rank via GroupService:GetRolesInGroupAsync (GetRankInGroupAsync is deprecated) | Admin decisions |
| reviewer | J025-R-Admin deep review r1 + Session fix3 recheck | opus · high | a0154517ead8c4243 | done: Admin ready (no blocking; R1 walk-speed reset keeps exemption, R2 minRank 0 makes everyone admin — lead: fix both), no over-building cuts; Session R2-1 closed; N1 PATCHES.md hashes must be LF-normalised |
| qa-lead | J025-Q3 Admin protected hard tests | opus · medium | a682a94795e6768ed | done: 19 Admin acceptance specs PASS, 32/32 plants, 3 identical runs on init a509b4f5…, Builtins 6f4e60f5… |
| reviewer | J025-R-Net-r2 Net recheck | opus · high | af6724b95004b2d70 | done (r2): Net ready; F1, F2, R1, CC-17 closed; recs R2-1 departed sender unbounded, R2-2 nested arrays pass lint → lead: fix both (round 3) |
| feature-builder | J025-T14 integration (Admin R1/R2, template Admin, locks, deprecated gate) | opus · medium | ac154c5eee6f68dc7 | done: T-14 items 1-8; ProofGame gate PASS (scratchpad/ProofGame); Admin init bb129382…, Builtins cbf4e7ee…; PATCHES.md LF hashes; install copies + locks test/ helpers and dev tools (README line fixed by lead) |
| feature-builder | J025-R-Net-fix3 R2-1, R2-2 | opus · high | a25defacc8e791c64 | done: R2-1 (allow false for departed sender), R2-2 (lint ≤ 512 values per message, 7/7 plants); init 9067f189…, lint fad552c2…; QA plant P03 obsolete → retarget |
| architect | J025-S3-fold contract text update CC-1..CC-19 | opus · medium | aac430c75bbabf3ce | done: CC-1..CC-19 + review text folded into 8 contracts; R2-1/R2-2 text ahead of code until Net round 3 lands |
| reviewer | J025-R-final recheck (Admin T-14, Net r3, template Admin) | opus · medium | ab65650a69e232b9c | done (r3): all closed, ready for Studio proof; gate PASS 488 specs |
| general-purpose (kit-writer stand-in) | J025-S9 kit books | opus · medium | a30fe40d90f91bdb8 | done: items 1-11 (framework.md 247 lines, 12 cards; skills §8 sections; packages exception; 7 package notes in knowledge/reference/libraries/); sync_harness in sync 347 |
