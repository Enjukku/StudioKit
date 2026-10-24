---
name: game-template-lessons
description: J025-S7 game template facts - Rojo RunContext scripts, luau-lsp literal/freeze friction with framework types, Blink event Fire(nil), sourcemap order after codegen (2026-10-24)
metadata:
  type: feedback
---

- Rojo 7.7 `"emitLegacyScripts": false` makes `.server.luau`/`.client.luau` Scripts with RunContext Server(1)/Client(2); verify by building .rbxlx and reading RunContext back.
- New solver: a table literal passed to a generic framework function (`Net.answer<A...>`) must spell optional fields (`beforeReady = false`), and `table.freeze` makes fields read-only so a frozen config fails a writable type. Write literals inline or use `local freeze = table.freeze :: <T>(T) -> T`.
- Blink event with no Data generates `Fire(Value: nil)`: wrap it (`function() X.Fire(nil) end`) where a `() -> ()` is expected.
- A gate that generates code must write the sourcemap after codegen, or fresh games show "Unknown require" for the generated module.
- Never put spec modules in a Loader `Systems/` folder: in the test place the Loader would boot them as systems (the template gate fails it).
- Rojo `globIgnorePaths` `**/test/**` drops the files but keeps an empty `test` Folder in the place; add `**/test` too and check by building a .rbxlx and reading the tree (J025-T14).
- A game spec cannot reach a framework fake unless it is in the sourcemap: the test project must keep `test/` (the game project ignores it).
- Python edit scripts in a bash heredoc turn `\n` into a real newline in the written file; write edit scripts with the Write tool.
**Why:** each cost one gate run in J025-S7; the planted-fault run (10/10) proved the gate rules.
**How to apply:** any game template, Rojo project or framework wiring work. Related: [[blink-transport-lessons]]
