---
type: job
scope: game
status: active
updated: 2026-10-24
source: J020-sound-workbench
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-24

# Review: soundbench `rank` on layered rounds (2859a06), by reviewer

**Depth:** deep. `rank` decides which takes a cue uses and when it goes to the owner (J020-D7). The main risk is a wrong number that looks right. Round 1, against the frozen revision 2859a06; the working tree under `tools/audio` equals it (`render.py` is unchanged from 2859a06~1). I read the diff and the changed files before the commit message's claims. All runs used copies of the 62 real takes in the session scratchpad (`raw/`, scripts in `scripts/`); no ElevenLabs call; no repository file was written except this review.

**Goal questions:**
1. Is every layered `use` (exit 0) a recipe that `render` passes, for the recipe.json that rank reads (design steps, loop, variants, align or offset, a layer from an earlier round)? (§6.3-4, rank's "every use is proven")
2. Do the round and the 3-round limit stay per cue, the same count `generate` uses? (J020-D7)
3. Are the 16 `mix_misses` on level a true property of the mix or a wrong level or ceiling calculation? (§7 level derivation)
4. Is one-shot output unchanged by the refactors? (no regression)

**Verb and weight:** "choose the takes of a layered cue". I weighted the proof (harm area 3 analogue: a false verdict) and the round count most. Areas 1, 2, 4 and 5 hardly apply to an offline tool; I walked them (coverage in the hand-back).

```text
<spec>
artifact: tools/audio/soundbench@2859a06 (rank.py, __main__.py, README.md; tests test_soundbench_rank_layers.py, test_soundbench_realtakes.py)
reviewer: reviewer
looked_at_first: [git show 2859a06 (rank.py, __main__.py, README.md), render.py whole (plan, plan_form, mix_layers, layer_rows, render), generate.py cue_rounds/plan, the two test files, then the commit message]
findings:
  - {id: F1, class: blocking, where: "tools/audio/soundbench/rank.py:805 (place_candidate: `\"design\": []`), :894 (mix_entry: `\"design\": []`, and the mix is judged with no recipe design pass), :911-912 (prove_layers renders `design: []` for every layer and the mix); the warning at :788-792",
     expected: "rank's own doc: a `use` is proven by a real render of that recipe. For a layered cue the recipe already exists (rank requires recipe.json and reads its layers, targets and placement), so `use` must mean: recipe.json as written, with rank's takes and rank's edit pass, renders with exit 0",
     observed: "rank judges and proves a different recipe from the one it reads: every layer's design steps and the mix's design steps are removed. Test: real takes, the real-take test's layout (body aligned on its main transient at 300 ms, air at 60 ms on F-01, -6 dB; F-09 -18 +-1, TP max -1). Six recipe.json variants that only add one design step: rank exits 0 `use` on all six (the proof agrees, must_failed []), and render of recipe.json with rank's chosen takes and edit exits 1 on five of them, all on `level`: hit-speed-2 with a body `highpass 60` (a plain clean step) -> rank level -18.643 (pass), render -20.071 (min -19.0); the same with body `space 0.6 s` and with mix `transient +6 dB`; hit-strength-4 with body `highpass 60` and with body `space`. Only the warning line says design steps are not run; the verdict still says 'proven by a real render' and the `use` text says 'start recipe.json's layers from these takes (their placement as written)', while `recipe_layers` carries `design: []`, so a driver that copies it deletes the designer's steps to make render pass",
     evidence: "High (a false exit 0 on the main path: 5 of 6 ordinary design steps flip the verdict on real takes; the stripped design is the reason the proof agrees). Runs: scratchpad scripts/e1_design.py, scripts/e1b.py. The 11 layered tests and 8 planted faults pass because every fixture recipe has design: []. Label: not verified in Studio (a tool run, reproducible)",
     smallest_fix: "Keep the recipe's design: pass each planned layer with its own `design` to mix_layers (place_candidate, mix_entry), run the recipe's mix design (`render.apply_steps((('design', design),), ...)`) on the mix before `judge`, and prove recipe.json itself with only the layer `take` fields and `edit` replaced",
     protect: "the frame settling and the mix row guard (layer rows are read after the layer's design in render too); one-shot output (it has no recipe input); the 6 `use` and 16 `mix_misses` on design-free recipes",
     retest: "e1_design.py: each case's rank verdict equals render's exit on recipe.json (no `use` where render exits 1); add a layered test with a layer design step and a mix design step, and a planted fault 'design stripped' that the test catches"}
  - {id: F2, class: recommendation, where: "tools/audio/soundbench/rank.py:748-765 (cue_round: rounds from takes/ only, current layer names only) and :935 (the `last` decision; :613 in the plain path); pre-existing in find_takes for one-shots",
     expected: "J020-D7 as generate counts it (generate.py cue_rounds :332-345, lead decision on review-generate F5): every file of the cue or any layer, in takes/ and takes/rejected/, under any name",
     observed: "Round 1 (body + air) and round 2 (body) in takes/, round 3's body takes all rejected at intake (takes/rejected/*.body.r3.t*). generate counts rounds [1, 2, 3]. rank ranks round 2, rounds_left 1, exit 1 `regenerate`: 'regenerate the layers ['body'] ... (round 3 of 3)'. generate.plan then refuses round 4 ('it goes to the owner'). The cue should be `owner` with its table; instead the driver gets a regenerate instruction that the next tool refuses. A renamed layer's old round is missed the same way",
     evidence: "Medium (D7 off by one in rank's verdict text and rounds_left; no extra paid round, because generate refuses). Run: scratchpad scripts/e3_d7.py. Label: not verified in Studio",
     smallest_fix: "Take the count from generate's one function: `last = max(generate.cue_rounds(cue_dir / 'takes', cue)) >= MAX_ROUNDS` and rounds_left from the same maximum, in both the layered and the plain path; the round to rank stays the highest round with takes in takes/",
     protect: "test_the_cue_round_counts_every_layer_and_round_3_goes_to_the_owner; the plain path's report (byte-identical apart from rounds_left in this case)",
     retest: "e3_d7.py: rank gives `owner`, rounds_left 0"}
  - {id: F3, class: recommendation, where: "tools/audio/soundbench/rank.py:911-912 (prove_layers: the proof recipe has no `loop`) with fix_plan :245-253 (trim and fade planned for the mix)",
     expected: "render refuses trim, cut and fade in the edit pass of a loop recipe (render.py:369-372); rank should not give exit 0 to an edit render refuses for the recipe it read",
     observed: "Layered ambience card (form.loop, onset_ms max 5 must), recipe.json with loop_bed (crossfade 50 ms), the same real takes: rank exits 0 `use` with edit [trim, loudness, peak], proof must_failed [] and no warning or form note; render of recipe.json with those takes and that edit refuses: 'loop: ['trim'] in the edit pass would cut or fade across the seam'. Variants are fine: a layered hit with form.variants 3 and a variants block gets `use` with the form note, and render of recipe.json exits 0 (2 of 2)",
     evidence: "Medium (exit 0 that render refuses with exit 2; needs a loop card with an onset, main-transient or edge-click must; the one-shot path has the same plan on loop cards, review-step6 R2). Run: scratchpad scripts/e2_loop.py, scripts/e2_variants.py. Label: not verified in Studio",
     smallest_fix: "With F1's fix (prove recipe.json as written, loop included) this becomes a refusal, not a false use. To make it a verdict: for a recipe with a loop, plan no trim, cut or fade (the plain loudness and peak plan only)",
     protect: "the variants case (use, render 0)",
     retest: "e2_loop.py: no exit 0 that render refuses"}
