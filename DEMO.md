# Run the Public Demo

This repository includes a deterministic synthetic-data demo. No external credentials or proprietary datasets are required.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Test the analytics logic

```bash
pytest -q
```

The finance Q&A, executive briefing, variance analysis, and dashboard all run against synthetic data generated with a fixed seed for reproducibility.
