# AI Finance Intelligence Platform

An AI-assisted finance intelligence platform that connects structured enterprise data with natural-language analysis, executive reporting, and governed decision support.

> **Working public demo:** This repository now includes deterministic synthetic data generation, executable finance analytics logic, a Streamlit application, automated tests, and reproducible run instructions. See [`DEMO.md`](DEMO.md).

> **Portfolio note:** This public repository is a sanitized reference implementation based on enterprise finance-system patterns. It contains no employer data, credentials, internal identifiers, customer information, or proprietary source code.

## Try It

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The demo includes finance Q&A, executive briefing generation, monthly revenue / forecast / bookings analysis, regional performance, and variance detail. The underlying synthetic portfolio is regenerated deterministically on every run.

## Business Problem

Finance teams often operate across CRM, ERP, contract, revenue, forecast, and reporting systems. Analysts spend significant time locating data, reconciling definitions, answering recurring management questions, and translating results into executive commentary.

This project demonstrates a governed AI layer that sits above a modern finance-data platform and helps users:

- query finance and commercial metrics in natural language
- retrieve trusted data from governed sources
- apply finance-specific business rules
- identify anomalies and variances
- generate management-ready commentary
- distribute recurring executive briefings
- preserve human oversight for consequential decisions

## Reference Architecture

```text
CRM / ERP / Contracts / Forecasts
              |
              v
          Snowflake
              |
      Governed semantic layer
              |
      Python / FastAPI services
              |
         AI reasoning layer
              |
   +----------+-----------+
   |          |           |
   v          v           v
Q&A / SQL   Variance   Executive
Analysis    Detection   Briefings
   |          |           |
   +----------+-----------+
              |
      Human review / controls
```

## Core Capabilities

- Natural-language financial analysis
- Governed metric retrieval
- Revenue / bookings / forecast analysis
- Variance and anomaly-oriented reporting
- Executive commentary generation
- API-oriented architecture
- Audit-friendly controls and human review

## Technology

`Python` `Streamlit` `Pandas` `Plotly` `Snowflake` `FastAPI` `Claude` `OpenAI` `SQL` `REST APIs` `Azure` `Power BI`

## Repository Structure

```text
.
├── app.py                 # interactive demo
├── core.py                # finance logic / Q&A
├── synthetic.py           # deterministic dummy-data generator
├── requirements.txt
├── DEMO.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── business-rules.md
│   ├── data-dictionary.md
│   ├── security.md
│   └── runbook.md
└── tests/
    └── test_core.py
```

## Demo Status

- [x] Public-safe project definition
- [x] Deterministic synthetic finance data
- [x] Executable finance analytics logic
- [x] Interactive Streamlit demo
- [x] Finance Q&A example
- [x] Executive briefing example
- [x] Automated tests
- [x] Security / controls documentation
- [ ] Hosted live-demo URL
- [ ] Recorded 60–120 second walkthrough

## Design Principle

AI does not directly modify financial records in this reference design. Deterministic calculations, source-system controls, and human approvals remain authoritative. AI is used to retrieve, summarize, classify, and explain governed financial information.
