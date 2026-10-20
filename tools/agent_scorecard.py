#!/usr/bin/env python3
"""Agent scorecard for /agent-review: score each subagent type on how its runs went and on freshness.

Kit tool: universal (Studio Kit). Python 3.11+ standard library only. Read-only.

Agents scored: every role in .agents/roles/*.md and .claude/agents/*.md, plus every subagent type
seen in this project's Claude Code transcripts in the window (layout: see tools/improve_scan.py).

Per agent, over the last --days N:
  runs        subagent transcripts that started in the window
  failed      runs that did not end with a final report (last assistant turn was a tool call),
              or whose report says `status: failed`
  blocked     runs whose report says `status: blocked` or `status: needs-decision` (rules/company.md §5)
  corrected   runs followed by an owner correction (tools/improve_scan.py CORRECTION) in the parent
              session within 30 minutes of the run ending (an approximation; read the samples)
  error rate  tool errors / tool calls
  tokens      new tokens (input + cache writes + output), total and median per run
  freshness   role file last modified (git commit date, else file mtime) vs --since-release
              (the newest model or harness release date); older = stale; no date or no file = unknown

Score (0-100), only when the agent has runs:
  ok       30 x (runs neither failed nor blocked) / runs
  owner    30 x (1 - corrected / runs)
  errors   15 x max(0, 1 - error_rate / 0.15)          (15% tool errors or more = 0)
  tokens   10 x min(1, median of all agents' median tokens / this agent's median tokens)
  fresh    15 if fresh or unknown, 0 if stale
Runs < 3 marks the score low-evidence ("?"). No runs = no score (prune candidate?).

Usage:
  python tools/agent_scorecard.py [--days 30] [--since-release YYYY-MM-DD] [--json out.json]
                                  [--root REPO] [--projects-dir DIR]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from improve_scan import (  # noqa: E402
    CORRECTION,
    REPO,
    clean,
    is_owner_message,
    parse_ts,
    project_dir,
    read_meta,
    records,
    result_body,
    text_of,
)

STATUS = re.compile(r"\bstatus\b[*_`\s]*[:=-]?[*_`\s]*(blocked|failed|needs-decision|done)\b", re.I)
REPORT_TOOLS = {"SubagentHandback"}
CORRECTION_WINDOW = dt.timedelta(minutes=30)


def file_date(path: Path, repo: Path) -> dt.date:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            cwd=repo, capture_output=True, text=True, timeout=20,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        out = ""
    if out:
        try:
            committed = dt.date.fromisoformat(out)
        except ValueError:
            committed = None
        if committed:
            # Uncommitted edits after the last commit count as newer.
            mtime = dt.date.fromtimestamp(path.stat().st_mtime)
            return max(committed, mtime) if _dirty(path, repo) else committed
    return dt.date.fromtimestamp(path.stat().st_mtime)


def _dirty(path: Path, repo: Path) -> bool:
    try:
        out = subprocess.run(["git", "status", "--porcelain", "--", str(path)],
                             cwd=repo, capture_output=True, text=True, timeout=20).stdout
    except (OSError, subprocess.SubprocessError):
        return False
    return bool(out.strip())


def role_files(repo: Path) -> dict[str, Path]:
    """Agent name -> role file. The canonical .agents/roles source wins over the generated .claude copy."""
    found: dict[str, Path] = {}
    for folder in (repo / ".claude" / "agents", repo / ".agents" / "roles"):
        if folder.is_dir():
            for path in sorted(folder.glob("*.md")):
                if path.name.lower() != "readme.md":
                    found[path.stem.lower()] = path
    return found


def owner_corrections(root: Path, since: dt.datetime) -> dict[str, list[dt.datetime]]:
    stamps: dict[str, list[dt.datetime]] = {}
    for path in root.glob("*.jsonl"):
        hits = []
        for o in records(path):
            ts = parse_ts(o.get("timestamp"))
            if ts and ts >= since and is_owner_message(o):
                if CORRECTION.search(clean(text_of((o.get("message") or {}).get("content")))):
                    hits.append(ts)
        stamps[path.stem] = hits
    return stamps


def read_run(sub: Path) -> dict | None:
    meta = read_meta(sub)
    run = {
        "agent": str(meta.get("agentType") or "?").lower(), "desc": meta.get("description", ""),
        "session": sub.parent.parent.name, "start": None, "end": None, "tokens": 0, "tools": 0,
        "errors": 0, "last": None, "report": "", "error_samples": [],
    }
    seen: set = set()
    for o in records(sub):
        ts = parse_ts(o.get("timestamp"))
        if not ts:
            continue
        run["start"] = run["start"] or ts
        run["end"] = ts
        msg = o.get("message") or {}
        if o.get("type") == "assistant":
            usage = msg.get("usage") or {}
            if msg.get("id") not in seen and usage:
                seen.add(msg.get("id"))
                run["tokens"] += sum(usage.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "output_tokens"))
            blocks = [b for b in msg.get("content") or [] if isinstance(b, dict)]
            uses = [b for b in blocks if b.get("type") == "tool_use"]
            run["tools"] += len(uses)
            reports = [b for b in uses if b.get("name") in REPORT_TOOLS]
            texts = [b.get("text", "") for b in blocks if b.get("type") == "text" and b.get("text", "").strip()]
            if reports:  # background agents deliver their report through a hand-back tool
                run["last"] = "report"
                run["report"] = str((reports[-1].get("input") or {}).get("message", ""))
            elif uses:
                run["last"] = "tool"
            elif texts:
                run["last"] = "report"
                run["report"] = texts[-1]
        elif o.get("type") == "user":
            content = msg.get("content")
            for b in content if isinstance(content, list) else []:
                if isinstance(b, dict) and b.get("type") == "tool_result" and b.get("is_error"):
                    run["errors"] += 1
                    if len(run["error_samples"]) < 3:
                        run["error_samples"].append(re.sub(r"\s+", " ", result_body(b))[:90])
    if not run["start"]:
        return None
    statuses = [m.lower() for m in STATUS.findall(run["report"])]
    final = statuses[-1] if statuses else ""
    run["failed"] = run["last"] != "report" or final == "failed"
    run["blocked"] = not run["failed"] and final in ("blocked", "needs-decision")
    return run


def collect_runs(root: Path, since: dt.datetime) -> dict[str, list[dict]]:
    corrections = owner_corrections(root, since)
    by_agent: dict[str, list[dict]] = {}
    for sub in sorted(root.glob("*/subagents/*.jsonl")):
        run = read_run(sub)
        if not run or run["start"] < since:
            continue
        stamps = corrections.get(run["session"], [])
        run["corrected"] = any(run["end"] <= t <= run["end"] + CORRECTION_WINDOW for t in stamps)
        by_agent.setdefault(run["agent"], []).append(run)
    return by_agent


def summarize(runs: list[dict]) -> dict:
    n = len(runs)
    if not n:
        return {"runs": 0}
    tools = sum(r["tools"] for r in runs)
    return {
        "runs": n,
        "failed": sum(r["failed"] for r in runs),
        "blocked": sum(r["blocked"] for r in runs),
        "corrected": sum(r["corrected"] for r in runs),
        "tool_calls": tools,
        "errors": sum(r["errors"] for r in runs),
        "error_rate": (sum(r["errors"] for r in runs) / tools) if tools else 0.0,
        "tokens_total": sum(r["tokens"] for r in runs),
        "tokens_median": int(statistics.median(r["tokens"] for r in runs)),
        "error_samples": [s for r in runs for s in r["error_samples"]][:4],
    }


def score(stats: dict, fresh: bool | None, reference_tokens: float) -> int | None:
    """The formula documented in the module docstring."""
    n = stats.get("runs", 0)
    if not n:
        return None
    ok = 30 * (n - stats["failed"] - stats["blocked"]) / n
    owner = 30 * (1 - stats["corrected"] / n)
    errors = 15 * max(0.0, 1 - stats["error_rate"] / 0.15)
    median = stats["tokens_median"]
    tokens = 10.0 if median <= 0 or reference_tokens <= 0 else 10 * min(1.0, reference_tokens / median)
    freshness = 0 if fresh is False else 15
    return round(ok + owner + errors + tokens + freshness)


def build(repo: Path, projects_root: Path | None, days: int, since_release: dt.date | None,
          now: dt.datetime | None = None) -> dict:
    now = now or dt.datetime.now(dt.timezone.utc)
    since = now - dt.timedelta(days=days)
    root = project_dir(repo, projects_root)
    run_map = collect_runs(root, since) if root.is_dir() else {}
    files = role_files(repo)
    names = sorted(set(files) | set(run_map))
    stats = {name: summarize(run_map.get(name, [])) for name in names}
    medians = [s["tokens_median"] for s in stats.values() if s.get("runs") and s["tokens_median"] > 0]
    reference = statistics.median(medians) if medians else 0
    rows = []
    for name in names:
        s = stats[name]
        path = files.get(name)
        modified = file_date(path, repo) if path else None
        fresh = None if (modified is None or since_release is None) else modified >= since_release
        total = score(s, fresh, reference)
        flags = []
        if fresh is False:
            flags.append(f"role file last modified {modified} before release {since_release}")
        if path is None:
            flags.append("no role file in .agents/roles or .claude/agents (built-in or removed agent)")
        if not s.get("runs"):
            flags.append(f"no runs in {days} days (prune candidate?)")
        else:
            if s["runs"] < 3:
                flags.append("fewer than 3 runs: low evidence")
            if s["failed"]:
                flags.append(f"{s['failed']} of {s['runs']} runs failed or ended without a report")
            if s["blocked"]:
                flags.append(f"{s['blocked']} of {s['runs']} runs blocked or needs-decision")
            if s["corrected"]:
                flags.append(f"owner correction after {s['corrected']} of {s['runs']} runs")
            if s["error_rate"] > 0.15:
                flags.append(f"tool error rate {s['error_rate']:.0%}")
        rows.append({
            "agent": name,
            "role_file": path.relative_to(repo).as_posix() if path else None,
            "modified": modified.isoformat() if modified else None,
            "fresh": fresh,
            **s,
            "score": total,
            "low_evidence": bool(s.get("runs")) and s["runs"] < 3,
            "flags": flags,
        })
    rows.sort(key=lambda r: (r["score"] is None, r["score"] if r["score"] is not None else 0, r["agent"]))
    return {
        "window_days": days,
        "since": since.date().isoformat(),
        "since_release": since_release.isoformat() if since_release else None,
        "reference_tokens_median": reference,
        "agents": rows,
    }


def render(report: dict) -> str:
    lines = [f"# Agent scorecard, last {report['window_days']} days (since {report['since']})", ""]
    rel = report["since_release"] or "not given (freshness unknown)"
    lines += [f"Newest model/harness release: {rel}. Formula: tools/agent_scorecard.py header.", ""]
    lines += ["| Agent | Score | Runs | Failed | Blocked | Corrected | Err rate | Tokens total | Median tokens | Modified | Fresh |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in report["agents"]:
        fresh = {True: "yes", False: "STALE", None: "?"}[r["fresh"]]
        if r.get("runs"):
            sc = f"**{r['score']}{'?' if r['low_evidence'] else ''}**"
            lines.append(
                f"| {r['agent']} | {sc} | {r['runs']} | {r['failed']} | {r['blocked']} | {r['corrected']} | "
                f"{r['error_rate']:.0%} | {r['tokens_total']:,} | {r['tokens_median']:,} | {r['modified'] or '-'} | {fresh} |"
            )
        else:
            lines.append(f"| {r['agent']} | - | 0 | - | - | - | - | - | - | {r['modified'] or '-'} | {fresh} |")
    lines += ["", "'?' after a score = fewer than 3 runs. Corrections are an approximation; read the samples.", ""]
    for r in report["agents"]:
        if r["flags"] or r.get("error_samples"):
            lines.append(f"## {r['agent']} ({r['role_file'] or 'no role file'})")
            lines += [f"- {x}" for x in r["flags"]]
            lines += [f"- error sample: {x}" for x in r.get("error_samples", [])]
            lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--since-release", help="YYYY-MM-DD of the newest model or harness release")
    ap.add_argument("--json", help="also write the raw numbers to this file")
    ap.add_argument("--root", type=Path, default=REPO)
    ap.add_argument("--projects-dir", type=Path, default=None, help="default ~/.claude/projects")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    release = dt.date.fromisoformat(args.since_release) if args.since_release else None
    report = build(args.root.resolve(), args.projects_dir, args.days, release)
    print(render(report))
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=1, default=str), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
