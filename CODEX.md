# OpenAI Codex Instructions

Read `AGENTS.md` first and treat it as the canonical repository contract.

## Working style
- Begin with read-only inspection; provide a short plan before multi-file edits.
- Use specialized subagent roles (Researcher, Coder, Debugger, Reviewer) to maintain clean separation of concerns.
- Use existing repository tools before inventing new scripts or dependencies.
- Keep changes scoped, well-typed, and explain material trade-offs.

## Tool and approval boundaries
- Ask before destructive actions, broad dependency installs, network access, or git commit/push/deploy.
- Do not bypass permission prompts, sandbox controls, or project hooks.
- Do not claim a test passed unless you ran it and verified its exit status.

## Research tasks
- Keep all experiment results tied to configs, seeds, data versions, and logged outputs.
- Verify claims against evidence; never fabricate citations or benchmarks.
- Preserve train/validation/test boundaries; prevent data leakage.

## Completion response
Summarize: what changed, important files, checks run and actual outcomes, risks/limitations, and recommended next step.
