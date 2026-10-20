"""Configuration management and schema validation for research runs."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore[import-untyped]
except ImportError:
    yaml = None


@dataclass(frozen=True)
class ProjectConfig:
    """Project-level configuration parameters."""

    name: str = "agentic-research-framework"
    seed: int = 42
    data_dir: Path = field(default_factory=lambda: Path("data"))
    results_dir: Path = field(default_factory=lambda: Path("results"))
    parameters: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectConfig:
        """Instantiate ProjectConfig from dictionary."""
        project_dict = data.get("project", data)
        return cls(
            name=str(project_dict.get("name", "agentic-research-framework")),
            seed=int(project_dict.get("seed", 42)),
            data_dir=Path(project_dict.get("data_dir", "data")),
            results_dir=Path(project_dict.get("results_dir", "results")),
            parameters=dict(data.get("parameters", {})),
        )


def load_config(config_path: Path | str | None = None) -> ProjectConfig:
    """Load configuration from a YAML or JSON file with graceful defaults.

    Args:
        config_path: Path to configuration file. If None, default ProjectConfig is returned.

    Returns:
        ProjectConfig instance.

    Raises:
        FileNotFoundError: If the specified configuration path does not exist.
        ValueError: If file format is not supported or YAML is unavailable.
    """
    if config_path is None:
        return ProjectConfig()

    path = Path(config_path)
    if not path.is_file():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    content = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(content)
    elif path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise ValueError(
                "PyYAML is required to parse YAML configs. Install with pip install pyyaml."
            )
        data = yaml.safe_load(content) or {}
    else:
        raise ValueError(f"Unsupported config extension: {path.suffix}")

    return ProjectConfig.from_dict(data)
