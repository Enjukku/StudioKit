---
description: Convene 2–4 relevant specialist lenses in parallel, synthesize their findings, surface conflicts, then act on the agreed approach.
---

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20 (ported)

# /council: multi-lens consultation

Convene agents from the roster (`.agents/roles/README.md`, orchestration skill) on the owner's task. **Actually invoke them in parallel** with the harness's subagent tool. Statuses, hop limit and the decision digest follow `rules/company.md`.

## Step 1: Pick 2–4 (default 2; more only when the task truly spans more areas)

Choose the lenses the task needs. Typical pairs:

| Task class | Lenses (role + skill to load in the brief) |
| --- | --- |
| New system, authority, placement | architect (architecture skill) + researcher if an engine question is open |
| Economy, purchases, persistence | architect (datastores) + reviewer (remote security) |
| Performance, large worlds | architect (performance) + researcher + studio-operator if a measurement is needed |
| UI, HUD, menus | architect (UI) + researcher (mobile input facts) |
| Look, feel, motion, sound | art-director + the craft role (animator, vfx-designer, sound-designer) |
| Feature, loop, level design | game-designer + architect |

Model per tier (`kit.json`): **lead** for taste-critical or risky lenses, **craft** for most lenses, **mechanical** for pure lookups. Fewer than 2 lenses: no council, just route it. Tell the owner first: *"Convening council on: <task>. Lenses: <list>, <one-line reason each>."*

## Step 2: Invoke in parallel

Use the brief format in the orchestration skill. Tell each agent what the others cover. Each agent hands back a status block (`rules/company.md` §4-5).

## Step 3: Synthesize

Check the citations your decision rests on. Agreement forms the backbone. Resolve conflicts by precedence: `rules/` > ledger (`knowledge/design/decisions.md`) > engine docs > preference. Unlocked design choices are **owner questions**: add them to `knowledge/design/open-questions.md` and to the decision digest (`templates/jobs/decision-digest.md`). Agent agreement is never owner approval.

## Step 4: Present, then act

```
## Council: <task>
Agreed approach · Findings by lens (cited) · Conflicts → resolution · Owner questions · Proposed action
```

Proceed unless owner questions block the work or the owner only asked for advice. If the work is M or L size, it still needs its G1 gate first.

---

The owner's task follows.
