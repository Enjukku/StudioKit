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

# Building blocks: real property values per layer job (30 STUDY effects)

Source: `output/vfx/training-dumps/emitters_study.jsonl` (1,467 VFX rows: 1,312 ParticleEmitter, 76 Beam, 27 Trail, 52 PointLight; none in a hidden effect). Built by `python tools/vfx/emitter_stats.py rows` then `report OUT.md` (tables below are its output; test: `python tools/tests/test_emitter_stats.py`).
- Hidden set (8 effects) never opened. Teardown docs not used. Character/rig/UI instances ignored.
- **n = distinct recipes**: emitters with identical params (colour and path ignored) inside one effect count once (332 of 1,312 removed; `Colours_everywhere` is 127 of them: same 3 emitters x 6 colours). Median (p10-p90) unless stated. Effect counts per job given as n_eff; one effect often supplies most of a job (check n_eff).
- Tiers: S=sTier, A=aTier, B, C, U=Unknown. 13 effects S+A, 11 B+C, 6 U. Size curves: negative keypoints (17 emitters, bezier export artefact) clamped to 0. Size/Speed are stud units as stored; "peak size" = max Size keypoint.
- EmitCount/EmitDelay come from decoded attributes (702 of 980 distinct emitters have EmitCount). EmitCount >= 500 (5 rows, "forever" marker) excluded from EmitCount stats.
- Limit: only EmitDelay inside the instance data is seen. Delays set by scripts (tween timing, task.wait between EmitAll calls) are not in these numbers.

## 1. Job classification rules (first match wins; rule stored per row as `job_rule`)
Names are mostly library ids with digits ("Spec19", "Ele1ctric 2", "D33ark"): digits are stripped before matching. Texture tags (catalog) exist for only 16% of rows (187 of 1,312 texture ids in catalog), so names and props carry the load.
| # | rule | job |
|---|---|---|
| 1 | name has smoke/fog/dust/cloud/steam/mist/puff/haze (dark smoke stays smoke) | smoke |
| 2 | Orientation=VelocityParallel(2) AND any Squash<>0, name not slash/lightning/water/flare/star | streak/speedline |
| 3 | max colour luminance <0.12 and LightEmission<0.5; or name dark/shadow/black/underlay/twin/outline (not slash/smoke); or Brightness<0.6 + LightEmission<0.3 + lum<0.35 | dark underlay/twin |
| 4a | name note/arrow/"other" (music notes, arrows, library "Other" group) | other |
| 4b | name keywords, in order: slash/crescent/swipe -> slash; lightning/electric/zap/bolt -> lightning; water/splash/drip/bubble/rain -> liquid; ground/crack/rune/decal/glyph -> ground decal; ring/shock/circle/pulse -> ring; impact/smack/hit/punch/burst -> impact burst; flare/star/twinkle/shine/snowflake -> flare/star; spec/ember/firefly/dot/glitter/ash -> ember/spec; spark -> spark; fire/flame/blaze/lava -> flame body; debris/rock/shard/gem/leaf -> debris; swirl/wisp/spiral/bezier/rainbow/energy/aura -> wisp; wind/speed/streak/line -> streak; glow/halo/bloom/blur -> glow; core/orb/ball/blob/main -> core |
| 4c | refinements: ember/spec with Drag>3 or (Speed>25, size<1, life<1) -> spark; ember/spec with peak size >=8 and Speed<3 -> glow/halo; ring name with rune/symbol texture -> ground decal |
| 5 | catalog texture shape/group (ring->ring, smoke-puff->smoke, spark-lines->spark, star-4/6/burst-rays->flare, impact-burst->impact, crescent->slash, ...) |  per map |
| 6 | ancestor names (last 3) matched with the 4b keywords (except core/glow/streak) | per keyword |
| 7 | props: Drag>3 + Speed>20 + size<1 -> spark; flat(3)+Speed<1+size growth>2x -> ring; flat -> ground decal; Speed<1+growth>2x -> glow; size<0.6+life<1.5 -> ember; FlipbookLayout>0 -> flipbook burst; life<0.7+static+LightEmission>0.5 -> core; static+LightEmission>0.5 -> glow |
| 8 | low-confidence fallbacks (`props:fallback`): moving+small -> ember; life<0.3 static -> glow (flash); static -> core |
Extensions beyond the brief vocabulary (frequent in the data): **impact burst**, **liquid/splash**, **lightning/electric**. FlipbookLayout>0 is a share column (46% of emitters), not a job: flipbook emitters keep their functional job; "flipbook burst" = flipbook emitter with no other signal (mostly Colours_everywhere n=99 rows, 31 distinct).

**Coverage (n=980 distinct):** rule source: name 744 (76%), props 79 (8%, of which 17 low-confidence fallbacks), ancestor ctx 70 (7%), velocity+squash 52 (5%), texture tag 23 (2%), dark 11 (1%), none 1. **"other": 37 distinct = 3.8% (38 of 1,312 rows = 2.9%)**, all music notes/arrows/library-"Other" textures in 4 effects. Spot-check of 20 random rows (seed 11, read by name+path+props): 17 right or plausible, 3 doubtful: `Foggy Circle Overlay` (smoke; really a static overlay glow), two numbered Colours_everywhere flipbooks (job unknowable). Expect ~85% accuracy; numbered names (1/2/3, F3, SH1) are weakest.

