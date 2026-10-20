# Claude Code Instructions

Read `AGENTS.md` first and treat it as the canonical repository contract.

## Working style
- Begin with read-only inspection; provide a short plan before complex multi-file changes.
- Use subagents for independent, bounded analysis tasks (e.g. tests, security review, documentation). Avoid concurrent edits to the same files.
- Treat subagent output as unverified until confirmed against the actual repository and command results.
- Use available repository tools before inventing new scripts or abstractions.
- Keep changes scoped and explain material trade-offs.

## Tool and approval boundaries
- Ask before destructive operations, broad installs, external network access, uploading source/data, changing remote services, committing, pushing, publishing, or deploying.
- Do not bypass permission prompts, sandbox controls, or project hooks.
- Do not claim a test passed unless you actually ran it and inspected its exit status/output.

## Research tasks
- Keep results tied to configs, seeds, data versions, code revisions, and environment.
- Review manuscript claims against code, logs, tables, and cited sources.
- Do not fabricate citations, experiment results, or peer-review outcomes.

## Completion response
Summarize: what changed, important files, checks run and actual outcomes, risks/limitations, and recommended next step.
