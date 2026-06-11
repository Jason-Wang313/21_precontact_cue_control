# Plan

## Objective

Produce a complete, runnable, anonymous ICLR-style robotics paper for paper 21, starting from the seed idea "Precontact Cue Control" but choosing the final thesis only after an adversarial literature sweep.

## Required outputs

- `docs/related_work_matrix.csv` with at least 1000 literature entries.
- `docs/literature_map.md`.
- `docs/hostile_prior_work.md`.
- `docs/novelty_boundary_map.md`.
- `docs/novelty_decision.md`.
- `docs/claims.md`.
- `docs/reviewer_attacks.md`.
- `docs/final_audit.md`.
- Runnable code and cached experiment artifacts.
- Compiled anonymous ICLR-style PDF saved only to `C:/Users/wangz/Downloads/21.pdf`.
- Public GitHub repository `21_precontact_cue_control`, or documented failure with recovery details.

## Execution stages

1. Initialize status tracking and inspect reusable folder contents without deleting anything.
2. Retrieve and cache a broad manipulation/tactile/precontact literature landscape, targeting at least 1000 candidate papers.
3. Build a 1000-entry related-work matrix, a 300-paper serious skim, a 200-250-paper deeper synthesis set, and a 100-paper hostile prior-work set.
4. Identify hidden assumptions, novelty boundaries, reviewer attacks, and candidate directions; choose the strongest thesis only after the sweep.
5. Implement a small runnable embodied-manipulation simulation that tests whether precontact cues should trigger strategy switching before contact.
6. Run experiments with cached outputs and bounded timeouts.
7. Write the paper in an anonymous ICLR-style LaTeX template, with honest claims tied to evidence.
8. Build the PDF with direct `pdflatex`/`bibtex` passes and repair LaTeX/BibTeX issues if needed.
9. Save the final PDF to `C:/Users/wangz/Downloads/21.pdf`.
10. Create or update the public GitHub repo `21_precontact_cue_control`, push all artifacts, and record the GitHub URL or the exact failure.
11. Write the final audit with the required twelve answers and current Desktop-copy status.

## Safety rules for this run

- Use bounded helper scripts for literature, experiments, plotting, and build steps.
- Avoid brittle inline PowerShell and uncaught expected nonzero exits.
- Avoid destructive cleanup of existing artifacts.
- Keep `child_status.md` compact and rewrite it from current facts when updating.
- Prefer direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` with generous timeouts over `latexmk`.
