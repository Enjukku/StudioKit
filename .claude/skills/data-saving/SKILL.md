---
name: data-saving
description: Design, build or review player persistence in a Roblox game - save schema and migrations, loading, session locks, write timing, purchases and receipts, shutdown, failures. Use for "save the player's progress", "add a new stat", "players lost their data", "items got duplicated", "rename this saved field", and before any change touching saved data or receipts.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 3. Evidence: `references/engine-facts.md` (docs mirror upstream 7400643, Roblox staff posts 2026); community library design (ProfileStore, MadStudioRoblox, last code commit 2025-07-31) used as rank-4 evidence only. Short source names (BP, PDP, EL, IDX, VLC, Y) are defined at the top of `references/engine-facts.md`.

# Data saving: never lose or duplicate a player's progress

## 1. When this skill starts
Any change that adds, renames, removes or reinterprets saved data, any new write path (rewards, trades, purchases, teleports), and any report of lost, rolled-back or duplicated items. The game's chosen adapter is in `knowledge/design/game-profile.md` (tech choices row).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Limits, budgets, call semantics, error codes, versions, shutdown | `references/engine-facts.md` |
| Receipts, refunds and other money rules | the `platform-policy` skill, § B |
| The game's adapter API and file paths | the game's system note or overlay |

## 3. Steps
1. **Decide what is saved.** Only what cannot be rebuilt: progress, currencies, owned items, settings, receipt ids. Not world state, caches, or values derived from other saved values. Estimate bytes per player at the end of the game's content (max inventory), and write the number in the design note.
2. **Change the schema** (§4 D-02, D-03): bump the version, write the migration as a pure function, add a test with an old save fixture.
3. **Write through the adapter only**, with the check inside the atomic update (D-05).
4. **Pick the write cadence** (D-06): in memory always; to the store on autosave, leave, shutdown and money events.
5. **Test offline** (migrations, validation, merge rules) with the gate; then in Studio against a **test** data store (D-10).
6. **Review** with §6 before merge. Changes to receipts or saved currency need the reviewer.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | **One key per player**, named with the UserId (`Player_<UserId>`), holding everything that must change together. Few, fixed store names. Pass the UserId in the write's userIds | BP:15-31; RTBF templates need `{UserId}` (`right-to-be-forgotten.md:15-31`) |
| D-02 | **Versioned schema.** The save holds `schemaVersion`. On load: run each migration step in order (v3→v4→v5), then fill new keys from the template, then validate types. Migrations are pure functions with offline tests from fixtures: new account, every old schema, missing, extra and malformed fields, duplicate item ids, huge valid balances, a half-done migration and an unknown future schema. Choose between two copies of data by a version rule, never by the newest `UpdatedTime` (a stale copy rewritten later looks newest; Tower Defense Simulator lost data this way in 2024). The agent that changes a migration does not also change its expected outputs. Never delete unknown keys silently; log them. A save with a **newer** `schemaVersion` than this server knows (an old server still running during an update) is never migrated down or written: the session becomes degraded, so old servers cannot damage new saves | ours, from BP and the reconcile pattern of common libraries |
| D-03 | **JSON-safe values only**: numbers, strings, booleans, plain tables with consistent keys. Vectors as `{x, y, z}`; no NaN or inf; enums as strings. Validate before every write | VLC:269-292 |
| D-04 | **Load = lock.** The first read takes a session lock in the same `UpdateAsync` (Roblox pattern: LockId in metadata; abort on another live lock). Until the lock is held and migration has run, the player is **not ready**: no rewards, purchases or writes. Name the session states and what each allows: loading (nothing) → ready (all) → degraded (play on, no writes, no purchases) → closing (final save only) → closed | PDP:143-203 |
| D-05 | **Writes are atomic and validated.** Every change to a saved value goes through one adapter `update(player, fn)`; affordability and validity checks live inside `fn`, so check and write cannot split. Clients never write | BP:60-64; `AGENTS.md` §2 server authority |
| D-06 | **Memory first, store rarely.** Keep the live copy on the server. Write to the store on: autosave (Roblox sample 180 s, staggered randomly per player; shorter than the lock expiry), player leave, shutdown, and immediately after money or trade events. High-frequency changes (kills, hits, coins per tick) accumulate in memory | PDP:21-25,330-349; BP:46-52 |
| D-07 | **Every store write is an `UpdateAsync`** that checks we still own the lock and passes metadata and userIds through. No `SetAsync` on player keys | IDX:147-151,295-297; PDP:164-203 |
| D-08 | **Failure is normal.** `pcall` every call; ordered retries per key with backoff and jitter; on load failure mark the session **degraded** (D-04): the player may play on defaults, but nothing from that session is ever written, and purchases are refused with a message. A failed write may have landed: re-read with `UseCache = false` before retrying a grant | PDP:33-35,285-300; EL:564 |
| D-09 | **Shutdown in 30 s.** `BindToClose` saves all players in parallel and releases locks; nothing else yields there. Test it with a full server and read the write budget. Shutdown saving reduces loss but cannot guarantee it (a crash skips it): the autosave interval is the real bound on lost progress | Y/DataModel.yaml:556-568; PDP:351-354 |
| D-10 | **Never test on live data.** Studio uses the real stores when API access is on. Use a separate test experience, or a store name prefix the game sets for Studio, or a mock store in offline tests | IDX:20-29 |
| D-11 | **Purchases and trades are transactions.** Receipts: grant + record `PurchaseId` in the same update, save, then `PurchaseGranted`. Trades between two players: each side's change is one atomic update and the trade has an id stored on both sides so a retry cannot apply twice. Rewards from rounds or quests are award requests with an id, applied once by the data layer | PDP:221-261; platform-policy § B |
| D-12 | **Budgets are shared.** Game servers and Open Cloud tools draw from one per-minute budget (2026-07-29). External tools that touch data stores must throttle themselves. In-game bulk work checks `DataStoreService:GetRequestBudgetForRequestType` first; external tools cannot call it, so they rate-limit themselves and watch the quota on the Creator Hub data stores dashboard. **External tools respect the session lock:** in the same `UpdateAsync`, read the lock metadata and refuse to write a player whose lock is live (online); deliver grants for online players through the game instead (a pending-grant entry with an id that the game applies once on load) | DF 4739240 (2026) |
| D-13 | **Global data is not player data.** Leaderboards: ordered stores (`BatchGetAsync`) or Roblox's native leaderboards; cross-server state: MemoryStore (ephemeral) or MessagingService (best effort). Never write one hot shared key from every server | EL:622-634; memory-stores/best-practices.md:19 |
| D-14 | **Recovery path exists before launch.** Versions are kept per UTC hour, not per write, for 30 days; the Data Stores Manager and `GetVersionAtTimeAsync` restore one key; a daily snapshot freezes the state before a save-logic change; the Data Stores Batch Processor repairs many keys (runs at least once per key, so jobs must be idempotent). In an incident: stop the bad writes first, then roll back code or config, then repair only the affected keys, keeping legitimate purchases and trades made since. Restoring while bad code still writes undoes nothing. Write the steps in the game's system note and rehearse them on test data | VLC:59-98; `knowledge/reference/architecture/roblox-operations-2026-10.md` §2 |
| D-15 | **Old and new servers write at the same time** after every update until old servers empty or restart. A save change that old servers cannot read safely ships only after Server Management restarts all outdated servers (or old writers are fenced); test old server + new save and new server + old save | `projects/update-games.md`; `knowledge/reference/architecture/roblox-operations-2026-10.md` §2 |

