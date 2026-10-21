"""Reads calc/show/*.json (saved `analytics.py show` outputs, pulls da92f66a1c21 weekly, aeb68b544ba4 performance, 3a0a68c06b50 adhoc). Writes weekly-numbers.json."""
import json,datetime as dt
def load(m):
    d=json.load(open(f'show/{m}.json')); out={}
    for p in d['points']:
        k=','.join(s['value'] for s in p['series']) or 'total'
        out.setdefault(k,{})[p['bucket_time_utc'][:10]]=p['value']
    return out
def days(a,b):
    a=dt.date.fromisoformat(a);b=dt.date.fromisoformat(b)
    return [(a+dt.timedelta(i)).isoformat() for i in range((b-a).days+1)]
W={'B_before_video_and_v112':('2026-09-22','2026-09-28'),'P_prior_week':('2026-10-06','2026-10-12'),'T_target_week':('2026-10-13','2026-10-19')}
R={}
dau=load('DailyActiveUsers')
def s(m,k,a,b): return sum(load_[m][k][d] for d in days(a,b))
load_={m:load(m) for m in ['DailyActiveUsers','DailyRevenue','PayingUsers','ForwardD1Retention','ForwardD7Retention','ClientCrashCount','OomUnexpectedExits','ClientCrashRate15m','ClientFpsP10','ClientMemoryUsageP90','PeakConcurrentPlayers','AveragePlayTimeMinutesPerDAU','Visits','AverageSessionLengthMinutes']}
for w,(a,b) in W.items():
    r={}
    r['dau_player_days_total']=s('DailyActiveUsers','total',a,b)
    r['dau_player_days_new']=s('DailyActiveUsers','true',a,b)
    r['dau_player_days_returning']=s('DailyActiveUsers','false',a,b)
    r['visits']=s('Visits','total',a,b)
    if a>='2026-09-25':
        for k in ['Friends','HomeRecommendations','Other','Search','Phone','Computer','Console','Tablet']:
            r['dau_pd_'+k]=s('DailyActiveUsers',k,a,b)
        r['client_crash_count']=s('ClientCrashCount','total',a,b)
        r['oom_exits']=s('OomUnexpectedExits','total',a,b)
    r['playtime_min_per_dau_range']=[min(load_['AveragePlayTimeMinutesPerDAU']['total'][d] for d in days(a,b)),max(load_['AveragePlayTimeMinutesPerDAU']['total'][d] for d in days(a,b))]
    r['session_len_min_range']=[min(load_['AverageSessionLengthMinutes']['total'][d] for d in days(a,b)),max(load_['AverageSessionLengthMinutes']['total'][d] for d in days(a,b))]
    # revenue final days only (10-19 is Projected)
    rb=b if b<'2026-10-19' else '2026-10-18'
    r['revenue_days']=[a,rb]; r['daily_revenue_sum_final_days']=s('DailyRevenue','total',a,rb)
    r['paying_users_range_final_days']=[min(load_['PayingUsers']['total'][d] for d in days(a,rb)),max(load_['PayingUsers']['total'][d] for d in days(a,rb))]
    # D1 readable cohorts only (last readable first-play 2026-10-18)
    db=min(b,'2026-10-18')
    d1=[load_['ForwardD1Retention']['total'][d] for d in days(a,db)]
    r['d1_cohorts']=[a,db]; r['d1_range']=[min(d1),max(d1)]
    new=[dau['true'][d] for d in days(a,db)]
    r['d1_new_players_cohort_proxy_sum']=sum(new)
    r['d1_est_returned']=round(sum(x*n for x,n in zip(d1,new)))
    r['d1_weighted_rate_est']=round(r['d1_est_returned']/sum(new),4)
    # D7 readable cohorts only (last readable first-play 2026-10-12)
    if a<='2026-10-12':
        e=min(b,'2026-10-12'); d7=[load_['ForwardD7Retention']['total'][d] for d in days(a,e)]
        newd=[dau['true'][d] for d in days(a,e)]
        r['d7_cohorts']=[a,e]; r['d7_range']=[min(d7),max(d7)]
        r['d7_new_players_proxy_sum']=sum(newd); r['d7_est_returned']=round(sum(x*n for x,n in zip(d7,newd))); r['d7_weighted_rate_est']=round(r['d7_est_returned']/sum(newd),4)
    R[w]=r
# phone / performance ranges, by phase
ph={'pre_both_09-25..10-03':('2026-09-25','2026-10-03'),'video_only_v111_10-04..10-08':('2026-10-04','2026-10-08'),'video_v112_10-13..10-18':('2026-10-13','2026-10-18')}
P={}
for n,(a,b) in ph.items():
    P[n]={}
    for plat in ['Phone','Computer','Console','Tablet']:
        d1=[load('ForwardD1Retention')[plat][d] for d in days(a,b)]
        f=[load_['ClientFpsP10'].get(plat,{}).get(d) for d in days(a,b)]
        cr=[load_['ClientCrashRate15m'][plat][d] for d in days(a,b)]
        P[n][plat]={'d1_range':[min(d1),max(d1)],'fps_p10_range':[min(f),max(f)],'crash_rate_range':[min(cr),max(cr)]}
    c=[load_['ClientCrashCount']['total'][d] for d in days(max(a,'2026-09-25'),b)]
    P[n]['crash_count_per_day_range']=[min(c),max(c)]
    o=[load_['OomUnexpectedExits']['total'][d] for d in days(a,b)]
    P[n]['oom_per_day_range']=[min(o),max(o)]
    m=[load_['ClientMemoryUsageP90']['total'][d] for d in days(a,b)]
    P[n]['mem_p90_range']=[min(m),max(m)]
R['phases']=P
# source D1 (Other) and new-player step on 10-04
R['video_day']={'new_players_10-03':dau['true']['2026-10-03'],'new_players_10-04':dau['true']['2026-10-04'],'other_dau_10-03':dau['Other']['2026-10-03'],'other_dau_10-04':dau['Other']['2026-10-04'],'d1_total_10-03':load('ForwardD1Retention')['total']['2026-10-03'],'d1_total_10-04':load('ForwardD1Retention')['total']['2026-10-04'],'d1_other_10-03':load('ForwardD1Retention')['Other']['2026-10-03'],'d1_other_10-04':load('ForwardD1Retention')['Other']['2026-10-04'],'d1_other_10-12..10-18_range':[min(load('ForwardD1Retention')['Other'][d] for d in days('2026-10-13','2026-10-18')),max(load('ForwardD1Retention')['Other'][d] for d in days('2026-10-13','2026-10-18'))]}
json.dump(R,open('weekly-numbers.json','w'),indent=1)
print(json.dumps(R,indent=1))
