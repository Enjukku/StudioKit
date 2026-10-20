---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "kit phase 2, retrieval tooling"
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-20

# Retrieval evals: how to score the context packet

`retrieval.jsonl` holds cases: a real task and the files the work **actually needed**. `python tools/eval_context.py` runs the packet ranking (`tools/context_packet.py`) on each task and reports recall@5, recall@10 and MRR per case and overall. Spec: `rules/knowledge.md` §6.

## Case format

One JSON object per line. Lines starting with `#` or `//` are comments.

| Key | Content |
| --- | --- |
| `task` | The task as the owner or lead phrased it, not a copy of a heading |
| `expect` | Paths that the work needed: `path` (any section counts) or `path#heading` (heading slug, prefix allowed: `rules/company.md#2` matches `## 2. Job sizes and owner gates`) |
| `note` | Why these files; where the case came from (job id, session date) |

## Add cases from real tasks

1. At job end, list the notes and sections the agents **opened and used** (job ledger, hand-backs, the files cited in the result). Not the files the packet happened to return.
2. Write the owner's request as `task`, those paths as `expect` (2-4 items; prefer `path#heading` when one section holds the answer).
3. Add misses too: a case where an agent missed a needed file is the most useful case.
4. Keep cases that still point at existing files; when a note is superseded, point the case at its replacement.
5. Never tune ranking to one case (no task-specific words, paths or boosts in the tool). A change must help in general.

## Compare before and after a retrieval change

```text
python tools/eval_context.py --save tmp/eval-before.json     # on the unchanged tool
# change tools/context_packet.py
python tools/eval_context.py --compare tmp/eval-before.json  # per-case and overall deltas
```

| Result | Action |
| --- | --- |
| `RESULT: recall@10 held`, MRR same or better | keep the change |
| `RESULT: recall@10 dropped` (exit 1) | revert, or fix and re-run |
| a case newly fails | read its printed top results; fix the ranking or the note (missing headings, missing frontmatter), never the case |

A case passes when recall@10 is 1.0. Run the eval in `/improve` (weekly) and before and after any change to the packet tool, the search roots in `kit.json` (`context.search_roots`) or a large note move.
