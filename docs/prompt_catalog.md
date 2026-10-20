# Prompt Catalog: Goals & Self-Improvement Loops

The **Agentic Research Framework (ARF)** provides a comprehensive library of battle-tested prompts under `prompts/antigravity/`. These prompts guide autonomous agents through structured milestones and bounded execution loops.

---

## 1. Research Goals (`prompts/antigravity/goals/`)

Goals are milestone-driven instructions that guide agents through specific research phases:

| Goal ID | File | Description & Scope |
|:---|:---|:---|
| **`00`** | [`00-repository-baseline-and-plan.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/00-repository-baseline-and-plan.md) | Initial environment check, Git status, package installation, and tool verification. |
| **`01`** | [`01-multi-agent-codebase-research-and-custom-prompts.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/01-multi-agent-codebase-research-and-custom-prompts.md) | Reproducing initial baseline numbers and logging seed-deterministic metrics to `results/`. |
| **`02`** | [`02-hypothesis-and-claim-matrix-audit.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/02-hypothesis-and-claim-matrix-audit.md) | Scaling out grid and random parameter searches across benchmark datasets. |
| **`10`** | [`10-code-quality-and-maintainability.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/10-code-quality-and-maintainability.md) | Dataset acquisition, checksum verification (`SHA-256`), and leakage-free splits. |
| **`15`** | [`15-test-suite-expansion-and-edge-cases.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/15-test-suite-expansion-and-edge-cases.md) | Feature transformations, dimensionality reduction, and component contribution tracking. |
| **`20`** | [`20-security-privacy-and-prompt-injection.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/20-security-privacy-and-prompt-injection.md) | Implementing novel algorithmic extensions, layers, or loss functions. |
| **`25`** | [`25-data-pipeline-and-leakage-audit.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/25-data-pipeline-and-leakage-audit.md) | Conformal prediction intervals, temperature scaling, and reliability diagrams. |
| **`30`** | [`30-performance-and-resource-efficiency.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/30-performance-and-resource-efficiency.md) | Wilcoxon signed-rank tests, Bonferroni corrections, and bootstrap confidence intervals. |
| **`35`** | [`35-gpu-acceleration-and-memory-profiling.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/35-gpu-acceleration-and-memory-profiling.md) | Profiling memory footprint, GPU utilization, asymptotic complexity, and cache hit rates. |
| **`40`** | [`40-research-reproducibility-and-paper-audit.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/40-research-reproducibility-and-paper-audit.md) | Stress-testing models under extreme noise, missing features, and adversarial outliers. |
| **`45`** | [`45-manuscript-and-typesetting-audit.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/45-manuscript-and-typesetting-audit.md) | Automated publication-ready figure rendering (`PDF`/`EPS`/`SVG`) at 300+ DPI. |
| **`50`** | [`50-production-readiness-and-documentation.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/50-production-readiness-and-documentation.md) | Exporting frozen metrics to `numbers.tex` and updating LaTeX tables. |
| **`60`** | [`60-baseline-fairness-and-benchmarking-parity.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/goals/60-baseline-fairness-and-benchmarking-parity.md) | Comprehensive pre-submission audit mimicking rigorous peer review. |

---

## 2. Bounded Iteration Loops (`prompts/antigravity/loops/`)

Loops are self-correcting prompt cycles where agents test, measure, and refine implementations under strict safety constraints:

> [!IMPORTANT]
> **Safety Rule:** Every autonomous loop enforces a hard ceiling of **at most 5 iterations per session**.

| Loop ID | File | Focus & Termination Condition |
|:---|:---|:---|
| **`01`** | [`01-bounded-improvement-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/01-bounded-improvement-loop.md) | Core test-driven development loop: code $\to$ test $\to$ refine $\to$ pass. |
| **`02`** | [`02-research-reproducibility-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/02-research-reproducibility-loop.md) | Runs pipeline twice with identical seeds; fails if metric delta $> 10^{-7}$. |
| **`03`** | [`03-regression-and-release-gate.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/03-regression-and-release-gate.md) | Final release validation: tests, types, linter, docs, and git cleanliness. |
| **`04`** | [`04-red-team-adversarial-audit-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/04-red-team-adversarial-audit-loop.md) | Evaluates robustness against random Gaussian noise, feature dropout, and extreme $D \gg N$. |
| **`05`** | [`05-ablation-and-hypotheses-verification-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/05-ablation-and-hypotheses-verification-loop.md) | Systematically disables components to validate scientific hypotheses H1 through H4. |
| **`06`** | [`06-performance-profiling-and-optimization-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/06-performance-profiling-and-optimization-loop.md) | Identifies runtime bottlenecks using `cProfile` and memory profilers. |
| **`07`** | [`07-manuscript-macro-sync-and-typesetting-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/07-manuscript-macro-sync-and-typesetting-loop.md) | Syncs JSON results to `paper/numbers.tex` and validates LaTeX compilation. |
| **`08`** | [`08-data-integrity-and-leakage-detection-loop.md`](https://github.com/AkashKundu114/agentic-research-framework/blob/main/prompts/antigravity/loops/08-data-integrity-and-leakage-detection-loop.md) | Audits split boundaries to guarantee zero feature leakage into preprocessing. |

---

## 3. Custom Prompt Synthesis Protocol

To adapt these prompts for any arbitrary new repository, ARF includes custom prompt templates under `prompts/antigravity/custom/` and iteration log templates under `prompts/antigravity/templates/`.

### Three-Phase Protocol:
1. **Multi-Subagent Deep Dive:** Launch parallel subagents to inspect project architecture, data boundaries, and verification suites.
2. **Custom Prompt Synthesis:** Automatically generate repository-tailored goal prompts and execution plans.
3. **Phased Execution:** Execute the planned milestones with automated testing and git checkpointing after each phase.
