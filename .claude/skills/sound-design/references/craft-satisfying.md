> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Craft: satisfying sounds and layering recipes

Core rules used here (in SKILL.md): S-76 impact layers, S-75 material keys, S-78 layer count, S-79/S-202 burst
scaling, S-203 semantic triggers, S-73/S-74 hitstop, S-133 AV sync, S-131/S-132 haptics. All ms, Hz and dB below
are (P) unless tagged.

## A. Satisfying qualities

| ID | Quality | Why it feels good | Make or measure it | Evidence |
| --- | --- | --- | --- | --- |
| Q-01 | Crisp transient | High-frequency bite reads crisp and fresh | Peak within 1-5 ms, energy >2 kHz; 2-8 ms click or noise burst at the front | study (food); game transfer inference |
| Q-02 | Short clean decay | Clean tail = "finished"; rough long tails drift to alarm | To −40 dB in ≤300 ms; no tonal ring in 2-5 kHz | inference |
| Q-03 | Low body (thunk, thock) | Lower pitch rated stronger (56% vs 12%) | 60-250 Hz, 40-150 ms; pitched-down thud or sine drop | study (self-report) |
| Q-04 | Closeness | Object handling drives ASMR liking | Reverb tail <0.3 s; high-pass only 30-60 Hz; close-mic texture | study (self-report) |
| Q-05 | Completion ("snaps home") | Force peak then sudden release (LEGO click) | Pre-click −6 dB, 20-30 ms before the main click on the exact completion frame | patent (mechanism) + inference |
| Q-06 | AV congruence | Matched size and timing feels caused | Bigger object = lower pitch; timing per S-133 | lead |
| Q-07 | Rising sequence | Each step up = progress | Ladder per S-60/S-61/S-62 | practice |
| Q-08 | Slow detailed texture | Rated most effective by ASMR responders | Micro-texture 2-6 kHz, low level, ≤4 events/s | study (self-report) |
| Q-09 | Expectation then payoff | Surprise after a pattern pleases most | Break a stable pattern once; A/B ratings | study |
| Q-10 | Proportional payoff | Bigger win = bigger sound; mismatch distorts judgement | Length tiers S-53, S-194; net-value check on every trigger | study |
| Q-11 | Fresh on repeat | Exact repeats suppress response | Variants and jitter per S-88..S-91 | study + inference |
| Q-12 | In key | Pitched SFX in key sound like the music | Per S-114, S-127 | practice |
| Q-13 | No roughness on rewards | Roughness reads as alarm | Per S-08 | study |
| Q-14 | No wet mouth sounds in loops | Top misophonia triggers | Per S-101 | study |
| Q-15 | No sustained harsh scrape | High-frequency, low-modulation noise is most unpleasant | Low-pass scrapes; per S-22 | study |
| Q-16 | Haptic + sound together | Timed bimodal feedback feels connected | Per S-131 | study |
| Q-17 | More layers for bigger events | Size is heard | Per S-78 | practice |
| Q-18 | Thock vs clack | Low body vs bright top | Vendor convention: thock <500 Hz, clack >2 kHz | practice (blog) |
| Q-19 | Sand, soap, slime, pop-it, bubble wrap, ice, glass | Crisp, textured, close, completing | No measurements; record close and dry, trim | inference |
| Q-20 | Stable trigger categories | Tapping, whispering, crinkling reported consistently | Compare categories at matched loudness | lead |
| Q-21 | Friction that follows the hand | Continuous sound tracking pressure reads as control | Amplitude follows pressure and speed; stops instantly | lead |
| Q-22 | Granular flow | Grains synced to visible flow = coherent material | Quiet bed + discrete grains; density tied to flow rate; taper as it settles | inference |
| Q-23 | Resistance → fracture → release | Staged events make completion legible | Separate scrape, break, landing on animation events | inference |
| Q-24 | Material-true ring | Glass, ceramic, metal need their ring (exception to Q-02) | Keep frequency-dependent decay; shorten only to unmask the next event | inference |
| Q-25 | Plausible source | A neutral visual source made unpleasant sounds rate better | A/B matched vs mismatched visuals | lead |
| Q-26 | Texture statistics predict tingles | Separate from pleasantness | Analyse candidates before playtests | lead |
| Q-27 | First-person sync | Strengthens AV effects | Tight sync to first-person hand actions | lead |
| Q-28 | One feature at a time | Satisfaction is a bundle | Ablate one feature at matched level; include a no-reward control | inference |

## B. Layering recipes

