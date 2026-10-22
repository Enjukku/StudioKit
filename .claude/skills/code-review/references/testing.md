> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Source: owner operations paper (`knowledge/reference/architecture/roblox-operations-2026-10.md` §1, §5), checked against the docs mirror (`_api-reference/classes/StudioTestService.yaml`). Tool versions are the paper's verified 2026-10-20 values; re-check on adoption (`rules/packages.md`). Player-facing cases and boundary brackets added by J018 maker reviewer · claude-opus-5-5 · high · 2026-10-22, built also from the owner's Riot transcripts (J018); the reviewer's planted-fault route added in J018 repair round 1 (scratch-copy commands run on a synthetic repository, J018 coverage table d).

# Testing Roblox code that AI agents wrote

## Test lanes
| Lane | Runs | Catches | Misses |
| --- | --- | --- | --- |
| Every change (the gate) | format, lint, strict type check (Luau-LSP `analyze`, `strictDatamodelTypes`), offline unit tests of pure rules and save migrations (Lune or the game's runner) | syntax, types, config errors, rule and migration logic | engine behaviour, replication |
| Merge | server tests inside the real engine: Jest (`roblox/jest` + `roblox/jest-globals`) through Open Cloud Luau Execution against an explicit test-place version (≤ 5 min per task, each task a fresh server); a short two-client Studio scenario | module loading, server wiring, simple concurrency | rendering, real devices, teleports |
| Nightly or risky change | 8-client churn (`StudioTestService:ExecuteMultiplayerTestAsync`), lifecycle counters, memory checkpoints | leaks, retention, join/leave races | production scale |
| Release candidate | physical floor phone + PC; published-game route through teleport, save and rejoin | device memory, real service journey | every device |

## Rules for a test result to count
- A structured result: tests found, run, passed, failed, skipped. **Zero tests, a timeout or a missing result is a fail.**
- Retry infrastructure errors with the same build; never retry a failing assertion until it passes.
- Test the production code from the same revision; publish only the production build, never the test build with its hooks.
- Teleports cannot be tested in Studio: say "not verified" until a published test.
- Save tests run in a **separate test universe** (places in the same universe share data stores).

## Fixtures and cases to require
| Area | Cases |
| --- | --- |
| Pure rules | normal, edge (0, max, empty), invalid (NaN, inf, wrong type, huge strings) |
| Saves | new account, each old schema, missing / extra / malformed fields, duplicate ids, huge valid balance, half-done migration, unknown future schema; old server + new save; lock lost; rejoin before the final save |
| Concurrency (2 clients) | simultaneous claim of one reward, trade while one player leaves, respawn during an ability, late join, stale client action |
| Lifecycles | 100 create/destroy cycles: counted connections and tasks back to zero; memory plateaus at idle checkpoints |
| Security | the damage-ranked list in `networking-security` N-15 |
| Player-facing truth (`presentation.md`) | the server denies the request: no success layer, label or sound; a slow answer shows the pending state; buy right after a gain while the count-up runs; a paid reveal's lowest and highest tier (the windup code path takes no tier); a bystander client during another player's effect; reduced motion on; a frequent effect at its real rate (live copies within the cap); two hit-stops overlapping, then an interruption |

## Tests that can fail
AI agents can write code and tests with the same wrong assumption. So:
- The **briefer** writes the acceptance examples and failure cases; the builder adds tests but does not change those expected results.
- Spot-check that a test fails on a deliberately wrong version (drop a field, grant twice, skip a check). A test that still passes is not a test. As the reviewer, first read the qa-lead's planted-fault result (caught x of n, false alarms y). Without it, plant one fault in a scratch copy outside the repository, never in the tree under review: `git archive -o <scratch>/cand.tar <candidate>` then `tar -xf <scratch>/cand.tar -C <scratch dir>` (two steps, so it also works in PowerShell), then run the covering test there with the game's offline runner. The copy holds only committed files (line endings follow `core.autocrlf`): install untracked folders (packages) there first; a run that errors is "not run", never a pass. If neither is possible, it is a could-not-check line.
- Bracket every limit the change sets: one case just inside and one just outside (price equal to the balance and one coin short; the rate limit's last allowed request and the next one; the cap's last copy and one more). A suite with only the middle case cannot see an off-by-one.

## Tool notes (verified 2026-10-20)
TestEZ is archived (2024-09-14): keep old suites, write new ones in Jest. Lune 0.11.0 has a limited Roblox API: pure logic only. run-in-roblox 0.3.0 (2020) is a legacy bridge into installed Studio. Record the Studio build with every engine test run.
