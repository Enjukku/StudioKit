> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Facts extracted by a researcher agent (claude-sonnet-5-5, medium) from the docs mirror (upstream 7400643) and Roblox staff posts; spot-checked by the orchestrator. Paths relative to `knowledge/external/roblox-creator-docs/`. EL = `cloud-services/data-stores/error-codes-and-limits.md`, VLC = `.../versioning-listing-and-caching.md`, BP = `.../best-practices.md`, PDP = `.../player-data-purchasing.md`, IDX = `.../index.md`, Y = `_api-reference/classes/`.

# Data store engine facts

## Limits (read the page on the day for numbers marked *)
| Fact | Source |
| --- | --- |
| Store name, key, scope: 50 chars each | EL:43-54 |
| Value: 4,194,304 chars of serialized JSON per key | EL:55-56 |
| Metadata: key 50, value 250, total 300 chars; UserIds list length is dynamic (error 512) | EL:72-90,746-748 |
| Per key, all servers, rolling 60 s: read 25 MB, write 4 MB; each request rounds up to 1 KB; UpdateAsync counts as both | EL:96-127 |
| No documented same-key "6 second" cooldown any more; the symptom of hammering a key is `KeyThrottled` | EL:123,957 |
| `GetAsync` caches 4 s per store instance; a cache hit costs no budget; `UseCache = false` forces a read | VLC:228-234; Y/GlobalDataStore.yaml:106-111 |
| *Game budget per minute, shared by game servers **and** Open Cloud (since 2026-07-29): standard read 300 + 40×CCU, write 300 + 20×CCU, list 300 + 2×CCU, remove 300 + 40×CCU | EL:152-228; DF 4739240 (LeafGreen888, 2026-07-15) |
| *Per-server defaults: standard read/write/remove 60 + 40×players; list 5 + 2×players. Read the live value with `DataStoreService:GetRequestBudgetForRequestType(Enum.DataStoreRequestType.StandardWrite)` | EL:470-554; Y/DataStoreService.yaml:130-157 |
| Request queues hold 30 each (Set, Get, ordered Set, ordered Get); overflow drops the request (codes 301-306) | EL:15-24 |
| *Storage: latest versions only, compressed: 500 MB + 1 MB × lifetime users. Do not pre-compress | EL:131-139 |
| Ordered stores: integer values, pages ≤ 100, no versions or metadata, writes overwrite history. `BatchGetAsync` ≤ 100 keys, ordered only | EL:622-634; IDX:210-212,365-371 |
| Serialization: JSON; UTF-8 strings only; no NaN/inf; Vector3, CFrame, Instances, functions fail or become nil; numeric-key tables can turn into string keys | VLC:269-292 |
| Studio uses the **same** data stores as the live game when API access is on; memory stores are separate | IDX:20-29; memory-stores/index.md:385 |

## Semantics
| Call | Behaviour | Source |
| --- | --- | --- |
| `GetAsync` | value + `DataStoreKeyInfo` (Version, times, UserIds, Metadata); missing key → nil | IDX:242-248 |
| `SetAsync` | blind overwrite; two servers can lose each other's data | IDX:142-145 |
| `UpdateAsync` | reads latest, runs your callback, writes; if another server wrote in between, the callback **runs again**. Callback must not yield; returns (value, userIds, metadata); returning nil cancels. Omitting userIds or metadata **clears** them: pass `keyInfo:GetUserIds()` and `keyInfo:GetMetadata()` through | IDX:116-151,295-297; Y/GlobalDataStore.yaml:385-435 |
| `IncrementAsync` | integers only | Y/GlobalDataStore.yaml:146-199 |
| `RemoveAsync` | tombstone; old versions readable for 30 days | Y/GlobalDataStore.yaml:245-268; VLC:47-53 |
| Versions | first write in each UTC hour makes a version; overwritten versions kept 30 days. Restore: `ListVersionsAsync` → `GetVersionAsync` → write back with old metadata | VLC:15-17,59-92 |
| Snapshots | Open Cloud snapshot (once a day): take one before publishing an update that changes save logic | VLC:96-98 |
| Scopes | new games use key prefixes, not scopes | VLC:127-129 |
| `OnUpdate` | deprecated; use MessagingService | Y/GlobalDataStore.yaml:234-239 |

## Errors
- Wrap every call in `pcall`. Retry with exponential backoff, jitter and a cap; retries for one key run **in order** (an old retry can overwrite newer data). BP:56-58; PDP:71-105.
- Do not retry: 101-107 (bad input), 401/402 (shutting down), 511-513 (metadata/UserIds size), 403 (Studio access off: a setting). Retry later: 301-306 (queue full), 502, `InternalServerError` (documented "retry with exponential backoff"), throttles. EL:566-1012 (only InternalServerError's retry advice is explicit; the rest is our reading).
- A failed write may still have happened: re-read with `UseCache = false` before you retry a grant or refund. EL:564; VLC:242-264.

## Shutdown
`game:BindToClose` callbacks run in parallel; the server stops after **30 s** regardless (Y/DataModel.yaml:556-568). Save all players in parallel, skip stale queued requests (PDP:351-354). How many saves fit is not documented: each save is one UpdateAsync (read + write budget), so check `GetRequestBudgetForRequestType` in tests with a full server.

## Session locking
No engine lock exists. Roblox documents a pattern (PDP:143-203, "reference only, not proven in a popular game"): the first `UpdateAsync` writes a LockId into the key's metadata; every later write is an `UpdateAsync` that aborts if another unexpired lock is present or our lock is gone; the final save removes it; the autosave refreshes it. Roadmap "player-data management (transactions, session locking, schemas)" for early 2027 is unconfirmed on an official page: build our own until it ships.
MemoryStore can hold a lease (hash map `UpdateAsync` with expiry; values ≤ 32 KB) but is ephemeral and "not for persistent player records" (memory-stores/best-practices.md:19). MessagingService is best effort (1-2 s, 1 KB): never rely on it for lock correctness (Y/MessagingService.yaml:11-85).

## Batching
Transparent batching covers MarketplaceService and avatar APIs only, **no DataStore call** (scripting/transparent-batching.md:75-102). For data stores the batching tools are: one key per player, an in-memory copy, coarse writes, and `BatchGetAsync` for ordered stores.

## Tools for the owner
Creator Hub → Monitoring → Data Stores (requests by API and status, quota usage, storage, 30 days); alerts on data store metrics (≤ 20 per game, 100+ DAU); Data Stores Manager (browse, compare, revert, delete with 30-day undo). observability.md:22-47; production/analytics/alerts.md; data-stores-manager.md:11-76.
