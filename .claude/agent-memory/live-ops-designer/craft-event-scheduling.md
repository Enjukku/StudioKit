---
name: craft-event-scheduling
description: Fitting a dated event into release windows and builder lanes - ship dormant in an earlier window, keep the pre-event release gap, design the event around open incidents and the reserved builder
metadata:
  type: feedback
---

When the studio forbids releases close to an event start, ship the event content dormant (time-gated) in an earlier release window and let its start time open it; give a fallback window with a later start, never a start that sits on the rule's edge.

**Why:** J014 G2 (2026-10-21): the 24 h no-release rule plus Tue/Thu windows made a Thu release + Fri start an edge case; the Tue window with a dormant event kept 72 h of margin.

**How to apply:**
- Fit the event to the lane that is actually free (data/config builder) and keep the code builder for harm fixes; if the event needs code, drop it rather than squeeze it.
- Exclude event steps that touch systems with open incidents (a save fault, a broken tutorial step, a laggy area) and add a go/no-go tied to the incident.
- No rewards tied to friends on games with Kids/Select players; no event currency without a written end and conversion rule.
- Kind-level capacity windows are not scope estimates: label them and request the scope estimate.

Related: [[craft-feedback-reading]]
