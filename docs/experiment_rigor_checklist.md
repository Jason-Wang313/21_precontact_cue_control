# Experiment Rigor Checklist

- [x] Detailed per-paper v3 execution plan written before substantive edits.
- [x] Full-scale runner: `python experiments/full_scale_precontact.py`.
- [x] RAM-light execution: family-by-family CSV streaming with compact summaries.
- [x] Full-scale rows: 191,384.
- [x] Full-scale cases: 26,000.
- [x] Policies include fixed nominal, contact reactive, fixed posterior, tuned posterior, v2 guard, deadline threshold, calibrated deadline guard, risk guard, and oracle.
- [x] Metrics include safe success, harmful contact, late switch, deadline violation, early false switch, first-contact impulse, and expected cost.
- [x] Families include main latency/cue sweep, cost asymmetry, distribution shift, negative controls, and ablations.
- [x] Negative controls include zero latency, evidence at contact, random cue, no hidden mode, equal impulse, high early-switch cost, and switch too slow.
- [x] Generated figures and LaTeX tables are used in the paper.
- [ ] Real robot experiment.
- [ ] Learned precontact policy baseline.
- [ ] Sensor model calibrated to a physical device.

Decision: rigorous for a synthetic mechanism submission; not a hardware validation paper.
