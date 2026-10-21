#!/usr/bin/env python3
"""SubagentStart hook: give a kit-role subagent a short pointer to its job context at start.

Kit tool (universal). Python 3 standard library only, no network. Spec: J016-T01, design-context §3b.

Reads the SubagentStart JSON on stdin (fields used: `agent_type`). When `agent_type` is a kit role
(a stem of .agents/roles/*.md) and knowledge/jobs/active.md lists open jobs, prints one JSON object:
    {"hookSpecificOutput": {"hookEventName": "SubagentStart", "additionalContext": "<text>"}}
The text holds the role's existing overlays, the line of its docs-map row, and per active job the
job block of tools/context_packet.py (canonical files with revisions) and the packet command to run.
At most CONTEXT_CAP characters: job file lines are dropped first, the command lines stay.
Otherwise (another agent, no active jobs) it prints nothing.

Never fails: on any error it exits 0 with no stdout and one line on stderr.

Usage (settings.json runs it; see tools/hooks/README.md):
    python tools/hooks/subagent_context.py [--root DIR]  < hook-input.json
Exit codes: always 0.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTEXT_CAP = 2000
EVENT = "SubagentStart"


def build_text(cp, root: Path, role: str, file_lines: int | None) -> str:
    """The context text; file_lines limits the job file lines per job (None = all)."""
    info = cp.role_info(root, role)
    overlays = ", ".join(f"`{o}`" for o in info["overlays"]) or "none"
    rows = info["docs_map"]
    docs = f"`{cp.DOCS_MAP}` L{', L'.join(str(r['line']) for r in rows)}" if rows else f"no row names this role in `{cp.DOCS_MAP}`"
    lines = [
        f"Studio Kit context for role {role} (tools/hooks/subagent_context.py, from {cp.ACTIVE_JOBS}).",
        f"Role overlays: {overlays}",
        f"Docs map row: {docs}",
    ]
    for job_id, title in cp.active_jobs(root):
        try:
            job = cp.job_info(root, job_id)
        except ValueError:
            lines += ["", f"Active job {job_id} · {title}: no matching folder under {cp.JOBS_DIR}/"]
            continue
        files = [line for line in job["lines"][2:] if line.strip()]  # drop the "## Job" heading and blank line
        if file_lines is not None and len(files) > file_lines:
            files = files[:file_lines] + ["- … more job files: the packet command lists them"]
        lines += ["", f"Active job {job['job']} · {title}", *files,
                  f'Run: python tools/context_packet.py packet "<your task>" --role {role} --job {job["job"]}']
    return "\n".join(lines)


def context_for(payload: dict, root: Path) -> str | None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import context_packet as cp

    role = payload.get("agent_type")
    if not isinstance(role, str) or role not in cp.role_names(root) or not cp.active_jobs(root):
        return None
    text = build_text(cp, root, role, None)
    limit = 24
    while len(text) > CONTEXT_CAP and limit >= 0:
        text = build_text(cp, root, role, limit)
        limit -= 1
    return text[:CONTEXT_CAP]


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    try:
        root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else ROOT
        raw = sys.stdin.buffer.read().decode("utf-8-sig")
        payload = json.loads(raw) if raw.strip() else None
        text = context_for(payload, root.resolve()) if isinstance(payload, dict) else None
        if text:
            out = {"hookSpecificOutput": {"hookEventName": EVENT, "additionalContext": text}}
            sys.stdout.write(json.dumps(out, ensure_ascii=True) + "\n")
    except Exception as error:  # a hook must never fail or block the subagent
        try:
            sys.stderr.write(f"subagent_context: {type(error).__name__}: {error}".replace("\n", " ")[:300] + "\n")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
