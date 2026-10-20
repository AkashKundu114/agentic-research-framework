#!/usr/bin/env python3
"""Data preprocessing and leakage-free dataset split generator."""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path


def split_data(
    input_path: Path,
    output_dir: Path,
    train_ratio: float = 0.7,
    seed: int = 42,
) -> None:
    """Read raw dataset, apply normalization fitted strictly on train split, and emit splits."""
    if not input_path.is_file():
        raise FileNotFoundError(f"Input data file not found: {input_path}")

    data = json.loads(input_path.read_text(encoding="utf-8"))
    rows = data["rows"]
    header = data["header"]

    rng = random.Random(seed)
    shuffled = list(rows)
    rng.shuffle(shuffled)

    n_total = len(shuffled)
    n_train = int(n_total * train_ratio)
    train_rows = shuffled[:n_train]
    test_rows = shuffled[n_train:]

    # Compute feature means and stds ONLY on training set to prevent leakage
    num_feats = len(header) - 1
    means = [sum(r[i] for r in train_rows) / max(1, len(train_rows)) for i in range(num_feats)]
    stds = [
        (sum((r[i] - means[i]) ** 2 for r in train_rows) / max(1, len(train_rows))) ** 0.5
        for i in range(num_feats)
    ]
    stds = [s if s > 1e-6 else 1.0 for s in stds]

    def scale_rows(subset: list[list[float]]) -> list[list[float]]:
        scaled = []
        for r in subset:
            feats = [(r[i] - means[i]) / stds[i] for i in range(num_feats)]
            scaled.append(feats + [r[-1]])
        return scaled

    output_dir.mkdir(parents=True, exist_ok=True)
    train_file = output_dir / "train.json"
    test_file = output_dir / "test.json"

    train_file.write_text(json.dumps({"header": header, "rows": scale_rows(train_rows)}, indent=2), encoding="utf-8")
    test_file.write_text(json.dumps({"header": header, "rows": scale_rows(test_rows)}, indent=2), encoding="utf-8")

    print(f"[+] Saved {len(train_rows)} train rows to {train_file}")
    print(f"[+] Saved {len(test_rows)} test rows to {test_file}")


def main() -> int:
    """CLI entrypoint for data preprocessing."""
    parser = argparse.ArgumentParser(description="Preprocess raw datasets into leakage-free train/test splits.")
    parser.add_argument("--input", type=Path, default=Path("data/raw/synthetic_benchmark.json"), help="Raw data file")
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed"), help="Processed output directory")
    parser.add_argument("--seed", type=int, default=42, help="Split seed")

    args = parser.parse_args()
    try:
        split_data(args.input, args.output_dir, seed=args.seed)
        return 0
    except Exception as e:
        print(f"[!] Preprocessing error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
