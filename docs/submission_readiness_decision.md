# Submission Readiness Decision

Decision: final synthetic mechanism paper; hardware-claim readiness remains strong-revise.

## Why It Is Now Submission-Ready For The Synthetic Scope

- 26-page final manuscript with formal timing claim, method, full-scale experiments, negative controls, ablations, appendices, and audit notes.
- Full-scale suite has 191,384 rows over 26,000 cases.
- Strong baselines are included and not hidden.
- The risk guard failure is reported.
- Final PDF is verified in Downloads with hash recorded.

## Why It Is Not A Real-Robot Claim

- No physical gripper experiment.
- No measured strategy-switch latency.
- No calibrated physical proximity/tactile sensor.
- No learned policy baseline.

## Required Next Work For Hardware-Strength Submission

- Measure switch latency on a real gripper.
- Measure cue onset and first-contact impulse.
- Compare against learned precontact policies and tuned posterior thresholds.
- Validate that final success hides first-contact harm on real objects.
