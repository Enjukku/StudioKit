#!/usr/bin/env python3
"""Feedback count tool: exact distinct-author counts per theme, per source, per time window.

The live-ops designer reads and tags player feedback; this tool does only the arithmetic and the warnings
(templates/live-ops/feedback-sort.md §A sampling counts, §C "distinct authors / sampled authors" and
"messages" columns). Counting rules (owner's live-ops research paper, feedback section; J014-T06):
  - One author counts once per theme per source per window, whatever the number of items or tags.
  - Message volume (items carrying the theme) is a separate intensity column.
  - Share = theme authors / sampled authors of the SAME source. Never across sources, never over DAU.
  - Sampled authors = distinct authors with >= 1 item in the window, tagged or not.
  - A source with no items in the window is "no data", never 0.
  - Cross-source overlap is "unknown" unless the sources share a key scheme (--same-key-scheme a,b); only
    then a combined distinct count is printed, labelled "distinct across <sources>".
  - Output never prints author_key values. No network, no model, no weighting, no rounding of counts.

Input: JSONL, one item per line (example: tools/liveops/items.example.jsonl).
  required: item_id (unique str), source (SOURCES), author_key (opaque str: pseudonym or hashed id),
            occurred_at_utc (ISO 8601 ending in Z), themes (list of theme id strings; [] = untagged)
  optional: severity (SEVERITIES), cohort (str), build (str), urgent (bool), excerpt (str, <= 280 chars)
  Unknown fields are kept and ignored. A bad line is reported with file and line number and excluded; the
  good lines are still counted; exit 1 if any line was rejected.

Data dir: env FEEDBACK_DATA_DIR, default <repo>/.tools/feedback-data/ (gitignored). An ITEMS path that does
not exist as given is looked up there.

CLI:
  python tools/liveops/feedback_count.py count ITEMS.jsonl [...] --start ISO --end ISO
         [--same-key-scheme a,b] [--json] [--out PATH]
  python tools/liveops/feedback_count.py validate ITEMS.jsonl [...]

Python 3.11+ standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TOOL_VERSION = "feedback_count/0.1.0"
SOURCES = ("in-game", "discord", "comments", "reviews", "support", "survey", "other")
SEVERITIES = ("low", "medium", "high", "critical")
REQUIRED = ("item_id", "source", "author_key", "occurred_at_utc", "themes")
EXCERPT_MAX = 280
# PROPOSAL (J014-T06 open choice): flag a theme in a source when one author wrote at least this many of its
# messages and at least half of them. Intensity warning only; it never changes a count.
LOUD_MIN_MESSAGES = 5


def data_dir() -> Path:
    env = os.environ.get("FEEDBACK_DATA_DIR")
    return Path(env) if env else ROOT / ".tools" / "feedback-data"


def parse_utc(text: str) -> datetime:
    """ISO 8601 with Z (or a bare YYYY-MM-DD for window bounds) -> aware UTC datetime. ValueError otherwise."""
    if not isinstance(text, str) or not text:
        raise ValueError("not a string")
    if len(text) == 10:
        dt = datetime.fromisoformat(text)
        return dt.replace(tzinfo=timezone.utc)
    if not text.endswith("Z"):
        raise ValueError("time must end in Z (UTC)")
    dt = datetime.fromisoformat(text[:-1] + "+00:00")
    return dt.astimezone(timezone.utc)


@dataclass(frozen=True)
class Item:
    item_id: str
    source: str
    author_key: str
    occurred_at: datetime
    themes: tuple[str, ...]
    urgent: bool
    severity: str | None


@dataclass
class Loaded:
    items: list[Item] = field(default_factory=list)
    rejected: list[str] = field(default_factory=list)  # "<file>:<line>: <reason>" (never an author_key)
    sources_in_files: set[str] = field(default_factory=set)


def _check(obj: object) -> Item:
    """One parsed JSON line -> Item. ValueError names the field, never echoes author_key."""
    if not isinstance(obj, dict):
        raise ValueError("line is not a JSON object")
    missing = [k for k in REQUIRED if k not in obj or obj[k] is None]
    if missing:
        raise ValueError(f"missing required field(s) {missing}")
    for k in ("item_id", "author_key"):
        if not isinstance(obj[k], str) or not obj[k].strip():
            raise ValueError(f"{k} must be a non-empty string")
    if obj["source"] not in SOURCES:
        raise ValueError(f"source {obj['source']!r} not in {list(SOURCES)}")
    try:
        when = parse_utc(obj["occurred_at_utc"])
        if len(obj["occurred_at_utc"]) == 10:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("occurred_at_utc must be an ISO 8601 time ending in Z") from None
    themes = obj["themes"]
    if not isinstance(themes, list) or not all(isinstance(t, str) and t.strip() for t in themes):
        raise ValueError("themes must be a list of non-empty strings")
    severity = obj.get("severity")
    if severity is not None and severity not in SEVERITIES:
        raise ValueError(f"severity {severity!r} not in {list(SEVERITIES)}")
    for k in ("cohort", "build"):
        if k in obj and obj[k] is not None and not isinstance(obj[k], str):
            raise ValueError(f"{k} must be a string")
    urgent = obj.get("urgent", False)
    if not isinstance(urgent, bool):
        raise ValueError("urgent must be true or false")
    excerpt = obj.get("excerpt")
    if excerpt is not None and (not isinstance(excerpt, str) or len(excerpt) > EXCERPT_MAX):
        raise ValueError(f"excerpt must be a string of at most {EXCERPT_MAX} characters")
    return Item(obj["item_id"], obj["source"], obj["author_key"], when,
                tuple(dict.fromkeys(t.strip() for t in themes)), urgent, severity)


def resolve(path: str) -> Path:
    p = Path(path)
    if p.exists() or p.is_absolute():
        return p
    return data_dir() / p


def load(paths: list[Path]) -> Loaded:
    """Read every file; reject bad lines (with file:line) and duplicate item_ids across all files."""
    out = Loaded()
    seen: dict[str, str] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            where = f"{path.name}:{n}"
            try:
                obj = json.loads(line)
            except ValueError:
                out.rejected.append(f"{where}: not valid JSON")
                continue
            try:
                item = _check(obj)
            except ValueError as err:
                out.rejected.append(f"{where}: {err}")
                continue
            if item.item_id in seen:
                out.rejected.append(f"{where}: duplicate item_id {item.item_id!r} (first at {seen[item.item_id]})")
                continue
            seen[item.item_id] = where
            out.items.append(item)
            out.sources_in_files.add(item.source)
    return out


def count(loaded: Loaded, start: datetime, end: datetime, same_key_scheme: tuple[str, ...] = ()) -> dict:
    """Exact counts for the window [start, end). Returns a JSON-ready dict without any author_key."""
    window = [i for i in loaded.items if start <= i.occurred_at < end]
    authors_by_source: dict[str, set[str]] = defaultdict(set)
    items_by_source: dict[str, int] = defaultdict(int)
    untagged_by_source: dict[str, int] = defaultdict(int)
    urgent_by_source: dict[str, list[str]] = defaultdict(list)
    theme_authors: dict[tuple[str, str], set[str]] = defaultdict(set)
    theme_messages: dict[tuple[str, str], int] = defaultdict(int)
    theme_author_msgs: dict[tuple[str, str], dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for i in window:
        authors_by_source[i.source].add(i.author_key)
        items_by_source[i.source] += 1
        if not i.themes:
            untagged_by_source[i.source] += 1
        if i.urgent:
            urgent_by_source[i.source].append(i.item_id)
        for t in i.themes:
            theme_authors[(t, i.source)].add(i.author_key)
            theme_messages[(t, i.source)] += 1
            theme_author_msgs[(t, i.source)][i.author_key] += 1

    sources = [s for s in SOURCES if s in authors_by_source]
    sampling = []
    for s in SOURCES:
        if s in authors_by_source:
            sampling.append({"source": s, "status": "data", "items": items_by_source[s],
                             "sampled_authors": len(authors_by_source[s]), "untagged_items": untagged_by_source[s]})
        elif s in loaded.sources_in_files:
            sampling.append({"source": s, "status": "no data in window"})

    themes = []
    for (t, s) in sorted(theme_authors, key=lambda k: (k[0], SOURCES.index(k[1]))):
        n_auth, sampled, msgs = len(theme_authors[(t, s)]), len(authors_by_source[s]), theme_messages[(t, s)]
        top = max(theme_author_msgs[(t, s)].values())
        flags = []
        if top >= LOUD_MIN_MESSAGES and 2 * top >= msgs:
            flags.append(f"one loud author: {top} of {msgs} messages from one author")
        themes.append({"theme": t, "source": s, "distinct_authors": n_auth, "sampled_authors": sampled,
                       "share": n_auth / sampled, "messages": msgs, "flags": flags})

    group = [s for s in same_key_scheme if s in authors_by_source]
    overlap: dict = {"same_key_scheme": list(same_key_scheme)}
    if len(same_key_scheme) < 2:
        overlap["status"] = "unknown"
        overlap["reason"] = "No shared key scheme declared (--same-key-scheme); counts are per source only"
        overlap["themes"] = []
    else:
        overlap["status"] = "checked"
        overlap["sources_with_data"] = group
        rows = []
        for t in sorted({t for (t, _s) in theme_authors}):
            per = [theme_authors.get((t, s), set()) for s in group]
            if not any(per):
                continue
            union = set().union(*per)
            multi = sum(1 for a in union if sum(a in p for p in per) >= 2)
            rows.append({"theme": t, "distinct_across": group, "distinct_authors": len(union),
                         "possible_cross_source_overlap": multi})
        overlap["themes"] = rows
        others = [s for s in sources if s not in same_key_scheme]
        if others:
            overlap["outside_scheme"] = others

    return {
        "tool": TOOL_VERSION,
        "window": {"start_utc": _iso(start), "end_utc": _iso(end), "rule": "start inclusive, end exclusive"},
        "dedup_rule": "author_key within source",
        "sampling": sampling,
        "themes": themes,
        "overlap": overlap,
        "urgent": [{"source": s, "item_ids": urgent_by_source[s]} for s in SOURCES if s in urgent_by_source],
        "rejected_lines": loaded.rejected,
    }


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _pct(x: float) -> str:
    return f"{x * 100:.1f} %"


def to_markdown(r: dict) -> str:
    w = r["window"]
    ov = r["overlap"]
    if ov["status"] == "unknown":
        overlap_cell = {s["source"]: "unknown (no shared key scheme)" for s in r["sampling"]}
    else:
        overlap_cell = {}
        for s in r["sampling"]:
            if s["source"] in ov["same_key_scheme"]:
                overlap_cell[s["source"]] = "checked: shared key scheme " + ", ".join(ov["same_key_scheme"])
            else:
                overlap_cell[s["source"]] = "unknown (not in the shared key scheme)"
    out = [f"# Feedback counts - {w['start_utc']} to {w['end_utc']} (start in, end out)", "",
           f"Tool: `{r['tool']}`. Counts are exact; author keys are never printed.", "",
           "## A. Sampling (counts)",
           "| Source | Items in window | Sampled authors (distinct, tagged or not) | Untagged items | Dedup rule | "
           "Cross-source overlap |",
           "| --- | --- | --- | --- | --- | --- |"]
    if not r["sampling"]:
        out.append("| (none) | no data | no data | no data | | |")
    for s in r["sampling"]:
        if s["status"] == "data":
            out.append(f"| {s['source']} | {s['items']} | {s['sampled_authors']} | {s['untagged_items']} | "
                       f"{r['dedup_rule']} | {overlap_cell[s['source']]} |")
        else:
            out.append(f"| {s['source']} | no data in window | no data | no data | {r['dedup_rule']} | "
                       f"{overlap_cell[s['source']]} |")
    out += ["", "## B. Urgent items (also counted in their themes)", "| Source | Item ids |", "| --- | --- |"]
    out += [f"| {u['source']} | {', '.join(u['item_ids'])} |" for u in r["urgent"]] or ["| (none) | |"]
    out += ["", "## C. Themes per source (share = theme authors / sampled authors of that source only)",
            "| Theme id | Source | Distinct authors / sampled authors | Share of sampled authors | "
            "Messages (intensity) | Flags |",
            "| --- | --- | --- | --- | --- | --- |"]
    for t in r["themes"]:
        out.append(f"| {t['theme']} | {t['source']} | {t['distinct_authors']} / {t['sampled_authors']} | "
                   f"{_pct(t['share'])} | {t['messages']} | {'; '.join(t['flags'])} |")
    if not r["themes"]:
        out.append("| (none) | | | | | |")
    out += ["", "## Cross-source overlap"]
    if ov["status"] == "unknown":
        out.append(f"Overlap: **unknown**. {ov['reason']}. No combined total is printed.")
    else:
        names = ", ".join(ov["same_key_scheme"])
        out += [f"Sources declared to share one key scheme: {names}.",
                "| Theme id | Distinct authors (distinct across sources) | Possible cross-source overlap "
                "(authors in 2+ sources) |", "| --- | --- | --- |"]
        for t in ov["themes"]:
            out.append(f"| {t['theme']} | {t['distinct_authors']} (distinct across {', '.join(t['distinct_across'])}) | "
                       f"{t['possible_cross_source_overlap']} |")
        if not ov["themes"]:
            out.append("| (none) | | |")
        if ov.get("outside_scheme"):
            out.append(f"\nOverlap with {', '.join(ov['outside_scheme'])}: unknown (not in the shared key scheme).")
    if r["rejected_lines"]:
        out += ["", f"## Rejected lines ({len(r['rejected_lines'])}, excluded from every count)"]
        out += [f"- {x}" for x in r["rejected_lines"]]
    return "\n".join(out) + "\n"


def _report_rejects(rejected: list[str]) -> None:
    for x in rejected:
        print(f"REJECTED {x}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Exact feedback counts per theme, source and window.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("count", help="count distinct authors and messages per theme, source and window")
    c.add_argument("items", nargs="+")
    c.add_argument("--start", required=True, help="UTC, inclusive (ISO with Z, or YYYY-MM-DD)")
    c.add_argument("--end", required=True, help="UTC, exclusive (ISO with Z, or YYYY-MM-DD)")
    c.add_argument("--same-key-scheme", default="", help="comma list of sources that share one author key scheme")
    c.add_argument("--json", action="store_true", help="print JSON instead of markdown")
    c.add_argument("--out", help="write to this file instead of stdout")
    v = sub.add_parser("validate", help="check items files; exit 1 if any line is rejected")
    v.add_argument("items", nargs="+")
    args = ap.parse_args(argv)

    paths = [resolve(p) for p in args.items]
    missing = [str(p) for p in paths if not p.is_file()]
    if missing:
        print(f"ERROR: file not found: {', '.join(missing)}", file=sys.stderr)
        return 2
    loaded = load(paths)

    if args.cmd == "validate":
        _report_rejects(loaded.rejected)
        print(f"{len(loaded.items)} good item(s), {len(loaded.rejected)} rejected line(s)")
        return 1 if loaded.rejected else 0

    try:
        start, end = parse_utc(args.start), parse_utc(args.end)
    except ValueError as err:
        print(f"ERROR: --start/--end: {err}", file=sys.stderr)
        return 2
    if not start < end:
        print("ERROR: --start must be before --end", file=sys.stderr)
        return 2
    scheme = tuple(dict.fromkeys(s.strip() for s in args.same_key_scheme.split(",") if s.strip()))
    bad = [s for s in scheme if s not in SOURCES]
    if bad or len(scheme) == 1:
        print(f"ERROR: --same-key-scheme needs 2+ sources from {list(SOURCES)}", file=sys.stderr)
        return 2

    result = count(loaded, start, end, scheme)
    text = json.dumps(result, indent=2) + "\n" if args.json else to_markdown(result)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        sys.stdout.write(text)
    _report_rejects(loaded.rejected)
    return 1 if loaded.rejected else 0


if __name__ == "__main__":
    sys.exit(main())
