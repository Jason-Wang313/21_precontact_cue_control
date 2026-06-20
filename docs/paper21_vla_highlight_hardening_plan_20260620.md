# Paper21 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Make `C:/Users/wangz/Downloads/21.pdf` match the visible VLA-v4 role
model's boxed-link behavior while preserving the final 26-page precontact cue
control paper:

- citation links use green one-point boxes;
- internal figure/table/section links use red one-point boxes;
- URL links use green one-point boxes;
- the final PDF is rebuilt through the repository build script, copied only to
  Downloads, visually checked, and leaves no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/21.pdf`
- Pages: 26
- Size: 364,070 bytes
- SHA256: `A3CE9BC0033548239FD9C10F2B2C8835D2BAA567F1B7DB887665F4B32CDAE27A`
- Local `paper/main.pdf`: absent
- Repository state: clean against `origin/master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[]`
- Annotation colors: none
- Border widths: none
- Link annotations: 0

Source finding:

- `paper/main.tex` is the active manuscript source.
- The preamble loads `\usepackage{url}` but does not load `hyperref`, so the
  current PDF has no visible citation/reference/URL boxes.
- The repository build script is `scripts/build_paper.ps1`. It runs
  `pdflatex`, `bibtex`, repeated `pdflatex`, copies `paper/main.pdf` to
  `C:/Users/wangz/Downloads/21.pdf`, and removes the local PDF.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\usepackage{hyperref}` and `\hypersetup` block in
   `paper/main.tex` near the existing URL package setup.
2. Rebuild with `scripts/build_paper.ps1`, preserving its copy-to-Downloads
   and remove-local-PDF behavior.
3. If the LaTeX log requests another pass for cross-references, run the final
   canonical pass and use only the final artifact metadata.
4. Recompute page count, byte size, SHA256, annotation colors, border widths,
   and link pages from `C:/Users/wangz/Downloads/21.pdf`.
5. Render every page that contains link annotations into
   `tmp/pdfs/paper21_after`.
6. Visually inspect rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
7. Update README/status/audit/version/validation metadata with the new hash and
   VLA-style boxed-link inventory.
8. Validate build logs, JSON metadata, diff hygiene, final PDF hash, and absence
   of local `paper/main.pdf`.
9. Remove Paper21 temp renders, leaving only the shared role-model render
   directory.
10. Stage only Paper21 source and metadata files, commit, push, and verify a
    clean repository before moving to Paper20.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations, references, or URLs merely to change link
  counts.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

Final artifact after hardening:

- Canonical PDF: `C:/Users/wangz/Downloads/21.pdf`
- Pages: 26
- Size: 428,709 bytes
- SHA256: `C282912BC81046BD1B51C69B60DCEAF3B6798E89CD43F59638BE0FD76CF51F8C`
- Local `paper/main.pdf`: absent after export

Final link inventory:

- Link pages: `[(2, 41), (3, 28), (6, 2), (7, 1), (10, 1), (12, 4), (13, 21), (14, 19), (15, 6), (20, 1)]`
- Annotation colors: green = 118, red = 6, cyan = 0
- Border widths: `(0, 0, 1)` for all 124 link annotations

Visual check:

- Rendered affected pages 2, 3, 6, 7, 10, 12, 13, 14, 15, and 20 from the
  final Downloads PDF.
- Spot-checked pages 2, 6, and 13 at high detail.
- Green citation and URL boxes and red internal-reference boxes are crisp and
  aligned; no cyan boxes are visible.
