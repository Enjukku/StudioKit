---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J012; owner's marketing paper, thumbnail and icon checklist (knowledge/reference/marketing/03-launch-measurement-policy-process-templates.md §6.2 TP-THUMB); Roblox icon and thumbnail docs (mirror production/publishing/experience-icons.md, thumbnails.md); tools/art/thumb_check.py
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Thumbnail and icon checklist: <game> · <asset id> · <date>

Workflow: `marketing-craft` (images and checks). One copy per candidate image, next to its image brief. Fill §A with the tool before you look; then §B. Icon and thumbnail are checked **separately**: a picture that survives a wide crop may fail a square one.

**Rule of use.** PASS or FAIL with the named evidence. Missing evidence = FAIL. The tool measures; it never says "good". A number becomes pass/fail only with a tolerance the owner or art director approved (decision id). Nothing goes to the owner with an unexplained FAIL.

## A. Measured (`python tools/art/thumb_check.py ...`)
| Key | Value |
| --- | --- |
| surface | icon / thumbnail |
| file, size px, file size | |
| master check (icon: square, ≥ 512×512; thumbnail: 16:9, size vs 1920×1080, file size for personalization) | tool JSON field + docs line |
| small size used, and its source | icon: the size the icons doc names; thumbnail: tile width measured from a phone capture (file) |
| subject given by | mask / box / key (none = one-moment and contrast fields "not measured") |
| subject vs surround value contrast at small size | |
| separate subjects at small size (count, largest share) | |
| subject near the lower edge (thumbnail) | |
| contact sheet | path |
| tolerance used, with decision id | or "none: diagnostics only" |

## B. Pass or fail
| # | Pass when | Evidence | Result |
| --- | --- | --- | --- |
| I1 | The central action is clear at display size | the contact sheet's small preview with the title under it | |
| I2 | The subject reads without any tiny text | text-hidden preview (cover or remove the text, then view small) | |
| I3 | Subject and background do not merge | grayscale preview + the §A contrast numbers | |
| I4 | One clear moment: one hero, one action, one consequence | §A subject count + the agent's own look at the small preview, in one line | |
| I5 | The promised object, reward or event exists in the game | build capture + item or feature id; promise-ledger claim id | |
| I6 | The emotion fits the real player fantasy | the art director's note on tone and audience fit | |
| I7 | No fake Roblox reward, purchase, button, currency or system control | interface and policy review (who, date) | |
| I8 | No number, price, reward or status label invented by the image model | manual compare with the brief and the game's config | |
| I9 | The subject survives every crop, overlay and safe area | one preview per destination (Home tile, game page, ads tile if used) | |
| I10 | Protected characters, logos, fonts, music references and likenesses are cleared | rights record, not "it is trending" | |
| I11 | Distinct from our other live images and from competitors | comparison sheet with ids and date | |
| I12 | It tests one clear hypothesis | one line: which player expectation this image changes | |
| I13 | Traceable and reversible | brief id, art_refs record (prompt, inputs), edit history, owner approval, the image it replaces | |
| I14 | Generated key art is not called gameplay | label on the asset record: key art / gameplay capture | |

## C. Result
| Key | Value |
| --- | --- |
| verdict | ready for owner review / blocked (items) |
| art director recommendation | |
| owner decision id | |
