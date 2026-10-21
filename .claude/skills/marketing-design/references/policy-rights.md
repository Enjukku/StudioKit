# Truth, platform rules, younger players, rights, owner gate

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-design`. Sources: `knowledge/reference/marketing/03-...md` §3-4, §7 (PO, RG, DN ids); `02-...md` §5 (CM); fact-checks `fact-check-roblox-ads-policy.md` (FA ids) and `fact-check-roblox-discovery.md` (FD), read 2026-10-21. The base rules live in `platform-policy` (load it for anything players buy, roll, trade or watch, and for ads); this file adds what marketing needs. Rules change: re-read the cited page on the day you rely on it, and write the date.

## 1. Truth (the first rule)
- **One promise everywhere.** Title, description, icon, thumbnails, native video, social edits, announcements and the first playable session promise the same achievable thing (PO-22). Each marketed claim has a promise-ledger row: the feature, the build where it works, where players meet it, the capture (`game-concept/references/hook-promise.md` §2).
- Never market a future feature as live; never imply official sponsorship or a partnership without permission (PO-22).
- Roblox treats misleading, mismatched, reward-led or too-similar metadata as a discoverability problem (FA-52, FA-60, FD-11). A thumbnail that over-promises raises clicks and then first-play bounce, which RFY ranks on (`discovery-promise.md` §1).
- Generated key art is labelled key art, never "gameplay". Native Roblox video shows real current gameplay (FD-34).
- No invented numbers, prices, rewards, timers, odds or status labels in any image or text (checklist I8).

## 2. Ads and younger players (V, P12 updated 2026-10-09 unless marked)
| Rule | Src |
| --- | --- |
| Ads are never personalized for users under 18 | FA-33 |
| Ads aimed at under-18 audiences may not directly urge children to buy, nor push them to ask adults to buy | FA-35 |
| No misleading free-Robux offers; no ads that mimic system controls or Roblox UI | FA-37 |
| Clear disclosure, truthful claims, non-infringing assets | FA-36 |
| Rewarded video: 13+ only; reward predetermined, opt-in, delivered promptly; watching is never a progression gate | FA-34 (code side: `platform-policy` C) |
| Age-appropriate integrations, Homepage formats and Billboards may reach all ages, including under-13, since 2026-05-04; under-13 limits differ by format and product category: use the current P12 list, not the older four-category summary | FA-31..32 corrected |
| P12's latest revision changed Portal rules; the page does not say which restrictions were removed: re-read before any Portal plan | FA-38 |
| PolicyService integration is **required** for restricted features; avoiding urgent or pushy messages to minors is **recommended** (both matter for announcements and notifications) | FA-50..51 |
| Paid random items: rules apply to purchases with Robux or Robux-bought currency; actual numerical odds required. Marketing never shows a rare drop as likely | FA-49; `platform-policy` P-01 |
| Keep three separate checks: ad exposure and disclosure · paid-random-item rules · earnings / DevEx eligibility. Passing one does not pass the others | PO-17, FA-30 |

## 3. Ad integrations (brand deals, own merch, paid branded content) (V)
| Rule | Src |
| --- | --- |
| Paid branded content and promoting your own off-platform merchandise count as ad integrations: register in Ads Manager, submit assets, label | FA-39 |
| `AdService:GetCampaignEligibilityAsync` decides per player whether campaign assets may show; region and age limits apply | FA-40 |
| One rejected asset makes the whole campaign ineligible; assets added to a live campaign show only to 18+ while in review | FA-41 |
| Whole-game ads: a persistent "Ad" label bottom-right of the HUD and an "Ad" mark bottom-left on the thumbnail | FA-42 |
| Submit at least 5 days ahead (docs) / 5 business days (P11 FAQ): plan on business days | FA-43 corrected |
| Revenue-share pricing for campaigns starting on or after 2027-01-01: USD per 1,000 qualified visits in the first 28 days, $1.50 U.S., $0.75 Tier 1, $0.20 Tier 2, $0.05 Tier 3, then a flat $0.10; a qualified visit is a session that engages with branded assets, not a person; influencer deals outside the integration excluded; docs also state a $400,000 cap for 2027 campaigns. These are platform charges, **never** an influencer fee or an ad price (read 2026-10-21; re-read before any contract) | FA-44..48, FA-68 |

## 4. Rights: trends are not permission
- US Copyright Office: a game idea, title or play method is not protected as such; expressive art and text can be (FA-53). USPTO: trademark confusion depends on how similar the marks are and how related the goods are, not on exact spelling (FA-54). US guidance only; no legal advice.
- So: borrow a loop, never expression (`market-trends` copying rules). A trending meme, franchise character, song, logo, font or competitor thumbnail is not licensed for your ads. Changing a few pixels or asking an AI for an imitation is not clearance (PO-20).
- Keep a rights record per outside asset: source, license, scope, platforms, paid use, territory, expiry. Unclear cases go to the owner for qualified legal review; never guess (PO-20, PR-09).
- Music for social video: platform commercial libraries do not automatically clear other platforms or paid use (see `channels.md` §1).

## 5. Player data and community
- Roblox (2026-06-02): no tracking Roblox users across platforms; no sending user data (user IDs and usernames are protected) to social, chat, ad or vendor platforms; no bypassing privacy settings. Allowed: Log in with Roblox / OAuth 2.0, Open Cloud, private single-player features, internal tools (FA-55..57). A vendor integration (for example a Discord SDK) does not override this: every data flow needs its own review before anything ships.
- Ask creators and communities for **aggregate** reports only; never collect children's contact details, birthdays, schools or IDs (CR-08, CM-05).
- Discord membership is never required for support, patch notes or rewards; the same essentials exist in game (CM-05).

## 6. The owner's release gate (O, RG-01..07)
Before any publication, post, outreach or spend, the owner approves, with a decision id each:
1. product, format, objective, audience and region (no blanket age rule)
2. promise vs build (proof sheet), rights register, disclosures
3. creator deliverables, pay, rights, adult representative for a minor creator, who monitors
4. spend: total loss ceiling, duration, currency, funding; auto-reload off unless approved
5. integrations: registration, moderation, runtime eligibility, fallback for ineligible players
6. tracking ids, cohort maturity, accounting labels (forecast / attributed / incremental)
7. a pause owner and escalation route for spend anomalies, moderation failure, misleading content, player harm

**Owner-only actions** (FA owner-actions table): create the ad account and accept the terms; add a card (18+) or convert Robux to ad credit (irreversible); publish, pause or cancel a campaign (payment, goal, audience and budget type are fixed after publish); accept Earnings or Engagement; register integrations and invoicing; create any Open Cloud key (a campaign created through the Ads API spends, so it counts as publishing); upload or activate icons, thumbnails and videos; post announcements and notifications; contact creators; sign anything. The marketing agent plans, drafts, measures and writes the package.

## 7. Don't (DN-01..11, checked)
1. Rely on a default-only thumbnail for Home recommendations (FD-01).
2. Call adaptive thumbnail allocation, sequential posts or a rename an A/B test.
3. Call high click-through a success while hiding poor player quality after the click.
4. Reuse a voiced social trailer as the native Roblox video.
5. Hide a sponsorship, or assume a platform label covers every disclosure duty.
6. Invent creator fees, ad-credit rates, cost-per-player targets, minimum spends or a "profitable budget"; the old "285 Robux" rule has no source (FA-26 dropped).
7. Personalize ads to under-18 users or gate progress behind rewarded video.
8. Treat a licensed studio case as permission to use its character, franchise, music or logo.
9. Export Roblox presence or user data because a vendor offers a connection.
10. Use views, sessions and unique players as the same thing, or count projected figures as results.
11. Turn a draft plan into spend, outreach, publication or a contract without the owner.
