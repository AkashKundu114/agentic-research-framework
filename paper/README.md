# Manuscript and Publication Assets

This directory contains manuscript sources, LaTeX files, and publication artifacts for the project.

## GitHub Repository Policy
To keep the public repository lightweight, maintain preprint/peer-review anonymity, and prevent premature disclosure before publication:
- LaTeX source files (`paper.tex`, `main.tex`, `*.tex`), bibliography files (`*.bib`), formatting styles (`*.cls`, `*.bst`), and compiled PDFs (`*.pdf`) are **excluded from Git tracking** via `.gitignore`.
- Rendered high-resolution figures (`figures/`) are generated programmatically via reproducible scripts in `scripts/` or `experiments/` rather than stored in version control.

## Local Manuscript Structure
When working on the manuscript locally, organize your assets as follows:
```text
paper/
├── README.md               # This documentation file (tracked in Git)
├── paper.tex (or main.tex) # Main manuscript LaTeX source (local only)
├── references.bib          # BibTeX bibliography references (local only)
├── figures/                # Vector/raster figures generated from experiments (local only)
│   └── README.md           # Figure manifest and reproduction commands
├── tables/                 # Auto-generated LaTeX tables from results (local only)
└── submission/             # Venue-specific packages / camera-ready files
```

## Reproducing Figures & Tables
Do not manually edit figures or tables. Use the designated analysis scripts:
```bash
# Example: generate all manuscript figures and tables from experiment results
python scripts/generate_figures.py
python scripts/generate_tables.py
```

## Compiling the Manuscript Locally
Compile the document using standard LaTeX tooling (TeX Live, MacTeX, or MiKTeX):
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```
Or if using latexmk:
```bash
latexmk -pdf paper.tex
```

## Citation & Preprints
If citing the work associated with this repository prior to formal publication, please refer to the `CITATION.cff` or root `README.md`.
