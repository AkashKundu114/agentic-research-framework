"""Unit tests for configuration loading and validation."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from agentic_research.config import ProjectConfig, load_config


def test_default_config() -> None:
    """Verify default ProjectConfig initialization values."""
    cfg = ProjectConfig()
    assert cfg.name == "agentic-research-framework"
    assert cfg.seed == 42
    assert cfg.data_dir == Path("data")
    assert cfg.results_dir == Path("results")


def test_load_config_none() -> None:
    """Verify load_config(None) returns defaults."""
    cfg = load_config(None)
    assert cfg.seed == 42


def test_load_yaml_config(mock_yaml_config: Path) -> None:
    """Verify loading from a YAML file."""
    cfg = load_config(mock_yaml_config)
    assert cfg.name == "fixture-project"
    assert cfg.seed == 999
    assert cfg.parameters.get("learning_rate") == 0.001


def test_load_json_config(tmp_path: Path) -> None:
    """Verify loading from a JSON file."""
    json_path = tmp_path / "config.json"
    json_path.write_text(
        json.dumps({"project": {"name": "json-test", "seed": 7}}), encoding="utf-8"
    )
    cfg = load_config(json_path)
    assert cfg.name == "json-test"
    assert cfg.seed == 7


def test_load_config_missing_file() -> None:
    """Verify FileNotFoundError on missing configuration path."""
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent_path_12345.yaml")


def test_load_config_unsupported_ext(tmp_path: Path) -> None:
    """Verify ValueError on unsupported file extension."""
    txt_path = tmp_path / "config.txt"
    txt_path.write_text("hello: world", encoding="utf-8")
    with pytest.raises(ValueError, match="Unsupported config extension"):
        load_config(txt_path)
