> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Repetition and fatigue

Core rules used here (in SKILL.md): S-88/S-89 variant pools and shuffle-bag, S-90/S-91 pitch and volume jitter,
S-94 retrigger floor, S-100 long-stay zones, S-101 misophonia, S-79/S-202 burst scaling, S-152 voice caps.

## A. Repetition plan procedure

1. Estimate plays per minute and max burst per second for the cue (cue-card field 34).
2. Variant count from the rate (S-88). Shuffle-bag with exclusion (S-89); simulate it (S-204).
3. Jitter by cue type (S-90/S-91); random pitch at one level only (S-92).
4. Retrigger floor (S-94); above about 8 plays/s switch to start + loop + tail (S-95); above 15 events/s aggregate
   into one grouped sound per window (S-66, S-194).
5. Voice cap and steal policy (S-152).
6. Machine-gun test (S-96), then a real-loop test (S-205).
7. If the cue is heard 1,000+ times a session, keep it short, quiet relative to rare cues, and meaningful (S-97, S-98).

## B. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
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
