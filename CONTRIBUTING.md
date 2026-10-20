# Contributing Guidelines

Thank you for contributing to the Local AI Research Boilerplate!

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   # Using standard venv
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev]"

   # Or using uv (recommended for speed)
   uv venv
   uv pip install -e ".[dev]"
   ```

3. **Verify the environment:**
   ```bash
   make check
   ```

## Workflow & Coding Standards

- **Universal Agent Contract:** All human contributors and AI agents must follow the core research integrity, safety, and code quality principles in [`AGENTS.md`](./AGENTS.md).
- **Code Style:** Formatted using `ruff`. Run `make lint` or `make format` before committing.
- **Static Typing:** Typed with PEP 561 compliance. Run `make typecheck` or `mypy src/ tests/`.
- **Testing:** Every feature or bugfix must include corresponding unit tests in `tests/`. All tests must pass cleanly (`make test`).
- **Data & Artifacts:** Never commit raw datasets, model weights, or manuscript PDF build products to Git. Keep them local per `.gitignore`.

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-feature`.
2. Implement focused, minimal changes.
3. Run the full verification suite: `make check`.
4. Open a Pull Request with a clear description of the change, test evidence, and any architectural implications.
