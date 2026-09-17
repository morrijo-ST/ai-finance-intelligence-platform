import re
import pandas as pd
from synthetic import generate_finance_data

METRICS = {
    "revenue": "actual_revenue",
    "forecast": "forecast_revenue",
    "bookings": "bookings",
    "backlog": "backlog",
    "acv": "acv",
    "pipeline": "pipeline",
}

def load_data(path=None):
    df = generate_finance_data() if path is None else pd.read_csv(path, parse_dates=["month"])
    df["variance"] = df["actual_revenue"] - df["forecast_revenue"]
    df["variance_pct"] = df["variance"] / df["forecast_revenue"].replace(0, pd.NA)
    return df

def executive_brief(df):
    rev = df["actual_revenue"].sum()
    fcst = df["forecast_revenue"].sum()
    bookings = df["bookings"].sum()
    backlog = df["backlog"].sum()
    variance = rev - fcst
    pct = variance / fcst if fcst else 0
    top_region = df.groupby("region")["actual_revenue"].sum().idxmax()
    return (
        f"Revenue is ${rev/1e6:,.1f}M, {pct:+.1%} versus forecast. "
        f"Bookings total ${bookings/1e6:,.1f}M and backlog is ${backlog/1e6:,.1f}M. "
        f"{top_region} is the largest revenue region in the selected view."
    )

def answer_question(df, question):
    q = question.lower()
    metric_key = next((k for k in METRICS if k in q), "revenue")
    metric = METRICS[metric_key]
    scoped = df.copy()
    for region in df["region"].dropna().unique():
        if region.lower() in q:
            scoped = scoped[scoped["region"] == region]
    years = re.findall(r"\b(20\d{2})\b", q)
    if years:
        scoped = scoped[scoped["month"].dt.year == int(years[0])]
    value = scoped[metric].sum()
    if scoped.empty:
        return "No records matched that question."
    if "top" in q or "largest" in q:
        g = scoped.groupby("region")[metric].sum().sort_values(ascending=False)
        return f"Top region for {metric_key}: {g.index[0]} at ${g.iloc[0]/1e6:,.1f}M."
    return f"{metric_key.title()} for the selected scope is ${value/1e6:,.1f}M."
