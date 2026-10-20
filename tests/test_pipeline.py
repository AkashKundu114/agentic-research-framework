"""Unit tests for pipeline execution, determinism, and reproducibility."""

from __future__ import annotations

from pathlib import Path

from agentic_research.config import ProjectConfig
from agentic_research.pipeline import generate_synthetic_data, run_pipeline


def test_synthetic_data_determinism() -> None:
    """Verify that identical seeds produce identical synthetic samples."""
    run1 = generate_synthetic_data(num_samples=50, seed=101)
    run2 = generate_synthetic_data(num_samples=50, seed=101)
    run3 = generate_synthetic_data(num_samples=50, seed=102)

    assert run1 == run2
    assert run1 != run3


def test_pipeline_execution(sample_config: ProjectConfig) -> None:
    """Verify pipeline runs and produces expected metric structures."""
    result = run_pipeline(config=sample_config, num_samples=80)

    assert result.status == "success"
    assert result.seed == 123
    assert result.num_samples == 80
    assert "accuracy" in result.metrics
    assert "stability_index" in result.metrics
    assert result.runtime_seconds >= 0.0


def test_pipeline_artifact_saving(sample_config: ProjectConfig, tmp_path: Path) -> None:
    """Verify evaluation results save to disk as valid JSON."""
    out_file = tmp_path / "out_metrics.json"
    result = run_pipeline(config=sample_config, num_samples=30, artifact_path=out_file)

    assert out_file.is_file()
    assert result.to_dict()["seed"] == 123
