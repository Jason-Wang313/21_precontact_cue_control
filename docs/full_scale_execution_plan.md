# Paper 21 Full-Scale Execution Plan

## Scope lock

Work on exactly one paper: `21_precontact_cue_control`.

Do not copy a PDF to `C:\Users\wangz\Downloads\21.pdf` until the manuscript is final, compiles cleanly, and verifies at or above the page threshold. Intermediate PDFs stay local and are removed after the final export. Only after Paper21 is final, documented, committed, pushed, and clean/upstream verified may work move to Paper22.

## Current claim and evidence state

The v2 manuscript studies precontact cue control for switching grasp strategy before first touch. The supported physics claim is the activation-deadline lemma: if evidence arrives at remaining distance `d < v tau_s`, a switch that requires `tau_s` cannot be active by first contact. The empirical claim is currently weaker: a hand-coded guard strongly improves over contact-reactive switching but does not dominate a tuned posterior-only precontact baseline.

Current v2 evidence:

- Normal-cue guard safe success is about `0.962`, greatly above contact-reactive switching at about `0.405`.
- The tuned posterior-only baseline reaches about `0.977` normal-cue safe success and also beats the guard under weak and late cues.
- Existing manuscript length is about six pages, with limited formalism, limited baselines, limited simulator variation, and limited appendix evidence.

The v3 goal is not to erase the negative result. The goal is to make a stronger, submission-ready paper by turning the benchmark into a rigorous study of physically valid precontact decisions under latency, asymmetric first-contact costs, cue timing, and calibration shift. The proposed method should be upgraded from a single hand-coded guard into a deadline-aware guard family, while keeping the paper honest about when tuned posterior thresholds are enough.

## Target contribution after hardening

The final paper should support this narrower but stronger thesis:

Precontact cues become a control primitive, rather than just classifier evidence, when the policy explicitly accounts for whether a selected strategy can become active before first contact and for the asymmetric cost of early wrong switches versus late harmful contacts. The activation deadline induces measurable failure modes that final grasp success and posterior accuracy can hide. A deadline-aware guard family improves safety in latency-limited, cost-asymmetric regimes and provides diagnostic negative controls showing when the benefit disappears.

The final paper must not claim:

- Real-robot validation.
- Universal dominance over every tuned classifier threshold.
- Novelty of pre-touch sensing, proximity perception, tactile feedback, or grasp planning.
- That learned end-to-end policies cannot learn similar behavior.

## Experiment design

Implement a RAM-light full-scale runner that writes streaming CSV shards and summaries under `results/full_scale/`. It should reuse the existing simulator where useful but expand the scale, policy set, conditions, and diagnostics. Keep arrays small, write rows incrementally, and aggregate per family after each family completes.

### Family A: Main latency and cue-timing benchmark

Purpose: establish the deadline-aware control problem at meaningful scale.

Sweep:

- Approach speeds: at least five values from slow to fast.
- Switch latencies: at least seven values, including zero-latency negative control and high-latency stress cases.
- Cue conditions: normal, weak, late, early, high-noise, calibrated-shift, uninformative-until-contact.
- Object/contact modes: nominal, thin-lip, slippery, fragile, plus at least two new ambiguous modes with similar cue prototypes.
- Seeds/episodes: enough for stable confidence intervals without loading all episodes into memory at once.

Policies:

- fixed nominal
- contact reactive
- fixed posterior-only
- tuned posterior-only
- oracle precontact
- v2 guard contract
- deadline-aware risk guard
- calibrated deadline guard
- deadline-aware tuned threshold grid

Metrics:

- safe success
- final success
- harmful first contact
- late-switch rate
- early false-switch rate
- mean and p90 impulse
- deadline violation rate
- avoidable lateness
- calibration error where relevant

Expected interpretation:

- Contact-reactive should fail as latency rises.
- Zero latency should shrink or remove the guard-specific advantage.
- Uninformative-until-contact cues should prevent legitimate precontact gains.
- If tuned posterior-only still wins broadly, the manuscript must frame the method as diagnostic/accounting plus a deadline-aware family, not algorithmic dominance.

### Family B: Cost asymmetry and risk sensitivity

Purpose: test whether the deadline-aware guard matters when early wrong switches and late harmful contacts have different consequences.

Sweep:

- False early-switch costs from mild to severe.
- Harmful first-contact costs from mild to catastrophic.
- Mode-specific impulse thresholds.
- Cost-sensitive objective weights.

Policies:

- tuned posterior-only optimized for safe success
- tuned posterior-only optimized for expected cost
- v2 guard
- deadline-aware risk guard
- oracle

Metrics:

- expected cost
- safe success
- harmful contact
- early false switches
- cost regret versus oracle

