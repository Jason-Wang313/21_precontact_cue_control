# Hostile Reviewer Response

## Likely Rejection Point

"Your guard is just a tuned precontact classifier threshold; posterior-only can do the same thing."

## Response

The v2 paper agrees that tuned posterior-only is a strong baseline. A threshold sweep over posterior confidence and margin reaches 0.977 safe success under normal cues, 0.758 under weak cues, and 0.438 under late cues, exceeding the proposed guard in this synthetic setup.

The revised claim is narrower. The contribution is not algorithmic dominance over every tuned precontact threshold. It is the activation-deadline contract: a strategy-switch decision is physically valid only if it can become active before first contact, and safe-success/late-switch metrics expose failures hidden by final success.

## What The Paper Still Cannot Claim

- Real-robot validation.
- Dominance over tuned precontact thresholds.
- Dominance over learned policies.
- A complete optimal-control theory.

## Honest Position

Workshop-only / strong-revise: useful timing mechanism and diagnostic benchmark, but not main-track without real hardware and stronger learned/tuned baselines.
