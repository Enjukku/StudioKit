<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; revised 2026-10-21 (J016: packet, owner_words, inputs@rev, protected, consumers, peers); revised by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (peers only for hand-spawned agents; brief files need frontmatter). A brief saved as a file in the job folder (a ledger ticket's `ask`) starts with the frontmatter block of templates/jobs/contract-header.md (type: job, without revision) so kb_index --lint passes. -->
# Brief: <job-id>-T<nn> <craft>

Format and rules: `rules/messages.md` §1-2. Prose in `<intent>`, every exact value in `<spec>`. A `fixed` value needs a source; the how goes in `open`. Every input has a revision. Send the brief whole, in one message.

```text
<intent>
<goal, the feeling or result for the player, why it matters, where it sits>
</intent>
<spec>
id: <job-id>-T<nn>
from: <role>
to: <role>
model: <tier model>
effort: <low | medium | high>
skills: [<craft skills to load first>]
packet: python tools/context_packet.py packet "<task>" --role <to-role> --job <job-id>
owner_words: ["<the owner's sentences, verbatim, when the work touches taste>"]
refs:
  - <path>   # take: <what>; avoid: <what>
inputs:
  - <path>@rev<n>
fixed:
  <key>: <value with unit>   # <source: owner D-id | contract rev | budget | style lock | vocabulary>
open: [<choices the receiver owns>]
avoid: [<named patterns to avoid>]
protected: [<what already passed and must stay passed>]
consumers: [<roles that use this output>]
peers: {<role>: <agent id from crew.md>}   # only for agents the lead spawns by hand; none inside a saved workflow
owns: [<paths the receiver may write>]
not_in_scope: [<items>]
rules: [<every rule the work must keep, in full words, incl. the owner's limits>]
deliver: <path, not named report/summary/findings/analysis>
checks:
  - C1: <runnable pass rule>
return: <hand-back to whom>
</spec>
```
