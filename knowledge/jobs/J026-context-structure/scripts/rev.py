import json,glob,os,re,collections
fs=glob.glob(os.path.expanduser('~/.claude/projects/C--Users-Firew-Downloads-uterd-Reverse*/*.jsonl'))+glob.glob(os.path.expanduser('~/.claude/projects/C--Users-Firew-Downloads-uterd-Reverse/*/subagents/*.jsonl'))
P={'docs':r'roblox-creator-docs|_api-reference','docsmap':'docs-map','packet':'context_packet','rolefile':r'(\.agents|\.claude).{1,3}(roles|agents).{1,3}[\w-]+\.md','skillref':r'skills.{1,3}[\w-]+.{1,3}references'}
for f in sorted(fs,key=os.path.getmtime):
    first=None; calls=[]; skills=[]; agents=[]; n_user=0
    for line in open(f,encoding='utf-8',errors='replace'):
        e=json.loads(line); c=(e.get('message') or {}).get('content')
        if e.get('type')=='user' and not e.get('isMeta'):
            t=c if isinstance(c,str) else ' '.join(x.get('text','') for x in (c or []) if isinstance(x,dict) and x.get('type')=='text')
            if t.strip() and first is None and not t.startswith('<'): first=t
        if e.get('type')=='assistant' and isinstance(c,list):
            for x in c:
                if x.get('type')=='tool_use':
                    s=x['name']+' '+json.dumps(x.get('input'))
                    calls.append(s)
                    if x['name']=='Skill': skills.append(x['input'].get('skill'))
                    if x['name']=='Agent': agents.append((x['input'].get('subagent_type'),x['input'].get('model')))
    blob='\n'.join(calls)
    hits={k:len(re.findall(p,blob)) for k,p in P.items()}
    role=re.search(r"(?:as|is) the studio'?s? `?([\w-]+)`?",first or '')
    name=os.path.basename(os.path.dirname(f)) if 'subagents' in f else os.path.basename(os.path.dirname(f))[-30:]
    print(f"{name[:34]:34} calls={len(calls):4} role={role.group(1) if role else '-':20} skills={skills[:5]} agents={agents[:4]} {hits}")
    print('    brief:',(first or '')[:160].replace('\n',' '))
