# Security — AI Finance Intelligence Platform

## Security Principles
- No credentials or secrets are stored in source control.
- Use environment variables or managed secret storage.
- Restrict model/tool access to approved datasets and operations.
- Apply least-privilege Snowflake roles.
- Log user, query, tool, and output metadata where appropriate.
- Minimize sensitive data sent to external model providers.
- Separate development, test, and production environments.

## AI-Specific Controls
- Generated SQL must be validated before execution.
- Restrict queries to allow-listed schemas/views.
- Block write operations by default.
- Do not allow autonomous modification of financial records.
- Require human review for official reporting outputs.

## Public Repository Controls
This repository contains synthetic examples only. Do not commit employer names, internal endpoints, account identifiers, private keys, passwords, service-account details, or real customer data.
