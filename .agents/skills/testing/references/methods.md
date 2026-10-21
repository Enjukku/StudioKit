> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Sources: owner engineering paper §7 and §11 (P249-P266, P339-P349), fact-checked (`knowledge/reference/engineering/paper/factcheck-practice.md`, `factcheck-engine.md`); first-game practice (`knowledge/reference/engineering/rework/` git-b §4, logs §6).

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

## 2. Planted-fault check (does the suite fail when it should)
1. Write down the intended observable failure for each fault before you plant it.
2. Plant one fault at a time in a copy: remove a validation, grant twice, skip cleanup, off-by-one at a boundary, wrong owner, stale state after a yield, order-dependence on a dictionary.
3. Run the suite on each copy. Caught = at least one test fails. Survived = a missing test: add it.
4. Run the suite on the correct build: every test must pass. A failure there is a false alarm and the test is wrong.
5. Record: caught x of n, false alarms y, with the fault list. Keep at least one clean control.

## 3. Studio scenarios
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
