---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: framework block contracts rev 2 (J025-S3-R2), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\contracts\` Session.md, Net.md, Admin.md, Anim.md, Loader.md, files as of 2026-10-24 (no git revision: the framework repo is uncommitted by rule 7). Depth: deep for Session, Net, Admin; standard for Anim, Loader. Round 2, selective (`rules/company.md` §7): every round-1 item re-traced against its own sequence, then the harm order over the architect's changed lines only. Carried: README, Helpers, State, Screens, Motion, Config, Analytics, ContentTests (ready in round 1, not re-read).

Goal questions: (1) Does any load, fence, failure or end path still write data other than what was loaded or earned (S2, S7, D-02)? (2) Is a paid receipt granted once for the join-time delivery (S10, D-11)? (3) Can one client flood the server through a listener-less event (N5, Q7)? (4) Do the new end-of-session rules show players the true state (S12)?

Evidence read: `vendor/ProfileStore/init.luau` 556-577, 700-730, 780-805, 1082-1094, 1302-1330, 1440-1625, 2068-2108, 2185-2235; `probes/p1-transport/gen/blink/Server.luau` 440-555; `_api-reference/classes/` MarketplaceService.yaml 2237-2310, Workspace.yaml 150-170, DataModel.yaml 25-56 and 544-560, Players.yaml 1550-1560, Animator.yaml 189-214 and 293-300, LayerCollector.yaml 55-77; `enums/AuthorityMode.yaml` 15-17.

## Round-1 items

| Item | Result | Where (contract file:line) | Re-trace |
| --- | --- | --- | --- |
| F1 | closed | Session.md:51, :79, :89 | Fence, then migrate, reconcile (own, never `profile:Reconcile()`) and validate on a deep copy; `profile.Data` assigned only after validate returns nil. A migration that drops Inventory now fails validate with `profile.Data` still the loaded table, so `EndSession` writes it back unchanged (`init.luau:790`). |
| F2 | closed | Session.md:95-96, :156 | Join-time receipt in `loading` now waits on `save:wait`, then grants; ProcessReceipt may yield for as long as the server runs (`MarketplaceService.yaml:2297-2299`). Residual ordering question in N2 below. |
| F3 | closed | Session.md:71, :79, :86, :138 | Session's `Cancel` returns true at 120 s; `init.luau:1610-1618` returns nil on `cancel_condition()`; a lock taken in the same call is released before return (`:1553-1556`), so the timeout leaves no lock. nil with the player present → degraded. |
| F4 | closed (new problem F11 in the same line) | Session.md:61, :89 | Own-end flag set before `EndSession`; `OnSessionEnd` fires synchronously inside the spawned `SaveProfileAsync` (`init.luau:720-726`, `:1090-1093`); fence and validate failures stay degraded, not kicked. A second `EndSession` on leave is a no-op (`:1091`). |
| F5 | closed | Net.md:33, :70, :112 | Patch step 3 replaces insert + warn past 256 with drop + `guard.reject(player, "no_listener")` in each reliable queue branch (`Server.luau:476-482` pattern, 5 branches); the unreliable branch keeps no queue (`:545-550`). Next packet stopped by `allow` after 20 rejects. |
| F6 | closed | Admin.md:48-49, :97, :103, :129-130 | No `AuthorityMode` read; Ad-T14 no longer tests it; Ad-T16 checks a clean boot and greps for the read. |
| F7 | closed | Admin.md:86, :124 | Join handler runs for `Players:GetPlayers()` after connecting; characters already present handled; Ad-T8 adds the solo-playtest case (`Players.yaml:1553-1558`). |
| F8 | closed | Session.md:63, :151 | S15 test cell = S-T18; S-T19 is in the Tests table; every invariant and failure row names an existing test id (S-T26 added for the overwrite row). |
| F9 | closed | Session.md:139, :151 | S-T3 and S-T19 assert the `Data` subtree byte-identical and the session released; MetaData writes (`init.luau:1513-1517`, `:797-801`) excluded. |
| F10 | closed | Anim.md:27-31, :38-39, :93 | `Anim.observe` connects `AnimationPlayed` (`Animator.yaml:295`), matches by asset id, never calls `LoadAnimation`; A3b keys connections by track object on both paths; A-T13 spies for no `LoadAnimation`. |
| R1 | closed | Session.md:98, :150 | Overwrite logged with store and key; S-T26. |
| R2 | closed | Session.md:121 | Path is `vendor/ProfileStore/init.luau`; env lists `warn`, `debug`, `Instance`, `GetDataStore(name, nil, options)`; fake API-check `SetAsync` succeeds (`init.luau:2071-2105`). |
| R3 | closed | Net.md:39, :113 | Lint requires `SingleAsync`/`ManyAsync` for client calls; Net-T19 fails a `SingleSync`. |
| R4 | closed | Net.md:51, :104 | `on`/`answer` error before `Net.guard`; Net-T11. |
| R5 | closed (wording note N3) | Admin.md:68, :71, :122, :125 | Value never leaves [min, max]; Ad7 adds `step > 0`, `min <= max`, `maxLength >= 1`; Ad-T9 covers them. |
| R6 | closed | Admin.md:37, :58, :96, :129 | 65,535 bytes including the marker (Blink u16 length). |
| R7 | closed | Loader.md:97 | `ReplicatedStorage.Framework.Loader`, as the README placement table. |

Lead decisions: applied. Studio admins (Admin.md:65, :118-119: `-1`, creator only when `CreatorType` is User, `-2` not; `DataModel.yaml:27-35`). Save view online only (Admin.md:58). Client boot failure = `error()` + visible message, no kick (Loader.md:49, :52, :81; durability note N1).

## Findings in the changed lines

```text
<spec>
artifact: roblox-game-framework/contracts/{Session,Net,Admin,Anim,Loader}.md @ 2026-10-24
reviewer: reviewer
findings:
  - {id: F11, class: blocking, where: "Session.md:61 (S12), :79 ('OnSessionEnd -> closed')",
     observed: "The new rule kicks on every OnSessionEnd that Session did not start. ProfileStore also ends sessions itself at shutdown: its BindToClose sets IsClosing and calls SaveProfileAsync(profile, true, nil, 'Shutdown') for every active profile (init.luau:2208-2229), which fires OnSessionEnd (:720-726) with no Session mark. Sequence: server shuts down while players are still in it (bound functions run in parallel and may teleport players, DataModel.yaml:544-560; e.g. a game's soft-shutdown teleport) -> ProfileStore releases each profile -> OnSessionEnd -> S12 kicks each player with TEXT.sessionMoved -> players see a false 'session moved' reason, and a teleport the game started for them fails because they were kicked.",
     expected: "S12's own scope ('another server took it'); players shown the true state; H-S5 shutdown path.",
     evidence: "High (player-facing, irreversible kick with a false reason on shutdown). Proof: ProfileStore source lines above (D, read). Whether players are still present in each CloseReason is not verified (S); the parallel-BindToClose case is enough for the sequence.",
     smallest_fix: "S12: kick only when Session did not end it and ProfileStore.IsClosing is false; at shutdown OnSessionEnd -> closed, no kick (IsClosing is set before the first release, :2210).",
     protect: "H-S3 (a stolen session still kicks), the own-end flag of F4.",
     retest: "H-S5 also asserts 0 kicks during shutdown; H-S3 unchanged."}
  - {id: N1, class: recommendation, where: "Loader.md:49, :81 (L-T14)",
     observed: "The client failure ScreenGui is made by script in PlayerGui; ResetOnSpawn defaults to true, and a true LayerCollector deletes itself when the character respawns (LayerCollector.yaml:55-69). The client Loader runs before or around the first spawn, so the message can vanish on that spawn or the next respawn, leaving a broken client with no message.",
     smallest_fix: "Set ResetOnSpawn = false on the failure ScreenGui (as Admin Ad6 does); L-T14 adds one respawn.",
     blocking: no}
  - {id: N2, class: recommendation, where: "Session.md:95-96, :156 (S-T22)",
     observed: "The docs say ProcessReceipt runs once the user is on the server (MarketplaceService.yaml:2308-2309) but not whether before or after PlayerAdded handlers. A receipt that runs before Session's PlayerAdded handler made the entry has no status row: 'not on this server' -> NotProcessedYet would bring back F2 for that order.",
     smallest_fix: "Row :96: a player in Players with no Session entry yet counts as loading; S-T22 also delivers the receipt before the PlayerAdded handler runs.",
     blocking: no}
  - {id: N3, class: recommendation, where: "Admin.md:68 vs :122 (Ad-T6), Net.md:51",
     observed: "Ad4 'snapped from min ... and clamped back' does not name the rounding: nearest rounding gives 10 -> 12 -> 10, Ad-T6 expects 8 (floor). Net N8 still says the queue 'warns past 256, no cap', against patch step 3.",
     smallest_fix: "Ad4: 'the largest grid value <= the input' (or name the rounding); N8: 'capped at 256 by patch step 3'.",
     blocking: no}
