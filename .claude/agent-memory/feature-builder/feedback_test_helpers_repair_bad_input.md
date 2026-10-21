---
name: test-helpers-repair-bad-input
description: Row-building test helpers can silently fix the invalid input a rejection test means to send; build bad rows by hand
metadata:
  type: feedback
---

Build invalid test rows by hand, not through the normalizing helper, and assert the exact number of rejected lines.

**Why:** J014-T06: a helper did `list(themes)`, turning the bad value "t.shop" into a valid list of characters; only the exact rejected-count assertion caught it.

**How to apply:** any validator test with a fixture helper (feedback tools, manual imports, save-data loaders). Related: [[planted-faults-unequal]].
