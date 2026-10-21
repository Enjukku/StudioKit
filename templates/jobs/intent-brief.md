<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-20 -->
# Brief: <job-id>-T<nn> <craft>

Format and rules: `rules/messages.md` §1-2. Prose for intent, `yaml` for every exact value. A `fixed` value needs a source; the how goes in `open`.

<Intent: goal, the feeling or result for the player, why it matters, where it sits. Max 6 sentences.>

```yaml
id: <job-id>-T<nn>
from: <role>
to: <role>
model: <tier model>
effort: <low | medium | high>
refs: [<paths>]
fixed:
  <key>: <value with unit>   # <source: owner D-id | contract | budget | style lock>
open: [<choices the receiver owns>]
owns: [<paths the receiver may write>]
not_in_scope: [<items>]
deliver: <path>
checks:
  - C1: <runnable pass rule>
return: <hand-back to whom; sample first (G2) or full>
```
