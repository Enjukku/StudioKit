// SVG text for the floor and the flow map. Plain strings: the pane's Svg element draws them (≤ 131,072 characters).

import type { StudioRole } from '../types'
import { effortPips, type Flow, hhmm, modelLetter, ROOMS, roomOf, short, span } from './model'

export const SVG_LIMIT = 131_072

/** The role files' `color:` names (8 in the kit) as fills. */
const COLORS: Record<string, string> = {
  green: '#3f9d5a',
  cyan: '#2a9fb5',
  orange: '#e08a2c',
  purple: '#8a5cc7',
  yellow: '#d2ad1c',
  blue: '#3b6fd1',
  pink: '#d6609b',
  red: '#d0453f',
}
const GREY = '#8a8f98'
const INK = '#2b2a28'
const PAPER = '#f6f3ec'
const WALL = '#cfc8b8'

export function esc(text: string): string {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

export function colorOf(type: string, roles: StudioRole[]): string {
  const role = roles.find(r => r.name === type.replace(/^[^:]+:/, ''))
  return COLORS[role?.color ?? ''] ?? GREY
}

/** Hat per role (feasibility page, "Agent figures"); drawn over a body of radius 15 at (0, 0). */
const HATS: Record<string, string> = {
  orchestrator: `<rect x="-11" y="-20" width="22" height="7" rx="2" fill="${INK}"/><rect x="-14" y="-14" width="28" height="3" fill="${INK}"/>`,
  'game-designer': `<path d="M-12,-9 A12,10 0 0 1 12,-9 Z" fill="#c0392b"/><rect x="-20" y="-10" width="10" height="3" rx="1" fill="#c0392b"/>`,
  'art-director': `<ellipse cx="-2" cy="-14" rx="13" ry="5" fill="${INK}"/><circle cx="-2" cy="-19" r="2" fill="${INK}"/>`,
  'film-director': `<ellipse cx="2" cy="-14" rx="13" ry="5" fill="#7a2230"/><circle cx="2" cy="-19" r="2" fill="#7a2230"/>`,
  architect: `<path d="M-13,-8 A13,12 0 0 1 13,-8 Z" fill="#f1c40f"/><rect x="-16" y="-9" width="32" height="3" rx="1" fill="#e1b40a"/>`,
  'feature-builder': `<rect x="-11" y="-21" width="22" height="9" rx="3" fill="#5d6d7e"/><rect x="-7" y="-19" width="14" height="4" fill="#2c3e50"/>`,
  'quick-builder': `<rect x="-15" y="-11" width="30" height="4" rx="2" fill="#e74c3c"/>`,
  reviewer: `<circle cx="-5" cy="-15" r="4" fill="none" stroke="${INK}" stroke-width="1.5"/><circle cx="5" cy="-15" r="4" fill="none" stroke="${INK}" stroke-width="1.5"/><line x1="-1" y1="-15" x2="1" y2="-15" stroke="${INK}"/>`,
  'qa-lead': `<path d="M-13,-8 A13,12 0 0 1 13,-8 Z" fill="#ecf0f1" stroke="${INK}" stroke-width="0.8"/><rect x="-15" y="-9" width="30" height="3" fill="#bdc3c7"/>`,
  modeler: `<path d="M-12,-9 A12,9 0 0 1 12,-9 Z" fill="#a0522d"/>`,
  'character-rigger': `<path d="M-13,-8 A13,12 0 0 1 13,-8 Z" fill="#7f8c8d"/><circle cx="0" cy="-16" r="3" fill="#ffe066"/>`,
  animator: `<rect x="-15" y="-12" width="30" height="5" rx="2" fill="#16a085"/>`,
  'vfx-designer': `<rect x="-15" y="-8" width="30" height="3" fill="${INK}"/><circle cx="-6" cy="-6" r="4.5" fill="#9be7ff" stroke="${INK}"/><circle cx="6" cy="-6" r="4.5" fill="#9be7ff" stroke="${INK}"/>`,
  'sound-designer': `<path d="M-15,-2 A15,15 0 0 1 15,-2" fill="none" stroke="${INK}" stroke-width="3"/><rect x="-18" y="-4" width="5" height="9" rx="2" fill="${INK}"/><rect x="13" y="-4" width="5" height="9" rx="2" fill="${INK}"/>`,
  'environment-designer': `<ellipse cx="0" cy="-11" rx="19" ry="3.5" fill="#b9935a"/><path d="M-10,-11 A10,9 0 0 1 10,-11 Z" fill="#c8a46a"/>`,
  'ui-ux-designer': `<rect x="10" y="-20" width="4" height="16" rx="1" fill="#f39c12" transform="rotate(25 12 -12)"/>`,
}

export type Figure = {
  id: string
  type: string
  model: string
  effort: string
  status: string
  job: string
  description: string
}

const FIG_W = 76
const FIG_H = 74
const PER_ROW = 3
const ROOM_W = FIG_W * PER_ROW + 8
const COLS = 4

function figureSvg(f: Figure, x: number, y: number, roles: StudioRole[], showJob: boolean): string {
  const fill = colorOf(f.type, roles)
  const isWaiting = f.status === 'waiting' || f.status === 'pending' || f.status === 'idle'
  const isFailed = f.status === 'failed' || f.status === 'killed'
  const name = short(f.type.replace(/^[^:]+:/, ''), 15)
  const pips = effortPips(f.effort)
  const bob = f.status === 'running'
    ? `<animateTransform attributeName="transform" type="translate" values="0 0; 0 -2.5; 0 0" dur="${(0.9 + (f.id.length % 5) * 0.12).toFixed(2)}s" repeatCount="indefinite"/>`
    : ''
  const label = `${f.type} · ${f.status}${f.job ? ` · ${f.job}` : ''}\n${f.description}\n${f.model}${f.effort ? ` · ${f.effort}` : ''}`
  return [
    `<g transform="translate(${x},${y})" opacity="${isWaiting ? 0.55 : 1}"><title>${esc(label)}</title>`,
    `<text x="0" y="-30" text-anchor="middle" font-size="10" fill="${INK}">${esc(name)}</text>`,
    showJob && f.job ? `<text x="0" y="-41" text-anchor="middle" font-size="8" fill="${GREY}">${esc(f.job)}</text>` : '',
    `<g>${bob}`,
    `<ellipse cx="0" cy="17" rx="13" ry="3" fill="#0002"/>`,
    `<circle cx="0" cy="0" r="15" fill="${fill}" stroke="${INK}" stroke-width="1"/>`,
    `<circle cx="-11" cy="9" r="3" fill="${fill}" stroke="${INK}" stroke-width="0.8"/><circle cx="11" cy="9" r="3" fill="${fill}" stroke="${INK}" stroke-width="0.8"/>`,
    isWaiting
      ? `<line x1="-8" y1="-3" x2="-2" y2="-3" stroke="${INK}" stroke-width="1.5"/><line x1="2" y1="-3" x2="8" y2="-3" stroke="${INK}" stroke-width="1.5"/>`
      : `<circle cx="-5" cy="-3" r="3.6" fill="#fff"/><circle cx="5" cy="-3" r="3.6" fill="#fff"/><circle cx="-4.4" cy="-2.6" r="1.7" fill="${INK}"/><circle cx="5.6" cy="-2.6" r="1.7" fill="${INK}"/>`,
    HATS[f.type.replace(/^[^:]+:/, '')] ?? '',
    `<circle cx="0" cy="8" r="5" fill="#fff" stroke="${INK}" stroke-width="0.6"/><text x="0" y="10.6" text-anchor="middle" font-size="7" font-weight="bold" fill="${INK}">${modelLetter(f.model)}</text>`,
    Array.from({ length: pips }, (_, i) => `<circle cx="${(i - (pips - 1) / 2) * 4}" cy="25" r="1.4" fill="${INK}"/>`).join(''),
    `</g>`,
    isWaiting ? `<text x="14" y="-14" font-size="9" fill="${GREY}">zz</text>` : '',
    isFailed ? `<text x="12" y="-10" font-size="13" font-weight="bold" fill="#d0453f">!</text>` : '',
    `</g>`,
  ].join('')
}

/** The floor plan: 8 rooms in 2 rows of 4, each figure in its craft's room. */
export function floorSvg(figures: Figure[], roles: StudioRole[]): string {
  const byRoom = new Map(ROOMS.map(room => [room.id, [] as Figure[]]))
  for (const f of figures) byRoom.get(roomOf(f.type))?.push(f)
  const showJob = new Set(figures.map(f => f.job).filter(Boolean)).size > 1
  const rowsIn = (ids: string[]): number => Math.max(1, ...ids.map(id => Math.ceil((byRoom.get(id)?.length ?? 0) / PER_ROW)))
  const top = ROOMS.slice(0, COLS).map(r => r.id)
  const bottom = ROOMS.slice(COLS).map(r => r.id)
  const heights = [26 + rowsIn(top) * FIG_H, 26 + rowsIn(bottom) * FIG_H] as const
  const width = ROOM_W * COLS
  const height = heights[0] + heights[1]
  const parts = [
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" font-family="system-ui, sans-serif">`,
    `<rect x="0" y="0" width="${width}" height="${height}" rx="8" fill="${PAPER}"/>`,
  ]
  ROOMS.forEach((room, i) => {
    const col = i % COLS
    const row = Math.floor(i / COLS)
    const x = col * ROOM_W
    const y = row === 0 ? 0 : heights[0]
    const h = row === 0 ? heights[0] : heights[1]
    const list = byRoom.get(room.id) ?? []
    parts.push(
      `<rect x="${x + 2}" y="${y + 2}" width="${ROOM_W - 4}" height="${h - 4}" rx="6" fill="none" stroke="${WALL}" stroke-width="2"/>`,
      `<text x="${x + 10}" y="${y + 16}" font-size="9" font-weight="bold" letter-spacing="1" fill="${list.length ? INK : GREY}">${esc(room.label)}${list.length ? ` · ${list.length}` : ''}</text>`,
    )
    list.forEach((f, k) => {
      const fx = x + 4 + FIG_W / 2 + (k % PER_ROW) * FIG_W
      const fy = y + 26 + Math.floor(k / PER_ROW) * FIG_H + 42
      parts.push(figureSvg(f, fx, fy, roles, showJob))
    })
  })
  parts.push('</svg>')
  return parts.join('')
}

const LANE_H = 22
const LABEL_W = 118
const BREAK_W = 26
const FLOW_W = 760

/** The flow map: a lane per role, a bar per run (width = wall time, shade = tokens read), gates dashed. */
export function flowSvg(flow: Flow, roles: StudioRole[]): string {
  const plotW = FLOW_W - LABEL_W - 10
  const breaks = flow.pieces.filter(p => p.isBreak).length
  const linear = flow.pieces.filter(p => !p.isBreak).reduce((n, p) => n + (p.t1 - p.t0), 0) || 1
  const scale = (plotW - breaks * BREAK_W) / linear
  const x = (t: number): number => {
    let at = LABEL_W
    for (const p of flow.pieces) {
      const w = p.isBreak ? BREAK_W : (p.t1 - p.t0) * scale
      if (t <= p.t1) return at + (p.t1 > p.t0 ? Math.max(0, t - p.t0) / (p.t1 - p.t0) : 0) * w
      at += w
    }
    return at
  }
  const top = 22
  const height = top + flow.lanes.length * LANE_H + 26
  const maxRead = Math.max(1, ...flow.bars.map(b => b.read))
  const shade = (read: number): number => 0.25 + 0.75 * (Math.log10(1 + read) / Math.log10(1 + maxRead))
  const parts = [
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${FLOW_W} ${height}" width="${FLOW_W}" height="${height}" font-family="system-ui, sans-serif">`,
    `<rect x="0" y="0" width="${FLOW_W}" height="${height}" rx="8" fill="${PAPER}"/>`,
  ]
  flow.lanes.forEach((lane, i) => {
    const y = top + i * LANE_H
    parts.push(
      i % 2 ? '' : `<rect x="4" y="${y}" width="${FLOW_W - 8}" height="${LANE_H}" fill="#0000000a"/>`,
      `<text x="10" y="${y + 15}" font-size="10" fill="${INK}">${esc(short(lane, 20))}</text>`,
    )
  })
  // Time ticks at each piece start; breaks get a zigzag and their length.
  let at = LABEL_W
  let lastTick = -99
  for (const p of flow.pieces) {
    const w = p.isBreak ? BREAK_W : (p.t1 - p.t0) * scale
    if (p.isBreak) {
      parts.push(
        `<rect x="${at}" y="${top}" width="${w}" height="${flow.lanes.length * LANE_H}" fill="${PAPER}"/>`,
        `<path d="M${at + w / 2 - 3},${top} l6,6 l-6,6 l6,6" fill="none" stroke="${WALL}"/>`,
        `<text x="${at + w / 2}" y="${height - 8}" text-anchor="middle" font-size="8" fill="${GREY}">${esc(span(p.t1 - p.t0))}</text>`,
      )
    } else if (at - lastTick > 44) {
      parts.push(`<text x="${at}" y="14" font-size="8" fill="${GREY}">${hhmm(p.t0)}</text>`)
      lastTick = at
    }
    at += w
  }
  for (const bar of flow.bars) {
    const lane = flow.lanes.indexOf(bar.lane)
    if (lane < 0) continue
    const x0 = x(bar.start)
    const w = Math.max(3, x(bar.end) - x0)
    const y = top + lane * LANE_H + 4
    const fill = bar.lane === 'lead' ? INK : colorOf(bar.lane, roles)
    const tip = `${bar.detail}\n${hhmm(bar.start)}–${hhmm(bar.end)} (${span(bar.end - bar.start)})`
    parts.push(
      `<g><title>${esc(tip)}</title>`,
      `<rect x="${x0.toFixed(1)}" y="${y}" width="${w.toFixed(1)}" height="${LANE_H - 8}" rx="3" fill="${fill}" fill-opacity="${shade(bar.read).toFixed(2)}"`,
      bar.peak > 500_000 ? ` stroke="#d0453f" stroke-width="2"` : bar.isLive ? ` stroke="${INK}" stroke-dasharray="3 2"` : '',
      `/>`,
      w > 70 ? `<text x="${(x0 + 4).toFixed(1)}" y="${y + 10}" font-size="8" fill="#fff">${esc(short(bar.label, Math.floor(w / 5)))}</text>` : '',
      `</g>`,
    )
  }
  for (const gate of flow.gates) {
    const gx = x(gate.t).toFixed(1)
    parts.push(
      `<line x1="${gx}" y1="${top - 4}" x2="${gx}" y2="${top + flow.lanes.length * LANE_H + 4}" stroke="${INK}" stroke-width="1.2" stroke-dasharray="4 3"/>`,
      `<text x="${gx}" y="${height - 8}" text-anchor="middle" font-size="9" font-weight="bold" fill="${INK}">${esc(short(gate.label, 34))}</text>`,
    )
  }
  parts.push('</svg>')
  return parts.join('')
}

/** Drops the `<title>` tooltips when a drawing would pass the Svg limit; "" when it still would. */
export function fit(svg: string): string {
  if (svg.length <= SVG_LIMIT) return svg
  const bare = svg.replace(/<title>[\s\S]*?<\/title>/g, '')
  return bare.length <= SVG_LIMIT ? bare : ''
}
