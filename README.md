# Agentic Research Framework (ARF)

[![CI](https://github.com/AkashKundu114/agentic-research-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/AkashKundu114/agentic-research-framework/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

A production-grade autonomous research framework & starter template engineered for **local AI coding agents** (Google Antigravity, Claude Code, Cursor, Codex, Gemini) and **reproducible scientific discovery**. 

Combines local-first safety guardrails, multi-agent orchestration contracts, single-source manuscript macro synchronization, and structured prompt libraries for zero-hallucination scientific research.

---

## Key Highlights

- **Multi-Agent Governance:** Canonical universal contract in [`AGENTS.md`](./AGENTS.md) with dedicated adapter overlays for [Google Antigravity](ANTIGRAVITY.md), [Claude Code](CLAUDE.md), [Gemini CLI](GEMINI.md), [OpenAI Codex](CODEX.md), and [Cursor](CURSOR.md).
- **Multi-Subagent Deep Dive Protocol:** Structured prompts in [`prompts/antigravity/`](./prompts/antigravity/) implementing a strict **Codebase Research $\to$ Custom Prompt Synthesis $\to$ Phased Plan Execution** workflow.
- **Reproducible Pipeline Out-of-the-Box:** Includes a fully-typed Python package (`src/agentic_research/`), parameterized CLI (`arf` / `research-cli`), clean unit tests (`tests/`), and data provisioning scripts (`scripts/`).
- **Single-Source Research Integrity:** Strict zero-fabrication rules: all empirical claims, LaTeX tables, and manuscript figures map directly to frozen JSON registries via `numbers.tex`.
- **Air-Gapped & Offline Ready:** Configured to run offline by default without leaking credentials, private datasets, or unpublished manuscript drafts.

---

## Quickstart

### 1. Clone & Set Up Environment

```bash
# Clone repository
git clone https://github.com/AkashKundu114/agentic-research-framework.git
cd agentic-research-framework

# Option A: Standard Python venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev,docs]"

# Option B: Ultra-fast setup via uv
uv venv
uv pip install -e ".[dev,docs]"
```

### 2. Run Verification Suite

Verify that everything passes out of the box:
```bash
make check
# Or manually:
python -m pytest tests/
python -m ruff check src tests scripts
python -m mypy src tests scripts
```

### 3. Run Sample Research Pipeline & CLI

```bash
# View project configuration
arf info

# Run parameterized evaluation pipeline
arf run --samples 100 --output results/metrics.json

# Evaluate existing metric artifact
arf eval --metrics results/metrics.json

# Convenience direct runner (works without pip install):
python run_demo.py run --samples 50
```

# Run evaluation pipeline (creates results/metrics.json)
research-cli run --samples 150 --output results/metrics.json

# Generate publication-ready vector figure and LaTeX table
python scripts/generate_figures.py --metrics results/metrics.json
python scripts/generate_tables.py --metrics results/metrics.json
```

---

## Multi-Agent Architecture & Prompt Library

This repository introduces an opinionated, phased multi-subagent lifecycle:

```text
┌─────────────────────────────────────────────────────────────────┐
│ Phase 1: Multi-Subagent Codebase Deep Dive                      │
│ • Researcher Subagent: Maps symbols, AST, and dependencies     │
│ • Auditor Subagent: Evaluates test coverage and static typing   │
│ • Security Subagent: Scans secrets, leaks, and path boundaries │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ Phase 2: Custom Prompt Synthesis                                │
│ • Compiles findings into repo-tailored, concrete prompt specs   │
│ • Binds exact file paths, line ranges, class names, & commands  │
│ • Defines unambiguous pass/fail acceptance criteria             │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ Phase 3: Phased Implementation Plan Execution                   │
│ • Sequences custom prompts into an actionable roadmap           │
│ • Dispatches Coder Subagents for surgical, minimal edits        │
│ • Runs automated verification gates after every phase           │
└─────────────────────────────────────────────────────────────────┘
```

See [`prompts/antigravity/README.md`](./prompts/antigravity/README.md) for the complete library of:
- **Goals (`goals/`):** 00 Baseline Deep Dive, 01 Custom Prompt Generator, 02 Hypothesis & Claim Audit, 15 Edge-Case Testing, 25 Data Leakage Audit, 35 GPU Profiling, 45 Manuscript Typography, 60 Baseline Parity.
- **Loops (`loops/`):** Bounded self-improvement loops with hard stop-conditions (max 5 iterations per run).
- **Custom Prompts (`custom_prompts/`):** Precision prompts for typing fixes, citation resolution, and boundary tests.

---

## Repository Layout

```text
.
├── .github/
│   └── workflows/ci.yml         # GitHub Actions multi-OS / multi-Python CI
├── config/
│   ├── agent.project.yaml       # Version-controlled project goals and policies
│   └── agent.local.example.yaml # Local machine resource and hardware limits
├── data/
│   ├── raw/                     # Original, immutable datasets (git-ignored)
│   ├── interim/                 # Intermediate transformations (git-ignored)
│   ├── processed/               # Model-ready train/test splits (git-ignored)
│   └── README.md                # Provenance and dataset acquisition guide
├── docs/
│   ├── architecture.md          # System boundaries and data flow topology
│   ├── reproducibility.md       # Manifest requirements and determinism checklist
│   └── security.md              # Local execution policies and sandboxing
├── experiments/
│   ├── configs/                 # YAML configuration specs for experimental runs
│   └── README.md                # Experiment protocols and hypothesis tracking
├── paper/
│   ├── figures/                 # Generated vector/raster figures (git-ignored)
│   └── README.md                # Manuscript LaTeX sources and build guide
├── prompts/
│   └── antigravity/             # Multi-subagent goal and loop prompt library
├── results/
│   ├── figures/                 # Consolidated visual artifacts
│   ├── tables/                  # Auto-generated LaTeX / Markdown tables
│   └── README.md                # Result registry guidelines
├── scripts/
│   ├── fetch_data.py            # Dataset provisioning with SHA-256 checks
│   ├── preprocess_data.py       # Leakage-free train/test splitting
│   ├── run_experiment.py        # Experiment matrix execution
│   ├── generate_figures.py      # Automated vector/raster figure generator
│   └── generate_tables.py       # LaTeX booktabs and Markdown table exporter
├── src/
│   └── agentic_research/        # Core Python research package (PEP 561 typed)
├── tests/                       # Complete pytest unit and integration suite
├── AGENTS.md                    # Canonical universal AI agent contract
├── CLAUDE.md                    # Claude Code instructions
├── GEMINI.md                    # Gemini CLI instructions
├── CODEX.md                     # OpenAI Codex instructions
├── CURSOR.md                    # Cursor AI instructions
├── ANTIGRAVITY.md               # Google Antigravity instructions
├── Makefile                     # Cross-platform developer targets
├── pyproject.toml               # Package build, dependencies, ruff & mypy config
├── LICENSE                      # MIT Open-Source License
├── CONTRIBUTING.md              # Contributor workflow and PR guidelines
└── CITATION.cff                 # Citation metadata
```

---

## Security & Privacy Notice

This repository starter provides behavioral constraints via `AGENTS.md`, but **prompt instructions are not an operating system sandbox**. Enforce filesystem isolation, command permissions, network restrictions, and model-server access through your operating system, virtual machine, or container runtime.

---

## Author & Citation

Maintained and authored by **Akash Kundu** ([@AkashKundu114](https://github.com/AkashKundu114), `akashkundu1152@gmail.com`).

If you use this boilerplate in your academic research or projects, please cite it using the metadata provided in [`CITATION.cff`](./CITATION.cff).

---

## License

Distributed under the [MIT License](./LICENSE).
