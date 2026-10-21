---
name: same-moment-eval
description: When parallel chats edit the corpus, compare old vs new retrieval tools in the same minute, and test withholding on paths, not words
metadata:
  type: feedback
---

Score a retrieval change by running the old tool (from `git archive <rev>` into the scratchpad, `--root .`) and the new tool on the current tree back to back, with the same case file. A "before" run taken an hour earlier is not comparable when other fixers edit rules and skills in parallel (J016 G3, 2026-10-21: the old tool's MRR on the same cases moved 0.538 → 0.608 in 20 minutes with no tool change).

**Why:** the corpus is the other half of the measurement; parallel edits changed it under me.

**How to apply:** report old-vs-new at one timestamp, plus the historical baseline, and name content changes (renumbered sections, shortened skill descriptions) as the reason for drops the tool did not cause. For "never list X" checks on real repo text, assert on link targets and paths (and a path-mention regex), never on a bare word: visible notes legitimately use the word ("hidden tests"). Planted fault on the real case file: monkeypatch the filter off and count forbidden hits (counts only). Related: [[default-unchanged-goldens]].