answers:
  - "Q1 false use: yes, through the recipe's design steps (F1) and, on loop cards, the loop (F3). A layer read from an earlier round is safe: G-1 checked, copied by name into the proof, warned. Align versus offset is safe: each layer is placed alone in render's own mix_layers (the align correction reads the layer alone, so its offset does not depend on the other layers), and the mix guard (rank.py:898-901) compares every chosen layer row with the real mix"
  - "Q2 D7: the per-cue round is right for files in takes/ (mixing layers across rounds counts one round per cue; round 3 goes to the owner). It differs from generate for rejected rounds and renamed layers (F2)"
  - "Q3 frame settling: when the tops repeat, each top was read in the frame max(own, other tops) = the frame of the mix the tops make, so the guard cannot be reached with a settled choice; a 2-cycle ends in a refusal (exit 2), never a verdict. The settled pair is one fixed point, not necessarily the best pair; the verdict text says rank tries no other combination. No finding. Every real round settled in 2 passes (12 of 12 here)"
  - "Q4 the 16 mix_misses: a correct verdict. Hand check against a real render, independent numpy F-09 (loudest 400 ms RMS) and x4 true peak: hit-strength-1 mix crest (F-09 - TP) 22.1 dB; with TP at -1.5 the best F-09 is -23.6, target -18 +-1, so gain alone cannot reach it; render exits 1 on level at -23.614, the same as rank's derivation (-23.614). thump-4: best -21.6 to -22.0 (my F-09 is not bound to the F-12 sound, 0.36 dB lower), render -21.618. The summing does not cause it: the mix's TP equals the body take's own (-0.37 / -0.37; 0.01 / 0.01) and the air layer lowers the crest (24.4 -> 22.1 dB). The README's 'the summed layers' true peak caps the loudness gain' is true in value; the cap is the hit's own transient"
  - "Q5 refactors: one-shot rank of 4 real rounds with the old (2859a06~1) and the new rank.py: the .json and .md reports are byte-identical apart from the folder path in `pictures` (scripts/e5_identity.py). judge, plain_rounds, render_copy, row_mismatches and the Markdown helpers are moves with the same order of keys"
