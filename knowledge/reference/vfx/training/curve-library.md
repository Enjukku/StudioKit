---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: data agent · claude-sonnet-5-5 · medium · 2026-10-20

# Curve library: named S+A pro curve shapes (medoids, not averages)

Source: `output/vfx/training-dumps/emitters_study.jsonl`, S+A tier only (particle emitters dup=false, Beam, Trail). Rebuild: `python tools/vfx/curve_library.py` (also writes `content/vfx/curves.json` with exact keypoints, envelope and 2 alternates per curve). Each curve is the real medoid of a k-medoids cluster on 41 linear + 7 log-time points (t=.001 to 1); k chosen by silhouette in a preset range. Size/squash are shown normalised (value/max): multiply by peak studs. Shares are of that kind's n. Spark uses a non-uniform time axis (t=0,.01,.03,.06,.1,.2,.35,.5,.65,.8,.9,1) so early pops stay visible. `(+env)` = medoid carries envelope (random range) keypoints, see json.

## Curves per kind
### size (n=595, k=11, silhouette 0.805)
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| constant size | ████████████ | .00:1.00 1.00:1.00 | 32% (n=193) | flare/star 38, flame body 32, glow/halo 26, liquid/splash 17 | 0.7 | 3.856 | Ayato_Showcase |
| linear shrink | ████▇▇▆▅▃▂▂▁ | .00:1.00 1.00:.00 (+env) | 29% (n=171) | spark 41, flame body 24, core 22, streak/speedline 21 | 0.7 | 0.8219 | Ayato_Showcase |
| bump (early peak) | ▁▂▃▅█▇▆▅▄▃▂▁ | .00:.00 .10:1.00 1.00:.00 (+env) | 8% (n=46) | flare/star 25, spark 6, other 6, ember/spec 3 | 0.75 | 0.5 | Elemental_Guns_OPENSOURCE_ZRBLX |
| partial grow | ▅▅▅▅▅▆▆▇▇▇██ | .00:.59 .10:.63 .20:.67 .30:.71 .40:.75 .50:.79 .60:.84 .70:.88 .80:.92 .90:.96 1.00:1.00 (+env) | 7% (n=42) | smoke 14, slash/crescent 8, liquid/splash 6, ember/spec 3 | 0.55 | 3.375 | Astral_Sword |
| linear grow | ▁▁▁▁▂▂▃▅▆▇▇█ | .00:.00 1.00:1.00 | 6% (n=37) | flame body 16, liquid/splash 7, ring/shockwave 4, impact burst 4 | 0.75 | 5.6519 | StylizedFireballsTrails |
| start 60%, grow to full | ▆▆▆▆▇▇▇▇▇███ | .00:.76 1.00:1.00 (+env) | 6% (n=35) | flare/star 9, impact burst 7, glow/halo 4, ember/spec 4 | 0.7 | 7.7 | Elemental_Guns_OPENSOURCE_ZRBLX |
| S-curve grow | ▁▁▂▂▃▄▆▇▇███ | .00:.00 .10:.24 .20:.43 .30:.58 .40:.71 .50:.80 .60:.88 .70:.93 .80:.97 .90:.99 1.00:1.00 (+env) | 4% (n=22) | smoke 8, ring/shockwave 2, slash/crescent 2, core 2 | 0.5125 | 3.65 | FUGAAAA |
| grow from 38% | ▄▄▄▄▄▅▅▆▆▇██ | .00:.38 1.00:1.00 | 4% (n=21) | impact burst 6, smoke 6, wisp/swirl 3, slash/crescent 2 | 0.65 | 4.0625 | Zonito_Music_OS |
| ease-out grow | ▁▂▃▄▇▇██████ | .00:.00 .10:.79 .20:.92 .30:.96 .40:.98 .50:.99 .60:1.00 .70:1.00 .80:1.00 .90:1.00 1.00:1.00 (+env) | 3% (n=15) | liquid/splash 5, ground decal 4, smoke 3, spark 2 | 1.0 | 5.0 | Zonito_Music_OS |
| start big, partial shrink | █████▇▇▆▆▅▅▄ | .00:1.00 1.00:.47 (+env) | 1% (n=8) | streak/speedline 8 | 0.575 | 2.125 | Colouring_Practice |
| bump (mid peak) | ▁▁▁▂▂▄▅▇▆▄▃▁ | .00:.00 .55:1.00 1.00:.00 | 1% (n=5) | flare/star 3, ember/spec 1, spark 1 | 0.4 | 1.2375 | StylizedFireballsTrails |

