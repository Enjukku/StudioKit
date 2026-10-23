// Kit tool (universal): run a saved job workflow script with fake agents, so its control flow is tested without spending tokens.
// Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); revised by workflow-fixer W3 · claude-opus-5-5 · high · 2026-10-21, J016 G3
// (concurrency and exclusive-resource checks, schema-vs-template check, role check, null and status scenarios, timeline and brief dumps).
// Usage: node tools/workflows/wf_harness.mjs <script.js> '<args json>' '<scenario json>'
// Scenario keys (all optional):
//   refuseSign            every sign step says no
//   blockOnce             the first art-director review of round 0 finds one blocking defect (maker: scenario.maker or art-director)
//   blockAlways           every review finds a blocking defect (maker: scenario.maker or art-director)
//   blockLabel            regex: reviews whose label matches find one blocking defect (maker: scenario.maker); blockLabelOnce: only the first match
//   greybox, newCast      the contract asks for a greybox / says a new cast is needed
//   conflicts             the first interface round has a conflict
//   affected              array: the repair scope's affected roles
//   timing                fix and scope steps report timing_changed true
//   images                'pending': every image step returns images.state pending; imagesLabel (regex): only the matching ones
//   lesson                every hand-back carries the optional lesson draft
//   set                   {key: value}: override that hand-back key on every agent that returns it (e.g. {no_visible_parts: true})
//   nullLabel             regex: matching agent() calls return null (the subagent died or was skipped)
//   statusLabel, status   regex and status: matching agent() calls return that status
//   uniform               every fake agent takes the same time (default: a fixed per-label duration, so lanes interleave unevenly)
//   timeline              print start and end ticks per call
//   dump                  regex: print the brief and the returned object of matching calls
// Prints one JSON line: {status, outcome, agents, maxConcurrent, phases, labels, result, meta, dumps, timeline?, violation} and exits 0;
// exits 1 on a contract violation: an agent() call without agentType, model, effort or schema; a brief without <intent>, <spec> and checks;
// a hand-back schema that does not match templates/jobs/handback.schema.json; an unknown role or a model off its tier; a phase not in meta.phases;
// more than 5 agents at once; two agents at once that both hold the Studio, Blender or the built-in browser; a brief that names SendMessage or peers.
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const [, , file, argsJson = '{}', scenarioJson = '{}'] = process.argv
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..')
const raw = fs.readFileSync(file, 'utf8')
const src = raw.replace(/^export const meta =/m, 'const meta =')
const args = JSON.parse(argsJson)
const scenario = JSON.parse(scenarioJson)
const metaMatch = raw.match(/^export const meta = (\{[\s\S]*?\n\})\n/m)
const meta = metaMatch ? new Function('return ' + metaMatch[1])() : null
const phaseTitles = meta && meta.phases ? meta.phases.map(p => p.title) : []

// ---------------------------------------------------------------- reference data
const TEMPLATE = JSON.parse(fs.readFileSync(path.join(ROOT, 'templates', 'jobs', 'handback.schema.json'), 'utf8'))
const TIER_MODEL = { lead: 'opus', craft: 'opus', research: 'sonnet', mechanical: 'haiku' }
const roleTier = {}
for (const f of fs.readdirSync(path.join(ROOT, '.agents', 'roles'))) {
  if (!f.endsWith('.md') || f === 'README.md') continue
  const m = fs.readFileSync(path.join(ROOT, '.agents', 'roles', f), 'utf8').match(/^tier:\s*(\w+)/m)
  roleTier[f.slice(0, -3)] = m ? m[1] : ''
}
function strip(x) {
  if (Array.isArray(x)) return x.map(strip)
  if (x && typeof x === 'object') { const o = {}; for (const k of Object.keys(x)) if (k !== 'description' && k !== '$comment') o[k] = strip(x[k]); return o }
  return x
}
function schemaProblem(sch) {
  const keys = Object.keys(sch.properties || {})
  const req = sch.required || []
  const tkeys = Object.keys(TEMPLATE.properties)
  const lost = tkeys.filter(k => !keys.includes(k))
  if (lost.length) return `schema lacks template fields ${lost.join(', ')}`
  const pos = tkeys.map(k => keys.indexOf(k))
  if (pos.some((p, i) => i && p < pos[i - 1])) return 'schema fields are not in the template order (evidence before answers)'
  if (keys.slice(-2).join(',') !== 'status,outcome') return 'status and outcome are not the last fields'
  for (const k of tkeys) {
    if (TEMPLATE.required.includes(k) !== req.includes(k)) return `field ${k} is ${req.includes(k) ? '' : 'not '}required, unlike the template`
    if (JSON.stringify(strip(TEMPLATE.properties[k])) !== JSON.stringify(strip(sch.properties[k]))) return `field ${k} differs from the template`
  }
  if (sch.additionalProperties !== false) return 'schema allows additional properties'
  return ''
}

