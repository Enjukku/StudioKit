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
6. **Review** with §6; anything client-callable that touches money, saves or other players gets the reviewer.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| N-01 | **One transport module** (the game's remote layer) registers every client-callable method in one list. No remotes created ad hoc in feature code. The wrapper moves bytes; the handler authorises. Remotes need no protocol version (each server sends its own client code); saved data and cross-server messages do | `AGENTS.md` §2; RE:13-17 |
| N-02 | **Validation order, every handler:** (1) player is ready and alive, (2) types and shape: `typeof`, string length and table size caps, `math.isfinite` on every number, integers where expected, Instance args checked with `typeof` and `IsDescendantOf` a known folder, (3) rate limit (server token bucket per player and method), (4) ownership and permission, (5) range and line of sight against server positions with latency slack, (6) game state (equipped, off cooldown, phase), (7) idempotency for anything that grants. Only then act. Cheap checks run before expensive ones (spatial queries, saves). If the handler yields, re-check afterwards that the player and character are still the same ones (a session or generation token) | SEC/client-server-boundary.md:17-303 |
| N-03 | **Server computes outcomes.** Hits, damage, drops, rolls, prices and rewards are decided on the server from server state. The client may suggest a target point; the server checks it | SEC/client-server-boundary.md:141-153; SEC/defensive-design.md |
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
