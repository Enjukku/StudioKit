---
name: marketing-design
description: What and why of a Roblox game's marketing - one promise across title, icon, thumbnails, page and video, discovery, ads, creators, honest testing. Use when a game is pitched, named, launched or updated, for "nobody finds the game", "the thumbnail doesn't get clicks", "players click but leave", "make a better title", "should we run ads". Marketing reads first; marketing-craft is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J012 from the owner's marketing research paper (2026-10-21; VERIFIED / EXPERIENCE / OPINION tags kept) and three fact-checks (`knowledge/reference/marketing/fact-check-*.md`, FD / FA / FS ids, read 2026-10-21). Tags here: **V** platform-documented fact · **E** someone's reported result, never a forecast · **O** the paper's proposed practice. Revised by J018 maker marketing · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the marketing-art standards (§4 M-15..M-23), the box-art step (§3 step 3) and the core principles of this craft (§7); after the stage 3 review the timing grammar in §7 row 8 gained the beat.

# Marketing design: sell the game players will really get

## 1. When this skill starts
It answers five questions, in this order:
1. **What does the game promise, and what is being launched?** The player fantasy and the one moment that proves it, reachable in ordinary play (from the game designer's hook and promise ledger); for an update, the new world, character or mode that becomes the hero of every image.
2. **Who is it for, and what do they already want?** Audience, age band, devices, the words they use, what fans of this game or genre want to see (trend scout, analyst, community; dated).
3. **How will they meet it?** Which Roblox surfaces and outside channels, and what each one needs (§3).
4. **How will we know it worked?** The decision, metric, cohort and window, agreed with the analyst before anything goes live.
5. **What may we not do?** Platform rules, younger players, rights, and the owner's gate.

The marketing agent owns the answers as **proposals**. The owner approves the promise, every final asset, every external message and every spend (paper rule 15). How to make and check the assets: `marketing-craft`.

§4 holds the standards and §7 the core principles of this craft; after a compaction, re-read both before judging an image.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Roblox discovery and RFY facts, titles, icon and thumbnail facts, personalization, the game page and native video | `references/discovery-promise.md` |
| Short video and trailers, creators, Roblox Ads Manager, updates / events / notifications, community and Discord | `references/channels.md` |
| Truth rules, ads and younger players, ad integrations, rights, player data, the release gate, owner-only actions, don'ts | `references/policy-rights.md` |
| Cases (Roblox and other studios): what they show, what they do not | `references/cases.md` |
| How to make marketing art to the §4 standards: the stages, the self-review, worked examples | `marketing-craft/references/image-pipeline.md`, `image-review.md` |
| How to do the work: steps, tools, templates, tests, hand-offs | `marketing-craft` |
| The hook test, the promise ledger, the title as fantasy | `game-concept` (C-02, C-08, `references/hook-promise.md`) |
| Marketing art that matches the game | `art-direction/references/platform-evolution-marketing.md` §3 |
| Trend numbers and their labels | `market-trends` |
| Platform rules in code (ads, paid random items, PolicyService) | `platform-policy` |

## 3. Steps
1. **Start at the concept, not at launch.** Marketing joins the game designer at preproduction step 1: title candidates and the first image test the concept itself (`preproduction` growth order). *Check:* the promise line and its moment are in the vision record.
2. **One promise, everywhere.** Title, description, icon, thumbnails, native video, social edits, announcements and the first session promise the same achievable thing; each claim has a playable promise-ledger row (`policy-rights.md` §1).
3. **Earn the click with the real moment, made like box art.** Titles name the action and a real stake; the icon carries identity; each thumbnail shows one hero, one action, one consequence the game really has (`discovery-promise.md` §2-3). Browsing players choose from small tiles in a glance, so the icon and thumbnails get the job's highest effort and are judged at tile size among the tiles they compete with (§4 M-15..M-23).
4. **Deliver in the first session.** RFY ranks on what organically arrived players do next (PTR, first-play bounce, play days, playtime): marketing that overpromises is punished by the platform, not only by players (`discovery-promise.md` §1). Bring onboarding friction to the game designer instead of buying more impressions.
5. **Pick channels by fit, not by habit.** Native video and page first; then updates and events tied to real changes; short video where the game films well; creators with a bounded first deliverable; ads only as a measured test with a loss ceiling (`channels.md`).
6. **Test honestly.** Define the decision with the analyst first. Name the method: adaptive (thumbnail personalization), observational (titles, icons), attributed (ads, share links), randomized (only real experiments). Inconclusive is a valid result (`marketing-craft/references/testing-measurement.md`).
7. **Gate with the owner.** Nothing goes out without the seven-item release gate and a decision id (`policy-rights.md` §6).

## 4. Craft core (what separates great marketing from weak)
| ID | Practice | Evidence or why |
| --- | --- | --- |
| M-01 | **Optimize promise-to-play, not clicks.** A click from the wrong player costs ranking: RFY weighs PTR and first-play bounce of organic RFY players, then play days and playtime per user | V: RFY signals (FD-04..09); O: paper's central rule (MP:7) |
| M-02 | **The title is the fantasy, said plainly.** Action + distinct condition; the game answers any "what happens if". Keep the name stable; no repeated words; emojis at most one or two; genre matches | O: TI-04..06; V: Roblox naming rules (FD-13..17); `game-concept` C-02 |
| M-03 | **No title, video or posting optimum exists.** Never state a best length, word count, emoji count, posting hour or cadence; test your own game | V: FD-18; YouTube gives no numeric cadence, only "consistent, sustainable", and says publish time is not known to affect long-term performance (FS-04..05); O: OQ-04, OQ-06 |
| M-04 | **Icon = identity; thumbnail = one moment.** Icon: theme, tone, genre at about 150×150. Thumbnail: the moment ordinary play reaches, readable at the phone tile, nothing essential at the bottom | V: FD-19..25, FD-74; O: IM-19 |
| M-05 | **A custom thumbnail is the entry ticket** to Home recommendations since 2026-10-19; it guarantees nothing | V: FD-01..02 |
| M-06 | **Real gameplay early.** Native video in RFY: current gameplay in the first seconds, no cinematic trailer; reported lifts are directional, not forecasts | V: FD-47..48; E: FD-49 |
| M-07 | **Adaptive is not A/B.** Thumbnail personalization is a bandit over 2-5 images; no native title or icon test exists; ad creative delivery is documented as even. Label every result by its method | V: FD-26, FD-35..36, FA-11; T04 answer |
| M-08 | **Every number keeps its denominator.** qPTR is not PTR; views, sessions and unique players differ; immature cohorts are pending; 2026-10-12 changed Roblox's recording | V: FD-30, FD-42..43, FD-51..52; O: ME-19, ME-24 |
| M-09 | **Ads buy consideration, never ranking.** Ad-arrived players do not count for RFY; plan an ad test as a bounded experiment with a loss ceiling and a holdout where possible; two ledgers (platform-attributed vs studio incremental) | V: FD-10, FA-58 (E: Roblox-reported 21-campaign medians); O: AD-17 |
| M-10 | **Creators: buy a deliverable and an audience, not followers.** Written quote per campaign, disclosure inside the video, rights and reuse separate, one share link each, aggregate reports only | O: CR-01..08; V: disclosure rules (FS-12..14, FS-20, FS-32..33); share links (FD-68) |
| M-11 | **Return messages need a real reason.** Announcements, events and notifications point to something live; a sending limit is not a cadence target | V: FD-53..64; O: UP-10 |
| M-12 | **Younger players change the rules.** No ad personalization under 18; no urging children to buy; rewarded video 13+; PolicyService required; no pushy messages to minors | V: FA-31..37, FA-50..51 |
| M-13 | **Borrow loops and craft lessons, never expression.** Cases are hypotheses, not forecasts; trends are not licenses | O: RU-06, PO-20; V: FA-53..54; `references/cases.md` |
| M-14 | **The owner holds every external lever.** The agent drafts, measures and recommends; publishing, spending, outreach and contracts are owner actions with decision ids | O: paper rule 15, RG-01..07; `policy-rights.md` §6 |
| M-15 | **The launched thing is the hero.** The new world, character or mode (or, at launch, the game's core fantasy) is the largest readable element with the highest contrast; when options tie, go back to what is being launched, not to taste | the image's job is to make players want the new thing; a beautiful image that hides it fails |
| M-16 | **Recognised in about half a second beats unique.** At the tile a viewer names the game's kind and the action; choose the option read fastest, then add uniqueness inside that read; it must still stand apart from the neighbouring tiles | players scan a grid of small tiles; a look-alike is skipped or mistaken |
| M-17 | **A few chunky identifiers, silhouette first, face second.** The hero survives as 3-4 big identifying shapes (the art bible's anchors), pushed past real; small details are cut, not shrunk; the face and likeness match the game in every product | at tile size only big shapes survive; a drifting face reads as someone else |
| M-18 | **One message, one symbol, one read order.** Primary (hero and action), secondary (consequence or stakes), tertiary (place); 2-3 flow lines lead to the primary; a dark foreground frames, the midground carries, the background unifies; calm room for the title; detail clumped where the eye should go | an image that says many things equally says nothing at tile size |
| M-19 | **Contrast spent only on the hero.** Lower the surroundings first, then raise the hero; the brightest value and the strongest colour pop sit on the focal point; a wide value range for a dramatic moment, narrower for a calm or cosy game; the read holds in grayscale | attention goes to the strongest difference; if everything is loud, nothing is |
| M-20 | **Light and colour have jobs.** One motivated key light; a rim separates the hero; light from below means threat; colour roles from the art bible (dominant theme hue, support, complementary accent, the brand colour kept), gameplay colour meanings kept; shadows shift hue; checked on a phone | light leads the eye and sets good or evil; colour is read before shape and differs per screen |
| M-21 | **The pose sells the character.** A one-sentence premise picks the moment; the character takes its signature move's key pose from the game, at the peak or just before it, one line of action, weight believable; the camera height states its status (low for dominant, eye level for friendly) | a generic pose shows a character players never meet; a pushed pose on a believable base reads in a glance |
| M-22 | **One family, one brand.** Icon, thumbnails, title treatment, event art and the game itself read as one game; each event or update changes one property of the brand pattern (texture, colour, an ornament) and borrows its motif from the game's own UI, items or story; the theme reads first, a hidden detail rewards a close look | players recognise the series instantly and still see something new |
| M-23 | **Made for a specific audience, never the typical idea.** Show what this game's fans want at its strongest; reject the expected first idea and bring one unexpected element from outside the genre, inside the game's tone | work everyone is "okay with" is loved by no one; the expected tile disappears in the grid |

## 5. Rules (final check, short)
- No promise the build does not deliver. No future feature as live. No fake UI, Robux, prices, rewards, odds or timers in any asset.
- No invented optimum, benchmark, fee, CPM, CPP, minimum spend or forecast. Platform limits are stated as limits with a read date.
- Case results and platform-reported lifts are EXPERIENCE with scope, never targets.
- Ads and younger players, paid random items, player data: `platform-policy` + `references/policy-rights.md`.
- No franchise, character, music, logo or competitor art without the owner's rights record.
- The owner approves the promise, assets, messages and spend; the agent never acts externally.

## 6. Self-check before returning
- [ ] The promise line, its moment and its promise-ledger row are named before any asset; for an image, the launched hero, the sell list, the premise and the audience's "fans want" line are written first.
- [ ] Every image meets §4 M-15..M-23 as measured and looked at through `marketing-craft/references/image-review.md`, each line labelled by what proved it.
- [ ] Every Roblox fact used has its source id and read date; re-read the live page if older than the decision.
- [ ] Every test names its method label and its analyst spec.
- [ ] Age, ad, rights and data rules checked for every channel used.
- [ ] Owner decisions listed with a recommendation and a default; nothing external done.

## 7. Core principles for this craft
The studio's universal principles (master numbers), said for marketing work. Checks name their input; MR lines are in `marketing-craft/references/image-review.md`.

| # | Principle for marketing | Example | Check |
| --- | --- | --- | --- |
| 1 | **The promise read comes first.** The tile says what the player will do in the game; style and beauty never hide the hero or the action | a moody wide landscape loses to the tile where the digger's strike is the biggest shape | MR-06, MR-07 on the sheet at tile size |
| 2 | **Judge it where players meet it:** the tile on a phone with the title under it and the metadata band over it, the icon at 150×150, among the tiles it competes with | an icon rich at 1024 px shows a 9 px face at 150 px | MR-06, MR-21 to MR-23; the owner on a phone at G1 |
| 3 | **Decide what is read first and spend contrast only there:** the hero has the highest contrast and the largest readable area; the title has calm room; lower the surroundings before raising the hero | the cave walls were darkened instead of brightening the digger | MR-12, MR-17, MR-20 |
| 4 | **Big before small:** brief, thumbnails, silhouette, value and light, colour, then detail; composition in the final frame first; effects last | smoke painted before the layout locked had to be repainted | stage dates in the campaign record; MR-13, MR-28 |
| 5 | **Shape carries identity:** the hero's identifying shapes fill the crop and name it in black-fill; sharp reads dangerous, round friendly; a group reads as one shape | the knight's frying-pan shield and plume name it in the mask panel alone | MR-08 |
| 6 | **Less is more:** one message, one symbol, a clean backdrop, 3-4 identifiers; what does not raise the read is removed | taking the coin pile out of the tile made the strike read faster | MR-20 (remove-one-element test) |
| 7 | **One code for meaning:** the game's colour meanings and the brand pattern (name, fonts, lock-up, colours) hold in every asset; an event changes one property | the enemy red never goes on the hero; the event logo keeps the font and gains a frost texture | MR-15, MR-26 |
| 8 | **Timing tells cause and effect:** a still shows the peak of a real action or the instant before, cause before consequence; a video opens on one real action's tell, build, beat (the held instant of tension), peak and result | the pickaxe at contact with the light bursting out, not the digger walking up | MR-09; `marketing-craft/references/channel-kits.md` §3 opening-beat check |
| 9 | **Push what must read past real, on a believable base:** big hero, oversized signature item, stronger pose and contrast, with weight and contact still believable | the pickaxe doubled in size while the feet stay planted under the body | MR-09, MR-11 |
| 10 | **The subject's character drives every choice:** a one-sentence premise and the sell list come first; the character takes its own signature pose; every choice traces to them | "the toughest brawler is secretly sweet": the thumbs-up key pose, not a generic punch | MR-01, MR-09 |
| 11 | **One world, one style; identity survives every variant:** art bible locks and anchors, the same face and colours in every product, the family reads as one game | a likeness that drifted toward another character is fixed before review | MR-10, MR-26 |
| 12 | **Controlled variation, never the generic:** the typical first output is a warm-up; one unexpected element; no machine-made sameness (identical repeats, flat fills, tidy symmetry) | the atypical rough (the view from inside the crystal) gave the final its framing | MR-03, MR-04 |
| 13 | **Problem, constraints and target first:** the brief (hero, sell list, premise, message, audience, surfaces, crop plan, claim id) before the first prompt | no image is generated for a world whose claim id is still `planned` | MR-01 |
| 14 | **Research, many distinct options, a reasoned pick:** our game's anchors and captures first, outside reference second; 3-5 roughs from different hooks at equal finish; one recommended with reasons | four roughs from scale, strike, friends and an inside view; B picked with A's scale, reasons tied to the sell list | MR-02, MR-04, MR-05 |
| 15 | **Cheap stages first; gates freeze:** thumbnail round (G1), green light (G2: big shapes, values, light stop moving), render, polish; closed directions are not reopened without new owner words | a "change the composition" note at polish becomes the next update's ticket | MR-28; the G1 and G2 records |
| 16 | **Critique against the goal, one problem at a time:** questions name the goal ("which says 'break in' fastest on a phone?"); notes name the layer; mirror and grey refresh my eyes; ties go to the owner with a recommendation | a note "make it pop" is restated as "the digger merges with the rock at tile size" and fixed by value | MR-05, MR-24, MR-32 |
| 17 | **Build for the next craft and the engine:** a layered, crop-safe master; the crop plan and the asset kit list; briefs that give the animator the premise and camera and the renderer named groups | the event team made the banner by toggling the effects layer, without asking | MR-22, MR-30 |
| 18 | **Know when it is done:** done when every crop passes at its real size, the budget is spent or the notes start repeating; new ideas become follow-ups | the third review round brought only repeats, so the set went to the owner | MR-22; budget line in the hand-back |
| 19 | **Feedback follows the real outcome:** never show a reward, rarity or celebration the shown action does not earn in ordinary play; a reveal image shows a tier players really get | no rare-glow burst on a common egg in the thumbnail | MR-25; `references/policy-rights.md` §1-2 |
| 20 | **Every player can read it:** the promise reads in grayscale at icon size; meaning never rides on colour alone (shape, words); a video reads muted with captions and with sound | the event tile names the event in words, not only in its new colour | MR-12, MR-13 (grey); `marketing-craft/references/channel-kits.md` §3 muted review |

Project overlay: if `knowledge/overlays/marketing-design.md` exists, read it after this file; it wins for this game.
