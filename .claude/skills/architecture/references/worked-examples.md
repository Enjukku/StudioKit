> Author: J018 maker architect · claude-opus-5-5 · high · 2026-10-22. Part of `architecture`: built also from the owner's Riot transcripts (J018); repair rounds 1 and 2 after the stage 3 reviews. Every name and number here is an example of the method, not a decision; PROPOSAL values are starting values a check may change.

# Worked examples

Each example shows the decisions, the presentation contract rows that matter, and what a plan without them got wrong. Row columns are shortened; a real contract fills every field of `presentation-contract.md` §2.

## A. Melee swing in a third-person brawler (12 players per server, phones first)
**Parameters:** third-person camera, touch first, 12 players, 3-minute rounds, streaming on. Target experience: "hits feel heavy and fair". Inputs: feature spec F-04 v2 (feedback stack: attempt, miss, blocked, hit, big hit), timing list `timing-swing.json` rev 3, VFX read card `slash-impact` rev 1, cue table rev 4.
**Decisions:**
- The server owns hits (R-02, `networking-security` N-03): `Combat.Swing` (client → server, rate-limited) → `CombatService` checks range, cooldown and line of sight → `Combat.HitResolved {requestId, attacker, target, outcome, tier, cause, position}` to clients in range.
- The swing clip starts on the owning client, so it replicates (`Animator.yaml:217-232`); the trail starts on its marker. Whether `contact_candidate` fires on an observing client for another player's track is not stated in the docs: a probe settles it before the contract relies on it (spike, §3 step 5). If it does not fire there, the bystander's small contact tick keys from `HitResolved` instead.
- Hit-stop runs only on the attacker's and the target's clients: both characters' tracks pause for the tier's length (the game value from the feature spec), and one owner per track sets the base speed back when the stop ends or on death, so two fast hits never leave a track frozen; bystanders see none; the server keeps running. The spec allows no prediction for hits, so the stop starts one round trip after the contact pose: the animator agrees a short hold of the contact pose, checked with a 150 ms server delay (seed "Hit-stop"). Whether a pause of a track replicated from another client holds, and whether the owner's own pause replicates, is the third probe in `presentation-contract.md` §5, run in the same spike.
| Row | Layer | Source | Runs on | Per viewer | Comfort | Information |
| --- | --- | --- | --- | --- | --- | --- |
| P-1 | attempt: swing whoosh + trail | input, then `swing_accel` marker | client | all see the trail; only self hears the whoosh at full level | none intense | motion + sound |
| P-2 | outcome hit / big hit: spark, hit sound, hit-stop | `HitResolved{done, tier}` | client | self and target full; bystanders toned spark, no hit-stop on their screen | big hit shake for self only, off in comfort | spark shape + sound + target reaction pose |
| P-3 | outcome blocked: clink, "blocked" icon | `HitResolved{done, blocked}` | client | self and target | none | icon + distinct sound |
| P-4 | outcome miss: no spark, short whiff | `HitResolved{done, miss}` | client | self only | none | absence of spark + whiff |
| P-5 | refusal: swing on cooldown | `denied{cooldown}`; the client checks the same cooldown rule before the press | client | self only | none | cooldown ring on the button + no swing |
| P-6 | cleanup: trail and loops cleared | `cleanup` marker, unequip, death | client | all | none | — |
**What the old plan missed:** it played the hit spark on `contact_candidate` (a hit shown for a miss), shook every client's camera on every hit, and hard-coded a 0.18 s delay for the sound.
**Checks:** AR-07 (P-2 starts from the result), AR-08 (marker names match rev 3), AR-09 (bystander camera), RV-01 rejected-swing capture, RV-02 two-client capture, RV-08 overlap test.

