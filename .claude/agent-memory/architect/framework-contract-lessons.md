---
name: framework-contract-lessons
description: Craft lessons from writing the J025 base-framework block contracts (2026-10-24): placement, generated-code error paths, typed handles, engine API traps
metadata:
  type: feedback
---

Lessons from J025-S3 (block contracts for the universal Roblox framework, 2026-10-24).

- Check the repo skeleton's Rojo project before writing placement: the test project mapped server-only code (Session, ProfileStore, Admin) under ReplicatedStorage. A placement table per block folder (ReplicatedStorage / ServerScriptService / ServerStorage) belongs in the contracts README.
  **Why:** server code under ReplicatedStorage replicates, and an "admin code absent on non-admin" test then proves nothing.
  **How to apply:** in any framework or package contract, name the service each folder goes to, and flag the require-style consequence of splitting trees.
- Read the generated transport code's reject path, not only its validation: Blink raises inside OnServerEvent (log flood, heartbeat 16.7 -> 42 ms under a bad-packet flood). The smallest fix was a deterministic post-generation patch checked by the "generated is current" gate step.
- Module-level singletons lose the game's data type; a typed handle returned by `start<T>(def)` keeps strict types without casts. Admin-style consumers that need to edit data go through methods on that handle (one writer).
- Engine traps seen: `Player:GetRankInGroup` and `LoadCharacter` are deprecated (use the Async forms); `Animator:GetTrackByAnimationId` returned nil after loads (cache tracks yourself); clients reuse the same track object when a server rig replays a clip (key marker connections by track object); `GuiService.ReducedMotionEnabled` already maps to the in-experience Settings toggle (no second setting).
- ProfileStore can be driven deterministically under Lune without a patch by loading its source per fake server with `luau.load(source, { environment = env })` (env gives game, task, os, script); see [[framework-contract-lessons]] for the J025 Session contract.