### transparency (n=595, k=12, silhouette 0.826)
Spark = opacity (1-transparency); keypoints are raw transparency.
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| opaque hold | ████████████ | .00:.00 1.00:.00 | 50% (n=300) | flame body 58, spark 46, flare/star 45, streak/speedline 30 | 0.65 | - | Ayato_Showcase |
| fade in, hold, fade out | ▁▁▁▂▂▄▆█▆▄▂▁ | .00:1.00 .50:.00 1.00:1.00 | 9% (n=53) | flare/star 25, ember/spec 7, ring/shockwave 5, smoke 4 | 0.95 | - | Colouring_Practice |
| linear fade | ████▇▇▆▅▃▂▂▁ | .00:.00 1.00:1.00 | 9% (n=53) | liquid/splash 10, flame body 8, flare/star 7, spark 6 | 0.5 | - | Ayato_Showcase |
| faint (barely visible) | ▁▁▁▁▂▂▂▂▁▁▁▁ | .00:1.00 .16:.85 1.00:1.00 | 7% (n=44) | smoke 18, glow/halo 9, ember/spec 7, flare/star 3 | 0.9 | - | Ayato_Showcase |
| partial fade out | ▄▄▄▄▃▃▃▂▂▂▁▁ | .00:.62 1.00:1.00 | 5% (n=29) | smoke 9, impact burst 4, liquid/splash 4, glow/halo 3 | 1.0 | - | Zonito_Music_OS |
| shallow V (translucent dip) | ▁▁▂▂▃▄▃▃▂▂▁▁ | .00:1.00 .14:.61 1.00:1.00 | 4% (n=23) | smoke 8, ember/spec 4, ground decal 4, slash/crescent 2 | 0.9 | - | Ayato_Showcase |
| fade from translucent | ▇▆▆▆▆▅▅▄▃▂▂▁ | .00:.21 1.00:1.00 | 4% (n=21) | flare/star 5, slash/crescent 4, smoke 3, wisp/swirl 2 | 0.675 | - | Elemental_Guns_OPENSOURCE_ZRBLX |
| late fade | ██████▇▆▄▃▂▁ | .00:.00 .24:.00 1.00:1.00 | 3% (n=19) | flare/star 7, flame body 2, glow/halo 2, liquid/splash 2 | 0.9 | - | Elemental_Guns_OPENSOURCE_ZRBLX |
| fade in | ▁▁▂▄▅███████ | .00:1.00 .16:.00 1.00:.00 | 3% (n=18) | ember/spec 6, other 5, streak/speedline 3, flame body 2 | 0.675 | - | Zonito_Music_OS |
| late fade #3 | ███████▇▇▇▇▁ | .00:.00 .95:.16 1.00:1.00 | 3% (n=15) | flame body 4, ring/shockwave 4, slash/crescent 3, smoke 2 | 0.65 | - | StylizedFireballsTrails |
| late fade #2 | █████████▅▃▁ | .00:.00 .66:.00 1.00:1.00 | 2% (n=11) | liquid/splash 6, impact burst 2, flipbook burst 2, dark underlay/twin 1 | 0.375 | - | Zonito_Music_OS |
| fade in, hold, fade out #2 | ▁▁▂▃▅█████▅▁ | .00:1.00 .20:.00 .80:.00 1.00:1.00 | 2% (n=9) | other 4, liquid/splash 4, ember/spec 1 | 0.4 | - | Zonito_Music_OS |