## B. Coin pickup with a magnet in a simulator (up to 20 pickups per second)
**Parameters:** high follow camera, phones, 30 players, sessions of about 10 minutes. Feedback stack: pickup tick, "+N" label, counter bump; merge window PROPOSAL about 100 ms (`game-design/references/principles.md` §7).
**Decisions:**
- The server owns the balance (award request with an id, `data-saving` D-11); the client never predicts a balance.
- `PickupPresenter` (client) owns the merge window, one label per window, the live-copy cap and the pool; callers never spawn bursts themselves (R-24).
- The counter shows the true value as soon as `Wallet.Changed` arrives; the count-up is decoration; the buy button checks the true balance (R-21).
| Row | Layer | Source | Rate | Truth | Information |
| --- | --- | --- | --- | --- | --- |
| P-1 | attempt: coin flies toward the player | magnet enters range (client) | up to 20 per second; pooled, cap per VFX read card | coin positions from the server's drop list | motion |
| P-2 | outcome: tick, "+N" label, counter bump | `Wallet.Changed{delta, requestIds}` | merged per window: one tick, one label | the server balance | number + sound |
| P-3 | big haul (merge total over a threshold) | same, threshold from the feature spec | at most one per window | the merged total | bigger label + chime |
**What the old plan missed:** 20 bursts and 20 labels per second, a sound per coin, a count-up that lagged the balance so the shop said "can't afford" for half a second.
**Checks:** AR-12, AR-14, RV-09 real-rate and burst test (final counter exact), RV-05 screen for asset ids in the presenter.

## C. Boss ground slam (a threat the player must dodge)
**Parameters:** third-person, 8 players, boss arena. Threat sheet: reaction window, two-channel tell, danger area as tuning keys `BossConfig.slam.radius` and `.fuse`.
**Decisions:**
- One truth source: the server rule and the ring both read `BossConfig.slam`; the countdown follows the replicated server timer (`slamAt`), never a client guess (R-21).
- The tell plays for everyone at full strength because every player in range is threatened; the impact shake is the local player's own top-tier event only when it is inside the radius.
- Reduced flashes turns the fuse blink into a steady glow with a fill countdown; the ring stays (R-22).
| Row | Layer | Source | Per viewer | Comfort | Truth |
| --- | --- | --- | --- | --- | --- |
| P-1 | tell: windup pose, ring, rising sound | `Boss.SlamWarned{slamAt, position}` | full for everyone in range | blink → steady glow + fill | radius, fuse from `BossConfig.slam` |
| P-2 | outcome: impact burst, dust, sound | `Boss.SlamLanded{hitPlayers}` | hit players: big layer + shake; others: burst, no shake | shake off → weight in sound and pose | ring removed on this event |
| P-3 | aftermath: scorch decal | `SlamLanded` | all | none | never larger than the radius |
**What the old plan missed:** the VFX ring was sized by eye 20 % larger than the hit area, and the client started its own fuse timer, so the blow drifted from the real one.
**Checks:** AR-11, AR-10, the truth-overlay seed (vfx-designer), RV-04 grayscale + reduced capture.

## D. Shop purchase that is refused
**Parameters:** shop screen, phones. Feedback stack: press sink at once; pending state when slow; success burst only on a confirmed purchase; refusal at the control with cause and fix.
**Decisions:**
- `PurchaseService.requestPurchase` returns `done`, `denied(reason)` or `unavailable` (R-13); reason codes (`need_gold`, `level_locked`, `sold_out`) carry the numbers the UI needs (`{need = 40}`).
- The UI shows the press feedback before any reply; the coin burst and chime play only on `done`; `unavailable` shows "try again" with no charge.
| Row | Layer | Source | Information |
| --- | --- | --- | --- |
| P-1 | attempt: button sinks, click | input | motion + sound |
| P-2 | pending: spinner on the button | no reply after the pending threshold (feature spec) | icon |
| P-3 | outcome: burst, chime, item in inventory | `done` | text + sound + item |
| P-4 | refusal: "Need 40 more gold" at the button, soft rate-limited thud | `denied(need_gold, {need = 40})` | text + icon + sound |
**What the old plan missed:** a denial with no reason, so the UI could only flash red; the burst played on the press and "un-played" on refusal.
**Checks:** AR-07, AR-16, RV-01.
