#!/usr/bin/env python3
"""Convenience root runner for Agentic Research Framework (works without pip install)."""

import sys
from pathlib import Path

# Add src to sys.path for direct out-of-the-box execution
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from agentic_research.cli import main

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("info")
    sys.exit(main())
