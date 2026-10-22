---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J002; research paper RP via knowledge/reference/ui/05b-research-templates.md (T01-T04), 06a (RB-*), 06b (step 3 states); J018 (flow sheet, inputs from the game designer)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Revised by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (one job per element, read rank and fixed zones, refusal fields, §7 flow sheet, §8 inputs from the game designer).

# Screen contract: what to write before drawing

All templates are the paper's proposals (O) unless a row says V. Copy the tables into `content/ui/<screen-id>/spec.md` and fill them.

## 1. Decision record (T01)
| Field | Fill with |
| --- | --- |
| Goal | what the player is trying to do right now (one goal per screen) |
| Info needed | what they must know before choosing (price, stats, owned?, odds) |
| Actions | every choice, including Back / Close |
| Consequence | what each action does, including cost |
| Proof it registered | what changes on screen when the action is accepted (attempt cue), and when it is confirmed (outcome) |
| Recovery | back, cancel, retry or undo route, and where focus lands |
Reject any component with no role here. Decoration stays only with a stated narrative role that does not compete (RA-57).

## 2. Attention inventory (T02) and HUD contract (T03)
Per visible element: **its one job** (the one thing the player understands from it and the one action it leads to, or "status") · read rank (1st, 2nd, 3rd; from the game designer's read rank when the screen is in play) · persistence · zone (from the rule sheet's screen zones) · contrast on its real background · rendered size · space around it · motion · sound. An element with two jobs is split; one with none is cut. Then check salience against rank with three captures: **grayscale** (the luminance image), **phone fit**, **normal moving** (RA-58, RA-59). Rank 1 wins by being different (value, size, colour, isolation, motion); lower the rest before raising rank 1.

