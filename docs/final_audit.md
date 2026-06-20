# Final Audit

## Decision

Paper21 is a final v3 synthetic mechanism paper under the strict batch standard. It is 26 pages and supported by a full-scale experiment suite, but it remains a synthetic paper rather than a real-robot systems claim.

## Final PDF

- Path: `C:\Users\wangz\Downloads\21.pdf`
- Pages: 26
- Bytes: 428,709
- SHA256: `C282912BC81046BD1B51C69B60DCEAF3B6798E89CD43F59638BE0FD76CF51F8C`
- VLA-style link markers: 124 link annotations; pages `[(2, 41), (3, 28), (6, 2), (7, 1), (10, 1), (12, 4), (13, 21), (14, 19), (15, 6), (20, 1)]`; colors green = 118, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- Visual link-page render check: pages 2, 3, 6, 7, 10, 12, 13, 14, 15, and 20 show green citation/URL boxes and red internal-reference boxes matching the visible VLA-v4 role model.
- Local `paper/main.pdf`: removed

## Full-Scale Evidence

- Stage: complete
- Seed: 21021
- Rows: 191,384
- Cases: 26,000
- Plot failures: 0
- Results directory: `results/full_scale/`
- Figures directory: `figures/full_scale/`

## Strongest Results

- Normal calibrated deadline guard safe success: 0.814.
- Normal contact-reactive safe success: 0.286.
- High-latency calibrated deadline guard safe success: 0.542 versus fixed posterior 0.500.
- Cost-asymmetry mean cost: calibrated deadline guard 1.333 versus fixed posterior 1.550.
- Onset-late shift safe success: calibrated deadline guard 0.512 versus source-tuned posterior 0.292.

## Hard Boundaries

- No real robot experiment.
- Synthetic cue and impulse model.
- Tuned posterior remains a strong baseline and wins in some regimes.
- Risk guard extension fails and is reported as a negative result.

## Readiness Judgment

Submission-ready as a full synthetic mechanism/diagnostic paper. Not sufficient as a main-track real-robot manipulation claim without hardware validation, measured switch latency, calibrated sensor data, and learned baselines.
