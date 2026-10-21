import json,sys,collections
S='show/'
def load(m):
    d=json.load(open(S+m+'.json')); out=collections.defaultdict(dict)
    for p in d['points']:
        k=','.join(f"{s['value']}" for s in p['series']) or 'total'
        out[k][p['bucket_time_utc'][:10]]=(p['value'],p['point_status'],p['final'])
    return out
ms=sys.argv[1:]
for m in ms:
    o=load(m); print('==',m)
    for k,v in o.items():
        print(' ',k)
        print('   ',' '.join(f"{d[5:]}:{x[0]}{'*' if not x[2] else ''}" for d,x in sorted(v.items())))
