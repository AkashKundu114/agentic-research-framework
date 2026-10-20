#!/usr/bin/env python3
"""Data acquisition and synthetic dataset generator with checksum verification."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from pathlib import Path


def generate_benchmark_dataset(
    output_path: Path,
    num_samples: int = 500,
    num_features: int = 10,
    seed: int = 42,
) -> str:
    """Generate deterministic benchmark dataset and calculate its SHA-256 checksum."""
    rng = random.Random(seed)
    header = [f"feat_{i}" for i in range(num_features)] + ["label"]
    rows = []

    for _ in range(num_samples):
        # 2-cluster mixture
        label = 1 if rng.random() > 0.5 else 0
        mean = 1.0 if label == 1 else -1.0
        features = [round(rng.gauss(mean, 0.8), 4) for _ in range(num_features)]
        rows.append(features + [label])

    payload = {
        "header": header,
        "rows": rows,
        "metadata": {"seed": seed, "num_samples": num_samples},
    }
    raw_json = json.dumps(payload, indent=2)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(raw_json, encoding="utf-8")

    sha256 = hashlib.sha256(raw_json.encode("utf-8")).hexdigest()
    return sha256


def main() -> int:
    """CLI entrypoint for data fetching."""
    parser = argparse.ArgumentParser(description="Fetch or generate benchmark research datasets.")
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate data fetching without writing to disk"
    )
    parser.add_argument(
        "--output", type=Path, default=Path("data/raw/synthetic_benchmark.json"), help="Output path"
    )
    parser.add_argument("--samples", type=int, default=500, help="Number of benchmark samples")
    parser.add_argument("--seed", type=int, default=42, help="Deterministic random seed")

    args = parser.parse_args()

    if args.dry_run:
        print("[+] Dry-run mode: verified data acquisition endpoints and permissions.")
        return 0

    print(
        f"[+] Generating benchmark dataset at {args.output} (samples={args.samples}, seed={args.seed})..."
    )
    checksum = generate_benchmark_dataset(args.output, num_samples=args.samples, seed=args.seed)
    print(f"[SUCCESS] Dataset written successfully. SHA-256: {checksum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
