# Claims

## Formal Claim

Let a robot approach first contact at speed `v`, require a discrete strategy switch time `tau_s`, and have remaining distance `d` when the decisive evidence is obtained. If `d < v tau_s`, then no controller that waits for that evidence can make the new strategy active before first contact. When the nominal strategy causes harmful impulse or failure for a subset of hidden contact modes, a contact-triggered policy has a nonzero irreducible late-switch failure probability on those modes. A precontact guard can reduce that probability only when it obtains sufficiently reliable evidence at `d >= v tau_s`.

Status: proved in the paper as a timing lemma under deterministic approach speed and fixed switch latency. It is not a general optimal-control theorem.

## Empirical Claims To Test

- A latency-aware precontact guard reduces late-switch failures relative to fixed and contact-reactive policies when cue lead distance is positive.
- The advantage increases with switch latency and approach speed.
- The advantage disappears when the cue becomes informative only at contact or when switch latency is zero.
- A posterior-only policy that ignores remaining distance can switch too late or too early under asymmetric costs.
- First-contact impulse reveals failures hidden by final grasp success.

## Unsupported Or Limited Claims

- No real robot experiments are claimed.
- No claim is made that the synthetic cue model matches a particular sensor exactly.
- No claim is made that precontact cues are always available or reliable.
- No claim is made that the method outperforms large learned policies in all tasks.
- The contribution is a mechanism and diagnostic experiment, not a complete manipulation stack.
