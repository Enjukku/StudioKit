---
name: ui-design
description: What and why for a Roblox game screen before anyone styles it - the player's decision, what is seen first, every state and device, shop and paid-random honesty, onboarding. Use before designing or reviewing any HUD, menu, shop, inventory, popup or reward screen, for "the UI is confusing", "players can't find X", "make the shop clear". Does not draw (ui-figma) or build (ui-basics).
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J002. Evidence: owner-supplied research paper (RP, ChatGPT, paper's stated date 2026-10-21; notes `knowledge/reference/ui/05a`-`06b`), tags kept as the paper gives them: **V** VERIFIED (published rule or measurement), **E** EXPERIENCE (studio account), **O** OPINION (the paper's adaptation), **U** UNSPECIFIED (no value exists). Tutorial ids TC/TS/TA/TP: `knowledge/reference/ui/README.md`. Rebuilt by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (flow before style; structure study, wireframe options and a grey value pass before styling; one UI rule sheet; the motion goals and one motion table; outcome feedback, refusals and true counters; a self-review by stage; §7 core principles).

# UI design: the screen works before it is pretty

## 1. When this skill starts
A screen, HUD element, popup, shop, reward sequence or onboarding step is new, changed or under review. It answers: what is the player deciding, what must they see first, what are all the states, what can go wrong, what style fits, and what proves it works. Output feeds a style book and then `ui-basics` (Roblox build). §7 (core principles) applies to every UI task. After a context compaction, re-read §3, §6 and §7 of this file before continuing.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Decision record, attention inventory, HUD contract, state list, focus map, size math, text containers, the flow sheet, what I take from the game designer | `references/screen-contract.md` |
| Shops, offers, purchase states, paid random items and honest reveals, ads, rewards, onboarding | `references/shops-rewards-onboarding.md` |
| Motion: beats, records, handoff fields, the game's motion table, refusals, counters, frequent events, pulse rates | `references/motion.md` |
| Picking a style, the visual thesis, the style spec, the UI rule sheet, value bands and colour | `references/style-choice.md` |
| The release checks, my self-review by stage (inputs, commands, image budget), what each input proves | `references/review.md` |
| Two worked examples (egg shop popup, simulator HUD) from moment to hand-off | `references/worked-examples.md` |
| Roblox rules for anything players buy, roll or watch (binding; wins over my books) | `platform-policy` skill |
| Roblox build facts (insets, scaling, text, input, native modifiers, UI effect timings) | `ui-basics` skill |

