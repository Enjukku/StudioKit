---
name: ui-design
description: What and why for a Roblox game screen before anyone styles it - the player's decision, what is seen first, every state and device, shop and paid-random honesty, onboarding. Use before designing or reviewing any HUD, menu, shop, inventory, popup or reward screen, for "the UI is confusing", "players can't find X", "make the shop clear". Does not draw (ui-figma) or build (ui-basics).
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J002. Evidence: owner-supplied research paper (RP, ChatGPT, paper's stated date 2026-10-21; notes `knowledge/reference/ui/05a`-`06b`), tags kept as the paper gives them: **V** VERIFIED (published rule or measurement), **E** EXPERIENCE (studio account), **O** OPINION (the paper's adaptation), **U** UNSPECIFIED (no value exists). Tutorial ids TC/TS/TA/TP: `knowledge/reference/ui/README.md`.

# UI design: the screen works before it is pretty

## 1. When this skill starts
A screen, HUD element, popup, shop, reward sequence or onboarding step is new, changed or under review. It answers: what is the player deciding, what must they see first, what are all the states, what can go wrong, what style fits, and what proves it works. Output feeds a style book and then `ui-basics` (Roblox build).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Decision record, attention inventory, HUD contract, state list, focus map, text-container spec, on-device size math | `references/screen-contract.md` |
| Shops, offers, purchase states, paid random items, ads, rewards, onboarding | `references/shops-rewards-onboarding.md` |
| Motion: what an animation must explain, the 25 motion records, what is a real number and what is not | `references/motion.md` |
| Picking a style, the visual thesis, the style spec table, what to learn from reference games | `references/style-choice.md` |
| Review: the 22-check list, do-not list, AI failure modes, which evidence proves what | `references/review.md` |
| Roblox rules for anything players buy, roll or watch | `platform-policy` skill |
| Roblox build facts (insets, scaling, text, input, native modifiers) | `ui-basics` skill |

## 3. Steps (the designer's process, RP §12, O)
Each step has a deliverable. Write them into `content/ui/<screen-id>/spec.md`.
1. **Player moment.** Goal, what they already know, game state, input device, locale, accessibility settings, cost of failure. *Check:* one sentence says what the player is trying to do.
2. **Evidence ledger.** For every claim you will rely on (a size, a timing, a "players like X"): tag, source, date, unit, scope. Unknown = **U**, never a guess (H12).
3. **Decision and states.** Fill the decision record (goal → info needed → actions → consequence → proof it registered → recovery) and list every state (§4 D-04). *Check:* no component without a role in the record (RA-57).
4. **Wireframe before materials.** Grey boxes, real content (longest name, biggest number, real price format), at least two structures compared, a written reason for the winner (P01, U06). Mark interactive vs decorative bounds and the core-UI safe area.
5. **Visual grammar.** Pick the style book (`references/style-choice.md`); give every shape, colour, type size, icon and material one job (identity, grouping, selection, feedback, warning, ornament) (C12-C14).
6. **Storyboard motion.** Separate beats: input acknowledged · result confirmed · information visible · input available again · decoration ends. Each with cancel, repeat and reduced-motion behaviour (`references/motion.md`).
7. **Implementation contract.** Sizes on the 1920×1080 canvas, states, assets (native vs baked), text behaviour, focus map, motion fields, acceptance tests. Unknown numbers stay PROPOSAL with a test that will set them.
8. **Review the real artifact.** Screenshots at real size per device class, grayscale, smallest phone, longest text, Largest text size, reduced motion, failure states (`references/review.md`).
9. **Test and revise.** Observation for *why*, metrics for *how often*; keep disconfirming results; approved values get versioned as project decisions, never relabelled as "industry standard".

