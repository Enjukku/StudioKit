// The Studio pane (J028): Floor shows who runs and what waits on the owner; Flow shows one job's runs.
// Data is read-only: $.agent.list() and agent.spawn for live runs, job folders through $.fs,
// `python tools/usage_report.py --json` through $.process every 60 s while the pane is open.

import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { StudioAgent, StudioDeskJob, StudioRole, StudioRun, StudioUsage } from '../types'
import { buildFlow, hhmm, jobOf, mtok, parseActive, parseDesk, roleOf, short, span } from './model'
import { type Figure, fit, floorSvg, flowSvg } from './svg'

const PANE = 'studio'
const TITLE = 'Studio'
const TOOL = 'open_pane'

const openA = atom({ plugin: 'studio', key: 'open' } as const, false)
const tabA = atom({ plugin: 'studio', key: 'tab' } as const, 'floor')
const jobA = atom({ plugin: 'studio', key: 'job' } as const, '')
const runsA = atom({ plugin: 'studio', key: 'runs' } as const, [])
const agentsA = atom({ plugin: 'studio', key: 'agents' } as const, [])
const rolesA = atom({ plugin: 'studio', key: 'roles' } as const, [])
const deskA = atom({ plugin: 'studio', key: 'desk' } as const, [])
const usageA = atom({ plugin: 'studio', key: 'usage' } as const, { at: 0, error: '', agents: [], sessions: [] })

const ACTIVE = new Set(['pending', 'running', 'waiting'])

let cwd = '.'
let isKit = false
let isUsageRunning = false
const written: Record<string, string> = {}

/** Writes only when the value changed, so a poll that finds nothing new draws nothing. */
function changed(key: string, value: unknown): boolean {
  const text = JSON.stringify(value)
  if (written[key] === text) return false
  written[key] = text
  return true
}

async function loadRoles($: EngineInterface): Promise<void> {
  const entries = await $.fs.list('.agents/roles').catch(() => [])
  const kit = await $.fs.read('kit.json').catch(() => '')
  let tiers: Record<string, string> = {}
  try {
    tiers = (JSON.parse(typeof kit === 'string' ? kit : '') as { models?: { claude?: Record<string, string> } }).models?.claude ?? {}
  } catch {
    // No readable kit.json: badges fall back to the model each run reports.
  }
  const roles: StudioRole[] = []
  for (const entry of entries) {
    if (entry.kind !== 'file' || !entry.name.endsWith('.md') || entry.name === 'README.md') continue
    const text = await $.fs.read(`.agents/roles/${entry.name}`).catch(() => '')
    if (typeof text === 'string') roles.push(roleOf(entry.name, text, tiers))
  }
  if (changed('roles', roles)) await update($, rolesA, () => roles)
}

async function refreshDesk($: EngineInterface): Promise<void> {
  const active = await $.fs.read('knowledge/jobs/active.md').catch(() => '')
  const desk: StudioDeskJob[] = []
  for (const entry of parseActive(typeof active === 'string' ? active : '')) {
    const card = await $.fs.read(`knowledge/jobs/${entry.folder}/job-card.md`).catch(() => '')
    const decisions = await $.fs.read(`knowledge/jobs/${entry.folder}/decisions.md`).catch(() => '')
    desk.push(parseDesk(entry, typeof card === 'string' ? card : '', typeof decisions === 'string' ? decisions : ''))
  }
  if (changed('desk', desk)) await update($, deskA, () => desk)
}

async function refreshAgents($: EngineInterface): Promise<void> {
  const list = await $.agent.list()
  const agents: StudioAgent[] = list.map(a => ({ id: a.id, type: a.type, description: a.description, status: a.status }))
  if (changed('agents', agents)) await update($, agentsA, () => agents)
  const ended = new Set(list.filter(a => !ACTIVE.has(a.status) && a.status !== 'idle').map(a => a.id))
  if (ended.size === 0) return
  const now = await $.clock.now()
  await update($, runsA, runs =>
    runs.some(r => r.end === null && ended.has(r.id)) ? runs.map(r => (r.end === null && ended.has(r.id) ? { ...r, end: now } : r)) : runs,
  )
}

