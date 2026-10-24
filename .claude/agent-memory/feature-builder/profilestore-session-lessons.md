---
name: profilestore-session-lessons
description: ProfileStore 1.0.3 behaviours and save/receipt test lessons learned building the J025 Session block (2026-10-24)
metadata:
  type: project
---

Lessons from building Session over vendored ProfileStore 1.0.3 with a Lune FakeWorld (J025-B6, 2026-10-24).

- `EndSession` fires `OnSessionEnd` synchronously (inside the spawned SaveProfileAsync) before the save lands; a later `OnAfterSave` still fires with `LastSavedData`. Mark own ends before calling it.
- ProfileStore signals fire newest-first; any guard that must hold "inside" `OnSessionEnd` needs `profile:IsActive()`, not only a status flag set by your own handler.
- Same key, same server, new `StartSessionAsync` while the old one is still in its DataStore call: the new call takes the old job's result; if that transform ran with the old Cancel true, the new call returns nil. Seen only under throttling.
- The message-based release ignores messages until `os.clock()` > 6 s: a fake clock that starts at 0 hides the fast steal path. Start fake `os.clock` high.
- ProfileStore queues UpdateAsync per key on one server, so an in-flight release blocks a same-server reload; the hole is the release's retry back-off (1, 2, 4 s), where the new load takes the stale record and the release then writes nothing (SessionLoadCount). Session must hold a same-server rejoin until the release's OnAfterSave (J025 R1 F1).
- There is no "release landed" event: any save in flight at leave also fires OnAfterSave. Name that window; closing it needs a vendor patch.
- Closed in J025 R3 by vendor patch P-1 (`OnAfterSave:Fire(LastSavedData, is_ending_session == true)`, 3 lines incl. doc and type). A stolen release still fires OnAfterSave (EditProfile writes nothing, the answer still lands), so the flag also clears a stolen release; a data-compare clear does not (review P2). Prove a vendor patch byte-compatible by old-vs-new: plant the upstream line back and compare whole stored records. FakeWorld plants apply once per server load: two servers → count 2.
- Luau new solver: a local reassigned in a loop does not narrow after `if not x then return end`; copy it into a fresh local first.
- Receipt confirm waits must wake only when `LastSavedData` holds their own id; waking on any save makes the second concurrent receipt wait a full retry.

**Why:** each one was found by a spec or a planted fault, not by reading; two cost a repair round.
**How to apply:** any save or purchase work on ProfileStore; when a planted fault survives, look for a second, unnamed guard doing the work (see [[planted-fault-double-guard]]).
