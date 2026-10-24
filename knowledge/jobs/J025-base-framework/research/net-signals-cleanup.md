---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# J025 research: transport, signals, promises/async, cleanup

All "seen" dates were checked on **2026-10-24**. Labels: **[doc]** documented fact, **[src]** read in installed source, **[vendor]** the library author's own claim or benchmark, **[inf]** my inference, **[nv]** not verified. Paths under `knowledge/external/roblox-creator-docs/` are shortened to `mirror/`. `GWS` = `C:\Users\Firew\Downloads\uterd\GreatWallSim`.

Method limits: no shell, so the context packet was not run (briefer's job). GitHub's API began returning 403 (rate limit) after about 20 calls, so some repos lack a push date. Wally's site would not render, so Wally release dates are **[nv]**; version numbers come from `wally.toml` files.

## 0. Engine facts first (the platform may already do the job)

| Fact | Source |
| --- | --- |
| RemoteEvent reliable and ordered; UnreliableRemoteEvent may drop or reorder; ~500 requests/s per client, shared per remote type; RemoteEvent delays the excess, Unreliable drops it **[doc]** | `mirror/scripting/events/remote.md:378,403-411`; `mirror/_api-reference/classes/UnreliableRemoteEvent.yaml:42-57` |
| Unreliable payload over 1,000 bytes is dropped; buffers are compressed on the wire, so the size is hard to predict **[doc]** | `UnreliableRemoteEvent.yaml:55-63` |
| A buffer sent through a remote arrives as a copy; `buffer` is meant for custom binary serialization; max 1 GiB **[doc]** | `mirror/_api-reference/libraries/buffer.yaml:15-24,43` |
| Remotes are not on Server Authority's shared timeline; remotes may arrive out of order with property/attribute updates **[doc]** | `mirror/projects/server-authority/index.md:260-263` |
| Server Authority (live, opt-in, 2026-07-09) moves movement and combat off remotes (InputAction, BindToSimulation). It does **not** replace remotes for purchases, rewards, trades **[doc]** | `knowledge/reference/roblox/whats-new.md:92`; skill N-09 |
| No 2026 change to RemoteEvent / UnreliableRemoteEvent found in the studio's tracker **[doc]** | `whats-new.md:94` |
| Network Simulator (latency, jitter, loss) full release 2026-10-16: lets us test unreliable streams under loss without a package **[doc]** | `whats-new.md:76` |
| Unconfirmed lead: DevForum remote-events-bug tag lists a thread "Recent roblox update changed how replicated events fire data over network?" dated 2026-05-20; I could not open it **[nv]** | devforum.roblox.com/tag/remote-events-bug |

**2025-2026 engine feature that makes a package unnecessary:** none for transport or signals. Server Authority removes the need for a fast-movement remote stream only in games that opt in. The `task` library (`task.spawn/defer/delay/cancel`, `mirror/_api-reference/libraries/task.yaml:56,232`) plus `coroutine.close` already gives cancellation, which removes the main reason to want Promise.

## 1. Networking transport

### 1a. Status table (adopt test, `rules/packages.md` items 2-3)

| Candidate | Owner | Latest release / commit seen | Licence | Stars / open issues | 12-month test |
| --- | --- | --- | --- | --- | --- |
| **Blink** (IDL compiler, written in Luau) | 1Axen | v0.18.9 published 2026-09-19; last push 2026-09-23 (api.github.com/repos/1Axen/blink) | MIT | 193 / 20 | pass |
| **Zap** (IDL compiler) | red-blox; 0.6.x branch maintained by @sasial-dev; README says a rewrite is in progress on a separate branch | v0.6.29 published 2026-06-23; last push 2026-06-23 | MIT | 190 / 9 | pass (4 months) |
| **Warp** (library, optional schema) | imezx | 1.1.0-pre8 published 2026-10-09 (pre-release tag); 171 commits | MIT | 35 / 0 | pass, but pre-release |
| **ByteNet** (library) | ffrostfall | last push 2025-08-01; newest tag seen v0.4.3 (date **[nv]**); no GitHub release | MIT | 183 / 19 | **fail** (14.8 months) |
| **Packet** (library) | Suphi | v1.7, DevForum post dated 2025-03-26 (devforum.roblox.com/t/3573907); newer **[nv]**; licence **[nv]** | **[nv]** | **[nv]** | **fail** if nothing newer (19 months) |
| **Red** (library) | red-blox | repo **archived by owner 2025-12-23**, read-only | MIT | 56 / 2 | **fail** |
| **leifstout/Networker** (installed, 0.3.1) | leifstout | last push 2026-01-23; created 2025-04-12; GitHub has no tags or releases (API returned empty) | MIT | 72 / 5 | pass (9 months), pre-1.0 |
| **Plain remotes + our typed wrapper**; reference design `sleitnick/typed-remote` in RbxUtil | Roblox engine; Sleitnick | RbxUtil last push 2026-08-11; no GitHub releases | MIT | RbxUtil 470 / 48 | n/a (engine); TypedRemote pass |

### 1b. Capability table

| Candidate | Strict types | Buffer serialization | Unreliable events | Server-side validation | Code-gen step and tooling cost | Tests / known users |
| --- | --- | --- | --- | --- | --- | --- |
| Blink | typed generated code claimed; strict header **[nv]** | yes (all events) | **[nv]** this session (docs pages 404) | yes: "client data is validated before it reaches critical game code" **[vendor]**; range types such as `f64(A...B)`, `vector(0..1)`; v0.18.9 (2026-09-19) fixed "NaN scalars and vectors bypassing inexact range validation" **[doc: release body]** | `.blink` file, then CLI (binary per OS) or Studio plugin writes server and client Luau. Cost: one extra tool in Rokit/the gate and "generated file is current" check. Binaries for Linux, macOS, Windows **[vendor, DF 2959671]** | tests **[nv]**; users **[nv]** |
| Zap | `types_output` option; TypeScript output; strict header **[nv]** | yes ("no overhead") | **yes**, `type: Unreliable`, 1000-byte cap noted in docs | yes: "validates all received data" **[vendor]**; ranges `u8(..100)`; non-optional Instance that resolves to nil drops the packet; NaN rule for floats **not stated** in the page I read **[nv]** | `.zap` file, Rust CLI via `aftman add red-blox/zap` or GitHub download. Reliable events are sent once per Heartbeat (so up to one frame of added delay) unless `manual_event_loop` **[doc: zap 0.6.x options page]** | tests **[nv]**; users **[nv]** |
| Warp | "strictly typed" **[vendor]** | yes, schema optional; default is dynamic | not stated **[nv]** | not documented **[nv]** | none (runtime library) | **[nv]** |
| ByteNet | "strictly typed" **[vendor]** | yes | not stated | automatic type validation **[vendor]** | none | **[nv]** |
| Packet | typed constructors, strict autocomplete **[vendor]** | yes (also 16/24-bit floats) | via a manual wrapper, not built in | built-in per-heartbeat data cap and a 60 events/s client limit (v1.3) **[vendor]**; replies reported a bypass of an 8,000-byte cap and out-of-bounds reads, fix status **[nv]** | none | author says v1.7 fixed a vulnerability |
| Red | **[nv]** | packs events | **[nv]** | **[nv]** | none | archived |
| Networker 0.3.1 | `--!strict` in server/client files; args are `...any` **[src]** | **no** | **no** | **none**: it dispatches `access.method(access.module, player, ...)` for any whitelisted name **[src: NetworkerServer.luau:97-105]** | none | none in package; GWS uses it in 24 files (138 hits) **[src grep]** |
| Plain remotes + typed wrapper | generics carry argument types (TypedRemote `Event<T...>`); **no** runtime validation **[doc: sleitnick.github.io/RbxUtil/api/TypedRemote]** | no (engine encoding) | yes (`unreliableEvent`) | whatever we write (skill N-02) | none | engine-tested |

### 1c. Benchmarks (with source)

| Source | What | Result |
| --- | --- | --- |
| Blink repo `benchmark/Benchmarks.md`, updated 2025-04-30, **[vendor: Blink's author]**; blink 0.17.1, zap 0.6.20, bytenet 0.4.3; Ryzen 9 7900X; 1000 events/frame for 10 s, same data | "Entities" FPS (median) | Roblox 16, Blink 42, Zap 39, ByteNet 32 |
| same | "Booleans" FPS | Roblox 21, Blink 97, Zap 52, ByteNet 35 |
| same | Bandwidth, Entities and Booleans | all three libraries ≈ 42 kbps and ≈ 8 kbps; default Roblox encoding reported ~559,000 and ~353,000 kbps. The Blink thread admits its kbps scaling (`Kbps*(60/FPS)`) "isn't as accurate" as hoped (DF 2959671) |
| Blink DevForum title claims **[vendor]** | speed, bandwidth | "1.6-3.7x faster" and "1000x less bandwidth" than default |
| QuickNet post (DF 4624342), **competitor's own table** | Entities / Strings FPS | ByteNet 14.66 / 0.21; Blink 23.39 / 22.20; default remote 10.82 on Strings |

[inf] Buffer libraries are close to each other on bandwidth (all within a few percent); the gap that matters is CPU, where Blink led in its author's run, and by data type (ByteNet strings were slow in the competitor's run). No neutral third-party benchmark exists. Run our own on our payloads before locking in (see the proof step below). Warp has no numbers **[nv]**.

### 1d. Source finding: what the current transport (Networker 0.3.1) does not do **[src]**
- No argument checks, no rate limit, no per-method type information; handlers get `...any` (`NetworkerServer.luau:97-105`). All of N-02 is hand-written per service; GWS wrote its own `src/server/Lib/RateLimit.luau` (token bucket `allowance`, cooldown) for this.
- Creates one RemoteEvent and one RemoteFunction per service (`NetworkerServer.luau:61-65`); no unreliable channel; no buffers.
- A client-chosen method name that is not whitelisted triggers `warn(...)` on the server (`:98-101`): a client can flood the server log [inf].
- `NetworkerClient.new` yields forever if the server never created the channel (the game's own comment, `GWS/src/server/Net/Networkers.luau:15-18`).
- Client-side `module[method]` is asserted to exist (`NetworkerClient.luau:75`): a server push for a missing method errors on the client.

### 1e. Ranking and reasons

| Rank | Pick | Reasons | Weakest part |
| --- | --- | --- | --- |
| **1** | **Blink**, behind one `Net` module of ours | Newest release of the IDL group (2026-09-19); one schema file is the single source of truth for both sides; generated typed code and receive-side validation remove shape and type bugs agents make by hand; best CPU result in the only benchmark with all three IDLs (vendor) [inf]; MIT, readable output, replaceable (our handlers are plain functions of typed arguments) | Validation bugs do exist and get fixed late (NaN bypass fixed 2026-09-19): treat the generated layer as a first filter, not the whole of N-02. Single main maintainer. Tool step must be in the gate. Unreliable support in Blink not confirmed by me |
| **2** | **Zap** | Same model, so switching between Blink and Zap touches the schema file and one adapter; unreliable events confirmed in docs; 9 open issues; typed output option | 0.6.x is the "keep alive" branch while a rewrite is planned [doc: README]; last release is 4 months old; reliable events wait up to one Heartbeat |
| **3** | **Plain RemoteEvents + our own typed wrapper** (TypedRemote-style generics, plus the N-02 validators and the `RateLimit` module already written in GWS) | No tool, no dependency, engine-tested; fits a prototype or a game that sends little; also the fallback if Blink/Zap stall | We write and test all validation; every argument is Roblox's generic encoding (more bandwidth); drift between the types we declare and what we validate is possible |
| not recommended | Networker (keep in old games until migrated), Warp (pre-release, validation undocumented), ByteNet (14.8 months stale, 19 open issues), Packet (stale in my sources, reported bypasses), Red (archived) | Fail an adopt-test line each | Networker: no validation or rate limit, `any` arguments |

**Answers for the brief**
- **Best mix of speed, safety, simplicity for agents:** Blink (or Zap) for typed, validated, low-bandwidth traffic; the studio-owned handler layer for everything the IDL cannot know: rate, ownership, range against server state, game state, idempotency (N-02 steps 3-7) [inf].
- **Does an IDL help agents more than a runtime library?** [inf] Yes for shape bugs: the schema is one reviewable file, both sides are generated from it (no client/server drift), wrong types fail at compile time or at the receive check before game code runs. A runtime library without a schema leaves the types in each agent's head. Costs: the compile step can go stale (add a "generated files current" gate check); the generator can have validation bugs (the 2026-09-19 NaN fix); schema changes need the tool. It does not replace rate limits or ownership checks.
- **Proof step recommended before build [inf]:** a 1-day spike with Blink and Zap on three real payloads (a state delta, a string, an Instance reference), a NaN/inf/oversize test per N-15, and a 1000/s spam test; confirm Unreliable in Blink and that the generated output passes `--!strict`.

## 2. Signals

### 2a. Table

| Candidate | Owner | Latest seen | Licence | `--!strict`, generics | Speed (source) | Yield safety | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **sleitnick/signal 2.0.3** (installed in all games) | Stephen Leitnick (RbxUtil, last push 2026-08-11; module commit date **[nv]**) | wally.toml 2.0.3; no GitHub releases | MIT | exports `Signal<T...>` generics and `Connection` types; **file has no `--!strict` line** (opens with a comment block) **[src: init.luau:1-34]** | GoodSignal-derived; "direct copy of GoodSignal with added methods" **[src:129]**. GoodSignal numbers: Fire 0.8 µs, ConnectAndDisconnect 0.3 µs, FireManyHandlers 4.4 µs vs BindableEvent wrapper 3.2 / 1.8 / 6.0 µs **[DF 1387063, 2021-08-02, updated 2022-06-19]** | yes: reusable runner coroutines, handlers may yield; `Wait` threads are cancelled on `DisconnectAll` **[src:44-60,300-308]** | `Once`, `FireDeferred`, `Wrap`, `Is`, `Destroy`. Handlers run **newest connection first** (head insertion, `:221-226`, `:328-337`) [inf]; `Disconnect` walks the list, O(n) (`:91-100`) |
| GoodSignal | stravant | origin of the code above; standalone repo status **[nv]** | MIT (header) | not typed in the original | same numbers as above | yes | The community baseline; sleitnick's file is its maintained fork |
| LemonSignal | Data-Oriented-House | 53 commits; stars 51; dates **[nv]** (API 403) | MIT | **[nv]** | "faster than most other implementations" with no numbers [vendor] | **[nv]** | Same org archived Red on 2025-12-23: maintenance risk **[inf]** |
| Signal+ | Alexx (DevForum) | v2.5.0, 2025-03-23 (DF 3552231) | **[nv]** | typed generics added in v2.4.0 | author claims 3x BindableEvent with no benchmark; testers: "about the same speed" as GoodSignal, slightly less memory; one tester saw no difference vs SimpleSignal | **[nv]** | Author says internals are not meant to be read (number-keyed): fails "we can read its source" in spirit; no 2026 update seen |
| FastSignal | RBLXUtils | 2021 post | **[nv]** | **[nv]** | 0.2 µs Fire; the 2021 author says it gives up correctness (yielding handlers, connecting during a fire) | **no** | Not suitable |
| BindableEvent (engine) | Roblox | engine | n/a | n/a | slowest in the DF 1387063 table (CreateAndFire 18.5 µs); copies arguments; "almost no reason to use RobloxSignal now that task.spawn exists" (the post's author) | n/a | Use only to cross script boundaries that need engine copying |

### 2b. Ranking

| Rank | Pick | Reasons | Weakest part |
| --- | --- | --- | --- |
| **1** | **Keep sleitnick/signal** (one package, already in every game, pass on all six adopt lines) | Correct and fast baseline; yield-safe; typed generics; same author and repo as Trove (one upstream for two layers); migration cost zero | No `--!strict` line, so strict callers see typed exports but the module itself is not checked; LIFO fire order surprises agents who expect connection order; O(n) disconnect; no 2026 module-level release proof |
| 2 | LemonSignal | Possibly faster | No numbers, no dates I could read, org archived a sibling package; do not switch without our own benchmark |
| not recommended | Signal+, FastSignal, BindableEvent | See table | |

[inf] A signal library is warranted (a game's own module events cross many files); do **not** write our own (one-user rule would be met only after a measured problem). Add one rule to the framework: never rely on handler order.

## 3. Promises and async

### 3a. Table

| Candidate | Owner | Latest seen | Licence | Strict, generics | Speed | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| **evaera/roblox-lua-promise** (v4.0.0; installed transitively at `GWS/Packages/_Index/evaera_promise@4.0.0`) | evaera | v4.0.0 published **2022-03-03**; last push **2024-08-06** | MIT | no `--!strict` assurance; the typed fork `howmanysmall/typed-promise@4.0.3` exists | **[nv]** | 351 stars / 13 open issues. **Fails the 12-month test** (26 months since the last commit). Only the games' Janitor dependency pulls it in; **GWS `src` has 0 references to Promise, Trove or Maid** (grep, 2026-10-24) |
| **howmanysmall/typed-promise 4.0.3** | howmanysmall | Wally dependency of Janitor 1.18.3 `[src: janitor wally.toml:12-13]`; dates **[nv]** | **[nv]** | typed (`TypedPromise<T...>` used by Janitor) | **[nv]** | Fork; one more owner to trust |
| **Concur** (RbxUtil module) | Sleitnick | in RbxUtil `modules/concur` (push 2026-08-11) | MIT | **[nv]** | **[nv]** | API: `spawn/defer/delay/value/event/all/first`, `Await` with timeout, `OnCompleted`, `Stop`; status and stability not stated on its page. Not a Promise: no chaining |
| **Future** (Zap `yield_type = "future"` needs an `async_lib`) | n/a | no maintained standalone package found **[nv]** | **[nv]** | **[nv]** | **[nv]** | Do not adopt |
| **Plain `task` + `pcall` + our patterns** | Roblox | engine; Luau 0.734-0.743 (2026-08-14..10-16) has faster `pcall`/`xpcall` **[doc: whats-new.md:67]** | n/a | native | native | `task.spawn/defer/delay/cancel`, `coroutine.close` |

### 3b. Ranking

| Rank | Pick | Reasons | Weakest part |
| --- | --- | --- | --- |
| **1** | **No promise library. `task` + `pcall` + a few written patterns** | Zero uses in the newest game [src grep]; Promise's maintained state fails our adopt test; cancellation exists natively; the places that *really* fail (DataStore, Marketplace, Teleport, HTTP) need `pcall` and retry anyway (`rules/anti-overengineering.md` §9) and read better as a flat loop; fewer concepts for every agent | Combinators (race, all, timeout) must be written by us; a single-use helper must wait for a second user (rule 5). Error propagation is manual: an unprotected `task.spawn` loses the caller's traceback |
| 2 | **Concur** (RbxUtil), only when `all`/`first` with timeouts is needed in 2+ places | Same upstream as Signal and Trove | Status unstated; not verified tested |
| not recommended | roblox-lua-promise, typed-promise | Stale (26 months); extra owner | Removing it means swapping or patching Janitor (see 4) |

**Answer:** [inf] No, we do not need a promise library; `task` and our patterns suffice. A write-our-own `Async` helper (retry-with-backoff, timeout wrapper, ≈ 40 lines) is justified only for the data layer's retries (a real boundary), and belongs to the data package, not this layer.

## 4. Cleanup

### 4a. Table

| Candidate | Owner | Latest seen | Licence | Strict, generics | Notable behaviour | Weaknesses |
| --- | --- | --- | --- | --- | --- | --- |
| **howmanysmall/janitor 1.18.3** (installed) | howmanysmall (+ Validark and others) | repo push 2026-07-28; GitHub releases stop at v1.17.0 (2024-08-12) though Wally ships 1.18.3 **[nv: Wally date]**; 151 stars / 6 issues | MIT | `--!strict` and `--!optimize 2`; `Add<T>` returns T **[src: init.luau:1-2,262]** | keyed objects (`Add(obj, method, key)` replaces the old one), `LinkToInstance(s)`, `Get`, `Remove`, `RemoveList`, `AddPromise`, re-entrancy guard (`CurrentlyCleaning`) **[src:193-262,824-896]** | Cleanup walks the table with `next`, so **order is undefined** (`:833,883`); no `pcall` per item, so one erroring cleanup aborts the rest (`:837,864`) [inf]; **hard dependency on typed-promise 4.0.3** and `require`s it at load (`:13`; wally.toml:12-13) |
| **sleitnick/trove 1.8.0** | Stephen Leitnick | wally.toml 1.8.0; RbxUtil push 2026-08-11 | MIT | `--!strict` (first line, raw source); `Add` returns the object | `Add`, `Clone`, `Connect`, `Once`, `BindToRenderStep`, `Extend`, `AttachToInstance`, `WrapClean`, `Pop`, `Remove`; `AddPromise` only with roblox-lua-promise v4 **[doc: sleitnick.github.io/RbxUtil/api/Trove]** | Docs: "ordering of the objects removed is not guaranteed" (source cleans in insertion order but removal swaps in the last item); no `pcall` per item (threads only) |
| **Maid** (Quenty, `@quenty/maid`) | Quenty (NevermoreEngine monorepo) | dates **[nv]** (API 403) | **[nv]** | strictness **[nv]** | handles deferred events, re-entrancy, tasks and promises [doc: repo README] | Distributed through npm; no Wally package confirmed **[nv]**, so fails "replaceable and installable" until shown |
| Plain `Destroy` + manual `Disconnect` lists | Roblox | engine | n/a | n/a | zero dependency | The failure class this layer exists to prevent (leaked connections) |

### 4b. Ranking

| Rank | Pick | Reasons | Weakest part |
| --- | --- | --- | --- |
| **1** | **Keep Janitor** | In every game since May 2026 (`old-framework.md`), so zero migration; strict and typed; keyed replace and `LinkToInstance` fit state-driven UI and per-player lifetimes; guards re-entrant cleanup | The mandatory Promise dependency (unused in code but loaded) and undefined cleanup order. Document: "never depend on cleanup order; never put code that can throw in a cleanup" |
| 2 | **Trove** | No dependencies; same upstream as Signal; `Connect`, `Clone`, `Extend` helpers prevent the common "forgot to track it" slip; easy to pick up | Another package to learn; docs say cleanup order not guaranteed; no keyed replace [nv: confirmed from the method list only] |
| not recommended | Maid, plain tables | See table | |

[inf] A switch from Janitor to Trove would be justified only when a new game has no legacy code and we want to drop typed-promise from the lock file. If the owner wants one cleanup class that matches Signal's upstream, pick Trove for new games and leave old games on Janitor; two cleanup packages in one game is forbidden by `rules/packages.md` ("one package per concern").

## 5. Summary picks (for the lead)

| Layer | Pick | Alternative | Single biggest risk |
| --- | --- | --- | --- |
| Transport | Blink behind a `Net` adapter | Zap; then plain remotes with our typed wrapper | Validation bugs in the generator; tool step stale |
| Signals | Keep sleitnick/signal | LemonSignal (only after our own benchmark) | Module is not `--!strict`; LIFO order |
| Promises/async | None: `task` + `pcall` + patterns | Concur for `all/first` | Hand-written combinators |
| Cleanup | Keep Janitor | Trove | Transitive Promise; undefined order |

## 6. Uncertain and next action

- **[nv]** Blink's Unreliable support and strict-mode output; Zap's NaN handling for float ranges; Packet's current version and licence; ByteNet, LemonSignal, Maid push dates; every Wally publish date; package tests and known users.
- No neutral benchmark exists for transport; only vendor data (Blink repo 2025-04-30) and a competitor's table.
- **Recommended next action:** the lead asks for a short probe job (Studio and the gate, not research): compile one schema in Blink and Zap, run NaN/inf/oversize/spam tests and a 3-payload bandwidth/CPU test, then lock rank 1. Until then keep Networker in the old games and do not start a second transport in any of them.

## Sources (all fetched 2026-10-24)
- Installed source: `GWS/Packages/_Index/leifstout_networker@0.3.1/networker/src/*.luau`; `sleitnick_signal@2.0.3/signal/init.luau`; `howmanysmall_janitor@1.18.3/janitor/src/init.luau` and `wally.toml`; `GWS/src/server/Lib/RateLimit.luau`; `GWS/src/server/Net/Networkers.luau`.
- Mirror: `mirror/scripting/events/remote.md`; `mirror/_api-reference/classes/{RemoteEvent,UnreliableRemoteEvent}.yaml`; `mirror/_api-reference/libraries/{buffer,task}.yaml`; `mirror/projects/server-authority/index.md`; `knowledge/reference/roblox/whats-new.md`; skill `networking-security/references/facts.md`.
- GitHub API and pages: 1Axen/blink (+ releases/latest, benchmark/Benchmarks.md), red-blox/zap (+ releases/latest, 0.6.x docs options/events/types/install), red-blox/Red, ffrostfall/ByteNet (+ tags), imezx/Warp (+ releases/latest), leifstout/Networker, Sleitnick/RbxUtil, howmanysmall/Janitor, evaera/roblox-lua-promise, Data-Oriented-House/LemonSignal, Quenty/NevermoreEngine, raw `modules/trove/{wally.toml,init.luau}`, `modules/signal/wally.toml`.
- DevForum: Blink thread 2959671; Packet 3573907; Signal+ 3552231; GoodSignal comparison 1387063; QuickNet 4624342. Docs: sleitnick.github.io/RbxUtil/api/{TypedRemote,Concur,Trove}; zap.redblox.dev.
