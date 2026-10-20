# Quickstart Guide

Get up and running with the **Agentic Research Framework (ARF)** in under 5 minutes.

---

## 1. Prerequisites

- **Python 3.10+** (Tested on Python 3.10, 3.11, 3.12, 3.13, 3.14)
- **Git**
- Optional: [uv](https://github.com/astral-sh/uv) for ultra-fast environment setup

---

## 2. Installation

Clone your repository and set up a clean virtual environment:

### Standard Setup (Python `venv`):
```bash
git clone https://github.com/AkashKundu114/agentic-research-framework.git
cd agentic-research-framework

python -m venv .venv

# Activate environment:
# On Linux/macOS:
source .venv/bin/activate
# On Windows PowerShell:
.venv\Scripts\Activate.ps1

# Install in editable mode with development dependencies:
pip install -e ".[dev,docs]"
```

### Ultra-Fast Setup (via `uv`):
```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
uv pip install -e ".[dev,docs]"
```

---

## 3. Verify the Test Suite

ARF includes a complete unit test suite out of the box. Verify that all components pass:

```bash
# Run pytest
python -m pytest tests/ -v

# Run static analysis
python -m ruff check src tests scripts
python -m mypy src tests scripts
```

All 13 tests will pass in under 0.1s.

---

## 4. Run the Research CLI (`arf`)

ARF provides a built-in CLI entrypoint (`arf` or `research-cli`):

```bash
# 1. Display environment and configuration info
arf info

# 2. Run an evaluation pipeline with 100 samples
arf run --samples 100 --output results/metrics.json

# 3. Evaluate and inspect the generated metrics artifact
arf eval --metrics results/metrics.json
```

---

## 5. Launch Your First AI Agent Session

ARF is preconfigured for your favorite AI coding assistant. Choose your tool:

- **Google Antigravity:** Start Antigravity in this repository directory. The agent automatically detects `ANTIGRAVITY.md` and `prompts/antigravity/`.
- **Claude Code:** Start `claude`. It automatically loads project instructions from `CLAUDE.md`.
- **Gemini CLI:** Launch `gemini`. Instructions are read from `GEMINI.md`.
- **Cursor:** Open the project folder in Cursor. Rules in `.cursorrules` and `CURSOR.md` are ingested.
- **OpenAI Codex:** Ingests instructions from `CODEX.md`.

To run a multi-subagent codebase audit, prompt your agent with:
```
Read prompts/antigravity/templates/custom_prompt_generator.md and execute a multi-subagent deep dive on this codebase.
```
