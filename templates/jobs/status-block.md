<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; revised 2026-10-21 (J016: built_on); revised by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (STATUS first, docs_read, lesson); revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021: belief check, BAR line, target-experience sentence) -->
# Hand-back (STATUS is the first line of every hand-back)

Format and rules: `rules/messages.md` §3. What the reader needs, no padding; detail goes in files.

STATUS: <done | blocked | needs-decision | failed>. <one-sentence outcome>

```text
<spec>
coverage:
  - <every item in scope>: <done | not done (why) | skipped (why)>
built_on: [<path>@rev<n>, ...]
files: [<paths>]
checks: {C1: <pass (evidence path or log line) | fail (why) | not verified (why)>, BAR: <pass (bar met: evidence) | fail or not verified (floor only: why)>}   # BAR when the brief's stop or AGENTS.md §4 sets a bar
decisions_made: [<open choices taken>]
proposals: [<PROPOSAL items, not built>]
questions: [{q: "<question>", default: "<what I will do if nobody answers>"}]
docs_read: [<docs pages and skill references you opened, path:lines>]
lesson:                             # optional; the lead writes the inbox draft from it at the gate or close
  type: <win | failure | owner-correction>
  cause: <one cause from rules/knowledge.md §8>
  layer: <the file or skill step that should change>
  what_happened: "<1-3 sentences; owner corrections word for word>"
  proposed_change: "<one sentence>"
</spec>
```
