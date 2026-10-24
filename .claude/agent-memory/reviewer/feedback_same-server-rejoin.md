---
name: same-server-rejoin
description: Session-lock reviews must trace a rejoin to the SAME server in every phase (mid-load, mid-release); ProfileStore treats this server's own lock as already held
metadata:
  type: feedback
---

When reviewing code over ProfileStore (or any lock keyed by server JobId), trace "leave, then rejoin the same server" while the old load or the old release save is still in flight, not only the two-server cases.

**Why:** J025 Session r1 (2026-10-24): two blocking findings came from it, both proven in FakeWorld. (1) Rejoin while the leave save is retrying: `IsThisSession` is true, the new load takes the stale record and bumps SessionLoadCount, so the old release writes nothing: progress lost. (2) Rejoin while the first load is throttled: the second StartSessionAsync steals the cancelled call's job result and returns nil: degraded. QA's 25 acceptance rows and 16 planted faults covered steals, crashes and shutdown but no same-server rejoin.

**How to apply:** for each in-flight vendor call (load job, release save), ask "what does a new call for the same key on this server see?"; a short scratch Lune probe on the fake settles it. See [[end-path-callers]].