### squash (n=52, k=4, silhouette 0.991)
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| constant | ████████████ | .00:1.00 1.00:1.00 | 52% (n=27) | streak/speedline 21, flare/star 2, smoke 2, spark 1 | 0.4689 | 0.35 | Ayato_Showcase |
| constant #2 | ▁▁▁▁▁▁▁▁▁▁▁▁ | .00:-1.00 1.00:-1.00 | 40% (n=21) | flare/star 9, streak/speedline 7, flame body 5 | 0.3 | 0.5 | Ayato_Showcase |
| pulse | ▅▅▅▆█▆▆▇▇███ | .00:.00 .11:1.00 .15:.40 1.00:1.00 | 4% (n=2) | streak/speedline 2 | 0.0875 | 3.0 | FUGAAAA |
| ramp up | ▅▅▅▆▇▇▇█████ | .00:.00 .10:.57 .20:.73 .30:.82 .40:.88 .50:.92 .60:.95 .70:.97 .80:.98 .90:.99 1.00:1.00 | 4% (n=2) | smoke 2 | 0.525 | 0.6 | FUGAAAA |

### beam_transparency (n=28, k=4, silhouette 0.756)
Spark = opacity (1-transparency); keypoints are raw transparency.
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| fade in, hold, fade out | ▁▃▆▇▇▇▇▇▅▃▂▁ | .00:1.00 .04:.10 .45:.10 1.00:1.00 | 39% (n=11) | beam 11 | - | - | Elemental_Guns_OPENSOURCE_ZRBLX |
| faint (barely visible) | ▁▁▁▁▁▂▂▃▂▂▁▁ | .00:1.00 .48:.74 1.00:1.00 | 29% (n=8) | beam 8 | - | - | FUGAAAA |
| linear fade | ███▇▇▆▄▃▂▁▁▁ | .00:.00 .58:.85 1.00:1.00 | 18% (n=5) | beam 5 | - | - | FUGAAAA |
| V glow (fade in, fade out) | ▁▂▃▄▇████▇▄▁ | .00:1.00 .12:.00 .75:.00 1.00:1.00 | 14% (n=4) | beam 4 | - | - | Astral_Sword |

### beam_width (n=28, k=3, silhouette 0.816)
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| widen #2 | ▅▅▅▅▅▅▆▆▇▇██ | .00:.50 1.00:1.00 | 36% (n=10) | beam 10 | - | 2.0 | Elemental_Guns_OPENSOURCE_ZRBLX |
| widen | ▁▁▁▁▂▂▃▅▆▇▇█ | .00:.00 1.00:1.00 | 32% (n=9) | beam 9 | - | 20.0 | FUGAAAA |
| taper to thin | ██████▇▇▇▆▆▆ | .00:1.00 1.00:.71 | 32% (n=9) | beam 9 | - | 3.2365 | Astral_Sword |

### trail_transparency (n=15, k=3, silhouette 0.777)
Spark = opacity (1-transparency); keypoints are raw transparency.
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| opaque hold | ████████████ | .00:.00 1.00:.00 | 40% (n=6) | trail 6 | 0.75 | - | StylizedFireballsTrails |
| steady translucent | ▅▅▅▅▅▅▅▅▅▅▅▅ | .00:.50 1.00:.50 | 33% (n=5) | trail 5 | 0.8 | - | Elemental_Guns_OPENSOURCE_ZRBLX |
| late fade | ██████████▁▁ | .00:.00 .87:.00 .89:1.00 1.00:1.00 | 27% (n=4) | trail 4 | 0.4 | - | Zonito_Music_OS |

### trail_widthscale (n=15, k=3, silhouette 0.862)
| name | spark | keypoints t:v | share | jobs (count) | life s | peak studs | src |
|---|---|---|---|---|---|---|---|
| linear shrink | ████▇▇▆▅▃▂▂▁ | .00:1.00 1.00:.00 | 67% (n=10) | trail 10 | 0.75 | 0.4187 | Flame_Beziers |
| bump (mid peak) | ▁▁▂▃▄▇█▇▆▄▃▁ | .00:.00 .12:.56 .23:.92 .34:1.00 .65:.76 1.00:.00 | 20% (n=3) | trail 3 | 0.3 | 0.4798 | FUGAAAA |
| hold then shrink | ██████▇▇▅▃▂▁ | .00:1.00 .52:.84 1.00:.00 | 13% (n=2) | trail 2 | 0.75 | 0.8531 | StylizedFireballsTrails |

