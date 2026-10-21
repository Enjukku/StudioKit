<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-20 -->
# Brief: <job-id>-T<nn> <craft>

Format and rules: `rules/messages.md` §1-2. Prose in `<intent>`, every exact value in `<spec>`. A `fixed` value needs a source; the how goes in `open`. Send the brief whole, in one message.

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
refs:
  - <path>   # take: <what>; avoid: <what>
fixed:
  <key>: <value with unit>   # <source: owner D-id | contract | budget | style lock>
open: [<choices the receiver owns>]
avoid: [<named patterns to avoid>]
owns: [<paths the receiver may write>]
not_in_scope: [<items>]
rules: [<every rule the work must keep, in full words, incl. the owner's limits>]
deliver: <path, not named report/summary/findings/analysis>
checks:
  - C1: <runnable pass rule>
return: <hand-back to whom; sample first (G2) or full>
</spec>
```