## 4. Design core (what separates great UI from pretty UI)
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | **Decisions before decoration.** Design each screen as a player decision. An attractive redesign that removes a fast route is a regression (VALORANT restored one-click navigation after removing it) | H03 E; RA-32 O; RA-64 V (U07) |
| D-02 | **Priority = salience.** List every element's priority, then check what the render actually makes loud (size, contrast, isolation, motion, sound). A health warning quieter than a shop sparkle fails. Review a grayscale, a small and a moving capture | RA-58, RA-59 O |
| D-03 | **HUD contract.** Sort every HUD fact into *actionable now* (always findable while possible), *planning* (stable secondary region), *on demand* (detail view). Busy HUDs need explicit priority, capacity, replacement and overflow rules | H07, RA-60 O (U05) |
| D-04 | **Every state, named apart.** Entry, normal, empty, max content, loading, pending, error, not enough currency, not eligible, success, recovery; and per item: selected ≠ equipped ≠ owned ≠ claimed. A disabled control says why | RA-62 O; RP §12 step 3 |
| D-05 | **Mobile first, with numbers in their own units.** Roblox DAU 2025: mobile 83 %, desktop 14 %, console 3 % (not 2026, not playtime). Touch rubrics: Apple 44×44 pt frequent / 28×28 pt minor; Android 48×48 dp + 8 dp gap; Xbox 15 mm phone / 24 mm tablet. Pick one rubric per project, write it down, never average them | H01 V; RA-44..47 V; RA-48 O |
| D-06 | **Canvas px are not device size.** A 1920×1080 design fitted to a phone shrinks. Convert before you approve a size (`references/screen-contract.md` §5). Default rubric PROPOSAL: frequent touch controls ≥ 44 pt on the smallest supported phone (≈ 150 canvas px at the phone fit f ≈ 0.294); essential text ≥ 11 pt (≈ 38 px); thick lines ≥ 5 px | arithmetic from P02; O |
| D-07 | **Safe areas.** Interactive UI inside `CoreUISafeInsets` (cutouts + Roblox core UI); default move/jump controls own the lower corners; Roblox's buttons own the top-left and top-right. Decorative and functional bounds are specified separately | RA-49..51 V/O; ui-basics U-01, U-03 |
| D-08 | **Every input reaches everything.** Touch, mouse, gamepad: initial focus, traversal, wrap, back, restored focus per screen; modals trap focus; nothing needs hover or long-press only | RA-53..54 V (XAG 112-113); RA-55 O |
| D-09 | **Meaning never by colour alone.** Rarity, team, danger, success: add text, icon or shape. Reserve one hue for urgent danger | RB-13 V; RA-05, RA-34 |
| D-10 | **Text you can read on the phone.** Meet the project's declared text rubric (default PROPOSAL: font size ≥ 11 pt on the smallest phone; if the XAG rubric is chosen, measure glyph height, not font size); contrast 4.5:1 normal, 3:1 large or inactive, 7:1 high-contrast mode, on the weakest background; works at 200 % text; TextScaled ignores the player's text-size setting. Default text rubric and the outlined-text contrast method: `references/screen-contract.md` §5 | RB-02..12, RB-17 V; rubric P |
| D-11 | **Icons: meaning before polish.** Write what the icon must mean, test unlabelled then in context, at real size and in grayscale; keep labels for unfamiliar categories (Candy Crush: calendar beat the designers' trophy) | H05 E; RA-11, RA-12 |
| D-12 | **Shops are contracts.** Show item, quantity, duration, price (read from Roblox), eligibility, random or not, limits and what happens after; preview ≠ commit; celebrate only after the server confirms. Robux items: Roblox's prompt is the commit step (flow in `references/shops-rewards-onboarding.md` §2) | H08 V; RA-77, RA-78 O; ui-basics U-07 |
| D-13 | **Paid random items:** every outcome and its real % odds before purchase (totals 100 %), a labelled odds button (not a bare ⓘ), an alternative or block for restricted users. No fake discounts, false scarcity or misleading timers | RA-79..81 V (R14-R16); RA-82 O |
| D-14 | **Motion explains, never misleads.** An animation implies a rule; test the rule players infer. Input acknowledgement and confirmed result are separate beats. Reduced motion keeps every meaning | H10 E; H13 V; RA-27 |
| D-15 | **No invented numbers.** Timings, easing, overshoot, scale pops: unspecified in the evidence. Use project PROPOSAL values (start from `ui-basics/references/ui-effects.md`) and say how they will be tuned | H11, H12; RA-105 |
| D-16 | **Real content, real devices.** Longest translation, largest number, smallest phone; pseudo-locale finds weak boxes, not translation quality; the emulator is not a memory benchmark | H14 V; RB-23..27 |
| D-17 | **Onboarding = demonstrated skill.** A finished dialogue is not learning; a lesson counts when the player repeats the action unprompted. Teach what / how / why, never during heavy action | RA-67, RA-69, RA-73 |
| D-18 | **Borrow logic, not looks.** Learn each reference game's reason; never copy its art, layout density, business model or assets | H02 O |
| D-19 | **Approve by evidence.** A screenshot proves layout and some contrast; a recording proves sequence and focus; only players prove comprehension. Label every check PASS / FAIL / UNVERIFIED | H15 O; RB-40 |

## 5. Rules (final check, short)
- No interactive UI outside the core-UI safe area or over the default touch controls.
- No meaning by colour, sound or animation alone. No text below the project's text rubric.
- No price, odds, count or name baked into art; no Robux price typed by hand.
- Paid random: odds before commit, labelled, 100 %. No celebration before server confirmation. No dark patterns (`platform-policy`).
- No timing, size or easing presented as an industry fact; PROPOSAL values carry a tuning test.
- No copied characters, logos, renders or UI from other games (TA warning).

## 6. Self-check before returning
- [ ] `spec.md` has the moment, decision record, full state list, focus map and HUD contract (if HUD).
- [ ] Every number has a tag and source; every PROPOSAL has a test.
- [ ] Sizes converted to the smallest supported phone (§5 of screen-contract) and meet the declared touch and text rubric.
- [ ] Grayscale, small-size and longest-text checks done or listed as UNVERIFIED.
- [ ] Shop / reward screens pass the purchase state machine and paid-random rules.
- [ ] Motion beats separated; reduced-motion variant keeps all information.
- [ ] Style chosen with a one-line visual thesis; style book named for the build.

Project overlay: if `knowledge/overlays/ui-design.md` exists, read it after this file; it wins for this game.
