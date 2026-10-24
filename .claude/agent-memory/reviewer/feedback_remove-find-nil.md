---
name: remove-find-nil
description: table.remove(t, table.find(t, x)) removes the LAST element when x is absent (nil pos = #t); check registries that remove by find, esp. re-entrant close paths
metadata:
  type: feedback
---

`table.remove(list, table.find(list, entry) :: number)` is unsafe when the entry can be absent: Luau treats a nil position as `#t` and removes the last element (Lune 0.11.1 probe, J025 2026-10-24).

**Why:** J025 code review G1 F1: Screens.closeEntry used it; a handle.close() called inside build (before the entry was listed) removed the newest other screen and left a closed entry inserted forever.

**How to apply:** in any open/close or subscribe/unsubscribe registry, grep `table.remove(.*table.find` and ask "can close run before insert or twice?" Also check whether the registering call runs user code (build, callback) before the entry is registered. See [[end-path-callers]].
