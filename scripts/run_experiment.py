#!/usr/bin/env python3
"""Execute a parameterized experiment configuration with provenance logging."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from agentic_research.config import load_config
from agentic_research.pipeline import run_pipeline


def main() -> int:
    """CLI entrypoint for running an experiment."""
    parser = argparse.ArgumentParser(description="Run experiment according to config specification.")
    parser.add_argument("--config", type=Path, default=Path("experiments/configs/baseline.yaml"), help="Config file")
    parser.add_argument("--output-dir", type=Path, default=Path("results"), help="Results directory")

    args = parser.parse_args()

    try:
        cfg = load_config(args.config)
        print(f"[+] Loaded experiment config from: {args.config}")
        print(f"    Experiment Name: {cfg.name} (seed={cfg.seed})")

        num_samples = int(cfg.parameters.get("num_samples", 150))
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        artifact_path = args.output_dir / f"{cfg.name}_{timestamp}_metrics.json"

        result = run_pipeline(config=cfg, num_samples=num_samples, artifact_path=artifact_path)
        print(f"[SUCCESS] Experiment completed in {result.runtime_seconds:.4f}s")
        print(f"          Metrics: {result.metrics}")
        print(f"          Saved to: {artifact_path}")
        return 0
    except Exception as e:
        print(f"[!] Experiment execution failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
