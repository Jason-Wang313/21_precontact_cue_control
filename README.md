# 21 Precontact Cue Control

Anonymous ICLR-style paper artifact for the 60-paper robotics/embodied-intelligence batch.

## Thesis

Precontact cues should act as latency-aware controller guards for switching grasp strategy before first contact when the switch has nonzero activation latency. The v3 claim is bounded: calibrated deadline guards are useful in latency-limited, noisy, shifted, and cost-asymmetric regimes, but tuned posterior thresholds remain strong and sometimes win.

## Final v3 Status

- Final PDF: `C:\Users\wangz\Downloads\21.pdf`
- Page count: 26
- File size: 364,070 bytes
- SHA256: `A3CE9BC0033548239FD9C10F2B2C8835D2BAA567F1B7DB887665F4B32CDAE27A`
- Local build PDF: `paper/main.pdf` removed after export
- Full-scale suite: 191,384 policy rows over 26,000 cases, seed 21021, zero plot failures

## Reproduce

```powershell
python experiments\full_scale_precontact.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Do not run `scripts/build_paper.ps1` for intermediate builds under the strict batch workflow because it copies to Downloads. Copy to Downloads only after the final PDF passes page-count and text checks.

## Key Artifacts

- `docs/full_scale_execution_plan.md`: per-paper v3 execution plan written before substantive edits.
- `experiments/full_scale_precontact.py`: v3 full-scale runner.
- `results/full_scale/metadata.json`: final run metadata.
- `results/full_scale/tex/`: generated paper tables.
- `figures/full_scale/`: generated figures.
- `docs/evidence_summary.md`: headline full-scale evidence.
- `paper/main.tex`: final v3 manuscript source.
