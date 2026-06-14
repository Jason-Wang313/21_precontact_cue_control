# Final Audit

## Decision

Paper21 is a final v3 synthetic mechanism paper under the strict batch standard. It is 26 pages and supported by a full-scale experiment suite, but it remains a synthetic paper rather than a real-robot systems claim.

## Final PDF

- Path: `C:\Users\wangz\Downloads\21.pdf`
- Pages: 26
- Bytes: 364,070
- SHA256: `A3CE9BC0033548239FD9C10F2B2C8835D2BAA567F1B7DB887665F4B32CDAE27A`
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
