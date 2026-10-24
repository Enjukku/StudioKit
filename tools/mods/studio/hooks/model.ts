// Pure parts of the Studio pane: kit files in, plain data out. No `$` here, so tests run them directly.

import type {
  StudioDeskItem,
  StudioDeskJob,
  StudioGate,
  StudioRole,
  StudioUsageRun,
  StudioUsageSession,
} from '../types'

/** Craft rooms on the floor (feasibility page, Part 2 "Studio floor"); any other type goes to Helpers. */
export const ROOMS: { id: string; label: string; roles: string[] }[] = [
  { id: 'art', label: 'ART', roles: ['art-director', 'modeler', 'character-rigger', 'animator', 'ui-ux-designer'] },
  { id: 'code', label: 'CODE', roles: ['architect', 'feature-builder', 'quick-builder', 'reviewer', 'performance-engineer'] },
  { id: 'fx', label: 'SOUND & FX', roles: ['vfx-designer', 'sound-designer'] },
  { id: 'stage', label: 'STAGE & FILM', roles: ['environment-designer', 'film-director'] },
  { id: 'design', label: 'DESIGN', roles: ['game-designer', 'progression-designer', 'live-ops-designer'] },
  { id: 'qa', label: 'QA & STUDIO', roles: ['qa-lead', 'studio-operator'] },
  { id: 'market', label: 'DATA & MARKET', roles: ['analyst', 'marketing', 'trend-scout'] },
  { id: 'help', label: 'HELPERS', roles: [] },
]

/** Types that count as reviewers for the "3+ reviewers in one round" flag. */
export const REVIEWERS = new Set(['reviewer', 'qa-lead', 'art-director', 'performance-engineer'])

/** Built-in helpers: not counted in the "same role 3+ runs" flag. */
export const HELPERS = new Set(['general-purpose', 'Explore', 'explore', 'Plan', 'claude', 'fork', 'doc-keeper'])

export const MIN = 60_000
export const WAIT_MS = 30 * MIN
export const ROUND_MS = 30 * MIN
export const CONTEXT_MARK = 500_000

export function roomOf(type: string): string {
  const role = type.replace(/^[^:]+:/, '')
  return ROOMS.find(room => room.roles.includes(role))?.id ?? 'help'
}

/** O / S / H / F for Opus, Sonnet, Haiku, Fable; C for Codex or GPT models; ? when unknown. */
export function modelLetter(model: string): string {
  const m = model.toLowerCase()
  if (m.includes('opus')) return 'O'
  if (m.includes('sonnet')) return 'S'
  if (m.includes('haiku')) return 'H'
  if (m.includes('fable')) return 'F'
  if (m.includes('gpt') || m.includes('codex')) return 'C'
  return '?'
}

export function effortPips(effort: string): number {
  return { low: 1, medium: 2, high: 3, xhigh: 4, max: 4 }[effort] ?? 0
}

/** `--job J0xx` in a brief first, else the first job id in the text (as usage_report.py's job_of). */
export function jobOf(text: string): string {
  const flag = /--job\s+(J\d{3})/.exec(text)
  const any = /\b(J\d{3})\b/.exec(text)
  return flag?.[1] ?? any?.[1] ?? ''
}

