import json,glob,os,re,collections
fs=glob.glob(os.path.expanduser('~/.claude/projects/C--Users-Firew-Downloads-uterd-GreatWallSim*/*/subagents/agent-*.jsonl'))
DOCNAME=re.compile(r'([A-Za-z][\w-]+\.(?:md|yaml))')
SECT=('scripting','luau','physics','workspace','players','ui','effects','animation','environment','audio','art','parts','production','cloud','studio','performance-optimization','characters','avatar','input','_api-reference','classes','sound','chat','discovery')
tot=collections.Counter(); byrole=collections.defaultdict(collections.Counter); bad=[]
for f in fs:
    mp=f[:-6]+'.meta.json'; at=json.load(open(mp)).get('agentType','?') if os.path.exists(mp) else '?'
    body=[]; hb=None
    for line in open(f,encoding='utf-8',errors='replace'):
        e=json.loads(line); c=(e.get('message') or {}).get('content')
        if not isinstance(c,list): continue
        for x in c:
            if x.get('type')=='tool_use':
                if x['name']=='SubagentHandback': hb=x['input'].get('message','')
                else: body.append(json.dumps(x['input']))
            elif x.get('type')=='tool_result': body.append(json.dumps(x.get('content'))[:20000])
    if hb is None: continue
    m=re.search(r'docs[_ ]read',hb,re.I)
    if not m: byrole[at]['no_docs_read']+=1; tot['no_docs_read']+=1; continue
    seg=re.split(r'\n\s*\n|\n\**lesson',hb[m.start():m.start()+1800])[0]
    names=set()
    for line in seg.splitlines():
        if any(s in line for s in SECT) or 'roblox-creator-docs' in line:
            for n in DOCNAME.findall(line):
                if n.lower() not in ('docs-map.md','agents.md','skill.md'): names.add(n)
    blob='\n'.join(body).lower()
    missing=[n for n in names if n.lower() not in blob]
    byrole[at]['docs_read']+=1; tot['docs_read']+=1
    if names: byrole[at]['claims_pages']+=1; tot['claims_pages']+=1; tot['pages']+=len(names)
    if missing: byrole[at]['unverified']+=1; tot['unverified']+=1; tot['missing_pages']+=len(missing); bad.append((at,os.path.basename(f)[:24],missing[:4],len(names)))
print(dict(tot))
for r,c in sorted(byrole.items(),key=lambda x:-sum(x[1].values())): print(r,dict(c))
for b in bad: print(b)
