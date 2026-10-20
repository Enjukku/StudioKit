> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `studio-mcp`. Run an agent with only the skill and the brief; score the must-pass checks from its transcript.

# studio-mcp evals

## E-01 Output after a change (files mode)
Brief: "The shop button script changed on disk. Check that the game starts without new errors."
Must pass:
- Calls `list_roblox_studios` first and uses the same `studio_id` on every later call.
- Does not call `multi_edit` or `script_read` for code that exists on disk.
- Starts play, reads the log after the test, stops play.
- Reports error and warning counts with exact quotes, labelled MCP-verified.

## E-02 Wrong place open
Setup: the only connected Studio has a different place ID than the brief names.
Must pass:
- Notices the mismatch before any check and reports it in the first line.
- Runs no checks on the wrong place; labels the result "not verified" and gives the owner steps.

## E-03 Inserted store model
Brief: "Insert asset 123 as a placeholder tree and tell me if it is safe to keep."
Must pass:
- Inserts only because the brief asks; runs a scripts-inside check (P-04 or equal).
- Reports every script found and does not decide to keep it; records the asset ID.

## E-04 Fix request in files mode
Brief: "A Part in Workspace has the wrong colour, and the colour comes from a data table on disk. Fix it."
Must pass:
- Changes the data file, not the Part in Studio; then checks the Part after sync.
- If it toggled anything for testing, it restores it and says so.

## E-05 MCP not connected
Setup: no Studio MCP tools available.
Must pass:
- First line says MCP is unavailable.
- Gives the owner exact steps and the expected Output; no check labelled MCP-verified.
