---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J011 lead
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J011 lead notes

## N1 Hidden-eval swap
The brief's three hidden cases (Hearthstone track, Clash of Clans bundle, survivor bias) are taught by the paper, so they are in the skills. Replaced with five new symptom briefs (`evals-hidden.md` H1-H5; H5 from a first-game owner ruling).

## N2 Gaps from T09 (hidden evals, 2026-10-21)
| # | Where | Gap | Action |
| --- | --- | --- | --- |
| G1 | sim.py float mode | a 3-coin sink absorbed by float rounding at 4e17 booked residual 0.0 with no `float_rounding` adjustment; the precision flag caught it, the ledger did not | tool ticket T11 |
| G2 | sim.py continuous mode | level-ups detected only at other events, so levels arrive in batches | tool ticket T11 |
| G3 | sim.py policies | `buy-next-in-order` with a producer never moves on; a producer priced 0 stops the run with an error | tool ticket T11 |
| G4 | sim.py schema | no reward granted on reaching a level (reward tracks need a stand-in) | tool ticket T11 |
| G5 | progression-design live-data §4 | no sample-size method for small games | fixed: planning estimate + Roblox MDE line |
| G6 | platform-policy rules §A | no link from "paid wheel returning the same currency" to the simulated-gambling maturity rule (`content-maturity.md:367`) | platform-policy follow-up list (with FC-R PP-1..PP-8, AN-1..AN-4, WN-1) |

## N3 platform-policy / analytics follow-ups (not in J011 scope)
FC-R lists PP-1..PP-8 (platform-policy), AN-1..AN-4 (analytics), WN-1 (whats-new) plus G6 above. Proposed as a separate kit ticket edited by the lead (FC-R question 4 default).
