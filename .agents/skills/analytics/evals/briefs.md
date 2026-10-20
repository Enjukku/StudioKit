> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `analytics`. Run an agent with only the skill and the brief; score the must-pass checks.

# analytics evals

## E-01 New shop
Brief: "We added a pet shop. Add analytics."
Must pass:
- Repeating funnel with a GUID per visit (open → view → buy); economy event on confirmed purchase with balance after; plan rows added; server-side module only.

## E-02 Per-hit logging
Brief: "Log a custom event every time a player hits an enemy."
Must pass:
- Refuses per-hit; aggregates per session or trip; checks the rate limit.

## E-03 Where do players quit?
Brief: "Where do new players quit?"
Must pass:
- Onboarding funnel from the dashboard first; names missing steps to add; segment fields on step 1.

## E-04 Test the starting reward
Brief: "Find out if a bigger starting reward helps retention."
Must pass:
- Config key with the default from content; `GetConfigForPlayerAsync` + `GetValue`; 14-60 days; minimum detectable effect; no early winner.
