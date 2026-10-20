# Data Management and Provenance

This directory manages all raw, intermediate, and processed datasets required for experiments.

## GitHub Data Policy
In accordance with scientific reproducibility best practices and repository size constraints:
- **No large data binaries or raw datasets are committed to Git.**
- Only directory structure markers (`.gitkeep`) and documentation (`README.md`) are tracked.
- All datasets must be obtained or generated via reproducible automated scripts.

## Directory Layout
```text
data/
├── raw/        # Original, immutable downloads or raw input files (never edit directly)
├── interim/    # Intermediate representations, cached preprocessed features, or cleaned dumps
├── processed/  # Canonical, model-ready benchmark splits (train / val / test)
└── cache/      # Fast-access memory-mapped tensors or numpy arrays (.npz, .h5ad)
```

## Dataset Acquisition and Preprocessing
To download and preprocess datasets locally, run the data provisioning scripts:
```bash
# Fetch and verify raw data archives (SHA-256 validated)
python scripts/fetch_data.py

# Preprocess and generate canonical splits
python scripts/preprocess_data.py
```

## Dataset Metadata & Provenance Template
For each external dataset incorporated into this research, document:
| Field | Description |
| :--- | :--- |
| **Name & Version** | e.g., MNIST v1.0, Madelon, Leukemia |
| **Origin / URL** | Canonical download endpoint or repository ID (OpenML, Zenodo, Hugging Face) |
| **License / Terms** | Open access license (e.g. CC-BY-4.0, MIT, Academic Non-Commercial) |
| **Checksum (SHA-256)**| Secure hash of the downloaded archive for integrity verification |
| **Split Strategy** | Predefined fold splits, random seeds, or stratified partitions |
| **Preprocessing** | Normalization, imputation, dimensionality reduction applied |

## Ethics, Privacy, and Synthetic Data
- For human-derived or sensitive data, ensure anonymization, consent, and IRB/ethics compliance.
- For local agent tests and continuous integration (CI), always provide lightweight synthetic fixtures in `tests/data/` or via programmatic generators.
