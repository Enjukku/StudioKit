> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `data-saving`. Run an agent with only the skill and the brief; score the must-pass checks.

# data-saving evals

## E-01 Rename a field
Brief: "Rename saved `coins` to `gold` and split `inventory` into `weapons` and `pets`."
Must pass:
- Bumps `schemaVersion`; one pure migration step; offline test from an old save fixture; old keys removed only inside the migration.

## E-02 Coins every second
Brief: "Players earn 1 coin per second while standing in the zone; save it."
Must pass:
- Accumulates in memory; no store write per tick; saved on autosave, leave and shutdown.

## E-03 Load failure
Brief: "Data stores are down when a player joins. What happens?"
Must pass:
- Session marked errored; player may play on defaults; nothing from that session is saved; purchases refused with a message; player told.

## E-04 Teleport dupes
Report: "Players who teleport fast between places sometimes have items twice."
Must pass:
- Names the cause class (a second server read before the first saved) and the fix: a session lock taken in the loading `UpdateAsync`, owner check on every write, release in the final save.

## E-05 Admin tool
Brief: "Write an external script that gives 500 gems to 10,000 players through Open Cloud."
Must pass:
- Throttles itself (shared budget with game servers since 2026-07-29); respects the lock (only writes offline players or goes through the game); records an id so a rerun cannot double-grant; takes a snapshot first.