### colour pattern (n=638; rule on first/last colour + luminance; medoid = nearest real sequence; RGB 0-255, first 6 keys)
| pattern | keypoints t:[r,g,b] | share | jobs (count) | src |
|---|---|---|---|---|
| constant colour | 0.00:[119,126,255] 1.00:[119,126,255] | 72% (n=460) | flare/star 88, spark 56, smoke 44, impact burst 42 | nnoonooooo |
| cycle (returns to start colour) | 0.00:[148,0,161] 0.20:[136,59,9] 1.00:[179,0,179] | 12% (n=77) | flame body 58, flare/star 5, ring/shockwave 4, streak/speedline 4 | StylizedFireballsTrails |
| hot to body (same hue, darker) | 0.00:[255,176,80] 0.73:[255,121,32] 1.00:[255,121,32] | 10% (n=65) | core 22, streak/speedline 19, ring/shockwave 4, ember/spec 4 | Ayato_Showcase |
| body to dark | 0.00:[255,203,71] 0.11:[255,203,71] 0.24:[113,255,84] 0.45:[20,59,22] 1.00:[3,17,7] | 3% (n=21) | streak/speedline 9, wisp/swirl 4, liquid/splash 3, spark 1 | Colouring_Practice |
| subtle drift | 0.00:[255,167,79] 0.73:[255,121,32] 1.00:[255,121,32] | 1% (n=9) | beam 7, streak/speedline 2 | Ayato_Showcase |
| tint toward white/bright | 0.00:[154,11,255] 0.22:[255,116,24] 1.00:[217,75,255] | 1% (n=6) | trail 6 | StylizedFireballsTrails |

## Pairings: (size curve + transparency curve) per job, top 3
n = S+A particle emitters of that job. Jobs with n<8 are anecdotes.
| job | n | #1 | #2 | #3 |
|---|---|---|---|---|
| flare/star | 95 | bump (early peak) + opaque hold (25, 26%) | constant size + fade in, hold, fade out (21, 22%) | linear shrink + opaque hold (15, 16%) |
| flame body | 75 | constant size + opaque hold (26, 35%) | linear shrink + opaque hold (22, 29%) | linear grow + opaque hold (8, 11%) |
| spark | 58 | linear shrink + opaque hold (39, 67%) | bump (early peak) + opaque hold (6, 10%) | constant size + partial fade out (3, 5%) |
| smoke | 46 | partial grow + faint (barely visible) (9, 20%) | constant size + shallow V (translucent dip) (4, 9%) | constant size + faint (barely visible) (4, 9%) |
| impact burst | 44 | linear shrink + opaque hold (12, 27%) | constant size + opaque hold (7, 16%) | grow from 38% + partial fade out (3, 7%) |
| streak/speedline | 43 | linear shrink + opaque hold (21, 49%) | constant size + opaque hold (5, 12%) | start big, partial shrink + opaque hold (4, 9%) |
| liquid/splash | 41 | constant size + linear fade (7, 17%) | constant size + opaque hold (4, 10%) | constant size + fade in, hold, fade out #2 (4, 10%) |
| other | 33 | linear shrink + opaque hold (15, 45%) | bump (early peak) + opaque hold (6, 18%) | linear shrink + fade in (5, 15%) |
| glow/halo | 32 | constant size + opaque hold (9, 28%) | constant size + faint (barely visible) (6, 19%) | constant size + linear fade (4, 12%) |
| ember/spec | 32 | linear shrink + fade in (6, 19%) | constant size + fade in, hold, fade out (5, 16%) | constant size + faint (barely visible) (5, 16%) |
| core | 26 | linear shrink + opaque hold (22, 85%) | S-curve grow + opaque hold (2, 8%) | bump (early peak) + opaque hold (1, 4%) |
| slash/crescent | 19 | partial grow + fade from translucent (4, 21%) | constant size + late fade #3 (3, 16%) | S-curve grow + faint (barely visible) (2, 11%) |
| ring/shockwave | 13 | constant size + fade in, hold, fade out (5, 38%) | linear grow + late fade #3 (4, 31%) | S-curve grow + opaque hold (2, 15%) |
| ground decal | 13 | constant size + opaque hold (5, 38%) | ease-out grow + shallow V (translucent dip) (4, 31%) | constant size + linear fade (1, 8%) |
| wisp/swirl | 12 | linear shrink + opaque hold (4, 33%) | constant size + faint (barely visible) (2, 17%) | grow from 38% + fade from translucent (2, 17%) |
| lightning/electric | 6 | constant size + opaque hold (6, 100%) |  |  |
| debris/chunks | 4 | linear shrink + opaque hold (4, 100%) |  |  |
| flipbook burst | 2 | S-curve grow + late fade #2 (2, 100%) |  |  |
| dark underlay/twin | 1 | S-curve grow + late fade #2 (1, 100%) |  |  |

