"""Agentic Research Framework (ARF) - Autonomous multi-agent research package."""

from .config import ProjectConfig, load_config
from .pipeline import EvaluationResult, run_pipeline

__version__ = "0.1.0"
__all__ = ["ProjectConfig", "load_config", "EvaluationResult", "run_pipeline"]
