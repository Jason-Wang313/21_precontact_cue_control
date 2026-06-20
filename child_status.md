# Child Status

- Stage: v3 final full-scale hardening complete; VLA-style boxed-link hardening complete
- Last update: 2026-06-20
- Current focus: final PDF exported to Downloads with VLA-style red/green boxed links; local `paper/main.pdf` removed; docs updated for v3 evidence

## Commands and Work Completed

- Wrote `docs/full_scale_execution_plan.md` before substantive v3 edits.
- Added `experiments/full_scale_precontact.py`.
- Ran `python experiments\full_scale_precontact.py`.
- Final full-scale run: 191,384 rows, 26,000 cases, seed 21021, plot failures 0.
- Rewrote `paper/main.tex` into a 26-page v3 manuscript with formal setup, full-scale experiments, negative controls, ablations, appendices, and audit notes.
- Built with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Verified local PDF text markers for `v3 final full-scale`, `191,384`, `26,000`, `0.814`, `1.333`, and `0.512`.
- Exported final PDF to `C:\Users\wangz\Downloads\21.pdf`.
- Removed local `paper/main.pdf`.
- Added explicit VLA-style `hyperref` boxed-link styling.
- Rebuilt with `scripts/build_paper.ps1`, exported to Downloads, and removed local `paper/main.pdf`.
- Rendered and visually checked affected link pages 2, 3, 6, 7, 10, 12, 13, 14, 15, and 20.

## Final PDF

- Path: `C:\Users\wangz\Downloads\21.pdf`
- Pages: 26
- Bytes: 428,709
- SHA256: `C282912BC81046BD1B51C69B60DCEAF3B6798E89CD43F59638BE0FD76CF51F8C`
- Link annotations: 124
- Link pages: `[(2, 41), (3, 28), (6, 2), (7, 1), (10, 1), (12, 4), (13, 21), (14, 19), (15, 6), (20, 1)]`
- Annotation colors: green = 118, red = 6, cyan = 0
- Border widths: `(0, 0, 1)` for all 124 link annotations

## Headline Evidence

- Normal contact-reactive safe success: 0.286.
- Normal fixed posterior safe success: 0.814.
- Normal calibrated deadline guard safe success: 0.814 with lower expected cost than fixed posterior.
- High-latency calibrated deadline guard safe success: 0.542 versus fixed posterior 0.500.
- Cost-asymmetry calibrated deadline guard mean cost: 1.333 versus fixed posterior 1.550.
- Onset-late shift calibrated deadline guard safe success: 0.512 versus source-tuned posterior 0.292.
- Risk guard underperforms and is reported as a negative method result.

## Remaining Weaknesses

- No real robot experiment.
- Synthetic cue/contact/impulse model.
- Tuned posterior thresholds remain strong and win in weak/early cue regimes.
- Learned policies are not evaluated.

## Next

- None remaining for Paper21 after commit/push and clean/upstream verification.
