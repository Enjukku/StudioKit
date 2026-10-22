> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# Repetition and fatigue

Rules S-88/S-89, S-90/S-91, S-94, S-100 and S-101 live in §B (moved from SKILL.md in J018); S-79/S-202 burst scaling
and S-152 voice caps stay in SKILL.md §3. Vary samples, never the meaning: tells, warnings and countdowns get no
jitter (SKILL.md SC-12).

## A. Repetition plan procedure

1. Estimate plays per minute and max burst per second for the cue (cue-card field 34).
2. Variant count from the rate (S-88). Shuffle-bag with exclusion (S-89); simulate it (S-204).
3. Jitter by cue type (S-90/S-91); random pitch at one level only (S-92); none on tells, warnings, countdowns; never jitter the timing of a meaningful cue.
4. Retrigger floor (S-94); above about 8 plays/s switch to start + loop + tail (S-95); above 15 events/s aggregate
   into one grouped sound per window (S-66, S-194).
5. Voice cap and steal policy (S-152).
6. Machine-gun test (S-96), then a real-loop test (S-205). I cannot listen: the 10 s storm and the real loop are check-in C listens (`review.md` §2); the 1,000-selection fixture (S-204) and the debug cue log at the burst rate (`review.md` R-41) are mine.
7. If the cue is heard 1,000+ times a session, keep it short, quiet relative to rare cues, and meaningful (S-97, S-98).
8. Beds and long loops: splice several takes with crossfades and a short fade on every splice (`craft-process.md` §6); seam ratio and length measured (`review.md` R-26).

## B. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-88/S-89 | Variants: over 2 plays/s → 4-10 (start 6); moderate → 3-5; under 1/min → 1-3; scares 3+. Shuffle-bag, never the same clip twice in a row, exclude the last 2-3. | inference; P |
| S-90/S-91 | Jitter: non-tonal hits ±50 to ±100 cents (test to ±150, cap ±200); ladder, reward, warning and speech ±0-30 cents; tells and countdowns none (SC-12). Volume ±1-1.5 dB, never over ±3 dB on informative cues. Randomise pitch at one level only; vary samples, never the timing of a meaningful cue. | inference; P |
| S-94 | Retrigger floor per sound ID: 40-80 ms for UI and coins; drop identical repeats inside 40 ms. | inference; P |
| S-100 | Long-stay zones (lobby, hub, shop, queue) must not audibly repeat within 10 min: resequence 15-20 s segments or stack unequal-length stems. Hook in the first 3 s. | practice |
| S-101 | Mouth-like sounds (chew, slurp, smack, sniff, breath) never loop or repeat in frequent events and play at most 4 times per second; tonal pickups follow S-194 and S-94 instead; offer a "reduce repetitive sounds" option. | study prevalence; P limit |
| S-92 | Combine variant, pitch and volume randomisation; apply random pitch at one level only (offsets at two levels add). | practice (Unity docs) |
| S-93 | Repeated attacks get a new EQ or pitch offset on every repeat. | practice (God of War Ragnarok) |
| S-95 | Fire rates above about 8/s use start + loop + tail assets, not one sample per shot. (P) | inference |
| S-96 | Machine-gun test: record 10 s of the fastest realistic repetition; if it sounds like a metronome, add variants, jitter or a lower retrigger rate before changing the sound. | inference |
| S-97 | Variants help only partly: the brain suppresses repeats across different recordings of one source. Keep sounds meaningful and rare; give big cues varied timing or a one-off layer. | study (N=9) |
| S-98 | Assume liking falls with heavy repetition (fell over 7 plays of one excerpt) and test it. | study |
| S-204 | Variant fixture: simulate 1,000 selections for immediate repeats, weighting and starvation; keep "exclude last" across bag refills; declare whether history is per character or shared nearby. Also listen in play. | lead |
| S-205 | Test repetition in the real loop: 10-15 min normal play + a dense-event fixture. Measure intelligibility, annoyance, missed warnings, volume or mute changes, not playtime alone. (P) | lead |
| S-206 | Close or crunchy textures are optional: normal mix + opt-in close-texture mix, and ≥1 alternate texture for close, crunchy, squeaky or mouth-like cues triggered often. Opting out never removes the confirmation. | inference |

## C. Cents to PlaybackSpeed (=)

PlaybackSpeed = 2^(cents/1200). Volume multiplier = 10^(dB/20).

| Cents | ±25 | ±50 | ±100 | ±150 | ±200 |
| --- | --- | --- | --- | --- | --- |
| Speed range | 0.986-1.015 | 0.971-1.029 | 0.944-1.059 | 0.917-1.091 | 0.891-1.122 |

| dB | −1.5 | −1 | +1 | +1.5 | −3 | −6 |
| --- | --- | --- | --- | --- | --- | --- |
| Volume × | 0.841 | 0.891 | 1.122 | 1.189 | 0.708 | 0.501 |

## D. Methods behind these rules

| ID | Source | Extra fact not in a rule |
| --- | --- | --- |
| M-44 | Unity, Wwise, FMOD | Random containers with shuffle and "avoid last N"; pitch jitter in cents, volume in dB; voice limits that steal oldest, furthest or quietest |
| M-60 | Disney Imagineering | Queue ambience loops up to 2 h (film loops about 2 min); silent respites reset urgency; impact sounds triggered individually, not baked |
| M-94 | Wwise 2024.1, FMOD 2.03 | Random vs shuffle selection, recent-item exclusion, instance limits with priority (lead) |
| M-95 | GDC 2024 audio QA | Audio-specific QA with project tools finds problems in context (lead) |

## E. Gaps

| ID | Gap | In-house test |
| --- | --- | --- |
| G-03 | Pitch-jitter size | Blind 10 s runs at ±50, ±100, ±200 cents and ±8%; pick the widest nobody hears as "a different object" |
| G-04 | Variant counts | Blind 4 vs 8 variants (3 vs 6 for impacts) in a 10 s storm; pass if listeners cannot spot repeats |
| G-17 | Fatigue over about 1,000 plays | Telemetry vs pool size: SFX volume changes, mute rate, session length, "reduce repetitive sounds" toggle rate |
