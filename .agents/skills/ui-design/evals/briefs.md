> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): C7-C12, brief 5 (calibration)

# Eval briefs for the UI/UX designer (ui-design + ui-figma + style books)

Give the agent the brief text only. Grade each check pass / fail. A brief passes at ≥ 80 % of its checks with no "must" check failed. No hidden test set exists: all four owner tutorials were used to build the skills (J002). Brief 1 is the G2 first real task.

| ID | Common check |
| --- | --- |
| C1 (must) | `spec.md` has the moment, decision record, full state list, focus map; every number tagged (source or PROPOSAL); no timing or size presented as an industry fact |
| C2 (must) | Sizes converted to the smallest supported phone and checked against one declared touch rubric (ui-design screen-contract §5) |
| C3 (must) | Every layer marked native / baked / tiled; no runtime blend modes, inner shadows, blurs or dashed strokes; no text, price or count in baked art |
| C4 | Built from components with state variants; tokens (radius, outline, lip, text ladder, spacing) consistent and from the chosen style book |
| C5 | Self-review screenshots: phone, tablet and PC size, grayscale, longest text, each state; labels MCP-verified (Figma) vs not verified |
| C6 | Generated images (if any): originals, no text, logged with model and prompt, inside the image budget |
| C7 (briefs 1-3) | Flow sheet with taps per task (ui-design §3 step 3; screen-contract §7) |
| C8 (briefs 1-3) | 2-3 wireframe options that differ in structure, the first labelled warm-up, one atypical; the pick and each rejection have a reason (ui-design §3 step 5; review §6 S-08) |
| C9 (briefs 1-3) | Grey value pass with numbers: in the phone-fit luminance image rank 1 is the loudest (largest contrast to its ring), rank 2 next (ui-design §3 step 6; review §6 S-10, S-11) |
| C10 (briefs 1-3) | Motion records name the motion-table row of every animated element; a value without a row is tagged PROPOSAL (ui-design §3 step 9; motion §7; review §6 S-32) |
| C11 | Every refusal names its cause and its fix at the control, in text and icon (motion §8; review §6 S-38) |
| C12 | A rejected request shows no success layer: success plays only on confirmation (ui-design D-26; review §6 S-37) |

## 1. Cartoon pet shop (G2 first task)
> A pet simulator for kids, mostly on phones. Make the egg shop screen: three eggs the player can buy with in-game coins, one featured egg for Robux. Cartoon style.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Paid-random rules: every pet and its % odds visible before buying (labelled "Odds", totals 100 %), for the coin eggs too if coins can be bought with Robux (ui-design D-13, platform-policy) |
| 1.2 (must) | Purchase states: inspect, review, pending, confirmed, failed, not enough coins; celebration only after confirmation; Robux price live |
| 1.3 | Cartoon tokens from ui-style-cartoon §4 (phone-checked: outline 5, halo 10, rim 4, lip 8 / 10, Fredoka One with stroke and depth) |
| 1.4 | Featured egg is the loudest element; buy buttons readable in grayscale; rarity by label, not colour only |
| 1.5 | Close button and buy buttons meet the touch rubric on a small phone; nothing in the bottom corners |
| 1.6 | Young audience: claiming a free reward cannot be confused with buying |

## 2. Stud HUD on phones
> An obby with checkpoints. Players need to see coins, open the shop, skip a stage (Robux) and toggle music. Stud style. Most players are on phones.

| Check | Expected |
| --- | --- |
| 2.1 (must) | HUD contract: actionable now / planning / on demand; nothing under the jump button, the thumbstick zone or Roblox's top-left / top-right buttons |
| 2.2 (must) | Frequent side buttons sized for phones (the tutorial's ≈ 98 px ≈ 29 pt fails 44 pt; ≥ 150 canvas px at f 0.294), or larger hit areas stated |
| 2.3 | Role colours plus icons or labels; the music toggle shows its current state |
| 2.4 | Skip-stage purchase: price live, pending and owned states, no fake urgency |
| 2.5 | Stud tile exported once as a tile; outline 5 / inner stroke 3-4-5 ladder / lip 7 consistent |

## 3. Anime summon screen
> An anime tower-defense game. Make the summon (banner) screen and the reveal for 1x and 10x summons using gems bought with Robux. Make it hype.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Odds before commit, labelled, 100 %, including pity or guaranteed rules if any; restricted players get a blocked or alternative path |
| 3.2 (must) | Reveal follows the reward states: confirmed outcome first, skip reaches the same result, 10x ends on a full summary; no hint that tapping speed changes odds |
| 3.3 (must) | All character art original or generated originals; no franchise look-alikes |
| 3.4 | Rarity by colour **and** label; reduced-motion version keeps every meaning; flash safety noted |
| 3.5 | Glow reserved for the summon button and the hero; secondary controls calm |

## 4. Pixel hotbar and health review
> Review this rogue-like HUD (screenshot provided): 9-slot hotbar, health and stamina bars, a party list top-right. Players say it is hard to read on phones.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Findings ranked with the failed check ids (ui-design review §1), each with a fix; "could not check" list for anything a still image cannot prove |
| 4.2 | Art-pixel scale problem identified (1 px lines at phone scale) with the S rule fix (ui-style-pixel §3) |
| 4.3 | Contrast measured on the weakest background; low health not colour-only |
| 4.4 | Party list position checked against Roblox's top-right buttons |
| 4.5 | No invented player data ("players prefer..."): proposes how to test |

## 5. Calibration: one button press in four moods
> One primary "Play" button. Make its press in four moods: heavy, light, playful, premium. Same button art and canvas for all four; show each as a Figma prototype or a frame folder at normal speed.

| Check | Expected |
| --- | --- |
| 5.1 (must) | The grader, shown the four unlabelled and in random order, matches each to its mood (all four correct) |
| 5.2 | Each mood is a motion-table row with its Material column filled (motion §7); every value PROPOSAL |
| 5.3 | The moods differ in timing, easing, overshoot or scale, not only colour; exits no longer than entrances (review §6 S-32) |
| 5.4 | In every mood the press answers on the press frame or the next (motion §2; review §6 S-33) |
| 5.5 | Feel is not claimed from stills: the prototype or frame folder is the evidence, labelled (ui-design §3 step 11) |
