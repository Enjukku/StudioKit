---
name: kit-python-tests
description: StudioKit tool tests are stdlib unittest; pytest is not installed on this machine (checked 2026-10-24)
metadata:
  type: reference
---

Briefs may say `python -m pytest tools/tests/...`, but no installed Python (3.11 WindowsApps, 3.13) has pytest (2026-10-24).
**How to apply:** run `python -m unittest tools.tests.<module>` from the kit root; the tests are unittest classes. Errors from `sync_harness.run` go to stderr, not the `out` buffer: assert on exit code or call `sh.load_kit` directly.
