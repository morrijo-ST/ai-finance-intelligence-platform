import numpy as np
import pandas as pd

def generate_finance_data(seed=42):
    rng=np.random.default_rng(seed)
    months=pd.date_range("2025-01-01","2026-12-01",freq="MS")
    regions=["North America","Europe","Asia Pacific","Middle East & Africa"]
    bus=["Core Software","Digital Operations","Industrial AI"]
    rows=[]
    for m in months:
        for reg in regions:
            for bu in bus:
                base={"Core Software":8.5e6,"Digital Operations":5.2e6,"Industrial AI":3.6e6}[bu]
                rm={"North America":1.25,"Europe":0.9,"Asia Pacific":0.75,"Middle East & Africa":0.45}[reg]
                season=1+0.08*np.sin((m.month-1)/12*2*np.pi)
                actual=base*rm*season*rng.normal(1,0.05)
                forecast=actual*rng.normal(1.01,0.045)
                bookings=actual*rng.normal(1.10,0.10)
                backlog=actual*rng.uniform(2.2,4.1)
                acv=actual*rng.uniform(0.75,0.95)
                pipeline=bookings*rng.uniform(2.4,4.0)
                rows.append([m,reg,bu,actual,forecast,bookings,backlog,acv,pipeline])
    return pd.DataFrame(rows,columns=["month","region","business_unit","actual_revenue","forecast_revenue","bookings","backlog","acv","pipeline"])
