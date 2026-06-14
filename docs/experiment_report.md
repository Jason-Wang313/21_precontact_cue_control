# Experiment Report

## Full-Scale Run

- Command: `python experiments\full_scale_precontact.py`
- Stage: complete
- Seed: 21021
- Rows: 191,384
- Cases: 26,000
- Plot failures: 0
- Metadata: `results/full_scale/metadata.json`

## Families

- Family A: main latency/cue benchmark, 90,720 rows.
- Family B: cost asymmetry, 32,400 rows.
- Family C: distribution shift, 23,040 rows.
- Family D: negative controls, 14,504 rows.
- Family E: ablations, 30,720 rows.

## Headline Outcomes

- Normal contact reactive safe success: 0.286.
- Normal calibrated deadline guard safe success: 0.814.
- High-latency calibrated deadline guard safe success: 0.542 versus fixed posterior 0.500.
- Cost-asymmetry calibrated deadline guard mean cost: 1.333 versus fixed posterior 1.550.
- Onset-late shift calibrated deadline guard safe success: 0.512 versus source-tuned posterior 0.292.
- Risk guard mean cost in Family B: 2.216; negative method result.

## Interpretation

The full-scale suite supports a bounded activation-deadline claim. It does not support universal dominance over tuned posterior thresholds, and it does not support real-robot deployment claims.