async function refreshUsage($: EngineInterface): Promise<void> {
  if (isUsageRunning) return
  isUsageRunning = true
  try {
    const at = await $.clock.now()
    const ran = await $.process
      .run(['python', 'tools/usage_report.py', '--json', '--root', cwd], { timeoutMs: 120_000 })
      .catch((error: unknown) => ({ exitCode: -1, stdout: '', stderr: String(error) }))
    let usage: StudioUsage = { at, error: '', agents: [], sessions: [] }
    if (ran.exitCode !== 0) {
      usage = { ...usage, error: short(ran.stderr.trim() || `exit ${ran.exitCode}`, 200) }
    } else {
      const data = JSON.parse(ran.stdout) as { agents?: StudioUsage['agents']; sessions?: StudioUsage['sessions'] }
      usage = {
        at,
        error: '',
        agents: (data.agents ?? []).filter(a => a.job).map(a => ({ ...a, effort: String(a.effort ?? '') })),
        sessions: (data.sessions ?? []).filter(s => s.job),
      }
    }
    await update($, usageA, () => usage)
  } finally {
    isUsageRunning = false
  }
}

async function refreshAll($: EngineInterface): Promise<void> {
  if (!isKit) return
  await Promise.all([refreshAgents($), refreshDesk($)])
  await refreshUsage($)
}

async function openPane($: EngineInterface, tab: string, job: string): Promise<boolean> {
  if (tab === 'floor' || tab === 'flow') await update($, tabA, () => tab)
  if (/^J\d{3}$/.test(job)) await update($, jobA, () => job)
  await update($, openA, () => true)
  const { isPlaced } = await $.ui.open({ id: PANE, title: TITLE })
  $.clock.after(0, () => void refreshAll($))
  return isPlaced
}

