> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Source: local docs mirror `studio/mcp.md` (upstream 7400643) unless a row says otherwise. Re-check after each docs refresh.

# Studio MCP tools: what to use for what

Every call takes `studio_id` (from `list_roblox_studios`).

| Tool | Use it for | Trap |
| --- | --- | --- |
| `list_roblox_studios` | Find the Studio instance: name, instance ID, place ID | Local unsaved places have no place ID; two windows can share a name, so match the place ID |
| `get_studio_state` | Edit or Play, which data models exist | Call it before any play or edit-targeted call |
| `search_game_tree` | Find instances by path, class or keyword, flat JSON | Always set a path filter and a small depth; a full tree is huge |
| `inspect_instance` | All properties, attributes and a child summary of one instance | One instance per call; prefer it to a Luau dump |
| `script_read` / `script_search` / `script_grep` | Read code that exists only in the place (`studio` mode, plugins, inserted models) | In `files` mode read the files on disk instead. Grep returns ≤ 50 matches, search ≤ 10 |
| `multi_edit` | Edit or create a script (Edit data model) | **`studio` mode only.** In `files` mode it splits disk and Studio |
| `execute_luau` | Short probes in Edit, Server or Client (`datamodel_type`) | Plugin context: `require` gives separate module copies. Return one short string. No yields that can hang |
| `start_stop_play` | Start or stop a play-test | Edit-targeted tools fail while playing. Single player only from MCP (observed 2026-10) |
| `get_console_output` | Output log after a test | Long; for filters use `LogService:GetLogHistory()` in `execute_luau` |
| `screen_capture` | Visual review; optional camera position and look-at | Can leave the camera Scriptable; can time out in Play |
| `character_navigation` | Walk the character to a position or instance | Play mode only |
| `user_keyboard_input` / `user_mouse_input` | Key, text, click, scroll sequences, optionally aimed at a UI instance | Add `wait` steps between actions so the game can react |
| `subagent` (`explore`, `playtest`) | Let Roblox's in-Studio agent run a multi-step scenario | Playtest Agent is beta: false passes, 50-turn stop, daily cap (DF 2026-04-09) |
| `search_asset` / `insert_asset` | Creator Store or inventory assets by ID | Inspect inserted models for scripts; record kept IDs |
| `generate_mesh` / `generate_material` / `generate_procedural_model` / `wait_job_finished` | AI-generated assets | Only when the brief asks; art direction decides if it ships |
| `upload_image` / `store_image` | Upload images from URLs; load a local image as a reference | Uploads create real assets on the account; brief must allow it |
| `http_get` / `skill` | Roblox docs and Roblox's own how-to notes | Local mirror first; our skills win on conflict |

Removed: `set_active_studio` (2026-08-19). Code that calls it is outdated.

## Setup (once per machine; the owner does it, agents never edit settings)
1. Studio: **Assistant → … → Manage MCP Servers → Enable Studio as MCP server**. (Older notes say "Beta Features → Model Context Protocol Server": outdated.)
2. Client: **Quick connect** in the same panel lists installed clients (Claude Code, Codex CLI, Claude Desktop, Cursor, Gemini CLI, VS Code, Antigravity). Or the CLI: Windows `cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat`; macOS `/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP`. For Claude Code: `claude mcp add --transport stdio Roblox_Studio -- cmd.exe /c "%LOCALAPPDATA%\Roblox\mcp.bat"`.
3. Restart the client. A green indicator in Manage MCP Servers shows connected clients.
4. Not working: restart Studio and the client; check the path exists; check JSON commas.
