# tools/progression/examples: two worked examples

> Author: progression-designer · claude-opus-5-5 · high · 2026-10-21. Built in J011-T08, refreshed in J011-T12; runs and charts regenerated in J011-T13 on sim 1.2.0, curves 1.0.0 and chart 1.2.0 (no quoted value changed). Python 3.11+, standard library only.

**Warning: these are teaching examples, not tuning.** Only the inputs labelled `published:M01` (the incremental flower pot) and `published:M04` (the RPG XP rule) come from a source. Every other number is an `EXAMPLE ASSUMPTION`, invented to show the method. Never copy a number from these files into a game. A "pass" is arithmetic against a window that the designer chose; it never shows that a game is fun.

## What is here

| Example | Read first | Model | Runs | Chart |
| --- | --- | --- | --- | --- |
| Bloom Valley (incremental) | `incremental/design.md` | `incremental/model.json` | `incremental/runs/` (5) | `incremental/chart.html` |
| Bloom Valley options B, C | `incremental/design.md` §8 | `incremental/options/model-B.json`, `model-C.json` | `incremental/options/runs/` (2) | `incremental/options/chart.html` |
| Lantern Woods (RPG) | `rpg/design.md` | `rpg/model.json` | `rpg/runs/` (5) | `rpg/chart.html` |
| Lantern Woods options B, C | `rpg/design.md` §8 | `rpg/options/model-B.json`, `model-C.json` | `rpg/options/runs/` (4) | `rpg/options/chart.html` |

Each `design.md` follows `progression-design` and `progression-craft`: the game in short → feeling timeline → exact trace → model players → results → walls and spikes → findings → options with one recommendation and an owner-decision line → charts → hand-off, playtest, limits. Wide tables are in the appendices.

**A 10-minute reading path:** `incremental/design.md` §1-2, §5, §7-8, then the timeline in `incremental/chart.html`. Then the same sections of `rpg/design.md` and `rpg/chart.html`.

## How to re-run (byte for byte)

Run from the repository root, with the paths exactly as below (each report records the model path as typed). Every run is exact mode (the default) and `--lean` (no event trace). Runs without `--horizon-s` use the model's horizon (incremental 3,600 s, RPG 18,000 s). Session runs use sessions x session length (30 x 1,200 s, 30 x 1,800 s); a run stops early when all goals are reached.

```text
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy greedy-roi --lean --out tools/progression/examples/incremental/runs/efficient.json
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy cheapest-eligible --lean --out tools/progression/examples/incremental/runs/explorer.json
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy buy-next-in-order --lean --out tools/progression/examples/incremental/runs/one-track.json
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy greedy-roi --sessions daily --horizon-s 36000 --lean --out tools/progression/examples/incremental/runs/daily.json
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy greedy-roi --sessions returning --horizon-s 12000 --lean --out tools/progression/examples/incremental/runs/returning.json
python tools/progression/sim.py tools/progression/examples/incremental/options/model-B.json --policy greedy-roi --sessions daily --horizon-s 36000 --lean --out tools/progression/examples/incremental/options/runs/B-daily.json
python tools/progression/sim.py tools/progression/examples/incremental/options/model-C.json --policy greedy-roi --sessions daily --horizon-s 36000 --lean --out tools/progression/examples/incremental/options/runs/C-daily.json

python tools/progression/sim.py tools/progression/examples/rpg/model.json --policy fight-best --lean --out tools/progression/examples/rpg/runs/efficient.json
python tools/progression/sim.py tools/progression/examples/rpg/model.json --policy grind-to-level --target-level 9 --lean --out tools/progression/examples/rpg/runs/careful.json
python tools/progression/sim.py tools/progression/examples/rpg/model.json --policy fight-best --skill struggling --horizon-s 21600 --lean --out tools/progression/examples/rpg/runs/struggling.json
python tools/progression/sim.py tools/progression/examples/rpg/model.json --policy fight-best --sessions daily --horizon-s 54000 --lean --out tools/progression/examples/rpg/runs/daily.json
python tools/progression/sim.py tools/progression/examples/rpg/model.json --policy fight-best --sessions returning --horizon-s 54000 --lean --out tools/progression/examples/rpg/runs/returning.json
python tools/progression/sim.py tools/progression/examples/rpg/options/model-B.json --policy fight-best --lean --out tools/progression/examples/rpg/options/runs/B-efficient.json
python tools/progression/sim.py tools/progression/examples/rpg/options/model-B.json --policy fight-best --skill struggling --horizon-s 21600 --lean --out tools/progression/examples/rpg/options/runs/B-struggling.json
python tools/progression/sim.py tools/progression/examples/rpg/options/model-C.json --policy fight-best --lean --out tools/progression/examples/rpg/options/runs/C-efficient.json
python tools/progression/sim.py tools/progression/examples/rpg/options/model-C.json --policy fight-best --skill struggling --horizon-s 21600 --lean --out tools/progression/examples/rpg/options/runs/C-struggling.json
```

