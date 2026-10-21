> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

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
