> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `performance`. Run an agent with only the skill and the brief; score the must-pass checks.

# performance evals

## E-01 "It lags in the city"
Must pass:
- Captures first (MicroProfiler frame colour and top scopes, or render stats) before proposing a fix.
- Names one bottleneck; one change; before and after numbers on the same scene.

## E-02 1,000 coins on the map
Brief: "Spawn 1,000 spinning coins around the map."
Must pass:
- One loop for all coins on the client (or a cheaper idea), not a script or tween per coin; Box collision with Can* off; reused mesh; server sends only pickups.

## E-03 Memory grows
Report: "After 20 minutes memory keeps rising."
Must pass:
- Uses Dev Console memory categories and/or Scene Analysis to find the category; checks connections, per-player tables, characters and animations; repeat test returns to baseline.

## E-04 New open world
Brief: "Design the map system for a big open world on phones."
Must pass:
- Streaming on with deliberate model modes; budgets from a named baseline device; join size check; far static scenery considered for SLIM with its limits.

## E-05 Parallel everything
Brief: "Make the game faster by putting all scripts in Actors with --!native."
Must pass:
- Refuses without a capture; explains when Parallel Luau and native code help and what they cost.
