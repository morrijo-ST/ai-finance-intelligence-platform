import streamlit as st
import plotly.graph_objects as go
from core import load_data, answer_question

st.set_page_config(page_title="Morris | Finance Intelligence", page_icon="◈", layout="wide")
with st.sidebar:
    st.markdown("## ◈ MORRIS\nFINANCE INTELLIGENCE")
    st.caption("WORKSPACE / PUBLIC DEMO")
    page = st.radio("Workspace", ["Overview", "Revenue detail", "Finance questions"], label_visibility="collapsed")
    st.divider()
    light = st.toggle("Light appearance")
    df = load_data()
    year = st.selectbox("Reporting year", sorted(df.month.dt.year.unique()), index=1)
    quarter = st.selectbox("Reporting period", ["Full year", "Q1", "Q2", "Q3", "Q4"])
    regions = st.multiselect("Regions", sorted(df.region.unique()), default=sorted(df.region.unique()))
    units = st.multiselect("Business units", sorted(df.business_unit.unique()), default=sorted(df.business_unit.unique()))
    st.divider()
    st.caption("SYNTHETIC DATA\n\nReproducible finance demonstration. No client records or production connections.")
    st.link_button("Explore the source ↗", "https://github.com/morrijo-ST/ai-finance-intelligence-platform")

bg, panel, ink, muted, border = ("#f2f5fa", "#ffffff", "#15253d", "#596b83", "#dce4ef") if light else ("#080f1c", "#101c2e", "#eef4ff", "#98abc6", "#243650")
blue, teal, amber = "#579dff", "#35d5b1", "#f6b660"
st.markdown(f"""<style>
.stApp {{background:{bg};color:{ink};}}
[data-testid="stHeader"] {{background:transparent;}}
[data-testid="stSidebar"] {{background:{panel};border-right:1px solid {border};}}
.block-container {{padding-top:2rem;max-width:1540px;padding-bottom:3rem;}}
h1,h2,h3 {{color:{ink};letter-spacing:-.035em;}}
[data-testid="stMarkdownContainer"] p, label {{color:inherit;}}
[data-testid="stMetric"] {{background:linear-gradient(125deg,{panel},{bg});border:1px solid {border};border-radius:16px;padding:22px 24px;min-height:142px;}}
[data-testid="stMetricValue"] {{color:{ink};font-weight:600;letter-spacing:-.04em;}}
[data-testid="stMetricLabel"] {{color:{muted};}}
[data-testid="stVerticalBlockBorderWrapper"] > div {{border-color:{border}!important;border-radius:16px!important;}}
.kicker {{color:{blue};font-size:11px;font-weight:700;letter-spacing:.18em;margin-bottom:10px;}}
.sub {{color:{muted};font-size:14px;line-height:1.7;}}
.brief {{background:linear-gradient(110deg,{panel},{bg});border:1px solid {border};border-left:3px solid {teal};border-radius:12px;padding:20px 24px;margin:16px 0 24px;}}
.brief strong {{color:{ink};font-size:17px;}}
.stButton button, .stDownloadButton button {{border-radius:9px;}}
</style>""", unsafe_allow_html=True)

f = df[(df.month.dt.year == year) & df.region.isin(regions) & df.business_unit.isin(units)]
if quarter != "Full year":
    f = f[f.month.dt.quarter == int(quarter[-1])]

st.markdown('<div class="kicker">MORRIS / FINANCE INTELLIGENCE</div>', unsafe_allow_html=True)
a,b=st.columns([4,1])
a.title({"Overview":"Your financial picture. In focus.","Revenue detail":"From headline to detail.","Finance questions":"Answers with a clear scope."}[page])
a.markdown(f'<div class="sub">{year} · {quarter} · USD · Synthetic portfolio demonstration</div>', unsafe_allow_html=True)
b.caption("REPORTING SCOPE")
b.write(f"{len(regions)} regions · {len(units)} business units")
if f.empty:
    st.info("No records in this view. Select at least one region and business unit to explore the dashboard.")
    st.stop()

rev=f.actual_revenue.sum(); fc=f.forecast_revenue.sum(); bookings=f.bookings.sum()
variance=rev-fc; pct=variance/fc if fc else 0
latest=f[f.month==f.month.max()]
backlog=latest.backlog.sum()
monthly=f.groupby("month",as_index=False)[["actual_revenue","forecast_revenue","bookings"]].sum()
regional=f.groupby("region",as_index=False)[["actual_revenue","forecast_revenue","variance"]].sum().sort_values("actual_revenue")

def chart(fig, height=310):
    fig.update_layout(height=height, margin=dict(l=12,r=12,t=24,b=16), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color=ink,family="Arial",size=12), legend=dict(orientation="h",y=1.14,x=0), hoverlabel=dict(bgcolor=panel,font_color=ink), separators=".,")
    fig.update_xaxes(showgrid=False,zeroline=False,color=muted)
    fig.update_yaxes(gridcolor=border,zeroline=False,color=muted)
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

def detail():
    st.subheader("The numbers behind the view")
    st.caption("Revenue and bookings are period totals. Backlog is a month-end snapshot; the headline uses the latest selected month.")
    cols=["month","region","business_unit","actual_revenue","forecast_revenue","variance","variance_pct","bookings","backlog"]
    d=f[cols].sort_values(["month","region"],ascending=[False,True]).copy()
    d["month"]=d.month.dt.strftime("%b %Y")
    d["variance_pct"]*=100
    d.columns=["Month","Region","Business unit","Revenue","Forecast","Variance","Variance %","Bookings","Backlog snapshot"]
    st.dataframe(d,hide_index=True,use_container_width=True,column_config={c:st.column_config.NumberColumn(format="$%.0f") for c in ["Revenue","Forecast","Variance","Bookings","Backlog snapshot"]}|{"Variance %":st.column_config.NumberColumn(format="%.1f%%")})
    st.download_button("Download selected data ↓",f[cols].to_csv(index=False),"finance-selected-scope.csv","text/csv")

