---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
---
> Author: <reviewer role> · <model id> · <effort> · <date>
<!-- Template: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); frontmatter added by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3. One file per review in the job's reviews/ folder: reviews/<artifact>-rev<N>-<reviewer>.md. Format: rules/messages.md §6. Reviewers never edit the work. -->

# Review: <artifact> rev <N>, by <reviewer>

```text
<spec>
artifact: <path>@rev<N>
reviewer: <role>
looked_at_first: [<the artifact, captures, references opened before the maker's hand-back>]
findings:
  - {id: F1, class: blocking | recommendation | new request, where: "<frame, test, location>", expected: "...", observed: "...", evidence: "...", smallest_fix: "..."}
keep: [<what works; joins the protected list>]
verdict: fix-first | ready for the next review | ready for the owner
</spec>
```
