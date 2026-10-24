import type { AgentInfo } from 'claude-code'
import { describe, expect, mock, test } from 'claude-code/testing'

import { buildFlow, parseActive, parseDesk, roleOf, roomOf } from '../hooks/model'
import { floorSvg, flowSvg, SVG_LIMIT } from '../hooks/svg'
import type { StudioUsageRun } from '../types'

const NOW = Date.parse('2026-10-24T18:00:00Z')
const at = (min: number) => new Date(NOW - 10 * 3600_000 + min * 60_000).toISOString()

const CARD = [
  '| Status | build: step 3 of 5; needs-decision on the reviewer limit |',
  '',
  '## Gates',
  '| Gate | Date | Revision approved | Owner\'s words |',
  '| --- | --- | --- | --- |',
  `| G1 direction | ${at(100).slice(0, 10)} | rev 2 | "yes" |`,
  '| G3 final | | | |',
].join('\n')

const ACTIVE = '# Active jobs\n- J025-base-framework · universal base game framework · linked: J023\n- J028-studio-pane · the Studio pane\n'

function run(id: string, type: string, from: number, to: number, extra: Partial<StudioUsageRun> = {}): StudioUsageRun {
  return {
    id, type, description: `${type} run`, model: 'claude-opus-5-5', effort: 'high', job: 'J025',
    first: at(from), last: at(to), calls: 10, read: 1_000_000, out: 9_000, peak: 120_000, session: 's1', ...extra,
  }
}

const RUNS: StudioUsageRun[] = [
  run('a1', 'architect', 0, 40),
  run('a2', 'feature-builder', 45, 90),
  // 60 min with no agent: the G1 gate lands in this gap.
  run('a3', 'reviewer', 150, 170),
  run('a4', 'qa-lead', 155, 175),
  run('a5', 'art-director', 160, 180, { peak: 610_000 }),
  run('a6', 'feature-builder', 185, 200),
  run('a7', 'feature-builder', 205, 215),
  run('a8', 'feature-builder', 220, 230),
  run('x1', 'reviewer', 0, 10, { job: 'J099' }),
]

describe('kit files', () => {
  test('active jobs, open gates and needs-decision lines reach the owner\'s desk', async () => {
    const [entry] = parseActive(ACTIVE)
    expect(entry).toEqual({ folder: 'J025-base-framework', job: 'J025', title: 'universal base game framework' })
    const desk = parseDesk(entry!, CARD, '| D1 | x | needs-decision: owner picks the package list |')
    expect(desk.status).toMatch(/^build: step 3/)
    // The Status row is shown once, as the status, not again as a needs-decision item.
    expect(desk.items.map(i => i.kind)).toEqual(['gate', 'decision'])
    expect(desk.items[0]).toEqual({ kind: 'gate', text: 'G3 final open', file: 'knowledge/jobs/J025-base-framework/job-card.md' })
    expect(desk.gates.map(g => g.label)).toEqual(['G1 direction', 'G3 final'])
  })

  test('a role without model: gets its tier model from kit.json', async () => {
    const role = roleOf('qa-lead.md', '---\nname: qa-lead\ntier: research\neffort: medium\ncolor: cyan\n---\n', { research: 'sonnet' })
    expect(role).toEqual({ name: 'qa-lead', color: 'cyan', model: 'sonnet', effort: 'medium' })
  })

  test('each role has a room; unknown types go to the helpers', async () => {
    expect(roomOf('vfx-designer')).toBe('fx')
    expect(roomOf('studio:reviewer')).toBe('code')
    expect(roomOf('general-purpose')).toBe('help')
  })
})

describe('flow map', () => {
  const desk = parseDesk(parseActive(ACTIVE)[0]!, CARD, '')
  const flow = buildFlow('J025', RUNS, [], [], desk.gates, NOW)

  test('one lane per role in order of first run, one bar per run of the job', async () => {
    expect(flow.lanes).toEqual(['architect', 'feature-builder', 'reviewer', 'qa-lead', 'art-director'])
    expect(flow.bars.length).toBe(8)
    expect(flow.gates.map(g => g.label)).toEqual(['G1 direction (rev 2)'])
  })

  test('flags: same role 3+ in a stage, 3+ reviewers in a round, a wait on the owner, the 500k mark', async () => {
    expect(flow.flags).toContain('feature-builder ran 3 times in stage 2')
    expect(flow.flags.some(f => f.startsWith('3 reviewers in one round'))).toBe(true)
    expect(flow.flags.some(f => f.startsWith('wait 1 h 00 m on the owner') && f.includes('G1 direction'))).toBe(true)
    expect(flow.flags.some(f => f.includes('passed the 500k context mark'))).toBe(true)
    expect(flow.flags.some(f => f.startsWith('feature-builder ran') && f.endsWith('stage 1'))).toBe(false)
  })

  test('the drawings stay under the Svg limit', async () => {
    expect(flowSvg(flow, []).length).toBeLessThan(SVG_LIMIT)
    const many = Array.from({ length: 40 }, (_, i) => ({ id: `a${i}`, type: 'reviewer', model: 'opus', effort: 'high', status: 'running', job: 'J025', description: 'x'.repeat(200) }))
    expect(floorSvg(many, []).length).toBeLessThan(SVG_LIMIT)
  })
})

