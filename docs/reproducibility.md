# Scientific Reproducibility Protocol & Manifest Standards

This document establishes the reproducibility protocols, artifact provenance guidelines, and determinism policies enforced across all research projects developed with the **Agentic Research Framework (ARF)**.

---

## 1. Core Reproducibility Principles

Scientific claims must be reproducible by independent researchers and auditable by autonomous verification loops. All experiments conform to the following six tenets:

1. **Immutable Raw Data:** Raw benchmark files in `data/raw/` are write-protected and hash-verified (`SHA-256`). Preprocessing scripts must be purely deterministic functions from `data/raw/` to `data/processed/`.
2. **Deterministic Seed Control:** Every pipeline run, benchmark, split, and baseline evaluation consumes an explicit integer seed. Pseudo-random generators (`random`, `numpy.random`, `torch.manual_seed`) must be deterministically initialized.
3. **Single Source of Truth:** All numerical claims, table cells, and statistical significance values presented in manuscripts originate from frozen JSON result registries (`results/*.json`). No human or AI agent may hardcode numbers into LaTeX.
4. **Environment Freezing:** Experimental environments must be reproducible across operating systems using locked dependency specifications (`pyproject.toml`, `requirements.lock`, or `uv.lock`).
5. **Ablation & Baseline Equity:** All comparisons between novel algorithms and baselines must occur on identical preprocessed data splits under identical compute budgets and parameter grids.
6. **Provenance Tracking:** Every generated figure and table in `results/figures/` and `results/tables/` maps back to an executable generation script in `scripts/`.

---

## 2. Experiment Run Manifest Standard

Every experimental run logged by `scripts/run_experiment.py` or `arf run` records an immutable JSON provenance record containing:

```json
{
  "experiment_id": "exp01_baseline_benchmark",
  "timestamp_iso": "2026-10-20T14:46:12+00:00",
  "git_commit": "a1b2c3d4e5f67890123456789abcdef012345678",
  "git_dirty": false,
  "config": {
    "name": "baseline-experiment",
    "seed": 42,
    "parameters": {
      "learning_rate": 0.001,
      "batch_size": 64,
      "num_samples": 500
    }
  },
  "environment": {
    "python_version": "3.10.14",
    "platform": "Linux-6.5.0-generic-x86_64",
    "cpu_model": "AMD EPYC 7763 64-Core Processor",
    "gpu_model": "NVIDIA A100-SXM4-80GB",
    "driver_version": "535.129.03",
    "cuda_version": "12.2"
  },
  "metrics": {
    "accuracy": 0.8471,
    "macro_f1": 0.8392,
    "stability_index": 0.6121,
    "runtime_seconds": 4.1205
  },
  "artifact_checksums": {
    "model_checkpoint": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "predictions_parquet": "sha256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"
  }
}
```

---

## 3. Data Hygiene & Leakage Prevention Checklist

Before training models or reporting evaluation scores, AI agents and engineers must verify:
- [ ] **Split Independence:** Train, validation, and test splits were computed before any normalization, imputation, or feature scaling.
- [ ] **Leakage Audit:** Scalers (e.g. `StandardScaler`) and encoders are fit *strictly* on training data and applied transformationally to test data.
- [ ] **Subspace Independence:** Unsupervised feature extraction or subspace selection does not access test labels.
- [ ] **Temporal Discipline:** If working with time-series or sequential data, splits enforce chronological order with zero forward lookahead.

---

## 4. Verification Workflow

Run the automated verification suite before publishing results:

```bash
# 1. Run unit and integration tests
python -m pytest tests/ -v

# 2. Verify static typing and style constraints
python -m ruff check src tests scripts
python -m mypy src tests scripts

# 3. Execute bounded reproducibility loop
# (Checks hash determinism across consecutive runs with identical seed)
python scripts/run_experiment.py --config experiments/configs/baseline.yaml
```