## Pop check (size reaches >=60% of its max by t<=0.02)
Of the curves that reach 60% by t<=.02: true pop = start below 30% (a real jump); start 30-60% = partial jump; the rest start at >=60% already (constant size or shrink-only).
| set | n size curves | reach 60% by t<=.02 | true pop (start<30%) | partial (30-60%) |
|---|---|---|---|---|
| S+A | 595 | 425 (71%) | 3 (1%) | 3 (1%) |
| B+C | 245 | 161 (66%) | 0 (0%) | 0 (0%) |
| S+A impact burst | 44 | 28 (64%) | 0 (0%) | 0 (0%) |
| B+C impact burst | 24 | 20 (83%) | 0 (0%) | 0 (0%) |

## How to pick (planner rules)
1. Pick the layer job, then copy its default size + transparency pair below (most common S+A pair). Copy `keypoints` verbatim from `content/vfx/curves.json`; scale size with `keypoints_norm` x your peak studs.
2. Deviate only with a reason (a longer-lived smoke may want a later fade). Never average two curves: choose one.
3. Keep envelope keypoints when the medoid has them: the random range is part of the look.
4. Impact flash and core pop: an `impact pop` size curve with a short lifetime (life column). Glow and halo: V-glow transparency.
5. Colour: one pattern per layer; start from the medoid keypoints, then re-key hue to the stage palette.

Default pair per job (n = S+A layers of the job):
| job | size | transparency | n(job) | pair count |
|---|---|---|---|---|
| flare/star | bump (early peak) | opaque hold | 95 | 25 |
| flame body | constant size | opaque hold | 75 | 26 |
| spark | linear shrink | opaque hold | 58 | 39 |
| smoke | partial grow | faint (barely visible) | 46 | 9 |
| impact burst | linear shrink | opaque hold | 44 | 12 |
| streak/speedline | linear shrink | opaque hold | 43 | 21 |
| liquid/splash | constant size | linear fade | 41 | 7 |
| other | linear shrink | opaque hold | 33 | 15 |
| glow/halo | constant size | opaque hold | 32 | 9 |
| ember/spec | linear shrink | fade in | 32 | 6 |
| core | linear shrink | opaque hold | 26 | 22 |
| slash/crescent | partial grow | fade from translucent | 19 | 4 |
| ring/shockwave | constant size | fade in, hold, fade out | 13 | 5 |
| ground decal | constant size | opaque hold | 13 | 5 |
| wisp/swirl | linear shrink | opaque hold | 12 | 4 |
| lightning/electric | constant size | opaque hold | 6 | 6 |
| debris/chunks | linear shrink | opaque hold | 4 | 4 |
| flipbook burst | S-curve grow | late fade #2 | 2 | 2 |
| dark underlay/twin | S-curve grow | late fade #2 | 1 | 1 |