function parseArgs(text: string): { tab: string; job: string } {
  const words = text.trim().split(/\s+/)
  return { tab: words.find(w => w === 'floor' || w === 'flow') ?? '', job: jobOf(text) }
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    cwd = e.cwd
    isKit = (await $.fs.exists('tools/usage_report.py')) && (await $.fs.exists('knowledge/jobs/active.md'))
    await $.command.register({
      name: 'studio',
      description: 'Open the Studio pane: the studio floor and the flow map of one job',
      argumentHint: '[floor|flow] [job id]',
    })
    await $.tool.register({
      name: TOOL,
      description:
        'Opens the Studio pane beside the chat: the studio floor (running agents by craft room, the owner\'s desk of open gates and needs-decision items) and the flow map of one job. The lead calls it at the start of every owner request.',
      inputSchema: {
        type: 'object',
        properties: {
          tab: { type: 'string', enum: ['floor', 'flow'], description: 'The tab to show; floor when absent' },
          job: { type: 'string', description: 'A job id (J025) for the flow tab' },
        },
      },
      isDeferred: false,
    })
    if (isKit) {
      await loadRoles($)
      $.clock.every(3_000, () => void refreshAgents($))
      $.clock.every(30_000, async () => {
        if (await read($, openA)) await refreshDesk($)
      })
      $.clock.every(60_000, async () => {
        if (await read($, openA)) await refreshUsage($)
      })
    }
    return next(e)
  })

  on('command.run', { command: 'studio' }, async ($, e) => {
    const { tab, job } = parseArgs(e.args ?? '')
    const isPlaced = await openPane($, tab, job)
    return { text: isPlaced ? 'Studio pane opened.' : 'Studio pane opened; this surface has not placed it yet.' }
  })

  // Matched by name inside the hook: the mod's own tool is in no tool-name type the engine lays.
  on('tool.call', async ($, e, next) => {
    if (String(e.tool) !== `mcp__studio__${TOOL}`) return next(e)
    const input = e as unknown as { tab?: string; job?: string }
    const isPlaced = await openPane($, input.tab ?? '', input.job ?? '')
    return { result: isPlaced ? 'The Studio pane is open beside the chat.' : 'The Studio pane is opened; the surface has not placed it yet.' }
  }).catch(($, e, next) => (next.called || String(e.tool) !== `mcp__studio__${TOOL}` ? next(e) : { result: 'The Studio pane could not open.' }))

  on('agent.spawn', async ($, e, next) => {
    const started = await next(e)
    if (started.deny !== undefined) return started
    const run: StudioRun = {
      id: started.agentId ?? e.tool_use_id,
      type: e.subagentType,
      description: e.description,
      model: started.model,
      job: jobOf(e.prompt),
      start: await $.clock.now(),
      end: null,
      tokens: 0,
    }
    await update($, runsA, runs => [...runs.filter(r => r.id !== run.id), run].slice(-300))
    return started
  }).catch(($, e, next) => next(e))

  on('turn.complete', async ($, e, next) => {
    const id = e.agentId
    if (id !== undefined) {
      const now = await $.clock.now()
      const u = e.usage
      const tokens = u ? (u.input_tokens ?? 0) + (u.cache_read_input_tokens ?? 0) + (u.cache_creation_input_tokens ?? 0) : 0
      await update($, runsA, runs =>
        runs.some(r => r.id === id) ? runs.map(r => (r.id === id ? { ...r, end: now, tokens: r.tokens + tokens } : r)) : runs,
      )
    }
    return next(e)
  })

  on('ui.close', async ($, e, next) => {
    if (e.id === PANE) await update($, openA, () => false)
    return next(e)
  }).catch(($, e, next) => next(e))

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const ui = $.ui.resolve(e)
    const { Box, Text, Button } = ui
    const Svg = 'Svg' in ui ? ui.Svg : undefined
    const [tab, pickedJob, runs, agents, roles, desk, usage] = await Promise.all([
      read($, tabA),
      read($, jobA),
      read($, runsA),
      read($, agentsA),
      read($, rolesA),
      read($, deskA),
      read($, usageA),
    ])
    const now = await $.clock.now()
    const px = Math.max(320, e.props.bodyColumns * 8)
    const picture = (source: string, alt: string, width: number) =>
      Svg && source ? <Svg source={source} alt={alt} width={Math.min(width, px)} isInteractive /> : <Text dimColor>{alt}</Text>

    const tabs = (
      <Box flexDirection="row" gap={1} alignItems="center">
        <Button key="tab-floor" label="Floor" variant={tab === 'floor' ? 'primary' : 'secondary'} onPress={() => update($, tabA, () => 'floor')} />
        <Button key="tab-flow" label="Flow" variant={tab === 'flow' ? 'primary' : 'secondary'} onPress={() => update($, tabA, () => 'flow')} />
        <Text dimColor size="caption">
          {usage.at ? `usage ${hhmm(usage.at)}` : 'usage loading'}
        </Text>
      </Box>
    )
    if (!isKit) {
      return (
        <Box flexDirection="column" gap={1}>
          <Text>This folder is not a Studio Kit repository (no tools/usage_report.py or knowledge/jobs/active.md).</Text>
        </Box>
      )
    }

    if (tab === 'floor') {
      const role = (type: string) => roles.find(r => r.name === type.replace(/^[^:]+:/, ''))
      const figures: Figure[] = agents
        .filter(a => ACTIVE.has(a.status))
        .map(a => {
          const run = runs.find(r => r.id === a.id)
          return {
            id: a.id,
            type: a.type,
            model: run?.model || role(a.type)?.model || '',
            effort: role(a.type)?.effort ?? '',
            status: a.status,
            job: run?.job ?? '',
            description: a.description,
          }
        })
      const listed = new Set(agents.map(a => a.id))
      for (const run of runs) {
        if (run.end !== null || listed.has(run.id)) continue
        figures.push({ id: run.id, type: run.type, model: run.model, effort: role(run.type)?.effort ?? '', status: 'running', job: run.job, description: run.description })
      }
      const running = figures.filter(f => f.status === 'running').length
      const deskJobs = desk.filter(d => d.items.length > 0 || d.status)
      return (
        <Box flexDirection="column" gap={1}>
          {tabs}
          <Text>
            {figures.length === 0 ? 'No agent runs now.' : `${running} running · ${figures.length - running} waiting`}
          </Text>
          {picture(fit(floorSvg(figures, roles)), figures.map(f => `${f.type} (${f.status})`).join(', ') || 'Empty studio floor', 920)}
          {figures.length > 0 && (
            <Box flexDirection="row" flexWrap="wrap" gap={1}>
              {figures.map(f => (
                <Button key={`view-${f.id}`} plain onPress={() => $.ui.view({ agentId: f.id })}>
                  {short(f.type, 20)} <Text dimColor>{short(f.description, 30)}</Text>
                </Button>
              ))}
            </Box>
          )}
          <Text bold>Owner's desk</Text>
          {deskJobs.length === 0 && <Text dimColor>No active jobs.</Text>}
          {deskJobs.map(d => (
            <Box key={`desk-${d.job}`} flexDirection="column">
              <Text>
                <Text bold>{d.job}</Text> {d.title}
              </Text>
              {d.status && <Text dimColor>{d.status}</Text>}
              {d.items.map((item, i) => (
                <Box key={`item-${d.job}-${i}`} flexDirection="row" gap={1} alignItems="center">
                  <Text color={item.kind === 'gate' ? 'yellow' : 'red'}>{item.kind === 'gate' ? 'gate' : 'needs-decision'}</Text>
                  <Text>{item.text}</Text>
                  <Button key={`open-${d.job}-${i}`} label="Open" onPress={() => openFile($, item.file)} />
                </Box>
              ))}
            </Box>
          ))}
        </Box>
      )
    }

    // Flow: one job at a time.
    const latest = new Map<string, number>()
    for (const a of usage.agents) latest.set(a.job, Math.max(latest.get(a.job) ?? 0, Date.parse(a.last)))
    for (const r of runs) if (r.job) latest.set(r.job, Math.max(latest.get(r.job) ?? 0, r.end ?? now))
    const activeJobs = new Set(desk.map(d => d.job))
    const jobs = [...latest.entries()]
      .sort((a, b) => Number(activeJobs.has(b[0])) - Number(activeJobs.has(a[0])) || b[1] - a[1])
      .map(([job]) => job)
      .slice(0, 10)
    const job = pickedJob || jobs[0] || ''
    const deskJob = desk.find(d => d.job === job)
    const flow = buildFlow(job, usage.agents, usage.sessions, runs, deskJob?.gates ?? [], now)
    return (
      <Box flexDirection="column" gap={1}>
        {tabs}
        <Box flexDirection="row" flexWrap="wrap" gap={1}>
          {jobs.map(j => (
            <Button key={`job-${j}`} label={j} variant={j === job ? 'primary' : 'secondary'} onPress={() => update($, jobA, () => j)} />
          ))}
        </Box>
        {usage.error && <Text color="red">usage report failed: {usage.error}</Text>}
        {!job && <Text dimColor>No job has runs in the usage report yet.</Text>}
        {job && (
          <Text>
            <Text bold>{job}</Text> {deskJob?.title ?? ''} · {flow.bars.length} {flow.bars.length === 1 ? 'run' : 'runs'} · read {mtok(flow.read)} · wall {span(flow.t1 - flow.t0)} · agents active{' '}
            {span(flow.active)}
          </Text>
        )}
        {flow.bars.length > 0 && picture(fit(flowSvg(flow, roles)), `Flow map of ${job}: ${flow.lanes.join(', ')}`, 760)}
        {flow.flags.map((flag, i) => (
          <Text key={`flag-${i}`} color="yellow">
            ⚑ {flag}
          </Text>
        ))}
        {flow.bars.length > 0 && (
          <Text dimColor size="caption">
            Bar width = wall time, shade = tokens read (darker = more), red edge = past 500k context, dashed edge = running now. Gates sit in the
            longest idle gap on their date (the card gives no time). Gaps over 90 min are drawn as breaks.
          </Text>
        )}
      </Box>
    )
  })
}

async function openFile($: EngineInterface, file: string): Promise<void> {
  const path = `${cwd.replace(/[\\/]$/, '')}/${file}`.replace(/\//g, cwd.includes('\\') ? '\\' : '/')
  await $.process.run([cwd.includes('\\') ? 'explorer.exe' : 'xdg-open', path]).catch(() => undefined)
}
