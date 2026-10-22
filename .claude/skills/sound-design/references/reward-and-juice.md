> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# Rewards, juice and honest outcomes

Rules S-194, S-59, S-60/S-61/S-62, S-64, S-114 and S-134 live in §B (moved from SKILL.md in J018); guardrails
D-01 to D-08 stay in SKILL.md §4. Attempt cue on input, reward layer on the confirmed result: SKILL.md S-150/S-219.
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
| S-194 | Frequent feedback tiers: A pickup 60-120 ms; B chain or subgoal 150-300 ms; C milestone 500-1000 ms. Merge floods into one audible confirm per merge window (the feature spec's, about 100 ms [P]) while the visual count stays exact. In play a celebration ends before the next decision (under about 2 s [P]); longer ones (S-53) only on non-play screens. Tiers and rates follow the progression designer's reward tier table: T1 → A, T2 → B, T3 → C, T4 → the rare tier of S-53; the rate is the table's measured rate. | inference; P |
| S-59 | Reward cues use bands outside the action midrange (below 200 Hz, above 4 kHz) and land in gaps between loud transients. | practice |
| S-60/S-61/S-62 | Pitch ladder: with music, walk the track's scale (pentatonic 0, +2, +4, +7, +9, +12 st); without, +1 st per step (PlaybackSpeed ×1.0595). Cap 8 steps or +12 st, then hold. Reset after 0.8-1.5 s idle. | practice step; P cap and reset |
| S-64 | One signature hero sound per major achievement type, the same every time, used rarely. No sound on very frequent trivial actions. | inference, lead |
| S-114 | One key per music track, stored as data. Pitched reward, UI and ladder sounds use notes of that key; shift at most ±6 st. | practice; P ±6 |
| S-134 | Honest fail or no-gain cue: falling glide of about an octave, low register, rich harmonics (template 131 → 69 Hz over about 1.5 s; UI versions shorter), partials above 300 Hz, quieter than rewards. | study |
| S-53 | Rare earned celebrations scale with tier: small 1.5 s, medium about 4 s, rare up to 12 s. In play a celebration ends before the player's next decision (under about 2 s (P), S-194); the 4-12 s versions run only on non-play screens (results, unlock, reveal). Shorten or allow skip after the 10th repeat inside 60 s. (P middle tier, skip) | study (ends) + inference |
| S-54 | Level-up or boss defeat: riser 2-4 s, hit about 1.5 s, gap 300-1000 ms (P), tail about 5 s carrying the reward UI. | practice |
| S-55 | Pre-payoff gap: 1 beat at current BPM (500 ms at 120, 375 ms at 160); 2-4 beats for bigger moments. Test 200/500/1000 ms by "impact" rating. | practice + inference |
| S-56 | Pulse into a payoff doubles each bar: 1, 2, 4, 8 per beat. | practice |
| S-57 | Riser envelope: attack about 50 ms (no click), release about 1000 ms. | practice |
| S-58 | During a build, narrow stereo toward mono and filter highs; open to full width + sub on the payoff. | practice |
| — | Counters: a count-up plays no sound per digit; flying coins tick on the first few arrivals and one closing sound on the last; same-kind gains in one merge window share one sound (S-194). | inference |
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
| S-164 | Paid random reveals: the rule is SKILL.md D-03 (one windup, no near-miss or fake-out, result scaled to real value by note count, register and tail, never by loudness or peak) and D-07 (no countdown tension or siren on any paid roll); below-cost outcomes follow S-162. | inference (ethics) + study |
| S-168 | Free random rewards follow the same honest-reveal rule (odds disclosure not required). | practice + inference |
| S-170 | No fake social proof; only real events, in true proportion. | inference (ethics) |
| S-171 | Shops: calm, unhurried UI sound, same tone at every price; no tempo or arousal ramp in purchase flows. | inference + study |
| S-233 | Urgency cues only for real deadlines or hazards, stopped when they end; never on purchases or paid random items. | inference (ethics) |

Fair alternatives for the banned methods:

| ID | Fair alternative |
| --- | --- |
| D-01 | Neutral "result" tick + the net number; celebrate only on net gain |
| D-02 | Deterministic progress cue: a bar plus a rising tone showing true distance, resolving when reached (S-33) |
| D-03 | One shared windup asset for every tier, odds shown before purchase (`platform-policy`), honest proportional result after the result frame; tap to skip after the result; in a batch open only the best result gets the full ceremony; big stingers for earned milestones |
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
