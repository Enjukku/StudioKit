#!/usr/bin/env python3
"""Context and usage report: how big each session's context gets, and which sessions to fix first.

Kit tool: universal (Studio Kit). Python 3.11+ standard library only. Read-only. J022.

Every model call re-reads the whole context, so the cost of a session is about calls x context size.
This report shows, per main session and per subagent: calls (one per message id), the context at the
first call (start-up cost), the median and peak context per call, the total context read, images that
entered the context, and compactions. It reads the repository's transcript folder and every
worktree folder of it (`<slug>--claude-worktrees-*`), and subagents at any depth (workflow agents too).

Flags (peak is the owner's number, J023-D1; the others are PROPOSAL values, J022; change them per run):
  big context      median context per call over --median-k (300 k)
  no compaction    peak over --peak-k (500 k, the owner's session size, J023-D1) with no automatic compaction
  many images      a main chat with more than --images (20) images
  many calls       more than --calls (400) calls in one session or agent
  helper on Opus   a built-in helper agent (general-purpose, Explore, Plan) that ran on an Opus model

Usage:
  python tools/usage_report.py [--since YYYY-MM-DD | --days 7] [--json] [--top 15]
                               [--root REPO] [--projects-dir DIR]
                               [--median-k 300] [--peak-k 500] [--images 20] [--calls 400]

Exit codes: 0 ok, 1 no transcript folder for this project.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from improve_scan import REPO, parse_since, parse_ts, project_dir, read_meta, records  # noqa: E402

HELPERS = {"general-purpose", "Explore", "Plan"}


def project_dirs(repo: Path, projects_root: Path | None = None) -> list[Path]:
    """The repository's transcript folder plus the folders of its worktrees."""
    base = project_dir(repo, projects_root)
    found = [base] if base.is_dir() else []
    return found + sorted(p for p in base.parent.glob(base.name + "--claude-worktrees-*") if p.is_dir())


def images_in(content) -> int:
    n = 0
    for block in content if isinstance(content, list) else []:
        if not isinstance(block, dict):
            continue
        if block.get("type") == "image":
            n += 1
        elif block.get("type") == "tool_result":
            n += images_in(block.get("content"))
    return n