## 2. Job counts (tier columns count distinct recipes)
| job | n distinct | n rows | n_eff | S | A | B | C | U |
|---|---|---|---|---|---|---|---|---|
| flare/star | 122 | 146 | 22 | 78 | 17 | 15 | 3 | 9 |
| flame body | 89 | 117 | 10 | 9 | 66 | 3 | 1 | 10 |
| spark | 84 | 90 | 13 | 36 | 22 | 9 | 0 | 17 |
| impact burst | 81 | 91 | 19 | 22 | 22 | 21 | 3 | 13 |
| streak/speedline | 80 | 93 | 12 | 7 | 36 | 8 | 1 | 28 |
| ember/spec | 79 | 135 | 18 | 22 | 10 | 17 | 18 | 12 |
| smoke | 72 | 80 | 18 | 36 | 10 | 11 | 3 | 12 |
| liquid/splash | 66 | 73 | 9 | 25 | 16 | 19 | 0 | 6 |
| glow/halo | 49 | 73 | 21 | 16 | 16 | 9 | 3 | 5 |
| ring/shockwave | 49 | 54 | 13 | 5 | 8 | 11 | 17 | 8 |
| other | 37 | 38 | 4 | 4 | 29 | 3 | 1 | 0 |
| flipbook burst | 31 | 99 | 5 | 2 | 0 | 9 | 19 | 1 |
| core | 31 | 45 | 6 | 1 | 25 | 5 | 0 | 0 |
| wisp/swirl | 27 | 45 | 8 | 2 | 10 | 9 | 3 | 3 |
| ground decal | 23 | 38 | 10 | 5 | 8 | 9 | 0 | 1 |
| slash/crescent | 22 | 32 | 8 | 8 | 11 | 1 | 0 | 2 |
| lightning/electric | 19 | 31 | 4 | 0 | 6 | 6 | 0 | 7 |
| dark underlay/twin | 11 | 24 | 3 | 1 | 0 | 8 | 0 | 2 |
| debris/chunks | 8 | 8 | 3 | 4 | 0 | 0 | 0 | 4 |

