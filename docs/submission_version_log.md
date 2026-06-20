# Submission Version Log

## v3-link-hardening - 2026-06-20

- Added explicit VLA-style `hyperref` boxed-link styling to `paper/main.tex`.
- Rebuilt and re-exported the canonical PDF to `C:\Users\wangz\Downloads\21.pdf`.
- Verified final PDF: 26 pages, 428,709 bytes, SHA256 `C282912BC81046BD1B51C69B60DCEAF3B6798E89CD43F59638BE0FD76CF51F8C`.
- Verified 124 link annotations: green = 118, red = 6, cyan = 0, with one-point borders on pages `[(2, 41), (3, 28), (6, 2), (7, 1), (10, 1), (12, 4), (13, 21), (14, 19), (15, 6), (20, 1)]`.

## v3 final full-scale - 2026-06-14

- Added `docs/full_scale_execution_plan.md`.
- Added `experiments/full_scale_precontact.py`.
- Ran a five-family full-scale suite: 191,384 rows, 26,000 cases, seed 21021.
- Added generated tables under `results/full_scale/tex/` and figures under `figures/full_scale/`.
- Rewrote `paper/main.tex` into a 26-page final manuscript.
- Exported final PDF to `C:\Users\wangz\Downloads\21.pdf`.
- Final SHA256 before the 2026-06-20 link-style hardening: `A3CE9BC0033548239FD9C10F2B2C8835D2BAA567F1B7DB887665F4B32CDAE27A`.

## v2 - 2026-06-13

- Added posterior-threshold sweep to the original synthetic benchmark.
- Narrowed claim after tuned posterior-only exceeded the v2 guard.

## v1 - 2026-06-11

- Original generated precontact cue-control paper with literature sweep, synthetic timing experiment, ICLR-style manuscript, and public GitHub repository.
