> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Rewards, juice and honest outcomes

Core rules used here (in SKILL.md): S-194 frequent reward tiers, S-59 bands and gaps, S-60/S-61/S-62 ladder,
S-64 one hero sound per achievement, S-114 key, S-134 honest fail glide, D-01 to D-08 guardrails.
Pickup, collect, coin and sell recipes: `craft-satisfying.md` §B.

## A. Pitch ladder table (=)

PlaybackSpeed = 2^(st/12); it also shortens the sound (S-144).

| Step | Pentatonic st (with music) | Speed | Chromatic st (no music) | Speed |
| --- | --- | --- | --- | --- |
| 1 | 0 | 1.000 | 0 | 1.000 |
| 2 | +2 | 1.122 | +1 | 1.059 |
| 3 | +4 | 1.260 | +2 | 1.122 |
| 4 | +7 | 1.498 | +3 | 1.189 |
| 5 | +9 | 1.682 | +4 | 1.260 |
| 6 | +12 (cap, hold) | 2.000 | +5 | 1.335 |
| 7-8 | hold | 2.000 | +6, +7 (cap at 8 steps) | 1.414, 1.498 |

Pentatonic is safe only as the pentatonic of the track's own key. Ladder jitter stays ±0-30 cents (S-90).

## B. Celebration and build rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-53 | Rare earned celebrations scale with tier: small 1.5 s, medium about 4 s, rare up to 12 s. Shorten or allow skip after the 10th repeat inside 60 s. (P middle tier, skip) | study (ends) + inference |
| S-54 | Level-up or boss defeat: riser 2-4 s, hit about 1.5 s, gap 300-1000 ms (P), tail about 5 s carrying the reward UI. | practice |
| S-55 | Pre-payoff gap: 1 beat at current BPM (500 ms at 120, 375 ms at 160); 2-4 beats for bigger moments. Test 200/500/1000 ms by "impact" rating. | practice + inference |
| S-56 | Pulse into a payoff doubles each bar: 1, 2, 4, 8 per beat. | practice |
| S-57 | Riser envelope: attack about 50 ms (no click), release about 1000 ms. | practice |
| S-58 | During a build, narrow stereo toward mono and filter highs; open to full width + sub on the payoff. | practice |
| S-63 | Score tally: one ascending note per counted item about 50 ms apart; last item adds a bass drop. (P) | inference (secondary) |
| S-71 | One braam-class stinger per major reveal; never the same signature hit more than once per minute. | practice |
| S-72 | Rotate stinger families per area; no single signature hit for everything (trailer devices wear out, M-16). | practice |
| S-195 | Every cue carries an event-semantic field (earned item, currency spent, net loss, cancelled, no gain); sound follows semantics, never marketing value. | inference |

## C. Sonic identity

| ID | Rule | Evidence |
| --- | --- | --- |
| S-68 | Logo family: signature about 3 s, UI confirm about 1.3 s with ≤6 notes, launch version 10-16 s; same final motif in all. | practice (Mastercard, Netflix) |
| S-69 | A hummable logo has 3-5 notes and a rhythm matching the game-name syllables. Test sung recall after 1 day. | practice + lead |
| S-70 | Unlock or loading swell: noisy cluster drifting 5-6 s, landing on stacked octaves with a rising low-pass; total 10-15 s. (P) | practice (recreation) |
| S-197 | Original 3-5-note motif; 0.8-1.5 s master + 150-300 ms UI derivative; fixed invariants (contour, rhythm, one timbral feature). Never sample or imitate famous logos. (P) | lead |

## D. Honest outcome rules (expand D-01 to D-08)

| ID | Rule | Evidence |
| --- | --- | --- |
| S-161 | Win or celebration sound only when net value > 0 (payout > cost). Test: every reward trigger reads a net-value check. | study |
| S-162 | Net loss or below-cost result gets a distinct neutral or low "no gain" sound. Removing the win sound is not enough (silence 42.3% vs 33.3% called a loss, not significant). | study |
| S-232 | Audit outcome meaning: play every outcome sound without context; a no-gain sound passes only if most listeners classify it as not positive (15 of 19 "different" slot sounds still read positive, N=400). | study |
| S-163 | A win sound sits next to the plain number won (sound inflated remembered wins +24% vs +15%). | study |
| S-164 | Paid random reveals: build-up equal in length for every outcome; no near-miss, fake-out or extra hype on paid pulls; result sound honest and scaled to real value by note count, register and tail (≤2× the shortest), never by level (within 1 LU); below-cost outcomes follow S-162. Under-13 or restricted regions: no countdown tension, no jackpot siren on paid rolls. | inference (ethics) + study |
| S-168 | Free random rewards follow the same honest-reveal rule (odds disclosure not required). | practice + inference |
| S-170 | No fake social proof; only real events, in true proportion. | inference (ethics) |
| S-171 | Shops: calm, unhurried UI sound, same tone at every price; no tempo or arousal ramp in purchase flows. | inference + study |
| S-233 | Urgency cues only for real deadlines or hazards, stopped when they end; never on purchases or paid random items. | inference (ethics) |

Fair alternatives for the banned methods:

| ID | Fair alternative |
| --- | --- |
| D-01 | Neutral "result" tick + the net number; celebrate only on net gain |
| D-02 | Deterministic progress cue: a bar plus a rising tone showing true distance, resolving when reached (S-33) |
| D-03 | Equal build-up, odds shown before purchase, honest proportional result; big stingers for earned milestones |
| D-04 | Calm shop sounds, same tone at every price |
| D-05 | Real events only, in true proportion |
| D-06 | Rate-limit; warn only when the player can act |
| D-07 | Replace countdowns and sirens with the same short neutral build for every outcome |
| D-08 | Urgency only for real deadlines, stopped when they end |

## E. Methods behind these rules

| ID | Source | Extra fact not in a rule |
| --- | --- | --- |
| M-33 | Peggle Blast | Whole game audio under 5 MB; one asset pitched up over 0.5 s replaces many assets |
| M-34 | Candy Crush | +1 st per extra cleared row |
| M-35 | Balatro (third-party analysis) | C-D-E-F-G per scored card, about 50 ms apart, bass drop at the threshold |
| M-36 | The Finals | Kill sound tuned for timing, band and money association (cash register, bell) |
| M-49/M-50 | Slot studies | Win sound raised skin conductance; 72.5% prefer sound on; jingle length scales 1.5-12 s with win size |
| M-52 | Slot "chase" music | Fair use only with a visible deterministic timer; never near-miss |
| M-77 | Candy Crush refresh 2022 | Reward families re-tested against every music state; short or skippable celebrations (lead) |
| M-78 | Vampire Survivors | Routine pickups brief and rate-limited; milestone celebrations separate (lead) |
| M-85 | UK slot rule RTS-14F | Banned win sounds at or below stake; operators kept other celebratory sounds, still heard as positive |

Also traced: M-14 → S-71; M-15 → S-54; M-17 → S-57, S-58; M-18 → S-55; M-19 → S-56; M-22, M-25 → S-68;
M-23, M-26 → S-69; M-24 → S-70; M-84 → S-197; M-51 → D-01; M-53 (casino floor layers action, win, fail, bed: a
checklist only); M-92 boss entrance: motif 0-3 s, build 3-7 s, 0.25 s negative space, hit, settle (P, lead).

Gaps: G-05 ladder step, cap, reset (A/B 1 st vs scale step, reset 1.0 vs 1.5 s; telemetry on SFX volume changes).
G-29 outcome confusion (confusion matrix earned / neutral / loss; reject cues that move losses toward "win").
