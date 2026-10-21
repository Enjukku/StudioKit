---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J012-T07
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-21

# Lessons: thumbnail and icon check tool (J012-T07)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | A planted fault (largest component share computed from the smallest component) survived: the three-subject test used three equal discs | A share or ratio test needs unequal parts, or largest and smallest are the same number | `tools/tests/test_thumb_check.py` `test_dominant_subject_share`; planted-fault run 11 of 12 caught before, 12 of 12 after |
| 2 | A test that reads each cited docs line and checks the number is still on it caught a wrong line number (planted :216 for :215) | When a tool cites docs file:line, add a test that opens the line and looks for the number; docs mirrors move | `SourcesTest.test_cited_lines` |
| 3 | The kit gate failed on generated-file drift (sync_harness, kb_index) from a parallel chat writing progression skills, while all 317 tests passed | A builder reports the gate line by line and names whose files fail; it does not run generators outside its scope | `python tools/verify.py` output, 2026-10-21 |
| 4 | Reusing look_check by import worked without changing it: `resolve_mask`, `mask_params`, `value_stats`, `components`, `resize_mask`, `base_record` covered everything; argparse `set_defaults(component=None, exclude=None, exclude_box=None)` satisfied its CLI-shaped helpers | Before forking a tool, check whether its CLI helpers accept a namespace you can fill with defaults | `tools/art/thumb_check.py` build_parser |
