---
name: performance
description: Keep a Roblox game smooth on phones - set budgets at design time, build with cheap defaults, measure the real bottleneck with the 2026 tools (MicroProfiler, LibMP, Scene Analysis, Script Profiler, device and network simulators, Creator Hub dashboards) and fix it. Use for "it lags", "low FPS", "hitches when X", "memory keeps growing", "slow to load", "will this run on phones", for budget planning of a new system, and before shipping anything with many parts, effects, NPCs or network traffic. Engine-level and universal; game-specific world or physics systems belong in the game's own notes.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 4. Evidence: `references/measure.md` and `references/fixes.md` (docs mirror upstream 7400643; Roblox staff posts 2026). Short source names (PO, MP) are defined at the top of `references/measure.md`.

# Performance: smooth on the players' phones

## 1. When this skill starts
- **Design:** a new system will create many instances, effects, NPCs, physics bodies, UI rows or network messages.
- **Build:** before merge, check the cheap defaults (§4 F-03).
- **Problem:** a report of lag, hitches, memory growth or slow joins.
Measurement rounds cost the owner time and usage (`rules/owner-profile.md`): run them when the brief asks, when a design budget is at risk, or when a problem is reported. Never as routine.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Targets, tool steps, profiler scopes, dashboards | `references/measure.md` |
| Starting budgets and a test method when the game has none | `references/budgets.md` (owner paper proposals) |
| The fix for a known bottleneck (scripts, render, physics, memory, network, streaming, UI, sound) | `references/fixes.md` |
| Driving Studio through MCP for a capture | `studio-mcp` skill (exclusive Studio, no log scans during a capture) |
| The game's baseline device and budgets | `knowledge/design/game-profile.md` (platform row) or the game's performance note |

## 3. Steps
1. **Know the baseline.** The game's baseline device (an entry-level Android unless the profile says otherwise) and its budgets. None recorded → start from `references/budgets.md`, mark them PROPOSAL, and replace them with measured numbers.
2. **Design budget** (new system): how many instances, draw-call groups, moving parts, effects, messages per second at worst case; where it runs (server, client); what streams. Write the numbers in the design note.
3. **Measure before fixing** (problem): reproduce, then one capture that names the bottleneck: frame colour and top scopes (MicroProfiler), memory category (Dev Console), or network senders. Add `debug.profilebegin` labels to our systems.
4. **Fix the named bottleneck** with `references/fixes.md`; one change at a time.
5. **Verify** with the same capture, same scene, same device class. Report before → after numbers and where measured (Studio, device, dashboard).

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| F-01 | **Budgets come from a baseline device, not from Studio.** Roblox publishes no draw-call, triangle or memory budget. Measure the baseline device and derive limits; Studio runs server and client together and misleads | PO/design.md:17-29 |
| F-02 | **Frame time is the target**: 16.67 ms for 60 FPS, steady. Server heartbeat 60. Server memory under 50 % of 6.25 GiB + 100 MiB × peak players | MP/index.md:56-65; PO/identify.md:82-127 |
| F-03 | **Cheap defaults when building:** anchor what does not move; Box/Hull collision and all three Can* off for decoration; `RenderFidelity` Automatic; `CastShadow` off on small, moving or transparent effect parts; reuse the same mesh and texture ids; textures ≤ 512²; transparency 0 or 1; one loop per system; connections owned by a cleanup object | `references/fixes.md` |
| F-04 | **Streaming on by default** for any game with a large or multi-area world; design models as Atomic or Nonatomic on purpose; client code never assumes a far part exists | workspace/streaming/index.md |
| F-05 | **The client draws, the server decides.** VFX, tweens, view models and cosmetic debris on the client; the server sends small deltas only on change | PO/improve.md:483-526 |
| F-06 | **Join size is a budget.** ReplicatedStorage downloads to every client at join: only client-needed content there; check with `PrintJoinSizeBreakdown` | PO/design.md:67; PO/identify.md:149-176 |
| F-07 | **Name the bottleneck before changing code.** Frame colour + top scopes, or a memory category, or a sender. A fix without a capture is a guess. Keep a fixed, repeatable test scene and record device, settings, player count and content version with every number, so a changed map is not mistaken for a changed algorithm. Test the peaks too: crowded fights, full inventories, long server uptime | MP/index.md:109-124 |
| F-08 | **Label our systems** with `debug.profilebegin/profileend` so captures show our names, not just `Heartbeat` | MP/index.md:174-193 |
| F-09 | **Leaks show over time:** compare instance count and memory after 10-15 minutes of normal play and after leaving and re-entering an area; they must return to baseline. Every cache names who clears it, and every sleeping or skipped object lists what wakes it: an optimisation that sometimes forgets an update is a bug | PO/improve.md:93-139; PO/test-on-hardware.md:56-74 |
| F-10 | **Big tools only on evidence:** Parallel Luau after a capture shows script-bound work that splits; `--!native` only for number-heavy server code, measured both ways; SLIM only for static far scenery | scripting/multithreading.md; luau/native-code-gen.md; slim.md |
| F-11 | **Simulators are partial.** Device Simulator checks layout and input, not CPU, GPU or memory; Network Simulator adds latency, jitter, loss in Studio tests. Real phones are the truth | DF 4861695 (2026-10-16) |
| F-12 | **After launch, the dashboard decides.** Creator Hub Performance by place version (P10/P50/P90, client CPU by category) shows whether an update helped real players | production/analytics/performance.md; DF 4737435 |

## 5. Rules (final check)
- No performance claim without a number, the tool and where it was measured.
- No per-object loops, connections or tweens for things that come in large numbers.
- No content that the client never uses in ReplicatedStorage.
- No PreciseConvexDecomposition, Precise render fidelity or high-res texture without a reason in the design note.
- Profiling runs with Studio to yourself and no other probes or log scans running.

## 6. Self-check before returning
- [ ] Baseline device and budgets named (or proposed).
- [ ] Bottleneck named from a capture, with before and after numbers on the same scene.
- [ ] Defaults in F-03 applied to new content.
- [ ] Memory and instance count return to baseline after the repeat test (F-09) when the change creates or destroys things.

Project overlay: if `knowledge/overlays/performance.md` exists, read it after this file; it wins for this game.