/** Frontmatter `key: value` pairs of a Markdown file. */
export function frontmatter(text: string): Record<string, string> {
  const block = /^---\r?\n([\s\S]*?)\r?\n---/.exec(text)
  const out: Record<string, string> = {}
  for (const line of (block?.[1] ?? '').split(/\r?\n/)) {
    const [, key, value] = /^([A-Za-z_-]+):\s*(.*)$/.exec(line) ?? []
    if (key !== undefined) out[key] = (value ?? '').trim().replace(/^["']|["']$/g, '')
  }
  return out
}

/** A role file's keys; its model is `model:` when pinned, else its `tier:` through kit.json `models.claude`. */
export function roleOf(file: string, text: string, tiers: Record<string, string> = {}): StudioRole {
  const fm = frontmatter(text)
  const model = fm.model || tiers[fm.tier ?? ''] || ''
  return { name: fm.name || file.replace(/\.md$/, ''), color: fm.color ?? '', model, effort: fm.effort ?? '' }
}

/** `- J028-studio-pane · title` lines of knowledge/jobs/active.md. */
export function parseActive(text: string): { folder: string; job: string; title: string }[] {
  const out: { folder: string; job: string; title: string }[] = []
  for (const line of text.split(/\r?\n/)) {
    const [, folder, title] = /^-\s+(J\d{3}[\w-]*)\s+·\s+(.*)$/.exec(line.trim()) ?? []
    if (folder !== undefined) out.push({ folder, job: folder.slice(0, 4), title: (title ?? '').split(' · ')[0] ?? '' })
  }
  return out
}

function cells(line: string): string[] {
  return line.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim())
}

/** Rows of the job card's `## Gates` table (any table whose header starts with "Gate"). */
export function parseGates(card: string): StudioGate[] {
  const out: StudioGate[] = []
  let inTable = false
  for (const line of card.split(/\r?\n/)) {
    if (!line.trim().startsWith('|')) {
      inTable = false
      continue
    }
    const row = cells(line)
    const first = row[0] ?? ''
    if (first === 'Gate') {
      inTable = true
      continue
    }
    if (!inTable || /^-+$/.test(first.replace(/[\s:]/g, ''))) continue
    if (/^G\d/.test(first)) out.push({ label: first, date: /\d{4}-\d{2}-\d{2}/.exec(row[1] ?? '')?.[0] ?? '', rev: row[2] ?? '' })
  }
  return out
}

/** The owner's desk for one job: its Status row, open gates, and every needs-decision line. */
export function parseDesk(
  entry: { folder: string; job: string; title: string },
  card: string,
  decisions: string,
): StudioDeskJob {
  const base = `knowledge/jobs/${entry.folder}`
  const status = card.split(/\r?\n/).map(cells).find(row => row[0] === 'Status')?.[1] ?? ''
  const gates = parseGates(card)
  const items: StudioDeskItem[] = gates
    .filter(gate => gate.date === '')
    .map(gate => ({ kind: 'gate', text: `${gate.label} open`, file: `${base}/job-card.md` }))
  for (const [file, text] of [['job-card.md', card], ['decisions.md', decisions]] as const) {
    for (const line of text.split(/\r?\n/)) {
      if (/needs-decision/i.test(line) && !/^\s*>/.test(line) && cells(line)[0] !== 'Status') {
        items.push({ kind: 'decision', text: short(line.replace(/[|*`#]/g, ' ').replace(/\s+/g, ' ').trim(), 140), file: `${base}/${file}` })
      }
    }
  }
  return { job: entry.job, folder: entry.folder, title: entry.title, status: short(status, 160), items, gates }
}

export function short(text: string, n: number): string {
  return text.length > n ? `${text.slice(0, n - 1)}…` : text
}

// ---- Flow map ---------------------------------------------------------------------------------

export type FlowBar = {
  id: string
  lane: string
  start: number
  end: number
  read: number
  peak: number
  label: string
  detail: string
  isLive: boolean
}

export type FlowPiece = { t0: number; t1: number; isBreak: boolean }

export type Flow = {
  job: string
  lanes: string[]
  bars: FlowBar[]
  pieces: FlowPiece[]
  gates: { t: number; label: string }[]
  flags: string[]
  t0: number
  t1: number
  read: number
  active: number
}

/** A gap longer than this between agent runs is drawn as a short break, not to scale. */
export const BREAK_MS = 90 * MIN

const ms = (iso: string): number => Date.parse(iso)

export function hhmm(t: number): string {
  const d = new Date(t)
  return `${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`
}

export function span(msLength: number): string {
  const m = Math.round(msLength / MIN)
  return m < 60 ? `${m} min` : `${Math.floor(m / 60)} h ${String(m % 60).padStart(2, '0')} m`
}

function dateOf(t: number): string {
  const d = new Date(t)
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
}

/** Merged busy intervals of the bars, sorted. */
function busy(bars: FlowBar[]): [number, number][] {
  const out: [number, number][] = []
  for (const bar of [...bars].sort((a, b) => a.start - b.start)) {
    const last = out[out.length - 1]
    if (last && bar.start <= last[1]) last[1] = Math.max(last[1], bar.end)
    else out.push([bar.start, bar.end])
  }
  return out
}

export type LiveRunInput = { id: string; type: string; description: string; model: string; job: string; start: number; end: number | null; tokens: number }

/**
 * One job's flow: a lane per role (the lead's sessions first), a bar per run, gates, flags.
 * Runs come from the usage report; this session's live runs fill in what the report has not read yet.
 */
export function buildFlow(
  job: string,
  usageRuns: StudioUsageRun[],
  sessions: StudioUsageSession[],
  live: LiveRunInput[],
  gates: StudioGate[],
  now: number,
): Flow {
  const agents: FlowBar[] = usageRuns
    .filter(run => run.job === job)
    .map(run => ({
      id: run.id,
      lane: run.type,
      start: ms(run.first),
      end: Math.max(ms(run.last), ms(run.first)),
      read: run.read,
      peak: run.peak,
      label: run.description || run.type,
      detail: `${run.type} · ${run.description}\n${run.model}${run.effort ? ` · ${run.effort}` : ''} · ${run.calls} calls\nread ${mtok(run.read)} · out ${ktok(run.out)} · peak ${ktok(run.peak)}`,
      isLive: false,
    }))
  const known = new Set(agents.map(bar => bar.id))
  for (const run of live) {
    if (run.job !== job || known.has(run.id)) continue
    agents.push({
      id: run.id,
      lane: run.type,
      start: run.start,
      end: run.end ?? now,
      read: run.tokens,
      peak: 0,
      label: run.description || run.type,
      detail: `${run.type} · ${run.description}\n${run.model} · ${run.end === null ? 'running' : 'done'} (this session)`,
      isLive: run.end === null,
    })
  }
  const lead: FlowBar[] = sessions
    .filter(s => s.job === job)
    .map(s => ({
      id: s.session,
      lane: 'lead',
      start: ms(s.first),
      end: Math.max(ms(s.last), ms(s.first)),
      read: s.read,
      peak: s.peak,
      label: s.title,
      detail: `lead session ${s.session} · ${s.title}\n${s.model} · ${s.calls} calls\nread ${mtok(s.read)} · out ${ktok(s.out)} · peak ${ktok(s.peak)}`,
      isLive: false,
    }))
  const bars = [...lead, ...agents]
  const empty: Flow = { job, lanes: [], bars: [], pieces: [], gates: [], flags: [], t0: now, t1: now, read: 0, active: 0 }
  if (bars.length === 0) return empty

  const runsBusy = busy(agents.length ? agents : bars)
  const t0 = Math.min(...bars.map(b => b.start))
  const t1 = Math.max(...bars.map(b => b.end))

  // Pieces: to scale where agents ran or gaps are short; a fixed break where the gap passes BREAK_MS.
  const pieces: FlowPiece[] = []
  let cursor = t0
  for (const [a, b] of runsBusy) {
    if (a - cursor > BREAK_MS) {
      pieces.push({ t0: cursor, t1: a, isBreak: true })
      cursor = a
    }
    if (b > cursor) {
      pieces.push({ t0: cursor, t1: b, isBreak: false })
      cursor = b
    }
  }
  if (t1 > cursor) pieces.push({ t0: cursor, t1, isBreak: t1 - cursor > BREAK_MS })

  // Idle gaps between agent runs; a gate sits in the longest gap on its date (inference: the date has no time).
  const gaps = runsBusy.slice(1).map(([a], i) => ({ from: runsBusy[i]?.[1] ?? a, to: a })).filter(g => g.to > g.from)
  const placed: { t: number; label: string }[] = []
  const unplaced: string[] = []
  for (const gate of gates.filter(g => g.date)) {
    const onDate = gaps.filter(g => dateOf(g.from) === gate.date || dateOf(g.to) === gate.date)
    const best = onDate.sort((a, b) => b.to - b.from - (a.to - a.from))[0]
    const label = `${gate.label}${gate.rev ? ` (${short(gate.rev.replace(/`/g, ''), 28)})` : ''}`
    if (best) placed.push({ t: (best.from + best.to) / 2, label })
    else unplaced.push(`${gate.label} on ${gate.date}`)
  }
  placed.sort((a, b) => a.t - b.t)

  const flags: string[] = []
  // Same role 3+ runs in one stage (stages split at the placed gates).
  const cuts = [t0 - 1, ...placed.map(g => g.t), t1 + 1]
  for (let s = 0; s < cuts.length - 1; s++) {
    const counts = new Map<string, number>()
    const [from = t0, to = t1] = cuts.slice(s, s + 2)
    for (const bar of agents) {
      if (bar.start >= from && bar.start < to && !HELPERS.has(bar.lane)) counts.set(bar.lane, (counts.get(bar.lane) ?? 0) + 1)
    }
    for (const [lane, n] of counts) if (n >= 3) flags.push(`${lane} ran ${n} times in stage ${s + 1}`)
  }
  // 3+ reviewer runs that start within ROUND_MS of the round's first start.
  const reviews = agents.filter(bar => REVIEWERS.has(bar.lane)).sort((a, b) => a.start - b.start)
  for (let i = 0; i < reviews.length; ) {
    const round = reviews.slice(i).filter(r => r.start - (reviews[i]?.start ?? 0) <= ROUND_MS)
    if (round.length >= 3) flags.push(`${round.length} reviewers in one round at ${hhmm(round[0]?.start ?? 0)} (${round.map(r => r.lane).join(', ')})`)
    i += Math.max(1, round.length)
  }
  // Waits: no agent ran for more than WAIT_MS; with a gate in the gap it waited on the owner.
  for (const gap of [...gaps].sort((a, b) => b.to - b.from - (a.to - a.from))) {
    if (gap.to - gap.from <= WAIT_MS) break
    const gate = placed.find(g => g.t > gap.from && g.t < gap.to)
    flags.push(
      gate
        ? `wait ${span(gap.to - gap.from)} on the owner at ${hhmm(gap.from)} (${gate.label})`
        : `idle ${span(gap.to - gap.from)} at ${hhmm(gap.from)}: no agent ran (lead or owner)`,
    )
  }
  for (const bar of bars) if (bar.peak > CONTEXT_MARK) flags.push(`${bar.lane} "${short(bar.label, 40)}" passed the 500k context mark (${ktok(bar.peak)})`)
  for (const text of unplaced) flags.push(`${text}: no idle gap on that date, not drawn`)

  const order = new Map<string, number>()
  for (const bar of [...agents].sort((a, b) => a.start - b.start)) if (!order.has(bar.lane)) order.set(bar.lane, order.size)
  const lanes = [...(lead.length ? ['lead'] : []), ...order.keys()]
  return {
    job,
    lanes,
    bars,
    pieces,
    gates: placed,
    flags,
    t0,
    t1,
    read: bars.reduce((n, b) => n + b.read, 0),
    active: runsBusy.reduce((n, [a, b]) => n + (b - a), 0),
  }
}

export function mtok(n: number): string {
  return `${(n / 1e6).toFixed(n >= 1e7 ? 0 : 1)} M`
}

export function ktok(n: number): string {
  return n >= 1e6 ? mtok(n) : `${Math.round(n / 1000)} k`
}
