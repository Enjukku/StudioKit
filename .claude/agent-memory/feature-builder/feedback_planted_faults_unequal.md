---
name: planted-faults-unequal-parts
description: Planted-fault runs on kit Python tools; symmetric synthetic fixtures (equal discs) hide largest/smallest bugs
metadata:
  type: feedback
---

Run a planted-fault pass (copy the file, swap one expression, run the suite, restore) on every new kit tool, and use synthetic fixtures with unequal parts.

**Why:** in J012-T07 (2026-10-21) a "largest share" bug survived because the three-subject fixture used equal discs; also, a parallel chat's generated-file drift can fail `tools/verify.py` while every test passes. Report that line by line and do not run generators outside the brief.

**How to apply:** for any ratio or ranking measure, add one case where the parts differ in size; for docs-cited numbers, add a test that reads the cited line. Related: [[kit-tool-reuse-by-import]]
