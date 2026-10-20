# Generated Research Figures

This directory holds figures generated during model evaluation, benchmarking, and sensitivity studies.

## Repository Policy
Figure image binaries (`*.png`, `*.jpg`, `*.svg`, `*.eps`) are excluded from version control via `.gitignore` to prevent bloated Git histories and avoid binary merge conflicts.

## Reproducing Figures
Figures can be regenerated automatically by running the corresponding experiment or plotting scripts:
```bash
# Generate all benchmark and evaluation figures
python scripts/generate_figures.py
```
Generated outputs will be saved directly into this directory.
