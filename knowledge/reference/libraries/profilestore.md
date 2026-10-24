---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
roles: [feature-builder, reviewer, architect, qa-lead]
---
> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24

# ProfileStore (vendored, patched): package record

| Field | Value |
| --- | --- |
| Package | ProfileStore by loleris (MadStudioRoblox/ProfileStore); Wally id `lm-loleris/profilestore` |
| Version | **1.0.3**, pinned copy (not from Wally) |
| Checked | 2026-10-24 (`knowledge/jobs/J025-base-framework/research/data.md` §3.1, §6) |
| Licence | Apache-2.0; `LICENSE` kept in `roblox-game-framework/vendor/ProfileStore/` (NOTICE/attribution when shipped as source) |
| Upstream state | last commit 2025-07-31 (about 15 months); five PRs unmerged since April 2026, incl. #22 (deep copy of buffers) and #19 (new type solver); no offline test suite (only a live Studio script) |
| Where pinned | `roblox-game-framework/vendor/ProfileStore/init.luau`; source copy, sha256 and patch list in `vendor/ProfileStore/PATCHES.md`; games get it only through `tools/install.py` (lock-checked), placed at `ServerScriptService.Framework.vendor` |
| Used by | the Session block only (`contracts/Session.md`); game code never requires it (`code-review` §8 B1) |
| Exception | fails `rules/packages.md` item 2 read literally; owner approved the pinned copy (J025-G1 D-2): `rules/packages.md` "ProfileStore exception" |

## Why chosen
- It gives the parts we least want to write: the session lock in the key's own metadata, set inside `UpdateAsync` on load; every save checks the session still owns the key; force-load over MessagingService, steal after 40 s; autosave 300 s staggered; parallel save and release on `BindToClose`; metadata and userIds passed through (`data-saving` D-04, D-07, D-09).
- Both earlier games already ran it (through DataService), so existing saves keep their format (Session S13: key `PLAYER_<UserId>`).
- Alternatives checked (Lapis, DataService, Scribe, DataSafe, ProfileService) were older, unproven at scale or a different record format (`research/data.md` §5-6). Our own lock is closed door CD-2.

## Known gaps and how the framework covers them

| Gap in ProfileStore 1.0.3 | Covered by |
| --- | --- |
| No schema version, migrations or newer-version guard; `profile:Reconcile()` writes `profile.Data` in place | Session: `schemaVersion`, pure migrations, its own reconcile on a deep copy, `validate`, the newer-version fence (S2, S7) |
| A failed start returns `nil` with no reason; no degraded mode | Session: retry every 1 s while the player stays, 120 s timeout through `Cancel`, then `degraded` (S9) |
| No receipt handling | Session's receipt handler: grant + `PurchaseId` in one update, confirm after `LastSavedData` holds it (S10) |
| No "release landed" event: a save already in flight at leave also fires `OnAfterSave` (lost 1 gold in review probe R2-1) | **Patch P-1**: `OnAfterSave` passes `is_ending_session`; Session clears the same-server rejoin hold only on the final save |
| `OnSessionEnd` fires synchronously; `IsActive`/`IsClosing` guards unreachable through events | kept as defense, held by direct-state specs (Session CC-5) |
| Malformed record replaced by the template (`OnOverwrite`) | Session logs store and key (S-T26) so a restore can start |
| Studio uses live stores when API access is on | Session prefixes `STUDIO_` in Studio (S14) |
| No offline tests | `src/Session/test/FakeWorld.luau` loads the real file per fake server (scripted DataStore faults, crash, shutdown); hard tests in `tests/acceptance/Session/` |

## Update path
Diff a new upstream release against our source copy and P-1; re-apply P-1 (or drop it if upstream adds the argument); run every Session spec and hard test; record the new source sha256 and a `PATCHES.md` row; move the pin in a framework tag; games re-install with `tools/install.py --ref <tag>`. Replacement cost: one block (Session); saved records keep ProfileStore's format, so a replacement must read it.