keep:
  - "layer placement, rows, the mix and the proof all go through render's own functions (mix_layers, layer_rows, apply_steps, evaluate): one house way, no second mixer"
  - "the mix row guard (rank.py:898-901) and the proof comparing every whole-cue row and every layer row"
  - "frame settling with identity comparison and a refusal after LAYER_FRAME_PASSES"
  - "mixed sample rates refused before ranking (rank.py:990-993), since render resamples to the first layer's rate"
  - "a round with plain and layer takes refused; a stray layer name refused; the plain path unchanged (byte-identical)"
  - "per-layer NEAR margins read from the target's own margin"
weakest_part: "Frame settling was only seen settling (2 passes on every real round); I did not build a synthetic 2-cycle to watch the refusal fire. F3 needs an unusual card (an onset must on a loop card), so its weight on real cues is unproven"
could_not_check:
  - {step: "a real layered ambience or loop cue", missing_input: "real takes of 2 s or more (the set has none)", closes_it: "the first long layered cue ranked and rendered", who: "feature-builder"}
  - {step: "the planted-fault log beyond the in-file test", missing_input: "a qa-lead planted-fault result on 2859a06", closes_it: "the in-file test ran here: 8 of 8 caught, 11 tests OK in 17 s; F1 is a fault none of them plant", who: "qa-lead"}
  - {step: "LAYER_FRAME_PASSES refusal path", missing_input: "a round whose tops oscillate", closes_it: "a synthetic 2-cycle test", who: "feature-builder"}
verdict: fix-first
</spec>
```

## Round 2 (6922e83)

> Author: reviewer · claude-opus-5-5 · medium · 2026-10-24

Frozen revision 6922e83, found with `git log -1 --grep "^J020 soundbench layered rank repair round 1"`. The working tree under `tools/audio` matches it. Scope: F1-F3, the variants path the builder named as untested, the round count's effect on one-shots, and new ways around each fix. The layered tests pass (15, including the planted-fault test). Runs: copies of the real takes in the session scratchpad (`scripts/`: e1_design, e1b, e2_loop, e2_variants, e3_d7 re-run; r2_variants, r2_loop, r2_rounds, e5_identity new).

```text
<spec>
artifact: tools/audio/soundbench/rank.py@6922e83
reviewer: reviewer
looked_at_first: [git show 6922e83 (rank.py), then the coordinator's summary of the builder's report]
earlier_findings:
  - {id: F1, status: fixed, retrace: "e1_design: rank's verdict now equals render's exit on recipe.json in 6 of 6 (5 mix_misses on level with render exit 1; hit-strength-4 + mix transient: use, render 0). e1b: rank's mix level -20.071 = render's -20.071 (was -18.643). The proof renders recipe.json with only the layer takes and edit replaced (proof_recipe)"}
  - {id: F2, status: fixed, retrace: "e3_d7: rank round 2, rounds_left 0, exit 1 owner, 'round 3 of 3'; generate refuses round 4: they agree. The round ranked is unchanged (rounds_used only sets last, rounds_left and the text)"}
  - {id: F3, status: fixed for what it claims, retrace: "e2_loop: the mix plan has no trim (edit [loudness, peak]); rank mix_misses on onset_ms; render of recipe.json exits 1 on onset_ms and form.loop_crossfade_level. No exit 0 that render refuses with exit 2. But see R2-1: the loop's own form rows are still exempted"}
