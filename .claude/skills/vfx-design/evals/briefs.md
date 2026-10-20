> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-13

# Eval briefs for the vfx-design skill

Give the agent the brief text only. Grade each check pass/fail (v2 2026-10-20: C4, C6 and 1.6 rewritten for the craft-first skill; other checks citing old caps follow SKILL.md §6 overrides); a brief passes at ≥80% of its checks with no
"must" check failed. Checks common to all briefs (C1-C5) apply to every run.

| ID | Common check |
| --- | --- |
| C1 (must) | Every number carries a provenance tag ([study] [preprint] [practice] [spec] [inference] [P]); every [P] is in the PROPOSAL list; nothing claims to be seen in motion, played, measured or tested |
| C2 (must) | No invented asset ids, sheet paths, properties or engine limits; every sheet picked was opened and logged (FB-02), or the layer says "sheet needed" |
| C3 | Rule IDs cited for design choices, and every cited ID exists in a reference file |
| C4 | Deliverable follows the v2 output (brief, frame script, layer plan, spec.json, sound brief, self-check, capture request, PROPOSAL list) or the review format (ranked findings, fixed values, "could not check" list) |
| C6 (must, v2) | Frame script uses the screen-size math at the game camera and is compared with ≥1 pro frame script of the same type; layer values start from vfx-craft/references/pro-defaults.md with reasons for departures; curves are named library curves; LightInfluence 0 everywhere |
| C5 | Composite flash count, colour backup (shape/icon/label), reduced-motion/reduced-flash variant that keeps the information, and a per-tier budget line with a static flipbook fallback (CA-13, EL-37, CA-22, RB-28, FB-30) |

## 1. Heavy rocket hit on a wall (mobile-first)

> A destruction game with a toy look. A rocket launcher hits a wall and breaks a chunk out of it. Make the hit feel heavy. Most players are on phones.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Rated per viewer at about 5 for the shooter (medium blast; destruction preset), lower for others; no FOV punch, slow motion or 100% white at this band (MO-01, MO-02, CD-16) |
| 1.2 (must) | Weight comes from outcome link, timing and truth, not more intensity; drawn blast and dust edge = server radius (JU-02, RV-08, EL-04, MO-11) |
| 1.3 | Punch: brightest layer 2 f@60 inside a flash Lifetime 0.05-0.1 s; intact blocks swap to broken at the flash peak; front-loaded, staggered exits (EL-41, JU-30, EL-44, EL-43) |
| 1.4 | Hit-stop 0 on explosions; shake by trauma (rotation only, t³, delayed to the shockwave, distance falloff), none per block (CA-08, CA-02, CA-03, CA-05, CA-04) |
| 1.5 | Toy vocabulary: chunky toy-piece chips in the toy palette, no realistic smoke, debris fades never pops; dust see-through by 2 s (MO-21, MO-14, MO-13) |
| 1.6 (must) | Budget v2: impact recipe layers (flash 0.03-0.05 s, impact shape 0.1-0.2 s, sparks with drag, dark twin, glow, ring, ground mark); est. live particles ≤~1000 and unique textures listed; Emit(n) bursts; blast PointLight Shadows false, fade ≤0.3 s (SKILL §4, pro-defaults §B, RB-03, RB-23) |
| 1.7 | LightEmission 1 on core and sparks, 0 on dust; LightInfluence set on every emitter (RB-05, RB-06) |
| 1.8 | One trigger for picture punch and sound transient; sound 0 to +40 ms late, never >1 frame early (JU-28, JU-29) |
| 1.9 | Test plan: real low-end phone, full composite, 10-15 min; A/B complete builds, not liking alone (RV-14, JU-13) |

## 2. Coin pickups with a magnet

> A collecting simulator. Players pick up coins all the time, up to 20 per second with a magnet upgrade. Design the pickup effect.

| Check | Expected |
| --- | --- |
| 2.1 (must) | Importance about 2 for the collector, lower for others; no shake, flash, FOV or post effect (MO-01, CA-04, SC-57) |
| 2.2 (must) | Same-kind pickups within 100 ms merge into one burst, one sound trigger, one count label; the final counter stays exact (JU-20, T-05) |
| 2.3 (must) | Caps: ≤8 live copies (cull oldest), ≤10 particles per copy, coin sprites ≤20 on screen (JU-21, T-07, T-08, C6 coins row) |
| 2.4 | Short and subtle: whole pickup ≤300 ms, tail ≤0.5 s, coin flight about 0.5 s, count-up ≤0.6 s (JU-19, T-03, T-11) |
| 2.5 | Plays on the confirmed credit; first response ≤100 ms; pending state if confirm is slower (MO-05, T-04) |
| 2.6 | 3 variants by layer recombination; decoration-only randomness (T-06, JU-17, JU-16) |
| 2.7 | Never brighter than a threat; reward gold only on rewards; others' pickups toned (MO-04, SC-24, MO-19) |
| 2.8 | Repetition test at 20 events/s and over hundreds of pickups, not one view (JU-24, JU-21) |

## 3. Legendary egg reveal (paid egg)