Expected interpretation:

- The risk guard should matter most when harmful contact is much more costly than early conservative switching.
- If posterior-only can match the risk guard after cost tuning, report that as a boundary condition.

### Family C: Calibration and distribution shift

Purpose: distinguish posterior confidence from physically valid, calibrated decisions.

Sweep:

- Train/tune on source cue distributions, evaluate on shifted onset distances, noise levels, prototype drift, velocity mix, and latency mix.
- Include miscalibrated posterior likelihoods and temperature-scaled calibrated variants.

Policies:

- source-tuned posterior-only
- validation-tuned posterior-only
- temperature-calibrated posterior-only
- deadline-aware calibrated guard
- oracle

Metrics:

- source and target safe success
- expected calibration error
- harmful contact under shift
- deadline violations
- robustness drop from source to target

Expected interpretation:

- A guard that separates physical deadline feasibility from posterior confidence should degrade more transparently under shift.
- Do not overclaim if calibration alone explains most improvement.

### Family D: Negative controls and falsification tests

Purpose: prevent a padded positive-only story.

Controls:

- zero switch latency
- perfect posterior but evidence only at contact
- random/uninformative cue
- no hidden non-nominal mode
- all strategies have equal impulse
- very high cost of early wrong switch
- switch latency longer than total approach time

Expected interpretation:

- The advantage should disappear when the activation deadline is irrelevant or the cue has no precontact information.
- The method should fail gracefully when no valid precontact action exists.

### Family E: Ablations of the proposed guard family

Purpose: isolate which components matter.

Ablations:

- remove deadline feasibility term
- remove margin term
- remove cost-sensitive threshold
- remove calibration/temperature scaling
- remove persistence/streak requirement
- use distance-only trigger
- use posterior-only trigger

Metrics:

- safe success
- cost regret
- deadline violations
- harmful contact
- early false switch

Expected interpretation:

- The manuscript should identify which terms matter and where they do not.

## Figures and tables

Generate publication-ready figures under `figures/full_scale/`:

- safe success versus switch latency
- harmful first-contact impulse versus latency
- expected cost versus cost asymmetry
- robustness under cue shift
- deadline violation heatmap over speed and latency
- policy frontier: harmful contact versus early false switch
- ablation bars for guard components
- negative-control summary

Generate LaTeX tables under `results/full_scale/tex/`:

- main benchmark aggregate with confidence intervals
- strongest baseline comparison
- cost asymmetry results
- distribution shift results
- negative-control outcomes
- ablation table
- reproducibility/runtime metadata

## Manuscript expansion strategy

Rewrite `paper/main.tex` into a full manuscript with enough real content for at least 25 pages:

- Expanded introduction with concrete failure case and claim boundaries.
- Related work split into pre-touch sensing, tactile/contact feedback, grasp learning/planning, hybrid/control guards, calibration/risk-sensitive decision making.
- Formal problem setup with activation deadline, safe success, first-contact cost, and physically valid switch definitions.
- Method section for deadline-aware guard contracts, risk-aware thresholding, calibrated guard, and implementation details.
- Full experimental protocol with simulator details, policies, hyperparameter search, confidence intervals, metrics, and RAM-light reproducibility.
- Results sections for Families A-E.
- Failure cases and negative controls.
- Limitations and ethics/safety discussion.
- Reproducibility checklist and audit notes.
- Appendix with derivations, pseudocode, parameter tables, extra plots, and full result tables.

Length must come from substantive results, figures, tables, and explanations, not filler.

## Documentation updates

After experiments and manuscript hardening, update:

- `README.md`
- `child_status.md`
- `docs/claims.md`
- `docs/experiment_report.md`
- `docs/experiment_rigor_checklist.md`
- `docs/final_audit.md`
- `docs/hostile_reviewer_response.md`
- `docs/submission_readiness_decision.md`
- `docs/version_history.md`
- any paper-specific reproducibility or evidence summary files

All docs must state the true final evidence, including negative or boundary results.

## Acceptance checklist before final export

- Full-scale runner completes with status JSON showing `stage: complete`.
- Streaming outputs, summaries, tables, figures, and metadata exist under `results/full_scale/`.
- Manuscript compiles without fatal errors.
- Final PDF is at least 25 pages.
- Final PDF text contains v3/final marker, full-scale episode counts, strongest baseline outcomes, negative controls, and final audit language.
- `C:\Users\wangz\Downloads\21.pdf` is copied only after the final PDF passes verification.
- Local `paper/main.pdf` is removed after final export.
- SHA256 hash, bytes, and page count for `Downloads\21.pdf` are recorded in docs.
- Repo is committed and pushed.
- `git status --short --branch` is clean and `HEAD == @{u}` before moving to Paper22.
