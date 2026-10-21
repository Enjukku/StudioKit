#!/usr/bin/env python3
"""SessionStart hook (matcher `compact`): give the lead its job state back after compaction.

Kit tool (universal). Python 3 standard library only, no network. Spec: J016-T01, design-context §3b;
revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D R3: open tickets).

Reads the SessionStart JSON on stdin (field used: `source`; any value other than "compact" gives no
output, so a missing matcher does no harm). For each job in knowledge/jobs/active.md it prints the
`Status` row of the job card, the rows of its Gates table that have no date and the number of open
tickets in its ledger.md (status proposed, approved, working, blocked or needs-decision; the line is
left out when the ledger has no status column), then the line
`Re-load the orchestration skill before the next step.` Output is one JSON object:
    {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "<text>"}}
At most CONTEXT_CAP characters; the re-load line is always last.

Never fails: on any error it exits 0 with no stdout and one line on stderr.

Usage (settings.json runs it; see tools/hooks/README.md):
    python tools/hooks/compact_context.py [--root DIR]  < hook-input.json
Exit codes: always 0.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTEXT_CAP = 2000
EVENT = "SessionStart"
RELOAD = "Re-load the orchestration skill before the next step."
ROW_CHARS = 400
NO_DATE = {"", "-", "—", "–"}
OPEN_TICKET = {"proposed", "approved", "working", "blocked", "needs-decision"}  # templates/jobs/ledger.md statuses
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
SEPARATOR_RE = re.compile(r"^\|?[\s:|-]+\|?$")


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def card_state(text: str) -> tuple[str | None, list[str]]:
    """(Status row, Gates rows without a date) from a job card, rows verbatim."""
    lines = text.splitlines()
    status = next((l.strip() for l in lines if l.strip().startswith("|") and cells(l)[0] == "Status"), None)
    open_gates: list[str] = []
    in_gates = False
    header: list[str] | None = None
    for line in lines:
        heading = HEADING_RE.match(line.strip())
        if heading:
            in_gates = heading.group(1).strip().lower().startswith("gates")
            header = None
            continue
        stripped = line.strip()
        if not in_gates or not stripped.startswith("|") or SEPARATOR_RE.fullmatch(stripped):
            continue
        if header is None:
            header = [c.lower() for c in cells(stripped)]
            continue
        date_at = header.index("date") if "date" in header else 1
        row = cells(stripped)
        if (row[date_at] if date_at < len(row) else "") in NO_DATE:
            open_gates.append(stripped)
    return status, open_gates


def open_tickets(text: str) -> int | None:
    """Ledger rows whose `status` cell is an open status; None when no table has a status column."""
    count: int | None = None
    header: list[str] | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            header = None  # a table ended
            continue
        if SEPARATOR_RE.fullmatch(stripped):
            continue
        row = cells(stripped)
        if header is None:
            header = [c.lower() for c in row]
            continue
        if "status" in header:
            at = header.index("status")
            count = (count or 0) + (1 if at < len(row) and row[at].lower() in OPEN_TICKET else 0)
    return count


def clip(text: str) -> str:
    return text if len(text) <= ROW_CHARS else text[: ROW_CHARS - 1] + "…"


def context_for(payload: dict, root: Path) -> str | None:
    if payload.get("source", "compact") != "compact":
        return None
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import context_packet as cp

    jobs = cp.active_jobs(root)
    body = [f"Open jobs after compaction ({cp.ACTIVE_JOBS}; tools/hooks/compact_context.py):"]
    if not jobs:
        body.append("No open jobs are listed.")
    for job_id, title in jobs:
        body += ["", f"Job {job_id} · {title}"]
        try:
            folder = root / cp.JOBS_DIR / cp.resolve_job(root, job_id)
            status, gates = card_state((folder / "job-card.md").read_text(encoding="utf-8", errors="replace"))
        except (OSError, ValueError):
            body.append(f"No job card found for {job_id} under {cp.JOBS_DIR}/.")
            continue
        body.append(clip(status) if status else "No Status row in the job card.")
        body += [f"Open gate: {clip(row)}" for row in gates] or ["Open gates: none (every gate row has a date)."]
        ledger = folder / "ledger.md"
        tickets = open_tickets(ledger.read_text(encoding="utf-8", errors="replace")) if ledger.is_file() else None
        if tickets is not None:
            body.append(f"Open tickets: {tickets} (`{ledger.relative_to(root).as_posix()}`)")
    room = CONTEXT_CAP - len(RELOAD) - 1
    kept: list[str] = []
    for line in body:
        if len("\n".join(kept + [line, "… cut at the size cap; open the job cards."])) > room:
            kept.append("… cut at the size cap; open the job cards.")
            break
        kept.append(line)
    return "\n".join(kept + [RELOAD])[:CONTEXT_CAP]


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
    except Exception as error:  # a hook must never fail or block the session
        try:
            sys.stderr.write(f"compact_context: {type(error).__name__}: {error}".replace("\n", " ")[:300] + "\n")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
