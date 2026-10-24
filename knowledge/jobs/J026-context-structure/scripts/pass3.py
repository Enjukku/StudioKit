import json,glob,os,re,collections
fs=glob.glob(os.path.expanduser('~/.claude/projects/C--Users-Firew-Downloads-uterd-GreatWallSim*/*/subagents/agent-*.jsonl'))
K={'docs':re.compile(r'roblox-creator-docs|_api-reference',re.I),'docsmap':re.compile('docs-map'),'company':re.compile(r'rules.{1,3}company\.md'),
   'messages':re.compile(r'rules.{1,3}messages\.md'),'skillref':re.compile(r'skills.{1,3}[\w-]+.{1,3}references',re.I),'packet':re.compile('context_packet'),
   'overlay':re.compile(r'knowledge.{1,3}overlays'),'mcpdocs':re.compile('rbx-docs|docs-search',re.I)}
rows=[]
for f in fs:
    mp=f[:-6]+'.meta.json'; meta=json.load(open(mp)) if os.path.exists(mp) else {}
    at=meta.get('agentType','?'); first=None; calls=[]
    for line in open(f,encoding='utf-8',errors='replace'):
        e=json.loads(line); c=(e.get('message') or {}).get('content')
        if e.get('type')=='user' and first is None: first=c if isinstance(c,str) else json.dumps(c)
        if e.get('type')=='assistant' and isinstance(c,list):
            for x in c:
                if x.get('type')=='tool_use' and x['name']!='SubagentHandback': calls.append(x['name']+' '+json.dumps(x.get('input')))
    blob='\n'.join(calls)
    r={k:bool(p.search(blob)) for k,p in K.items()}
    r.update(at=at,n=len(calls),brief_docs=bool(re.search(r'roblox-creator-docs|docs-map|_api-reference|Roblox docs',first or '',re.I)),blen=len(first or ''),
             engine=bool(re.search(r'\.luau|Luau|ParticleEmitter|Animator|RemoteEvent|Studio|TweenService|Workspace',first or '')))
    rows.append(r)
by=collections.defaultdict(list)
for r in rows: by[r['at']].append(r)
cols=['docs','docsmap','skillref','packet','company','messages','overlay','mcpdocs']
print('role | n | '+' | '.join(cols)+' | brief names docs | median brief chars')
for at,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    bl=sorted(r['blen'] for r in rs)
    print(at,'|',len(rs),'|',' | '.join(str(sum(r[c] for r in rs)) for c in cols),'|',sum(r['brief_docs'] for r in rs),'|',bl[len(bl)//2])
T=len(rows); print('ALL',T,{c:sum(r[c] for r in rows) for c in cols},'brief_docs',sum(r['brief_docs'] for r in rows))
kit=[r for r in rows if r['at'] not in ('general-purpose','Explore','ui-artist','?')]
e=[r for r in kit if r['engine']]
a=[r for r in e if r['brief_docs']]; b=[r for r in e if not r['brief_docs']]
print('kit roles, engine-touching briefs:',len(e),'| brief names docs -> opened docs',sum(r['docs'] for r in a),'/',len(a),'| brief silent -> opened docs',sum(r['docs'] for r in b),'/',len(b))
