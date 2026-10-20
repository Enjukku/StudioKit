> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Genre presets

Starting defaults only; the game's own design overrides them. All tempo, length, count and LRA values are (P) and
inference. Loudness target for every genre: S-102/S-207 (SKILL.md). Name the preset in every deliverable and say
where the brief departs from it.

## A. Direction per genre

| Genre | Music | Reward cues | Threat cues | Mix priority (high → low) | LRA | Signature techniques | Avoid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Simulator | Exploration 100-125 BPM, shop 85-110; major; reward SFX in track key (S-114) | Pickup (S-65); ladder (S-60..S-62); sell run (S-67); frequent tiers (S-194), rare celebrations (S-53) | Almost none; honest fail glide (S-134) | Own feedback > reward > UI > world > music > ambience | 5-10 LU | Close dry pickups (S-32); ASMR-style counter (S-31); one hero sound per milestone (S-64); chill moment on rare drops (S-28) | Celebration on below-cost random results (S-161); near-miss (D-02); roughness on rewards (S-08); short lobby loops (S-100) |
| Horror | States calm, near-unaware, warning, battle (S-48); dread slow or no pulse; chase 160-175 BPM | Sparse; relief after a chase | Roughness 40-80 Hz (S-07); rear threats (S-11); emitters stay alive (S-47); unique lethal cue (S-51); decoy + 2 s duck (S-37, S-38); stress heartbeat (S-46) | Lethal threat > own feedback > threat world > ambience > music | 15-20 LU | Dread vs terror (S-36); distant bed (S-43); silence once per area (S-34); Shepard + ticking for timers (S-44) | >1 startle per scene (S-19); same scare gap twice (S-38); infrasound claims (S-16); warning spam (S-99) |
| Battlegrounds, combat | 120-150 BPM; 2 adaptive layers (S-115) | Hit or kill confirm below 200 Hz and above 4 kHz, in gaps (S-59); hitstop by strength (S-73) | Distinct incoming-attack cue per move; attackers placed behind (S-11) | Own feedback > enemies attacking the player > teammates > world > music | 15-20 LU | Start + middle + end layers (S-78); new EQ or pitch per swing (S-93); duck spikes for ultimates (S-109) | One shared hit sound for all weapons; constant ducking pump; voice pile-ups (S-152) |
| Obby | 100-125 BPM steady, major | Checkpoint chime, always the same (S-64); stage complete riser, hit, gap, tail (S-54) | Fall or death: short honest falling cue, low tier, varied (S-134, S-88) | UI and checkpoint > own feedback > music | 5-10 LU | J-cut into the next section (S-116); small ladder on consecutive jumps (S-60) | Loud fail sound replayed hundreds of times (S-98, S-101); long death jingles |
| Tycoon | 85-110 BPM calm; beds that do not repeat within 10 min (S-100) | Coin and register runs (S-67); build-complete snap with pre-click (Q-05); purchase confirm about 1.3 s tier (S-68) | None | UI > reward > music > ambience | 5-10 LU | Income ladder with a cap (S-61); quiet idle textures (S-31) | One sound per dropper item (group, S-79); arousal ramps in shops; pricier = louder (S-171) |
| Disaster survival | Calm lobby → warning → survival 140-175 BPM; 4-5 states | Survival relief: decrescendo, width opens | Warning IOI 300 then 100 ms (S-135); auditory icon per disaster (S-137); approach ramps on pitched tones (S-10); distant bed (S-43); show-then-delay far impacts (S-85); ground-sourced giants (S-45) | Warnings > own feedback > disaster world > music > ambience | 15-20 LU | Every warning has an action (S-136); angle curves for facing hazards (S-145) | Warnings with no action; sub-only rumbles phones cannot play (S-156, S-157) |
| Destruction | Blasting 120-140 BPM; shop 85-110; major | Collect stream + counter smack (S-66); sell run (S-67); rare-drop chill (S-28) | Minimal | Own blast and impact > collect > reward > UI > world > music | 8-12 LU (S-105) | (material, size, event) keys (S-75); count-based layers (S-78); one burst sound scaled by N (S-79); debris cap (S-80); hitstop 2-6 frames (S-73); dry assets + engine reverb (S-84); sub for hero blasts only (S-117) | N copies for N pieces (S-79); sustained 2-5 kHz scrape (S-22); bass-only weight (S-157) |

## B. Budgets and the failure case to test (pack presets, all P)

| Genre | Cue lengths | Variants and voices | Cooldown, aggregation | Ducking | Failure case to test |
| --- | --- | --- | --- | --- | --- |
| Simulator | Gathering 60-160 ms; milestone flourish 0.4-0.9 s, 2-4 s flourish cooldown | 6-10 variants; 2 voices per collection family | 80-150 ms aggregation in rapid gains (S-194) | None for pickups; ≤3 dB for a major unlock | Auto-collectors build a permanent high-pitched wall: aggregate, summarise, offer a flourish toggle |
| Horror | Threat-signature tail 0.3-1.2 s | 4-8 variants per movement and material family; 2-4 foreground environmental events | — | Music −3 to −6 dB for a critical warning | Same sting in every room tires and predicts the scare; offer reduced startle and removable ringing |
| Combat | Confirms 40-150 ms | 6-10 per material family; 4 local impact voices; nearby-world group 8-12 | 80-120 ms same-source collision cooldown | Music −3 to −6 dB only for major intelligibility needs | A spectacular local attack hides an incoming attack; test the worst crowd on the lowest device |
| Obby | Jumps, landings 50-180 ms; checkpoint 0.2-0.5 s | 4-6 movement variants; 2 own-movement voices; 1 checkpoint voice | 100-200 ms repeated-contact cooldown | None for routine movement | Retrying a hard section produces hundreds of identical punitive sounds |
| Tycoon | Build actions 80-200 ms; upgrade confirm 0.3-0.8 s | 3-5 construction variants; 3-6 nearby machinery voices | 100-250 ms batch window for automatic production | — | The base gets louder only because the player owns more machines: aggregate by audible function |
| Disaster survival | Warning motif 0.3-1 s; repeat ≥2-4 s apart | 2-4 reserved warning voices | Coalesce redundant local warnings | Ambience and music −4 to −6 dB around the main warning | A rain or wind bed masks an imminent collapse |
| Destruction | Hero impact 0.2-0.6 s | 6-12 fracture variants; 4-6 foreground breakage voices; 8-12 quieter debris voices | 80-150 ms repeat-contact cooldown | Large events −3 to −6 dB, 200-500 ms recovery | A thousand rigid bodies each trigger a full explosion asset |

For a genre not listed, blend the two nearest rows and state the blend.
