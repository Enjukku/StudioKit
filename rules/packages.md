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
