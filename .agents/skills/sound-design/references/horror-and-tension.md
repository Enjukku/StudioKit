> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Revised by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# Horror, tension and warnings

S-07 and S-11 live in `elements.md` §B, S-186 in `emotion-recipes.md` §C, S-136/S-99 and S-137 in §B here (moved
from SKILL.md in J018). Tells for enemy attacks and hazards: `craft-process.md` §2 and SKILL.md SC-12. Recipes for dread, anxiety, fear,
shock, suspense, tension, urgency: `emotion-recipes.md`.

## A. Scare and dread rules

| ID | Rule | Evidence |
| --- | --- | --- |
| S-36 | Two profiles. Dread and anxiety: varied, sparse, less predictable (exploration, build-up). Terror: loud, dense, rough (chases, scare peaks). | inference (secondary) |
| S-19 | A sharp attack (<about 25 ms) at high level is a startle-class event: at most one per scene. Gentle sounds get slower attacks. | lead |
| S-37 | Duck music and ambience for about 2 s before a scare. Test: at equal peak level the ducked version is rated louder. | practice |
| S-38 | Misdirect: small decoy sound, the real event about 1000 ms later; never the same gap twice in a row. | practice |
| S-39 | Scare anatomy: low boom + high screech, hard attack, tail 2-5 s (never <1.5 s), ≥3 variants per scare. | practice (vendor, weak) |
| S-40 | False-relief two-stage stab: hit, short silence, second hit about 6 dB lower. (P) | practice + inference |
| S-41 | Drive scare timing from player action (door, camera turn), not a fixed timer. Tune timing before polishing sound (Bologna estimates timing is most of a jump scare). | practice |
| S-42 | Scare sounds are unidentified at impact; no sting that announces the source first. | practice |
| S-43 | Distant threat bed: continuous off-screen layer whose low-pass cutoff and level fall with distance. | practice |
| S-44 | Timer stages: endless riser or Shepard tone + ticking pulse; 2-3 scales at different speeds. No Hz found. | practice |
| S-192 | Tie a restrained endless rise or fall to a real resource or timer and stop it decisively when that ends. Start: 12-20 s loop, ≥4 octave-spaced parts, plus a non-pitched and a reduced version. (P) | lead |
| S-45 | Giant enemies sound like the ground they touch (rumble, scrape), pitched down; not a vocal growl. | practice |
| S-46 | One stress value 0-1 drives heartbeat speed and level and picks 1 of 3 breath loops (calm, fatigued, injured); breath and exertion on separate layers. Breath layers are nasal and dry, gated by stress, covered by the "reduce repetitive sounds" toggle; no lip, saliva or throat clicks (S-101). Test: stress 1 vs 0 audibly different within 1 s. | practice |
| S-47 | A culled or off-screen threat keeps its emitter playing at its position. | practice |
| S-48 | Horror music has 4-5 states (calm, near-unaware, warning, battle); intensity rises with enemy count, not new tracks. | practice |
| S-49 | Each room: 1 tone loop + 4-8 random one-shots on random timers + 1-3 stationary emitters (+ weather outdoors). (P counts) | practice + inference |
| S-50 | Stealth monsters hear the player: 3 noise tiers (quiet, medium, loud), ranges per game. | practice |
| S-51 | Each lethal entity has one unique, spectrally distinct cue not shared with ambience; test it in the busiest mix. Co-present enemy families differ in spectrum and rhythm (similar sources blur localisation, M-87). | practice + lead |
| S-52 | Stunned or downed: low-pass "deaf/underwater" filter on the world bus. | lead |
| S-189 | Separate world danger from danger the player may know; only the second drives music escalation, or the score leaks hidden information. | inference |
| S-190 | Music intensity follows a 0-1 value smoothed over 0.5-1.5 s; 0.15 threshold gap; 2 s minimum stay; urgent warnings bypass smoothing. (P) | inference |
| S-191 | Every scare ships in full and reduced-intensity versions; log the real peak and short-window level jump. Never need the player to turn the volume up before an uncontrolled impact. | inference + standard |
| S-193 | Simulated tinnitus or ringing (flashbang, close blast) is removable via an option offered on first run. | standard (ITU-T H.872) |

