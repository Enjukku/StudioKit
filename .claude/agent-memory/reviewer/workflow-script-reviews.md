---
name: workflow-script-reviews
description: How to review the kit's saved job workflows (.agents/workflows/jobs/job-*.js): prove findings with the fake-agent harness scenarios, where defects cluster
metadata:
  type: feedback
---

Prove workflow-script findings by running them under the fake-agent harness, not only by reading them. From Python, `tools.tests.test_job_workflows.run(name_or_path, full(name, **args), scenario)` takes these scenario keys: `nullLabel` (an agent died), `statusLabel` + `status` (a step that did not finish), `blockLabelOnce` / `blockLabel` + `maker` (blocking findings for one maker). Planted faults go in a copy in the scratchpad, run by path.

**Why:** in J019 G3-P4 (2026-10-22), reading the code gave candidates. One harness run each turned them into proven sequences: a stale lineup was still judged when its recapture died, and a reviewer role was routed as a maker.

**How to apply:** where defects cluster:
- step results that are kept but never checked: check-ins, fix steps, recaptures (`keep(...)` with no `ok()` after it)
- `if (!rv)` checks that catch only null, so a blocked or failed review counts as a pass
- `roleOf()` routing that accepts reviewer roles as makers (job-stage.js routes every role in ROLE)
- result keys that differ between workflows for the same contract item

Mark old defects as pre-existing follow-ups by checking `git show <commit> -- <file>`.
