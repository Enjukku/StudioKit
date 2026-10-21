// Kit tool (universal): run a saved job workflow script with fake agents, so its control flow is tested without spending tokens.
// Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016).
// Usage: node tools/workflows/wf_harness.mjs <script.js> '<args json>' '<scenario json>'
// Scenario keys: refuseSign (every sign step says no), blockOnce (the first art-director review finds one blocking defect),
//   blockAlways (every review finds a blocking defect), greybox, conflicts (first interface round has a conflict).
// Prints one JSON line: {status, outcome, agents, phases, labels} and exits 0; exits 1 on a contract violation:
//   an agent() call without agentType, model, effort or schema, or a prompt without <intent>, <spec> and checks.
import fs from 'node:fs'

const [, , file, argsJson = '{}', scenarioJson = '{}'] = process.argv
const src = fs.readFileSync(file, 'utf8').replace(/^export const meta =/m, 'const meta =')
const args = JSON.parse(argsJson)
const scenario = JSON.parse(scenarioJson)

function fake(sch, label) {
  const out = {}
  for (const [k, v] of Object.entries(sch.properties)) {
    if (v.type === 'array') out[k] = []
    else if (v.type === 'boolean') out[k] = false
    else if (v.type === 'integer') out[k] = 1
    else if (k === 'status') out[k] = 'done'
    else if (v.enum) out[k] = v.enum[0]
    else out[k] = 'x'
  }
  if ('signs' in out) out.signs = !scenario.refuseSign
  const finding = (maker) => [{ id: 'F1', class: 'blocking', maker_role: maker, where: 'w', evidence: 'e', smallest_fix: 'f' }]
  if ('findings' in out && scenario.blockAlways) out.findings = finding(scenario.maker || 'art-director')
  if ('findings' in out && scenario.blockOnce && /art-director: RV-[^ ]*-r0-/.test(label)) out.findings = finding(scenario.maker || 'art-director')
  if ('affected_roles' in out) out.affected_roles = scenario.affected || []
  if ('needs_greybox' in out) out.needs_greybox = !!scenario.greybox
  if ('conflicts' in out && scenario.conflicts && /-r1-/.test(label)) out.conflicts = [{ about: 'B1', why: 'w', needs: 'n' }]
  return out
}

const calls = []
let violation = ''
const agent = async (prompt, o = {}) => {
  if (!o.agentType || !o.model || !o.effort || !o.schema) violation ||= `agent() without agentType/model/effort/schema: ${o.label}`
  if (!/<intent>/.test(prompt) || !/<spec>/.test(prompt) || !/checks:/.test(prompt)) violation ||= `brief without <intent>/<spec>/checks: ${o.label}`
  calls.push({ label: o.label || '', phase: o.phase || '' })
  return fake(o.schema || { properties: {} }, o.label || '')
}
const parallel = async (thunks) => Promise.all(thunks.map(t => t().catch(() => null)))
const pipeline = async (items, ...stages) => Promise.all(items.map(async (item, i) => {
  let prev = item
  for (const s of stages) { try { prev = await s(prev, item, i) } catch { return null } }
  return prev
}))
const noop = () => {}
const run = new Function('args', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'budget', 'workflow',
  'return (async () => {\n' + src + '\n})()')
const res = await run(args, agent, parallel, pipeline, noop, noop, { total: null, spent: () => 0, remaining: () => Infinity },
  async () => { throw new Error('nested workflow() not mocked') })
console.log(JSON.stringify({ status: res && res.status, outcome: res && res.outcome, agents: calls.length,
  phases: [...new Set(calls.map(c => c.phase))], labels: calls.map(c => c.label), violation }))
process.exit(violation ? 1 : 0)
