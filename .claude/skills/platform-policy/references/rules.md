> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Rules extracted by a researcher agent (claude-sonnet-5-5, medium) from the local docs mirror (upstream 7400643), the live create.roblox.com pages (checked 2026-10-20: "live" = live page matched) and official Roblox DevForum announcements. Paths are relative to `knowledge/external/roblox-creator-docs/`. Updated 2026-10-21 by orchestrator · claude-opus-5-5 · default with the J011 fact-check follow-ups (`knowledge/jobs/J011-progression-designer/policy-followups.md`). Help Center articles (Advertising Standards 13722260778260, Promoting Items to Younger Audiences 47965190783892) are readable with curl and a browser User-Agent or through the Help Center API copy; WebFetch gets HTTP 403. Not read: the Terms of Use.

# Platform rules by area

MUST / MUST NOT are Roblox rules. SHOULD is Roblox advice or our safest reading (marked "ours").

## A. Paid random items (eggs, crates, wheels, gacha, keys, spins, re-rolls, luck boosts)
| Rule | API | Source |
| --- | --- | --- |
| Counts as paid random: anything with a random outcome bought with Robux **or with currency that can be bought with Robux**. Types: capsule, enhancement (random duration, chance-based upgrade), combination (merge), probability modifier (luck boost, pity, rate-up). A bundle with a random item inside, a luck game pass (post 60), a blind shop restock, a shown "next outcome" when later outcomes stay random and only buying reveals them (posts 29, 54), an item whose contents change (for example each minute) so the buyer does not know what they get (post 54): all count. Not counted: skill-based variance, even when the player cannot predict a win (post 30); a paid item whose only random part is cosmetic visuals (post 54); earn-only items (no direct or indirect Robux path) | - | `production/monetization/paid-random-items.md:16-47,72,78` (live); DF "Clarifying requirements for paid random items" 4654622 (official Roblox announcement, 2026-05-26; post numbers are its author's replies) |
| MUST show each outcome's odds as numbers **before purchase**, summing to exactly 100 %. Rounding only with a disclaimer, for example "Probabilities are rounded; total of displayed individual probabilities may not equal 100%." Round to four or more decimal places lower than the place of the first non-zero digit: 0.0123456 % (first non-zero digit in the 2nd decimal place) shows as 0.012346 % or longer, never 0.01 %. When unsure, show more digits (ours) | - | `paid-random-items.md:55` (live); DF 4654622 FAQ |
| Long lists MAY go in a pop-up opened by a visible "Info" or "Details" label. A bare (i) icon is not enough. Many items with equal odds MAY share one line "Odds for each item listed below: X %" | - | `:53,57` (live) |
| MUST update the shown odds for that player when an outcome can be won only once | - | `:59` (live) |
| A modifier (luck potion, pity) MUST explain its numeric effect before purchase AND the shown odds MUST change while it is active | - | `:75` (live) |
| Nested boxes: final-outcome odds for every level, before purchase | - | DF 4654622 |
| Every outcome MUST give value; a payment never ends in nothing | - | Community Standards (Roblox economy); DF 4654622 |
| A paid roll whose prize is the currency it was paid with (or currency that converts into it), so the player stakes value to win more or less of it, is a game of chance for items of value: treat it as simulated gambling and do not build it (ours). Currency prizes from a disclosed-odds paid random item are not banned as such (the fixed-order example pays gems, `paid-random-items.md:104-105`); the stake-and-win-back shape is the risk. Unclear cases go to the owner | - | `production/promotion/content-maturity.md:367` (gambling = exchanging money, Robux or in-game items of value for a game of chance; no playable or simulated gambling) |
| MUST check `ArePaidRandomItemsRestricted` per player; if true the player MUST NOT use the generator (Robux or Robux-bought currency). The six permitted treatments (`paid-random-items.md:96-123`): a free earnable path; outcomes in a fixed order disclosed before purchase; direct purchase of the outcome priced at expected value (5 % at 10 Robux → 200 Robux); remove or hide the item; block the purchase with an error message; move the player out of those parts of the game. Prefer hiding or replacing it (DF FAQ). The error-message block is compliant ("technically compliant", DF FAQ) but confusing, so flag it as a player-experience issue, not a violation. Keeping ineligible players out of the whole game is acceptable but more than required (DF FAQ). Roblox changes the region list centrally: never hard-code regions | `PolicyService:GetPolicyInfoForPlayerAsync` → `ArePaidRandomItemsRestricted` | `_api-reference/classes/PolicyService.yaml:91-95`; `paid-random-items.md:83-124` (live); DF 4654622 FAQ |
| MUST check `IsPaidItemTradingAllowed`; if false the player MUST NOT trade any paid item: paid-random outcomes and items bought directly with Robux or with Robux-bought currency. This check is separate from `ArePaidRandomItemsRestricted` and covers different players | `IsPaidItemTradingAllowed` | `PolicyService.yaml:115-118`; `paid-random-items.md:126-130`; DF 4654622 first post and post 31 |
| MUST declare paid random items and paid trading in the maturity questionnaire | - | `production/promotion/content-maturity.md:453-477` (live) |
| Enforcement: human review of the live game; removal and account suspension possible | - | DF 4654622 |

## B. Purchases
| Rule | API | Source |
| --- | --- | --- |
| Grant developer products only from the receipt callback, never from `PromptProductPurchaseFinished` | `MarketplaceService.ProcessReceipt`, `Enum.ProductPurchaseDecision` | `production/monetization/developer-products.md:174-176` (live) |
| Set `ProcessReceipt` once, in one server Script, handling every product. Unset → receipts auto-acknowledged and lost | - | `MarketplaceService.yaml:2247-2249,2303-2305` |
| Return `PurchaseGranted` only after the grant is saved; on failure `NotProcessedYet` (retried only on the next purchase or rejoin) | - | `MarketplaceService.yaml:2274-2299,2347-2355` |
| The same receipt can run on two servers at once: grant idempotently, keyed on `receiptInfo.PurchaseId`, stored with the player's data (ours, from the documented facts). Keep the id: refunds need it | `PurchaseId`, `PlayerId`, `ProductId`, `CurrencySpent` | `MarketplaceService.yaml:2306-2341` |
| `BindReceiptHandler` exists in the API reference (per product type or id; returns `Enum.ReceiptDecision`; overrides `ProcessReceipt`). No guide or announcement: use `ProcessReceipt` as the default | `MarketplaceService:BindReceiptHandler` | `MarketplaceService.yaml:46-185` |
| Purchases outside the game (Store tab, homepage, search): product MUST be Listed and `ProcessReceipt` correct. Roblox checks; a flagged product disappears outside the game | Creator Hub → Monetization → Shop | `developer-products.md:181-217` (live); DF 4888425 (pearvessel, 2026-09-22) |
| Cross-game developer product sales off since 2026-05-30: use Robux transfers | `PromptRobuxTransferAsync` | `developer-products.md:52`; `production/monetization/robux-transfers.md:13-19` |
| MUST NOT hard-code prices in UI. Managed Pricing charges regional prices; read them at runtime on the client so the label matches the prompt | `GetProductInfoAsync`, `GetDeveloperProductsAsync` | `production/monetization/regional-pricing.md:71,93-97`; `developer-products.md:55-56` |
| Gifting or trading across price levels SHOULD check price levels at join; do not cache past the session. Levels run 1-1000 (guide: 1000 = full global price, 500 = half). The docs disagree on the return shape and meaning: the guide shows an array of `{UserId, PriceLevel}`; the reference says a dictionary keyed by user id strings and that level 100 means a suggested price of 100 Robux. Test the real return in Studio and handle both shapes | `MarketplaceService:GetUsersPriceLevelsAsync` | `regional-pricing.md:101-126`; `MarketplaceService.yaml:769-795` |
| Subscriptions: distinct names with price and duration; same benefits on every platform; honour the full term; no steering to off-platform purchase; no new tasks after payment (battle passes exempt). Gate on eligibility fields | `PromptSubscriptionPurchase`, `GetUserSubscriptionStatusAsync`; `IsEligibleToPurchaseSubscription`, `IsEligibleToPurchaseCommerceProduct` | `production/monetization/subscriptions.md:24-31,339-341` |
| Refunds: Roblox revokes passes; developer-product benefits are ours to revoke (Open Cloud "Transaction Refunded" webhook, no retry) | webhook | DF 4890339 (2026-09) |
| Prompt purchases after a player action (docs examples always do; no explicit rule found, ours) | `PromptProductPurchase`, `OpenShop` | `developer-products.md:114` |

## C. Ads
| Rule | API | Source |
| --- | --- | --- |
| Rewarded video: native Roblox format only (own implementations banned from 2026-05-04); no third-party ad SDKs or measurement calls | `AdService` | DF "New advertising policies & standards" 4527365 (superburr0, 2026-03-20, upd. 06-17). Not in the docs page: the post is newer and binding |
| Rewarded video: player presses a button first; reward and action disclosed before every ad; reward right after; not a progress gate; reward is a Robux-sold developer product, never Robux, **never random**; no rewarded ads to under-13 | `GetAdAvailabilityNowAsync` (late), `CreateAdRewardFromDevProductId`, `ShowRewardedVideoAdAsync` (server) | `production/promotion/rewarded-video-ads.md:30,35,358-362` (live); DF 4527365; Advertising Standards § Publisher Integrity (Advertising Integrations, Ad Fraud) |
| Publisher eligibility (rewarded and immersive): 13+, ID-verified, 2FA, public game, approved questionnaire, ≥ 2,000 monthly visitors; rewarded video not for free-form user creation games | - | `rewarded-video-ads.md:44,350-364`; `production/monetization/immersive-ads.md:88-100` |
| MUST hide, replace or block ad units when `AreAdsAllowed` is false | `AreAdsAllowed` | `immersive-ads.md:284-290`; `PolicyService.yaml:85-89` |
| Brand deals and promoting your own off-platform merch are ad integrations: register in Ads Manager, wait for approval (~48 h; submit 5+ days ahead), label "Ad" (legible within 500 studs; whole-game: HUD label bottom-right + thumbnail mark) | `GetCampaignEligibilityAsync`, `RegisterDisclosureButton` | `production/promotion/ad-integrations.md:14-35,125-173` (live) |
| No ads personalised to under-18 | - | Advertising Standards (Help Center 13722260778260), first paragraph; page "Last Updated: Oct 9, 2026" (the rule is older than that update) |

## D. Age, chat and safety
| Rule | API | Source |
| --- | --- | --- |
| Never gate core gameplay on the age check: console and VR cannot run it, and Unchecked can be permanent. Prompt after a deliberate player action, not at spawn | `Player.AgeChecked`, `Player:PromptAgeCheck()` | `Player.yaml:63-82,2565-2578`; DF 4607091 (peraldon, 2026-04-30) |
| Chat is age-based (Kids 5-8 off by default; Select 9-15 off until age-checked; 16+ on). Never assume players can chat with each other; check before chat-dependent features | `TextChatService:CanUserChatAsync`, `CanUsersChatAsync`, `GetChatGroupsAsync` (server; enable Chat & Voice Groups APIs) | `production/publishing/kids-and-select.md:43-45`; `TextChatService.yaml:286-470` |
| Filter all shown text you do not control (TextBox input, names, codes, generated or fetched words, stored pet names) on the server, after submit, in `pcall`. Unfiltered games are removed until fixed | `TextService:FilterStringAsync` → `GetNonChatStringForBroadcastAsync` / `GetNonChatStringForUserAsync` | `ui/text-filtering.md:11-40,74-105` (live) |
| Every public game MUST have an accurate maturity questionnaire; resubmit after any update that changes an answer. Labels: Minimal/Mild → Kids + Select; Moderate → Select + 16+; Content May Vary → age-checked 16+; Restricted → age-verified 18+ | - | `content-maturity.md:18-35,67-73` (live). `production/promotion/experience-guidelines.md` is stale (13+/17+): do not use |
| Restricted (18+) triggers: strong violence, heavy realistic blood, strong language, romance, alcohol, adult venues, private-space settings. Free-form user creation and social hangouts 16+ | - | `content-maturity.md:99-103,144,250,377-447` |
| MUST NOT include playable or simulated gambling. A paid roll that pays back its own currency: § A | - | `content-maturity.md:363-367`; Community Standards |
| Under-18 games avoid settings that are mainly bedrooms, bathrooms, closets | - | `safety.md:20` |
| Younger players: the game MUST use PolicyService for subscriptions, paid random items, paid trading, immersive ads and commerce products. Sales wording SHOULD NOT be pushy or urgent ("GET IT NOW", "LAST CHANCE, ACT NOW"); use "View Item", "See Price", "Open Shop" (Roblox best practice, not a rule). Linked parents can set spend and screen-time limits until the child turns 13, so a purchase prompt can fail for a reason the game cannot see: handle a declined prompt quietly (ours) | `PolicyService` | Help Center "Promoting Items to Younger Audiences" 47965190783892 (updated 2026-10-08); `production/publishing/kids-and-select.md:48-51`; newsroom 2026-06-16 (per J011 fact-check FB17) |
| Media sharing (screenshots, video, feeds): hide when `IsContentSharingAllowed` is false. Kids/Select: no feed + autoplay/infinite scroll + reward for watching | `IsContentSharingAllowed`, `IsEndlessContentLoadAllowed`, `IsEndlessContentAutoplayAllowed` | `PolicyService.yaml:97-101,139-149`; DF 4829188 (Roblox, 2026-08-25) |
| Social links appear only on the game, group or profile page, seen by age-checked 16+. MUST NOT show links or handles in the game ("join discord.gg/..."). Allowed: "Links on our game's page" | - | `production/promotion/social-media-links.md:11-70` (live); DF 4685717 (2026-06-16) |
| Bans: `Players:BanAsync`. Trading and ranked play may gate on `Player:IsVerified()` | `BanAsync`, `IsVerified` | `safety.md:32-34` |

## E. Regions (all `GetPolicyInfoForPlayerAsync` keys)
`AreAdsAllowed`, `ArePaidRandomItemsRestricted`, `IsContentSharingAllowed`, `IsEligibleToPurchaseCommerceProduct`, `IsEligibleToPurchaseSubscription`, `IsPaidItemTradingAllowed`, `IsPhotoToAvatarAllowed`, `IsSubjectToChinaPolicies`, `IsEndlessContentLoadAllowed`, `IsEndlessContentAutoplayAllowed`, `AllowedExternalLinkReferences` (legacy, always empty). Source `PolicyService.yaml:85-149`. Call on the server per player per session, in `pcall`; it can error ("called too many times"); do not cache across sessions (`:153-184`). Roblox can also block a whole game per country (`production/promotion/regional-content-availability.md:21-24`).

## F. Player data and privacy
| Rule | Source |
| --- | --- |
| Key all player data by UserId (in the store name, key or scope), never username: deleted accounts' usernames are retired, and RTBF automation finds data only by `{UserId}` | `cloud-services/data-stores/right-to-be-forgotten.md:15-31` (live) |
| We stay responsible for deleting all personal data on a right-to-erasure request. Set RTBF deletion templates (≤ 100) in Creator Hub; other data via the "Right to Erasure Request" webhook; verify within 30 days | `production/publishing/RTBF-and-creators.md:29-42`; `right-to-be-forgotten.md:52-57,159-165` |
| Collect nothing personal beyond Roblox's own ids: no emails, phones, addresses, birth dates, photos; never send personal data to external servers | Community Standards (personal information) |

## G. AI features inside the game
| Rule | Source |
| --- | --- |
| Any player-triggered generative AI response (text, voice, image, 3D, movement) MUST be declared in the questionnaire and shown with a visible notice at start and throughout ("AI-powered, not human, may make mistakes") | `generative-AI.md:30,67-71`; `content-maturity.md:495-499` |
| Extended AI interactions (memory across sessions, or an AI character as the main purpose) → Restricted (18+) | `generative-AI.md:49-59` |
| Third-party AI output is ours to moderate and MUST go through TextChatService; point users to real help on medical or crisis topics | `generative-AI.md:19-46,73-75` |
| Using AI to build the game is not covered by these rules | `generative-AI.md` |

## H. Off-platform, money and IP
| Rule | Source |
| --- | --- |
| MUST NOT sell items for real money or Robux off-platform, route around Roblox payments, trade Robux, run gambling, or solicit charity; real-value contests and off-platform promotions tied to rewards need Roblox involvement | Community Standards |
| MUST NOT direct players off Roblox except through Social Links | Community Standards; `subscriptions.md:30` |
| MUST NOT use third-party copyright or trademarks without a licence; credit or "no profit" is no defence. Franchise themes need original designs (licensing route: `ip-licensing/`) | `production/publishing/ip-guidelines.md:25,45-52`; Community Standards |
| Terms of Use update effective 2026-11-01 (Roblox as merchant of record): re-read before writing sales wording | DF 4907620 (2026-10-01) |

## Numbers that change: link, do not copy
Kids/Select entry threshold (500 → 250 → 100 announced for November 2026), expedited review and publishing fees, ad revenue-share rates (campaigns from 2027-01-01), rewarded-video visitor floor, subscription price tiers and minimum, managed-pricing cap, restricted regions. Read the page on the day; write the date next to any number you use.

## Not verified (2026-10-21)
Terms of Use full text; a written rule that purchase prompts need a player action; product-description wording rules beyond subscriptions; "no engagement data to advertisers" (an earlier line here, cited to Community Standards): not in the Advertising Standards on 2026-10-21, Community Standards not re-read.
