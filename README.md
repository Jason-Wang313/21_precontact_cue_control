# 21 Precontact Cue Control

Anonymous ICLR-style paper artifact for the 60-paper robotics/embodied-intelligence batch.

## Thesis

Precontact cues should act as latency-aware hybrid-control guards for switching grasp strategy before first contact, rather than only as perception features.

## Reproduce

```powershell
python scripts/collect_literature.py
python scripts/analyze_literature.py
python scripts/run_experiments.py
python scripts/write_paper.py
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
```

The final PDF is copied to `C:/Users/wangz/Downloads/21.pdf` by the build script and the intermediate `paper/main.pdf` is removed afterward.

The v2 experiment also writes `results/posterior_threshold_sweep.csv` and
`results/posterior_threshold_sweep_table.tex`, a hostile tuned posterior-only
baseline that narrows the guard claim.

## Key Artifacts

- `docs/related_work_matrix.csv`: 1000-paper matrix.
- `docs/hostile_prior_work.md`: 100-paper hostile set.
- `docs/novelty_decision.md`: selected direction and rejected alternatives.
- `results/summary.csv`: aggregate experiment results.
- `results/posterior_threshold_sweep.csv`: v2 tuned posterior-only baseline.
- `paper/main.tex`: anonymous ICLR-style manuscript.

## Template

Template status: `already_present`. Source attempted: ICLR Master-Template `iclr2026.zip`.
