# Child Status

- Stage: v3 final full-scale hardening complete
- Last update: 2026-06-14
- Current focus: final PDF exported to Downloads; local `paper/main.pdf` removed; docs updated for v3 evidence

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

## Final PDF

- Path: `C:\Users\wangz\Downloads\21.pdf`
- Pages: 26
- Bytes: 364,070
- SHA256: `A3CE9BC0033548239FD9C10F2B2C8835D2BAA567F1B7DB887665F4B32CDAE27A`

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

- Commit and push v3.
- Verify clean tree and `HEAD == @{u}` before moving to Paper22.
