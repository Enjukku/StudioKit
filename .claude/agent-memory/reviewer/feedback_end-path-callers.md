---
name: end-path-callers
description: When a contract fix adds a "who ended it" flag around a vendor callback (e.g. ProfileStore OnSessionEnd), list every vendor caller of that path, shutdown included
metadata:
  type: feedback
---

When a fix splits a vendor callback's meaning with an own-end flag (Session S12: kick only when Session did not end it), grep every place the vendor fires that callback, not only the case the finding named.

**Why:** J025 round 2 (2026-10-24): the F4 fix covered Session's own ends and the steal, but ProfileStore's BindToClose release (`SaveProfileAsync(profile, true, nil, "Shutdown")`) also fires OnSessionEnd, so the new rule kicked every present player with "session moved" at shutdown. Round 1 missed it too.

**How to apply:** for any "fires X when Y" rule, grep the vendor for the firing call sites (`OnSessionEnd:Fire`, `SaveProfileAsync(.., true`) and map each to a contract behaviour before marking the fix closed. See [[review-by-problem]].
