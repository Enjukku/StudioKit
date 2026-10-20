---
name: networking-security
description: Design, build or review every client-server path in a Roblox game so exploiters cannot cheat, dupe or crash it. Covers remote design (reliable, unreliable, functions), the server validation order, rate limits, what clients can see and decompile, network ownership, Server Authority (2026) for fast combat or movement, detection and bans, secrets and API keys, and untrusted models. Use for any new remote or client request, "players are cheating", "items got duplicated", "someone flies or teleports", "is this exploitable", and before merging anything client-callable. Wrapper-neutral: any remote library is transport, not authorisation.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 5. Evidence: `references/facts.md` (docs mirror upstream 7400643; Roblox staff posts 2026). Short source names (SEC, RE, SA, Y) are defined at its top.

# Networking and security: the client can lie about everything

## 1. When this skill starts
Any new or changed client request, relay, physics interaction, reward path, trade, admin tool, external HTTP call or inserted model. Also any report of cheating, duping or a crash caused by a player.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Remote limits, data that survives the trip, validation guidance, Server Authority, secrets, bans, sandboxing | `references/facts.md` |
| Money, receipts, trading rules | `platform-policy` skill § A-B |
| Saving the result of a request | `data-saving` skill (D-05, D-11) |
| What changed this year | `knowledge/reference/roblox/whats-new.md` § Networking and security |

## 3. Steps
1. **Threat-model the feature** (SEC/security-tactics.md:48-54): for each argument the worst value; the request fired 1,000 times a second; its effect on other players; the most server work it can cause; the least state the client needs; and what each object involved *can* do, not only what we intend (a reused NPC or tool may keep abilities it should not have).
2. **Design the request as intent**, not result: `requestFire(weaponId, origin, direction)`, never `dealDamage(target, 50)` or `giveCoins(100)`. The server computes outcomes.
3. **Write the server handler in the fixed order** (§4 N-02). Fail early and silently.
4. **Place code and data** (§4 N-05): only what the client needs replicates.
5. **Choose the channel** (§4 N-06) and, for fast combat or movement games, consider Server Authority (N-09).
   - Server Authority covers movement and combat simulation only. Purchases, rewards, trades and every other remote still follow N-02.
   - Without Server Authority, check movement on the server: average speed over time with a leaky bucket, on the XZ plane, exempting real teleports (`references/facts.md`).
