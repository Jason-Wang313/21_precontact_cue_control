# Claims

## Supported Formal Claim

If a robot approaches first contact at speed `v`, a discrete strategy switch takes `tau_s`, and decisive evidence first arrives at remaining distance `d < v tau_s`, then no policy that waits for that evidence can make the new strategy active by first contact. This is proved as an activation-deadline timing lemma under constant approach speed and fixed switch latency.

## Supported Empirical Claims

- Contact-reactive switching is too late under nonzero latency in the synthetic benchmark: normal safe success is 0.286.
- Strong posterior baselines are competitive: fixed posterior reaches 0.814 normal safe success.
- The calibrated deadline guard is competitive in normal cues, also 0.814 safe success, with lower expected cost and fewer deadline violations than fixed posterior.
- In the high-latency normal slice, calibrated deadline guard reaches 0.542 safe success versus 0.500 for fixed posterior.
- In cost-asymmetry sweeps, calibrated deadline guard reaches 1.333 mean cost versus 1.550 for fixed posterior.
- Under onset-late shift, calibrated deadline guard reaches 0.512 safe success versus 0.292 for source-tuned posterior.
- Negative controls behave correctly: random cues and evidence-at-contact prevent useful precontact gains; zero latency removes deadline violations.

## Boundary and Negative Claims

- Tuned posterior thresholds remain strong and win in some weak/early cue regimes.
- The risk guard extension underperforms because it over-switches on ambiguous cues.
- The paper does not claim real-robot validation.
- The paper does not claim universal dominance over tuned classifiers or learned policies.
- The contribution is a timing contract, calibrated deadline guard, and diagnostic benchmark, not a complete manipulation stack.
