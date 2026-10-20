.PHONY: help install test lint typecheck format clean check all

help:
	@echo "Available targets:"
	@echo "  install    - Install package in editable mode with development dependencies"
	@echo "  test       - Run test suite via pytest"
	@echo "  lint       - Check code style and imports via ruff"
	@echo "  typecheck  - Verify static type annotations via mypy"
	@echo "  format     - Automatically format code via ruff format"
	@echo "  clean      - Remove temporary caches and build artifacts"
	@echo "  check      - Run lint, typecheck, and test suite"
	@echo "  all        - Default target (runs check)"

install:
	python -m pip install -e ".[dev]"

test:
	python -m pytest tests/

lint:
	python -m ruff check src tests scripts

typecheck:
	python -m mypy src tests scripts

format:
	python -m ruff format src tests scripts

clean:
	python -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"
	python -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in ['.pytest_cache', '.ruff_cache', '.mypy_cache', 'build', 'dist', 'src/*.egg-info']]"

check: lint typecheck test

all: check