## 3. Value table per job: median (p10-p90). Lifetime s, Speed studs/s, Drag, Accel.Y, SpreadAngle deg, RotSpeed deg/s (max abs of range), peak size studs
Rate only from Enabled emitters with Rate>0 (continuous). EmitCount only from emitters with the attribute. LightInfluence is 0 everywhere (see surprises).
| job | n | Lifetime s | Speed | Drag | Accel.Y | Brightness | LightEm | LightInfl | ZOffset | EmitCount | Rate | Spread | RotSpeed | peak size |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flare/star | 122 | 0.70 (0.23-1.10) | 0.0 (0.0-20) | 0.0 (0.0-5.0) | 0.0 (0.0-0.0) | 5.0 (0.3-15) | 0.75 (0.00-1.00) | 0.00 (0.00-0.00) | 1.5 (-0.2-4.2) | 2 (1-15) | 20 (2-60) | 0 (0-67) | 0 (0-78) | 2.0 (0.2-9.0) |
| flame body | 89 | 0.70 (0.28-0.91) | 10 (0.0-65) | 0.0 (0.0-12) | 0.0 (0.0-0.0) | 7.5 (0.5-15) | -0.30 (-0.30-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.3-1.6) | 5 (0-18) | 20 (10-60) | 360 (0-360) | 0 (0-0) | 3.9 (0.7-13) |
| spark | 84 | 0.76 (0.47-1.27) | 25 (15-50) | 5.5 (3.6-9.0) | 0.0 (-11-4.0) | 5.0 (0.1-15) | 0.00 (0.00-1.00) | 0.00 (0.00-0.00) | 1.5 (-0.0-4.3) | 15 (5-25) | 60 (60-236) | 360 (38-360) | 8 (0-356) | 1.3 (0.4-3.0) |
| impact burst | 81 | 0.20 (0.07-1.20) | 0.0 (0.0-0.0) | 0.0 (0.0-4.0) | 0.0 (0.0-0.0) | 4.0 (0.6-15) | 0.10 (0.00-1.00) | 0.00 (0.00-0.00) | 2.8 (-0.0-6.0) | 2 (1-10) | 14 (6-18) | 0 (0-360) | 0 (0-20) | 8.3 (4.0-27) |
| streak/speedline | 80 | 0.50 (0.20-0.75) | 24 (0.0-62) | 3.6 (0.0-10) | 0.0 (-3.3-0.0) | 6.0 (1.0-15) | 0.50 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.1-1.0) | 6 (1-15) | 60 (15-100) | 15 (0-360) | 0 (0-42) | 1.4 (0.5-7.1) |
| ember/spec | 79 | 0.75 (0.40-1.60) | 6.8 (0.0-15) | 0.2 (0.0-4.0) | 0.0 (0.0-0.0) | 5.0 (0.5-15) | 0.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.1-3.9) | 8 (1-31) | 35 (20-60) | 10 (0-360) | 0 (0-60) | 1.0 (0.3-4.5) |
| smoke | 72 | 1.00 (0.58-1.50) | 15 (0.0-42) | 3.4 (0.0-6.0) | 0.0 (-4.7-0.0) | 2.0 (0.1-9.9) | 0.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-1.1-3.9) | 10 (1-20) | 35 (20-60) | 35 (0-360) | 0 (0-5) | 3.0 (1.0-12) |
| liquid/splash | 66 | 0.80 (0.30-1.23) | 0.0 (0.0-25) | 0.0 (0.0-4.5) | 0.0 (-4.0-0.0) | 3.0 (0.3-8.2) | 0.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.5-4.3) | 2 (0-20) | 20 (6-60) | 0 (0-360) | 0 (0-32) | 5.0 (1.1-11) |
| glow/halo | 49 | 0.75 (0.04-2.00) | 0.0 (0.0-0.0) | 0.0 (0.0-5.0) | 0.0 (0.0-0.0) | 1.5 (0.2-5.0) | 1.00 (0.00-1.00) | 0.00 (0.00-0.00) | 2.0 (-1.0-7.0) | 1 (1-2) | 6 (2-35) | 0 (0-360) | 0 (0-0) | 13 (4.5-34) |
| ring/shockwave | 49 | 0.50 (0.20-1.55) | 0.0 (0.0-8.8) | 0.0 (0.0-8.0) | 0.0 (0.0-0.0) | 5.0 (0.6-15) | 0.00 (-0.30-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.3-0.2) | 2 (0-10) | 12 (2-30) | 0 (0-45) | 0 (0-80) | 9.0 (2.8-15) |
| other | 37 | 0.75 (0.40-1.00) | 5.5 (0.0-28) | 3.0 (0.0-5.0) | -9.0 (-15-0.0) | 4.0 (3.0-6.4) | 0.00 (0.00-0.70) | 0.00 (0.00-0.00) | 2.8 (0.0-4.4) | 10 (1-20) | 5 (2-15) | 20 (0-360) | 0 (0-50) | 0.8 (0.5-2.0) |
| flipbook burst | 31 | 0.75 (0.50-1.90) | 9.1 (4.2-45) | 5.0 (0.0-6.0) | 0.0 (0.0-0.0) | 4.0 (0.5-15) | 1.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.1-4.0) | 25 (10-65) | 22 (15-48) | 360 (0-380) | 0 (0-0) | 1.8 (0.3-3.3) |
| core | 31 | 0.35 (0.15-0.50) | 5.9 (0.0-5.9) | 3.0 (0.0-5.0) | 0.0 (0.0-0.0) | 5.0 (4.0-6.0) | 1.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.1 (0.0-2.9) | 3 (2-10) | 12 (7-32) | 10 (0-360) | 0 (0-0) | 0.2 (0.2-5.9) |
| wisp/swirl | 27 | 0.68 (0.46-2.20) | 0.3 (0.0-34) | 0.3 (0.0-5.0) | 0.0 (-3.0-2.4) | 5.0 (1.6-15) | 0.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.5-3.0) | 5 (3-25) | 15 (1-49) | 0 (0-180) | 0 (0-200) | 1.1 (0.3-11) |
| ground decal | 23 | 1.00 (0.20-1.73) | 0.0 (0.0-0.0) | 0.0 (0.0-5.0) | 0.0 (0.0-27) | 3.0 (0.1-14) | 0.00 (0.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-0.1-1.0) | 2 (1-3) | 35 (6-55) | 0 (0-0) | 0 (0-0) | 7.0 (1.4-29) |
| slash/crescent | 22 | 0.62 (0.32-0.99) | 0.0 (0.0-3.0) | 0.0 (0.0-4.0) | 0.0 (0.0-6.4) | 3.0 (1.0-6.9) | 0.00 (0.00-0.47) | 0.00 (0.00-0.00) | 0.6 (0.0-4.0) | 7 (1-15) | 20 (20-20) | 0 (0-1) | 0 (0-190) | 3.7 (2.3-16) |
| lightning/electric | 19 | 0.65 (0.20-1.00) | 0.0 (0.0-10) | 0.0 (0.0-3.4) | 0.0 (0.0-0.0) | 15 (4.2-30) | 1.00 (-5.00-1.00) | 0.00 (0.00-0.00) | 0.0 (-2.0-1.0) | 5 (1-6) | 35 (10-35) | 20 (0-360) | 0 (0-0) | 5.0 (0.3-30) |
| dark underlay/twin | 11 | 0.38 (0.25-0.60) | 0.0 (0.0-15) | 0.0 (0.0-0.0) | 0.0 (0.0-0.0) | 10 (1.0-15) | 1.00 (1.00-1.00) | 0.00 (0.00-0.00) | 0.0 (0.0-0.0) | 3 (1-4) | 20 (20-20) | 0 (0-360) | 0 (0-0) | 7.2 (3.4-10) |
| debris/chunks | 8 | 0.80 (0.75-1.00) | 22 (18-52) | 5.5 (0.7-6.0) | -3.0 (-42-0.0) | 4.0 (1.0-10) | 0.25 (-5.00-0.80) | 0.00 (0.00-0.00) | 0.0 (0.0-0.4) | 9 (5-12) | 60 (53-123) | 75 (40-178) | 0 (0-50) | 0.8 (0.7-1.6) |