## 5. Adapters (wrappers)
A persistence package is one adapter behind the game's own data module. Before adopting or keeping one, check it against D-02, D-04, D-07, D-08, D-09 and D-11, and record the answers in `knowledge/reference/`. Roblox's guidance: vet the module's maintenance and know how to read your data without it (BP:33-42). DataStore2 is legacy. Known traits of ProfileStore (community, rank 4): lock in the profile metadata via `UpdateAsync`, autosave 300 s, takes over a lock after about 40 s of waiting and treats a holder as dead after 630 s, replaces malformed records with the template (hook `OnOverwrite`).

**Default adapter (J025):** in a game built on `roblox-game-framework`, the adapter is the framework's **Session** block over our pinned, patched ProfileStore 1.0.3. Its answers to every D-rule: §8.

## 6. Rules (final check)
- No player data written before load, lock and migration finish, or from a degraded session.
- No `SetAsync` on player keys; every write passes metadata and userIds through.
- No saved data keyed by username; no Instances, vectors or NaN in saves.
- No schema change without a version bump, a pure migration and a test from an old save.
- No Studio test against live data. No external tool without its own throttle.

## 7. Self-check before returning
- [ ] Bytes per player estimated at max content; far below 4 MB.
- [ ] Migration tested from every older version still in the wild.
- [ ] Load failure, lock held elsewhere, write failure and shutdown each have a defined behaviour and a test or Studio check.
- [ ] Purchases and trades cannot apply twice (id stored with the grant).
- [ ] The design note says what is saved, where, the cadence and the restore steps.