// ---------------------------------------------------------------- fake hand-backs
let intCounter = 0
function fakeValue(s, key) {
  if (!s) return 'x'
  if (s.type === 'array') return []
  if (s.type === 'boolean') return false
  if (s.type === 'integer') return ++intCounter   // unique, rising: revisions differ from call to call
  if (s.type === 'object') { const o = {}; for (const k of (s.required || [])) o[k] = fakeValue(s.properties[k], k); return o }
  if (key === 'status') return 'done'
  if (s.enum) return s.enum[0]
  return 'x'
}
const onceUsed = {}
function fake(sch, label) {
  const out = fakeValue(sch, '')
  const finding = (maker) => [{ id: 'F1', class: 'blocking', maker_role: maker, where: 'w', expected: 'e', observed: 'o', evidence: 'e', smallest_fix: 'f' }]
  const maker = scenario.maker || 'art-director'
  if ('signs' in out) out.signs = !scenario.refuseSign
  if ('findings' in out) {
    if (scenario.blockAlways) out.findings = finding(maker)
    if (scenario.blockOnce && /art-director: RV-[^ ]*-r0-/.test(label)) out.findings = finding(maker)
    if (scenario.blockLabel && new RegExp(scenario.blockLabel).test(label)) out.findings = finding(maker)
    if (scenario.blockLabelOnce && !onceUsed.block && new RegExp(scenario.blockLabelOnce).test(label)) { onceUsed.block = true; out.findings = finding(maker) }
  }
  if ('affected_roles' in out) out.affected_roles = scenario.affected || []
  if ('needs_greybox' in out) out.needs_greybox = !!scenario.greybox
  if ('new_cast_needed' in out) out.new_cast_needed = !!scenario.newCast
  if ('timing_changed' in out) out.timing_changed = !!scenario.timing
  if ('conflicts' in out && scenario.conflicts && /-r1-/.test(label)) out.conflicts = [{ about: 'B1', why: 'w', needs: 'n' }]
  if (out.images && scenario.images && (!scenario.imagesLabel || new RegExp(scenario.imagesLabel).test(label))) out.images.state = scenario.images
  if (scenario.lesson && sch.properties && sch.properties.lesson) {
    out.lesson = fakeValue(sch.properties.lesson, 'lesson')
    out.lesson.type = scenario.lesson === 'none' ? 'none' : 'failure'   // 'none' = nothing to keep, the workflow skips it
  }
  for (const [k, v] of Object.entries(scenario.set || {})) if (k in out) out[k] = v
  if (scenario.statusLabel && new RegExp(scenario.statusLabel).test(label)) out.status = scenario.status || 'blocked'
  return out
}

// ---------------------------------------------------------------- the fake runtime
const RESOURCES = [
  ['Studio', /you are the only Studio driver/],
  ['Blender', /you are the only Blender user/],
  ['browser', /you are then the only browser user|you are the only agent using the built-in browser|you are its only user|you are the only image maker/],
]
const calls = []
const dumps = []
const active = new Set()
let clock = 0
let inFlight = 0
let maxConcurrent = 0
let violation = ''
function hash(s) { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h }
const tick = () => new Promise(r => setImmediate(r))
const agent = async (prompt, o = {}) => {
  const label = o.label || ''
  if (!o.agentType || !o.model || !o.effort || !o.schema) violation ||= `agent() without agentType/model/effort/schema: ${label}`
  if (!/<intent>/.test(prompt) || !/<spec>/.test(prompt) || !/checks:/.test(prompt)) violation ||= `brief without <intent>/<spec>/checks: ${label}`
  if (/SendMessage|\bpeers:/.test(prompt)) violation ||= `brief names SendMessage or peers (workflows use files only): ${label}`
  if (o.schema) { const p = schemaProblem(o.schema); if (p) violation ||= `${label}: ${p}` }
  if (o.agentType && o.agentType !== 'general-purpose') {
    if (!(o.agentType in roleTier)) violation ||= `${label}: no role file for ${o.agentType}`
    else if (TIER_MODEL[roleTier[o.agentType]] !== o.model) violation ||= `${label}: model ${o.model} is off the ${roleTier[o.agentType]} tier of ${o.agentType}`
  }
  if (phaseTitles.length && o.phase && !phaseTitles.includes(o.phase)) violation ||= `${label}: phase "${o.phase}" is not in meta.phases`
  const rec = { label, phase: o.phase || '', start: ++clock, end: 0, holds: RESOURCES.filter(([, re]) => re.test(prompt)).map(([n]) => n) }
  calls.push(rec)
  for (const other of active) {
    const both = rec.holds.filter(h => other.holds.includes(h))
    if (both.length) violation ||= `${both.join(', ')} held by two agents at once: "${other.label}" and "${label}"`
  }
  active.add(rec)
  inFlight++
  maxConcurrent = Math.max(maxConcurrent, inFlight)
  if (maxConcurrent > 5) violation ||= `more than 5 agents at once (rules/company.md §9), at "${label}"`
  const n = scenario.uniform ? 3 : 1 + (hash(label) % 5)
  for (let i = 0; i < n; i++) await tick()
  active.delete(rec)
  inFlight--
  rec.end = ++clock
  const out = scenario.nullLabel && new RegExp(scenario.nullLabel).test(label) ? null : fake(o.schema || { properties: {} }, label)
  if (scenario.dump && new RegExp(scenario.dump).test(label)) dumps.push({ label, prompt, returned: out })
  return out
}
const parallel = async (thunks) => Promise.all(thunks.map(t => Promise.resolve().then(t).catch(() => null)))
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
const outLine = { status: res && res.status, outcome: res && res.outcome, agents: calls.length, maxConcurrent,
  phases: [...new Set(calls.map(c => c.phase))], labels: calls.map(c => c.label), result: res, meta, dumps, violation }
if (scenario.timeline) outLine.timeline = calls.map(c => ({ label: c.label, start: c.start, end: c.end }))
console.log(JSON.stringify(outLine))
process.exit(violation ? 1 : 0)
