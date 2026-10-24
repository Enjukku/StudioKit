---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# Player data layer: keep, switch or write our own?

All web checks were made on **2026-10-24**. GitHub facts came through a page-reading tool (not `gh`); dates marked "API" are GitHub API `pushed_at`. Label key: DOC = documented fact, SRC = read in source, INF = my inference, NV = not verified. The context packet command could not be run (no shell in this role); I read the files the brief named.

## 1. Short answer

1. **`leifstout/dataservice@1.0.0` is a thin layer on top of ProfileStore 1.0.3** (loleris / Mad Studio). It requires `lm-loleris/profilestore@1.0.3` as a server dependency (`dataservice/wally.toml:19`) and calls `ProfileStore.New`, `StartSessionAsync`, `EndSession`, `MessageAsync` (`DataServiceServer.luau:131,188,309,264`). Every game we ship today therefore already gets its lock, autosave and shutdown from ProfileStore. SRC, installed copy at `GreatWallSim/Packages/_Index/`.
2. The real question is therefore "ProfileStore plus whose wrapper": dataservice (87 stars, one maintainer, 8 open issues, no migrations, no tests shipped), or our own thin adapter on ProfileStore.
3. **Recommendation: ProfileStore, vendored and pinned, behind our own small adapter** (schema versions and migrations, degraded state, receipt ids). Do not write our own lock. Details in section 5.
4. One rule conflict the owner must see: ProfileStore's last commit is **2025-07-31**, about 15 months old, so it fails `rules/packages.md` item 2 (release or commit within 12 months) read literally. Section 6.

## 2. Engine facts that bound the choice (docs first)

| Fact | Source |
| --- | --- |
| Roblox has **no engine session lock**. Roblox documents a lock pattern (LockId in key metadata set in the first `UpdateAsync`) but calls its own sample "reference only ... has not proven itself over a long period of time in a popular game ... Don't use this code in your game as-is" | `knowledge/external/roblox-creator-docs/cloud-services/data-stores/player-data-purchasing.md:44,164` |
| Roblox says third-party data modules "may be preferred to building systems from scratch"; vet owner, maintenance, features; know how to read your data without the module. DataStore2 is legacy | `.../best-practices.md:33-42` |
| Without session locking, one server saves stale data: "data loss and common item duplication loopholes" | `.../player-data-purchasing.md:37` |
| Autosave must be shorter than any lock expiry; Roblox sample uses 180 s | `.../best-practices.md:48` |
| Retries per key must be ordered; a failed write may have landed | `.../best-practices.md:58`; `data-saving/references/engine-facts.md:36-38` |
| Roadmap row: "player-data management (transactions, session locking, schemas)", early 2027, status **planned**, unconfirmed on an official page. Nothing native to adopt yet | `knowledge/reference/roblox/whats-new.md:108` (roadmap, 2026-09-18) |
| 2026 limit change that matters: one DataStore budget shared by game servers and Open Cloud since 2026-07-29; storage 500 MB + 1 MB per lifetime user | `whats-new.md:103` (DF 4739240) |
| No 2025-2026 engine feature found that replaces session locking or changes the lock pattern. MemoryStore remains ephemeral, "not for persistent player records" | `engine-facts.md:44-45`; NV beyond the mirror (web search found no official 2026 announcement) |

## 3. What the installed code really does (SRC)

