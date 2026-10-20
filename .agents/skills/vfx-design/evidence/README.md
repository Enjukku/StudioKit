> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-13

# Evidence library

The evidence lives outside the skill, in `knowledge/reference/vfx/` (synthesis, 2026-10-12/13). Every rule ID in
this skill traces to a row there through its R-ids and section cites (e.g. "R-124; 01 camera", "PD-03", "X-44").
Open it only to check a source or study detail, settle a conflict between rules, or update rules. Never load it for
routine design work.

| File in `knowledge/reference/vfx/` | Holds | Open when |
| --- | --- | --- |
| `README.md` | evidence rules (tiers, levels, PROPOSAL format, frames), file map, 20 highest-confidence rules | first, before any other evidence file |
| `00-sources.md`, `source-aliases.json` | register R-001..R-467 (title, author, year, tier, URL, read scope); input id → R-id map | checking a source's tier, date or scope; tracing a number into raw research |
| `01-elements.md` | element table (gameplay, shape, value, colour, timing, composition, camera); perception rows | checking an EL- or CA- rule |
| `02a-moments-action.md`, `02b-moments-reward-mood.md` | moment recipes (hits, blasts, breaks, abilities, warnings; rewards, reveals, movement, ambient, UI); paid-random-item rules | checking an MO- rule or a recipe row |
| `03-scene-rulebook.md` | placement rules V-01..V-89 | checking an SC- rule (its V-ids are in brackets) |
| `04-field-methods-flipbooks.md` | field methods; sheet, kitbash, cadence, tile-size, blending rules | checking an FB- rule |
| `05-juice-repetition-sync.md` | juice studies, repetition, sync numbers, P-01..P-15 | checking a JU- or T- rule |
| `06-mistakes-08-card-09-review.md` | mistakes M-01..M-94, card template, review R0-R14, fix order | checking an RV-, M- or CD- rule |
| `07-roblox-performance-accessibility.md` | Roblox feature table, budgets P01..P26, flash-safety and accessibility rules | checking an RB- rule, an engine limit or a flash rule |
| `10-genre-presets.md` | genre profiles | checking a preset in `effect-card-and-presets.md` §D |
| `11-glossary.md` | 239 terms | an unclear term |
| `12-gaps.md` | 96 open questions, each with a Roblox test | before trusting a [P] value; planning an owner test |
| `contradictions.md` | X rows (evidence conflicts), PD rows (start values to use), IF rows (integration fixes) | any contested number; two files disagree |

Raw research (two runs plus an independent package, with "Sources read" tables and verification logs) stays in the source game's repository (`knowledge/research/vfx-2026-10-12/`); it is not shipped with the kit and is optional. Go there only when a reference row is unclear or disputed and the folder exists.
Roblox engine truth: `knowledge/external/roblox-creator-docs/`.

Add evidence: add the source to `00-sources.md` with the next free R-id and tier, tag every number with its evidence
level, record any disagreement in `contradictions.md` (X row; newer and more direct evidence wins; a PD row names
the start value). Then update the one reference file that owns the rule ID (or SKILL.md for core rules and
guardrails), keep each fact in exactly one file, and re-run `evals/briefs.md`.