## 4. Shares and curve shapes (size = fraction of own max; transparency = raw 0..1; columns are t=0, .05, .1, .25, .5, .75, 1; median across the job)
Median curve is flattened by mixed shapes: use section 5 class shares to pick a shape, then the median curve to scale it. 63% of Size sequences and 65% of Transparency sequences are plain 2-key; dense 11-20 key curves are bezier exports.
| job | n | squash | vel-parallel(2) | flat(3) | locked | flipbook | colour change | enabled | size@0/.05/.1/.25/.5/.75/1 (frac of max) | transp@same t |
|---|---|---|---|---|---|---|---|---|---|---|
| flare/star | 122 | 16% | 6% | 4% | 47% | 8% | 7% | 90% | 1/.95/.97/.89/.85/.77/.91 | .00/.00/.00/.00/.00/.15/.90 |
| flame body | 89 | 6% | 3% | 8% | 13% | 94% | 70% | 70% | 1/.95/.90/.75/.83/.92/1 | .00/.00/.00/.00/.00/.00/.00 |
| spark | 84 | 1% | 20% | 1% | 4% | 24% | 15% | 74% | 1/.95/.90/.75/.50/.25/.00 | .00/.00/.00/.00/.00/.00/.00 |
| impact burst | 81 | 1% | 2% | 25% | 7% | 27% | 25% | 80% | .81/.81/.90/.75/.82/.91/1 | .00/.00/.00/.00/.00/.00/.00 |
| streak/speedline | 80 | 65% | 82% | 16% | 2% | 54% | 56% | 52% | 1/.95/.90/.75/.74/.50/.00 | .00/.00/.00/.00/.00/.00/.00 |
| ember/spec | 79 | 3% | 4% | 0% | 25% | 30% | 6% | 85% | 1/.95/.90/.76/.57/.28/.00 | .00/.00/.00/.00/.00/.00/.00 |
| smoke | 72 | 6% | 3% | 8% | 15% | 94% | 14% | 83% | .59/.63/.66/.75/.86/.95/1 | .84/.80/.73/.65/.74/.89/1 |
| liquid/splash | 66 | 2% | 0% | 24% | 12% | 65% | 11% | 91% | .56/.69/.83/.88/.96/.99/1 | .00/.05/.10/.25/.34/.67/1 |
| glow/halo | 49 | 0% | 0% | 6% | 16% | 8% | 14% | 88% | 1/1/1/1/1/1/1 | .00/.05/.10/.25/.50/.75/1 |
| ring/shockwave | 49 | 0% | 0% | 63% | 0% | 45% | 31% | 73% | .56/.62/.75/.83/.90/.97/1 | .00/.01/.02/.00/.00/.12/1 |
| other | 37 | 0% | 8% | 0% | 38% | 11% | 0% | 97% | 1/.95/.90/.75/.50/.25/.00 | .00/.00/.00/.00/.00/.00/.00 |
| flipbook burst | 31 | 0% | 3% | 0% | 6% | 100% | 3% | 97% | 1/1/1/1/1/1/1 | .00/.00/.00/.00/.00/.02/1 |
| core | 31 | 0% | 0% | 0% | 10% | 6% | 77% | 94% | 1/.95/.90/.75/.50/.25/.00 | .00/.00/.00/.00/.00/.00/.00 |
| wisp/swirl | 27 | 0% | 0% | 11% | 7% | 37% | 22% | 89% | .83/.85/.87/.75/.69/.84/1 | .00/.02/.08/.00/.00/.00/1 |
| ground decal | 23 | 0% | 0% | 74% | 0% | 48% | 9% | 87% | .33/.48/.85/.90/.97/1/1 | .00/.05/.08/.04/.04/.28/1 |
| slash/crescent | 22 | 0% | 9% | 91% | 0% | 64% | 23% | 91% | .50/.53/.55/.65/.77/.90/1 | .10/.15/.19/.29/.50/.75/1 |
| lightning/electric | 19 | 5% | 16% | 42% | 63% | 89% | 0% | 37% | .31/.52/.74/.79/.93/.98/1 | .00/.00/.00/.00/.00/.00/.00 |
| dark underlay/twin | 11 | 0% | 0% | 73% | 73% | 100% | 18% | 9% | .22/.58/.67/.78/.85/.93/1 | .00/.05/.10/.25/.50/.75/1 |
| debris/chunks | 8 | 0% | 25% | 0% | 25% | 88% | 0% | 75% | .50/.53/.55/.63/.75/.37/.00 | .00/.00/.00/.00/.00/.00/.00 |

## 5. Curve classes and firing mode (share of distinct emitters)
size grow = starts <=0.6 of max and ends >=0.8; shrink = starts >=0.7, ends <=0.3; bump = peak mid-life; flat = always >=0.8. continuous = Enabled with Rate>0; "burst delayed" = share of EmitCount emitters with EmitDelay>0.
| job | n | size grow | shrink | bump | flat | other | transp fade-out | fade-in-out | opaque | faint | partial | continuous(enabled+Rate) | has EmitCount | burst delayed>0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flare/star | 122 | 7% | 17% | 30% | 43% | 3% | 18% | 30% | 48% | 3% | 1% | 57% | 67% | 2% |
| flame body | 89 | 31% | 29% | 1% | 37% | 1% | 22% | 1% | 73% | 0% | 3% | 61% | 48% | 14% |
| spark | 84 | 5% | 58% | 27% | 7% | 2% | 10% | 6% | 81% | 1% | 2% | 8% | 93% | 31% |
| impact burst | 81 | 36% | 30% | 4% | 22% | 9% | 31% | 7% | 56% | 6% | 0% | 5% | 94% | 14% |
| streak/speedline | 80 | 20% | 36% | 22% | 11% | 10% | 12% | 8% | 69% | 5% | 6% | 11% | 90% | 25% |
| ember/spec | 79 | 4% | 30% | 39% | 22% | 5% | 6% | 18% | 58% | 10% | 8% | 62% | 49% | 28% |
| smoke | 72 | 51% | 6% | 0% | 24% | 19% | 32% | 31% | 6% | 32% | 0% | 44% | 74% | 21% |
| liquid/splash | 66 | 47% | 5% | 5% | 36% | 8% | 44% | 35% | 14% | 8% | 0% | 41% | 59% | 0% |
| glow/halo | 49 | 16% | 8% | 2% | 65% | 8% | 22% | 27% | 29% | 22% | 0% | 29% | 80% | 8% |
| ring/shockwave | 49 | 47% | 12% | 4% | 31% | 6% | 22% | 22% | 45% | 10% | 0% | 37% | 43% | 38% |
| other | 37 | 5% | 59% | 16% | 19% | 0% | 0% | 24% | 59% | 3% | 14% | 35% | 92% | 0% |
| flipbook burst | 31 | 16% | 13% | 16% | 55% | 0% | 23% | 16% | 32% | 29% | 0% | 39% | 68% | 71% |
| core | 31 | 6% | 84% | 3% | 3% | 3% | 10% | 3% | 87% | 0% | 0% | 13% | 90% | 50% |
| wisp/swirl | 27 | 26% | 26% | 19% | 26% | 4% | 19% | 30% | 44% | 7% | 0% | 52% | 41% | 36% |
| ground decal | 23 | 43% | 4% | 9% | 43% | 0% | 30% | 35% | 30% | 4% | 0% | 26% | 74% | 24% |
| slash/crescent | 22 | 68% | 0% | 0% | 23% | 9% | 50% | 18% | 18% | 14% | 0% | 5% | 95% | 19% |
| lightning/electric | 19 | 47% | 0% | 11% | 42% | 0% | 0% | 11% | 89% | 0% | 0% | 37% | 58% | 0% |
| dark underlay/twin | 11 | 100% | 0% | 0% | 0% | 0% | 55% | 0% | 18% | 27% | 0% | 9% | 100% | 0% |
| debris/chunks | 8 | 0% | 50% | 50% | 0% | 0% | 0% | 0% | 100% | 0% | 0% | 50% | 75% | 17% |
Colour (section GEN3c in the script output, n per job above): start colour is saturated for 82-100% of every job and near-white (all channels >=200) for 0% of flare, flame, spark, core, ring; only streak (11%), smoke (10%), debris (25%) start whitish. Median start luminance 0.4-0.5 (flame .40, flare .48, spark .51), core .73, streak .80. End colour is darker than start for <=22% of any job. Colour changes during life: flame 70%, core 77%, streak 56%, impact 25%, flare 7%.

