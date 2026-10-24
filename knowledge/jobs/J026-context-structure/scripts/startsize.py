import re,sys,pathlib
root=pathlib.Path(sys.argv[1])
def tok(s): return round(len(s)/3.8)
def fm(t):
    m=re.match(r'^---\n(.*?)\n---\n',t,re.S); return (m.group(1),t[m.end():]) if m else ('',t)
always=0
for f in ['CLAUDE.md','AGENTS.md','rules/assistants/claude.md']:
    always+=tok((root/f).read_text(encoding='utf-8'))
print('always-loaded (CLAUDE+imports) tok',always)
print('role | body_tok | skills | skills_tok | mem_tok | total | docs-rule line/total | "docs" mentions')
for f in sorted((root/'.claude/agents').glob('*.md')):
    t=f.read_text(encoding='utf-8'); h,b=fm(t)
    sk=re.search(r'^skills:\s*(.*)$',h,re.M); sks=[]
    if sk:
        v=sk.group(1).strip()
        if v.startswith('['): v=v.strip('[]')
        sks=[x.strip().strip('"\'') for x in v.split(',') if x.strip()]
    if not sks:
        # yaml list form
        m=re.search(r'^skills:\s*\n((?:\s+-\s*.*\n)+)',h+'\n',re.M)
        if m: sks=[l.split('-',1)[1].strip() for l in m.group(1).splitlines()]
    st=0
    for s in sks:
        p=root/'.claude/skills'/s/'SKILL.md'
        if p.exists(): st+=tok(p.read_text(encoding='utf-8'))
    mem=root/'.claude/agent-memory'/f.stem/'MEMORY.md'
    mt=tok('\n'.join(mem.read_text(encoding='utf-8').splitlines()[:200])) if mem.exists() else 0
    lines=b.splitlines()
    dl=[i+1 for i,l in enumerate(lines) if re.search(r'docs-map|Roblox docs|roblox-creator-docs|docs mirror',l)]
    print(f"{f.stem} | {tok(b)} | {','.join(sks)} | {st} | {mt} | {always+tok(b)+st+mt} | {dl[:4]}/{len(lines)} | {len(dl)}")