Project overlay: if `knowledge/overlays/data-saving.md` exists, read it after this file; it wins for this game.

## 8. Session: the default adapter (J025)
§5 applies: in a game built on `roblox-game-framework`, the adapter is the **Session** block (`roblox-game-framework/contracts/Session.md`; card and example: `engineering-craft` → `references/framework.md` §4.3). A game uses another adapter only with the deviation and its §5 answers recorded in `knowledge/design/game-profile.md`. How Session keeps each D-rule:

| Rule | What keeps it in Session | Test (contract id) |
| --- | --- | --- |
| D-01 | key `PLAYER_<UserId>`, store name from `def.store`, `AddUserId` on load (S13; existing games keep their key and store) | S-T15 |
| D-02 | `schemaVersion = def.version`; `migrations[n]` (v(n-1) → v(n), pure) run in order on a deep copy, then reconcile against the template (fills missing keys, keeps unknown keys, S8), then `def.validate`; a newer save is fenced: `degraded`, never migrated down or written (S7) | S-T3, S-T4, S-T19 |
| D-03 | every `update` result is walked: finite numbers, strings, booleans, string-key or dense-array tables, depth ≤ 16; else `invalid_data`, nothing changes (S5) | S-T10 |
| D-04 | ProfileStore's session lock; status `loading` → `ready` → `degraded` / `closing` → `closed`, mirrored as Player attribute `SessionStatus`; writes only in `ready` (S2, S3, S9); 120 s load timeout is Session's `Cancel`; a session taken by another server stops writes and kicks (S12) | S-T1, S-T2, S-T7, H-S3 |
| D-05 | one writer: `save:update(player, fn)`; `fn` gets frozen data, must not yield, checks inside it; error, yield, deny or bad data change nothing (S1, S4) | S-T5, S-T8..S-T11 |
| D-06 | memory first; ProfileStore autosave 300 s (staggered), save on leave, on shutdown and after each receipt | S-T20, H-S5 |
| D-07 | every store write is ProfileStore's `UpdateAsync` on the locked profile; Session has no `SetAsync` on player keys | S-T15, H-S2 |
| D-08 | ProfileStore retries with backoff; load failure past 120 s → `degraded` (template copy, no write, purchase or award); critical state logged, sampled | S-T2, H-S1, H-S2 |
| D-09 | ProfileStore's `BindToClose` saves and releases all profiles in parallel; `ProfileStore.IsClosing` refuses updates (`unavailable, closing`); shutdown never kicks | H-S5 |
| D-10 | in Studio the store name is `STUDIO_` .. `def.store` (S14); Studio probes use a `test_` store prefix | S-T16, S-T17 |
| D-11 | receipt: grant and `PurchaseId` in one update, `PurchaseGranted` only after a save holding the id landed (S10, cap 100); awards: `save:award(player, awardId, fn)` applies an id once while it is in the log (S11, cap 200); `Purchased` is never a grant or revenue source (CC-4) | S-T12, S-T20..S-T25 |
| D-14 | a malformed record replaced by ProfileStore fires `OnOverwrite`: Session logs store and key so a restore can start (S-T26); restore steps stay the game's | S-T26 |
| D-15 | the newer-version fence (D-02 row) keeps an old server from writing a newer save | S-T3 |
| D-12, D-13 | not Session's: external tools throttle themselves; global data uses ordered stores or MemoryStore | — |

- **ProfileStore pin:** our own copy of 1.0.3 in `vendor/ProfileStore/` (Apache-2.0), with patch **P-1** (`OnAfterSave` also passes `is_ending_session`, so a same-server rejoin waits for the real release, not a save already in flight); every patch is a row in `vendor/ProfileStore/PATCHES.md` with its test. Owner exception: `rules/packages.md` "ProfileStore exception". Package note: `knowledge/reference/libraries/profilestore.md`.
- **Studio save edits** go through `save:studioReset` / `save:studioSet` (Studio only, refused live: `denied, studio_only`), never a direct DataStore edit.
