---
description: Tailor the universal kit to this game. Reads the game profile, design notes and new owner decisions, then writes a short "for this game" overlay per skill and role, so every agent applies the game's style and locks on top of the universal craft. Owner approves the changes.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit workflow: universal. Revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D B5: taste log, precedents and vocabulary as inputs, `rules/knowledge.md` §7).

# /integrate — kit → this game

Run after the game profile is filled in, then weekly or after big design decisions. Lead at medium effort; drafting on Sonnet.

## Inputs
- `knowledge/design/game-profile.md`, `knowledge/design/decisions.md` (rows since the last run), design notes (art bible, UI style, audio/VFX direction, economy), `rules/owner-profile.md`.
- The vault rows filed since the last run (`rules/knowledge.md` §7): `knowledge/design/taste-log.md` (the owner's corrections, word for word), `knowledge/design/precedents.md` (accepted work per craft) and `knowledge/design/vocabulary.md` (names every craft uses).
- The last run's log `knowledge/logs/integrate/*.md` (what changed since).

## Steps
1. **Diff:** list design facts that are new or changed since the last run (with their decision IDs), and the new taste-log, precedent and vocabulary rows (with their dates and ids). A taste entry that repeats, or that the owner states as a rule, becomes an overlay line; a new precedent becomes a **References** line of its craft's overlay; a new name becomes a **Paths and tools** line where a craft must use it.
2. **Map:** for each kit skill and role, which facts change how it works in this game (style, references, locks, budgets, paths, tools, review order). Skip skills with nothing game-specific.
3. **Write overlays** `knowledge/overlays/<skill-or-role>.md` (type `overlay`, scope `game`, ≤ 60 lines each):
   - **Style and taste for this game** (do / don't, with the owner's words and decision IDs)
   - **Locked values** (only from the ledger; everything else marked PROPOSAL)
   - **References** (approved images, clips, notes by path)
   - **Paths and tools** specific to this game
   - **Overrides:** where this game deliberately differs from the universal skill, and why
   Overlays never copy universal skill text; they only add or override.
4. **Check:** every overlay fact cites a decision ID or a design note; no contradiction with another overlay; universal files untouched.
5. **Owner review:** one digest: per overlay, 1-3 lines of what changes for the agents ("VFX: anime style, toy debris, dark test place"). Apply only what the owner approves.
6. **Log** `knowledge/logs/integrate/YYYY-MM-DD.md`; regenerate indexes (`python tools/kb_index.py`).

## How agents use overlays
Every kit skill and role ends with: "Project overlay: if `knowledge/overlays/<name>.md` exists, read it after this file; it wins for this game." The lead names the overlay in briefs.
