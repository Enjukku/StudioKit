# Writing and keeping the art bible

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-review`. Sources: `knowledge/reference/art-direction/02` §2, `03` §3, `04` §2, `05` §3; template `templates/skill/art-bible.md`; tool `tools/art/art_refs.py`.

## 1. What the bible is for
A decision tool, not a picture encyclopedia. Another maker (agent or image model) must be able to answer from it: what is fixed, what may vary, which image shows the rule, how approval is judged. Test it that way: could a new agent make a compatible asset without inventing a missing decision? An empty field is an open decision, never permission to fill it silently (02:BF-p1 to BF-p3).

## 2. Two layers in one file
| Layer | Where | Read by |
| --- | --- | --- |
| **Prompt locks** | the families table and the fenced `text` blocks whose first words are `<NAME> LOCK:` | `art_refs.py` (machine-read: keep exactly one copy of each lock, keep the first words) |
| **Direction record** | the other sections of the template (identity, camera, color roles, variation, exceptions, anchor register, cross-craft contracts, technical envelope, change log) | every agent and the owner |

New direction content never goes inside a lock block: the tool would send it to the image model. Run `python -m unittest discover -s tools/tests -p "test_art_refs.py" -t tools/tests` after editing the template's machine-read parts.

## 3. Fields (from the paper's template, mapped to the kit template)
| Field | Holds | Review consequence |
| --- | --- | --- |
| Identity and intent | fantasy line, pillars, owner decision ids, bible revision | reject work that promises another fantasy, however polished |
| Scope and camera | gameplay viewpoints, capture states (normal distance, closest view, smallest presentation), device classes, crowd states, supported orientations and input | compare under real use conditions |
| Locks | shape, proportion, value, palette roles, material, edge, light — each as relationship + purpose + scope + example + failure example + test | every change names the lock it touches |
| Allowed variation | what may differ by biome, faction, rarity, role, mood, event | keeps variety from being called drift |
| Color roles | role → treatment → non-color backup → where it must not appear | one meaning per treatment across world, VFX, UI, marketing |
| Anchor register | id, file, purpose (what it controls), what it does not control, revision, lighting/camera of the image, approval decision id, status (current / superseded / rejected) | only current anchors bind |
| Exceptions | the exception, why, which locks stay protected, how it is recognized as intended, decision id | later agents do not copy it as the new default (03:CM8) |
| Cross-craft contracts | per recurring event: importance rank, owner of each cue (model, motion, VFX, UI, sound), shared state name | test combinations, not pieces |
| Technical envelope | supported rendering modes and quality floor, device evidence, unresolved measurements | visually approved ≠ runtime approved |
| Change log | revision, date, what changed, why, owner's words, affected assets, migration plan | no silent change |

The paper's filled example ("Lantern Workshop") is fictional: copy its writing pattern, never its content (02:§2.3).

## 4. Writing a lock
- Name an observable relationship, not an adjective. "Premium", "stylized", "polished" or "like <studio>" are not locks (03:CM6).
- Good pattern: "Interactable objects keep one graspable feature (handle, wheel, lid) that decorative clutter never repeats; interactables carry the warm accent, clutter never does; backup cue: a slow glint every few seconds." It names the relationship, the forbidden confusion and the backup channel (02:LK1, LK3).
- Lock identity and relationships; never freeze every pixel of one anchor (03:CM7).
- Put exclusions in the lock (no text, no logos, plain background, cut-out color) so briefs need not repeat them (05:AB02).
- Technical budgets (particles, triangles) belong in craft skills with measured sources, not in the bible (05:AB07).

## 5. Revisions and drift
- Bible revision id in the header (`rev N, date`); every manifest row, review and brief names it.
- **Drift check** at every review and every owner decision that touches looks: lock text vs newest decision vs current anchor. Any disagreement: propose the fix to all three in one edit (05:AB04-AB05).
- Retire test locks after the test; one live lock per family (05:AB05).
- Each new environment gets its palette roles recorded in the bible when it is approved, not only in concept images (05:AB06).
- The studio always uses the newest image model (owner J009-D9). If a batch suddenly drifts from the anchors, re-run one approved manifest row and compare before changing any lock (03:CM5).

## 6. Changing the style (transition packet)
Name the problem the change solves (inconsistency, unreadability, new camera or audience, stronger fantasy, production limit). Then write one packet (04:EV1-EV3, TS2):
| Item | Content |
| --- | --- |
| Previous anchor(s) and lock text | as approved, with decision ids |
| Proposed replacement | new lock text and candidate anchors |
| Identity kept | the recognition cues that must survive |
| Rules changed | each changed relationship, why |
| Mixed-scene test | old and new assets in one scene at the gameplay camera |
| Affected assets | list, ordered by importance and dependency |
| Migration | new work adopts the new revision; old assets updated by priority; owner told the temporary mix will show |

Owner approves the packet; nothing is relabelled as approved under the new revision without review.