## 3. Steps (cheap stages first; each ends with its deliverable and its check)
Write the deliverables into `content/ui/<screen-id>/spec.md`. Self-review lines S-xx: `references/review.md` §6. A change inside an approved screen runs only the stages it touches (from its pain point down) and the S-lines of those stages; the approved flow, wireframe, rule sheet and target image stand.
1. **Moment and constraints.** Player goal, what they know, game state, devices (phone first; name the smallest supported phone), input, locale, accessibility settings, cost of failure; the game's parameters from the game profile (genre, camera, player count, session pace). Changing an existing screen: list the observed pain points (taps, confusion, missed information) and where each was seen. *Check:* one sentence says what the player is trying to do; no change without a pain point (S-07).
2. **Inputs and evidence.** Take the game designer's information list, read rank and feedback stack for this screen (`references/screen-contract.md` §8); a missing input is asked for, and meanwhile an assumption. Evidence ledger for every claim: tag, source, date, unit, scope; unknown = **U**, never a guess.
3. **Decision, flow, states.** Decision record; one job per element (D-20); flow sheet with taps per task (screen-contract §7); every screen, popup and state listed before any is designed (D-04); HUD load sized from the information list (D-03). *Check:* S-01 to S-06.
4. **Structure study.** Trace 2-3 working screens of the same job in the genre as wireframes: where the decision, price, close and currency sit. Keep the conventions players know for core controls (D-21); write a reason for each departure. Borrow structure, never art (D-18). No images made. Method and sources, including when the brief gives no screenshots: `references/style-choice.md` §4.
5. **Wireframe options.** 2-3 grey-box layouts that differ in structure, one deliberately atypical, the first labelled warm-up; real content (longest name, biggest number, real price format); a phone layout frame (1920 × 1080 canvas, the `@ViewportDisplaySizeSmall` arrangement, never a resampled copy) and a PC frame where the layout must change; tap targets marked apart from decoration, sized to the declared touch rubric at the smallest phone, outside the no-go overlay. Pick one with a reason tied to the decision and a reason per rejected option. *Check:* S-08, S-09, S-49. Budget: one contact sheet of the options at phone fit.
6. **Grey value pass.** On the picked wireframe, greys only: plan the read order (1st, 2nd, 3rd); lower everything that is not rank 1 before raising rank 1; critical state in fixed zones clear of the thumbs (D-23); each value next to what it describes (D-22); clear size steps between priorities; rest areas between groups. *Check:* S-10 to S-15. Budget: one luminance image at phone fit plus numbers. **Wireframe gate:** flow, states and grey pass approved before any Figma styling (in the UI screen recipe they go to G1 together with the target images of step 8).
7. **Rule sheet and style.** The UI thematic from the art bible, then the game's UI rule sheet (`references/style-choice.md` §5): colour roles from the art bible with reserved hues kept out of decoration, text styles, screen zones, shape vocabulary, motion material. Pick the style book; one-line visual thesis; one job per expressive device.
8. **Target reference image.** Before styling: 2-3 whole-screen references of this wireframe in the chosen style, equal finish, a different hook each; the owner picks (or the brief records an approved one); write what I take from it (shapes, palette, materials, depth, shine, type). Method and image budget: `ui-figma/references/image-generation.md` §2.
9. **Storyboard motion and sound.** Per event: the still end state that explains it, then the motion and sound that make it felt; separate beats (attempt cue on the press · result confirmed · information visible · input available again · decoration ends); every row from the game's motion table (`references/motion.md` §7); refusals, counters, frequent events and pulse rates by `motion.md` §8; a reduced variant per intense channel. Here I ask the sound designer for the UI cue list and the VFX designer for world-to-HUD beats, on one beat list.
10. **Implementation contract.** Sizes on the 1920×1080 canvas and at the phone fit, states, assets (N / B / T / L), live text fields with their data source, focus map, motion-table rows, acceptance tests. Unknown numbers stay PROPOSAL with the test that will set them.
11. **Self-review, then hand back.** `references/review.md` §6 on my own frames: numbers for every state, images only on failure and for the key states. When a build exists, the release checks (`references/review.md` §1) on Studio captures. Every check names its input and label; end with a could-not-check list and one named weakness. **Style gate:** the owner judges motion feel at normal speed on a playable preview (Figma prototype or Studio build) before motion polish; my stills never prove feel.
12. **Test and revise.** Observation for *why*, metrics for *how often* (A/B with the `analytics` skill and Roblox Experiments); keep disconfirming results; approved values become versioned project decisions, never "industry standard".

