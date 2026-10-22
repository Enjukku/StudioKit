---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J002; research paper RP §11-12 via knowledge/reference/ui/06a §4, 06b §5 (22 checks, do-not list, failure modes); J018 (self-review by stage, tool runs recorded in knowledge/jobs/J018-riot-craft/coverage/ui-ux-designer.md)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Rebuilt by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§6 self-review by stage with inputs, commands and image budget; §7 my review slot).

# Reviewing a screen

Each check is PASS, FAIL or UNVERIFIED, with the capture or test. **UNVERIFIED is not PASS.** Never write "looks AI-generated"; name the failure (§3). My own design work runs §6 before every hand-back; a built screen runs §1 on Studio captures.

## 1. The release checks (RP §12; untagged rows are the paper's OPINION gates, V marks a verified rule; 23-25 added J018)
| # | Check | Pass when |
| --- | --- | --- |
| 01 | Context | device, build, input, locale, scale recorded |
| 02 | Text size | meets the declared text rubric (default 11 pt font size, screen-contract §5; if XAG is chosen, rendered glyph height, V U12) |
| 03 | Text enlargement | 200 % with no lost content (V U12) |
| 04 | Contrast | 4.5:1 / 3:1 large / 7:1 high-contrast, weakest background (V U13); measured with `look_check.py contrast` (§6 S-18) |
| 05 | Touch | declared rubric met; no overlapping hit areas |
| 06 | Safe areas | nothing required under cutouts, Roblox chrome or the default touch controls |
| 07 | Digital navigation | every action reachable with gamepad / keys |
| 08 | Focus | one clear target; no focus behind an open modal |
| 09 | State semantics | selected / owned / equipped / pending / success distinguishable |
| 10 | Busy HUD | no essential signal pushed out by lower priority |
| 11 | Critical cues | nothing critical by colour only (V U18) |
| 12 | Captions | essential audio events have a visual equivalent |
| 13 | Motion provenance | every timing / easing / scale comes from a motion-table row or carries a PROPOSAL tag |
| 14 | Motion completeness | all handoff fields filled before release |
| 15 | Reduced motion | same meanings in the reduced variant |
| 16 | Temporal safety | flashing checked over time, not from a still; nothing above 3 flashes per second (V U20) |
| 17 | Localisation | price, conditions, names never clipped |
| 18 | Paid randomness | `platform-policy` § A passes; odds total 100 % before the buy button (V R14) |
| 19 | Price and grant | shown price = charge; ownership confirmed before celebration |
| 20 | Advertising | `platform-policy` § C passes (no rewarded ads to under-13; reward disclosed before the ad) |
| 21 | First-session learning | unprompted core action tested; threshold set before the test |
| 22 | Real-device performance | claims backed by phone measurements |
| 23 | Read order | at phone fit, the first-noticed element is rank 1 (§6 S-10 on the build capture) |
| 24 | Outcome feedback | a rejected request shows no success layer; press feedback on the press frame or the next (measured: §6 S-33) |
| 25 | Refusals and counters | every refusal names its cause and fix at the control; counters end on the server value |

## 2. Do not (RP §12; J018 additions after the ·· mark)
infer a rule from a flourish · remove a shortcut for a cleaner layout · treat your icon preference as player meaning · add more equal-priority statuses than the HUD can explain · turn "feels better" into invented % · equate longer sessions or more openings with better UX · use promo screenshots as specs · call one fade constant a studio preset · force repeated spectacle · celebrate when a prompt closes · hide odds behind a bare ⓘ · use old blanket ad age rules · use colour, sound or animation as the only cue · shrink translations to fit an English box · treat emulator memory as a phone benchmark ·· style a screen whose flow is not counted · move two things at once to get attention · make a celebration bigger than its outcome · refuse without saying the fix · let an animated counter drive logic · use a reserved gameplay hue as decoration · judge a screen on white or only at 1920.

