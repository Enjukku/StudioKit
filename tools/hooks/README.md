# Hooks: context for every agent without relying on the briefer

> Author: feature-builder · claude-opus-5-5 · high · 2026-10-21 (J016-T01; design: `knowledge/jobs/J016-orchestration/design-context.md` §3b); revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D B6, B7, R2, R3, R4)

Three Claude Code hook scripts. The kit ships the scripts; **the owner turns them on** by pasting the snippet below into the project `.claude/settings.json` (agents never edit settings). All three use the Python 3 standard library only, make no network calls, finish in about 0.1 s, and never fail: on any error they exit 0, print nothing on stdout and one line on stderr, so the subagent or session goes ahead as if the hook were not there.

| Script | Event | What it does | Output when it acts |
| --- | --- | --- | --- |
| `subagent_context.py` | `SubagentStart` | For a kit role (the agent type equals a stem of `.agents/roles/*.md`) and each job in `knowledge/jobs/active.md`: the job id and title, the job's canonical files with revisions (the `--job` block of `tools/context_packet.py`; held-out files are never listed), the role's existing overlays, the line of its row in `knowledge/reference/roblox/docs-map.md`, the lines of its rows in `knowledge/design/precedents.md` and the vocabulary file, one line naming the context withheld on purpose (`rules/knowledge.md` §3), the line `Several jobs are open. Use the job your brief names; ignore the others.` when more than one job is listed, and the line `Run: python tools/context_packet.py packet "<your task>" --role <role> --job <job-id>`. Another agent type, or no active jobs: nothing. At most 2,000 characters (job file lines are cut first; the `Run:` lines stay). | `{"hookSpecificOutput": {"hookEventName": "SubagentStart", "additionalContext": "..."}}` |
| `compact_context.py` | `SessionStart`, matcher `compact` | After compaction: for each active job, the job card's `Status` row, the rows of its Gates table with no date and `Open tickets: <n>` from its `ledger.md` (statuses proposed, approved, working, blocked, needs-decision; left out when the ledger has no status column), then `Re-load the orchestration skill before the next step.` Any `source` other than `compact` gives nothing. At most 2,000 characters; the re-load line is always last. | `{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "..."}}` |
| `handback_check.py` | `SubagentStop` | For a kit role: if the final message's first non-empty line does not start with `STATUS:` (markdown marks such as `**` or `##` before it are allowed), or no line holds a `coverage:` field (YAML key, list item, bold or JSON key; the word in a sentence does not count), the subagent is sent back once with the reason "Hand-back must start with 'STATUS: done \| blocked \| needs-decision \| failed.' and include coverage (rules/messages.md §3)." It allows the stop when `stop_hook_active` is true (already sent back once), for other agent types, and when the message has no text. | `{"decision": "block", "reason": "..."}` |

The active-jobs file is kept by the lead: one line per open M or L job, `- <job-id> · <title>` (`knowledge/jobs/active.md`).

## Settings snippet (project `.claude/settings.json`)

Merge this `hooks` object into the file (keep any keys that are already there). No matcher on `SubagentStart` and `SubagentStop`: the scripts themselves check that the agent is a kit role, so a new role needs no settings change.

```json
{
  "hooks": {
    "SubagentStart": [
      {
        "hooks": [
          { "type": "command", "command": "python", "args": ["${CLAUDE_PROJECT_DIR}/tools/hooks/subagent_context.py"], "timeout": 10 }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          { "type": "command", "command": "python", "args": ["${CLAUDE_PROJECT_DIR}/tools/hooks/compact_context.py"], "timeout": 10 }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          { "type": "command", "command": "python", "args": ["${CLAUDE_PROJECT_DIR}/tools/hooks/handback_check.py"], "timeout": 10 }
        ]
      }
    ]
  }
}
```

## Windows notes (from code.claude.com/docs/en/hooks, read 2026-10-21)

- The snippet uses **exec form** (`args` present): Claude Code finds `command` on `PATH` and starts it with no shell, so paths with spaces need no quoting and `${CLAUDE_PROJECT_DIR}` is put in as plain text. On Windows, exec form needs `command` to resolve to a real executable such as a `.exe`; `.cmd` and `.bat` shims cannot be started without a shell. `python.exe` and the launcher `py.exe` are real executables.
- If `python` is not on `PATH`, or it opens the Microsoft Store, use the launcher: `"command": "py", "args": ["-3", "${CLAUDE_PROJECT_DIR}/tools/hooks/subagent_context.py"]`. On the owner's machine `where python` lists `...\WindowsApps\python.exe` first (an app alias for Python 3.11), then `Python313\python.exe`; both run these scripts (Python 3.10 or later).
- **Shell form** (no `args`) also works. Then wrap the placeholder in double quotes: `"command": "python \"${CLAUDE_PROJECT_DIR}/tools/hooks/subagent_context.py\""`. Shell form runs in Git Bash, or in PowerShell when Git Bash is not installed (`"shell": "powershell"` chooses PowerShell). Set `CLAUDE_CODE_GIT_BASH_PATH` if Git Bash is installed where Claude Code does not find it.
- Paths inside hook input arrive with backslashes on Windows. These scripts do not read path fields from the input; they find the repository from their own location.
- The scripts read stdin as UTF-8 bytes and write ASCII-only JSON, so the console code page does not matter.

## Facts the scripts rely on (same docs page)

- SubagentStart input has `agent_id` and `agent_type` ("the agent name that the matcher filters on"); it "can't block subagent creation" and its `additionalContext` is added "at the start of its conversation, before its first prompt".
- SessionStart input has `source` = `startup`, `resume`, `clear`, `compact` or `fork`; matcher `compact` fires after auto or manual compaction.
- SubagentStop input has `stop_hook_active`, `agent_id`, `agent_type`, `agent_transcript_path` and `last_assistant_message`; `decision: "block"` with a `reason` keeps the subagent running and gives it `reason` as its next instruction. Repeated blocks are capped at 8 in a row (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`).
- JSON on stdout is read only on exit 0; `additionalContext` over 10,000 characters is moved to a file with a 2,000-character preview. These scripts stay under 2,000 characters, so the full text always arrives.

## Before turning on `handback_check.py`

A subagent that hands back through a tool (for example a `SubagentHandback` call) can end with no final text; the script then allows the stop because it has nothing to judge. Try it once on a real job: if hand-backs arrive only through a tool, this hook adds nothing and can stay off.

## Tests

`python -m unittest tools.tests.test_hooks` runs each script as a subprocess on the fixture repo `tools/tests/fixtures/context/repo/`.
