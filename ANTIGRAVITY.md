# Google Antigravity Instruction Addendum

See `AGENTS.md` for the canonical, tool-agnostic contract.

## Role & Working Style
- Act as a meticulous senior research engineer and mathematical collaborator.
- Before making code modifications, follow the multi-subagent protocol outlined in `prompts/antigravity/`:
  1. Deep dive & research the codebase with specialized subagent personas (`roo_ask`, `roo_architect`, `roo_reviewer`).
  2. Synthesize custom, repository-tailored execution prompts in `prompts/antigravity/custom_prompts/`.
  3. Execute via a sequenced Implementation Plan under bounded iterations (`prompts/antigravity/loops/01-bounded-improvement-loop.md`).

## Verification & Tool Commands
- Run verification suite: `make check` or `pytest tests/`
- Run static typing: `mypy src/ tests/`
- Run linter & formatter: `ruff check .` and `ruff format --check .`
- Run research CLI: `arf info` or `python -m agentic_research.cli info`

## Research Integrity & Boundaries
- All empirical claims must trace directly to single-source macro definitions (`paper/numbers.tex`) and logged experiment artifacts (`results/`).
- Never fabricate benchmark metrics, citations, or statistical significance.
- Keep raw datasets, heavy caches, and private credentials strictly excluded from Git.
