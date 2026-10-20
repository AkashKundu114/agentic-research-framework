# Experiments

Keep each experiment's configuration and execution entrypoint versioned. Store large outputs outside Git or in approved artifact storage.

Suggested naming: `YYYYMMDD-topic-method-seedNN`.

Each run should preserve:
- Config snapshot
- Git commit
- Dataset manifest/version
- Seed
- Exact command
- Environment details
- Metrics and uncertainty
- Output artifact paths and hashes
- Status (`completed`, `failed`, `interrupted`) and notes

Do not delete failed runs just because they are inconvenient.
