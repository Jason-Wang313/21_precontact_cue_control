# Experiment Rigor Checklist

- [x] Runnable experiment: `python scripts/run_experiments.py`.
- [x] Main episode count: 27,000.
- [x] Policies include fixed nominal, contact-reactive, posterior-only, guard contract, and oracle precontact.
- [x] Metrics include safe success, final success, harmful contact, late switch, early false switch, impulse, and regret.
- [x] Conditions include normal, weak cue, and late cue.
- [x] V2 hostile baseline: posterior confidence/margin threshold sweep.
- [x] Outputs include episode CSV, summary CSV, ablation CSV, posterior sweep CSV, generated LaTeX table, JSON summary, and figures.
- [ ] Real robot experiment.
- [ ] Learned precontact policy baseline.
- [ ] Sensor model calibrated to a specific proximity/tactile device.

Decision: rigorous enough for workshop-only / strong-revise positioning; not enough for full submission claims.
