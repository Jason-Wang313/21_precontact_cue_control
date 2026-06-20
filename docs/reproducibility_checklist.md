# Reproducibility Checklist

- [x] Dependencies listed in `requirements.txt`.
- [x] v3 experiment source: `experiments/full_scale_precontact.py`.
- [x] v3 outputs: `results/full_scale/`.
- [x] v3 figures: `figures/full_scale/`.
- [x] v3 manuscript source: `paper/main.tex`.
- [x] Final PDF path: `C:\Users\wangz\Downloads\21.pdf`.
- [x] Final PDF page count: 26.
- [x] Final PDF bytes: 428,709.
- [x] Final PDF SHA256: `C282912BC81046BD1B51C69B60DCEAF3B6798E89CD43F59638BE0FD76CF51F8C`.
- [x] VLA-style boxed links: 124 annotations; pages `[(2, 41), (3, 28), (6, 2), (7, 1), (10, 1), (12, 4), (13, 21), (14, 19), (15, 6), (20, 1)]`; colors green = 118, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- [x] Local `paper/main.pdf` removed after final export.

Recommended verification:

```powershell
python experiments\full_scale_precontact.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdfinfo C:\Users\wangz\Downloads\21.pdf
Get-FileHash -Algorithm SHA256 C:\Users\wangz\Downloads\21.pdf
```
