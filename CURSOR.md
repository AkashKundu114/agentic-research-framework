# Cursor Instructions

Read `AGENTS.md` first and treat it as the canonical repository contract.

## Working style
- Begin with read-only inspection; generate a clear implementation plan before refactoring.
- Use subagents or explicit persona transitions for exploration, implementation, and review.
- Preserve existing conventions, type annotations, and docstrings.
- Minimize editing surface area; avoid broad formatting churn.

## Tool and approval boundaries
- Ask before destructive actions, network access, or git commit/push/deploy.
- Never disable linting rules or delete tests to force a passing state.
- Do not claim a command succeeded without inspecting its output.

## Research tasks
- Keep experiment parameters, seeds, and metrics explicitly logged in `results/`.
- Verify claims against evidence; never fabricate numbers or citations.
- Preserve train/test boundaries and keep raw datasets immutable.

## Completion response
Summarize: what changed, important files, checks run and actual outcomes, risks/limitations, and recommended next step.