## 3. Failure modes in AI-made UI (O; J018 additions last)
Generic panels unrelated to the game · too much text · weak grouping · tiny controls · wrong apparent scale · flat state feedback · many animations at once · everything equally glossy (no rank 1 in grayscale) · the image model's default look instead of the game's anchors · ornaments on the decision path. Diagnose each as: style-role mismatch · failed comprehension · target geometry too small · hidden urgency · missing acknowledgement · motion or performance failure · broken read order.

## 4. Which evidence proves what (O; sharpened J018)
| Evidence | Can support | Cannot support |
| --- | --- | --- |
| spec, motion table, Figma metadata | values, sizes, states, rows | how it reads |
| one still screenshot | layout, contrast, content, read order at that moment | timing, onsets, sound, repetition, cost |
| frame folder at a known frame rate | sequence, timing, focus, interruption (ms = frame interval × index) | feel at normal speed, sound |
| video with audio on the target device | sync of sound and picture | comprehension |
| playable preview judged by the owner at normal speed | feel, motion material, rhythm | numbers |
| real interaction | hit testing | |
| profiler on a phone | performance | |
| real players | comprehension | |
| live analytics | how often, at scale | why |

A simulated user (another model) is not player evidence. Slow playback finds problems but never proves feel. A before/after pair shares camera, backdrop and state, or it is "not verified". Studio MCP captures are frames without sound: sound sync stays "not verified" unless captured on a device. Every number names device, resolution, fit and frame rate.

## 5. Self-review captures (light checks, owner J005-D8)
Numbers for every state; images only for a failing number and for the key states; the full device set (phone, tablet, PC, TV if console) once for the release candidate. Every capture sits over the game backdrop (busiest and brightest), never on white. Look for: elements touching or overlapping that were not designed to; layers showing through popups (counters, labels); variants of one state that use different marks (only some pending buttons show the spinner); focus rings, glows or break-out art cut flat by a parent frame (zoom to 2× on every focused control; J002-T09 popups clipped every focus ring); shine bars outlined by a stray stroke. Label each check: gate-verified / MCP-verified (say Figma or Studio) / owner-confirmed / not verified (AGENTS.md §3).

Image budget per job, unless the brief sets one: wireframe options 1 contact sheet · grey pass 1 luminance image · target references inside the brief's image budget (`ui-figma/references/image-generation.md` §1) · styled screens 1 side-by-side per key screen plus failures · motion ≤ 2 stills per transition and ≤ 4 per celebration · release candidate: one set per device class.

## 6. Self-review by stage (run before every hand-back; each line names its input)
Commands (run from the repo root; `L=tools/art/look_check.py`):
```
python $L value shot.png --box X0,Y0,X1,Y1 --name buy --box ... --name back --compare-subjects --out sal.json
python $L contrast --sample shot.png --fg-box <tight on the glyphs> --bg-box <beside them> --fg-stat p90 --rule wcag-text
python $L palette shot.png --box <panel> --k 8 --roles roles.json [--exclude-box <danger controls>]
python $L thumb shot.png --size 565x318          # the phone fit (1920·f × 1080·f, f from screen-contract §5)
python $L silhouette icon.png --compare other.png ; python $L thumb icon.png --size 48x48
python tools/vfx/clip_metrics.py <press folder>    # writes <press folder>/metrics.json; the lag comes from the next line
python -c "import sys,json;F=json.load(open(sys.argv[1]+'/metrics.json',encoding='utf-8'))['frames'];p=int(sys.argv[2]);b=max([r['coverage_pct'] for r in F if r['ms']<p]+[0]);c=next((r['ms'] for r in F if r['ms']>=p and r['coverage_pct']>b),None);print('pre-press max',b,'cue',c,'lag',None if c is None else c-p)" <press folder> <press ms>
python -c "import sys;from PIL import Image,ImageOps;p=sys.argv[1];ImageOps.mirror(Image.open(p)).save(p[:-4]+'-mirror.png')" shot.png
python -c "import sys,glob,numpy as np;from PIL import Image;b=tuple(map(int,sys.argv[3].split(',')));L=lambda d:sorted(glob.glob(d+'/f*.jpg'));D=[np.abs(np.asarray(Image.open(p).crop(b),float)-np.asarray(Image.open(q).crop(b),float)) for p,q in zip(L(sys.argv[1]),L(sys.argv[2]))];print([(round(float(x.mean()),2),int((x.max(-1)>40).sum())) for x in D])" <folder A> <folder B> X0,Y0,X1,Y1
python -c "import sys,csv;R=list(csv.DictReader(open(sys.argv[1])));F,M,G=map(float,sys.argv[2:5]);B=lambda r:[float(r[k]) for k in 'xywh'];X=lambda a,b,g:a[0]<b[0]+b[2]+g and b[0]<a[0]+a[2]+g and a[1]<b[1]+b[3]+g and b[1]<a[1]+a[3]+g;T=[r for r in R if r['kind']!='nogo'];N=[r for r in R if r['kind']=='nogo'];[print('FAIL size',r['name'],min(B(r)[2:])) for r in T if min(B(r)[2:])<(M if r['kind']=='minor' else F)];[print('FAIL no-go',r['name'],n['name']) for r in T for n in N if X(B(r),B(n),0)];[print('FAIL gap',r['name'],s['name']) for i,r in enumerate(T) for s in T[i+1:] if X(B(r),B(s),G)];print(len(T),'targets; biggest:',max(T,key=lambda r:B(r)[2]*B(r)[3])['name'])" targets.csv 150 96 27
```
The lag line (S-33), the reveal difference (S-44) and the hit-target check (S-49) are manual one-liners (no kit tool has these modes yet).