const PANE = {
  plugin: 'studio',
  component: 'Pane',
  requestId: 'studio',
  props: { title: 'Studio', isFocused: false, bodyColumns: 100, placement: 'dock', scroll: { offset: 0, bodyRows: 40 }, view: {} },
} as const

test('the pane shows a live agent on the floor and a job on the flow tab', async ($, on) => {
  const clock = mock.clock(on, { now: NOW })
  const files: Record<string, string> = {
    '.agents/roles/reviewer.md': '---\nname: reviewer\ncolor: red\nmodel: opus\neffort: high\n---\n',
    'knowledge/jobs/active.md': ACTIVE,
    'knowledge/jobs/J025-base-framework/job-card.md': CARD,
  }
  let agents: AgentInfo[] = [{ id: 'a9', type: 'reviewer', description: 'Review the save module', status: 'running' }]
  on('fs.exists', () => ({ value: true }))
  on('fs.list', () => ({ value: [{ name: 'reviewer.md', kind: 'file', size: 1, mtimeMs: 0, isLink: false }] }))
  // The test's working directory is the mod folder: files are matched by their path in the repository.
  const file = (path: string) => Object.entries(files).find(([name]) => path.replace(/\\/g, '/').endsWith(name))?.[1] ?? ''
  on('fs.read', (_, e) => ({ value: file(e.path) }))
  on('command.register', () => ({ value: { command: 'studio' } }))
  on('tool.register', () => ({ value: { tool: 'mcp__studio__open_pane' } }))
  on('agent.list', () => ({ value: agents }))
  on('agent.spawn', () => ({ model: 'claude-sonnet-5-5', agentId: 'a9' }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('process.run', () => ({
    value: { exitCode: 0, stdout: JSON.stringify({ agents: RUNS, sessions: [] }), stderr: '', isStdoutTruncated: false, isStderrTruncated: false },
  }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))

  await $.session.start({ cwd: 'C:\\repo', surface: 'desktop', isInteractive: true })
  await $.agent.spawn({
    tool_use_id: 't1',
    prompt: 'Review it. --role reviewer --job J028-studio-pane',
    description: 'Review the save module',
    subagentType: 'reviewer',
    provider: { plugin: 'engine', tier: 'core' },
    parentModel: 'claude-opus-5-5',
    background: true,
    fork: false,
  })
  await $.command.run({ command: 'studio', args: '', origin: { kind: 'composer' }, presentation: { isFullscreen: true, columns: 200 } })
  await clock.advance(3_000)

  for (const surface of ['desktop', 'terminal'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface })
    expect((await ui.find({ type: 'Text', text: /1 running/ }))?.text).toBe('1 running · 0 waiting')
    expect(await ui.find({ key: 'view-a9' })).toBeDefined()
    expect(await ui.find({ type: 'Text', text: /G3 final open/ })).toBeDefined()
    await ui.unmount()
  }

  const ui = await $.ui.mount({ ...PANE, surface: 'desktop' })
  await ui.press({ key: 'tab-flow' })
  expect((await ui.find({ type: 'Text', text: /^J028/ }))?.text).toMatch(/· 1 run ·/) // the newest active job shows first: the live run
  await ui.press({ key: 'job-J025' })
  expect(await ui.find({ type: 'Text', text: /feature-builder ran 3 times/ })).toBeDefined()
  expect((await ui.find({ type: 'Svg' }))?.props.alt).toMatch(/^Flow map of J025/)
  await ui.unmount()

  // The agent finishes: it leaves the floor at the next poll.
  agents = [{ ...agents[0]!, status: 'completed' }]
  await clock.advance(3_000)
  const after = await $.ui.mount({ ...PANE, surface: 'desktop' })
  await after.press({ key: 'tab-floor' })
  expect(await after.find({ type: 'Text', text: /No agent runs now/ })).toBeDefined()
  await after.unmount()
})