6. **Review** with §6; anything client-callable that touches money, saves or other players gets the reviewer.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| N-01 | **One transport module** (the game's remote layer) registers every client-callable method in one list. No remotes created ad hoc in feature code. The wrapper moves bytes; the handler authorises. Remotes need no protocol version (each server sends its own client code); saved data and cross-server messages do | `AGENTS.md` §2; RE:13-17 |
| N-02 | **Validation order, every handler:** (1) player is ready and alive, (2) types and shape: `typeof`, string length and table size caps, `math.isfinite` on every number, integers where expected, Instance args checked with `typeof` and `IsDescendantOf` a known folder, (3) rate limit (server token bucket per player and method), (4) ownership and permission, (5) range and line of sight against server positions with latency slack, (6) game state (equipped, off cooldown, phase), (7) idempotency for anything that grants, keyed by what may happen once: `(player, object id)` for per-player rewards (each player opens a chest once), `object id` for shared loot (one player claims it). Only then act. Cheap checks run before expensive ones (spatial queries, saves). If the handler yields, re-check afterwards that the player and character are still the same ones (a session or generation token) | SEC/client-server-boundary.md:17-303 |
| N-03 | **Server computes outcomes.** Hits, damage, drops, rolls, prices and rewards are decided on the server from server state. The client may suggest a target point; the server checks it. **Spending and granting go through the data layer's one atomic update** (`data-saving` D-05): the check (can afford, owns it) and the change happen together there, never as separate steps in the handler | SEC/client-server-boundary.md:141-153; SEC/defensive-design.md |
| N-04 | **Never trust built-in interaction objects alone.** ProximityPrompt and ClickDetector events reach the server from any distance: re-check distance and state in the handler | SEC/client-server-boundary.md:275-291 |
| N-05 | **Replicated means public.** Anti-cheat thresholds, server rules, admin lists, unreleased content and secrets live in ServerScriptService or ServerStorage. Never put server and client logic in one replicated module | SEC/access-control.md:15-67 |
| N-06 | **Channel choice.** RemoteEvent for state and anything that must arrive. UnreliableRemoteEvent only for small (≤ 1,000 bytes), frequent, replaceable streams with a sequence number. RemoteFunction only client → server for quick queries with a short server handler; never `InvokeClient`. ~500 requests/s per client per remote type: batch, send deltas | RE:360-407; Y/RemoteEvent.yaml:37-45 |
| N-07 | **Write for deferred signals.** Never assume a handler ran right after an event fired; order between remotes and property replication is not guaranteed | scripting/events/deferred.md; scripting/attributes.md:23 |
| N-08 | **Physics the client owns, the client controls.** Gameplay-critical moving parts: `SetNetworkOwner(nil)` or anchored; movement checks average over time and exempt real teleports | physics/network-ownership.md:17-35; SEC/network-ownership.md:49-52 |
| N-09 | **Server Authority** (`Workspace.AuthorityMode = Server`, live 2026-07-09) for fast competitive movement and combat: core logic in `BindToSimulation`, input through `InputAction`, `time()` only. It does not cover remotes: purchases, rewards and trades still follow N-02. Costs server CPU; decide per game, record in the game profile | SA/index.md; DF 4727993 |
| N-10 | **Design beats detection; detection is a ladder.** Remove the exploit by design first. Then signals feed a suspicion score, honeypot remotes catch scripted clients, consequences escalate log → quiet fix → temporary limit → ban (`BanAsync`). Never ban on client-side detection | SEC/defensive-design.md; SEC/server-side-detection.md |
| N-11 | **Secrets never in the place or the repo.** Places use the Secrets store (`HttpService:GetSecret`, secrets only in URL or headers). Tools read keys from environment variables or key files outside the repo, never print them. API keys: one per app, minimum scopes, restricted to the game | cloud-services/secrets.md; cloud/auth/api-keys.md |
| N-12 | **Untrusted code stays boxed.** Inserted models: inspect scripts (obfuscation, `require` by id, `loadstring`); keep `LoadStringEnabled` false; Creator Store scripts are sandboxed but malware has slipped through | scripting/capabilities.md; SEC/third-party-vulnerabilities.md |
| N-13 | **Places are a universe-wide door.** Any client can teleport to any place in the universe: set access to "Secure within universe only"; test and dev places live in a separate private universe | SEC/access-control.md:19-45 |
| N-14 | **Clear outcomes, quiet logs.** A request ends as done, denied (do not retry) or temporarily unavailable (may retry), and the client shows each differently. Repeated denials are counted with a few samples, never one log line each | strong-codebases A-13, A-14 (owner paper) |
| N-15 | **Test by damage, in a private test place.** Before launch, test in this order (economy games): 1 asset duplication or loss (replayed claims, overlapping trades, save failure mid-trade); 2 rewards or permissions from bad input (wrong types, NaN, wrong ancestry, forbidden actions); 3 rewards from client-owned physics contacts; 4 movement and combat advantage under latency; 5 hidden data sent to clients early; 6 innocent players caught by a detector (run detectors in log-only mode first). Combat games move 4 and 5 up. Synthetic data only; no exploit code | `knowledge/reference/architecture/roblox-operations-2026-10.md` §4 |
| N-16 | **Bans are reversible by rehearsal.** Record the detector version and evidence with every ban; rehearse an unban on test accounts first. A device block (`ApplyDeviceBlock`, Windows and macOS only, 24 h) is cleared only by `UnbanAsync` in the game, not by a website unban. Never judge a detector by its ban count | Y/Players.yaml; DF 2026-06-04/08 (eigenv3ctor) |

## 5. Rules (final check)
- No client-callable method without the N-02 checks; no generic setters (`setData`, `giveItem`).
- No client-sent results trusted: damage, hits on players, rewards, prices, roll outcomes.
- No `InvokeClient`, no `loadstring`, no asset load or `require` from remote arguments.
- No server-only logic, thresholds or secrets in replicated containers.
- Every grant idempotent; every trade validates both sides before commit.

## 6. Self-check before returning
- [ ] Threat model written (worst values, spam, other players, cost).
- [ ] Each handler shows the N-02 order; numbers checked with `math.isfinite`; rate limit present and cleared on leave.
- [ ] Placement checked: nothing sensitive replicates.
- [ ] Channel and, for combat games, the Server Authority decision recorded.
- [ ] Spam test (fire the request far beyond the limit) and bad-value test (NaN, huge strings, wrong types, far targets) planned or run.

Project overlay: if `knowledge/overlays/networking-security.md` exists, read it after this file; it wins for this game.