if page=="Overview":
    st.write("")
    c=st.columns(4)
    c[0].metric("ACTUAL REVENUE",f"${rev/1e6:,.1f}M",f"{pct:+.1%} vs forecast")
    c[1].metric("FORECAST",f"${fc/1e6:,.1f}M", "Selected period",delta_color="off")
    c[2].metric("BOOKINGS",f"${bookings/1e6:,.1f}M",f"{bookings/rev:.2f}× revenue",delta_color="off")
    c[3].metric("CLOSING BACKLOG",f"${backlog/1e6:,.1f}M",f.month.max().strftime("%b %Y snapshot"),delta_color="off")
    worst=regional.sort_values("variance").iloc[0]
    lead=regional.iloc[-1]
    st.markdown(f'<div class="brief"><div class="kicker">EXECUTIVE READOUT</div><strong>Revenue is {abs(pct):.1%} {"ahead of" if variance>=0 else "below"} forecast.</strong><div class="sub">{lead.region} leads revenue at ${lead.actual_revenue/1e6:,.1f}M. The lowest regional variance is {worst.region} at ${worst.variance/1e6:+,.1f}M. Calculated from the selected scope.</div></div>',unsafe_allow_html=True)
    left,right=st.columns([1.7,1])
    with left,st.container(border=True):
        st.subheader("Revenue trajectory")
        st.caption("Monthly actuals, forecast and bookings · USD millions")
        fig=go.Figure()
        for col,label,color,dash in [("actual_revenue","Actual revenue",blue,"solid"),("forecast_revenue","Forecast",muted,"dash"),("bookings","Bookings",teal,"solid")]:
            fig.add_trace(go.Scatter(x=monthly.month,y=monthly[col]/1e6,name=label,mode="lines+markers",line=dict(color=color,width=3 if col=="actual_revenue" else 2,dash=dash),marker=dict(size=5),hovertemplate="%{x|%b %Y}<br>$%{y:,.2f}M<extra>%{fullData.name}</extra>"))
        chart(fig)
    with right,st.container(border=True):
        st.subheader("Regional contribution")
        st.caption("Actual revenue · USD millions")
        chart(go.Figure(go.Bar(x=regional.actual_revenue/1e6,y=regional.region,orientation="h",marker_color=[blue,blue,blue,teal][-len(regional):],text=[f"${x/1e6:,.1f}M" for x in regional.actual_revenue],textposition="auto",hovertemplate="%{y}<br>$%{x:,.2f}M<extra></extra>")))
    left,right=st.columns([1.7,1])
    with left,st.container(border=True):
        st.subheader("Forecast to actual")
        st.caption("Regional variances explain the revenue movement · USD millions")
        bridge=go.Figure(go.Waterfall(x=["Forecast"]+regional.region.tolist()+["Actual"],y=[fc/1e6]+(regional.variance/1e6).tolist()+[0],measure=["absolute"]+["relative"]*len(regional)+["total"],increasing=dict(marker_color=teal),decreasing=dict(marker_color=amber),totals=dict(marker_color=blue),connector=dict(line=dict(color=border)),hovertemplate="%{x}<br>$%{y:,.2f}M<extra></extra>"))
        chart(bridge)
    with right,st.container(border=True):
        st.subheader("Business unit performance")
        st.caption("Actual revenue / forecast attainment")
        for name,g in f.groupby("business_unit"):
            ratio=g.actual_revenue.sum()/g.forecast_revenue.sum()
            st.markdown(f"**{name}**")
            st.caption(f"${g.actual_revenue.sum()/1e6:,.1f}M revenue · {ratio:.1%} of forecast")
            st.progress(min(max(float(ratio)/1.2,0),1))
        st.caption("Progress scale: 0–120% of forecast.")
    with st.expander("Inspect underlying records"):
        detail()
elif page=="Revenue detail":
    detail()
else:
    st.subheader("Ask the finance model")
    st.info("This public demo uses deterministic question matching, not a live language model. Ask for a supported metric, optionally a region and year. Dashboard filters apply first.")
    st.caption("Supported metrics: revenue, forecast, bookings, backlog, ACV, pipeline. Backlog, ACV and pipeline answers use the latest matching month.")
    with st.form("finance-question"):
        question=st.text_input("Your question",f"What is revenue in {year}?")
        submitted=st.form_submit_button("Analyze selected scope →")
    if submitted:
        q=question.strip().lower()
        keys=["revenue","forecast","bookings","backlog","acv","pipeline"]
        matches=[k for k in keys if k in q]
        if len(matches)!=1 or any(x in q for x in ["why","predict","compare","growth","margin","cash","profit","variance"]):
            st.warning("Try a single supported metric, for example ‘Top region for bookings in 2026’. This demo does not interpret causal, predictive or multi-metric questions.")
        else:
            scoped=f
            if matches[0] in ["backlog","acv","pipeline"]:
                scoped=f[f.month==f.month.max()]
            st.success(answer_question(scoped,question))
            st.caption(f"Source: synthetic finance dataset · {len(scoped):,} rows in dashboard scope before question-specific filters.")
    with st.expander("How to interpret this demonstration"):
        st.write("All displayed financial values are synthetic. Calculations respond to the selected year, quarter, regions and business units. No financial records are modified. This demonstration does not call Snowflake, an ERP, or an external AI provider.")

st.divider()
st.caption("MORRIS  /  Finance systems, built with clarity.       •       Synthetic demonstration · USD · Calendar-year reporting")