What each command needs, and how it gives a wrong number without an error:
- **`value`** (S-10, S-16, S-17). The grayscale view is the `<name>.luminance.png` it writes next to the input; for the phone-fit view run it on the `thumb` output (boxes scaled by f; without a box the verdict is `invalid-mask` but the luminance image is still written). `--compare-subjects` ranks by median luminance, so on a light panel read each `ratio_to_ring` as distance from 1 (a dark button on white is loud with a ratio below 1); the ring is shared, so run controls on different backgrounds (a close button over the sky) separately.
- **`contrast`** (S-18, S-22). p90 / p10 picks the lightest / darkest 10 % of the box, so a loose box around thin text samples the background: check the sampled hex is the text colour.
- **`palette`** (S-19, S-20). A small `--k` merges a small red area into a neighbour: use ≥ 8 and read the shares.
- **`thumb`** (S-23, S-28). Use the fit size, not the phone's full screen (667x375 overstates by about 18 %).
- **`silhouette`** (S-28). A soft glow round a keyed icon blends into the key and changes the area.
- **`clip_metrics.py` and the lag line** (S-33). The tool's background is the per-pixel median of all frames. Input: frames cropped to the control with a margin of about 15 % (the tool ignores the top-left 10 % × 7 % of every frame), named `f###_<ms>ms.jpg` with ms counted from the capture start (the name cannot hold a negative ms), with more idle frames before the press than changed frames after it (for example 13 idle up to and including the press frame, then 7), and the press frame's ms written down. Then run the lag line with the folder and the press ms: from the per-frame `coverage_pct` in `metrics.json` it prints the highest pre-press value, the cue frame (the first frame from the press on whose coverage rises above that value) and the lag (cue ms − press ms). The pre-press maximum must be 0. `summary.onset_ms` is never the lag: it is the first frame that reaches 10 % of the folder's peak, so when a bigger change follows inside the folder (the popup closing, the reveal starting, a Roblox prompt opening: in a Studio play-test the server often answers within the 7 frames) a small press cue is skipped and a 33 ms press reads as 167 ms. Wrong without an error: a control that stays changed (pressed, "Buying…", disabled) in more than half the frames makes the median the pressed look (the pre-press maximum rises above 0: re-capture with more idle frames); a control over a moving world (clouds, other players) puts motion in the crop margin and raises the pre-press maximum, which more idle frames cannot fix: crop inside the control's face, or capture it over a still backdrop; a press that changes the control by less than about 40 levels per channel gives `cue None`: that is UNVERIFIED, not PASS, and the idle and pressed stills side by side show whether the press look is too weak to see on a phone.
- **Reveal difference** (S-44). Per frame: the mean difference and the count of pixels that differ by more than 40 levels in a channel, inside one box: the reveal object's box covering its windup travel, the same box for both folders. Both folders start on the press frame (drop the frames before it), fixed camera, windup layers locked (no random start frames). First run it on two captures of the lowest tier: the noise floor is the largest mean and the largest count over the windup. Then run the lowest tier against each tier that adds a layer after the result (a tell on a middle tier alone passes a lowest-vs-highest check). Wrong without an error: a whole-frame or loose box dilutes a small tier tell (a 10 px gold glint on the egg moved the whole-frame mean by 0.01, inside the noise; in the egg's box it showed as about 140 changed pixels against 0); a noise pair misaligned by one frame, or with a moving camera, inflates the floor and hides real tells: a floor count far above 0 means fix the capture, never accept the floor.
- **Hit-target check** (S-49). `targets.csv` has one row per tap target (`name,kind,x,y,w,h`, kind `primary`, `frequent`, `minor` or `nogo`) in the screen frame's canvas px. The kind comes from how often the player uses the target (the flow sheet's How often column, screen-contract §7): a target used on most visits to the screen (buy, close, back, tabs, HUD buttons) is `frequent`; `minor` only for a rare control (info, a settings toggle, a switch set once a session), with that reason in the spec; the `nogo` rows are the parts of the frame's `no-go` layer (`ui-figma` F-24). Use the hit area's bounds (the separate hit frame when the art is smaller, screen-contract §5), from the Figma write results or `get_metadata`. Arguments: the minimum side for frequent (and primary) and for minor targets, and the gap, in canvas px for the declared rubric at the smallest phone's f (default Apple 44 / 28 pt at f 0.294: 150 and 96; gap PROPOSAL 8 pt: 27; screen-contract §5). It prints every FAIL and the biggest target, which must be the primary. Wrong without an error: Plugin API `x` / `y` are relative to the parent, so a button inside an auto-layout row needs its parents' offsets added (or read `absoluteBoundingBox` minus the frame's); a tappable card around its own button gives a false gap failure: list only what the player taps, never the containers.

**Flow and states** (input: `spec.md`, the flow sheet, the game designer's feature spec)
| ID | Pass when |
| --- | --- |
| S-01 | The decision record has one goal; every element on the wireframe has a row; Back / Close included |
| S-02 | Each element names one thing to understand and one action (or "status"); none with two jobs, none with no job |
| S-03 | Taps per task counted for every frequent task; frequent actions ≤ 2 taps from the HUD (PROPOSAL); each extra tap has a reason; no dead end |
| S-04 | Every screen, popup and state the flow reaches is listed (empty, error, loading, pending, disabled with its reason, cooldown, reward, purchase states) and matches the feature spec's list; a state seen later in a play-test capture is a finding |
| S-05 | HUD elements in core play counted; each maps to an item of the information list; stacks have capacity and overflow rules |
| S-06 | Core controls sit where the structure study found the genre puts them; each departure has a written reason |
| S-07 | A change to an existing screen names its pain point and where it was observed (capture id, analytics query, owner note) |

**Wireframe options** (input: one contact sheet at phone fit; Figma metadata)
| ID | Pass when |
| --- | --- |
| S-08 | 2-3 options whose block layouts differ (not only colour), one atypical, the first labelled warm-up; the pick has a reason tied to the decision; each rejection has a reason; no option polished before the pick |
| S-09 | Real content in the pick: longest name, biggest number (9 digits), real price format, longest locale; no text node clips |
| S-49 | On the phone layout frame (1920 × 1080 canvas; or the only frame), the hit-target check passes: every tap target's hit area meets the declared touch rubric (default frequent and primary ≥ 150 canvas px, minor ≥ 96 at f 0.294, each target's kind set by how often it is used: §6 note; screen-contract §5) with a gap between targets (PROPOSAL ≥ 27 px = 8 pt); the primary action is the biggest target; no tap target inside the no-go overlay (`ui-figma` F-24); a hit area larger than its art is its own frame. Input: Figma node bounds |

**Grey value pass** (input: the grey frame's screenshot at 1920, its luminance image at phone fit, `value --compare-subjects` numbers, Figma node bounds)
| ID | Pass when |
| --- | --- |
| S-10 | The first-noticed element in the phone-fit luminance image is rank 1; in `--compare-subjects` (a box per ranked control) rank 1 has the largest contrast to the ring, rank 2 the next |
| S-11 | Decoration and secondary elements sit closer to the ring than rank 1; dense information only where the decision is |
| S-12 | Each value or bar is nearer its owner than any other element (node gaps); gaps between groups are larger than gaps inside a group |
| S-13 | Critical state sits in the same zone on every screen of the feature, near the play focus, outside the no-go overlay (`ui-figma` F-24); the 1-second glance is done by a tester or the owner at the check-in |
| S-14 | Different priorities differ clearly in size (PROPOSAL ≥ 15 % on the larger side); same-priority siblings are identical |
| S-15 | Quiet areas between groups and calm room behind the title and the hero item at phone fit |

**Style** (input: Figma screenshots over the context backdrop; numbers for every state, images only for failures and key screens)
| ID | Pass when |
| --- | --- |
| S-16 | The styled screen's `--compare-subjects` ranking (same boxes) equals the grey pass ranking |
| S-17 | The brightest and most saturated element per screen region is its focal control; glow on the primary action only |
| S-18 | Every text class passes on its weakest backdrop (`contrast --rule wcag-text`, `wcag-large` for large text); outlined text passes both pairs: fill vs outline and outline vs background (screen-contract §5) |
| S-19 | `palette --roles` with the rule-sheet swatches: each role found within the tolerance (or MEASURED); with the controls that use the danger hue excluded, no cluster sits near the danger swatch; no hue has two meanings in the rule sheet |
| S-20 | Main, support and accent colours near 60 / 30 / 10 by cluster share (PROPOSAL), checked after the grey pass works |
| S-21 | Face gradients (token table numbers): ≥ 20 L\* between stops; the dark stop shifts toward a darker neighbouring hue and keeps its saturation (gold toward orange-brown, never grey); no stop is a black or white mix |
| S-22 | A badge, icon or label over a same-hue face keeps an edge: `contrast --rule wcag-nontext` (3:1) or a stroke |
| S-23 | `thumb --size <fit>`: every label, icon and state mark still reads; any detail that vanishes is removed or enlarged; key edges stay crisp (soft only on glows); no group of small high-contrast marks turns into a shimmering pattern |
| S-24 | The mirrored key screen shows no slanted row, lopsided margin or drift, and its dark and bright masses balance where the layout planned them |
| S-25 | Side by side with the target image and 2-3 approved UI anchors at the same size; the gaps (depth, shine, material, spacing, type) listed and closed or reported |
| S-26 | Each new component names its rule-sheet rule; corner types and button shapes follow the shape vocabulary; text from the ladder |
| S-27 | Ornaments use the game's own motif (from its icons or story) at more than one scale, off the decision path; with the ornament layer hidden, S-10's ranking is unchanged |
| S-28 | Each icon's meaning is written; the keyed icon's `silhouette` reads and `thumb --size 48x48` still says the meaning; two icons of different meaning with an aligned IoU at or above the flag (PROPOSAL 0.85) are look-alikes; the game's motif reads as a one-colour icon; a reaction or emote icon's intent is named in about 2 s at real size by a tester or the owner at the check-in |
| S-29 | Rarity and premium tiers are named in text and frame shape and stay distinct in the luminance image; the top tier has separable finishes |
| S-30 | On a studio-operator capture of the busiest moment at phone resolution (through the lead): no effect covers the HUD or the critical zone; the HUD does not cover the play focus, targets, the shop or placement areas |

**Motion and feedback** (input: motion records, the motion table, the Figma prototype, frame folders from Studio or Figma video, the owner at a playable preview)
| ID | Pass when |
| --- | --- |
| S-31 | Each event's end frame, sound off, says what happened (label, icon, colour) |
| S-32 | Every animated element uses a motion-table row (its value bracketed or decided); one element type, one set of values; eased, never linear, for anything that travels; exits ≤ entrances; the first visible change inside the table's instant anchor; an overshoot crosses its target once |
| S-33 | `clip_metrics.py`, then the lag line, on a press folder captured by the rules above: the pre-press maximum is 0, and the lag ≤ 67 ms at 30 fps (the press frame or the next, plus one frame of capture jitter; PROPOSAL), the same on every button; `cue None` is UNVERIFIED; `summary.onset_ms` is never the lag |
| S-34 | At most one element per screen state moves to draw attention, and it is the next action; other players' events never take it |
| S-35 | Each enter and exit names its start and end anchor; the first still is at the source, the last at the destination |
| S-36 | The motion material comes from the rule sheet; the owner names it at the playable preview |
| S-37 | The success layer starts only on confirmation; pending shows after about 100 ms; a rejected-request capture (or the prototype's failure branch) shows no success |
| S-38 | Each refusal states cause and fix at the control in text and icon, reads in the luminance image; only the control shakes; its sound plays at most about once per 0.5 s when spammed |
| S-39 | Affordability uses the true balance at once (buy right after a gain); the count-up stays inside its motion-table cap; the final number is exact; every shown number matches the progression designer's display fixtures; gains signed, spends neutral; no sound per digit |
| S-40 | Same-kind events inside the merge window share one label and one sound; a 20-per-second burst piles up nothing; toasts ≤ 3 stacked, outside the play focus |
| S-41 | Each looping pulse sits in its rate class (motion.md §8); nothing above 3 Hz at full contrast; timers follow the server value |
| S-42 | Every intense channel has a reduced variant; the reduced end still keeps every piece of information |
| S-43 | Each celebration has a beginning, middle and end; its size and length follow its tier; the build rises; a pop reaches most of its size fast and eases out; the peak follows its cause; the gaps between beats are not all equal; in play it ends in under about 2 s |
| S-44 | Paid reveal: in the reveal object's box, the lowest tier against every tier that adds a layer after the result (one folder per tier; numbers only, an image only for a failing frame): every windup frame stays at or under the noise floor (mean and changed-pixel count) up to the result frame (reveal difference above); no higher-tier layer on a lower result; odds visible before the buy button |
| S-45 | Every state change has a picture cue and a sound cue, or a written reason; nothing means something by sound only |

**Hand-back**
| ID | Pass when |
| --- | --- |
| S-46 | Every check carries its input and label; a could-not-check list names the step, the missing input and the capture that would close it |
| S-47 | One named weakness with its next step, or the reason there is none |
| S-48 | The stop criteria in `spec.md` each show passing; the image count is inside the budget (§5) |

## 7. My review slot (another maker's build against my target image)
In the UI screen recipe I review the built screen after the code and QA checks. I ask the lead before the slot for the studio-operator's captures: Device Simulator stills at the smallest supported phone and a PC size for every state; one integrated capture over the busiest moment; a frame folder of each press and key transition by the S-33 capture rules (§6: cropped to the control with a margin, or inside its face when the world moves behind it; more idle frames before the press than after it; the press frame's ms noted); for a paid reveal, one capture per tier (the lowest and every tier that adds a layer after the result) plus a second capture of the lowest tier, each starting on the press frame; a rejected-request capture; the same screen with reduced motion on and with the largest text size. Then §1 checks 01-25 and §6 S-16 to S-45 on those inputs, side by side with the target image. Findings follow `rules/messages.md` §6 (blocking, recommendation, new request) with the failed check id, the evidence and the fix; a visual gap comes with a marked capture (boxes and short notes drawn on the screenshot, before and after when a fix is proposed). Return paths: a read-order failure goes back to the grey value pass; a state failure to the state map; only a style gap goes to styling. I never edit the work under review.