### 3.1 ProfileStore 1.0.3 (`.../lm-loleris_profilestore@1.0.3/profilestore/ProfileStore.luau`, 2243 lines, Apache-2.0, `wally.toml` dependencies: none)
| Topic | Behaviour | Line |
| --- | --- | --- |
| Lock | Stored in the key's own data (`MetaData.ActiveSession = {PlaceId, JobId, uniqueId}`), set inside `UpdateAsync` on load; every save is an `UpdateAsync` whose edit step writes only if this session still owns it (`IsThisSession` and `SessionLoadCount == load_index`); otherwise the save is skipped | 1462-1466, 747-768 |
| Second server wants the key | Sets `ForceLoadSession`, publishes `EndSession` over MessagingService to the holder, polls at 5 s then every 10 s; the holder saves, releases and fires `OnLastSave("External")` | 1573-1590, 843-848 |
| Lock steal | Waiter steals after `SESSION_STEAL` = 40 s (4 poll rounds). The old server gets **no** last-save event and its unsaved changes since its last save are lost; the docs say so | 173, 1577, header 123-125 |
| Server crash | Lock stays in the key. A new server steals after about 40 s (INF from the steal path); `ASSUME_DEAD` = 630 s only skips the wait when the key's `LastUpdate` is older than that | 174, 1470-1476 |
| Teleport | Same path as a rejoin: request force load, holder releases on message. `ListenToHopReady` was removed in ProfileStore (DevForum release post, 2024-10-11) | 1584-1590 |
| Autosave | 300 s, staggered across profiles by index (`AUTO_SAVE_PERIOD / profile_count`), fresh profiles skipped for half a period | 170, 2115-2152 |
| Shutdown | `BindToClose` sets `IsClosing`, saves and releases all profiles in parallel, waits until all save and load jobs finish. It does not watch the 30 s limit itself (Roblox ends the server) | 2208-2239 |
| Failure handling | Exponential backoff (cap 20 s), 120 s start timeout, "critical state" after 5 errors in 120 s, `OnError` signal. A failed start returns `nil` (no degraded mode) | 175-179, 1610-1622, 2157-2172 |
| Metadata and userIds | Passed through on every `UpdateAsync` (`return latest_data, latest_data.UserIds, latest_data.RobloxMetaData`); `AddUserId` for GDPR | 588, 791-793 |
| Reconcile | Fills **missing keys** from the template only. No `schemaVersion`, no migration steps, no newer-schema guard | header 142-143 |
| Receipts | None built in. Docs give a `PurchaseId` cache pattern that yields in `ProcessReceipt` until `Profile.LastSavedData` holds the id | `docs/devproducts/index.md:85-235` |
| Cross-server updates | `MessageAsync` stored in the profile (max 1000 queued), delivered when the profile is next loaded or autosaved; not real time | 181, 1683 |
| Mock mode | `ProfileStore.Mock` with an in-memory store; no `VersionQuery` in mock | header 52-54, 1925-1927 |
| Strict types | File has no `--!strict` line. It exports typed interfaces (`Profile<T>`, `ProfileStore<T>`, `JSONAcceptable`) that strict callers use | `ProfileStore.luau:998-1030`; `ProfileStore.lua` shim in dataservice index |
| Tests | `ProfileStoreTest.server.luau` (about 390+ lines) is a **live** in-Studio script (needs API access) with payload, KeyInfo, mock and one versioning test. The author notes the versioning test no longer tests properly since the July 2024 version change. No offline suite | `ProfileStoreTest.server.luau:6,177-183,219-370` |

Mapping to our `data-saving` rules: D-04 lock on load = yes; D-07 UpdateAsync-only with metadata = yes; D-09 parallel save on shutdown = yes; D-06 cadence = autosave 300 s (Roblox sample is 180 s; rule says shorter than lock expiry, which is met); **D-02 versioned migrations = no; D-02 newer-schema guard = no; D-04 named session states (degraded) = no; D-11 receipt idempotency = pattern only**. Those four gaps are what a thin adapter must close.

