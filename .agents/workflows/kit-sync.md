---
description: Send universal improvements from this game back to the Studio Kit (skills, rules, roles, tools, universal lessons), or pull a newer kit version into this game. Owner approves every change.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit workflow: universal.

# /kit-sync — this game ⇄ the Studio Kit

Run when `/improve` reports universal candidates, after a kit release, or on request. Lead at medium effort.

## Setup
`kit.json` in the game records `kit_version` and `kit_path` (local kit checkout, e.g. `../StudioKit`). Kit files are those listed by the kit's own `git ls-files`.

## Up: game → kit
1. **Candidates:** lessons and notes with `scope: universal` promoted since the last sync; edits to kit-owned files in this game (diff against the kit at `kit_version`).
2. **Clean:** strip game-specific facts (names, styles, paths, numbers that only fit this game). A candidate that cannot be made game-neutral stays in the game.
3. **Check:** no conflict with newer kit text; the kit's own tests pass in the kit checkout (`python tools/tests/...`, `python tools/sync_harness.py --check`).
4. **Owner review:** one digest: per change, what it improves for every future game. Apply only approved changes, in the kit checkout, as one commit per topic; bump `kit_version` (minor for new parts, patch for fixes).
5. Record in the kit's `CHANGELOG.md` and in this game's `kit.json`.

## Down: kit → game
1. Diff the kit between this game's `kit_version` and the kit's current version.
2. Apply kit-owned files; never overwrite game files (`knowledge/design/`, overlays, game code). Conflicts in kit-owned files the game edited go to the owner digest.
3. Run `python tools/sync_harness.py` and the gate; then `/integrate` if skills changed.
4. Update `kit.json` `kit_version`.
