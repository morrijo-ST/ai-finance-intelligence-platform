# Data Dictionary — AI Finance Intelligence Platform

This public reference uses synthetic data. Field names below define the minimum demo contract.

| Table | Field | Type | Description |
|---|---|---|---|
| dim_customer | customer_id | string | Synthetic customer key |
| dim_customer | customer_name | string | Fictional customer name |
| dim_customer | region | string | Reporting region |
| fact_bookings | booking_id | string | Booking transaction key |
| fact_bookings | customer_id | string | Customer foreign key |
| fact_bookings | booking_date | date | Booking date |
| fact_bookings | booking_value | decimal | Booked contract value |
| fact_revenue | revenue_id | string | Revenue transaction key |
| fact_revenue | customer_id | string | Customer foreign key |
| fact_revenue | revenue_date | date | Revenue recognition date |
| fact_revenue | revenue_value | decimal | Recognized revenue |
| fact_forecast | forecast_id | string | Forecast row key |
| fact_forecast | customer_id | string | Customer foreign key |
| fact_forecast | forecast_period | date | Forecast period |
| fact_forecast | forecast_value | decimal | Forecast value |
| fact_contracts | contract_id | string | Contract key |
| fact_contracts | customer_id | string | Customer foreign key |
| fact_contracts | start_date | date | Contract start |
| fact_contracts | end_date | date | Contract end |
| fact_contracts | acv | decimal | Annual contract value |

## Conventions
- Monetary fields use the demo reporting currency unless `currency_code` is present.
- Dates use ISO `YYYY-MM-DD`.
- Public datasets contain no real customer or employer information.
