"""Command-line interface for the Agentic Research Framework (ARF)."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from .config import load_config
from .pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    """Construct command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="arf",
        description="Agentic Research Framework (ARF) CLI - Reproducible experiment runner and evaluation suite.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: info
    parser_info = subparsers.add_parser(
        "info", help="Display project configuration and environment info"
    )
    parser_info.add_argument(
        "--config", type=Path, default=None, help="Path to project config YAML/JSON"
    )

    # Subcommand: run
    parser_run = subparsers.add_parser("run", help="Execute the evaluation pipeline")
    parser_run.add_argument("--config", type=Path, default=None, help="Path to config file")
    parser_run.add_argument("--samples", type=int, default=100, help="Number of samples to process")
    parser_run.add_argument(
        "--output", type=Path, default=Path("results/metrics.json"), help="Output metrics path"
    )

    # Subcommand: eval
    parser_eval = subparsers.add_parser(
        "eval", help="Evaluate existing results or verify artifacts"
    )
    parser_eval.add_argument(
        "--metrics", type=Path, default=Path("results/metrics.json"), help="Path to metrics JSON"
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Main CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "info":
        cfg = load_config(args.config)
        print("=== Agentic Research Framework (ARF) Info ===")
        print(f"Project Name : {cfg.name}")
        print(f"Random Seed  : {cfg.seed}")
        print(f"Data Dir     : {cfg.data_dir}")
        print(f"Results Dir  : {cfg.results_dir}")
        return 0

    if args.command == "run":
        cfg = load_config(args.config)
        print(f"[+] Running research pipeline (seed={cfg.seed}, samples={args.samples})...")
        result = run_pipeline(config=cfg, num_samples=args.samples, artifact_path=args.output)
        print(f"[SUCCESS] Completed in {result.runtime_seconds:.4f}s")
        print(f"          Metrics: {result.metrics}")
        print(f"          Artifact saved to: {args.output}")
        return 0

    if args.command == "eval":
        if not args.metrics.is_file():
            print(f"[ERROR] Metrics file not found: {args.metrics}", file=sys.stderr)
            return 1
        print(f"[+] Verified metrics artifact: {args.metrics}")
        print(args.metrics.read_text(encoding="utf-8"))
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
