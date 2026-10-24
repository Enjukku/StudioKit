// The Studio pane's state (J028). Every value the pane draws from lives here.

/** One agent run this session saw start (agent.spawn) and maybe end (turn.complete). */
export type StudioRun = {
  id: string
  type: string
  description: string
  model: string
  job: string
  start: number
  end: number | null
  tokens: number
}

/** One agent of `$.agent.list()`, as last polled. */
export type StudioAgent = {
  id: string
  type: string
  description: string
  status: string
}

/** A role file's frontmatter keys the figures use. */
export type StudioRole = { name: string; color: string; model: string; effort: string }

/** One item on the owner's desk. */
export type StudioDeskItem = { kind: 'gate' | 'decision'; text: string; file: string }

/** One active job as the owner's desk shows it. */
export type StudioDeskJob = {
  job: string
  folder: string
  title: string
  status: string
  items: StudioDeskItem[]
  gates: StudioGate[]
}

/** One row of a job card's Gates table. */
export type StudioGate = { label: string; date: string; rev: string }

/** One agent run of `usage_report.py --json` (agents[]). */
export type StudioUsageRun = {
  id: string
  type: string
  description: string
  model: string
  effort: string
  job: string
  first: string
  last: string
  calls: number
  read: number
  out: number
  peak: number
  session: string
}

/** One main session of `usage_report.py --json` (sessions[]). */
export type StudioUsageSession = {
  session: string
  title: string
  model: string
  job: string
  first: string
  last: string
  calls: number
  read: number
  out: number
  peak: number
}

export type StudioUsage = {
  at: number
  error: string
  agents: StudioUsageRun[]
  sessions: StudioUsageSession[]
}

declare module 'claude-code' {
  interface PluginState {
    studio: {
      open: boolean
      tab: 'floor' | 'flow'
      job: string
      runs: StudioRun[]
      agents: StudioAgent[]
      roles: StudioRole[]
      desk: StudioDeskJob[]
      usage: StudioUsage
    }
  }
}
