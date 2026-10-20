> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `networking-security`. Run an agent with only the skill and the brief; score the must-pass checks.

# networking-security evals

## E-01 Sword hit
Brief: "When the client's sword touches an enemy, tell the server to deal 25 damage."
Must pass:
- Redesigns as intent (`requestSwing`); server checks range against server positions, cooldown and alive state, and computes damage.

## E-02 Shop buy
Brief: "Add `buyItem(itemId, price)` so the client can buy with coins."
Must pass:
- Drops the client price; server reads price from data; validation order N-02; atomic check-and-spend through the data layer; rate limit.

## E-03 Chest prompt
Brief: "Players open chests with a ProximityPrompt and get loot."
Must pass:
- Re-checks distance and chest state in the server handler; loot rolled on the server; once per chest per player.

## E-04 Anti-cheat config
Brief: "Put the max speed and teleport tolerance in a shared Config module in ReplicatedStorage."
Must pass:
- Refuses: thresholds are server-only (ServerScriptService or ServerStorage).

## E-05 Fast shooter
Brief: "We are making a fast arena shooter. How do we stop speed hacks and bad hit reg?"
Must pass:
- Considers Server Authority with its requirements and costs; notes remotes (rewards, purchases) still need N-02; movement checks otherwise.

## E-06 API key
Brief: "Call our leaderboard backend from the game with our API key."
Must pass:
- Uses the Secrets store and `GetSecret` in a header; never a key in code or the repo; minimum scopes.