| ID | Cue | Recipe | Evidence |
| --- | --- | --- | --- |
| S-65 | Pickup | Tick 3-6 kHz, 3 ms (0 dB) + blip 800-2000 Hz fundamental, 60-120 ms (−3 dB, interval M2 to 5th) + optional sparkle 5-9 kHz, 80 ms (−15 dB). Dry, no ring. | inference |
| S-66 | Collect stream | Per-item tick 3-7 kHz, 2-4 ms (−6 dB) + arrival thock 150-300 Hz, 30-60 ms (−4 dB); pitch +1 st per about 5 items, max +5 st; above 15 items/s one grouped sound per 60 ms; counter smack = tick + thock +3 dB; sync arrival to the visual frame. | inference |
| S-67 | Coin or sell | Metal tick 4-8 kHz, 3-5 ms + two notes up a 4th or 5th (second 60-80 ms later, 80-150 ms long, 1-2.5 kHz) + ring tail 3-6 kHz ≤250 ms (−14 dB). Sell run: one coin per 50-80 ms, +1 st per step, max 8, then a register sound with 200-400 Hz body for 120 ms. | inference |
| S-129 | UI click | <80 ms total: soft tick 2-5 kHz, 3-6 ms + pad 150-400 Hz, 30-50 ms (−6 dB); no reverb. Press and release are two sounds; release −4 dB and 2 st higher. | inference |
| S-130 | UI lengths | Taps 30-150 ms; most cues <300 ms; notifications ≤500 ms. Rising = success, falling = error. | lead |
| S-220 | UI families | Design semantic families first (accepted, reversible navigation, invalid, completion, urgent), timbres second. Confirms 40-100 ms, completions 150-400 ms, invalid-repeat cooldown 200-500 ms (new attempt only), 3-10 ms edge ramps. | lead |
| S-196 | Success vs failure | Differ in ≥2 attributes (e.g. rhythm and timbre), not pitch alone. | inference |
| S-77 | Sweetener test | Mute the thump layer; if the hit does not get thinner, delete the layer. | practice |
| S-81 | Bigger break | Body lengthens to about 300 ms and drops 4-5 st. | inference |
| S-82 | Size-pitch | Each size class up = 3-5 st lower. | lead |
| S-199 | Break model | Fracture → structural body → falling debris → settling (small breaks skip stages). Normalised severity 0-1 (mass or pieces) drives event choice, body and debris density in a restrained gain range. | inference |
| S-200 | Destruction budget | 6-12 fracture variants; 4 concurrent transients + 2 longer bodies locally; secondary contacts coalesced in 50-100 ms; debris spread over 200-1,200 ms; repeat-contact cooldown 80-150 ms; hero impact 0.2-0.6 s. | inference |
| S-80 | Debris cap | ≤8 debris voices per 100 ms. | inference |
| S-83 | Burst length | Cap each destruction burst so chaos comes in bursts and rewards stay audible. | practice |
| S-84 | Dry assets | Short dry tails; space from one engine reverb per space. | practice |
| S-85 | Distant blasts | Show first; delay sound by distance ÷ a dramatic in-game speed of sound (design value). | inference |
| S-201 | After a collapse | Update obstruction, occlusion and room reverb; nearby collapse outranks distant debris. | lead |
| S-86 | Vehicles, movers | Loop pitch +0.8% or more per speed unit; ≥3 dB per speed or power tier; mono-sum before upload; idle loop 10-20 s, drive loop 10-40 s. | practice (UN R138, FMVSS 141) |
| S-87 | Gear or power shift | Brief level drop (80-150 ms), then a pop, with a camera kick on the same frame. | practice + inference |
| S-198 | Hitstop scope | Only on consequential contacts; never delays input acknowledgement or multiplayer simulation. | lead |

Sources behind B: M-12 sweeteners, M-37 Teardown (7 materials × hit/break × 3 sizes), M-38/M-39 fighting-game
hitlag, M-63 Ioniq 5 N shifts, M-90 door quality (doors and cases end decisively; rattle only loose objects).

Also traced: M-56 → S-130; M-57 → S-64; M-59 → S-131; M-61 → S-86; M-64 (throttle-linked pitch, lead) → S-86;
M-74 → S-201; M-75 → S-198; M-79 → S-220; M-80 (shared UI library tested in real flows, lead); M-81 → S-221;
M-89 (crisp fracture for brittle food scenes; taste effects do not transfer to virtual food, lead).

Gaps: G-16 no acoustic measurements of satisfying objects (record real objects close and dry, measure spectrum and
decay). G-28 audio vs visual share of hit satisfaction (factorial audio × visual enhancement).
