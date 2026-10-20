> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Facts extracted by a researcher agent (claude-sonnet-5-5, medium) from the docs mirror (upstream 7400643) and Roblox staff posts 2026; spot-checked by the orchestrator. Paths relative to `knowledge/external/roblox-creator-docs/`. SEC = `scripting/security/`, RE = `scripting/events/remote.md`, SA = `projects/server-authority/`, Y = `_api-reference/classes/`.

# Networking and security facts

## Remotes
| Fact | Source |
| --- | --- |
| RemoteEvent: one-way, reliable, ordered (also across RemoteEvent instances, per connection and direction). RemoteFunction: two-way, yields. UnreliableRemoteEvent: may drop or reorder | RE:13-17,374-378 |
| The server handler's first argument is the real sending Player; the client controls every other argument | RE:140; SEC/security-tactics.md:25 |
| About 500 requests/s per client, shared by all remotes of one type. Over it, RemoteEvent **delays** the excess (keeps order); UnreliableRemoteEvent **drops** it | Y/RemoteEvent.yaml:37-45; RE:378,404 |
| UnreliableRemoteEvent: payloads over 1,000 bytes are dropped (buffers compress, size hard to predict); add a sequence number or timestamp and ignore older ones | Y/UnreliableRemoteEvent.yaml:55-63; RE:403-407 |
| No documented payload byte limit for RemoteEvent or RemoteFunction | not found |
| RemoteFunction and RemoteEvent have no order relative to each other. Ordering covers when handlers start, not finish | RE:385,393-395 |
| No handler connected: RemoteEvent queues (limited), UnreliableRemoteEvent discards. Undelivered messages are lost when a client leaves | RE:382-383,405 |
| `InvokeClient` is unsafe: a client error, disconnect or no return can error or hang the server forever. Use RemoteEvents to clients | RE:360-366 |
| Only the last `OnServerInvoke` assignment runs | RE:309 |
| What arrives: non-string keys become strings (do not mix key types, no nil holes); functions → nil; tables copied (identity lost); metatables lost; an Instance the receiver cannot see → nil | RE:417-621 |
| NaN and inf are valid numbers; NaN fails every comparison, so range checks pass silently. Reject with `math.isfinite` | SEC/client-server-boundary.md:85-124 |
| Remotes can arrive out of order relative to property and attribute replication | scripting/attributes.md:23; SA/index.md:263 |
| Deferred signals (`Workspace.SignalBehavior`): handlers run later; do not assume a handler already ran after firing. Default currently behaves as Immediate and will become Deferred; templates use Deferred | scripting/events/deferred.md:14,59-83 |

## Official validation guidance
| Rule | Source |
| --- | --- |
| Three layers: context and permission (alive, near, owns it), type and structure (cap string length and table size; a table can imitate an Instance, so check `typeof(x) == "Instance"` and `IsDescendantOf` a known folder), value (positive quantities, real ids, finite numbers) | SEC/client-server-boundary.md:17-92,303 |
| Hits: client sends origin + hit part or position, never a victim; server checks origin near the character (latency slack), hit near the part's server position, nothing static blocks the line; plus fire rate, server-held ammo, team, alive | SEC/client-server-boundary.md:141-153 |
| Rate limit every client path with a server token bucket per player; clear it on leave; client cooldowns are UI only | SEC/client-server-boundary.md:157-269 |
| ProximityPrompt can be fired from any distance, even disabled; only `Triggered` checks distance; hold events pass with HoldDuration 0. ClickDetector has no server checks; DragDetector checks only Enabled and PermissionPolicy | SEC/client-server-boundary.md:275-291 |
| Never let a remote name an arbitrary path or Instance to change or delete; never load assets or require code from remote arguments | SEC/client-server-boundary.md:303 |
| Relay remotes (client → server → all clients) validate everything before broadcasting | SEC/client-server-boundary.md:307-390 |
| Trades: validate all parties before commit, revert on failure (dupe races) | SEC/client-server-boundary.md:400-416 |
| Threat-model each feature: worst value per parameter, 1,000+ calls per second, effect on other players, worst resource use, least state exposed | SEC/security-tactics.md:48-54 |
| Design beats detection: sequential checkpoints, server-computed damage, server cooldowns plus inventory state, no reward for spawn kills | SEC/defensive-design.md:15-66 |
| Detection: signals (completion time, rate of gain, action cadence) feed a suspicion score; honeypot remotes no real client fires; consequence ladder: log → quiet mitigation → temporary restriction → visible action; prefer reversible; never ban on client-side detection | SEC/server-side-detection.md:19-86 |
| Exploiters can: decompile replicated scripts, own and move nearby unanchored parts (teleport, fling, NaN CFrames, suppress Touched), fire Touched and prompts at any range, change their local DataModel, set WalkSpeed locally, fire any remote with any arguments | SEC/security-tactics.md:19-27; SEC/network-ownership.md:15-37 |