def stats(path: Path, since: dt.datetime) -> dict | None:
    """One transcript: calls, context per call, output, images, compactions. None when idle in the window."""
    seen, ctx, models = set(), [], collections.Counter()
    out = images = auto = manual = 0
    title, first = path.stem[:8], None
    for o in records(path):
        if o.get("type") == "custom-title":
            title = o.get("customTitle") or o.get("title") or title
        ts = parse_ts(o.get("timestamp"))
        if not ts or ts < since:
            continue
        first = first or ts
        msg = o.get("message") or {}
        if o.get("type") == "system" and o.get("subtype") == "compact_boundary":
            if (o.get("compactMetadata") or {}).get("trigger") == "manual":
                manual += 1
            else:
                auto += 1
        elif o.get("type") == "assistant":
            usage, mid = msg.get("usage") or {}, msg.get("id")
            if usage and mid and mid not in seen:
                seen.add(mid)
                ctx.append(sum(usage.get(k, 0) or 0 for k in
                               ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")))
                out += usage.get("output_tokens", 0) or 0
                models[msg.get("model", "?")] += 1
        elif o.get("type") == "user" and not o.get("isCompactSummary"):
            images += images_in(msg.get("content"))
    if first is None or not ctx:
        return None
    return {"title": title, "calls": len(ctx), "start": ctx[0], "median": int(statistics.median(ctx)),
            "peak": max(ctx), "read": sum(ctx), "out": out, "images": images, "auto_compact": auto,
            "manual_compact": manual, "model": models.most_common(1)[0][0], "first": first.isoformat()}


def flags(row: dict, limits: dict, main: bool, agent_type: str = "") -> list[str]:
    f = []
    if row["median"] > limits["median"]:
        f.append("big context")
    if row["peak"] > limits["peak"] and not row["auto_compact"]:
        f.append("no compaction")
    if main and row["images"] > limits["images"]:
        f.append("many images")
    if row["calls"] > limits["calls"]:
        f.append("many calls")
    if agent_type in HELPERS and "opus" in row["model"]:
        f.append("helper on Opus")
    return f


def scan(dirs: list[Path], since: dt.datetime, limits: dict) -> dict:
    sessions, agents = [], []
    for root in dirs:
        place = root.name.split("--claude-worktrees-")[-1] if "--claude-worktrees-" in root.name else "main checkout"
        for path in sorted(root.glob("*.jsonl")):
            row = stats(path, since)
            subs = []
            for sub in sorted((root / path.stem / "subagents").rglob("agent-*.jsonl")):
                s = stats(sub, since)
                if not s:
                    continue
                kind = read_meta(sub).get("agentType", "?")
                s.update(type=kind, workflow="workflows" in sub.parts, session=path.stem[:8], place=place,
                         flags=flags(s, limits, main=False, agent_type=kind))
                subs.append(s)
            if row:
                row.update(session=path.stem[:8], place=place, subagents=len(subs),
                           sub_read=sum(s["read"] for s in subs), flags=flags(row, limits, main=True))
                sessions.append(row)
            agents.extend(subs)
    return {"sessions": sessions, "agents": agents}


def by_kind(agents: list[dict]) -> list[dict]:
    groups = collections.defaultdict(list)
    for a in agents:
        groups[(a["type"], a["model"])].append(a)
    rows = [{"type": t, "model": m, "n": len(g), "calls": sum(a["calls"] for a in g),
             "median": int(statistics.median(a["median"] for a in g)), "read": sum(a["read"] for a in g),
             "flags": sorted({f for a in g for f in a["flags"]})} for (t, m), g in groups.items()]
    return sorted(rows, key=lambda r: -r["read"])


def k(n: int) -> str:
    return f"{n / 1e6:.1f} M" if n >= 1e6 else f"{n / 1e3:.0f} k"


def render(out: dict, since: dt.datetime, limits: dict, top: int) -> str:
    s, a = out["sessions"], out["agents"]
    read = sum(r["read"] for r in s) + sum(r["read"] for r in a)
    calls = sum(r["calls"] for r in s) + sum(r["calls"] for r in a)
    lines = [f"# Context and usage since {since.date()}", "",
             f"{len(s)} sessions, {len(a)} subagents, {calls} calls, {k(read)} context read in total. "
             f"Limits: median {k(limits['median'])}, peak {k(limits['peak'])}, images {limits['images']}, "
             f"calls {limits['calls']} (peak: owner J023-D1; others PROPOSAL, J022).", "",
             "## Sessions (largest first)", "",
             "| Place | Session | Calls | Start | Median | Peak | Read | Subagents (read) | Images | Compactions auto/manual | Flags |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in sorted(s, key=lambda r: -(r["read"] + r["sub_read"]))[:top]:
        lines.append(f"| {r['place']} | {r['title']} | {r['calls']} | {k(r['start'])} | {k(r['median'])} | "
                     f"{k(r['peak'])} | {k(r['read'])} | {r['subagents']} ({k(r['sub_read'])}) | {r['images']} | "
                     f"{r['auto_compact']}/{r['manual_compact']} | {', '.join(r['flags']) or '-'} |")
    lines += ["", "## Subagents by type and model", "",
              "| Type | Model | Agents | Calls | Median context | Read | Flags |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in by_kind(a)[:top]:
        lines.append(f"| {r['type']} | {r['model']} | {r['n']} | {r['calls']} | {k(r['median'])} | {k(r['read'])} | "
                     f"{', '.join(r['flags']) or '-'} |")
    counts = collections.Counter(f for r in s + a for f in r["flags"])
    lines += ["", "## Flags", ""] + [f"- {f}: {n}" for f, n in counts.most_common()] if counts else ["", "No flags."]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--since", help="YYYY-MM-DD (default: --days ago)")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    ap.add_argument("--top", type=int, default=15, help="rows per table")
    ap.add_argument("--root", type=Path, default=REPO, help="repository whose transcripts to read")
    ap.add_argument("--projects-dir", type=Path, default=None, help="default ~/.claude/projects")
    ap.add_argument("--median-k", type=int, default=300)
    ap.add_argument("--peak-k", type=int, default=500)
    ap.add_argument("--images", type=int, default=20)
    ap.add_argument("--calls", type=int, default=400)
    args = ap.parse_args(argv)
    dirs = project_dirs(args.root.resolve(), args.projects_dir)
    if not dirs:
        print(f"usage_report: no transcript folder for {args.root}", file=sys.stderr)
        return 1
    since = parse_since(args.since, args.days)
    limits = {"median": args.median_k * 1000, "peak": args.peak_k * 1000, "images": args.images, "calls": args.calls}
    out = scan(dirs, since, limits)
    if args.json:
        print(json.dumps({"since": since.isoformat(), "limits": limits, **out}, indent=1))
    else:
        print(render(out, since, limits, args.top), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
