"""Unit tests for the arf / research-cli entrypoint."""

from __future__ import annotations

from pathlib import Path

import pytest

from agentic_research.cli import main


def test_cli_info(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify info subcommand runs without errors."""
    code = main(["info"])
    assert code == 0
    captured = capsys.readouterr()
    assert "=== Agentic Research Framework (ARF) Info ===" in captured.out


def test_cli_run(tmp_path: Path) -> None:
    """Verify run subcommand creates metric artifact."""
    out_file = tmp_path / "cli_run.json"
    code = main(["run", "--samples", "20", "--output", str(out_file)])
    assert code == 0
    assert out_file.is_file()


def test_cli_eval(tmp_path: Path) -> None:
    """Verify eval subcommand inspects existing metrics."""
    out_file = tmp_path / "eval_metrics.json"
    main(["run", "--samples", "10", "--output", str(out_file)])

    code = main(["eval", "--metrics", str(out_file)])
    assert code == 0


def test_cli_eval_missing_file() -> None:
    """Verify eval returns non-zero code on missing metrics file."""
    code = main(["eval", "--metrics", "missing_artifact_xyz.json"])
    assert code == 1
