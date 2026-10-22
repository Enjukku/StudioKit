> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Sources: owner engineering paper §7 and §11 (P249-P266, P339-P349), fact-checked (`knowledge/reference/engineering/paper/factcheck-practice.md`, `factcheck-engine.md`); first-game practice (`knowledge/reference/engineering/rework/` git-b §4, logs §6). Revised by J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (data oracles for what players see, presentation faults, conditions pointer); repair round 2 (J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22): range ends by where the range lives.

# Test methods

## 1. Oracles
| Oracle | Use for | How | First game |
| --- | --- | --- | --- |
| Exact expected value | stated examples in the brief | the brief's example, written before the code | — |
| Invariant over random sequences | rules over many states: support and collapse, inventory, economy, cooldowns | seed a random generator, apply 200+ random actions, check the invariant after each; print the seed on failure so it replays | the random-update oracle found 45-52 missed planes per 240 updates, then 0 in 384 |
| Independent simple model | a fast or clever implementation | a slow, obviously-right version of the rule (brute force); compare outputs on random inputs | — |
| Old-vs-new differential | "behaviour-identical" refactors and speed-ups | freeze a copy of the old module; feed both the same inputs (and fuzz); outputs must match exactly | 6 speed-up lanes merged with no rework |
| Golden output | a switch that must not change behaviour when off | hash or byte-compare the output with the switch off against the saved golden | Stage-1 checksum held across 120 blasts and every engine change |
| Spy / call counter | isolation: new rules must not run for ordinary content | count calls into the new module while unrelated content runs; expect 0 | windmill rules isolated after a revert |
| Server result in the log | what players see after a request: attempt cue, outcome layer, celebration, refusal | the builder's debug log (`FxLog`, `player-facing.md` §3) filtered by event id; the server's decision is the expected value; a rejected request expects 0 outcome lines | — |
| Gameplay data field | drawn danger edges, countdowns, counters, shown tiers | the data the effect or label reads (radius, fuse, balance, rolled tier) is the expected value; the debug hit shape is built from the same field, never from a second constant | — |
| Range ends, by where the range lives | randomised presentation | **Engine ranges** (particle properties; no seed exists for them): on the candidate in the play session, after a `Trigger`, `inspect_instance` (probe once that it shows keypoint envelopes; else one `execute_luau` read) on each layer the effect `spec.json` marks `semantic` (`vfx-craft/references/plan-and-spec.md`): `Lifetime`, `Speed`, `Rotation`, `RotSpeed` with Min = Max; every keypoint `Envelope` of `Size`, `Transparency`, `Squash` at 0; `FlipbookStartRandom` false; `SpreadAngle` (a random direction) equal to the spec's (the VFX designer's rule SP-06, read again on the candidate as protected acceptance; CP-09 is the same read on the spec). **Ranges the game's code rolls:** offline, inject a random source that returns the lowest, then the highest value; footprint, timing, colour role and tier identical. The `Seed` hook only repeats a server roll. The read is exact for what it reads, but: a layer whose instance name differs from its spec id is skipped silently (count layers read against layers marked); a layer wrongly marked decorative passes (the VFX designer's call: ask); randomness a script applies at emit time is invisible to it (read the effect's client code for `math.random`, `Random.new` and `NextNumber` on that layer); a `Rotation` range on a radially symmetric sprite reads as a FAIL but changes nothing a player reads (confirm with the VFX designer before the finding goes out) | — |

## 2. Planted-fault check (does the suite fail when it should)
1. Write down the intended observable failure for each fault before you plant it.
2. Plant one fault at a time in a copy: remove a validation, grant twice, skip cleanup, off-by-one at a boundary, wrong owner, stale state after a yield, order-dependence on a dictionary. Presentation faults, one per player-facing row group you run: the outcome layer plays on the client's prediction (shows on a rejected request); the ring is sized from its own constant 10 % larger than the data radius; the countdown runs on a local clock; affordability reads the tweened counter; a tier tint appears in the windup; the reduced variant drops the telegraph; a hue literal replaces the colour role; the live-copy cap or the merge window is removed; the telegraph is not removed on the damage frame; a size envelope or `FlipbookStartRandom` on a semantic layer.
3. Run the suite on each copy. Caught = at least one test fails. Survived = a missing test: add it.
4. Run the suite on the correct build: every test must pass. A failure there is a false alarm and the test is wrong.
5. Record: caught x of n, false alarms y, with the fault list. Keep at least one clean control.

## 3. Studio scenarios
The conditions players meet (phone viewport, busiest moment, graphics quality, latency, reduced motion, grayscale) and how to set each: `player-facing.md` §1.
- Play-test through Studio MCP (`studio-mcp` skill): start Play, act through the server or client data model, read state, stop. One driver per Studio.
- Multi-client: up to 8 clients in Studio; `StudioTestService:ExecuteMultiplayerTestAsync` runs programmatic multi-client tests and needs plugin security, so Studio must be open (no CLI route is documented).
- Repeat physics scenarios 3+ times and report each result; the solver is not fully deterministic.
- Teleport does not work in a Studio play-test: NOT RUN until a published test.
- Record the Studio build with every engine result.

## 4. Tools by job (four separate things)
| Job | Tool | Note |
| --- | --- | --- |
| Run pure Luau, strict analysis | Luau CLI 0.743 (`luau`, `luau-analyze`, 2026-10-16) | no Roblox APIs, no io; inject fakes |
| Fixture transforms, build scripts | Lune 0.11.0 (2026-10-11, built on Luau 0.740) | limited Roblox API: pure logic only; not engine proof |
| Test framework in the engine | Jest Roblox (maintained; runs through Open Cloud Luau Execution) | TestEZ archived 2024-09-14: keep old suites, write new ones in Jest |
| Build the test artifact | Rojo 7.7.1 (2026-10-02) `build` | build success is not test success |
| Run in the engine | Studio (MCP), Open Cloud Luau Execution | Luau Execution: 5 min per task, 10 incomplete tasks per place, no physics, scripts do not auto-run |
| Legacy bridge | run-in-roblox 0.3.0 (2020-07-20) | old; prefer Studio MCP or Luau Execution |

## 5. Scoring a test suite (for agent evaluation)
- Planted faults caught (x of n) and false failures on the correct build, reported separately.
- First-attempt result (before any feedback) apart from the result after repair rounds.
- Raw counts, the task list and what was excluded; no single blended score.
