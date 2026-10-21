---
name: bash-heredoc-escapes
description: The Bash tool in this harness rewrites backslash escapes inside heredocs and echo strings; write code and JSON payloads with the Write tool
metadata:
  type: feedback
---

Do not generate Python source or JSON test payloads through Bash heredocs or `echo '...'` here: `"\\n"` became a real newline (SyntaxError in sync_harness.py) and `\\` in echoed JSON became `\` (invalid JSON). A long multi-file heredoc also failed to parse at all.

**Why:** J016-T01, 2026-10-21, Windows + Git Bash tool.

**How to apply:** write helper scripts and payload files with the Write tool (scratchpad), then run them; use the Edit tool for source changes with escapes.