### 3.2 leifstout/dataservice@1.0.0 (`.../leifstout_dataservice@1.0.0/dataservice/src/`, 1289 lines in 5 files, MIT, 2021 notice)
| Topic | Finding | Line |
| --- | --- | --- |
| What it adds | Path-based get/set/update/array ops with change signals, auto-replication to the client through Networker, global messages, per-player removal hooks | `DataServiceServer.luau:480-688` |
| Dependencies | Signal 2.0.0, Janitor 1.17.0, Networker 0.3.1 (shared), ProfileStore 1.0.3 (server). Pulls our transport choice into the data layer | `wally.toml:13-19` |
| Load failure | Kicks the player ("Profile load fail - Please rejoin"); no degraded play | `DataServiceServer.luau:190-193` |
| Footguns | Options `resetData` (removes the profile on join), `overridenUserId`, `viewedUserId`, `dontSave`, `useMock` sit in the same table as production options. One wrong boolean wipes or hijacks saves | `:61-90,181-183` |
| Bug confirmed in source | `asyncGetProfile` uses the constant `DATA_PREFIX`, ignoring `profileStoreDataPrefix` (open issue #10, 2026-04-15) | `:395` |
| Key names | Store `"Default"` and key `"PLAYER_<UserId>"` by default, not our `Player_<UserId>` (D-01) | `:16-17,238` |
| Migrations, validation, receipts | None. `update` runs a callback on in-memory data; no validation hook | `:527-541` |
| Typed | `--!strict` at top | `:1` |
| Tests | None in the published package (`wally.toml:10-11` excludes everything but `src`); repo tree shows `docs` and `src` only | GitHub page 2026-10-24 |

## 4. Comparison table

Dates: "last push" is the newest commit date I saw; "release" is the newest tagged release. Stars are from the GitHub page on 2026-10-24.

| Candidate | Owner / licence | Release, last push | Strict types | Size, deps | Lock method; crash / steal / teleport | Migrations | Save timing, BindToClose | Receipts | Cross-server | Tests | Known open issues | Used by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ProfileStore 1.0.3** (MadStudioRoblox/ProfileStore, 346 stars) | loleris, Mad Studio / Apache-2.0 | No tagged releases on GitHub (Wally 1.0.3 is what we have; who published it: NV). Last push **2025-07-31** (API); newest commit message 2025-06-18 | Typed exports, file not `--!strict` | 2243 lines; 0 deps | Lock in key data, MessagingService hand-off, steal after 40 s, dead after 630 s (section 3.1) | No (Reconcile only) | 300 s staggered; parallel BindToClose | Pattern in docs, not built in | `MessageAsync` per profile | Live Studio script, no offline suite | 1 open issue (#21 asks for an official Wally upload, 2026-06-28). 5 open PRs 2026-04 to 2026-09 unmerged (#19 new type solver fix, #22 buffer deep copy by reference, #20, #23, #24) | DevForum thread names Grow a Garden and Dead Rails (second-hand summary; NV against the games). Scribe sits on it |
| **leifstout/dataservice 1.0.0** (87 stars) | Leif Stout / MIT | No GitHub releases listed; last push 2026-02-26 (docs), code 2025-12-01 | Yes (`--!strict`) | 1289 lines; Signal, Janitor, Networker, ProfileStore | Inherited from ProfileStore | No | Inherited | None | Wraps `MessageAsync` | None published | 8 open (2026-02 to 2026-06), e.g. #13 duplicate client listeners, #10 prefix ignored, #8 signal not fired on client; none about data loss | No named games found (NV) |
| **ProfileService** (MadStudioRoblox/ProfileService, 332 stars) | loleris / Apache-2.0 | README: "FOR NEW PROJECTS - USE ProfileStore", "no longer supported". Last push **2024-10-13** (API) | Untyped | One module | Same family, older: no MessagingService, longer waits (30 s autosave default) | No | 30 s autosave | Pattern in docs | GlobalUpdates | Not checked | 5 issues, 7 PRs open | Described as battle-tested by many popular games (DevForum search summary; no named game verified) |
| **Lapis 0.3.x** (nezuo/lapis, 82 stars) | nezuo / MIT | GitHub latest v0.3.3 2024-08-24; npm 0.3.8 2025-02-07; last push **2025-02-12** (API) | Yes (README says typed; NV in source) | Promise-based; Wally deps NV | One document per server; lock cleared on some failed closes; documents batch saves; autosave 5 min | **Yes**, plus `validate` and `freezeData` | 5 min; closes all documents on shutdown | No | No | `test/` folder exists; scope NV | 8 open issues; README: "has not been battle-tested in a large production game yet. It may contain obscure bugs" | No named games (README states none) |
| **Scribe 2.6.1** (ericplane/Scribe, 48 stars) | Eric / MIT | Posted 2026-07-15 on DevForum; no GitHub releases listed; 109 commits | Typed accessor tree (new type solver recommended) | Large: replication, leaderboards, gifting, perks, Studio plugin. Bundles ProfileStore | ProfileStore's lock | **Yes**, fail-closed, `VersionAheadPolicy`, schema hash handshake | ProfileStore's | **Yes**, idempotent, fail-closed | Gifting, leaderboards | Jest suite (203 to 231 tests per v1.0.8 notes); CI | 1 open PR; issue count NV | Eurotunnel, Border Roleplay, Project Flight (developer's own claim, 100M+ visits; NV) |
| **Suphi's DataStore Module** (DevForum 2425597) | 5uphi / permissive grant text | Version 1.1, 2023-06-19 (thread continues past post 336; later versions NV). No GitHub repo | Module not strict | Single module, compression | MemoryStore lease, 60 s interval, closes after 5 failed attempts | No ("does not tamper with data") | Autosave + BindToClose | Example only | MemoryStoreQueue messaging | None published | NV | None named |
| **DataSafe** (DevForum 4012832, Snow_o29) | Snow_o29 / MIT | v0.1 beta, 2025-10-18 | NV | Zero deps, no repo link | Lock in data, expires after 5 min | Yes, versioning | Backups (3 copies), retries | No | No | None described; author withdrew "battle-tested" label | NV | None |
| **DataKeep**, **DocumentService** | NV | NV | NV | NV | NV | NV | NV | NV | NV | NV | NV | **Not found.** Four searches returned no repo or thread under these names. Not verified, excluded |
| **Raw DataStoreService + our own lock** | Us | n/a | We choose | See section 7 | We write it | We write it | We write it | We write it | We write it | We write them | Our bugs | Only the Roblox sample as a design source, which Roblox says is unproven |

## 5. Ranked recommendation (PROPOSAL; the owner decides)

### Pick 1: ProfileStore (vendored, pinned) behind a Studio Kit adapter we write

**Why**
1. **Strongest field evidence.** It is the maintained successor of ProfileService, which the community treats as the standard lock library; ProfileStore adds MessagingService hand-off, typed exports, a mock store and a documented receipt pattern. Named popular users appear in the DevForum thread (second-hand; NV). No formal proof of "no loss, no dupes" exists for **any** candidate; I found no audit or model-checking. Read this as "most exposure and fewest reported loss bugs", not "proven".
2. **Our games already run it** underneath dataservice, so existing player keys stay readable. The adapter can keep the same store name and key prefix, or read both. INF; keys are `PLAYER_<id>` in store `Default` unless a game set `profileStoreIndex`, which must be checked per game.
3. **No dependencies, readable source** (2243 lines, SRC), Apache-2.0 (keep the notice), replaceable behind one module, readable without the module because the stored record is plain JSON with `Data`, `MetaData`, `GlobalUpdates` (`ProfileStore.luau:1497-1504`). That meets `rules/packages.md` items 3-5 and `best-practices.md:33-42`.
4. **Our rules are mostly met by the library itself** (D-04 lock, D-07, D-09). The adapter closes what is missing: schema version and pure migrations (D-02), newer-schema fence (D-02, D-15), named states including degraded (D-04, D-08), receipt id cache and award ids (D-11), data-store name prefix for Studio (D-10), offline tests through a fake `ProfileStore`.

**Weakest part**
- **Stale upstream.** Last commit 2025-07-31; five PRs unmerged since April 2026, one touching deep copy of buffers (#22) and one the new type solver (#19). We would own a pinned copy and patch it ourselves, and the lock code is the part we least want to edit.
- No offline test suite; the live test script is the only proof. We should add our own lock tests against the mock store (see section 7).
- `StartSessionAsync` returns `nil` on failure with no reason; the adapter must map that to degraded or kick.

### Alternative: Lapis, only if the owner wants migrations and validation inside the library

**Why:** the only other maintained-looking library with a lock, built-in migrations, validation, retries and throttling in one MIT package, with a design that is readable and the same one-document-per-server idea as the Roblox sample. Its release notes show real data-loss fixes (0.3.0, 2024-04-14: "fixes an edge case that could cause data loss"; 0.2.11: infinite yield in `BindToClose`), which means the author finds and fixes this class of bug.
**Weakest part:** last push 2025-02-12 (also older than 12 months), the README says it is **not battle-tested in a large production game**, promise-based API (Roblox Lua `Promise` dependency we do not otherwise use; NV), no receipts, no named users, and it would mean moving every live game's saved records (different format). I would not pick it for a launch-critical game.

**Scribe** is not ranked: it bundles replication, leaderboards, gifting and a plugin (the "framework for its own sake" `rules/packages.md` warns about), it is 3 months old on DevForum, and it still rests on ProfileStore, so it adds no independence. It is useful as a **design reference** for fail-closed migrations and `VersionAheadPolicy`.

**Keep dataservice as is?** Works today, but it mixes three concerns (data, replication, transport) and ties to Networker; has the `resetData` footgun; has no migrations or receipts; one maintainer. Replace it with the adapter when the framework is built; the replication part belongs to the state layer, not the data layer. INF.

## 6. Decision for the owner: the 12-month maintenance rule

`rules/packages.md` item 2 says "a release or commit within the last 12 months". ProfileStore: last commit **2025-07-31**, about 15 months. Lapis: 2025-02-12, about 20 months. ProfileService: 2024-10-13, about 24 months (and declared unsupported). Only dataservice (2026-02-26) and Scribe (2026-07) pass, and both sit on ProfileStore. **No data library passes the rule and has field proof.** Options for the owner:
- (a) Keep ProfileStore with a recorded exception: the code is complete, stable, 1 open issue, and we pin and own a copy under the "pinned fork" clause (`rules/packages.md:19`). My recommendation.
- (b) Write our own (section 7): satisfies the rule on paper, has no field proof.
- Not recommended: any candidate in section 4 below ProfileStore.

## 7. What "our own" would need

| Part | Purpose | Estimate (INF) |
| --- | --- | --- |
| Request queue, budget check, ordered retry with backoff and jitter per key | D-08, `best-practices.md:54-58` | 150-200 lines |
| Lock acquire, refresh, release, expiry, steal, force-load request | D-04, D-07, `player-data-purchasing.md:164-203` | 200-300 lines |
| Cross-server hand-off over MessagingService (best effort only) | quick release on teleport | 80-120 lines |
| Session object: states, autosave stagger, leave, BindToClose with 30 s guard | D-06, D-09 | 150-200 lines |
| Schema version, pure migrations, newer-schema fence, validation | D-02, D-03 | 120-180 lines |
| Receipts and award ids | D-11 | 100-150 lines |
| Mock store with injected failures (throttle, yield, conflicting writer) | tests | 150-250 lines |
| Tests: lock races, crash, steal, double server, migration fixtures, receipt replays | gate | 500-900 lines |
| **Total** | | **about 1,000-1,400 lines of code plus 500-900 lines of tests** |

ProfileStore for comparison: 2243 lines including about 400 lines of header comments and mock code.

Risks added by writing our own:
- **A lock bug shows up as duplicated or rolled-back items in live games**, and our only evidence would be our tests. Roblox itself calls its sample unproven (`player-data-purchasing.md:44`).
- Races are the hard part (lock held while a save retry lands late, steal while the old server is mid-save, two requests for one key). These cannot be found by review alone.
- No exposure time. ProfileStore has had that since ProfileService (2020, per repo creation date).
- Ongoing cost: every engine change to budgets, versions or metadata hits our code. Roblox's planned native player-data feature (early 2027, unconfirmed) may make the lock part redundant, so lock code we write now could be thrown away.
- Counter-case for owning it: ProfileStore's maintainer looks inactive, and we would carry a pinned copy anyway.

## 8. Is a thin adapter over a package enough for our data-saving rules?

Yes for D-01, D-04 (lock on load), D-06, D-07, D-08 (retries), D-09, D-10, D-12 (lock respected by external tools, since the lock sits in the key and our tool can read `MetaData.ActiveSession`), D-13, D-14 (versions are Roblox's). Not by itself for D-02 (migrations, newer-schema fence), D-04 (named degraded state), D-05 (our `update(player, fn)` with checks), D-11 (receipt and trade ids) and D-15 (old and new servers): those are adapter work, about 400-600 lines plus tests (INF). The rule in `data-saving/SKILL.md:48` already lists ProfileStore traits; it needs no change.

Adapter checklist before launch of any game (from this research):
1. Keep one `StartSessionAsync` call per player with a `Cancel` on leave (dataservice already does, `:186-188`).
2. Treat `nil` as degraded: no writes, no purchases, kick or play-on by game choice.
3. On `OnSessionEnd` with the player still present: stop all writes and kick (dataservice does, `:197-200`).
4. Write `schemaVersion` into the template; on load run migrations in order before `Reconcile`; a newer version makes the session read-only.
5. Receipts: store `PurchaseId` in `Profile.Data`, grant, then wait for `LastSavedData` to contain it (`docs/devproducts/index.md:85-235`).
6. Never expose `resetData`-style options in production code paths; gate them by Studio.
7. Add our own tests against `ProfileStore.Mock` for: crash then steal, two servers load, save after steal skipped, shutdown with 1 profile and with a full server.

## 9. Uncertain or not verified

- Who published `lm-loleris/profilestore` on Wally (issue #21 asks whether there is an official upload). The installed source matches the Mad Studio header, but the publisher is NV.
- Games named for ProfileStore (Grow a Garden, Dead Rails) come from a page-reading summary of the DevForum thread, not from the games; NV.
- Lapis dependencies and its strict-types claim; Suphi's latest version after 2023-06-19; dataservice newer Wally versions than 1.0.0 (its 2025-12-01 "version bump" commit suggests one exists; NV).
- DataKeep and DocumentService could not be found.
- GitHub API values (`pushed_at`, stars, issue counts) were read via a summarising tool; spot-check with `gh api repos/MadStudioRoblox/ProfileStore` before the owner's decision.
- No independent audit or formal proof of no-loss exists for any candidate (none found).

## 10. Sources

- Local: `knowledge/external/roblox-creator-docs/cloud-services/data-stores/best-practices.md:33-58`; `.../player-data-purchasing.md:37,44,143-203`; `knowledge/reference/roblox/whats-new.md:103,108`; `.agents/skills/data-saving/SKILL.md`; `.agents/skills/data-saving/references/engine-facts.md`; `rules/packages.md`.
- Installed code: `C:\Users\Firew\Downloads\uterd\GreatWallSim\Packages\_Index\leifstout_dataservice@1.0.0\` and `...\lm-loleris_profilestore@1.0.3\profilestore\` (checked 2026-10-24); `GreatWallSim/wally.toml:8`.
- https://github.com/MadStudioRoblox/ProfileStore (page, issues, pulls, commits via API; 2026-10-24)
- https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543/ (post 2024-10-11)
- https://github.com/MadStudioRoblox/ProfileService (README banner; 2026-10-24)
- https://github.com/nezuo/lapis, `/tags`, https://registry.npmjs.org/@rbxts/lapis, https://cdn.jsdelivr.net/npm/@rbxts/lapis@0.3.8/README.md (2026-10-24)
- https://github.com/leifstout/dataservice and `/commits/main`, `/issues` (2026-10-24)
- https://devforum.roblox.com/t/scribe-v132-persistent-typed-auto-replicated-player-data-built-on-profilestore/4738905 (post 2026-07-15) and https://github.com/ericplane/Scribe
- https://devforum.roblox.com/t/suphis-datastore-module/2425597 (post 2023-06-15)
- https://devforum.roblox.com/t/datasafe-production-ready-datastore-manager/4012832 (post 2025-10-18)
