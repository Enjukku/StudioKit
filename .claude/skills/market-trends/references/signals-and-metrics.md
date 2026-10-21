> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21. Kit reference: universal (J004). Evidence: owner research paper (notes `knowledge/reference/trends/01-roblox-data-loops.md` **N1**, `02-outside-access-scoring.md` **N2**), fact-checks `fact-check-roblox.md` (**FR**, ids C, D, M, G, K, TR) and `fact-check-outside.md` (**FO**), all checked 2026-10-20/21. Formulas and their traps: `trend-scan/references/formulas.md`.

# Signals and metrics: what each number is, and is not

## 1. Labels (one per number, always)
| Label | Means | Examples |
| --- | --- | --- |
| **OFF** | official: the platform's own counter, chart, document or filing, in its stated scope | Games API `playing`; Roblox charts; SEC letters; Steam Top Sellers definition |
| **3P-S** | third-party sampled: a tracker's repeated reading of public counters (gaps; misses the true peak) | Rolimon's, RoVitals, RoTrends, RoStats peaks and means |
| **3P-E** | third-party estimate or model: revenue, earnings, playtime, downloads | Statroblox, RoVitals earnings, Sensor Tower, tracker "average playtime" |
| **DEV** | developer or creator statement, not audited | interviews, DevForum spotlights |
| **DER** | derived by us; name the formula and inputs | g7, momentum, days since peak, and every mean from our own store (DER from OFF samples, with window and coverage) |
| **MAN** | read by hand from a page (with URL, region, window, read time) | TikTok Creative Center, Google Trends, store charts |
| **UNKNOWN** | not established; never 0, never a neutral guess | most revenue, all competitor retention |

Accuracy order (best first, N1 §2 O): own authorised data for the exact game and period → official aggregate or rank in its scope → owner disclosure → our timestamped counter samples → derived with stated assumptions → opaque estimates. Two sites that reuse one source are one confirmation, not two.

## 2. Roblox counters (Games API, OFF)
| Field | Is | Is not |
| --- | --- | --- |
| `playing` | players online at that moment (snapshot) | daily users; unique people |
| `visits` | cumulative entries | players, sales or retention |
| `favoritedCount` | cumulative favourites | loyalty; dominated by old players |
| up/down votes | cumulative votes | current sentiment: use votes added in a window |
| `created` | universe creation time | the public launch date |
| `updated` | last metadata/update time | a content release date |
| `maxPlayers` | server capacity | audience size |
Identity: key by **universe ID** (root place ID kept); names change and same-name games exist (N1 §3).

## 3. Roblox charts (OFF, ordinal)
| Chart | Official meaning | Use |
| --- | --- | --- |
| Most Popular | most players online now (FR C01) | scale now |
| Top Trending | games players spent more time in over the past two weeks; no formula or cadence published (FR C02) | engagement growth, not money |
| Top Earning | no official definition found; "last 7 days of spend" is one vendor's note (FR C03) | ordinal money signal with date; never dollars |
| Top Revisited, Fun with Friends, Up-and-Coming | exist; no official definition (FR C04) | investigate only; never a retention or co-play rate |
| Recommended For You | personalised; signals at day 1, days 2-7 and days 8-28 (28-day view since 2026-06-15), averages per user, from users who joined organically through RFY; tested daily (FR D01-D04) | a game can grow without topping a chart; a short spike is not enough |
| Editorial picks | curation | a confounder: featured growth is not organic |
Discovery is increasingly age-aware (RDC 2026-09-11, FR D06): the same game can be visible to one age group and not another.

## 4. Trackers (3P-S and 3P-E; read by hand only)
- Peaks are the **highest recorded sample**, not the true peak (Rolimon's states this, ~10-minute updates, FR TR1).
- Tracker means move live: a 24 h / 7 d mean is valid only with its read time (FR K11-K13).
- Tracker playtime is an estimate with no error rate; impossible values occur (−20 min on one page, FR TR3, K07).
- Revenue models: Statroblox range "never narrower than ÷/× 1.6", no measured error (FR TR2); RoVitals assumes 2 earned Robux per player-hour and shows a ×/÷ 3 band that is "not a confidence interval" (FR TR4). No independent validation of any tracker's revenue exists: accuracy **UNKNOWN** (N1 §5).
- Access: Rolimon's, RoTrends and RoStats forbid automated access; Rolimon's licence is personal and non-commercial (not used for studio decisions without consent); RoVitals and Statroblox: hand reading only (FR §1.3).

## 5. Money (context, never a forecast for one game)
| Fact | Value | Label |
| --- | --- | --- |
| Creator earnings | over $1.5 billion in 2025; $923 million in 2024 (published 2026-09-03) | OFF (FR M01) |
| DevEx | over 42,000 in the programme; median about $1,500 (12 months to 2026-06-30; group not stated, reads as DevEx participants) | OFF (FR M02) |
| DevEx rates | $0.0038 per earned Robux standard; $0.0054 for qualifying spend by U.S. players verified 18+ on products, passes, subscriptions, private servers (18+ page dates it 2026-06-08) | OFF (FR M03-M04) |
| Adults | "U.S. O18 users monetize over 50% higher than U18 users" (Q2 2026 letter): U.S. only, metric not named, extrapolated from age-checked users | OFF (FR M05) |
| Hits by spend | Grow a Garden was the top experience by spending within a month of its 2025-03-25 launch; Grow a Garden, Steal a Brainrot, Dead Rails were among June 2025's top 10 by Robux spend | OFF (FR M07-M08) |
| Benchmarks | median per-game session 9.8 min (p90 14.7, p99 21.1); median D1 10.3 %; 500+ titles with 1M+ MAU, Aug 2025-Jul 2026, GameAnalytics SDK games only, "not a census" | 3P (vendor sample, FR G01-G03) |
Rules: never value all Robux at the adult rate or the purchase price; aggregate spend does not show margin or ARPDAU; no fixed multiplier turns CCU into users or dollars; a money scenario is labelled "scenario".

## 6. Records worth knowing (for scale, not targets)
- Steal a Brainrot: over 25 million concurrent in September 2025 (OFF, FR M09); highest recorded tracker sample 25,836,222 on 2025-10-11 (3P-S, FR K02).
- Grow a Garden: 21.6 million (Guinness) / "nearly 22 million" (Roblox) in July 2025 (OFF); highest recorded tracker sample 22,375,597 on 2025-08-23 (3P-S, FR K01). Different dates, no conflict.
- Brookhaven, Grow a Garden, Steal a Brainrot were the top searches of 2025 (OFF, FR M10).
- Developer statements (DEV): Grow a Garden "about 500" → "about 100,000" CCU in about 2 weeks, about 1 million in about a month (FR J01); 99 Nights built "in a sprint of three months" (FR J03). One selected outlier each: never a forecast or a schedule target.
