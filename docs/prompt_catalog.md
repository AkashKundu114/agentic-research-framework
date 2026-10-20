# Prompt Catalog: Goals & Self-Improvement Loops

The **Agentic Research Framework (ARF)** provides a comprehensive library of battle-tested prompts under [`prompts/antigravity/`](../prompts/antigravity/). These prompts guide autonomous agents through structured milestones and bounded execution loops.

---

## 1. Research Goals (`prompts/antigravity/goals/`)

Goals are milestone-driven instructions that guide agents through specific research phases:

| Goal ID | File | Description & Scope |
|:---|:---|:---|
| **`00`** | [`00_system_alignment.md`](../prompts/antigravity/goals/00_system_alignment.md) | Initial environment check, Git status, package installation, and tool verification. |
| **`01`** | [`01_baseline_reproduction.md`](../prompts/antigravity/goals/01_baseline_reproduction.md) | Reproducing initial baseline numbers and logging seed-deterministic metrics to `results/`. |
| **`02`** | [`02_experiment_matrix.md`](../prompts/antigravity/goals/02_experiment_matrix.md) | Scaling out grid and random parameter searches across benchmark datasets. |
| **`10`** | [`10_data_curation_and_provenance.md`](../prompts/antigravity/goals/10_data_curation_and_provenance.md) | Dataset acquisition, checksum verification (`SHA-256`), and leakage-free splits. |
| **`15`** | [`15_feature_engineering_and_ablation.md`](../prompts/antigravity/goals/15_feature_engineering_and_ablation.md) | Feature transformations, dimensionality reduction, and component contribution tracking. |
| **`20`** | [`20_model_architecture_and_extension.md`](../prompts/antigravity/goals/20_model_architecture_and_extension.md) | Implementing novel algorithmic extensions, layers, or loss functions. |
| **`25`** | [`25_uncertainty_and_calibration.md`](../prompts/antigravity/goals/25_uncertainty_and_calibration.md) | Conformal prediction intervals, temperature scaling, and reliability diagrams. |
| **`30`** | [`30_statistical_rigor_and_significance.md`](../prompts/antigravity/goals/30_statistical_rigor_and_significance.md) | Wilcoxon signed-rank tests, Bonferroni corrections, and bootstrap confidence intervals. |
| **`35`** | [`35_scalability_and_profiling.md`](../prompts/antigravity/goals/35_scalability_and_profiling.md) | Profiling memory footprint, GPU utilization, asymptotic complexity, and cache hit rates. |
| **`40`** | [`40_failure_mode_falsification.md`](../prompts/antigravity/goals/40_failure_mode_falsification.md) | Stress-testing models under extreme noise, missing features, and adversarial outliers. |
| **`45`** | [`45_figure_generation_and_styling.md`](../prompts/antigravity/goals/45_figure_generation_and_styling.md) | Automated publication-ready figure rendering (`PDF`/`EPS`/`SVG`) at 300+ DPI. |
| **`50`** | [`50_manuscript_macro_synchronization.md`](../prompts/antigravity/goals/50_manuscript_macro_synchronization.md) | Exporting frozen metrics to `numbers.tex` and updating LaTeX tables. |
| **`60`** | [`60_peer_review_audit_and_hardening.md`](../prompts/antigravity/goals/60_peer_review_audit_and_hardening.md) | Comprehensive pre-submission audit mimicking rigorous peer review. |

---

## 2. Bounded Iteration Loops (`prompts/antigravity/loops/`)

Loops are self-correcting prompt cycles where agents test, measure, and refine implementations under strict safety constraints:

> [!IMPORTANT]
> **Safety Rule:** Every autonomous loop enforces a hard ceiling of **at most 5 iterations per session**.

| Loop ID | File | Focus & Termination Condition |
|:---|:---|:---|
| **`01`** | [`01_bounded_execution_loop.md`](../prompts/antigravity/loops/01_bounded_execution_loop.md) | Core test-driven development loop: code $\to$ test $\to$ refine $\to$ pass. |
| **`02`** | [`02_reproducibility_verification_loop.md`](../prompts/antigravity/loops/02_reproducibility_verification_loop.md) | Runs pipeline twice with identical seeds; fails if metric delta $> 10^{-7}$. |
| **`03`** | [`03_release_gate_loop.md`](../prompts/antigravity/loops/03_release_gate_loop.md) | Final release validation: tests, types, linter, docs, and git cleanliness. |
| **`04`** | [`04_redteam_adversarial_loop.md`](../prompts/antigravity/loops/04_redteam_adversarial_loop.md) | Evaluates robustness against random Gaussian noise, feature dropout, and extreme $D \gg N$. |
| **`05`** | [`05_ablation_hypothesis_loop.md`](../prompts/antigravity/loops/05_ablation_hypothesis_loop.md) | Systematically disables components to validate scientific hypotheses H1 through H4. |
| **`06`** | [`06_performance_profiling_loop.md`](../prompts/antigravity/loops/06_performance_profiling_loop.md) | Identifies runtime bottlenecks using `cProfile` and memory profilers. |
| **`07`** | [`07_manuscript_macro_sync_loop.md`](../prompts/antigravity/loops/07_manuscript_macro_sync_loop.md) | Syncs JSON results to `paper/numbers.tex` and validates LaTeX compilation. |
| **`08`** | [`08_data_leakage_audit_loop.md`](../prompts/antigravity/loops/08_data_leakage_audit_loop.md) | Audits split boundaries to guarantee zero feature leakage into preprocessing. |

---

## 3. Custom Prompt Synthesis Protocol

To adapt these prompts for any arbitrary new repository, ARF includes the **Custom Prompt Generator** located at:
[`prompts/antigravity/templates/custom_prompt_generator.md`](../prompts/antigravity/templates/custom_prompt_generator.md)

### Three-Phase Protocol:
1. **Multi-Subagent Deep Dive:** Launch parallel subagents to inspect project architecture, data boundaries, and verification suites.
2. **Custom Prompt Synthesis:** Automatically generate repository-tailored goal prompts and execution plans.
3. **Phased Execution:** Execute the planned milestones with automated testing and git checkpointing after each phase.
