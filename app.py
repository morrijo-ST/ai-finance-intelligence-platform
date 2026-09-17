import streamlit as st
import plotly.express as px
from core import load_data, executive_brief, answer_question

st.set_page_config(page_title="AI Finance Intelligence", layout="wide")
st.title("AI Finance Intelligence Platform")
st.caption("Synthetic public demonstration — finance Q&A, variance analysis, and executive briefing.")

df = load_data()
regions = st.sidebar.multiselect("Region", sorted(df.region.unique()), default=sorted(df.region.unique()))
bus = st.sidebar.multiselect("Business Unit", sorted(df.business_unit.unique()), default=sorted(df.business_unit.unique()))
years = st.sidebar.multiselect("Year", sorted(df.month.dt.year.unique()), default=sorted(df.month.dt.year.unique()))
f = df[df.region.isin(regions) & df.business_unit.isin(bus) & df.month.dt.year.isin(years)]

c1,c2,c3,c4=st.columns(4)
c1.metric("Revenue", f"${f.actual_revenue.sum()/1e6:,.1f}M")
c2.metric("Forecast", f"${f.forecast_revenue.sum()/1e6:,.1f}M")
c3.metric("Bookings", f"${f.bookings.sum()/1e6:,.1f}M")
c4.metric("Backlog", f"${f.backlog.sum()/1e6:,.1f}M")

st.subheader("Executive briefing")
st.info(executive_brief(f))

question = st.text_input("Ask the finance model", "What is revenue in 2026?")
if question:
    st.success(answer_question(f, question))

monthly=f.groupby("month",as_index=False)[["actual_revenue","forecast_revenue","bookings"]].sum()
fig=px.line(monthly,x="month",y=["actual_revenue","forecast_revenue","bookings"],markers=True,title="Monthly performance")
st.plotly_chart(fig,use_container_width=True)

region=f.groupby("region",as_index=False)[["actual_revenue","bookings","backlog"]].sum()
st.plotly_chart(px.bar(region,x="region",y="actual_revenue",title="Revenue by region"),use_container_width=True)

st.subheader("Variance detail")
detail=f[["month","region","business_unit","actual_revenue","forecast_revenue","variance","variance_pct"]].copy()
detail["variance_pct"]=(detail["variance_pct"]*100).round(1)
st.dataframe(detail.sort_values("month",ascending=False),use_container_width=True)
