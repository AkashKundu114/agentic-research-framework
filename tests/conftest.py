"""Shared pytest fixtures for the research project test suite."""

from __future__ import annotations

from pathlib import Path

import pytest

from agentic_research.config import ProjectConfig


@pytest.fixture
def sample_config(tmp_path: Path) -> ProjectConfig:
    """Fixture providing a temporary, isolated ProjectConfig."""
    return ProjectConfig(
        name="test-experiment",
        seed=123,
        data_dir=tmp_path / "data",
        results_dir=tmp_path / "results",
    )


@pytest.fixture
def mock_yaml_config(tmp_path: Path) -> Path:
    """Fixture providing a temporary valid YAML config file."""
    cfg_file = tmp_path / "test_config.yaml"
    cfg_file.write_text(
        "project:\n"
        "  name: fixture-project\n"
        "  seed: 999\n"
        "parameters:\n"
        "  learning_rate: 0.001\n",
        encoding="utf-8",
    )
    return cfg_file
