---
name: luau-framework-lessons
description: Craft lessons from J025 framework blocks (charm-sync filtering, new-solver freeze typing, Lune engine seams, gate type-check rules)
metadata:
  type: feedback
---

- charm-sync 0.4.1 tracks state globally **by key**; subscriptions are per client. Per-player private data = one wire key per player ("name@UserId", getter returns only that entry), renamed in the send wrapper. Its own Heartbeat interval diffs every key and allocates per client every frame: turn it off (`config.interval = -1`) and flush only after a dirty effect fires.
  **Why:** the contract assumed value filtering or "one syncer per player" (the server module is a singleton); reading the package source settled it in minutes.
  **How to apply:** read package source before trusting a contract's package assumption; prove it with one spec plus a planted fault.
- Luau new solver: `table.freeze(x)` marks fields read-only, which breaks assignment to a read-write type (Charm `Update<T>`). Use `local freeze = table.freeze :: <T>(T) -> T`. `a<b<c>>` trips StyLua: alias the inner type.
- Lune lane for code that reads `game:GetService` at load: load the module with `luau.load(source, {environment = {game = fake, ...}})()` from the spec; keep `@lune/` requires in the spec so the fake file stays type-checked (the gate skips files containing "@lune/").
- Fake engines: give fake connections both `Disconnect` and `Destroy` (Janitor's default method for non-RBX tables is Destroy).