HUD facts: **actionable now** (stays findable while the action is possible) · **planning** (stable secondary region) · **on demand** (detail view). Critical state (health, ability ready, objective, timer) has a fixed zone that is the same on every screen, near the play focus, outside the thumb and Roblox zones; a value sits next to the thing it describes (a bar beside a name reads as that thing's bar). How much HUD a game carries comes from its genre and the information list: card, tycoon and simulator games plan many screens; obby and story games keep the HUD minimal; on phones every extra element covers the play view. For any stack of statuses, buffs, toasts or quests write: priority order, capacity, what replaces what, overflow rule (H07; Destiny had > 2,000 possible buffs for 4 slots, V U05).

## 3. State list (RP step 3) and screen contract (T04)
States every screen spec lists (write "n/a" with a reason when one cannot happen): entry · normal · empty · max content · loading · pending · error · not enough currency · not eligible · cooldown · success · recovery. Per item: selected · equipped · owned · claimed · locked · new. Per control: idle · focused (gamepad / hover) · pressed · pending · disabled-with-reason · cooldown · refused. List every screen and popup the feature reaches (including in-world BillboardGui and SurfaceGui parts) before designing any of them.

Per refusal or disabled state: the cause in words ("Need 40 more coins", "Unlocks at level 5", "Backpack full") · the fix or unlock route · the icon · where the message sits (at the pressed control) · its sound (rate-limited) · how long it stays (PROPOSAL ≥ 2 s or until the next tap; motion.md §8).

| Question | Spec field | Review evidence |
| --- | --- | --- |
| Current decision? | goal + next meaningful action | unprompted attempt |
| What must stay visible? | essential state, priority, persistence, fixed zone | busy gameplay capture |
| What can wait? | on-demand detail + its route | compare / inspect task |
| What wins when signals clash? | capacity, replacement, overflow | maximum simultaneous case |
| How is change understood? | trigger, attempt cue, pending, confirmed result | frame folder + final state |
| How to recover? | back / cancel / retry / undo | failure + interruption route |

## 4. Focus map (RA-53..55, V XAG 112-113 + O)
Per screen: initial focus · traversal order (rows, columns, wrap yes/no) · Back target · what a modal traps · where focus returns on close · gamepad hint glyphs. Mixed input keeps the logical selection when the visual cue changes. Test launch → play → exit with no pointer.

## 5. On-device size math (PROPOSAL arithmetic from V rubrics)
The tutorials design on a **1920 × 1080** canvas (TC, TS, TP). Builders fit each screen with one outer `UIScale` (ui-basics U-02), and interactive UI lives in a `CoreUISafeInsets` ScreenGui (U-01), which is shorter than the screen by Roblox's top bar.

**Fit rule (engineering recommendation, J002):** `f = min(safe width ÷ 1920, safe height ÷ 1080)`, where "safe" is the CoreUISafeInsets area (`GuiService:GetInsetArea`, or that ScreenGui's AbsoluteSize). Then `device size (pt) ≈ canvas px × f`. The **phone-fit view** for reviews is the canvas resampled to 1920·f × 1080·f (565 × 318 at f 0.294): `look_check.py thumb --size 565x318` (`review.md` §6).
- Top-bar height T: **PROPOSAL 58 pt, UNVERIFIED** (not in the docs mirror); measure `GuiService.TopbarInset` in the Device Simulator for the smallest supported phone and replace it.
- Assumption: one Roblox GUI unit on a phone ≈ 1 iOS pt / Android dp. Check once: a frame's `AbsoluteSize` in the Device Simulator vs the device's pt size.
- A different fit (full height with a reserved top band, width caps) is allowed; redo the table with that rule and say so in the spec.

| Smallest target (landscape) | Screen (pt / dp) | Safe h = h − T | f | 44 pt (Apple frequent) | 28 pt (Apple minor) | 48 dp (Android) | 11 pt text |
| --- | --- | --- | --- | --- | --- | --- | --- |
| small iPhone | 667 × 375 | 317 | **0.294** (height-bound) | **150 canvas px** | 96 px | — | 38 px |
| small Android | 640 × 360 | 302 | **0.280** (height-bound) | — | — | **172 px** | 40 px |
| 4:3 iPad | 1024 × 768 | 710 | 0.533 (width-bound) | 83 px | 53 px | — | 21 px |
| iPad Air | 1180 × 820 | 762 | 0.615 (width-bound) | 72 px | 46 px | — | 18 px |
The phone row decides sizes; tablets only need checks for layout (width-bound fits leave empty bands top and bottom).

Consequences:
- TS side buttons start at 70 × 70 and are scaled up ≈ 1.4× (≈ 98 px, inferred from the stroke going 5 → 7, TS@41:08-41:46): ≈ 29 pt on a small iPhone, which passes Apple's 28 pt minor line and fails 44 pt for a frequent control. The G2 egg-shop Buy (128 px) is ≈ 38 pt: fails 44.
- Fix by bigger art on the phone layout (style-query variant `@ViewportDisplaySizeSmall`, ui-basics U-05) or by a hit area larger than the art (an invisible button around it; Android allows a 24 dp icon inside a 48 dp target, V P03). Gaps between targets count too. Write which in the spec. The primary action is the biggest target on its screen. Measured on the wireframe and the styled frame by `review.md` §6 S-49 (hit-target check from Figma node bounds).
- Xbox game guidance (15 mm phone ≈ 96 pt) is stricter; use it only if the project picks that rubric. **Declare one rubric** (D-05); default PROPOSAL = Apple 44 / 28 pt on the smallest supported phone.
- Thin details vanish: 3 px ≈ 0.9 pt. Lines meant to read as "thick" or that carry meaning (focus, selection, rarity) need ≥ 5 canvas px (≈ 1.5 pt); depth lips ≥ 8 px. A silhouette edge that is only an edge (anime) may be thinner (e.g. 4 px).

**Text.** Default project rubric (PROPOSAL until the owner decides; source: Apple HIG minimum text size 11 pt, practice, not in RP): essential reading text ≥ **11 pt font size** on the smallest phone (≥ 38 canvas px at f 0.294); short non-essential labels ≥ 9 pt (≥ 31 px). XAG's measured-glyph targets (V U12): console 26 px at 1080p; PC 18 px at 1080p; mobile 18 px at 100 DPI, 36 at 200, 72 at 400 (the same ≈ 4.6 mm ≈ 29 pt glyph height ≈ 99 canvas px at f 0.294): a stretch target for critical numbers (health, timers), owner decision. Support 200 % scaling (U12).

**Contrast** (V U13): 4.5:1 normal, 3:1 large or inactive, 7:1 high-contrast; sample the weakest background (the brightest and busiest backdrop the screen can sit over). Critical non-text marks (focus ring, danger edge, objective marker) ≥ 3:1 against their local background. **Outlined text** (the cartoon / stud signature), PROPOSAL reading of RB-06 / RB-08: it passes when the outline vs the background behind it ≥ 4.5:1 **and** the fill vs the outline ≥ 4.5:1, with the outline ≥ 2 device px; fill vs background alone may be lower. Measure both with `look_check.py contrast` (`review.md` §6 S-18) and write both in the spec. **Translucent panels:** the player's Background Transparency setting (`GuiService.PreferredTransparency`, 0 = fully opaque) is multiplied into `BackgroundTransparency` (`production/publishing/accessibility.md:104-129`); measure contrast at the default (most transparent) value, which is the weakest case.

## 6. Text container spec (RB-25..27, O)
Per text field: source (live data or fixed copy) · max length tested · wrap or one line · grow direction · truncation allowed? (never for item name, price, odds, eligibility, consequence; RB-26) · min size · locale test (longest real translation; short strings can grow most, e.g. a ratio of 3, V U21).

## 7. Flow sheet (before any styling)
One row per task the screen serves; count from the screen the player is on when the need arises (usually the HUD).
| Task | How often | Entry point | Steps (each tap or press) | Taps | Exit and where focus lands | Extra taps and why |
| --- | --- | --- | --- | --- | --- | --- |
| hatch the next egg | every session, many times | HUD Eggs button | Eggs (popup opens on the nearest egg) → Hatch | 2 | the reveal, then the popup with the new pet marked | none |
| sell all common pets | a few times a session | inventory | Sell all → confirm | 2 | the inventory, sold pets gone, coins bumped | the confirm: a destructive action |

The How often column also sets each tap target's touch kind (frequent or minor: `review.md` §6 S-49 note). PROPOSAL default: frequent actions (equip, buy, claim) within 2 taps of the HUD, plus Roblox's own prompt where one is required. Every extra tap has a reason (a review step before a paid random item, a confirm before a destructive action). Contextual controls appear only when they are useful (swap Sprint for Pass when the player holds the ball). A flow change after the wireframe gate is a change request with its reason, not a silent edit.

## 8. What I take from the game designer (before the flow)
The feature spec carries sheets I build from; I do not rewrite them, I cite their revision in `built_on` (`preproduction/references/documents.md`):
| Sheet (feature spec) | What I use it for |
| --- | --- |
| §9 Read rank and information list | the read rank for the attention inventory; the information per moment with where it lives and how fast it must read (critical about 1 s, PROPOSAL); the reserved signals; the screens and states list I check S-04 against |
| §6 Feedback stack | the named stages (the same names the animator's markers, VFX frame scripts and sound cue cards use), the attempt cue and outcome response per channel (my UI row of each), outcome tiers, failure and refusal causes, celebration tier and length, frequency and merge window, counters (true value, count-up length) and comfort variants |
| §7 Threat and hazard sheets | which threats and timers the HUD must show, with their windows and danger areas (a HUD marker of a danger area follows the same data, never my own size) |
| Decision the screen serves | the goal in my decision record; prices and odds come from the progression designer and `platform-policy` |

When a sheet is missing or `TBD`, I ask the game designer (a ticket or an exchange note) and mark the assumption; I never invent a gameplay rule, a window or a price to complete my spec. When my UI cue keys from a character action (a hit marker, a cooldown ready), I take the event name and time from the animator's timing list, never my own frame list.
