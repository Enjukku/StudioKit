---
name: admin-panel-lessons
description: Admin block lessons (J025-B8, 2026-10-24) - deprecated group API, client transport gap, sampled-log allocation, nil-in-table spec bug, planted-fault reason check
metadata:
  type: feedback
---

- `Player:GetRankInGroupAsync` is Deprecated (Player.yaml:1741-1746); use `GroupService:GetRolesInGroupAsync(userId, groupId)` and take the max `Rank` of `Roles` (order is not rank order). luau-lsp flags it as DeprecatedApi (a warning the gate does not count): read the analyzer's warnings too.
  **Why:** the frozen contract named the deprecated call; only the analyzer warning caught it.
  **How to apply:** grep each API you use for `Deprecated` in its class yaml, even when a contract names it.
- A server-cloned client (code copied into PlayerGui) cannot receive the transport functions the framework's "passed in, never looked up" rule needs: check how a cloned client gets its remotes before building; it is a contract gap (J025-B8 returned needs-decision with `Def.client: ModuleScript?`).
- A sampled log line built with string interpolation at the call site allocates on every refusal even when not emitted: check the time first, format only when due. A gcinfo flood spec caught it.
- `{ nil, a, b }` iterated with `for _, x in t` skips the nil slot (40 calls, not 60): use a sentinel value in spec tables.
- Planted faults: print each red's message; one fault went red at an unrelated earlier assertion (it also broke the success path). Edit the fault so only the guarded case changes. Related: [[parallel-gate-and-planted-faults]]
