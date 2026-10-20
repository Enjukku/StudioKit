---
name: data-saving
description: Design, build or review player persistence in any Roblox game - what to save, the save schema and its migrations, loading and session locks, when and how to write, purchases, shutdown, failure handling, request budgets and testing. Use for "save the player's progress", "add a new stat", "players lost their data", "items got duplicated", "rename this saved field", "is this safe to save", and before any change that touches saved data or receipts. Wrapper-neutral: any persistence package is one adapter that must pass this skill's checks.
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
| D-02 | **Versioned schema.** The save holds `schemaVersion`. On load: run each migration step in order (v3→v4→v5), then fill new keys from the template, then validate types. Migrations are pure functions with offline tests from real old saves. Never delete unknown keys silently; log them | ours, from BP and the reconcile pattern of common libraries |
| D-03 | **JSON-safe values only**: numbers, strings, booleans, plain tables with consistent keys. Vectors as `{x, y, z}`; no NaN or inf; enums as strings. Validate before every write | VLC:269-292 |
| D-04 | **Load = lock.** The first read takes a session lock in the same `UpdateAsync` (Roblox pattern: LockId in metadata; abort on another live lock). Until the lock is held and migration has run, the player is **not ready**: no rewards, purchases or writes | PDP:143-203 |
| D-05 | **Writes are atomic and validated.** Every change to a saved value goes through one adapter `update(player, fn)`; affordability and validity checks live inside `fn`, so check and write cannot split. Clients never write | BP:60-64; `AGENTS.md` §2 server authority |
| D-06 | **Memory first, store rarely.** Keep the live copy on the server. Write to the store on: autosave (Roblox sample 180 s, staggered randomly per player; shorter than the lock expiry), player leave, shutdown, and immediately after money or trade events. High-frequency changes (kills, hits, coins per tick) accumulate in memory | PDP:21-25,330-349; BP:46-52 |
| D-07 | **Every store write is an `UpdateAsync`** that checks we still own the lock and passes metadata and userIds through. No `SetAsync` on player keys | IDX:147-151,295-297; PDP:164-203 |
| D-08 | **Failure is normal.** `pcall` every call; ordered retries per key with backoff and jitter; on load failure mark the session **errored**: the player may play on defaults, but nothing from that session is ever written, and purchases are refused with a message. A failed write may have landed: re-read with `UseCache = false` before retrying a grant | PDP:33-35,285-300; EL:564 |
| D-09 | **Shutdown in 30 s.** `BindToClose` saves all players in parallel and releases locks; nothing else yields there. Test it with a full server and read the write budget | Y/DataModel.yaml:556-568; PDP:351-354 |
| D-10 | **Never test on live data.** Studio uses the real stores when API access is on. Use a separate test experience, or a store name prefix the game sets for Studio, or a mock store in offline tests | IDX:20-29 |
| D-11 | **Purchases and trades are transactions.** Receipts: grant + record `PurchaseId` in the same update, save, then `PurchaseGranted`. Trades between two players: each side's change is one atomic update and the trade has an id stored on both sides so a retry cannot apply twice | PDP:221-261; platform-policy § B |
| D-12 | **Budgets are shared.** Game servers and Open Cloud tools draw from one per-minute budget (2026-07-29). External tools that touch data stores must throttle themselves. Check `GetRequestBudgetForRequestType` before bulk work | DF 4739240 (2026) |
| D-13 | **Global data is not player data.** Leaderboards: ordered stores (`BatchGetAsync`) or Roblox's native leaderboards; cross-server state: MemoryStore (ephemeral) or MessagingService (best effort). Never write one hot shared key from every server | EL:622-634; memory-stores/best-practices.md:19 |
| D-14 | **Recovery path exists before launch.** Version history (30 days) and the Data Stores Manager can restore a player; take an Open Cloud snapshot before publishing a save-logic change; write the restore steps in the game's system note | VLC:59-98 |

## 5. Adapters (wrappers)
A persistence package is one adapter behind the game's own data module. Before adopting or keeping one, check it against D-02, D-04, D-07, D-08, D-09 and D-11, and record the answers in `knowledge/reference/`. Roblox's guidance: vet the module's maintenance and know how to read your data without it (BP:33-42). DataStore2 is legacy. Known traits of ProfileStore (community, rank 4): lock in the profile metadata via `UpdateAsync`, autosave 300 s, takes over a lock after about 40 s of waiting and treats a holder as dead after 630 s, replaces malformed records with the template (hook `OnOverwrite`).

## 6. Rules (final check)
- No player data written before load, lock and migration finish, or from an errored session.
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