## 4. Design core (what separates great UI from pretty UI)
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | **Decisions before decoration; flow before style before motion.** Design each screen as a player decision; count the taps before any styling; polish never rescues a bad flow. A cleaner redesign that removes a fast route is a regression (VALORANT restored one-click navigation) | H03 E; RA-32 O; RA-64 V (U07) |
| D-02 | **Priority = salience.** Rank every element, then make rank 1 the most different (value, size, colour, isolation, motion, sound); lower the rest before raising rank 1. A health warning quieter than a shop sparkle fails. Review a grayscale, a phone-fit and a moving capture | RA-58, RA-59 O; E |
| D-03 | **HUD contract, sized by need.** The genre and the information list set how much HUD there is, never habit; sort facts into *actionable now* (always findable while possible), *planning* (stable secondary region), *on demand* (detail view); busy HUDs need priority, capacity, replacement and overflow rules | H07, RA-60 O (U05); E |
| D-04 | **Every state, named apart.** Entry, normal, empty, max content, loading, pending, error, not enough currency, not eligible, cooldown, success, recovery; per item selected ≠ equipped ≠ owned ≠ claimed. All screens and popups are listed before any is designed | RA-62 O; RP §12 step 3; E |
| D-05 | **Mobile first, with numbers in their own units.** Roblox DAU 2025: mobile 83 %, desktop 14 %, console 3 % (not 2026, not playtime). Touch rubrics: Apple 44×44 pt frequent / 28×28 pt minor; Android 48×48 dp + 8 dp gap; Xbox 15 mm phone / 24 mm tablet. Declare one rubric per project; never average them | H01 V; RA-44..47 V; RA-48 O |
| D-06 | **Canvas px are not device size.** Convert before approving a size (screen-contract §5). Default PROPOSAL: frequent touch controls ≥ 44 pt on the smallest phone (≈ 150 canvas px at f ≈ 0.294); essential text ≥ 11 pt (≈ 38 px); thick lines ≥ 5 px | arithmetic from P02; O |
| D-07 | **Safe areas.** Interactive UI inside `CoreUISafeInsets`; the default move and jump controls own the lower corners; Roblox's buttons own the top corners; decorative and functional bounds specified apart | RA-49..51 V/O; ui-basics U-01, U-03 |
| D-08 | **Every input reaches everything.** Touch, mouse, gamepad: initial focus, traversal, wrap, back, restored focus; modals trap focus; nothing needs hover or long-press only | RA-53..54 V; RA-55 O |
| D-09 | **Meaning never on one channel.** Rarity, team, danger, success: colour plus text, icon or shape; every sound cue has a picture twin; reserve one hue for urgent danger | RB-13 V; RA-05, RA-34 |
| D-10 | **Text you can read on the phone.** The declared text rubric (default PROPOSAL ≥ 11 pt on the smallest phone); contrast 4.5:1 normal, 3:1 large or inactive, 7:1 high-contrast, on the weakest background; works at 200 % text; TextScaled ignores the player's text size. Outlined text: screen-contract §5 | RB-02..12, RB-17 V |
| D-11 | **Icons: meaning before polish.** Write what the icon must mean; test it unlabelled, in context, at real size, as a black fill and in grayscale; keep labels for unfamiliar categories (Candy Crush: a calendar beat the designers' trophy) | H05 E; RA-11, RA-12 |
| D-12 | **Shops are contracts.** Item, quantity, duration, price (read from Roblox), eligibility, random or not, limits, what happens after; preview ≠ commit; Roblox's prompt is the commit for Robux items (shops-rewards-onboarding §2) | H08 V; RA-77, RA-78 O; ui-basics U-07 |
| D-13 | **Paid random items are honest.** The binding rules are `platform-policy` § A; my side is the screen: odds before the buy button behind a visible worded label, one windup for every result, no near-miss (shops-rewards-onboarding §3, §5) | RA-79..81 V; E |
| D-14 | **Static explains, motion makes it felt, never misleads.** Every event reads from its still end frame with sound off; motion adds the feeling; an animation implies a rule, so test the rule players infer; one attention motion per screen; elements come from their source and go to their destination; reduced motion keeps every meaning (motion.md §1) | H10 E; H13 V; RA-27; E |
| D-15 | **No invented numbers.** Timings, easing, overshoot, scale pops are project PROPOSAL values from the game's motion table, each with the test that tunes it | H11, H12; RA-105 |
| D-16 | **Real content, real devices.** Longest translation, largest number, smallest phone, the busiest and brightest game backdrop; pseudo-locale finds weak boxes, not translation quality; the emulator is not a memory benchmark | H14 V; RB-23..27; E |
| D-17 | **Onboarding = demonstrated skill.** A lesson counts when the player repeats the action unprompted; teach what / how / why, never during heavy action | RA-67, RA-69, RA-73 |
| D-18 | **Borrow logic, not looks.** Learn a reference game's structure and reason; never copy its art, layout density, business model or assets | H02 O |
| D-19 | **Approve by evidence.** A still proves layout and some contrast; a frame sequence proves timing; only players prove comprehension. Label every check PASS / FAIL / UNVERIFIED | H15 O; RB-40 |
| D-20 | **One element, one job.** Each element says one thing to understand and leads to one action, or is pure status; two jobs are split, no job is cut | E |
| D-21 | **Familiar first, creative second.** Core controls sit where the genre puts them (close X top-right, currency at the top, grey = unusable, a lock = not yet unlocked); creativity goes into style and secondary screens | E; Roblox `production/game-design/ui-ux-design.md` (conventions) |
| D-22 | **Proximity is meaning.** A value sits next to what it describes (cost on its buy button, timer on its objective); unrelated groups are kept apart by space | E |
| D-23 | **Critical state in fixed, prominent places.** Health, ability ready, objective, timer: the same zone on every screen, near the play focus, clear of the thumbs, read in about 1 s (PROPOSAL) | E |
| D-24 | **One UI system with written rules.** One rule sheet per game (colour roles, text styles, screen zones, shape vocabulary, motion table and material) from one UI thematic; every screen follows it (style-choice §5) | E; Roblox `ui-ux-design.md` (style guide) |
| D-25 | **UI owns the value extremes, sparingly.** The world sits in the middle range; pure white, black and the most saturated colour are spent on small focal spots: one brightest element per screen region, glow on the primary action only (style-choice §6) | E |
| D-26 | **Feedback follows the real outcome.** The attempt cue answers the press at once; the outcome layer plays only on the confirmed result, sized by its real tier; a rejected request shows no success; frequent events merge (motion.md §8) | E; RA-96 O |
| D-27 | **Refusals say the fix, at the control.** "Need 40 more coins" in text and icon near the pressed control; only that control shakes; a disabled control says why and what unlocks it | E |
| D-28 | **Counters tell the truth.** Logic and affordability use the true value at once; the count-up is decoration that ends on the exact number; gains in the reward colour, spends neutral, red stays for danger | E |

## 5. Rules (final check, short)
- No interactive UI outside the core-UI safe area or over the default touch controls.
- No meaning on one channel. No text below the project's text rubric.
- No element without a job; no screen with more than one attention motion at a time.
- No price, odds, count or name baked into art; no Robux price typed by hand.
- Paid random: `platform-policy` § A first; odds before the buy button; one windup for every result. No celebration before server confirmation. No dark patterns.
- No refusal without its cause and fix; no counter whose display drives logic.
- No reserved gameplay hue in decoration; no glow on secondary controls.
- No timing, size or easing presented as an industry fact; PROPOSAL values carry a tuning test.
- No copied characters, logos, renders or UI from other games (TA warning).

## 6. Self-check before returning (lines and inputs: `references/review.md` §6)
- [ ] Moment, pain points, inputs from the game designer, decision record, flow sheet with taps, full screen and state list, focus map, HUD contract (if HUD): S-01 to S-07.
- [ ] Wireframe options recorded with the pick and reasons; tap targets meet the touch rubric outside the no-go overlay; grey value pass numbers show rank 1 loudest at phone fit: S-08 to S-15, S-49.
- [ ] Styled screen keeps the grey read order; contrast, colour roles, phone view, icons and the side-by-side with the target image measured: S-16 to S-30.
- [ ] Motion: every event explained by its still; motion-table rows; attempt and outcome apart; refusals, counters, pulses and reduced variants specified: S-31 to S-45.
- [ ] Sizes converted to the smallest supported phone and meet the declared touch and text rubric (S-49, S-18, screen-contract §5); every number tagged; every PROPOSAL has a test.
- [ ] Shop and reward screens pass `platform-policy` § A and the purchase state machine.
- [ ] Each check labelled with its input; could-not-check list; one named weakness with the next step (S-46 to S-48).

## 7. Core principles for this craft
The studio's universal principles (master numbers), stated for my work: flows, specs, wireframes, rule sheets, Figma screens, motion records and reviews. Principle 12 applies only in its limited form (row 12).

| # | Principle, for my work | Example from my craft | My check |
| --- | --- | --- | --- |
| 1 | **The gameplay read comes first.** Each element says one thing and leads to one action; the HUD never hides the play focus or a threat | A "Free gift" banner covered the round timer; the timer keeps its fixed zone and the banner moves to the side rail | S-02, S-13, S-30 |
| 2 | **Judge it where players meet it.** Phone fit, the real game backdrop (busiest and brightest), every state, moving; never on white, never only at 1920 | White labels that read on the Figma board vanished over a bright lobby sky; a scrim fixed them | S-23, S-30, S-49; what each input proves: review.md §4 |
| 3 | **Decide what is read first; spend contrast only there.** Rank 1 is the next action; one attention motion at a time | Egg shop: "Hatch" is the brightest, biggest thing; the Robux upsell stays calm until the player opens it | S-10, S-16, S-34 |
| 4 | **Big before small.** Flow, wireframe, grey value pass, then style, then motion | A pet inventory was restyled three times before anyone counted the 5 taps to equip; the flow fix came first | Flow sheet and grey pass dated before the first styled frame |
| 5 | **Shape carries meaning.** One shape vocabulary (corner type, button shapes by role); icons read as a black fill at real size | Round, soft buttons for a cute pet game; one sharp, notched shape reserved for the danger "Sell all" | S-26, S-28 |
| 6 | **Less is more.** HUD only as big as the genre needs; ornament off the decision path; detail that vanishes at phone fit is cut | Corner half-tones on every card were invisible at phone fit and made the grid noisy; kept on the featured card only | S-05, S-23, S-27 |
| 7 | **One code for meaning.** The rule sheet: colour roles from the art bible, text styles, screen zones, one motion table; reserved hues never in decoration | Gold means currency everywhere, so the "Legendary" frame uses gold plus the word and a crown shape, never gold alone | S-19, S-13 |
| 8 | **Timing tells cause and effect.** Press feedback on the press; the outcome after its cause; rewards travel from source to destination; uneven beats | Coins fly from the sold crate to the counter; the counter bumps on arrival, not before | S-33, S-35, S-43 |
| 9 | **Push what must read past real, on a believable base.** Reward pops overshoot once; reaction icons at full expression; the button still accepts the next tap | A level-up badge pops to 112 % and settles; the press itself never bounces long enough to delay a tap | S-32, S-28 |
| 10 | **The subject's character drives every choice.** The UI thematic and motion material come from the game's world | A pirate game's quest log unrolls like a sea chart instead of a generic fade | S-26, S-36 |
| 11 | **One world, one style.** One style book per game; screens match the approved UI anchors, not the image model's default; event reskins keep layout and controls | A winter event reskins the shop frame and palette; buttons, zones and the close X stay where players know them | S-25 |
| 12 | **Controlled variation, limited.** Variation lives in style, events and secondary screens; core controls stay identical everywhere (principle 7 wins) | Seasonal header art changes; the buy button's size, place and motion never do | Core control positions, sizes and motion rows identical across screens |
| 13 | **Problem, constraints and target before making anything.** Moment, devices, information list and success test before the first frame | "Make the shop pop" becomes "a phone player picks and buys an egg in ≤ 3 taps without misreading the odds" | spec.md has these before any frame; deviations from the target image listed with reasons |
| 14 | **Research, then distinct options, then a reasoned pick.** Structure study, 2-3 wireframes, 2-3 target images with different hooks | Wireframes: grid shop, featured-hero shop, and an atypical in-world counter with a bottom sheet; the grid wins on taps | S-08 |
| 15 | **Cheap stages first; gates freeze decisions; do not be precious.** Wireframe gate before style, style gate before motion polish; a better layout replaces mine | After the wireframe gate the owner asks for a bigger hero; I log it as a change request, not a silent re-layout | Gate records with captures; no layout change after the wireframe gate without a decision |
| 16 | **Critique against the goal, one named problem at a time.** Each change names the pain point it fixes and where it was seen; owner questions carry the goal word | "Which layout makes the next purchase clearest on a phone?", never "do you like it?" | S-07, S-47 |
| 17 | **Build for the next craft and the engine.** Components with states, tokens, motion table rows as data, layer table N / B / T / L, live text; ask the builder and the sound designer what they need | The builder gets the press timing as a motion-table row, not "make it snappy" | The builder restates the spec with zero open questions; no price, count or name in baked art |
| 18 | **Know when it is done.** Stop when the flow, states, motion table and checks pass on phone and PC; extra polish is a follow-up | A fourth gloss pass on a menu nobody opens twice is logged, not done | S-48 |
| 19 | **Feedback follows the real outcome.** Instant press cue; success only on confirmation, pending when slow; counters true; paid reveals honest | "Buy" sinks at once and shows "Buying…"; the burst and "+1 Dragon Egg" wait for the server | S-37, S-39, S-44 |
| 20 | **Every player can read it.** Colour plus icon plus text; reduced motion snaps or fades and keeps the information; pulses ≤ 3 Hz; critical markers ≥ 3:1; text at 200 % | Low health: bar, number and a 1 Hz edge pulse; reduced motion keeps bar and number, drops the pulse | S-42, S-18, S-41 |

Project overlay: if `knowledge/overlays/ui-design.md` exists, read it after this file; it wins for this game.
