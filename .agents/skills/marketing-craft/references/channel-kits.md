# Channel kits: the work for each surface

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-craft`. The facts and limits behind each step are in `marketing-design/references/discovery-promise.md` (page, video, images) and `channels.md` (video, creators, ads, events, community), with fact-check ids and read dates. Re-read the live page on the day; a value seen only in a logged-in form is "owner to confirm".

## 1. Game page
| Item | Work | Check |
| --- | --- | --- |
| Title | `templates/marketing/title-checklist.md` | T1-T12 |
| Description | first sentence = what the player does and why it is fun; then the loop, then what is new; relevant words used naturally, never repeated lists; genre matches | a new reader says the action back from the first sentence |
| Icon, thumbnails | `image-pipeline.md` | checklist + sheet per image |
| Gallery (up to 10 images or videos) | core action first, then social moment, then progression payoff, then secondary features; each item a claim id | order recorded with ids |
| Native video | §2 | |
| Badges, events | only rewards that exist; a real event or return reason | promise ledger |
| Eligibility | devices (native video not on Xbox, PlayStation, VR), age rating, regions | recorded |

## 2. Native gameplay video (Roblox page and Home RFY)
1. Capture from the shipping build: the signature moment within the first seconds, real controls, real UI.
2. Allowed: real-gameplay camera work, a logo, in-game UI text, sparse factual text, catalog music without lyrics. Not allowed: outside footage, narration, voice-chat audio, lyrical music. No cinematic trailer (FD-34, FD-48).
3. Check the live upload page for length, size and format on the day (the paper could not establish them, OQ-09). 3 free uploads a month; a rejection still uses one (FD-31..32).
4. Upload and approval = owner action. Afterwards, check a live page: is it shown, where.
5. Read with the Acquisition / Engagement / Retention video annotations; label "observational".

## 3. Short video (Shorts, TikTok, Reels)
`templates/marketing/short-video-plan.md` per edit. Work order: hook from a real moment → payoff timestamp → shot list → captions (muted review) → sound and music license → platform edit → disclosure if any → share link per platform. Variants differ in one thing. Measurement names each platform's view definition (YouTube public view = first frame since 2026-08-24; engaged views separate, FS-09, FS-11). Posting and channel accounts = owner.

## 4. Update announcements, events, notifications
| Kind | Draft | Limits to check (V) |
| --- | --- | --- |
| Update announcement | ≤ 60 characters, names the real new thing, points to it | once per 3 days; opted-in players (FD-55..56) |
| Event | title, real start and end in the game's time zone, what players do, spawn path checked, thumbnail through the image pipeline | up to 10 ongoing or upcoming; Trending needs ≥ 1,000 RSVPs and a start within 7 days, public (FD-53..54) |
| Off-platform featuring request | the event, art per the live form; submit with a 14-day studio buffer (docs say 7) | not automatic, no feedback (FD-57..58) |
| Personalized notification | one string per variant, `category` set; no urgent or pushy wording; PolicyService-gated content only for eligible players | 13+ only; one per user per day per experience; delivery not guaranteed; 100 impressions before stats (FD-61..64) |
Posting, scheduling and sending = owner (or a tool the owner runs). The live-ops designer's calendar is the source of dates (handoffs §5).

## 5. Creator brief and outreach package
Write, never send. Fields (CR-01..08): the real promise and claim ids, target language / region / platform, why this creator (recent relevant videos, median views on comparable recent videos, audience geography), deliverables and dates, disclosure wording per platform (YouTube paid-promotion setting, TikTok commercial content setting, visible and audible in video, FS-12..14, FS-20, FS-32..33), allowed edits, usage and paid-amplification rights (tagging a brand partner on TikTok can grant ad authorization, FS-21), approval limits, measurement access (aggregate only), one share link, a bounded first deliverable, "honest reactions welcome". Minor creators: flag for the owner's legal review and an authorized adult. Fee: "written quote requested", split into production, licensing, paid amplification, agency, performance; never a guessed rate.

## 6. Roblox ads test plan
| Field | Content |
| --- | --- |
| objective | Plays (acquisition test) / Earnings (if eligible, monetization) / Engagement (beta, its own purpose only) |
| audience and targeting | All / New / Recent (≥ 10,000 players) / Lapsed (≥ 20,000 players); targeting within audience eligibility; no personalization to under-18 (FA-04..05, FA-33) |
| creatives | 16:9 images through the image pipeline; count per the live form (10 vs 25 conflict, FA-10); no fake UI, free-Robux bait or urging children to buy (FA-35, FA-37) |
| spend | budget options only (for example three sizes with what each could show and could not), total loss ceiling, duration, currency, funding; auto-reload off; no minimum asserted (FA-23) |
| measurement | analyst spec; attribution windows from the docs (FA-06); 48 h reporting delay (FA-13); label "attributed"; holdout if available; two ledgers |
| fixed after publish | payment method, goal, audience, budget type (FA-61, FA-63) |
| pause owner | named, with triggers (spend anomaly, misleading creative, moderation failure, player harm) |
All account actions (account, card, Robux conversion, publish, pause, Open Cloud key) = owner (`policy-rights.md` §6).

## 7. Community plan
Channels (few), rules, human escalation owner, AutoMod setup to test in each language (coverage unconfirmed, FS-39..41), anti-scam notice, incident log, feedback form fields (bug, category; never personal data), the in-game route for every essential. No data flow between Roblox and Discord ships without its own policy and privacy review (FA-55..57). Server creation and moderation staffing = owner.

## 7b. Ad integrations (brand deals, own merch)
Only with the owner's deal in hand: register in Ads Manager with invoicing, submit assets 5 business days ahead, `GetCampaignEligibilityAsync` gating built by the feature builder (ticket), "Ad" labels per format, fallback for ineligible players; one rejected asset voids the campaign (FA-39..43). Pricing for campaigns from 2027-01-01 is a platform charge (FA-44..48).

## 8. The owner package
One file `knowledge/jobs/<job>/marketing/package-<date>.md`:
1. The promise line and its proof (captures, claim ids).
2. Recommended assets per surface + rejected candidates with one-line reasons; sheets and checklists linked.
3. Channel plan: what, where, when, why this channel.
4. Tests: spec, method label, earliest read date.
5. Budget options (if any), each with loss ceiling and what it can and cannot show; default: no spend.
6. Release-gate table (seven items) with evidence and an empty decision-id column.
7. Owner actions list, in order.
8. Rollback: the current live assets and how to restore them.
9. Open questions with a recommendation and a default.
