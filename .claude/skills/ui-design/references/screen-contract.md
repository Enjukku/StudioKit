---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; research paper RP via knowledge/reference/ui/05b-research-templates.md (T01-T04), 06a (RB-*), 06b (step 3 states)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Screen contract: what to write before drawing

All templates are the paper's proposals (O) unless a row says V. Copy the tables into `content/ui/<screen-id>/spec.md` and fill them.

## 1. Decision record (T01)
| Field | Fill with |
| --- | --- |
| Goal | what the player is trying to do right now |
| Info needed | what they must know before choosing (price, stats, owned?, odds) |
| Actions | every choice, including Back / Close |
| Consequence | what each action does, including cost |
| Proof it registered | what changes on screen when the action is accepted, and when it is confirmed |
| Recovery | back, cancel, retry or undo route, and where focus lands |
Reject any component with no role here. Decoration stays only with a stated narrative role that does not compete (RA-57).

## 2. Attention inventory (T02) and HUD contract (T03)
Per visible element: priority (semantic) · persistence · contrast on its real background · rendered size · space around it · motion · sound. Then check salience against priority with three captures: **grayscale**, **reduced size** (phone), **normal moving** (RA-58, RA-59).

HUD facts: **actionable now** (stays findable while the action is possible) · **planning** (stable secondary region) · **on demand** (detail view). For any stack of statuses, buffs, toasts or quests write: priority order, capacity, what replaces what, overflow rule (H07; Destiny had > 2,000 possible buffs for 4 slots, V U05).

## 3. State list (RP step 3) and screen contract (T04)
States every screen spec lists (write "n/a" with a reason when one cannot happen): entry · normal · empty · max content · loading · pending · error · not enough currency · not eligible · success · recovery. Per item: selected · equipped · owned · claimed · locked · new. Per control: idle · focused (gamepad / hover) · pressed · pending · disabled-with-reason · cooldown.

| Question | Spec field | Review evidence |
| --- | --- | --- |
| Current decision? | goal + next meaningful action | unprompted attempt |
| What must stay visible? | essential state, priority, persistence | busy gameplay recording |
| What can wait? | on-demand detail + its route | compare / inspect task |
| What wins when signals clash? | capacity, replacement, overflow | maximum simultaneous case |
| How is change understood? | trigger, acknowledgement, pending, result | recorded transition + final state |
| How to recover? | back / cancel / retry / undo | failure + interruption route |

## 4. Focus map (RA-53..55, V XAG 112-113 + O)
Per screen: initial focus · traversal order (rows, columns, wrap yes/no) · Back target · what a modal traps · where focus returns on close · gamepad hint glyphs. Mixed input keeps the logical selection when the visual cue changes. Test launch → play → exit with no pointer.

## 5. On-device size math (PROPOSAL arithmetic from V rubrics)
The tutorials design on a **1920 × 1080** canvas (TC, TS, TP). Builders fit each screen with one outer `UIScale` (ui-basics U-02), and interactive UI lives in a `CoreUISafeInsets` ScreenGui (U-01), which is shorter than the screen by Roblox's top bar.

**Fit rule (engineering recommendation, J002):** `f = min(safe width ÷ 1920, safe height ÷ 1080)`, where "safe" is the CoreUISafeInsets area (`GuiService:GetInsetArea`, or that ScreenGui's AbsoluteSize). Then `device size (pt) ≈ canvas px × f`.
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
- Fix by bigger art on the phone layout (style-query variant `@ViewportDisplaySizeSmall`, ui-basics U-05) or by a hit area larger than the art (an invisible button around it; Android allows a 24 dp icon inside a 48 dp target, V P03). Gaps between targets count too. Write which in the spec.
- Xbox game guidance (15 mm phone ≈ 96 pt) is stricter; use it only if the project picks that rubric. **Declare one rubric** (D-05); default PROPOSAL = Apple 44 / 28 pt on the smallest supported phone.
- Thin details vanish: 3 px ≈ 0.9 pt. Lines meant to read as "thick" or that carry meaning (focus, selection, rarity) need ≥ 5 canvas px (≈ 1.5 pt); depth lips ≥ 8 px. A silhouette edge that is only an edge (anime) may be thinner (e.g. 4 px).

**Text.** Default project rubric (PROPOSAL until the owner decides; source: Apple HIG minimum text size 11 pt, practice, not in RP): essential reading text ≥ **11 pt font size** on the smallest phone (≥ 38 canvas px at f 0.294); short non-essential labels ≥ 9 pt (≥ 31 px). XAG's measured-glyph targets (V U12): console 26 px at 1080p; PC 18 px at 1080p; mobile 18 px at 100 DPI, 36 at 200, 72 at 400 (the same ≈ 4.6 mm ≈ 29 pt glyph height ≈ 99 canvas px at f 0.294): a stretch target for critical numbers (health, timers), owner decision. Support 200 % scaling (U12).

**Contrast** (V U13): 4.5:1 normal, 3:1 large or inactive, 7:1 high-contrast; sample the weakest background. **Outlined text** (the cartoon / stud signature), PROPOSAL reading of RB-06 / RB-08: it passes when the outline vs the background behind it ≥ 4.5:1 **and** the fill vs the outline ≥ 4.5:1, with the outline ≥ 2 device px; fill vs background alone may be lower. Measure both and write both in the spec.

## 6. Text container spec (RB-25..27, O)
Per text field: source (live data or fixed copy) · max length tested · wrap or one line · grow direction · truncation allowed? (never for item name, price, odds, eligibility, consequence; RB-26) · min size · locale test (longest real translation; short strings can grow most, e.g. a ratio of 3, V U21).
