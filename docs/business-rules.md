# Business Rules — AI Finance Intelligence Platform

## Governance Rules

**BR-001 — Source of truth**  
Financial values must originate from approved analytical datasets. The AI layer cannot invent or override source-system values.

**BR-002 — Deterministic metrics**  
Revenue, bookings, forecast, variance, and other finance KPIs must be calculated using governed formulas outside the LLM.

**BR-003 — Read-only default**  
AI interactions are read-only unless a separately governed workflow explicitly permits an action.

**BR-004 — No autonomous posting**  
AI cannot post journal entries, modify contracts, update CRM records, or change financial ledgers without explicit human approval.

**BR-005 — Approved datasets only**  
Generated queries may access only allow-listed schemas, views, and fields.

**BR-006 — Explainable output**  
Executive commentary should reference the underlying metric movement, time period, and primary driver when available.

**BR-007 — Missing-data handling**  
If required inputs are unavailable, the system must surface the limitation rather than fabricate a conclusion.

**BR-008 — Auditability**  
Queries, tool calls, and generated management outputs should be logged with timestamps and user context.

**BR-009 — Sensitive data minimization**  
Only the minimum required fields should be sent to an external model provider.

**BR-010 — Human review**  
High-impact commentary or actions used for official financial reporting require finance-owner review.
