---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J014-T06
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-21

# Lessons: feedback count tool (J014-T06)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | A bad-input test (themes given as a string) passed the line as valid: the test helper did `list(themes)`, which turned "t.shop" into a list of characters. Only the "rejected count = bad lines" assertion caught it | A test helper that normalizes fields can repair the bad input the test means to send; build invalid rows by hand, and assert the count of rejections, not only that one exists | `tools/tests/test_feedback_count.py` `test_bad_lines_rejected_good_lines_counted` |
| 2 | 12 planted faults (author vs item count, tag dedupe, overlap gate, union vs sum, both window edges, duplicate id, untagged in sampled, exit code, key leak, cross-source share, untagged as theme) were all caught on the first run; the share test used unequal sources (2 and 4 sampled authors) so a cross-source denominator could not hide | For a "never print X" rule, test every output path (markdown, JSON, --out file, stderr rejects, validate) with keys that also appear in rejected lines | planted-fault run in the J014-T06 hand-back |
| 3 | The kit gate failed on sync_harness drift and kb_index stale/lint from parallel jobs while all 355 tests passed | Report the gate line by line and name whose files fail | `python tools/verify.py`, 2026-10-21 |
