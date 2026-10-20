#!/usr/bin/env python3
"""Weekly /improve digest: scan Claude Code transcripts for this project and print a compact digest.

Kit tool: universal (Studio Kit). Python 3.11+ standard library only. Read-only.

Reads (Claude Code transcript layout):
  ~/.claude/projects/<slug>/<session>.jsonl                       main sessions
  ~/.claude/projects/<slug>/<session>/subagents/<agent>.jsonl     subagent runs
  ~/.claude/projects/<slug>/<session>/subagents/<agent>.meta.json {"agentType", "model", "description"}
  <slug> = the repository path with every non-alphanumeric character replaced by "-".

Reports (since a date): owner messages (corrections flagged and shown in full), interrupts,
dismissed questions and rejected tool uses, tool errors clustered by tool and normalized message,
hook / gate / guard denials, repeated shell commands (automation candidates), slash commands,
tokens by model and by agent type. Never prints tool inputs other than normalized shell commands,
and never prints file contents.

Usage:
  python tools/improve_scan.py [--since YYYY-MM-DD | --days 7] [--json] [--max-chars 40000]
                               [--root REPO] [--projects-dir DIR] [--codex]

Exit codes: 0 ok, 1 no transcript folder for this project.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CORRECTION = re.compile(
    r"\b(no,|nope|not what|wrong|redo|again|i said|i told you|i asked|why did you|why is|doesn'?t work|"
    r"does not work|still (?:broken|wrong|not)|didn'?t|instead|stop|reject|ugly|"
    r"too (?:small|big|flat|much|long|many|slow)|worse|confus|frustrat|annoy|forgot|missing)\b",
    re.I,
)
REMINDER = re.compile(r"<system-reminder.*?</system-reminder>", re.S)
CD_PREFIX = re.compile(r"^(?:(?:cd |[A-Z]\w*=)\s*(?:\"[^\"]*\"|'[^']*'|\S+)\s*(?:&&|;)\s*)+")
# Absolute or home-relative paths only, so repo-relative commands (python tools/x.py) stay readable.
PATH = re.compile(r"[\"']?(?<![\w.\-])(?:[A-Za-z]:|\$\w+|~)?(?:[/\\][\w.\-]+)+[\"']?")
TAGS = re.compile(r"</?(?:pasted_content|command-[a-z]+|local-command-[a-z]+)[^>]*>")
NUMBER = re.compile(r"\d+")
# Hook, gate or guard refusals that show up as tool errors (PreToolUse hooks, permission rules, guard mods).
DENIAL = re.compile(
    r"(?:\bhook\b[^\n]{0,80}\b(?:block|den(?:y|ied)|refus)|PreToolUse[^\n]{0,80}|"
    r"\b[\w-]*guard: [^\n]{0,80}|\b\w+-gate: [^\n]{0,80}|permission[^\n]{0,30}denied[^\n]{0,60})",
    re.I,
)
SHELL_TOOLS = {"Bash", "PowerShell"}
QUESTION_TOOLS = {"AskUserQuestion"}
REJECTED = "The user doesn't want to proceed with this tool use"
DISMISSED = "User dismissed"
INTERRUPTED = "[Request interrupted"


def project_dir(repo: Path = REPO, projects_root: Path | None = None) -> Path:
    """Claude Code keeps transcripts in ~/.claude/projects/<repo path with non-alphanumerics as '-'>."""
    slug = re.sub(r"[^A-Za-z0-9]", "-", str(repo))
    return (projects_root or Path.home() / ".claude" / "projects") / slug


def parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        ts = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return ts if ts.tzinfo else ts.replace(tzinfo=dt.timezone.utc)


def text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def clean(text: str) -> str:
    text = TAGS.sub("", REMINDER.sub("", text))
    return re.sub(r"\s+", " ", text).strip()


def records(path: Path):
    with path.open(encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                yield obj


def read_meta(sub: Path) -> dict:
    meta_path = sub.with_suffix(".meta.json")
    if not meta_path.exists():
        return {}
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return meta if isinstance(meta, dict) else {}


def is_owner_message(o: dict) -> bool:
    if o.get("type") != "user":
        return False
    if o.get("turnOrigin") == "human":
        return True
    return (o.get("origin") or {}).get("kind") == "human" and not o.get("isSidechain")


def result_body(block: dict) -> str:
    content = block.get("content")
    return content if isinstance(content, str) else text_of(content)


def normalize_error(body: str) -> str:
    one = re.sub(r"\s+", " ", body).strip()
    return NUMBER.sub("N", PATH.sub("<path>", one))[:80]


def new_digest() -> dict:
    return {
        "sessions": [], "owner": [], "interrupts": 0, "dismissed": 0, "rejected": 0,
        "tool_errors": collections.Counter(), "denials": collections.Counter(),
        "commands": collections.Counter(), "slash": collections.Counter(),
        "tokens": collections.Counter(), "agents": collections.Counter(), "agent_tokens": collections.Counter(),
    }


def count_record(o: dict, out: dict, seen: set, tool_names: dict, agent_key: str | None) -> None:
    msg = o.get("message") or {}
    if o.get("type") == "assistant":
        mid = msg.get("id")
        usage = msg.get("usage") or {}
        if mid and mid not in seen and usage:
            seen.add(mid)
            total = sum(usage.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "output_tokens"))
            cached = usage.get("cache_read_input_tokens", 0) or 0
            model = msg.get("model", "?")
            out["tokens"][(model, "new")] += total
            out["tokens"][(model, "cache-read")] += cached
            if agent_key:
                out["agent_tokens"][agent_key] += total
        for block in msg.get("content") or []:
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            name = block.get("name", "?")
            if block.get("id"):
                tool_names[block["id"]] = name
            if name in SHELL_TOOLS:
                cmd = str((block.get("input") or {}).get("command", ""))
                cmd = CD_PREFIX.sub("", re.sub(r"\s+", " ", cmd).strip())
                out["commands"][PATH.sub("<path>", cmd)[:70]] += 1
    elif o.get("type") == "user":
        content = msg.get("content")
        if isinstance(content, str) and INTERRUPTED in content:
            out["interrupts"] += 1
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "text" and INTERRUPTED in block.get("text", ""):
                out["interrupts"] += 1
            if block.get("type") != "tool_result":
                continue
            body = result_body(block)
            tool = tool_names.get(block.get("tool_use_id", ""), "?")
            if DISMISSED in body or (tool in QUESTION_TOOLS and REJECTED in body):
                out["dismissed"] += 1
                continue
            if REJECTED in body:
                out["rejected"] += 1
                continue
            if block.get("is_error"):
                m = DENIAL.search(body)
                if m:
                    out["denials"][f"{tool}: {normalize_error(m.group(0))}"] += 1
                else:
                    out["tool_errors"][f"{tool}: {normalize_error(body)}"] += 1


def scan(root: Path, since: dt.datetime) -> dict:
    out = new_digest()
    for path in sorted(root.glob("*.jsonl")):
        title, first, owner_n, seen, tool_names = path.stem[:8], None, 0, set(), {}
        for o in records(path):
            if o.get("type") == "custom-title":
                title = o.get("customTitle") or o.get("title") or title
            ts = parse_ts(o.get("timestamp"))
            if not ts or ts < since:
                continue
            first = first or ts
            count_record(o, out, seen, tool_names, agent_key=None)
            if is_owner_message(o):
                text = clean(text_of((o.get("message") or {}).get("content")))
                if text and not text.startswith(INTERRUPTED):
                    owner_n += 1
                    m = re.match(r"/([a-z][\w:-]*)", text)
                    if m:
                        out["slash"][m.group(1)] += 1
                    out["owner"].append((ts, title, text))
        if first:
            out["sessions"].append((first, title, owner_n))
        for sub in sorted((root / path.stem / "subagents").glob("*.jsonl")):
            meta = read_meta(sub)
            kind = f"{meta.get('agentType', '?')} ({meta.get('model') or 'default'})"
            active, seen, tool_names = False, set(), {}
            for o in records(sub):
                ts = parse_ts(o.get("timestamp"))
                if not ts or ts < since:
                    continue
                active = True
                count_record(o, out, seen, tool_names, agent_key=kind)
            if active:
                out["agents"][kind] += 1
    return out


def flagged(out: dict) -> list[tuple]:
    return [(t, s, x) for t, s, x in out["owner"] if CORRECTION.search(x)]


def to_json(out: dict, since: dt.datetime) -> dict:
    return {
        "since": since.date().isoformat(),
        "sessions": [{"start": t.isoformat(), "title": s, "owner_messages": n} for t, s, n in sorted(out["sessions"])],
        "owner_messages": [
            {"time": t.isoformat(), "session": s, "text": x, "correction": bool(CORRECTION.search(x))}
            for t, s, x in out["owner"]
        ],
        "interrupts": out["interrupts"],
        "dismissed_questions": out["dismissed"],
        "rejected_tool_uses": out["rejected"],
        "tool_errors": dict(out["tool_errors"].most_common()),
        "denials": dict(out["denials"].most_common()),
        "repeated_commands": {k: v for k, v in out["commands"].most_common() if v >= 2},
        "slash_commands": dict(out["slash"].most_common()),
        "tokens_by_model": [{"model": m, "kind": k, "tokens": v} for (m, k), v in out["tokens"].most_common()],
        "agents": [
            {"agent": a, "runs": n, "new_tokens": out["agent_tokens"][a]} for a, n in out["agents"].most_common()
        ],
    }


def render(out: dict, since: dt.datetime, max_chars: int) -> str:
    lines = [f"# /improve digest since {since.date()}", ""]
    lines.append(
        f"Sessions: {len(out['sessions'])} · owner messages: {len(out['owner'])} · interrupts: {out['interrupts']}"
        f" · dismissed questions: {out['dismissed']} · rejected tool uses: {out['rejected']}"
    )
    lines += ["", "## Sessions", "| Start | Title | Owner msgs |", "| --- | --- | --- |"]
    lines += [f"| {t:%m-%d %H:%M} | {title[:60]} | {n} |" for t, title, n in sorted(out["sessions"])]
    lines += ["", "## Tokens by model (new = input + cache writes + output; cache-read is cheap)",
              "| Model | Kind | Tokens |", "| --- | --- | --- |"]
    lines += [f"| {m} | {k} | {v:,} |" for (m, k), v in out["tokens"].most_common()]
    lines += ["", "## Tokens by agent type", "| Agent (model) | Runs | New tokens |", "| --- | --- | --- |"]
    lines += [f"| {a} | {n} | {out['agent_tokens'][a]:,} |" for a, n in out["agents"].most_common()]
    lines += ["", "## Slash commands used"] + [f"- /{k}: {v}" for k, v in out["slash"].most_common()]
    lines += ["", "## Hook / gate / guard denials"] + [f"- {v}x {k}" for k, v in out["denials"].most_common(10)]
    lines += ["", "## Tool errors, clustered (top 15)"] + [f"- {v}x {k}" for k, v in out["tool_errors"].most_common(15)]
    lines += ["", "## Repeated shell commands (automation candidates, 5+ runs)"]
    lines += [f"- {v}x `{k}`" for k, v in out["commands"].most_common(15) if v >= 5]
    marked = flagged(out)
    lines += ["", f"## Owner messages flagged as correction ({len(marked)})"]
    lines += [f"- {t:%m-%d %H:%M} [{s[:30]}] {x[:400]}" for t, s, x in marked]
    lines += ["", "## Other owner messages (first 100 chars)"]
    lines += [f"- {t:%m-%d %H:%M} [{s[:30]}] {x[:100]}" for t, s, x in out["owner"] if not CORRECTION.search(x)]
    text = "\n".join(lines)
    return text if len(text) <= max_chars else text[:max_chars] + "\n\n[digest truncated at --max-chars]"


def parse_since(since: str | None, days: int) -> dt.datetime:
    if since:
        return dt.datetime.fromisoformat(since).replace(tzinfo=dt.timezone.utc)
    return dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--since", help="YYYY-MM-DD (default: --days ago)")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--max-chars", type=int, default=40000)
    ap.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    ap.add_argument("--root", type=Path, default=REPO, help="repository whose transcripts to scan")
    ap.add_argument("--projects-dir", type=Path, default=None, help="default ~/.claude/projects")
    ap.add_argument("--codex", action="store_true", help="scan Codex transcripts (stub)")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if args.codex:
        print("Codex transcript scan not implemented")
        return 0
    since = parse_since(args.since, args.days)
    root = project_dir(args.root.resolve(), args.projects_dir)
    if not root.is_dir():
        print(f"No transcripts at {root}", file=sys.stderr)
        return 1
    out = scan(root, since)
    if args.json:
        print(json.dumps(to_json(out, since), indent=2, ensure_ascii=False))
    else:
        print(render(out, since, args.max_chars))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