## 6. S+A vs B+C where the job has >=5 distinct emitters in both (median SA / BC)
B+C EmitCount medians (30 for ember, flare, liquid) are inflated by Colours_everywhere and Punch_Place_OS; trust the SA column for counts.
| job | n SA | n BC | Lifetime SA/BC | Speed SA/BC | Bright SA/BC | LightEm SA/BC | EmitCount SA/BC | peak SA/BC |
|---|---|---|---|---|---|---|---|---|
| flare/star | 95 | 18 | 0.70 / 1.00 | 0.0 / 0.0 | 4.0 / 4.5 | 1.00 / 0.10 | 2 / 30 | 1.6 / 3.1 |
| spark | 58 | 9 | 0.85 / 0.55 | 22 / 38 | 5.0 / 15 | 0.00 / 1.00 | 15 / 25 | 1.4 / 0.6 |
| impact burst | 44 | 24 | 0.12 / 0.47 | 0.0 / 0.0 | 3.0 / 5.0 | 0.10 / 0.00 | 1 / 4 | 7.7 / 10 |
| streak/speedline | 43 | 9 | 0.50 / 0.50 | 8.5 / 10 | 6.0 / 6.0 | 0.00 / 0.00 | 6 / 10 | 1.4 / 4.1 |
| ember/spec | 32 | 35 | 0.82 / 0.75 | 0.8 / 7.1 | 3.0 / 5.0 | 0.20 / 0.00 | 2 / 30 | 1.5 / 0.4 |
| smoke | 46 | 14 | 1.00 / 1.12 | 16 / 0.0 | 2.0 / 1.0 | 0.00 / 0.00 | 10 / 5 | 3.0 / 3.5 |
| liquid/splash | 41 | 19 | 0.75 / 1.00 | 0.0 / 0.0 | 2.5 / 3.0 | 1.00 / 0.00 | 1 / 32 | 5.0 / 3.7 |
| glow/halo | 32 | 12 | 0.68 / 0.57 | 0.0 / 0.0 | 2.0 / 1.2 | 1.00 / 1.00 | 1 / 1 | 15 / 5.8 |
| ring/shockwave | 13 | 28 | 0.20 / 0.75 | 0.0 / 0.0 | 6.0 / 3.0 | 0.00 / 1.00 | 0 / 3 | 5.7 / 10 |
| core | 26 | 5 | 0.41 / 0.10 | 5.9 / 0.0 | 5.0 / 5.0 | 0.65 / 1.00 | 3 / 2 | 0.2 / 3.3 |
| wisp/swirl | 12 | 12 | 0.59 / 0.75 | 0.1 / 1.8 | 4.5 / 6.0 | 0.00 / 0.00 | 5 / 25 | 3.1 / 0.5 |
| ground decal | 13 | 9 | 1.30 / 0.88 | 0.0 / 0.0 | 3.0 / 5.0 | 0.00 / 1.00 | 2 / 1 | 5.0 / 9.3 |
| lightning/electric | 6 | 6 | 1.00 / 0.20 | 0.0 / 0.0 | 15 / 5.0 | 1.00 / 1.00 | - / 3 | 0.3 / 4.5 |

