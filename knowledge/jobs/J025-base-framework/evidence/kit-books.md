---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-S9
supersedes: []
---
> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24

# J025 step 9: kit books point to the framework

All paths under `C:\Users\Firew\Downloads\uterd\StudioKit`. Canonical skills edited in `.agents/skills/`; `.claude/skills/` copies written by `python tools/sync_harness.py` (check: in sync, 347 files). None of these files had another session's uncommitted change before the edit (`git diff --stat` empty); every skill edit is additions only (`git diff --numstat`: 0 deletions).

| # | File | Change |
| --- | --- | --- |
| 1 | `.agents/skills/engineering-craft/references/framework.md` (NEW, 247 lines) | Rules FW-01..FW-06 (use the block before base code; never edit a copy); start (`new_game.py`), install/update (`install.py --ref`), lock check, game gate, require rule; block index (use for / never instead); 12 contract cards (API, the rule, owners, test lanes, usage example from the contracts with the real `@game/` requires); deviations |
| 2 | `.agents/skills/engineering-craft/SKILL.md:27` (§2 row), `:73` (§5 rule) | pointer row to `references/framework.md`; final-check rule against base code and edited copies |
| 3 | `.agents/skills/architecture/SKILL.md:126` (new §8) | Loader systems; owner table (Session, State, Net, Loader, Screens, game data, handlers); placement table; block service is part of the require path |
| 4 | `.agents/skills/data-saving/SKILL.md:50` (§5 line), `:68` (new §8) | Session = default adapter; D-01..D-15 mapped to Session invariants and test ids; ProfileStore pin + P-1; Studio save edits |
| 5 | `.agents/skills/networking-security/SKILL.md:67` (new §7) | Blink schema + Net = standard path; who does each N-02 step (steps 4-7 stay in handlers); gaps G1-G10 and what covers each |
| 6 | `.agents/skills/code-review/SKILL.md:133` (new §8) | bypass greps B1-B11 (DataStore/receipts outside Session, raw remotes, handlers outside Net, `LoadAnimation`, second library, `check_lock`, Instance requires, Config for money, tween literals, AnalyticsService, content without spec) |
| 7 | `.agents/skills/testing/SKILL.md:126` (new §8) | three lanes (Lune gate; Jest in Studio Edit DM / Server DM with LoadStringEnabled; multi-client via StudioTestService); planted faults through the patch argument; protected `tests/acceptance/`; memory limit; leak rule |
| 8 | `.agents/skills/ui-basics/SKILL.md:23`, `.agents/skills/animation-craft/SKILL.md:23` (§2 rows) | use Screens, Motion, Anim → framework.md §4.6-4.8 |
| 9 | `knowledge/design/game-profile.md:26` | packages row → framework version + blocks used + deviation and why (row kept in place); `updated` and Author revision line |
| 10 | `rules/packages.md:23` (new section at end) | ProfileStore exception with the owner's words (J025-G1 D-2), pinned copy, P-1, re-check triggers, notes folder |
| 11 | `knowledge/reference/libraries/{profilestore,blink,charm,charm-sync,janitor,signal,jest}.md` (NEW) | one record each: version, date, licence, why chosen, known gaps and how the framework covers them, where pinned, update path. Folder follows `rules/knowledge.md` §6 (`knowledge/reference/<area>/`) |

## Findings for the lead (not fixed: outside scope)
- Framework `CHANGELOG.md` "Vendored" still says ProfileStore "no patches"; `vendor/ProfileStore/PATCHES.md` lists P-1.
- The framework repo has no commit and no tag yet, so `install.py --ref <tag>` cannot run; framework.md says to leave `--ref` out until the first tag.
- Contract usage examples still use the `require(Framework.X)` placeholder (contracts `README.md` Placement note 2); framework.md shows the real `@game/` form.