## B. Warnings and alarms

| ID | Rule | Evidence |
| --- | --- | --- |
| S-136/S-99 | Every warning comes with an action the player can take; nonactionable warnings under 10%. Budget: ≤1 loudest-tier cue per 10 s; a cue that fires more often moves down a tier. | study basis; P numbers |
| S-137 | Critical warnings are auditory icons (sound resembles meaning); more accurate and faster than tonal alarms under load. | study |
| S-135 | Urgency ladder by pulse spacing: danger IOI 100 ms, caution IOI 300 ms (20 ms pulses, 920 ms bursts) + timing jitter. The reaction gain is small (about 10 ms); the job is to signal priority. | study |
| — | Warnings rise ≥3 dB per priority step (FMVSS 141's "audibly louder" step, M-62). | practice |

Warning lengths, repeat spacing and reserved voices: `genre-presets.md` §B (disaster survival row).

Tells: the sound tell starts on the VFX tell's event, is the same asset every time (no jitter), lasts the reaction window
from the game designer's threat sheet and stops on the damage event. A state with a timer or breaking point (a shield,
a fuse) gets a warning keyed to its end-of-state event whose intensity rises toward the end (`review.md` R-08, R-09).

## C. Methods behind these rules

| ID | Source method | Extra fact not in a rule |
| --- | --- | --- |
| M-03 | Morphic horror catalogue | Vendor lengths only; weak |
| M-04 | 28 Years Later (2025) | Close dry breath layer in the ear reads as physically near; 30 actors each recorded their own scream for crowds |
| M-05 | A Quiet Place | Quiet zones that reward listening make players hyper-aware of small sounds |
| M-06 | Zone of Interest (2023) | Propagation modelled: bass and highs lost, reverb per place |
| M-07 | Oppenheimer (2023) | Flash, 30-40 s gap, then shock wave: sharp bang + long thunder decay |
| M-08 | Dunkirk (2017) | Three Shepard scales at week, day, hour scales; ticking watch as synth pulse |
| M-27 | Dead Space remake ALIVE | One adrenaline state drives heartbeat, breathing and voice takes |
| M-28 | Dead Space remake | Occlusion and obstruction by material; fallback raycast wall count → low-pass per wall (Roblox: S-146) |
| M-29/M-30 | Resident Evil 4 remake | Five ambience layers per space (outside tone, inside tone, random one-shots, stationary sources, weather); room portals |
| M-31 | Alien: Isolation | Helper sounds (tracker beeps) have a cost: they can give the player away |
| M-32 | Silent Hill 2 remake | Trip-hop, industrial, dark ambient, musique concrète textures for ambiguous dread |
| M-71 | Amnesia: The Bunker | Descending Shepard texture runs while the generator burns fuel (lead) |
| M-72 | Alan Wake 2 | Grounded detail, near-silence, simple triggered stems; music complexity follows need (lead) |
| M-73 | Dead Space intensity director | Ambient events paced by an intensity value that schedules recovery (lead) |

Traced into rules above (no extra facts): M-01, M-02 → S-38, S-41; M-09 → S-45; M-65 → S-135; M-66 → S-136, S-99;
M-67, M-86 → S-137.

## D. Gaps

| ID | Gap | In-house test |
| --- | --- | --- |
| G-12 | Startle levels and rise times for young players | Adult testers rate scares; telemetry: quit within 30 s after a scare |
| G-22 | Alarm urgency in numbers (pitch, rate) | Rate 3 IOIs × 2 pitches |
| G-23 | Warning timings in popular Roblox horror games | Record gameplay; measure cue-to-arrival times |
| G-26 | Startle vs sustained dread for young players | Slow cue vs abrupt cue vs no cue at matched playback; adult testers only for intense versions |
| G-27 | Adaptive music leaking hidden threats | Compare fixed vs adaptive playback with identical events; can players predict hidden threats? |
