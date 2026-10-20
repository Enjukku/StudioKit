> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `architecture`. Run an agent with only the skill and the brief; score the must-pass checks.

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
