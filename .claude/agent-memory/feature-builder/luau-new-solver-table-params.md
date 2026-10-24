---
name: luau-new-solver-table-params
description: luau-lsp new solver rejects typed/frozen game tables against indexer param types; `{}` accepts them; annotate-then-freeze for data files; Lune harness pattern (J025-B2, 2026-10-24)
metadata:
  type: feedback
---

Before fixing a public param type for "any content table", probe it with luau-lsp on three inputs: an annotated
`{ [string]: Item }`, an unannotated `table.freeze({...})` literal, and an array.

- `{ [string]: { [string]: unknown } }`, `{ [K]: V }` and `{ read [unknown]: unknown }` all reject at least one
  (indexers are invariant; frozen literals become sealed `read` fields). `{}` accepts all three and rejects a number.
- A data file passed to a typed API (`{ [string]: Row }`) must be annotated first, then frozen:
  `local rows: { [string]: M.Row } = {...}; return table.freeze(rows)`. An unannotated frozen literal widens
  singletons (`"instant"` -> string) and fails.
- Lune harness: a test helper that `require("@lune/...")` breaks the type gate for every spec that requires it;
  keep the `@lune` requires in the spec (excluded from type check) and pass a loader function into the helper.
- On Windows, Python `open(p, "w")` / `write_text` writes CRLF; stylua (line_endings Unix) then fails the gate.
  Write with `newline="\n"` or run stylua after.

**Why:** J025-B2: two contract APIs (ContentTests Rows, Motion usage) did not compile on real data; found only
because Q9 required the usage example to compile.
**How to apply:** for any framework API that takes game data, write the usage spec with real typed data first.
Related: [[roblox-toolchain-probes]].