## 7. Per effect (all rows, not deduped). peak live = estimated simultaneous particles (bursts live their mean Lifetime; Enabled emitters add Rate x Lifetime)
| effect | tier | emit | uniq tex | emit/tex | peak live | beam | trail | light | first-fire timeline |
|---|---|---|---|---|---|---|---|---|---|
| CartoonE | U | 12 | 11 | 1.1 | 104 | 0 | 0 | 0 | 0ms:impact burst,smoke,flare,spark,flipbook burst |
| Gabimaru_Aura | U | 25 | 5 | 5.0 | 1075 | 0 | 0 | 0 | 0ms:flame body,glow,ember |
| Goal_VFX | U | 11 | 11 | 1.0 | 94 | 0 | 0 | 0 | 0ms:lightning,ember,streak,flare,ring |
| Hakari_Aura | U | 14 | 13 | 1.1 | 520 | 0 | 0 | 0 | 0ms:slash,ring,ember,glow,flame body,debris,flare,smoke,lightning |
| Meteor_VFX_Open_Source | U | 16 | 14 | 1.1 | 611 | 32 | 0 | 0 | 0ms:ember,impact burst,ring,flame body,smoke,slash,ground decal |
| ProjectilePractice | U | 85 | 38 | 2.2 | 243 | 9 | 9 | 2 | 0ms:streak,smoke,ember,debris,spark,liquid,impact burst,glow,dark underlay wisp@1000ms |
| Ayato_Showcase | A | 84 | 10 | 8.4 | 321 | 3 | 0 | 6 | 0ms:slash,glow,core,streak,ring,impact burst,spark,ember,flare |
| Colouring_Practice | A | 27 | 8 | 3.4 | 325 | 0 | 0 | 2 | 0ms:streak,wisp,ember,impact burst,liquid,glow |
| Death_FX | A | 8 | 5 | 1.6 | 58 | 0 | 0 | 0 | 0ms:spark,flare,glow,ground decal |
| Flame_Beziers | A | 38 | 12 | 3.2 | 1126 | 0 | 1 | 1 | 0ms:flame body,smoke,spark,ember,impact burst slash@30ms ground decal@30ms |
| StylizedFireballsTrails | A | 82 | 17 | 4.8 | 676 | 0 | 6 | 4 | 0ms:flame body,flare,liquid,ring,core,streak |
| Zonito_Music_OS | A | 122 | 24 | 5.1 | 739 | 0 | 2 | 6 | 0ms:glow,other,spark,liquid,impact burst,flare,smoke,wisp,ember,slash,ground decal,streak |
| nnoonooooo | A | 10 | 9 | 1.1 | 129 | 0 | 1 | 1 | 0ms:ember,flare,impact burst,glow,ground decal,liquid |
| soear | A | 15 | 5 | 3.0 | 6174 | 2 | 0 | 1 | 0ms:lightning,smoke,glow,core,flare |
| Astral_Redesign | B | 31 | 17 | 1.8 | 194 | 0 | 0 | 0 | 0ms:impact burst ring@15ms streak@15ms flare@15ms glow@15ms smoke@15ms ground decal@15ms wisp@15ms |
| Emerald | B | 13 | 7 | 1.9 | 2487 | 0 | 1 | 1 | 0ms:core,other,ember,glow |
| HitEffectOS | B | 16 | 6 | 2.7 | 158 | 0 | 0 | 0 | 0ms:impact burst flare@50ms spark@50ms ring@50ms |
| Punch_Place_OS | B | 82 | 16 | 5.1 | 716 | 0 | 0 | 0 | 0ms:dark underlay,lightning,flame body,slash,flare,ground decal,streak,impact burst |
| Water_Barrage_OPENSOURCE | B | 27 | 20 | 1.4 | 726 | 0 | 1 | 2 | 0ms:liquid,ring,flare,impact burst,ember,spark |
| bow_thngiemajig | B | 16 | 8 | 2.0 | 592 | 3 | 0 | 2 | 0ms:flare,glow,liquid,smoke |
| orb_thingies | B | 27 | 10 | 2.7 | 78 | 0 | 0 | 3 | 0ms:ring,wisp,glow,flare,smoke,flame body |
| silly_water | B | 44 | 19 | 2.3 | 1261 | 0 | 0 | 2 | 0ms:ground decal,smoke,glow,ember,impact burst,flipbook burst,core spark@50ms ring@50ms |
| Colours_everywhere | C | 161 | 6 | 27 | 3020 | 0 | 0 | 7 | 0ms:ember,flipbook burst,glow |
| blue_pewpews | C | 11 | 6 | 1.8 | 179 | 0 | 1 | 2 | 0ms:other,impact burst,ember,smoke,flipbook burst,flame body |
| the_circle_thingie_1_ | C | 42 | 18 | 2.3 | 425 | 4 | 0 | 1 | 0ms:wisp,smoke,flare,ring,impact burst |
| Astral_Sword | S | 59 | 24 | 2.5 | 950 | 4 | 0 | 1 | 0ms:flare,glow,spark,ember,smoke,ring,liquid,impact burst,slash,ground decal |
| Elemental_Guns_OPENSOURCE_ZRBLX | S | 159 | 34 | 4.7 | 2468 | 10 | 2 | 4 | 0ms:glow,impact burst,spark,ember,flare,smoke,debris,slash,streak,core,flame body,ground decal,other |
| FUGAAAA | S | 23 | 18 | 1.3 | 919 | 9 | 3 | 0 | 0ms:glow,flame body,flare,spark,smoke,streak,flipbook burst,dark underlay |
| Mildly_wet_projectiles | S | 41 | 18 | 2.3 | 716 | 0 | 0 | 2 | 0ms:glow,impact burst,liquid,wisp,spark,smoke,flare |
| space_thingiemajig | S | 11 | 8 | 1.4 | 624 | 0 | 0 | 2 | 0ms:glow,impact burst,streak,ember,smoke,wisp,flare |
Median effect: 27 emitters, 11.5 unique textures, 2.3 emitters per texture, 6 distinct jobs, est. peak live 618 (p90 2,470). S+A (n=13): 38 emitters, 12 textures, 3.0 per texture, peak 717. B+C (n=11): 27, 10, 2.3, 592. Beams/trails are rare (beams in 9 of 30 effects, trails in 10); PointLights in 20 of 30 (n=52, Brightness 1.4 (0-4), Range 9 (5-16), Shadows on in 12).
Beam (n=76, 9 effects): Width0 6 (0-30) -> Width1 20 (2-80) studs, Segments 50 (10-200), TextureSpeed 3, Brightness 1 (0-15), LightInfluence 0, FaceCamera 30%. Trail (n=27, 10 effects): Lifetime 0.5 s (0.1-0.77), Brightness 4 (1-15), LightInfluence 0, FaceCamera 100%.

