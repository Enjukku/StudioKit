> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `architecture`. Run an agent with only the skill and the brief; score the must-pass checks. Revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): E-05 and E-06 test the presentation contract the rebuilt book carries (R-19 to R-22, `references/presentation-contract.md`).

# architecture evals

## E-01 Burst-fire weapon
Brief: "Add a weapon that fires a three-shot burst."
Must pass:
- Invariants first (ammo per shot, stop on death or unequip, no new trigger during a burst, late-shot policy).
- Client sends one trigger request; server owns ammo and hits; results published with ids; locality check shows only definition, behaviour and tests change.

## E-02 Pets everywhere
Report: "Adding a new pet needs edits in 9 files including the save system."
Must pass:
- Finds the boundary problem (definitions not data, or save layer knows pet details); proposes moving pet stats into definitions and saving ids only; a refactor plan with an adapter, not a rewrite.

## E-03 Daily quest rewards
Brief: "Daily quests that give coins when finished."
Must pass:
- One owner for quest progress; reward as an award request with an id applied once by the data layer; server clock named; reset rule defined.

## E-04 Framework request
Brief: "Set up a full ECS framework and dependency injection before we build anything."
Must pass:
- Pushes back: plain modules first; ECS only for a measured large regular workload; asks what concrete problem it solves.

## E-05 Melee hit in a 12-player brawler
Brief: "Plan the melee hit for a third-person brawler, 12 players per server, phones first. The animator's timing list and the VFX and sound cue tables exist. Hits must feel heavy and fair."
Must pass:
- Attempt cue (swing, trail) on the client at once; the outcome layer (spark, hit sound, hit-stop) only on the server's `HitResolved`, never on a marker or `contact_candidate`; a rejected or missed swing shows no spark (R-19; AR-07; `references/worked-examples.md` A).
- Per-viewer column filled: the bystander's camera is never shaken or tinted by another player's hit; hit-stop runs only on the attacker's and target's clients, never on the server (R-20; AR-09).
- Marker and event names taken from the named timing-list revision, referenced by id; no guessed delay (`task.wait`) stands in for a marker (AR-08).
- Every intense channel the comfort service covers (shake, flash) names its reduced variant and the information it keeps, through one local read-only comfort service (R-22; AR-10; `references/presentation-contract.md` §4).

## E-06 Coin pickups at 20 per second
Brief: "A collecting simulator with a magnet upgrade: players pick up coins at up to 20 per second. Plan the pickup feedback and the coin counter."
Must pass:
- A merge window with one label (and one tick) per window; rate, burst and the cap and pool owned by one presenter, so callers never spawn bursts themselves (R-24; AR-12; `references/worked-examples.md` B).
- The counter shows the server balance as soon as it changes; the count-up is decoration; affordability (the buy button) uses the true balance at once, never the displayed value (R-21; AR-11).
