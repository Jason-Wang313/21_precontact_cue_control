# Hostile Reviewer Response

## Likely Rejection Point

"Your guard is just a tuned precontact classifier threshold."

## Response

The paper agrees that tuned posterior thresholds are strong. In v3, fixed posterior reaches 0.814 normal safe success and tuned posterior remains competitive. The calibrated deadline guard also reaches 0.814 normal safe success, but improves high-latency safe success (0.542 versus 0.500 for fixed posterior), cost-asymmetry mean cost (1.333 versus 1.550), and onset-late shift safe success versus source-tuned posterior (0.512 versus 0.292).

The claim is not universal dominance. The claim is that activation latency creates a physical validity condition for first-contact strategy switches, and that calibrated deadline guards expose and reduce failures in the regimes where that condition matters.

## Other Attacks

- "No real robot": correct; this is a synthetic mechanism paper.
- "Risk guard failed": correct; it is reported as a negative method result.
- "Weak cues favor tuned posterior": correct; this is a boundary condition.
- "A learned policy might do better": correct; future work should test that.