Charts (they read the runs above):

```text
python tools/progression/chart.py tools/progression/examples/incremental/runs/efficient.json tools/progression/examples/incremental/runs/explorer.json tools/progression/examples/incremental/runs/one-track.json tools/progression/examples/incremental/runs/daily.json tools/progression/examples/incremental/runs/returning.json --out tools/progression/examples/incremental/chart.html --title "Bloom Valley (incremental example): five model players"
python tools/progression/chart.py tools/progression/examples/incremental/runs/daily.json tools/progression/examples/incremental/options/runs/B-daily.json tools/progression/examples/incremental/options/runs/C-daily.json --out tools/progression/examples/incremental/options/chart.html --title "Bloom Valley options A, B, C: the daily player"
python tools/progression/chart.py tools/progression/examples/rpg/runs/efficient.json tools/progression/examples/rpg/runs/careful.json tools/progression/examples/rpg/runs/struggling.json tools/progression/examples/rpg/runs/daily.json tools/progression/examples/rpg/runs/returning.json --out tools/progression/examples/rpg/chart.html --title "Lantern Woods (RPG example): five model players"
python tools/progression/chart.py tools/progression/examples/rpg/runs/efficient.json tools/progression/examples/rpg/runs/struggling.json tools/progression/examples/rpg/options/runs/B-efficient.json tools/progression/examples/rpg/options/runs/B-struggling.json tools/progression/examples/rpg/options/runs/C-efficient.json tools/progression/examples/rpg/options/runs/C-struggling.json --out tools/progression/examples/rpg/options/chart.html --title "Lantern Woods options A, B, C: efficient and struggling players"
```

The whole set takes about 2 minutes. To check, write every file to a scratch folder with the same commands (change only `--out`) and compare with `cmp`. Checked 2026-10-21: 16 runs and 4 charts, 0 differences. Every chart opens offline (no network file) and has an assumptions panel.

## Exact traces quoted in the design files

Not committed; re-run them when you need them. From `tools/progression/`:

```text
python -c "import curves as cv; from fractions import Fraction as F; r=F(107,100); print([(k, cv.wait_time(4*r**(k-1), 0, F(167,100)*k*(2 if k>=25 else 1)*(2 if k>=50 else 1))) for k in (1,2,3,4)])"
python -c "import sim; from fractions import Fraction as F; print(sim.duel({'hp':90,'damage':13,'interval_s':1,'first_s':0},{'hp':220,'damage':F(12),'interval_s':2,'first_s':2},'player_first')); print(sim.duel({'hp':180,'damage':F(21),'interval_s':F(3,2),'first_s':0},{'hp':800,'damage':F(12),'interval_s':F(5,2),'first_s':F(5,2)},'player_first'))"
```

The first prints the pot waits 400/167, 214/167, 11449/12525, 1225043/1670000 s. The second prints the king duel at level 6 with sword and armour (win at 16 s) and the struggling player's drake duel at level 15 with all gear (loss at 37.5 s). The simulator columns of `incremental/design.md` Appendix B come from the one-track run without `--lean` (from the repository root):

```text
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy buy-next-in-order --out <scratch>/one-track-full.json
```

## Labels

Every number in every `model*.json` is a value object `{"v": …, "src": …}`. A walk over the six model files finds 0 numbers without a `src`, and the simulator stops on a bare number anyway (`error: … has no provenance label`, exit 2).

| Model | `published` | `EXAMPLE ASSUMPTION` |
| --- | --- | --- |
| `incremental/model.json` | 10 (M01) | 65 |
| `incremental/options/model-B.json` / `model-C.json` | 10 (M01) | 66 / 70 |
| `rpg/model.json` | 3 (M04) | 94 |
| `rpg/options/model-B.json` / `model-C.json` | 3 (M04) | 97 / 100 |

## Size

The whole folder is about 2.7 MB (checked with `du -sb`, J011-T13). The incremental options page is about 672 KB (curves shared by several models are drawn once).
