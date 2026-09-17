# Architecture — AI Finance Intelligence Platform

## System Overview

```text
Source Systems
  ├─ CRM
  ├─ ERP
  ├─ Contracts
  ├─ Forecasts
  └─ Reference Data
        |
        v
    Snowflake
        |
  Curated Finance Models
        |
        v
 Python / FastAPI Services
        |
        v
 AI Tool-Orchestration Layer
        |
  +-----+------+------+
  |     |      |      |
 Q&A  SQL   Variance Commentary
        |
        v
 Human Review / Distribution
```

## Design Principles
- Snowflake remains the analytical system of record.
- Finance calculations are deterministic and governed.
- AI receives only the context required for the current task.
- Generated SQL is validated against approved schemas and query patterns.
- Sensitive credentials are stored outside source code.
- Outputs are logged for traceability.

## Logical Components
### Data Layer
Curated fact and dimension models support finance questions across bookings, revenue, contracts, customers, forecasts, and time.

### Service Layer
FastAPI exposes narrowly scoped endpoints for query execution, metric retrieval, and briefing generation.

### AI Layer
The model interprets user intent, selects an approved tool, summarizes results, and produces management-ready commentary.

### Control Layer
Permissions, allow-listed datasets, logging, validation, and human approval protect the finance process.

## Deployment Reference
A public demo can run with synthetic data in Snowflake/PostgreSQL, a FastAPI service, and an LLM provider. Production implementations should use managed secret storage, role-based access, monitoring, and environment separation.
