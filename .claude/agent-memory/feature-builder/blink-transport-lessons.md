---
name: blink-transport-lessons
description: Blink 0.18.9 facts that shape Net code (function On returns nothing, import ignores options, queue/warn shapes) plus Lune spec craft for generated modules (J025-B7, 2026-10-24)
metadata:
  type: feedback
---

- Blink `function X` generates `X.On(listener)` returning **nothing** (no disconnect) and pcalls the listener itself, warning once per error: a wrapper that answers must never raise. Event `On` returns a disconnect. A shared `AnswerListen` type that returns a disconnect fails luau-lsp against the real module.
  **Why:** J025-B7 Net-T0; luau-lsp caught it only when a typed spec required the real generated module.
  **How to apply:** type-check one spec against the real generated output, not only fakes.
- `import "./x" as Name` works; options in an imported file are ignored; Blink needs both ServerOutput and ClientOutput and an existing output folder; one blink run costs about 1 s (rokit shim), lune about 0.15 s.
- Load generated modules in Lune with `luau.load(source, {environment = {game = fake, _G = {}, task, Vector3 = roblox.Vector3, ...}})`; give each load its own `_G` (Blink guards a second instance through `_G._BLINK`). Fake remotes should pcall handlers and count an error as engine Output (P1: 5 lines each) so the unpatched control can fail.
- The framework gate wipes `.gate/` at start and runs specs in parallel: specs that write scratch files create each directory level themselves (`fs.writeDir` does not make parents).
- Gate `rules` check forbids `require(variable)` in src/: alias the resolver (`local resolve = require`) in spec require hooks.
- The pinned selene std lacks `math.isfinite` (engine and Lune have it): one `-- selene: allow(incorrect_standard_library_use)` line.
- A planted fault that survived (skip "player in Players") was not a redundant clause but a missing case (Session still "ready" after removal): before deleting a clause, ask which real sequence it alone guards. Related: [[parallel-gate-and-planted-faults]]
- (J025-B7b) Blink's function reply writer runs after the handler; a handler that yields past PlayerRemoving recreates `PlayersMap[Player]` for good. Patch step 5 drops the reply when `Player.Parent ~= Players`. An event `Fire(player)` after a yield has the same leak (open follow-up).
- (J025-B7b) Luau new solver: an inline lambda passed where the type says `-> ()` may not return a value (bidirectional check), while a named fake with extra results passes. After a shared-type change, grep fakes in typed (engine) specs too.
- (J025-B7b) Text with `\n` or `\t` escapes that must stay literal in Luau: use the Edit tool; strings in a Bash heredoc Python script came out as real newlines and broke the file.
- (J025-R-Net-fix1) A per-packet guard bounds nothing in Blink: one packet holds up to 65,535 events (and unknown index bytes loop for free). The check belongs at the top of each dispatcher loop. Count a blocked sender in `reject`, not `allow`: a non-buffer payload raises before the loop, so `allow` never sees it.
- (J025-R-Net-fix1) QA plants anchor on exact code text (e.g. `if Current and not Current.allow(Player) then`): when moving a check, keep its text so the protected plant still means the same; a new early-return layer can make an older plant survive (allow dropping departed senders masked QA P03), so prefer the change that keeps every plant red.
- (J025-R-Net-fix3) Follow-up to the line above: keeping a plant red is not a reason to leave a hole open. Round 1 kept `allow` true for departed senders to save P03; review R2-1 showed that let one packet decode 65,535 events. Close the hole, then name the obsolete plant and its retarget (here: plant both sites with `all = true`) for QA in the hand-back.
- (J025-R-Net-fix3) Lint value bounds: count per call as Net's walk does (array 1 + n x inner, struct +1, merge joins the outer table, tuple = sum, tagged enum +1 tag, set 1 + flags); report at the innermost over-limit node with no size problem inside, so each event gets one line. Put safe cases exactly at the limit so over-count plants turn red too.