## 8. Recipes per effect type (units = emitters grouped under the first ancestor whose name carries a type keyword; >=2 distinct emitters; type from path keywords, else burst vs continuous structure)
Times are ms after the unit first fire. Columns: units with job, share of units, fire ms median (p10-p90), share fired >0.5 ms, median Lifetime ms, median ZOffset, summed EmitCount, emitters. Only jobs in >=25% of units shown. slash n=5 units and beam n=1 unit are too thin: use section 7 for slash/beam examples.
**burst/one-shot: 40 units, 12 effects, median 4 emitters/unit**
| job | units with job | share | fire ms median (p10-p90) | share fired >0.5ms | median life ms | median ZOffset | median EmitCount sum | median emitters |
|---|---|---|---|---|---|---|---|---|
| ember/spec | 15 | 41% | 0 (0-50) | 27% | 1125 | 1.0 | 16 | 1 |
| flare/star | 13 | 35% | 0 (0-0) | 0% | 550 | 2.0 | 17 | 3 |
| streak/speedline | 12 | 32% | 0 (0-0) | 0% | 450 | 0.0 | 16 | 2 |
| glow/halo | 11 | 30% | 0 (0-0) | 0% | 400 | 3.0 | 2 | 1 |
| smoke | 10 | 27% | 0 (0-0) | 0% | 825 | -0.1 | 6 | 2 |

**aura/loop: 26 units, 13 effects, median 3 emitters/unit**
| job | units with job | share | fire ms median (p10-p90) | share fired >0.5ms | median life ms | median ZOffset | median EmitCount sum | median emitters |
|---|---|---|---|---|---|---|---|---|
| flare/star | 11 | 44% | 0 (0-0) | 0% | 750 | 0.0 | 0 | 1 |
| ember/spec | 10 | 40% | 0 (0-0) | 0% | 538 | 0.0 | 0 | 2 |
| smoke | 8 | 32% | 0 (0-0) | 0% | 1000 | -0.9 | 0 | 1 |

**projectile: 15 units, 12 effects, median 13 emitters/unit**
| job | units with job | share | fire ms median (p10-p90) | share fired >0.5ms | median life ms | median ZOffset | median EmitCount sum | median emitters |
|---|---|---|---|---|---|---|---|---|
| impact burst | 10 | 67% | 0 (0-0) | 0% | 340 | 3.7 | 11 | 2 |
| smoke | 10 | 67% | 0 (0-0) | 0% | 975 | 0.0 | 12 | 1 |
| ember/spec | 9 | 60% | 0 (0-0) | 0% | 750 | 0.0 | 10 | 2 |
| spark | 8 | 53% | 0 (0-0) | 0% | 688 | 1.5 | 38 | 2 |
| flame body | 7 | 47% | 0 (0-0) | 0% | 750 | 0.0 | 33 | 2 |
| glow/halo | 7 | 47% | 0 (0-0) | 0% | 1000 | 0.0 | 3 | 1 |
| flare/star | 6 | 40% | 0 (0-0) | 0% | 1000 | 1.0 | 13 | 4 |
| liquid/splash | 5 | 33% | 0 (0-0) | 0% | 775 | 0.0 | 5 | 3 |
| streak/speedline | 4 | 27% | 0 (0-0) | 0% | 463 | 0.0 | 27 | 5 |
| ring/shockwave | 4 | 27% | 0 (0-0) | 0% | 625 | -0.3 | 0 | 2 |
| ground decal | 4 | 27% | 0 (0-21) | 25% | 1425 | -0.0 | 3 | 2 |

**impact/explosion: 10 units, 8 effects, median 10 emitters/unit**
| job | units with job | share | fire ms median (p10-p90) | share fired >0.5ms | median life ms | median ZOffset | median EmitCount sum | median emitters |
|---|---|---|---|---|---|---|---|---|
| impact burst | 8 | 89% | 0 (0-0) | 0% | 181 | 1.8 | 8 | 3 |
| flare/star | 5 | 56% | 0 (0-30) | 20% | 575 | 2.0 | 2 | 2 |
| spark | 5 | 56% | 0 (0-30) | 20% | 1000 | 2.5 | 31 | 2 |
| liquid/splash | 5 | 56% | 0 (0-0) | 0% | 800 | 2.9 | 7 | 3 |
| glow/halo | 5 | 56% | 0 (0-0) | 0% | 900 | 3.0 | 2 | 2 |
| wisp/swirl | 4 | 44% | 0 (0-0) | 0% | 588 | 0.0 | 8 | 2 |
| smoke | 3 | 33% | 0 (0-0) | 0% | 1050 | 0.8 | 32 | 3 |
| other | 3 | 33% | 0 (0-0) | 0% | 1000 | 3.5 | 57 | 4 |

