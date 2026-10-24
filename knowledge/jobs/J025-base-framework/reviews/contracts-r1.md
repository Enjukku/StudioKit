---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: framework block contracts rev 1 (J025-S3-R1), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\contracts\` (README + 12 contracts), files as of 2026-10-24 (no git revision: the framework repo is uncommitted by rule 7). Depth: **deep** for Session, Net, Admin (saves, money, remotes, admin surface); standard for the other nine. Round 1. Line numbers below are `contracts/<file>:line`.

Goal questions (each names an invariant): (1) Can any load, release or failure path write data other than what the player earned (Session S2, S4, S7, D-02)? (2) Is every receipt granted exactly once and never left unresolved for a player who paid (S10, D-11)? (3) Can one client hurt the server or other players through Net or Admin before a handler or the admin check runs (N1, N2, Ad2)? (4) Does each Q4 failure have one defined behaviour and a test that fails for the real cause?

Read first: every contract; then `vendor/ProfileStore/init.luau` (1.0.3, the whole load, save, shutdown path), Blink 0.18.9 generated `probes/p1-transport/gen/blink/Server.luau:440-682` and Blink source `scratch/blink-src/src/Generator/Prefabs.luau:306-331`, `docs/pages/language/5-events.mdx:30-38`; the API reference rows listed under C3; DataService `DataServiceServer.luau:16,131,185-196,238`; GWS `Receipts.luau:17-64`; then the probe verdicts and research.

## Findings (ranked by harm; blocking first)

```text
<spec>
artifact: roblox-game-framework/contracts/*.md @ 2026-10-24
reviewer: reviewer
findings:
  - {id: F1, class: blocking, where: "Session.md:51, :79, :89",
     observed: "The load order is 'migrate (on a copy) -> Reconcile -> validate' and names ProfileStore's Reconcile, but never says when profile.Data is assigned. ProfileStore's Profile:Reconcile() fills self.Data in place (init.luau:1086-1088, ReconcileTable :408-422). To reconcile the migrated copy with it the builder must first assign the copy to profile.Data. Sequence: save v1 loads; migration v1->v2 has a bug that drops Inventory; copy assigned to profile.Data; Reconcile; validate returns 'missing Inventory'; :89 ends the session; EndSession saves latest_data.Data = profile.Data (init.luau:790) -> the broken v2 data is written and the player's inventory is gone for good. Reconciling the original instead also writes to the record before validate.",
     expected: "Session.md:89 'session ended with the loaded record untouched'; data-saving D-02.",
     evidence: "Critical (harm 1, data loss in the path meant to stop it). Proof: ProfileStore source lines above (D, read).",
     smallest_fix: "One sentence in Lifecycle: fence first; migrate, reconcile (Session's own, ReconcileTable semantics) and validate on a deep copy; assign profile.Data only after validate returns nil; never call profile:Reconcile().",
     protect: "S8 (unknown keys kept), the newer-version fence S7.",
     retest: "the restored S-T19 (F8) with a migration that drops a key: backend Data bytes identical after the session."}
  - {id: F2, class: blocking, where: "Session.md:95 vs :152",
     observed: "Two behaviours for one case: the failure table says a receipt while the player is loading is NotProcessedYet; S-T22 says it waits. MarketplaceService calls ProcessReceipt for unresolved purchases 'when a user joins the server' and calls it again only on another purchase or a rejoin (MarketplaceService.yaml:2262-2265, :2290-2295). The load takes at least one UpdateAsync, so the join-time call lands in 'loading'. Sequence with :95: player buys a product on the Store tab, joins, receipt arrives while loading -> NotProcessedYet; every later join repeats this -> the paid item is never granted.",
     expected: "S10; D-11; a paying player gets the item.",
     evidence: "Critical (harm 3, money). Proof: API reference lines above (D).",
     smallest_fix: "Row :95: 'not on this server or degraded -> NotProcessedYet; still loading -> wait until ready, then grant (closed meanwhile -> NotProcessedYet)'.",
     protect: "S-T21 (two servers at once), S-T23.",
     retest: "S-T22 with the receipt delivered in the same frame as PlayerAdded: granted once after ready."}
  - {id: F3, class: blocking, where: "Session.md:79 ('{ Cancel = left }'), :86, :136 (S-T2)",
     observed: "The contract says ProfileStore stops retrying after 120 s and returns nil -> degraded. In ProfileStore 1.0.3 that timeout applies only when no Cancel is passed: 'if params.Cancel == nil then default_timeout = ...' (init.luau:1610-1614). Session passes Cancel, so during a DataStore outage StartSessionAsync retries until the player leaves. Sequence: DataStore down at join -> status 'loading' forever -> degraded never happens, Net drops every non-beforeReady request, a waiting receipt (F2) waits until leave. The player is stuck on a load screen with no message.",
     expected: "Session.md:86 and S9 (degraded play after the load fails).",
     evidence: "High (harm 1/4). Proof: source line above (D). S-T2 would go red against the real module, but the contract names ProfileStore as the owner of a timeout it does not apply.",
     smallest_fix: "Session owns the timeout: Cancel = function() return left or os.clock() - startedAt >= 120 end; nil while the player is present -> degraded, else closed. Owner row :71 changes to match.",
     protect: "lock conflicts: ProfileStore steals after about 45-50 s (FIRST_LOAD_REPEAT 5 + 4 x LOAD_REPEAT 10), inside 120 s.",
     retest: "S-T2 unchanged; H-S4 time to ready <= 50 s still passes."}
  - {id: F4, class: blocking, where: "Session.md:61 (S12), :79 ('OnSessionEnd -> closed'), :89, S7",
     observed: "On a newer-version save (S7) or a failed migration or validate (:89) Session itself calls EndSession and wants the player 'degraded'. EndSession fires profile.OnSessionEnd synchronously (SaveProfileAsync, init.luau:720-726). The contract maps OnSessionEnd to 'closed' (entries removed, get = nil) and S12 kicks a player who is still here with TEXT.sessionMoved. Sequence: v5 save joins a v4 server -> EndSession -> OnSessionEnd -> closed + kicked 'session moved'; every rejoin to an old server repeats it.",
     expected: "S7 and :89: degraded, play on a template copy.",
     evidence: "High (player-facing, wrong state and false message). Proof: source line above (D).",
     smallest_fix: "Session marks its own ends (leave, fence, migration or validate failure) before calling EndSession; OnSessionEnd -> closed and the S12 kick only when Session did not end it.",
     protect: "H-S3 (stolen session still kicks).",
     retest: "S-T3 and S-T19 also assert: not kicked, status degraded, get = template copy."}
  - {id: F5, class: blocking, where: "Net.md:50 (N8), :31-33 (patch steps)",
     observed: "Blink queues events for a client event that has no listener: insert into Queue with no cap, and a warn on every insert past 256 (gen Server.luau:476-482, the same in every queue branch). Nothing makes every From: Client event have a handler; framework.blink is merged into every game's schema (Net.md:38), so AdminAction and other framework messages exist even in a game that does not start that block. Net's rate check lives in the handler (never reached) and the guard blocks only after decode rejects (valid packets are not rejects). Sequence: one exploit client packs thousands of valid events per frame for a handler-less event into its Blink batches -> server memory grows without bound and Output gets one warn per event: the log flood and heartbeat cost the G6 patch exists to stop, plus a memory leak until the server dies.",
     expected: "Q7; N5 (no log line per denial); networking-security N-02 rate before work.",
     evidence: "High (harm 2/5, server-wide denial of service by one client). Proof: generated code lines above (D).",
     smallest_fix: "Patch step 4: in each queue branch, past 256 queued entries for that event, drop the event and call guard.reject(player, 'no_listener') instead of insert + warn.",
     protect: "N8 boot window (events sent before start still queue and are handled, Net-T15).",
     retest: "new Lune row: 10,000 events to an event with no listener -> queue <= 256, 0 new Output lines, sender blocked by allow after 20 rejects."}
  - {id: F6, class: blocking, where: "Admin.md:48-49, :97, :103, :128 (Ad-T14)",
     observed: "core.fly and core.noclip are 'not shown and refused' in a Server Authority place, decided by Workspace.AuthorityMode. That property's read security is RobloxScriptSecurity (Workspace.yaml:153-165): game scripts cannot read it. 'Not shown' means deciding at start or join, so the natural build reads it in Admin.start -> the read throws -> Admin.start errors -> Loader L5 fails the boot -> every player of every game using Admin is kicked. Ad-T14 tests it in Lune on a fake that can read the property, so the test cannot fail for the real cause.",
     expected: "README rule: engine APIs exist and are usable; test rows fail for the real cause.",
     evidence: "High (harm 7 turning into harm 4: boot failure). Proof: API reference security field (D). Not runtime-probed: a one-line Script `print(workspace.AuthorityMode)` in the probe place closes it.",
     smallest_fix: "Never read AuthorityMode. State in Failure behaviour that core.fly/noclip are not for Server Authority places (ticket stays), and drop the AuthorityMode case from Ad-T14, until a probe finds a value game scripts can read.",
     protect: "Admin.start touches no restricted property.",
     retest: "Studio engine row: Admin.start in a place with a Server Authority setting, boot report clean."}
  - {id: F7, class: blocking, where: "Admin.md:86 (Lifecycle)",
     observed: "Admin decides admin status and clones the panel only from PlayerAdded (and CharacterAdded for exemptions). In a Studio solo playtest the player exists before scripts connect PlayerAdded (Players.yaml:1553-1558). Session handles present players (Session.md:78); Admin does not. Sequence: the place creator presses Play in Studio -> PlayerAdded never fires for them -> isAdmin false, no panel. Ad-T8 runs with clients that join after start, so it cannot catch this.",
     expected: "Ad1 (creator is admin in Studio), Ad6.",
     evidence: "Medium (the panel fails in its most common test path). Proof: docs line above (D).",
     smallest_fix: "After connecting PlayerAdded, run the same join handler for each player in Players:GetPlayers() (task.spawn), and CharacterAdded's handler for characters already present.",
     retest: "Ad-T8 adds a solo-playtest case: panel present for the creator."}
  - {id: F8, class: blocking, where: "Session.md:63-64",
     observed: "Table damage: the S15 row's test cell reads 'S-T19 | a migration throws; validate returns a reason: degraded, backend record byte-identical | Lune |' and line 64 holds a stray '| S-T18 |'. Test S-T19 is missing from the Tests table (:133-161). The Q4 failure 'Migration throws, or validate returns a reason' (:89) has no test row, and S15 points to S-T19 while its test is S-T18.",
     expected: "Q4: every failure has a behaviour and a test.",
     evidence: "Medium (lost coverage on the F1 path). Proof: file text (D).",
     smallest_fix: "S15's test cell = S-T18; move S-T19 into the Tests table (wording per F9).",
     retest: "row count: every invariant and failure row names an existing test id."}
  - {id: F9, class: blocking, where: "Session.md:137 (S-T3) and the S-T19 text",
     observed: "Both assert 'backend record byte-identical' after the session. ProfileStore's own load writes MetaData.SessionLoadCount + 1, LastUpdate and ActiveSession (init.luau:1513-1517), and its release writes LastUpdate again and clears ActiveSession (:797-801). The record cannot be byte-identical even when the fence works, so the test is red for a reason that is not a bug, and the builder must change a contract test without a recorded decision (README.md:12).",
     expected: "Q3: tests can fail only for the real cause.",
     evidence: "Medium. Proof: source lines above (D).",
     smallest_fix: "Assert the record's Data subtree byte-identical and the session released.",
     retest: "H-S6 planted fault 'drop the newer-version fence' still turns S-T3 red."}
  - {id: F10, class: blocking, where: "Anim.md:36-40 (A3b, A3, A6), :87 (A-T8), :89 (A-T11)",
     observed: "A-T8 and A-T11 need markers on an observing client for a clip a server rig plays. The only marker path is onMarker on a track Anim loads with LoadAnimation (A3); LoadAnimation always makes a new track (Animator.yaml:191-213), which never plays. The replicated track arrives through Animator.AnimationPlayed (P4 item 2), which no API or Lifecycle row connects. Sequence: client does Anim.new(npcAnimator, Clips):onMarker('swing', 'Contact', fn); server plays 'swing' -> fn never fires. A3b describes de-duplication for a path that does not exist.",
     expected: "README: a builder builds a block from its contract alone.",
     evidence: "Medium (structure; Anim). Proof: contract text + P4 verdict lines 40, 43 + API reference (D).",
     smallest_fix: "Either add the observer path (on a client, for an Animator it does not drive, onMarker attaches through AnimationPlayed by animation id, once per track object), or scope Anim to tracks it plays and drop the observer halves of A-T8 and A-T11.",
     retest: "A-T11 as written."}
  - {id: R1, class: recommendation, where: "Session.md:83-97 (Failure behaviour)",
     observed: "ProfileStore replaces a malformed record with the template and only fires ProfileStore.OnOverwrite (init.luau:560-575, :430-433). Session then loads it as a new player. Sequence: a Data Stores Manager edit or an outside tool leaves Data as a string -> join -> fresh template -> first save buries the old record (recoverable from versions for 30 days only if someone notices).",
     smallest_fix: "Row: 'record overwritten (OnOverwrite) -> error log with the key (sampled), so a D-14 restore can start'.",
     blocking: no}
  - {id: R2, class: recommendation, where: "Session.md:119 (seam)",
     observed: "The seam is sound: ProfileStore 1.0.3 has no require and reaches the engine only through globals, so one luau.load per fake server gives separate module state. The env list misses `Instance` (Instance.new('DataStoreOptions') and SetExperimentalFeatures at init.luau:1305-1306, run by every ProfileStore.New), DataStoreService:GetDataStore(name, nil, options) (:1323, :1328, :2080), `warn`, `debug`; the file is vendor/ProfileStore/init.luau, not ProfileStore.luau. With IsStudio true the module runs an API check SetAsync and falls back to its in-memory mock on failure (:2071-2105): S-T16's fake SetAsync must succeed to test the real path.",
     smallest_fix: "Fix the path and add those names to the env list.",
     blocking: no}
  - {id: R3, class: recommendation, where: "Net.md:37-38 (schema rules), :70",
     observed: "Net says 'a yielding handler re-checks', but Blink calls Sync listeners inline and closes the thread when the next packet arrives while it is suspended (gen Server.luau:463-467, the unreliable dispatcher calls its listener inline at :545; Blink docs 5-events.mdx:30-38: yielding in a sync event 'can cause undefined and sometimes game-breaking behaviour'). A From: Client event declared SingleSync with a yielding handler is cut off half-way.",
     smallest_fix: "Lint rule: every From: Client event is SingleAsync (or ManyAsync).",
     blocking: no}
  - {id: R4, class: recommendation, where: "Net.md:22, :32",
     observed: "If a game never calls Net.guard, the patched dispatcher has guard = nil: decode errors are swallowed with no count and no Output, and floods are not blocked.",
     smallest_fix: "Net.on/answer error at boot when no guard is set (fail loud, like Loader).",
     blocking: no}
  - {id: R5, class: recommendation, where: "Admin.md:68 (Ad4), :71 (Ad7)",
     observed: "'in [min, max], snapped to step': a snap after the range check can leave the range (min 0, max 10, step 4: 10 -> 12), and Ad7 does not require step > 0 (step 0 -> NaN). The usage example's action trusts that Admin checked the range (:149).",
     smallest_fix: "Snap from min, then clamp to [min, max]; Ad7 adds step > 0, min <= max, maxLength >= 1.",
     blocking: no}
  - {id: R6, class: recommendation, where: "Admin.md:37, :58",
     observed: "Blink writes an unbounded string's length as u16 (Prefabs.luau:328-329, max 65,535). A truncation target of 64 KB = 65,536 bytes overflows it.",
     smallest_fix: "Say '<= 65,535 bytes including the marker' or declare the schema string bound.",
     blocking: no}
  - {id: R7, class: recommendation, where: "Loader.md:96",
     observed: "Usage requires ReplicatedStorage.Packages.Framework.Loader; README.md:48-52 places Framework beside Packages (wally install wipes Packages).",
     smallest_fix: "Use the README path or the Framework.X placeholder.",
     blocking: no}
keep:
  - Session: frozen data plus checks inside fn (S1, S4), newer-version fence (S7), receipt flow confirmed by LastSavedData (S10; it stays correct when a receipt runs on two servers: the losing server reads the winner's record), the FakeWorld fault list and H-S1..H-S6
  - DataService compatibility holds: store = profileStoreIndex, key PLAYER_<UserId> (DataServiceServer.luau:16,131,238), same ProfileStore 1.0.3 record; GWS PurchaseIds is the Ledger array-of-strings format (Receipts.luau:17-64); GWS saves are v0, DS template has schemaVersion = 1
  - Net: guarded decode patch with a loud anchor failure, determinism re-checked by byte-compare (P1 T5), check order N1, counted denials, lint for G1/G2/G4
  - Admin: server check order Ad2-Ad5, two Studio locks (Ad3 + Session S15), client copy only from ServerStorage (Ad6), fixed kick reasons, fail-closed group rule
  - Placement table keeps Session, Net, Config, Analytics, Admin, ProfileStore and the Blink Server module off the client; README flags test.project.json mapping everything under ReplicatedStorage
  - Loader fail-loud with yield detection; Helpers keyed without tostring; Config never-throw reads; State per-player filter with a defined fallback
could_not_check:
  - {step: "Lune luau.load environment overrides (injectGlobals interplay)", missing_input: "a Lune run", closes_it: "S-00", who: "feature-builder"}
  - {step: "F6 runtime: AuthorityMode read error from a game Script", missing_input: "Studio probe", closes_it: "1-line Script in the probe place", who: "studio-operator"}
  - {step: "charm-sync 0.11 per-player filtering and pre-hydrate patch drop (State St2, St4)", missing_input: "package source at install", closes_it: "St-T2, St-T4", who: "feature-builder"}
  - {step: "Blink `function` (answer) and `unknown` type behaviour in 0.18.9", missing_input: "generated code for a function and an unknown field", closes_it: "Net-T0", who: "feature-builder"}
  - {step: "whether OnServerEvent can fire after PlayerRemoving (a leaked reject-count entry, N6)", missing_input: "engine evidence", closes_it: "Net-T10 in the Studio lane", who: "qa-lead"}
weakest_part: "Session, Net and Admin were traced against source and the API reference. The other nine contracts were read once in standard depth, so a gap there is less likely to have been found."
verdict: fix-first (F1-F10)
</spec>
```

## Verdict per contract

| Contract | Verdict | Blocking ids |
| --- | --- | --- |
| README | ready | none (R7 touches Loader) |
| Helpers | ready | none |
| Loader | ready | none (R7; client-kick answer below) |
| Session | fix-first | F1, F2, F3, F4, F8, F9 (R1, R2) |
| Net | fix-first | F5 (R3, R4) |
| State | ready | none |
| Screens | ready | none |
| Motion | ready | none |
| Anim | fix-first | F10 |
| Config | ready | none |
| Analytics | ready | none |
| ContentTests | ready | none |
| Admin | fix-first | F6, F7 (R5, R6) |

**Set: fix-first.** All ten fixes are text changes in the contracts (one to three sentences each); none changes a block's approach.

## The architect's open questions

| Question | Answer |
| --- | --- |
| Require style, ticket to S2 | Accept. |
| Gate wiring of patch-generated and schema-lint to S2 | Accept; add the F5 queue cap to the same patch run. |
| Admin save view: online players only | Accept (an offline view needs a lock-respecting read: a ticket when a game needs it). |
| Studio admins = UserId -1 + place creator, -2 not | Accept with one change: match the creator only when `game.CreatorType` is User. For a group-owned place `CreatorId` is the group id (DataModel.yaml:27-35), so the rule never matches the developer. Inside Studio only, so no security cost. |
| Kick on boot failure on the client too (PROPOSAL) | Do not accept as reasoned. "A rejoin lands on a healthy server" is true for a server failure, but a client boot failure repeats on every join for that client build or device, so "Please rejoin" sends those players into a loop. The client gains no safety from the kick: the server keeps authority. The owner decides, because it changes what players see. My default: the client calls `error()` loudly and does not kick. |

## C3: engine APIs checked against `_api-reference/`

Session: `MarketplaceService.ProcessReceipt` (:2237-2330), `MarketplaceService:BindReceiptHandler` (:46, exists, rejected with a reason), `DataModel:BindToClose` (:544), `RunService:IsStudio` (:580), `Instance:SetAttribute` (:2064), `Player:Kick` (:2078), `Players.PlayerRemoving` (:1610), `Players:GetPlayerByUserId` (:1085), `DataStoreService:GetDataStore` (:32), `GlobalDataStore:UpdateAsync` (:368), `MessagingService:SubscribeAsync`/`PublishAsync` (:129, :99), `HttpService:GenerateGUID` (:130), `HttpService:JSONEncode` (:295). Net: `RemoteEvent.OnServerEvent` (:177), `UnreliableRemoteEvent.OnServerEvent` (:200) and its 1,000-byte drop (:42-63). Admin: `Player:GetRankInGroupAsync` (:1709; `GetRankInGroup` :1681 Deprecated), `Player:LoadCharacterAsync` (:2238; `LoadCharacter` :2163 Deprecated), `Player:GetNetworkPing` (:1655), `Stats:GetTotalMemoryUsageMb` (:707), `PVInstance:PivotTo` (:120), `Humanoid.JumpHeight` (:608) / `UseJumpPower` (:1132), `DataModel.CreatorId`/`CreatorType` (:27, :52), `Workspace.AuthorityMode` (:153, exists but read is RobloxScriptSecurity: F6). Also spot-checked: `Animator:LoadAnimation` (:191), `Animator.AnimationPlayed` (:295), `AnimationTrack:GetMarkerReachedSignal` (:409), `GuiService.ReducedMotionEnabled` (:262), `GuiService.SelectedObject` (:289), `ScreenGui.ScreenInsets` (:176), `InputContext` (class file present), `ConfigService:GetConfigAsync`/`SetTestingValue`/`ClearTestingValue` (:52, :107, :30), `ConfigSnapshot:Refresh`/`UpdateAvailable` (:119, :138). No invented API found. One unusable API: F6.
