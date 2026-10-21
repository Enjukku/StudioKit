#!/usr/bin/env python3
"""Score the context packet ranking on knowledge/evals/retrieval.jsonl.

Kit tool (universal). Standard library only.

Usage:
    python tools/eval_context.py [--cases FILE] [--save FILE] [--compare FILE] [--show N]

Case line: {"task": "...", "expect": ["path", "path#heading", ...], "note": "..."}
    "path" matches any section of that file; "path#heading" matches a section whose heading
    slug equals the given slug or starts with it plus "-" (so "rules/company.md#2" matches
    "## 2. Job sizes and owner gates").
Metrics per case: recall@5, recall@10 (share of expected items found in the top k) and MRR
(1 / rank of the first expected item, 0 if none in the ranked list). A case passes when
recall@10 is 1.0. `--compare` exits 1 if overall recall@10 drops below the saved run.
An expected path under the Roblox docs mirror (knowledge/external/roblox-creator-docs/) is
ranked in the packet's "Roblox docs" list instead of the kit-note list: a page by its rank among
the docs pages (top DOCS_DEPTH), an `_api-reference/` file by its rank among the API lines.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import context_packet as cp  # noqa: E402

CASES = "knowledge/evals/retrieval.jsonl"
DOCS_DEPTH = 10  # docs pages ranked for scoring; the packet shows the first cp.DOCS_PAGES
API_PREFIX = cp.DOCS_API_CLASSES.rsplit("/", 1)[0] + "/"


def load_cases(path: Path) -> list[dict]:
    cases = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        text = line.strip()
        if not text or text.startswith(("#", "//")):
            continue
        try:
            case = json.loads(text)
        except ValueError as error:
            raise ValueError(f"{path.name}:{number}: bad JSON ({error})") from None
        if not isinstance(case, dict) or not isinstance(case.get("task"), str) or not isinstance(case.get("expect"), list) or not case["expect"]:
            raise ValueError(f"{path.name}:{number}: needs a 'task' string and a non-empty 'expect' list")
        cases.append(case)
    return cases


def matches(expect: str, path: str, heading: str) -> bool:
    want_path, _, want_head = expect.partition("#")
    if want_path.strip() != path:
        return False
    if not want_head:
        return True
    want = cp.slugify(want_head)
    have = cp.slugify(heading)
    return have == want or have.startswith(want + "-")


def first_ranks(expect: list[str], ranked: list[tuple[str, str]]) -> list[int | None]:
    ranks: list[int | None] = []
    for item in expect:
        rank = next((i for i, (path, heading) in enumerate(ranked, start=1) if matches(item, path, heading)), None)
        ranks.append(rank)
    return ranks


def recall_at(ranks: list[int | None], k: int) -> float:
    return sum(1 for r in ranks if r is not None and r <= k) / len(ranks) if ranks else 0.0


def reciprocal_rank(ranks: list[int | None]) -> float:
    found = [r for r in ranks if r is not None]
    return 1.0 / min(found) if found else 0.0


def item_rank(item: str, ranked: list[tuple[str, str]], docs: list[str], api: list[str]) -> int | None:
    path = item.partition("#")[0].strip()
    if path.startswith(API_PREFIX):
        pool = api
    elif path.startswith(cp.DOCS_MIRROR + "/"):
        pool = docs
    else:
        return first_ranks([item], ranked)[0]
    return pool.index(path) + 1 if path in pool else None


def evaluate(root: Path, cases: list[dict]) -> dict:
    corpus = cp.Corpus(root)
    index = cp.DocsIndex.load(root)
    rows = []
    for case in cases:
        hits, _ = cp.rank(corpus, case["task"])
        ranked = [(h.path, h.heading) for h in hits]
        found = cp.roblox_docs(root, case["task"], DOCS_DEPTH, index, corpus, hits) if index else {"pages": [], "api": []}
        docs = [p["path"] for p in found["pages"]]
        api = [a["path"] for a in found["api"]]
        ranks = [item_rank(item, ranked, docs, api) for item in case["expect"]]
        wants_docs = any(item.startswith(cp.DOCS_MIRROR + "/") for item in case["expect"])
        wants_kit = any(not item.startswith(cp.DOCS_MIRROR + "/") for item in case["expect"])
        top = (docs + api if wants_docs else []) + ([f"{p}#{cp.slugify(h)}" for p, h in ranked[:10]] if wants_kit else [])
        rows.append(
            {
                "task": case["task"],
                "expect": case["expect"],
                "ranks": ranks,
                "recall@5": round(recall_at(ranks, 5), 4),
                "recall@10": round(recall_at(ranks, 10), 4),
                "mrr": round(reciprocal_rank(ranks), 4),
                "pass": recall_at(ranks, 10) == 1.0,
                "top": top,
            }
        )
    count = max(1, len(rows))
    overall = {
        "cases": len(rows),
        "passed": sum(1 for r in rows if r["pass"]),
        "recall@5": round(sum(r["recall@5"] for r in rows) / count, 4),
        "recall@10": round(sum(r["recall@10"] for r in rows) / count, 4),
        "mrr": round(sum(r["mrr"] for r in rows) / count, 4),
    }
    return {"overall": overall, "cases": rows}


def report(result: dict, show: int) -> str:
    out = ["| # | pass | R@5 | R@10 | MRR | ranks | task |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for i, row in enumerate(result["cases"], start=1):
        ranks = ",".join("-" if r is None else str(r) for r in row["ranks"])
        out.append(f"| {i} | {'yes' if row['pass'] else 'NO'} | {row['recall@5']:.2f} | {row['recall@10']:.2f} | {row['mrr']:.2f} | {ranks} | {row['task']} |")
    o = result["overall"]
    out.append("")
    out.append(f"overall: {o['passed']}/{o['cases']} pass · recall@5 {o['recall@5']:.3f} · recall@10 {o['recall@10']:.3f} · MRR {o['mrr']:.3f}")
    if show:
        for i, row in enumerate(result["cases"], start=1):
            if not row["pass"]:
                out.append(f"\ncase {i} missed {[e for e, r in zip(row['expect'], row['ranks']) if r is None or r > 10]}; top {show}:")
                out += [f"  {n}. {ref}" for n, ref in enumerate(row["top"][:show], start=1)]
    return "\n".join(out) + "\n"


def compare(result: dict, saved: dict) -> tuple[str, bool]:
    old_cases = {c["task"]: c for c in saved.get("cases", [])}
    out = ["", "vs saved run:"]
    for row in result["cases"]:
        old = old_cases.get(row["task"])
        if old is None:
            out.append(f"  new case: {row['task']}")
        elif old["recall@10"] != row["recall@10"] or old["mrr"] != row["mrr"]:
            out.append(f"  {row['task']}: R@10 {old['recall@10']:.2f} -> {row['recall@10']:.2f}, MRR {old['mrr']:.2f} -> {row['mrr']:.2f}")
    a, b = saved.get("overall", {}), result["overall"]
    for key in ("recall@5", "recall@10", "mrr"):
        out.append(f"  overall {key}: {a.get(key, 0):.3f} -> {b[key]:.3f} ({b[key] - a.get(key, 0):+.3f})")
    dropped = b["recall@10"] < a.get("recall@10", 0) - 1e-9
    out.append("  RESULT: recall@10 dropped" if dropped else "  RESULT: recall@10 held")
    return "\n".join(out) + "\n", dropped


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Score context-packet retrieval.")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--cases", type=Path, help=f"case file (default {CASES})")
    ap.add_argument("--save", type=Path, help="write the result as JSON")
    ap.add_argument("--compare", type=Path, help="saved JSON result to compare against")
    ap.add_argument("--show", type=int, default=5, help="top results to print for failing cases (0 = none)")
    args = ap.parse_args(argv)
    root = args.root.resolve()
    try:
        cases = load_cases(args.cases or root / CASES)
        result = evaluate(root, cases)
    except (OSError, ValueError) as error:
        print(f"eval_context: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(report(result, args.show))
    code = 0
    if args.compare:
        try:
            saved = json.loads(args.compare.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            print(f"eval_context: cannot read {args.compare}: {error}", file=sys.stderr)
            return 2
        text, dropped = compare(result, saved)
        sys.stdout.write(text)
        code = 1 if dropped else 0
    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        args.save.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"saved {args.save}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