keep:
  - Session load on a deep copy with assignment after validate; own timeout through Cancel (lock released if it lands, init.luau:1553-1556); own-end flag before EndSession; receipt wait with the yield guarantee cited; overwrite log
  - Net queue cap inside the existing patch run, reject counted against the sender, test for a listener-less flood and the boot window together (Net-T20)
  - Admin: no restricted property read, existing-player sweep, Studio admin rule with the group-owned case tested (Ad-T15), Ad7 limit checks
  - Anim: a separate observer path that never loads tracks; connections keyed by track object
could_not_check:
  - {step: "F11 severity: players present at ProfileStore's release for each CloseReason", missing_input: "engine evidence", closes_it: "H-S5 in the Studio lane or a probe-place shutdown with 1 client", who: "qa-lead"}
  - {step: "N1: script-inserted ResetOnSpawn GUI removed on the first spawn", missing_input: "Studio run", closes_it: "L-T14 with one respawn", who: "qa-lead"}
  - {step: "N2: ProcessReceipt vs PlayerAdded handler order", missing_input: "engine evidence", closes_it: "S-T22 variant; a live purchase test", who: "qa-lead"}
  - {step: "Ad-T16: AuthorityMode set from a Rojo project (write security RobloxScriptSecurity; can_load true, so rojo build works, a live rojo serve sync may not)", missing_input: "Studio run", closes_it: "Ad-T16 on a built place file", who: "feature-builder"}
weakest_part: "F11 is in a line the F4 fix rewrote but the same shutdown kick was already implied by round 1's 'OnSessionEnd -> closed' + S12, and round 1 missed it; Anim and Loader changed lines were read at standard depth."
verdict: fix-first (F11)
</spec>
```

## Verdict per contract

| Contract | Verdict | Blocking ids |
| --- | --- | --- |
| Session | fix-first | F11 (one clause in S12; N2 recommended) |
| Net | ready | none (N3 wording) |
| Admin | ready | none (N3 wording) |
| Anim | ready | none |
| Loader | ready | none (N1 recommended) |

**Set: fix-first (F11).** One clause in Session S12; no other round is needed for Net, Admin, Anim, Loader. F11 can be checked by the lead against `init.luau:2208-2229` without a round 3 review of the whole set.
