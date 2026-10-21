> Author: researcher (vfx-deep-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# P5 Juice and satisfaction, P6 Repeats, P7 Effect-and-sound sync

Scope notes (read first):
- WebSearch budget ran out mid-task. Part 6 (repeats) is the thinnest part: no tier-A source found that gives numbers for variant counts, caps, cooldowns or combo steps. Those cells say "no number found".
- Kao 2020 (Entertainment Computing) full text NOT read: ScienceDirect returned HTTP 403. Its results are reported second-hand from S1 (CHI 2024, which re-describes it) and S2 (survey). Treat Kao 2020 rows as "reported by S1/S2", not first-hand.
- Several PDFs returned binary to WebFetch. They were saved by the tool and converted to text locally with pdftotext; the text was then read. Counted as read.
- Evidence labels: study | preprint | industry practice | spec | inference.

## 1. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave us |
|---|---|---|---|---|---|---|---|
| S1 | How does Juicy Game Feedback Motivate? Testing Curiosity, Competence, and Effectance (CHI '24) | Kao, Ballou, Gerling, Breitsohl, Deterding | 2024 | A (peer-reviewed, pre-registered, OSF) | https://doi.org/10.1145/3613904.3642656 (read via KIT PDF https://publikationen.bibliothek.kit.edu/1000171104/152952099) | no | n=1,699; amplification lowered effectance and competence; success-dependence raised competence, curiosity, effectance; random variety gave no curiosity; curiosity best predictor of playtime; outcome-binding explanation [V: confirmed - n=1,699, pre-registered, DOI/KIT PDF text read] |
| S2 | Designing Game Feel. A Survey (arXiv 2011.09201) | Pichlmair, Johansen | 2020 | A-preprint (label "preprint") | https://arxiv.org/pdf/2011.09201 | no | juice definitions, restates Kao 2020 result, catalogue of techniques (hit stop, screen shake, freeze frames, particles, flashes) |
| S3 | What Features Influence Impact Feel? A Study of Impact Feedback in Action Games (arXiv 2208.06155, GEM 2022) | Lin, Duan, Wen, Cai | 2022 | A-preprint (label "preprint") | https://arxiv.org/pdf/2208.06155 | no | 44 Steam games ranked from 280K comments; 19-feature framework; hit stop, sound coherence, camera control separate top 8 from bottom 8; Guilty Gear Xrd hit-stop frames [V: confirmed - arXiv v3 Aug 2022, 44 games, 280K comments, 7/10 frames and 39th/40th rows found in text; preprint label correct] |
| S4 | Good Game Feel: An Empirically Grounded Framework for Juicy Design (DiGRA 2018) | Hicks, Dickinson, Holopainen, Gerling | 2018 | A | https://dl.digra.org/index.php/dl/article/view/936 | YES (2018). Newer: S1 tests parts of it (A4, B3, C3, C4.A) and partly supports | survey of 17 developers; juice framework A1-C4 (consistency, exaggerate, multimodal, unambiguous, relevant); redundancy can overwhelm [V: confirmed - DiGRA 2018, 17 developer survey on dl.digra.org] |
| S5 | Rec. ITU-R BT.1359 Relative timing of sound and vision for broadcasting | ITU-R | 1998 | A (standard) | https://itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1359-0-199802-S!!PDF-E.pdf | YES (1998, speech/newsreader basis). Newer: S6, S8 show non-speech tolerances differ | detectability +45 to -125 ms, acceptability +90 to -185 ms (positive = sound ahead) [V: confirmed - thresholds +45/-125 detect, +90/-185 accept, sign convention, +22.5/-30 all in the Rec text] |
| S6 | A subjective study of the perceptual acceptability of audio-video desynchronization in sports videos (arXiv 2212.01686) | Ebenezer | 2022 | A-preprint (label "preprint") | https://arxiv.org/pdf/2212.01686 | no | 20 subjects, 45 videos; non-speech tolerates far more offset than speech; sound-leads-picture is more annoying than picture-leads-sound [V: confirmed - 20 subjects, 45 videos, audio-leading more annoying] |
| S7 | Behavioural evidence for separate mechanisms of audiovisual temporal binding as a function of leading sensory modality (Eur J Neurosci 43(12)) | Cecere, Gross, Thut | 2016 | A | https://pmc.ncbi.nlm.nih.gov/articles/PMC4915493 | YES (2016). Newer confirmation not searched (budget) | n=30 analysed; sound-lead discrimination better than picture-lead: d' 1.58 vs 0.98; picture-lead trainable, sound-lead not [V: confirmed - n=30 of 34, d prime 1.58 vs 0.98, Eur J Neurosci 43(12)] |
| S8 | Perceived synchrony for realistic and dynamic audiovisual events (Front Psychol 6:736) | Eg, Behne | 2015 | A | https://pmc.ncbi.nlm.nih.gov/articles/PMC4451240 | YES (2015) | n=19; chess (action), drums, speech; window of integration FWHM 432 ms (1 s clips) vs 317 ms (13 s); PSS spread about 100 ms sound-lead to 250 ms sound-lag across people [V: confirmed - n=19, FWHM 432/317 ms, PSS spread about 100 ms lead to 250 ms lag] |
| S9 | The Effects of Auditory Latency on Experienced First-Person Shooter Players (ACM 2022) | Halbhuber, Kohler, Schmidbauer, Wiese, Henze | 2022 | A | https://doi.org/10.1145/3543758.3543760 (PDF https://epub.uni-regensburg.de/53766/1/3543758.3543760.pdf) | no | n=24, CS:GO, audio delay 0/40/270/500 ms; 40 ms no effect; 270 ms raised tension (p=.003 vs 0 ms); 500 ms lowered positive affect, raised negative affect and tension; no performance effect [V: corrected - 270 ms raised tension only; positive affect and negative affect changed only at 500 ms] |
| S10 | Good Feedback for Bad Players? A preliminary study of 'juicy' interface feedback (FDG/DiGRA 2016 poster) | Juul, Begy | 2016 | A (poster; abstract page only read, not full text) | https://adk.elsevierpure.com/da/publications/good-feedback-for-bad-players-a-preliminary-study-of-juicy-interf | YES (2016). Newer: S1 supports "juice can detract" | juicy version rated higher but players performed worse; n not on page [V: confirmed - peer-reviewed poster, FDG/DiGRA Aug 2016, juicy rated higher, performed worse; full text not read] |
| S11 | 10 Design Tips from the League of Legends VFX Style Guide | VFX Apprentice (summarising Riot style guide, Jin Ho Yang) | 2022 | C (secondary summary of tier-A 2017 guide; primary guide NOT opened: nexus URL redirected to homepage) | https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips | summary 2022; underlying guide 2017 = pre-2020 | scale effect to importance (basic attack vs ultimate); anticipation then payoff then room to process; do not linger; reduce clutter |
| S12 | Flipbook Frame offset on muzzle flashes for greater variations | jqarlsson (realtimevfx.com) | 2025 | C (single source; second source needed) | https://realtimevfx.com/t/flipbook-frame-offset-on-muzzle-flashes-for-greater-variations/28301 | no | random start frame plus random frame count per particle; about 16-frame flipbook usually enough; start+range must not exceed frame count |
| S13 | Roblox Creator Docs ParticleEmitter (local mirror) | Roblox | current | Spec | knowledge/external/roblox-creator-docs/_api-reference/classes/ParticleEmitter.yaml | n/a | FlipbookStartRandom, Rotation [0,360], RotSpeed, Rate semantics. Engine capability only, not design evidence |

Tier counts read: A peer-reviewed/standard = 6 (S1, S4, S5, S7, S8, S9) plus S10 (abstract only); A-preprint = 3 (S2, S3, S6); B = 0; C = 2 (S11, S12); spec = 1 (S13). Total opened = 13.

## 2. Findings

### 2a. Juice and satisfaction table

| quality or finding | why it works (or fails) | how to make it | game uses | effect size if known | evidence level |
|---|---|---|---|---|---|
| Feedback only on success (success-dependent amplification) | Player can link feedback to a skilled outcome; competence rises; also raised curiosity and effectance (S1) | Fire the big hit VFX/sound only when a hit lands. A miss or a swing gets a small cue only. Brick game: blast ring/dust only on an actual brick break | Weapon swings, projectile hits, brick break, kills, pickups | S1 Model B (n=1,699, unstandardised coefficients on 7-pt scales): success-dependence -> competence +.45 (p<.001), effectance +.26 (p<.001), curiosity +.29 (p<.001). No direct effect on enjoyment or playtime; effect goes through mediators. Mean voluntary playtime: lowest 6.17 min (standard feedback), highest 10.18 min (amplified + success-dependent, non-varied) | study (pre-registered) [V: confirmed - .45/.26/.29 and 6.17/10.18 min match S1; note effectance .26 and curiosity .29 were exploratory paths, and 10.18 min is the A+SD-V cell] |
| Amplifying feedback on mere acting (not on result) can hurt | Amplified swing effects engulfed hit/kill feedback and hid cause and effect. Authors' explanation: blocked "outcome binding" (seeing that my action caused that event). A proposed explanation, not proven (S1 sec 5.1, 6) | Keep action feedback small and legible; never let swing/launch effects cover the impact point. Keep a hierarchy: minor action < success < big success | Anything that fires on input before result: charge-up, trigger, throw | S1 Model A (n=678): amplified vs standard -> effectance -.19 (p<.05), competence -.43 (p<.001). No direct effect on enjoyment or playtime | study (pre-registered); mechanism = authors' inference [V: confirmed - Model A n=678, -.19 p<.05, -.43 p<.001] |
| "More juice is better up to a point" (inverted U) | Kao 2020 as reported: medium and high juice beat extreme and the lowest level on player experience, motivation, playtime, performance. NOT read first-hand (S1, S2 report it) | Design at medium-to-high, never extreme; the CHI 2024 result adds that what the juice is tied to matters more than the amount | Tuning global VFX intensity | Kao 2020 n=3,018 between-subjects (per S1). Per-measure effect sizes: no number found (paper not read) | study, second-hand (S1, S2) [V: unverified - Kao 2020 not opened. S1 confirms n=3,018 and "medium and high outperformed low and extreme"; S2 says "absence of juiciness", so comparison group still unresolved] |
| CHI 2024 does not overturn the inverted U but changes the lever | S1 shows amplified (louder) feedback was neutral-to-negative on its own (no enjoyment gain, lower competence and effectance) when not tied to success. It tested one amplified level vs standard, not a dose-response, so it can neither confirm nor deny the exact peak | Treat the knob as "what the feedback is tied to and how readable it is", then amount | Review rule: do not raise intensity to fix a flat hit; first check readability and success-linking | See rows above | study + inference |
| Curiosity is the strongest predictor of staying | In S1, each +1 curiosity point -> +.75 (Model A) / +.76 (Model B) enjoyment and +.88 / +.86 min extra playtime (10.8% of mean 7.9 min). Enjoyment itself did not predict playtime | Feedback that is learnable but not fully predictable: graded outcomes (small/medium/big by real cause: material, force, weak point) so the player learns a rule | Graded blast sizes, material-based break effects, crits | curiosity -> enjoyment .75, p<.001; curiosity -> playtime .99 (Model A exploratory) / .86 (Model B), p<.001 | study; "learnable rule" = authors' interpretation [V: confirmed - .75/.76, .88/.86 min, 10.8% of 7.9 min, enjoyment not linked to playtime are in S1 text. Note: paper also reports Model A curiosity->playtime coefficient .99 while its text says .88; both appear in the paper] |
| Hit stop (freeze frames on impact) | Separates miss from hit and light from heavy; games without it were described as dull (S3) | Light hits short freeze, heavy hits longer. Example: Guilty Gear Xrd light attack 7 frames, heavy about 10 frames (S3, citing Arc System Works material). At 60 fps that is about 117 ms and 167 ms (inference, arithmetic) | Melee, big explosions, boss hits, brick-wall breaks | Two games without hit stop (Sacred Citadel, Draw Slasher) ranked 39th and 40th of 44; players' "IF attitude" below 70% for those. Ranking from NLP on 280K comments; correlational | preprint (S3); industry practice for frame counts [V: confirmed - 7 and about 10 frames, Sacred Citadel and Draw Slasher 39th/40th, "less than 70%" IF attitude; correlational as stated. 117/167 ms arithmetic correct] |
| Sound-vision coherence | Delay between visual hit and hit sound makes impact feel unnatural (S3, one of three strongest features) | Fire the sound on the same frame as the visual impact; see AV sync table | Every hit | No number beyond top-8 vs bottom-8 comparison (16 games) | preprint |
| Camera control on big events | All 3 high-ranked beat-em-ups used dedicated camera control, neither of the 2 low-ranked did (S3) | Zoom/shake/push on heavy hits and finishers, scaled to event size | Big blasts, boss, finisher | n = 5 beat-em-ups; no effect size | preprint |
| Clean cause and effect (unambiguous, relevant, coherent hierarchy) | Hicks framework: feedback should reflect event importance (A4), highlight in harmony (B3), be unambiguous (C3), be relevant to game-critical events (C4.A). S1 partly tests it and finds violating it hurts | Hierarchy table per game: tiny / normal / big / rare. Same tier = same visual weight | VFX review checklist | S1 as above | industry practice (S4, 17 developers) + study (S1) |
| Scale effect to importance | A basic attack as big as an ultimate confuses the viewer and makes the ultimate less satisfying (Riot style guide per S11) | Size, brightness, duration, screen area all grow with importance | Every effect class | no number found | industry practice (Riot 2017 via tier-C summary; primary not opened) |
| Anticipation, payoff, room to process | Build before the hit, deliver at the moment the viewer expects, then give a moment to process (S11) | Windup frames before punch; do not stack more into the punch than the eye can read | Charged shots, C4 fuse, boss attacks | no number found | industry practice (tier-C summary) |
| Do not linger | Long dissipation clutters combat; short effects leave space for others (S11) | Short tails on frequent effects; long tails only on rare big effects | All dust/smoke/trails | no number found | industry practice (tier-C summary) |
| Slickness: smooth, responsive, natural | Developers describe good feel as smooth animation curves, immediate reaction, natural elements working together (S4) | Use easing curves rather than linear; start reaction on the input frame | UI pops, pickups, scale-ups | none (qualitative, n=17 developers) | industry practice |
| Redundancy helps until it overwhelms | Developers say redundant feedback is part of juice but can "overwhelm" (S4); S10: juicy version rated higher but players performed worse; S1: amplification neutral/negative without success link | Cap simultaneous layers per event (suggest 3 to 4: shape, flash, sound, shake; this count is my suggestion, no source gives one) and test performance, not only liking | Review: count layers per hit | S10: n not found on page; direction only | industry practice (S4) + study (S10, S1) |
| What makes effects feel cheap / mushy / floaty / delayed / noisy / annoying | From S3, S1, S4, S11: no hit stop (mushy); sound out of sync (unnatural); no camera work (flat); swing effects hiding impact (ambiguous); basic attacks as big as ultimates (noisy, devalues big events); lingering tails (clutter); everything loud (no hierarchy). "Floaty" and "cheap": no tier-A source defines them | Use as a review checklist: each item is a yes/no test | VFX reviewer agent | none | inference from studies; practitioner terms undefined in sources |
| Juice for mere action vs "feels like I did it" | Authors propose outcome binding as a precondition for competence. Not tested directly | Keep clear time order: input, then effect inside the response window (S9 gives audio bounds) | Inputs | none | inference (authors' hypothesis) |

### 2b. Repetition table

| technique | numbers | source |
|---|---|---|
| Random start frame per particle (Roblox) | `FlipbookStartRandom = true`; with `FlipbookFramerate = 0` each particle is a static random frame of the sheet | S13 (spec) |
| Random rotation per particle (Roblox) | `Rotation` range commonly `[0, 360]` for fully random start angle; `RotSpeed` = random range of degrees/second chosen at emission | S13 (spec) |
| Random segment of a flipbook (Unity technique) | Each particle plays a random segment: random start frame plus a frame-count range; start + range must not exceed frame count; about 16 frames "usually enough" per the author; example plays 4 frames. Single tier-C source, needs a second source before we rely on it | S12 (tier C) |
| Random variety in feedback (many swing/hit/death effects instead of one) | Effect on enjoyment: small positive, +.11 (p<.05). Effect on curiosity: none. No effect on competence or effectance. Authors: random variety in feedback is "unlikely to enhance player experience" (paraphrase); not a satisfaction driver, only a cosmetic hedge against repetition. Short session, minimum 10 min | S1 (study) [V: confirmed - enjoyment .11 p<.05, no curiosity link; paraphrase of authors not re-checked] |
| Number of variants needed | no number found. S1 compared "one effect per feature" vs "many" but did not state a count | S1; gap |
| Random size / colour / timing ranges | no number found in any opened source | gap |
| Toning down repeated effects | no number found. Principle only: short tails on frequent effects, scale to importance | S11 (tier C, Riot 2017 via summary) |
| Caps and cooldowns on identical effect | no number found. Engine control available: `Rate` = particles per second (rate 5 = one per 0.2 s) | S13 (spec) |
| Combo/streak escalation (step size, number of steps, reset time) | no number found. Constraint from S1: escalation should be tied to a real success and stay readable; amplifying non-success feedback lowered competence (-.43) and effectance (-.19). S1 lists "differentiable gradations of success feedback" as future work, so step count is untested | S1 (study); inference for design |
| Escalation must not occlude | In S1 the amplified swing visually covered the hit/kill effect (Fig 5 of paper). Rule: higher tiers add to the impact point, never cover it | S1 (study) |
| Every-second effects (gunfire flashes, footsteps, coin pickups) | no number found. No tier-A studio talk opened for this | gap |
| Habituation in general | A 2022 Cortex study of sound trains appeared in a search snippet only, NOT opened. No claim made | lead only |

### 2c. AV sync table

Sign convention: positive = sound ahead of picture (S5 states this). "Sound-lead" = sound before picture.

| finding | ms | source | evidence level |
|---|---|---|---|
| Broadcast detectability threshold (speech/news, average) | detect from +45 (sound early) to -125 (sound late) | S5 ITU-R BT.1359 (1998) | study (standard) [V: confirmed] |
| Broadcast acceptability threshold | +90 (sound early) to -185 (sound late) | S5 | study (standard) [V: confirmed] |
| Recommended broadcast chain tolerance | +22.5 (sound early) and -30 (sound late) | S5 | spec/standard [V: confirmed] |
| Sound-early is worse than sound-late | acceptability lower for sound-leads-picture than picture-leads-sound at same offset | S6 (preprint, 20 subjects) | preprint [V: confirmed] |
| Non-speech content tolerates much more offset | acceptability score 50 reached at sound-lead of: newsreader 200 ms; cricket 500 ms; soccer 1 s; tennis 1 s; football 1.3 s | S6 | preprint [V: confirmed - 200 ms, 500 ms, 1 s, 1.3 s, 1 s all in S6 text] |
| Sound-lead is detected better than picture-lead (sensitivity) | d' 1.58 (sound-lead) vs 0.98 (picture-lead); picture-lead sensitivity improved with training (d' 1.13 -> 1.57; 0.83 -> 1.48), sound-lead did not | S7 (n=30 analysed; 10 ms flash plus 10 ms 1800 Hz tone, offsets 50-500 ms) | study [V: confirmed] |
| Typical binding window widths cited | about 200-250 ms for picture-lead and 100-150 ms for sound-lead (cited by S7 from the literature, not measured in S7) | S7 (secondhand) | study, cited |
| Realistic action event vs speech | window of integration (FWHM) 432 ms for 1 s clips and 317 ms for 13 s clips; chess window about 60 ms wider than speech (not significant after correction); point of subjective simultaneity differed between people by more than 200 ms, about 100 ms sound-early to 250 ms sound-late | S8 (n=19) | study [V: confirmed] |
| Game audio delay vs experience (CS:GO, within-subject, n=24) | 0 and 40 ms: no effect on experience. 270 ms: higher tension only (no significant positive-affect drop vs 0 ms). 500 ms: lower positive affect, higher negative affect and tension; experts more tense at 500 vs 0 ms (p=.041). No significant effect on score at any delay | S9 | study [V: corrected - positive affect fell significantly only at 500 ms (vs 0 and 270); 270 ms: tension higher (0 vs 270 p=.003); 40 ms no effect; expert tension 0 vs 500 p=.041; score F p=.154 not significant] |
| Experts notice | All expert players could tell the audio was manipulated (S9 qualitative notes). Which level they noticed: no number in what was read | S9 | study |
| Visual latency context | visual latency above 25 ms said to reduce game experience (cited in S9 from earlier work) | S9 (cited) | study, cited [V: confirmed - 25 ms claim is in S9 abstract/intro, cited from earlier work] |
| Sound before or after picture? | Evidence says slightly late sound is safer than early sound. Practical rule for a Roblox hit: schedule sound on the same frame as the flash; if drift is unavoidable, let the sound arrive 0 to about 45 ms after the picture, never before | S5, S6, S7 combined | inference |
| One frame as a unit | at 60 fps one frame = 16.7 ms; at 30 fps 33.3 ms. Sound within 1 to 2 frames of the flash is inside the S5 detectability band | arithmetic on S5 | inference |
| Who shares the work | S3: sound coherence is one of three strongest impact-feel features; S4: multimodal feedback (visual, audio, haptic) at once. No tier-A source found on division of labour. Our split (sound carries weight and the transient; picture carries shape and size) is a design rule, not evidence | S3, S4 | preprint, industry practice; split = inference |
| Roblox-specific audio latency | no number found in opened sources | gap | n/a |

## 3. Quotes used (15 words or fewer)

| quote | attribution |
|---|---|
| "excessive amounts of feedback in relation to user input" | Juul, quoted in S1 (Kao et al. 2024), defining juiciness [V: confirmed - 8 words, in S1] |
| "Juice alone isn't enough" | developer respondent, S4 (Hicks et al. 2018) [V: unverified - S4 full text not opened] |
| "if it's distracting, then the effect isn't doing its job" | VFX Apprentice summary of Riot guide, S11 [V: unverified - S11 not re-opened] |

## 4. Conflicts between sources

| topic | older | newer | what changed / resolution |
|---|---|---|---|
| Is amplified juice good? | Juul and Begy 2016 (S10): juicy rated higher but performed worse; Hicks 2018 (S4): redundancy can overwhelm | Kao CHI 2024 (S1): amplified feedback alone lowered effectance and competence, no enjoyment gain | Newer evidence is stronger (pre-registered, n=1,699). Use S1: tie juice to success, keep readable |
| Kao 2020 comparison group | Survey S2 and secondary summaries: medium and high beat "extreme" and "absence of juiciness" (none) | S1 (2024, citing Kao 2020): "medium and high ... outperformed low and extreme" | Wording differs (none vs low). Original not read; cannot resolve. Safe statement: medium and high beat both the lowest and the extreme condition |
| Does random variety help? | Practitioner view (Deterding 2015, per S1): unexpected variety stokes curiosity | S1: random variety gave no curiosity gain, enjoyment +.11 only | Newer first: do not rely on variety for satisfaction; use it only against repetition |
| Why too much feedback hurts | Juul 2009 per S1: extraneous cognitive load | S1: more likely blocked outcome binding | Authors argue load theory is misapplied. Hypothesis only |
| AV sync tolerance | ITU 1998 (S5): +45/-125 ms detection (speech) | S6 2022: non-speech tolerates 200 ms to over 1 s before acceptability falls to 50; S8 2015: wide windows for action | Broadcast numbers are a strict bound for speech; for impacts use game data (S9) |
| Which direction is worse | ITU 1998: detect sound-early at +45, sound-late at -125 | S6, S7 agree sound-early is worse | Consistent. Aim for sound on, or slightly after, the picture |

## 5. Gaps (and how we could test)

| question | status | self-test |
|---|---|---|
| Per-measure effect sizes for the Kao 2020 conditions | Paper not readable (403). Only the headline result found | Ask owner for the PDF or open it from a university network |
| Where is the peak between medium and extreme for brick-break VFX | no number found; S1 did not test dose-response | Studio: one blast at 3 intensity levels, owner picks; log chosen levels |
| Number of variants to avoid repetition | no number found | Fire the effect 100 times at 1 per second; owner notes when it reads as repeat. Test 1, 3, 6 variants |
| Random size/colour/timing ranges | no number found | A/B with 0%, 10%, 25% scale/rotation/tint spread |
| Caps/cooldowns for frequent effects | no number found | Measure particle count and frame time with 1, 5, 20 simultaneous bursts on a phone |
| Combo escalation steps and reset time | no number found | Prototype 3 to 5 tiers; test whether players can name the tier without UI |
| Every-second effects at studios (gunfire, footsteps, coins) | no tier-A source opened | Next researcher: GDC Vault and Epic/Insomniac/DICE talks (search budget used up here) |
| Roblox audio-to-visual latency | not in spec reading | Studio test: flash a part and Sound:Play on the same frame; record screen and audio, compare waveform offset to frame |
| Habituation timing for VFX | not found | Long playtest of one weapon, 1000 shots, ask owner at 100, 500, 1000 |
| Primary Riot VFX style guide | nexus URL redirected; S11 is a secondary summary | Fetch the PDF from another route or ask owner |

## 6. Leads not followed

| lead | why not |
|---|---|
| Kao, "The Effects of Juiciness in an Action RPG", Entertainment Computing 34 (2020), https://www.sciencedirect.com/science/article/pii/S1875952119300850 | 403; only second-hand via S1/S2 |
| Schmid et al. 2024, JND for audio latency (snippet: mean 49 ms at 0 ms base, 27 ms at 64 ms, 77 ms at 512 ms), https://epub.uni-regensburg.de/59003/1/JND_Audio_Latency.pdf | snippet only; page returned 404 |
| Vatakis and Spence 2006 (music vs speech), Dixon and Spitz 1980 (hammer-and-nail window about 75 ms lead to 188 ms lag) | search snippets only; not opened |
| Stevenson and Wallace 2013 (speech binding window about 250 ms picture-lead, 150 ms sound-lead) | cited via Frontiers 2023 snippet; PDF fetch returned a logo file |
| "That Sound's Juicy!" (IFIP 2023, juicy audio and presence), https://dl.ifip.org/hal-04144377v1 | only abstract skimmed |
| Fabre et al., Juicy Text, arXiv 2512.13695 (ICMI 2024) | first page only; results not read |
| Jonasson and Purho, Juice it or Lose it (2012); Nijman, Art of Screenshake (2013); Eiserloh, Juicing Your Cameras (GDC 2016) | pre-2020 talks, video only; no transcript found before search budget ended |
| Singhal and Schneider, juicy haptics (CHI 2021) | not opened; outside scope |
| bugnet.io combo-system blog, wayline.io juice blogs, mechanicsofmagic.com | tier D, leads only |
| Cortex 2022 repetition suppression to sound trains | snippet only |

## Verification log

Checked 27 rows or claims against the sources (S1, S3, S5, S6, S9 PDF text; S7, S8 via PMC; S2, S4, S10 abstract pages). Confirmed 22, corrected 2 cells (one S9 finding), unverified 3. No claim was removed as false.

| item | result | reason |
|---|---|---|
| S9 "270 ms lowered positive affect" (source row, 2c row, and the researcher summary item 4) | corrected | Wilcoxon: positive affect differs only 0 vs 500 ms (p=.041) and 270 vs 500 (p=.017). At 270 ms only tension rose (0 vs 270, p=.003). Negative affect differs only 0 vs 500 (p=.048). |
| Kao 2020 comparison group ("none" vs "low") | unverified | Paper not opened. S1 text says "low and extreme"; S2 says "absence of juiciness". Do not quote either as fact. |
| Quote "Juice alone isn't enough" (S4) | unverified | S4 full text not opened. |
| Quote from S11 (Riot summary) | unverified | S11 not re-opened; tier C. |
| S1 curiosity->playtime Model A | note | Coefficient .99 in the model figure text, .88 in the discussion (the figure used for the 10.8%). Keep both visible. |
| S1 effectance .26 and curiosity .29 | note | Labelled Model B but reported as exploratory paths, not pre-registered hypotheses. |
| S3 "preprint" | confirmed | arXiv v3; also a conference paper (venue not re-checked). All S3 results stay correlational (ranking from comments, n=44 games; camera control n=5). |

Gaps and missing tier-A sources:
- Part 6 (repeats, variant counts, cooldowns) has no tier-A number. The Schmid 2024 audio-latency JND paper (Regensburg) would be a useful tier-A addition for the sync table; it was never opened.
- ITU-R BT.1359 is a speech/news standard from 1998; the file marks this, but the "never sound before picture" design rule rests on S6, a 20-subject preprint, and S7 (flash and tone, not impacts).
- S9 is one game (CS:GO), 24 players, with audio delay only; it does not cover Roblox or hit sounds.
- S10 has no sample size; treat it as direction only.

