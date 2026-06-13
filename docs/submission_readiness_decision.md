# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Why Not Submit-Ready

- Evidence is synthetic.
- No real gripper, proximity sensor, or measured switch-latency experiment is included.
- V2 shows tuned posterior-only thresholds outperform the proposed guard on this benchmark.
- The formal result is a useful timing lemma, not a full control theorem.

## Why Not Kill

- The activation-deadline condition is physically real and easy to miss.
- Contact-reactive switching fails badly when latency is nonzero.
- The v2 sweep makes the baseline boundary honest instead of hiding it.

## Required Next Work For Main-Track Strength

- Run on a real gripper with measured strategy-switch latency.
- Compare against learned precontact policies and tuned classifier thresholds.
- Calibrate the cue model to a specific sensor.
- Show cases where final success hides harmful first-contact impulse on real objects.
