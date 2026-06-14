# Reproducibility Checklist

- [x] Dependencies listed in `requirements.txt`.
- [x] v3 experiment source: `experiments/full_scale_precontact.py`.
- [x] v3 outputs: `results/full_scale/`.
- [x] v3 figures: `figures/full_scale/`.
- [x] v3 manuscript source: `paper/main.tex`.
- [x] Final PDF path: `C:\Users\wangz\Downloads\21.pdf`.
- [x] Final PDF page count: 26.
- [x] Final PDF SHA256: `A3CE9BC0033548239FD9C10F2B2C8835D2BAA567F1B7DB887665F4B32CDAE27A`.
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
