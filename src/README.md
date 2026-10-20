# Core Package Source (`src/`)

This directory contains the primary Python library code for the research project, packaged under [`src/agentic_research/`](./agentic_research).

## Package Architecture

```
src/agentic_research/
├── __init__.py      # Public API exports (ProjectConfig, run_pipeline, etc.)
├── config.py        # Schema validation, dataclass configs, YAML/JSON loading
├── pipeline.py      # Core research pipeline, synthetic benchmark, evaluation metrics
├── cli.py           # Command-line interface (`arf` and `research-cli`)
└── py.typed         # PEP 561 static type marker for strict mypy compliance
```

## Design Principles
1. **Separation of Concerns:** Keep core algorithmic and experimental logic independent from CLI argument parsing and ad-hoc scripts.
2. **Deterministic Execution:** Every pipeline function accepts an explicit random seed and avoids global state mutations.
3. **PEP 561 Type Completeness:** Full type annotations required (`strict = true` in mypy).
4. **No Import-Time Side Effects:** Importing `agentic_research` never runs computations, downloads datasets, or allocates GPU memory.
