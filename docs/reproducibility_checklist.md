# Reproducibility Checklist

- [x] Dependencies are listed in `requirements.txt`.
- [x] Main experiment source is `scripts/run_experiments.py`.
- [x] Paper generator is `scripts/write_paper.py`.
- [x] Main outputs are `results/episode_results.csv`, `results/summary.csv`, and `results/ablation_summary.csv`.
- [x] V2 outputs are `results/posterior_threshold_sweep.csv` and `results/posterior_threshold_sweep_table.tex`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical batch PDF path is `C:/Users/wangz/Downloads/21.pdf`.
- [x] Local `paper/main.pdf` is deleted after copying the canonical PDF to Downloads.

Recommended verification commands:

```powershell
python scripts\run_experiments.py
python scripts\write_paper.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