findings:
  - {id: R2-1, class: blocking, where: "tools/audio/soundbench/rank.py:980-983 (proof_misses drops every must row starting form. or variants.) used by layer_verdict :1005",
     expected: "F1's own rule: `use` means recipe.json as written, with rank's takes and edit, renders with exit 0. The form.*/variants.* exemption (review-step6 R2) existed because the old proof recipe had no loop or variants step; the proof recipe is now recipe.json itself, so a failing form or variants row is a failure of the recipe rank tells the driver to use",
     observed: "(a) Variants, the builder's named untested path: a layered hit, card form.variants 4, level F-09 -24 +-1, recipe variants {seed 19, max_cents 50, max_db 1.0}. rank exits 0 `use`, proof.must_failed ['variants.level_spread'], with the note 'form rows (loop, variants) are judged at render'. Render of recipe.json exits 1: variants.level_spread 1.098 > 1.0 (levels -24.0, -24.44, -24.98, -23.01; every per-file level row passes, so nothing else catches it). Same on hit-strength-4 (seed 19) and hit-speed-2 with 5 variants (seed 238: spread 1.062). (b) Loop: the e2_loop card without its onset target: rank exits 0 `use` with proof.must_failed ['form.loop_crossfade_level']; render of recipe.json exits 1 on that row (hit-speed-2 and hit-strength-4)",
     evidence: "High (exit 0 `use` while the proof render of the exact recipe exits 1, on 5 of 5 cases built; rank already holds the failing row). Runs: scratchpad scripts/r2_variants.py (level -24), scripts/r2_loop.py. Label: not verified in Studio (a tool run, reproducible)",
     smallest_fix: "In the layered path, `use` only when the proof's must_failed is empty (drop the form./variants. filter there; keep form_note for the one-shot path, whose proof recipe still has no loop or variants step)",
     protect: "per-variant rows (`<cue>-v<k>:level`) already turning use into mix_misses; e2_variants (use, render 0); the one-shot form_note",
     retest: "r2_variants.py and r2_loop.py: rank gives mix_misses (exit 1) naming variants.level_spread / form.loop_crossfade_level; add a layered variants test whose spread fails at render, and a planted fault 'form rows exempted'"}
broke_check:
  - "one-shot output: e5_identity on 4 real rounds (3 use, 1 regenerate): .json and .md identical to 2859a06~1 apart from the folder path"
  - "one-shot rounds (r2_rounds, swish-3 at rounds 1, 2, 3, old vs new): the round ranked and the default-round texts are identical ('round 2 of 3', 'round 3 of 3', owner after round 3). Only `--round 1` on an older round changed: rounds_left and the text now count the rounds used (left 0, owner after round 3), which matches generate; before it said 'regenerate (round 2 of 3)', which generate would refuse"
  - "the mix's design pass runs with context(card, []); the only op reading the context's fade_out_ms is cut (ops.py:640), an edit step, so the design pass is the same as render's"
  - "recipe.json's own `edit` is not read (warned); rank's `recipe` carries its own edit: consistent with the use text"
keep:
  - "proof_recipe: recipe.json as written with only takes and edit replaced; the `use` carries it"
  - "the mix built in render's order (layer design, mix design, loop) before judge"
  - "rounds_used from generate.cue_rounds, the ranked round unchanged"
  - "LOOP_REFUSES in plan_for, with its own reason in _why_kept"
pre_existing_follow_up:
  - "render/assemble (step 6, not this change): variant_plan draws gains in +-max_db around 0, but R-31's row measures each file against the set's mean, so a legal recipe (max_db 1.0, the allowed maximum) can plan a set that render's own must row fails (seed 19, 4 variants: 1.0975 dB by the plan alone). Render catches it (exit 1), so no wrong file ships; the planner should keep the drawn set within +-max_db of its own mean. Owner: render's builder"
weakest_part: "The variants case needed a level target with headroom (-24): at -18 the peak cap compressed the spread to 0.26-0.46 dB, so how often real cards hit R2-1 through variants depends on the card"
could_not_check:
  - {step: "LAYER_FRAME_PASSES refusal path (from round 1)", missing_input: "a round whose tops oscillate", closes_it: "a synthetic 2-cycle test", who: "feature-builder"}
  - {step: "a real layered loop cue", missing_input: "real takes of 2 s or more", closes_it: "the first long layered cue ranked and rendered", who: "feature-builder"}
verdict: fix-first
</spec>
```
