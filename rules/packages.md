> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit rule: universal. J001 step 9. Sources: Roblox data store best practices (`knowledge/external/roblox-creator-docs/cloud-services/data-stores/best-practices.md:33-42`), owner research paper (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-21), `rules/owner-profile.md`.

# Choosing packages

Each game's chosen packages (transport, data, UI state, cleanup, signals) are listed in `knowledge/design/game-profile.md`. That list is a **default, not a mandate**: use, patch, fork or replace a package when that is better for the game, and record why.

## Adopt a package only if all are true
1. It removes a **concrete** risk or repeated work we have now (not "it might help later").
2. **Maintained:** a release or commit within the last 12 months, a known owner, issues answered. Write the dates you saw.
3. **License** allows commercial use; keep its notice.
4. **Small and known:** we can read its source; no `require` by asset id, no `loadstring`, no hidden HTTP; it pulls in few other packages.
5. **Replaceable:** our code reaches it through one game module (adapter), so swapping it touches one file. For saved data: we can read our data without it.
6. **Typed** for strict mode, or we add types at our adapter.

## Rules
- **One package per concern.** Never two transports, two state libraries or two save layers in one game.
- **Pin versions** (lock file) and update deliberately, one package per change, with the gate passing.
- **Record each package** in `knowledge/reference/<package>.md`: version, owner, license, what we use, update path, replacement cost, and any local patch.
- **Edits to a package** go in a pinned fork or a checked-in patch, never an undocumented edit the installer overwrites.
- **No frameworks for their own sake:** a service framework, event bus, dependency-injection layer or persistence library each adds a contract every agent must learn. The game's own small modules are often enough.
- A builder restricted to a feature's files reports a needed shared-package change to the lead; it does not edit the package itself.

## ProfileStore exception (J025-G1 D-2)
- **What:** ProfileStore (loleris, Apache-2.0) fails item 2 read literally: upstream's last commit is 2025-07-31 (about 15 months on 2026-10-24). The owner approved keeping it with our own pinned copy: "Okay, yeah, these are all fine, and acceptable for the framework." (J025-G1 D-2, 2026-10-24; `knowledge/jobs/J025-base-framework/decisions.md`).
- **How:** the framework vendors ProfileStore **1.0.3** at `roblox-game-framework/vendor/ProfileStore/` (source sha256 and copy date in its `PATCHES.md`); games get it only through `tools/install.py` (lock-checked), never through Wally. Only the Session block requires it.
- **Patches:** every change to the copy is a row in `vendor/ProfileStore/PATCHES.md` (date, change, why, upstream issue, covering test). Today: **P-1** (2026-10-24) `OnAfterSave` also passes `is_ending_session`, so Session holds a same-server rejoin until the real release lands; record format, keys, retries and timing unchanged.
- **Re-check when:** a data-loss or duplication bug is found in ProfileStore that we cannot patch (then closed door CD-2, our own lock, may reopen); upstream ships a new release (diff it against our copy and P-1, re-run Session's specs and hard tests before moving the pin); Roblox ships an engine session lock or changes DataStore semantics ProfileStore relies on; or once a year from 2026-10-24.
- **Package notes** for the framework's packages live in `knowledge/reference/libraries/` (one per package; item "Record each package" above).
