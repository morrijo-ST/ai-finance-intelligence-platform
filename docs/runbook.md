# Operations Runbook — AI Finance Intelligence Platform

## Start-Up Checks
1. Confirm environment variables and secret references are available.
2. Verify database connectivity.
3. Verify approved model/provider connectivity.
4. Confirm required views and schemas are reachable.
5. Run a health-check query against synthetic/demo data.

## Common Failures
### Database connection failure
- validate account / host / role / warehouse configuration
- confirm network access
- confirm credentials are current

### AI provider failure
- retry according to backoff policy
- capture the provider error
- fall back to deterministic reporting where possible

### Invalid generated SQL
- reject query
- log failed SQL
- require corrected generation or human review

### Missing metric definition
- stop the response path
- return a clear unsupported-metric message
- add the definition before enabling future use

## Monitoring
Track request count, query failures, model failures, latency, user errors, and generated-output review status.

## Recovery
The finance data layer remains authoritative. If the AI layer is unavailable, governed SQL, Power BI, and standard finance reporting continue to operate independently.

## Manual Override
Human finance users may bypass AI commentary and use source-system / BI outputs directly at any time.
