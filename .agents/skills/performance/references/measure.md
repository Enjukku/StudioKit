> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Facts extracted by a researcher agent (claude-sonnet-5-5, medium) from the docs mirror (upstream 7400643) and Roblox staff posts 2026; spot-checked by the orchestrator. Paths relative to `knowledge/external/roblox-creator-docs/`. PO = `performance-optimization/`, MP = `performance-optimization/microprofiler/`.

# Measuring performance

## Targets Roblox states
| Fact | Source |
| --- | --- |
| 60 FPS = 16.67 ms per frame; 30 FPS = 33.33 ms. Steady frame times matter more than average FPS | MP/index.md:56-65 |
| Client and server CPU time must stay under 16 ms for 60 FPS. Server heartbeat is capped at 60; lower means trouble (Dev Console → Server Jobs → Heartbeat) | production/analytics/performance.md:94,121; PO/identify.md:82-84 |
| Server memory: keep below 50 % of 6.25 GiB + 100 MiB × peak players (30 players ≈ 9.18 GiB); memory gained on join is not returned on leave | PO/identify.md:119-127 |
| Client crash rate above 2-3 %, or a jump after an update: investigate | PO/identify.md:140 |
| Draw calls, triangles, memory: **no official budget**. Pick a baseline device, measure there, derive your own limits (Roblox's example team: under 1,000 draw calls and 1,000,000 triangles on *their* baseline) | PO/design.md:17-19 |
| Players: Android ≈ 65 %; of those ≈ 60 % have 2-4 GB RAM; over half of all players on 10,000-20,000 Passmark devices | PO/test-on-hardware.md:30-38 |
| No join-time target; if loading takes more than a few seconds, consider streaming. `NetworkSettings.PrintJoinSizeBreakdown` lists the 20 largest instances | PO/test-on-hardware.md:102; PO/identify.md:149-176 |

## Tools
| Tool | How | What it does not tell you | Source |
| --- | --- | --- | --- |
| MicroProfiler | Ctrl+F6 (some pages say Ctrl+Alt+F6); Ctrl+P pauses; dumps in `%LOCALAPPDATA%\Roblox\logs`. Phone: Settings → MicroProfiler on, open the shown IP:port in a browser on the same network. Server: Dev Console → MicroProfiler → Server (≤ 60 frames). Bar colours: orange = scripts/physics/animation heavier, blue = rendering heavier, red = GPU wait > 2.5 ms | Colours are hints; the frame time is the goal | MP/index.md:71-242 |
| Your own labels | `debug.profilebegin("Name")` … `debug.profileend()` around suspect systems | - | MP/index.md:174-193 |
| Key scopes | scripts: `RunService.Heartbeat/PreSimulation/PostSimulation/PreRender`, `GC`, `WaitingHybridScriptJob`; physics: `worldStep`, `stepContacts`, `assemble`; avatars: `stepHumanoid`, `stepAnimation`, `updateInvalidatedFastClusters` (> 4 ms = churn); render: `Prepare`, `Perform`, `ShadowMapSystem`, `LightGridCPU`; network: `Replicator/ProcessPackets`, `Data Senders`, `Physics Senders`; UI: `fillGuiVertices`, `UpdateUILayouts`, `Rebuild Z-order list` | Full list: github.com/Roblox/libmp docs/ALL-SCOPES.md | PO/improve.md:47-543; MP/tag-table.md |
| MicroProfiler + Assistant/MCP | pause a capture, ask Assistant; agents: Dump → binary format, analyse with Lute + LibMP | Scope names not fully documented | MP/index.md:195-210; DF 4704417 (ZenMa1n, 2026-06-26) |
| LibMP | Luau API to profiler data on client, server and Studio (module from github.com/Roblox/libmp); enable for a fraction of sessions (costs memory); `SetMemTargetMB` | Other function names: read the repo | DF 4703136 (ZenMa1n, 2026-06-25, Oct update) |
| Script Profiler | Dev Console, client or server, 1 or 10 kHz; `<native>` marks native functions | CPU only, not waiting threads | studio/optimization/scriptprofiler.md:11-53 |
| Dev Console memory | F9 → Memory: PlaceMemory categories (Instances, LuaHeap, PhysicsParts, GraphicsTexture, Sounds, Animation, Gui …); Luau heap snapshots with diff | Studio numbers mislead (it runs server + client): use a real client | studio/optimization/memory-usage.md:39-152; PO/design.md:25 |
| Stats service | `FrameTime`, `RenderCPUFrameTime`, `RenderGPUFrameTime`, `SceneDrawcallCount`, `SceneTriangleCount`, `InstanceCount`, `MovingPrimitivesCount`, `PhysicsStepTimeMs`, `HeartbeatTimeMs`, `DataReceiveKbps`, `DataSendKbps`, `GetTotalMemoryUsageMb()`; category memory needs `Stats.MemoryTrackingEnabled` | Harmony* methods are internal only | _api-reference/classes/Stats.yaml |
| Render stats | Shift+F2: Draw (scene), triangles | - | PO/design.md:17-19 |
| Scene Analysis | Window → Performance Summary → Scene Analysis: script memory, unparented instances, instance and triangle composition, audio and animation memory; `SceneAnalysisService` API | Studio only; numbers differ from phones | PO/scene-analysis.md:17-114; DF 4620678 (MrChickenRocket, 2026-05-05) |
| Device Simulator | screen size, density, platform, touch, keyboard; Flagship / Mid-range / Entry tiers | **Not** CPU, GPU or memory (staff, 2026) | studio/device-simulator.md; DF 4861695 (avienn_a, live 2026-10-16) |
| Network Simulator | per-direction latency, jitter, loss; presets 3G (150/70 ms, 0.5 %) to fiber; scriptable via `NetworkSettings.Inbound/OutboundNetworkMinDelayMs`, `...JitterMs`, `...LossPercent` | Studio play-tests only | studio/network-simulator.md:29-246 |
| Real device | MicroProfiler + Dev Console on a phone; 10-15 min to see heat throttling; real cellular for network | - | PO/test-on-hardware.md:41-74 |
| Creator Hub → Monitoring → Performance | client FPS, crashes, out-of-memory exits, CPU time; server CPU, memory, cores used; P10/P50/P90; by place version (≥ 100 DAU). Client CPU by category (Scripts, Networking, Physics, Animation) | Only after launch | production/analytics/performance.md; DF 4737435 (quazotheduck, 2026-07-14) |
| Error Reports | ≤ 100 custom rules; first-seen version | - | production/analytics/error-report.md |

## Not settled (verify in Studio)
Physics default (adaptive vs 240 Hz: pages disagree; set `PhysicsSteppingMethod` explicitly). Ctrl+F6 vs Ctrl+Alt+F6. The mirror's device and network simulator pages still say "beta" (released 2026-10-16).