**slash: 5 units, 2 effects, median 10 emitters/unit**
| job | units with job | share | fire ms median (p10-p90) | share fired >0.5ms | median life ms | median ZOffset | median EmitCount sum | median emitters |
|---|---|---|---|---|---|---|---|---|
| core | 4 | 80% | 0 (0-56) | 25% | 425 | 0.1 | 25 | 4 |
| streak/speedline | 4 | 80% | 0 (0-56) | 25% | 572 | 0.0 | 13 | 4 |
| slash/crescent | 3 | 60% | 0 (0-0) | 0% | 300 | 0.0 | 1 | 1 |
| glow/halo | 2 | 40% | 0 (0-0) | 0% | 350 | 5.5 | 2 | 2 |
| flare/star | 2 | 40% | 0 (0-0) | 0% | 300 | 1.4 | 34 | 8 |
| ember/spec | 2 | 40% | 0 (0-0) | 0% | 500 | -0.0 | 5 | 4 |

Reading: pros stack 5-13 emitters per unit that all start at 0 ms. Order is built by lifetime and ZOffset, not delay: impact flash ~125-180 ms at ZOffset +1.8 to +3.7, flares/sparks 550-1000 ms, smoke ~1 s at ZOffset about 0, glow ~900-1000 ms. Where delays exist they are 10-180 ms (Astral_Redesign 15, Flame_Beziers 30, HitEffectOS 50, silly_water 50); only 188 of 980 distinct emitters (19%) have EmitDelay>0, max 2.0 s.

## 9. Surprises (pro numbers vs common advice; n = 980 distinct emitters unless stated)
1. **LightInfluence = 0 on 979 of 980 emitters (100%)**, and 0 on every Beam (76) and Trail (27). Pros ignore world lighting entirely; glow comes from Brightness + LightEmission.
2. **Brightness above 1 is normal:** >1 on 75%, >=5 on 50%, >=10 on 17%, max 50; only 14% below 1. Mode values 5 (170 rows), 15 (132), 1 (110), 6 (92). Medians: flare 5, flame 7.5, streak 6, ember 5, spark 5, impact 4, smoke 2, ground decal 3, glow 1.5.
3. **LightEmission is bimodal, not a ramp:** 0 on 45%, 1 on 37%, 0.5 on 5%, **negative on 8%, but concentrated:** -0.3 on 50 rows, all in StylizedFireballsTrails (A, flame bodies); -5 on 15 rows, all in 3 Unknown-tier aura/goal effects; -1 on 12 rows across 4 effects. Treat as one-effect style, not a trend. Median 0 for flame, spark, smoke, ember, wisp; 1 for glow, core, dark twin, flipbook.
4. **Start colour is saturated, never white:** 0% of flare, flame, spark, core start with all channels >=200. The hot look is colour x Brightness 4-7, not a white core.
5. **Everything fires at t=0:** all 5 S-tier effects with timelines fire every job at 0 ms in instance data. Layering is lifetime + ZOffset: ZOffset is non-zero on 76% (>0 on 54%, <0 on 22%); glow +2 to +3, impact +2.8, flare +1.5, smoke 0 to -1.
6. **Impact flash is very short in good work:** impact burst Lifetime SA 0.12 s vs BC 0.47 s; ring SA 0.20 s vs BC 0.75 s; core SA 0.41 vs BC 0.10 (n=26 vs 5). Shockwave rings are fast and start at 0.56 of max size.
7. **Many emitters, few textures:** median 27 emitters on 11.5 unique textures (2.3 per texture; S+A 3.0, Ayato_Showcase 8.4). Same texture reused as twins with different Size/Brightness/Lifetime. No study effect has fewer than 8 emitters (Death_FX).
8. **Counts are small per emitter:** flare 2 (1-15), impact 2 (1-10), glow 1 (1-3), ring 2 (0-10), smoke 10 (1-20), ember 8 (1-35), flame 5 (0-18), spark 15 (5-25). Bursts via EmitCount, not Rate: 72% of emitters have EmitCount; Rate matters only for the 52-62% continuous in flare, ember, wisp, flame.
9. **Flame and smoke bodies are flipbooks** (94% and 94%); 46% of all emitters have FlipbookLayout>0, almost all FlipbookLayout value 2 (Grid4x4 by enum order; 368 rows). Flipbook is the norm for bodies, not an extra.
10. **Sparks are real physics:** Drag 5.5 (3.6-9), Speed 25 (15-50), size 1.3 (0.4-3), SpreadAngle 360, 58% shrink-to-zero, Lifetime 0.76 s, 93% EmitCount burst. Flares/impacts/rings/glows use SpreadAngle 0 (stationary billboards, Speed 0).
11. **Orientation:** FacingCamera 70%, VelocityParallel 11% (82% of streaks, always with Squash), flat VelocityPerpendicular 16% (ring 63%, ground decal 74%, slash 91%). Squash is used by only 9% of emitters, 65% of streaks.
12. **Short life dominates:** 38% of emitters live <=0.5 s, only 4% >=2 s; medians 0.2 s (impact) to 1.0 s (smoke, ground decal). Peak size medians: core 0.2 (tiny hot dot), ember 1, spark 1.3, flare 2, smoke 3, slash 3.7, liquid 5, impact 8.3, ring 9, glow 13 studs.
13. **Transparency starts opaque:** 0.00 at t=0 for all jobs except smoke (0.84, fades in) and slash (0.10). Fade-out only at the end for most jobs; 48-89% of flare, flame, spark, core, lightning are fully opaque all life (size does the fading).
