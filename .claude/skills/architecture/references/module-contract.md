> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Templates for `architecture`. Source: owner research paper (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-01, A-09, A-10, A-18).

# Templates

## Invariant card (one per rule that must always hold)
| Field | Example |
| --- | --- |
| Rule | A reward is granted once per quest completion, even if the request is retried |
| Owner | QuestService (server) |
| Inputs | player session, quest id, completion id |
| Clock | server `time()` at acceptance |
| On failure | denied (already granted) or unavailable (save not ready); no partial grant |
| Test | replay the same completion id twice; save failure between check and grant |

## Module contract (top of every important module, as a comment block)
```lua
--[[
Owns:        <the facts only this module may change>
Requests:    <public functions callers may use; which ones yield>
Promises:    <what is true after success>
Fails:       <how it rejects: denied / unavailable / error; what stays unchanged>
Needs:       <modules and services it depends on>
Lifetime:    <server | session | character | match>; how it stops (Destroy, cleanup)
Notes:       <re-entrant? returns copies or internal tables?>
]]
```

## Feature plan (before code, for M and L work)
1. Player-facing goal (one sentence) and the invariants (cards above).
2. Owners: which module owns each new or changed fact; who may request changes.
3. Messages: client requests (intent names), server results, events for independent reactions.
4. Data: definitions (content tables), runtime state, saved state (and schema change, if any).
5. Placement: server-only, client-only or shared; download size of shared parts.
6. Lifetimes: what is created, who cleans it up, what happens on respawn, leave and round reset.
7. Failure paths: denied, unavailable, save failure, player leaves mid-action, object streamed out.
8. Tests: unit (pure rules), server (Luau Execution or Studio), multi-client cases, negative cases.
9. Locality check: list every file the feature changes and why each must change.

## Roblox layout (default; a game may differ, recorded in its overlay)
| Place | Holds |
| --- | --- |
| `ServerScriptService` | one server entry Script (`RunContext = Server`) that starts services in an explicit order; server-only services and rules |
| `ServerStorage` | server-only content (future levels, templates, secrets-free config) |
| `ReplicatedStorage` | shared modules the client needs: message names and types, definitions safe to show, pure calculations, packages |
| Client entry | one `Script` with `RunContext = Client` in ReplicatedStorage (Roblox's recommendation, `scripting/locations.md:36-40`) or one LocalScript in StarterPlayerScripts; it starts controllers in order |
| `ReplicatedFirst` | only the loading screen |
| Content source (files) | definitions and tuning as data, compiled or required by the owners |
Lifecycle per service or controller: `init()` (build state, no yields, no other module's work) → `start()` (connect events, begin loops) → `destroy()` (cleanup, safe to call twice).