> A pet simulator. Eggs cost Robux-bought gems. Design the reveal for a Legendary pet. Make it exciting.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Windup identical in build and length for every outcome; no rarity tint before the punch; escalation only after it (MO-16) |
| 3.2 (must) | No near-miss: no higher-tier layer on a lower result; no celebration on a result worth less than its cost (MO-17, MO-06, JU-01) |
| 3.3 (must) | Odds for every outcome shown before purchase, summing to 100%, behind a worded Details control; PolicyService `ArePaidRandomItemsRestricted` path; no VFX over the odds panel, no urgency (MO-18, moment §D) |
| 3.4 | Legendary at importance 8 for the hatcher, toast only for others; 1-2 frames pure white on the item frame; post-punch length about 2.9 s + hold; skip and quick-open (C7 Legendary row, MO-02, CD-16) |
| 3.5 | Tier nameable without colour (name, frame shape, layer count); greyscale passes (MO-12, EL-37) |
| 3.6 | Push-in and shake off under reduced motion; flash count in the cap (MO-20, MO-08) |
| 3.7 | Pushes back on "make it exciting" for a paid pull: excitement tied to the real outcome, earned milestones; says so plainly (JU-01, guardrail paid random items) |

## 4. Boss ground-slam telegraph (battlegrounds)

> A battlegrounds game. A boss raises its fists and slams the ground, damaging everyone inside a circle. Design the warning and the slam.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Drawn circle = server hit area at cast, contact and expiry, in every tier and variant; never larger by default (EL-04, MO-11, X-31) |
| 4.2 (must) | Lead about 600 ms if one dodge direction, 1000 ms for 2-4 safe spots, as [P]; ≥2 channels incl. sound; ends and is removed on the damage frame (EL-40, EL-11, MO-11) |
| 4.3 | Rated 9 for the threatened player; the telegraph owns the brightest pixel; never out-ranked by rewards or others' effects (MO-04, SC-16) |
| 4.4 | Colour plus pattern or symbol; sharp downward shapes for threat; boss source cue (Highlight) does not rely on post effects (MO-12, EL-14, SC-18, RB-22) |
| 4.5 | Progress monotonic; pulses ≤3 Hz at full contrast; no random start on the telegraph (MO-15, MO-24) |
| 4.6 | Slam: trauma shake on the receivers scaled by distance; hit-stop by contact tier only, none in crowds; flash count on the composite (CA-02, CA-05, CA-08, CA-13) |
| 4.7 | Dodge test on a 30 fps phone and PC (SC-37) |

## 5. Review an existing explosion

> Review this explosion and fix it: 6 ParticleEmitters, 300 particles, a pure white additive core that lasts 0.8 s, 3 full-screen flashes in 0.5 s, camera shake 3 studs of translation.

| Check | Expected |
| --- | --- |
| 5.1 (must) | Starts at R0: asks for or assumes communication job, importance and server radius before art notes (RV-01) |
| 5.2 (must) | Flags 3 full-screen flashes in 0.5 s as a safety blocker: design ≤2 large-area flashes per rolling 1 s, leading edges ≥334 ms apart, counted on the composite; a toggle is not a fix (RV-T06, RV-11, RV-12, CA-13) |
| 5.3 (must) | Flags the 0.8 s pure white core: pure white only at rating ≥8; flash peak 2 f@60 inside Lifetime 0.05-0.1 s (SC-02, EL-41, RV-T04) |
| 5.4 (must) | Flags 3-stud translation shake: 3D shake is rotation only, max 3° per axis [P], trauma model (CA-03, RV-T18, CA-02) |
| 5.5 | Flags 6 emitters over budget (≤5 High, ≤3 Low) and asks for Rate × Lifetime and live count; merge non-truth layers; Emit bursts (MO-23, RB-04, CD-07, RB-03) |
| 5.6 | Findings table in ranked fix order (problem → rule ID → fix as `layer.property: from -> to` → severity); safety and performance block release at any rank (RV-05, RV-11) |
| 5.7 | Fixed cards plus a "could not check" list naming the captures needed; claims only what the config shows (RV-03, RV-02) |

## 6. Calm ambient mood for a toy bedroom level

> A toy bedroom level in a toy-themed destruction game. Design a calm ambient mood for it.

| Check | Expected |
| --- | --- |
| 6.1 (must) | Ambient at importance 1 (2 only where it changes play); never the brightest or most saturated pixel; no pickup or hazard hue (C9, MO-04, SC-24) |
| 6.2 | Fades in and out, no abrupt onsets; slow cycles, nothing pulsing above 1 Hz (SC-08, EL-60, MO-15) |
| 6.3 | Values from the ambient rows: dust motes Lifetime 6-10 s, 0.1-0.3 studs/s, Rate ≤5/s per volume (≈40 live); mood changes 3-5 s (C9) |
| 6.4 | Stage background muted, gameplay brighter and warmer; Bloom Threshold high so ambient does not glow; ColorGradingEffect Lighting-only (SC-50, SC-54, RB-15) |
| 6.5 | Stage palette read from the art bible or stage brief, not invented; effects tested on the stage's extreme surfaces; fog or motes never hide hazards or pickups (SC-50, SC-52, C9 Fog row) |
| 6.6 | Continuous emitters ≤40 live on phones; LightEmission 0 and LightInfluence 1 on dust (RB-04, SC-27, RB-06) |
| 6.7 | Test on the real stage with gameplay effects on top: pickup and threat still found (RV-13, SC-26) |