## Replication and visibility
| Fact | Source |
| --- | --- |
| Everything replicated is readable, even unused: LocalScripts, client-context Scripts and ModuleScripts can be decompiled. ServerStorage and ServerScriptService never replicate | SEC/access-control.md:15,65; projects/data-model.md:198-230 |
| Never mix server and client logic in one replicated ModuleScript; no passwords in code; avoid guessable names for sensitive remotes | SEC/access-control.md:61-67 |
| Only server changes replicate to everyone; client changes stay local | SEC/access-control.md:51-53 |
| Any client can teleport itself to any place in the universe; set Places access control to "Secure within universe only"; keep test places in a separate private universe | SEC/access-control.md:19-45 |
| Anchored parts are always server-owned; `SetNetworkOwner(nil)` on gameplay-critical unanchored parts (some jitter). Detectors on client-owned assemblies can be dragged to the exploiter | physics/network-ownership.md:17-35; SEC/client-server-boundary.md:299 |
| Movement checks (without Server Authority): average over time, leaky buckets, XZ-plane projection, exempt real teleports | SEC/network-ownership.md:49-52 |

## Server Authority (live, opt-in, 2026-07-09)
| Fact | Source |
| --- | --- |
| Server is the source of truth; clients predict, roll back and resimulate. Enable `Workspace.AuthorityMode = Server`: it also sets NextGenerationReplication, PlayerScriptsUseInputActionSystem, SignalBehavior Deferred, UseFixedSimulation and StreamingEnabled | SA/index.md:33-40; DF 4727993 (welblander, 2026-07-09) |
| Core logic in `RunService:BindToSimulation` callbacks in a ModuleScript required on both sides; use `time()` (not `tick`, `os.time`, `os.clock`); write attributes only inside the callback (mismatch → full rollback); `task.defer` not `task.spawn` restrictions | SA/index.md:141-224 |
| Simulation input through `InputAction` (InputContext under a Player), not `UserInputService`; still sanity-check inputs | SA/index.md:228-256 |
| Limits: 64 replicated attributes per instance (name and string value ≤ 50 chars); 8 playing tracks per Animator (post) | SA/index.md:210-216; DF 4727993 |
| RemoteEvents are not on the shared timeline (≈ 40-50 ms off, staff reply). Purchases, rewards, trades and inventory still need normal remote validation | DF 4727993; SA/index.md:260 |
| Suits fast competitive movement and combat (racing, sports, FPS, fighting); templates: Racing, Soccer, Laser Tag. Costs more server CPU; camera via `Player:GetCameraState()` | SA/index.md:272-289; DF 4727993 |
| Debug view Ctrl+Shift+F6 (prediction success, input drops, server FPS) | SA/techniques.md:399-441 |
| Note: `scripting/security/network-ownership.md:46` still calls it beta (stale) | - |

## Secrets and external calls
| Fact | Source |
| --- | --- |
| Secrets store: ≤ 500 per game, ≤ 1,024 chars; owner only; domain allow-list (avoid `*`); works on live servers and collaborative tests; local tests use Local Secrets in Experience Settings; secrets only in URL or headers via `Secret:AddPrefix/AddSuffix` | cloud-services/secrets.md:17-71; Y/HttpService.yaml:228-241 |
| HttpService: 500 external requests/min plus 2,500 Open Cloud requests/min per server; over the limit calls stall ~30 s. Authenticate calls to your own backend with a shared secret | Y/HttpService.yaml:590-594; cloud-services/http-service.md:219-277 |
| API keys: one per app, minimum scopes, restricted to the game, never in code or version control; keys used inside places must not use IP restriction; unused keys expire after 60 days; keys inherit their owner's permissions (use a dedicated low-permission account for group automation) | cloud/auth/api-keys.md:26-128 |
| Keep `ServerScriptService.LoadStringEnabled` false | Y/ServerScriptService.yaml:19-49 |

## Moderation and untrusted code
| Fact | Source |
| --- | --- |
| `Players:BanAsync`: server only, ≤ 50 UserIds, duration seconds or -1; alt accounts banned by default (`ExcludeAltAccounts`); `ApplyDeviceBlock` 24 h; universe-wide by default; can fail (pcall); no effect from Studio | Y/Players.yaml:355-483 |
| `Player:IsVerified(level)`: server only, false in Studio; default Low; staff suggest Low for trading, High for ranked | Y/Player.yaml:2041-2058; DF 4820514 (eigenv3ctor, 2026-08-19) |
| Script capabilities sandbox untrusted containers (`Workspace.SandboxedInstanceMode`, `Instance.Sandboxed`, `Instance.Capabilities`); Creator Store scripts are auto-sandboxed since 2026-05-13 (Model and Folder auto-sandboxing later paused); inspect inserted scripts for obfuscation | scripting/capabilities.md; SEC/third-party-vulnerabilities.md:23-35; DF 4634642 (Kairomatic, 2026-05-13) |
| Planned, not available: Android hardware attestation, Safety Callback API, suspicious activity alerts (late 2026) | DF 4880208 (roadmap, 2026-09-18) |
