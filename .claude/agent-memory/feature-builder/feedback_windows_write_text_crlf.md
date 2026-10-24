---
name: feedback-windows-write-text-crlf
description: Python Path.write_text / open("w") on Windows writes CRLF; the kit is LF everywhere (.gitattributes eol=lf) - write bytes or newline="\n" when scripting edits
metadata:
  type: feedback
---

When a scripted edit rewrites a kit file with `Path.write_text(s)` on Windows, every `\n` becomes `\r\n`: three LF
files turned fully CRLF in J020 rank-layers (2026-10-24); only `git diff` warnings ("CRLF will be replaced by LF")
showed it. The Edit/Write tools keep LF.

**Why:** `.gitattributes` has `* text=auto eol=lf` so `sync_harness --check` stays byte-exact; a CRLF file is churn and
can break byte-exact checks.

**How to apply:** in a scripted edit use `p.write_bytes(s.encode())` or `open(p, "w", newline="\n")`; after any
scripted edit count `b"\r\n"` in the touched files against `git show HEAD:<file>`. Related:
[[feedback-bash-heredoc-escapes]].
