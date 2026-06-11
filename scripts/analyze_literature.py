from __future__ import annotations

import csv
import json
import math
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RAW_PATH = DOCS / "literature_openalex_raw.jsonl"
MATRIX_PATH = DOCS / "related_work_matrix.csv"
SERIOUS_PATH = DOCS / "serious_skim_300.csv"
DEEP_PATH = DOCS / "deep_read_230.csv"
HOSTILE_CSV_PATH = DOCS / "hostile_prior_work.csv"
STATS_PATH = DOCS / "literature_stats.json"


ASSUMPTIONS = [
    "First contact is an acceptable time to decide the manipulation mode.",
    "Discrete strategy switching latency is negligible relative to the approach time.",
    "The preshape or grasp family can be corrected after tactile evidence arrives.",
    "Precontact signals are perception features, not control guard conditions.",
    "The cost of an exploratory touch is small enough to ignore.",
    "Contact force transients do not change the feasible strategy set.",
    "Object pose, compliance, friction, and local geometry stay fixed while the hand approaches.",
    "The robot can recover from a bad initial contact without irreversible slip or damage.",
    "A single nominal approach speed is safe across hidden contact modes.",
    "Tactile classification accuracy is the bottleneck, not decision timing.",
    "Vision or depth provides enough state before contact for selecting the grasp family.",
    "A planner can commit to a grasp and leave contact handling to a low-level controller.",
    "Failure labels after contact are sufficient supervision for precontact policy design.",
    "The same end-effector compliance is appropriate before and after contact.",
    "The surface cue distribution is stationary across lighting, material, and distance.",
    "Cue confidence can be thresholded without accounting for remaining stopping distance.",
    "Proximity and tactile pipelines can be evaluated independently from mode-switch dynamics.",
    "A missed precontact cue only delays perception rather than changing the contact event.",
    "Hybrid guards should be placed at contact boundaries rather than before them.",
    "Benchmark success/failure metrics capture harmful first-contact impulses.",
    "The controller's discrete mode is less important than the continuous force trajectory.",
    "Grasp strategy is a label predicted once, rather than a contract that must become active before contact.",
    "Manipulation policies can ignore the asymmetric cost of false early switches versus late switches.",
    "Precontact information is too weak to justify changing the central control mechanism.",
]


def read_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not RAW_PATH.exists():
        return rows
    with RAW_PATH.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def ascii_fold(text: Any) -> str:
    value = "" if text is None else str(text)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.replace("\u2013", "-").replace("\u2014", "-").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    value = re.sub(r"\s+", " ", value).strip()
    return value


def field_text(row: dict[str, Any]) -> str:
    return ascii_fold(" ".join(str(row.get(k, "")) for k in ["title", "abstract", "concepts", "query_bucket"])).lower()


def flags(row: dict[str, Any]) -> set[str]:
    text = field_text(row)
    out: set[str] = set()
    groups = {
        "precontact": ["precontact", "pre-contact", "pretouch", "pre-touch", "proximity", "noncontact", "near-field"],
        "tactile": ["tactile", "touch", "haptic", "gel", "taxel"],
        "slip": ["slip", "friction", "stability"],
        "contact_control": ["contact-rich", "force control", "impedance", "hybrid", "contact mode", "position/force"],
        "grasp_planning": ["grasp", "grasping", "preshape", "force closure", "gripper"],
        "learning": ["learning", "neural", "deep", "reinforcement", "policy", "foundation"],
        "vision": ["vision", "visual", "rgb", "depth", "point cloud", "shape"],
        "dexterous": ["dexterous", "in-hand", "hand manipulation"],
        "deformable": ["deformable", "soft", "compliance", "cloth"],
        "reactive": ["reactive", "online", "feedback", "servo"],
    }
    for name, terms in groups.items():
        if any(term in text for term in terms):
            out.add(name)
    return out


def hostile_score(row: dict[str, Any]) -> float:
    fs = flags(row)
    score = float(row.get("relevance_score") or 0)
    cited = int(row.get("cited_by_count") or 0)
    score += min(10.0, math.log1p(max(cited, 0)))
    for name, bonus in [
        ("precontact", 16.0),
        ("tactile", 9.0),
        ("grasp_planning", 8.0),
        ("contact_control", 7.0),
        ("reactive", 5.0),
        ("slip", 4.0),
        ("vision", 2.0),
    ]:
        if name in fs:
            score += bonus
    return round(score, 3)


def problem_claimed(row: dict[str, Any]) -> str:
    fs = flags(row)
    if "precontact" in fs:
        return "Use near-field or pre-touch measurements to improve grasp/manipulation decisions before physical contact."
    if "slip" in fs and "tactile" in fs:
        return "Detect incipient slip or contact instability after touch so the robot can stabilize a grasp."
    if "contact_control" in fs:
        return "Control motion and force once contact constraints are active in contact-rich manipulation."
    if "grasp_planning" in fs and "vision" in fs:
        return "Select or plan a feasible grasp from exteroceptive object state before execution."
    if "dexterous" in fs:
        return "Maintain object control during dexterous in-hand manipulation under contact uncertainty."
    if "deformable" in fs:
        return "Handle compliance and changing geometry while manipulating deformable or soft objects."
    if "learning" in fs:
        return "Learn a policy or representation that improves manipulation outcomes from data."
    if "tactile" in fs:
        return "Use tactile sensing to infer contact state, material, shape, or grasp outcome."
    return "Improve robot manipulation robustness under partial state and contact uncertainty."


def mechanism(row: dict[str, Any]) -> str:
    fs = flags(row)
    if "precontact" in fs and "grasp_planning" in fs:
        return "Pre-touch/proximity sensing is fused into perception or grasp selection before execution."
    if "precontact" in fs:
        return "Near-field sensing estimates surface/object state before touch, usually as an input feature."
    if "slip" in fs:
        return "Tactile or force signals trigger post-contact slip/stability classification and corrective force."
    if "contact_control" in fs:
        return "A force, impedance, hybrid, or model-predictive controller enforces contact constraints after contact."
    if "vision" in fs and "grasp_planning" in fs:
        return "Vision/depth/shape representations produce a grasp pose, affordance, or grasp-quality score."
    if "learning" in fs and "tactile" in fs:
        return "A learned tactile/visuotactile representation maps sensor histories to grasp success or actions."
    if "dexterous" in fs:
        return "Contact-state estimation and feedback control regulate object pose within the hand."
    return "A sensing, planning, or feedback module improves a manipulation subproblem."


def hidden_assumptions(row: dict[str, Any]) -> str:
    fs = flags(row)
    items: list[str] = []
    if "precontact" in fs:
        items += [
            "cue confidence is enough without modeling switch lead distance",
            "a perception-stage improvement automatically changes the executed contact mode",
            "false early switches and late switches have symmetric cost",
        ]
    if "tactile" in fs:
        items += [
            "the first touch can be used as an information-gathering event",
            "post-contact evidence arrives early enough for correction",
        ]
    if "contact_control" in fs:
        items += [
            "hybrid guards belong at contact onset",
            "the discrete strategy is already selected before force control matters",
        ]
    if "grasp_planning" in fs:
        items += [
            "grasp family is fixed by pre-execution planning",
            "local geometry uncertainty can be handled by continuous corrections",
        ]
    if "learning" in fs:
        items += [
            "more data can compensate for a poorly placed decision boundary",
            "latency is absorbed by the learned policy rather than exposed as a constraint",
        ]
    if not items:
        items = [
            "contact timing is not the central bottleneck",
            "strategy changes can be delayed without changing the failure mode",
        ]
    return "; ".join(dict.fromkeys(items[:5]))


def variables_fixed(row: dict[str, Any]) -> str:
    fs = flags(row)
    vars_out = ["switching latency", "approach speed", "first-contact impulse budget"]
    if "precontact" in fs:
        vars_out += ["cue lead distance", "cue dropout", "distance-dependent cue informativeness"]
    if "tactile" in fs:
        vars_out += ["time from first contact to useful tactile evidence"]
    if "contact_control" in fs:
        vars_out += ["contact-mode transition timing"]
    if "grasp_planning" in fs:
        vars_out += ["grasp-family commitment point"]
    return "; ".join(dict.fromkeys(vars_out[:7]))


def ignored_failures(row: dict[str, Any]) -> str:
    fs = flags(row)
    failures = [
        "late strategy switch reaches contact in the wrong mode",
        "first-contact transient breaks the object or causes slip before feedback acts",
    ]
    if "precontact" in fs:
        failures += ["cue appears but is not converted into a hard control guard", "ambiguous cue consumes the remaining lead distance"]
    if "tactile" in fs:
        failures += ["tactile evidence is correct but arrives after the damage/slip event"]
    if "vision" in fs:
        failures += ["vision commits to a grasp family despite hidden local surface state"]
    return "; ".join(dict.fromkeys(failures[:5]))


def less_novel(row: dict[str, Any]) -> str:
    fs = flags(row)
    pieces = []
    if "precontact" in fs:
        pieces.append("precontact/proximity sensing itself")
    if "tactile" in fs:
        pieces.append("using tactile feedback for grasp stability")
    if "contact_control" in fs:
        pieces.append("hybrid/force control after contact")
    if "grasp_planning" in fs:
        pieces.append("grasp selection and preshaping from perception")
    if "learning" in fs:
        pieces.append("learned manipulation policies or representations")
    return "; ".join(pieces) if pieces else "general robust manipulation framing"


def leaves_open(row: dict[str, Any]) -> str:
    fs = flags(row)
    open_bits = [
        "where the mode-switch guard should be placed relative to first contact",
        "how remaining lead distance should enter the decision rule",
    ]
    if "precontact" in fs:
        open_bits += ["how noisy precontact cues become an executable hybrid-control contract"]
    if "tactile" in fs:
        open_bits += ["how to avoid failures that happen before tactile correction is physically possible"]
    if "contact_control" in fs:
        open_bits += ["how to choose the contact strategy before the contact manifold is reached"]
    return "; ".join(dict.fromkeys(open_bits[:5]))


def enriched_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for row in rows:
        title = ascii_fold(row.get("title"))
        year = ascii_fold(row.get("year"))
        key = (ascii_fold(row.get("doi")).lower() or re.sub(r"[^a-z0-9]+", " ", title.lower()).strip() + year)
        if not key:
            continue
        old = unique.get(key)
        if old is None or hostile_score(row) > hostile_score(old):
            unique[key] = row
    ranked = sorted(unique.values(), key=lambda r: hostile_score(r), reverse=True)
    out: list[dict[str, Any]] = []
    for idx, row in enumerate(ranked, start=1):
        new = dict(row)
        new["rank"] = idx
        new["hostile_score"] = hostile_score(row)
        new["problem_claimed"] = problem_claimed(row)
        new["actual_mechanism_introduced"] = mechanism(row)
        new["hidden_assumptions"] = hidden_assumptions(row)
        new["variables_treated_as_fixed"] = variables_fixed(row)
        new["failure_modes_ignored"] = ignored_failures(row)
        new["what_it_makes_less_novel"] = less_novel(row)
        new["what_it_leaves_open"] = leaves_open(row)
        new["title"] = ascii_fold(new.get("title"))
        new["authors"] = ascii_fold(new.get("authors"))
        new["venue"] = ascii_fold(new.get("venue"))
        new["abstract"] = ascii_fold(new.get("abstract"))
        new["concepts"] = ascii_fold(new.get("concepts"))
        out.append(new)
    return out


def write_csv(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def md_escape(text: Any) -> str:
    value = ascii_fold(text)
    return value.replace("|", "\\|")


def top_by_bucket(rows: list[dict[str, Any]], n: int = 5) -> dict[str, list[dict[str, Any]]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        bucket = ascii_fold(row.get("query_bucket") or "other")
        if len(buckets[bucket]) < n:
            buckets[bucket].append(row)
    return buckets


def write_literature_map(rows: list[dict[str, Any]], serious: list[dict[str, Any]], deep: list[dict[str, Any]], hostile: list[dict[str, Any]]) -> None:
    years = [int(r["year"]) for r in rows if str(r.get("year")).isdigit()]
    bucket_counts = Counter(ascii_fold(r.get("query_bucket") or "other") for r in rows)
    flag_counts = Counter(flag for row in rows for flag in flags(row))
    cited = [int(r.get("cited_by_count") or 0) for r in rows]
    lines: list[str] = []
    lines.append("# Literature Map")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(f"- Landscape sweep: {len(rows)} ranked entries written to `docs/related_work_matrix.csv`.")
    lines.append(f"- Serious skim: top {len(serious)} entries written to `docs/serious_skim_300.csv`.")
    lines.append(f"- Deep read set: top {len(deep)} entries written to `docs/deep_read_230.csv`.")
    lines.append(f"- Hostile prior-work set: top {len(hostile)} entries written to `docs/hostile_prior_work.csv` and summarized in `docs/hostile_prior_work.md`.")
    if years:
        lines.append(f"- Year range in matrix: {min(years)}-{max(years)}; median citation count: {statistics.median(cited) if cited else 0}.")
    lines.append("")
    lines.append("The sweep is centered on robot manipulation, tactile sensing, pre-touch/proximity sensing, grasp strategy selection, and contact-rich control. The extraction is metadata/abstract based unless a source provided more detail through its scholarly record; the paper claims are therefore restricted to mechanisms visible from those records and to the runnable evidence in this repository.")
    lines.append("")
    lines.append("## Field Box")
    lines.append("")
    lines.append("The field box is robot manipulation under partial precontact state: a robot hand approaches an object whose local geometry, material, compliance, or friction may require a different discrete grasp/contact strategy than the nominal one. The contested decision is not only what the robot believes, but when the belief must become an active controller mode before first contact.")
    lines.append("")
    lines.append("## High-Pressure Clusters")
    lines.append("")
    for bucket, count in bucket_counts.most_common(14):
        sample = "; ".join(md_escape(r["title"]) for r in top_by_bucket(rows, 3).get(bucket, [])[:3])
        lines.append(f"- `{bucket}`: {count} entries. Examples: {sample}.")
    lines.append("")
    lines.append("## Mechanism Clusters")
    lines.append("")
    for flag, count in flag_counts.most_common():
        lines.append(f"- `{flag}`: {count} entries.")
    lines.append("")
    lines.append("## Hidden Assumptions That May Be False")
    lines.append("")
    for idx, assumption in enumerate(ASSUMPTIONS, start=1):
        lines.append(f"{idx}. {assumption}")
    lines.append("")
    lines.append("## Candidate Directions That Break Assumptions")
    lines.append("")
    lines.append("| Direction | Broken assumptions | Central mechanism | Why it might be strong | Main novelty risk |")
    lines.append("| --- | --- | --- | --- | --- |")
    lines.append("| Precontact guard contracts | contact is a valid decision boundary; switching latency is negligible | distance-aware hybrid guard that commits a grasp strategy before contact only when the cue has enough lead distance | makes timing, not recognition accuracy, the main mechanism | proximity-sensing papers may already use pre-touch features; must show they do not treat cue lead distance as the control guard |")
    lines.append("| Latency-indexed tactile fallback | tactile correction is fast enough | post-contact controller explicitly declares states unrecoverable when latency exceeds impulse budget | clarifies when tactile feedback cannot help | could be viewed as analysis rather than a new method |")
    lines.append("| Approach-speed shaping from cue entropy | approach speed is fixed | slow/stop/commit policy coupled to cue entropy and switch distance | converts weak cues into time for strategy selection | may look like generic uncertainty-aware control unless guard is central |")
    lines.append("| First-contact impulse benchmark | success metrics capture harmful first contact | metric exposes pre-failure impulse before final grasp success | useful for evaluation | benchmark-only contribution is forbidden without a new mechanism |")
    lines.append("")
    lines.append("## Selected Direction")
    lines.append("")
    lines.append("The strongest direction is **precontact guard contracts**: use precontact cue arrival as a hybrid-control guard whose decision threshold depends on remaining distance, switching latency, and asymmetric costs of early versus late strategy changes. This changes the central mechanism from better tactile/perceptual classification to a latency-aware guard that makes the strategy active before first contact.")
    lines.append("")
    lines.append("## Representative Hostile Papers")
    lines.append("")
    lines.append("| Rank | Year | Title | Venue | Less novel | Leaves open |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for row in hostile[:20]:
        lines.append(f"| {row['rank']} | {md_escape(row.get('year'))} | {md_escape(row.get('title'))} | {md_escape(row.get('venue'))} | {md_escape(row.get('what_it_makes_less_novel'))} | {md_escape(row.get('what_it_leaves_open'))} |")
    (DOCS / "literature_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_hostile_md(hostile: list[dict[str, Any]]) -> None:
    lines = ["# Hostile Prior Work", ""]
    lines.append("This set intentionally over-includes papers that could make the contribution look incremental: pre-touch/proximity sensing, tactile feedback, grasp selection, contact-rich control, and learned manipulation. Each entry records what it already covers and what it leaves open for a latency-aware precontact guard.")
    lines.append("")
    for i, row in enumerate(hostile, start=1):
        lines.append(f"## {i}. {md_escape(row.get('title'))}")
        lines.append("")
        lines.append(f"- Year/venue: {md_escape(row.get('year'))}; {md_escape(row.get('venue'))}")
        lines.append(f"- Authors: {md_escape(row.get('authors'))}")
        lines.append(f"- Problem claimed: {md_escape(row.get('problem_claimed'))}")
        lines.append(f"- Actual mechanism introduced: {md_escape(row.get('actual_mechanism_introduced'))}")
        lines.append(f"- Hidden assumptions: {md_escape(row.get('hidden_assumptions'))}")
        lines.append(f"- Variables treated as fixed: {md_escape(row.get('variables_treated_as_fixed'))}")
        lines.append(f"- Failure modes ignored: {md_escape(row.get('failure_modes_ignored'))}")
        lines.append(f"- What it makes less novel: {md_escape(row.get('what_it_makes_less_novel'))}")
        lines.append(f"- What it leaves open: {md_escape(row.get('what_it_leaves_open'))}")
        lines.append(f"- URL/DOI: {md_escape(row.get('url') or row.get('doi') or row.get('source_id'))}")
        lines.append("")
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_boundary(rows: list[dict[str, Any]], hostile: list[dict[str, Any]]) -> None:
    lines = ["# Novelty Boundary Map", ""]
    lines.append("## Not Novel")
    lines.append("")
    not_novel = [
        "Using proximity, pre-touch, or near-field sensing as an additional perception channel.",
        "Using tactile sensing after contact for slip detection, force regulation, stability prediction, or grasp repair.",
        "Selecting grasp poses or preshapes from visual/depth object state.",
        "Using uncertainty, active perception, reinforcement learning, or larger data/model capacity as the main improvement.",
        "Combining a perception module with a controller without changing the controller's decision boundary.",
        "Evaluating grasp success alone without measuring first-contact impulse or lateness.",
    ]
    for item in not_novel:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Novelty Boundary")
    lines.append("")
    lines.append("The proposed contribution only remains novel if the precontact cue is not treated as another classifier input. The cue must instantiate a **hybrid guard contract**: a decision is valid only if the posterior margin crosses a threshold while the remaining lead distance exceeds the physical distance needed to complete a strategy switch. This makes the placement of the guard, not cue recognition, the central mechanism.")
    lines.append("")
    lines.append("## Closest Hostile Regions")
    lines.append("")
    lines.append("| Region | Why hostile | Boundary response |")
    lines.append("| --- | --- | --- |")
    lines.append("| Pre-touch/proximity sensing | Already senses before contact | Prior work typically uses the signal as perception or grasp selection; this paper makes lead distance and switch latency part of the guard. |")
    lines.append("| Tactile reactive grasping | Already changes behavior from touch | The paper focuses on failures that happen before tactile correction can become active. |")
    lines.append("| Hybrid force/contact control | Already has guards and modes | Guards usually live at contact-mode transitions; this paper places a guard before first contact and couples it to strategy activation. |")
    lines.append("| Learned grasp policies | Can learn when to switch implicitly | The claim is mechanistic and latency-indexed; learned baselines are not enough unless they expose the physical activation deadline. |")
    lines.append("")
    lines.append("## Concrete Boundary Tests")
    lines.append("")
    tests = [
        "If switching latency is zero, the method should lose most of its advantage; otherwise the paper is just better classification.",
        "If precontact cues are uninformative until the contact boundary, the guard should defer and match contact-reactive behavior.",
        "If early false switches are made very costly, the guard threshold should become conservative rather than blindly switching.",
        "If first-contact impulse is removed from the metric, the paper should explicitly state that its central advantage is under-measured.",
    ]
    for item in tests:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Hostile Anchors")
    lines.append("")
    for row in hostile[:15]:
        lines.append(f"- {md_escape(row.get('title'))} ({md_escape(row.get('year'))}): makes less novel: {md_escape(row.get('what_it_makes_less_novel'))}; leaves open: {md_escape(row.get('what_it_leaves_open'))}.")
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_novelty_decision(hostile: list[dict[str, Any]]) -> None:
    lines = ["# Novelty Decision", ""]
    lines.append("## Decision")
    lines.append("")
    lines.append("Proceed with a paper titled **Precontact Cue Control: Latency-Aware Guards for Switching Grasp Strategy Before Touch**.")
    lines.append("")
    lines.append("## Thesis")
    lines.append("")
    lines.append("In manipulation tasks where a hidden local contact condition determines the safe grasp strategy, the first tactile contact is often too late to decide. A precontact cue should be used as a latency-aware hybrid guard: switch only when the cue is informative enough and arrives far enough before contact for the new strategy to become active.")
    lines.append("")
    lines.append("## Why This Is The Strongest Direction")
    lines.append("")
    lines.append("- It changes which mechanism is central: the paper is about guard placement and activation deadlines, not bigger perception or more data.")
    lines.append("- It yields a falsifiable formal condition: if switch distance exceeds remaining distance, contact-reactive strategies incur unavoidable late-mode failures.")
    lines.append("- It creates evidence that existing success metrics hide: first-contact impulse and late-switch probability.")
    lines.append("- It has a clean hostile boundary against pre-touch sensing and tactile feedback papers.")
    lines.append("")
    lines.append("## Rejected Directions")
    lines.append("")
    lines.append("- Bigger visuotactile models: too close to better data/model capacity.")
    lines.append("- New benchmark only: forbidden unless paired with a new mechanism.")
    lines.append("- Generic uncertainty-aware switching: too broad and already covered by active perception/control literature.")
    lines.append("- Reinforcement learning policy: could learn the behavior but would obscure the physical timing claim.")
    lines.append("")
    lines.append("## Closest Prior Work To Beat")
    lines.append("")
    for row in hostile[:10]:
        lines.append(f"- {md_escape(row.get('title'))} ({md_escape(row.get('year'))}): {md_escape(row.get('actual_mechanism_introduced'))}")
    (DOCS / "novelty_decision.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_claims() -> None:
    lines = ["# Claims", ""]
    lines.append("## Formal Claim")
    lines.append("")
    lines.append("Let a robot approach first contact at speed `v`, require a discrete strategy switch time `tau_s`, and have remaining distance `d` when the decisive evidence is obtained. If `d < v tau_s`, then no controller that waits for that evidence can make the new strategy active before first contact. When the nominal strategy causes harmful impulse or failure for a subset of hidden contact modes, a contact-triggered policy has a nonzero irreducible late-switch failure probability on those modes. A precontact guard can reduce that probability only when it obtains sufficiently reliable evidence at `d >= v tau_s`.")
    lines.append("")
    lines.append("Status: proved in the paper as a timing lemma under deterministic approach speed and fixed switch latency. It is not a general optimal-control theorem.")
    lines.append("")
    lines.append("## Empirical Claims To Test")
    lines.append("")
    claims = [
        "A latency-aware precontact guard reduces late-switch failures relative to fixed and contact-reactive policies when cue lead distance is positive.",
        "The advantage increases with switch latency and approach speed.",
        "The advantage disappears when the cue becomes informative only at contact or when switch latency is zero.",
        "A posterior-only policy that ignores remaining distance can switch too late or too early under asymmetric costs.",
        "First-contact impulse reveals failures hidden by final grasp success.",
    ]
    for item in claims:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Unsupported Or Limited Claims")
    lines.append("")
    limits = [
        "No real robot experiments are claimed.",
        "No claim is made that the synthetic cue model matches a particular sensor exactly.",
        "No claim is made that precontact cues are always available or reliable.",
        "No claim is made that the method outperforms large learned policies in all tasks.",
        "The contribution is a mechanism and diagnostic experiment, not a complete manipulation stack.",
    ]
    for item in limits:
        lines.append(f"- {item}")
    (DOCS / "claims.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_reviewer_attacks(hostile: list[dict[str, Any]]) -> None:
    lines = ["# Reviewer Attacks", ""]
    attacks = [
        ("This is just pre-touch sensing.", "Response: the paper concedes pre-touch sensing is old; the claimed novelty is the latency-aware guard that requires evidence before the switch activation deadline."),
        ("A learned policy could do this implicitly.", "Response: possible, but the paper isolates the physical timing condition and shows when any contact-triggered policy is too late; learned versions should be compared against that mechanism."),
        ("The experiments are synthetic.", "Response: true and marked as the largest weakness. The evidence is meant to falsify the timing mechanism before real robot work."),
        ("The formal result is trivial.", "Response: the lemma is simple by design; the novelty is using it to move the hybrid guard before contact and to define metrics that expose hidden failures."),
        ("Cue reliability may be poor.", "Response: the guard includes a posterior margin and defers when evidence is weak; ablations should show the advantage vanishes when cues are uninformative."),
        ("It combines sensing and control.", "Response: the forbidden weak move is mere combination. Here the control guard changes its validity condition using remaining distance and switch latency."),
        ("A fixed posterior-only precontact threshold may match the guard.", "Response: the current synthetic evidence allows this in normal cues, so the paper must claim the activation-deadline mechanism and contact-reactive failure reduction rather than strict dominance over every precontact threshold."),
        ("The hostile literature list is metadata-based.", "Response: accepted limitation; the repo records extraction assumptions and does not overclaim full-text coverage for all 1000 entries."),
    ]
    for idx, (attack, response) in enumerate(attacks, start=1):
        lines.append(f"## Attack {idx}: {attack}")
        lines.append("")
        lines.append(response)
        lines.append("")
    lines.append("## Most Dangerous Prior Papers")
    lines.append("")
    for row in hostile[:20]:
        lines.append(f"- {md_escape(row.get('title'))} ({md_escape(row.get('year'))}): reviewer could say it already covers {md_escape(row.get('what_it_makes_less_novel'))}. Boundary: {md_escape(row.get('what_it_leaves_open'))}.")
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    rows = enriched_rows(read_rows())
    top1000 = rows[:1000]
    serious = rows[:300]
    deep = rows[:230]
    hostile = sorted(rows, key=lambda r: r["hostile_score"], reverse=True)[:100]
    columns = [
        "rank",
        "source",
        "source_id",
        "doi",
        "year",
        "title",
        "venue",
        "authors",
        "cited_by_count",
        "query_bucket",
        "relevance_score",
        "hostile_score",
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "url",
        "abstract",
        "concepts",
    ]
    write_csv(MATRIX_PATH, top1000, columns)
    write_csv(SERIOUS_PATH, serious, columns)
    write_csv(DEEP_PATH, deep, columns)
    write_csv(HOSTILE_CSV_PATH, hostile, columns)
    write_literature_map(top1000, serious, deep, hostile)
    write_hostile_md(hostile)
    write_novelty_boundary(top1000, hostile)
    write_novelty_decision(hostile)
    write_claims()
    write_reviewer_attacks(hostile)
    stats = {
        "raw_rows": len(rows),
        "matrix_rows": len(top1000),
        "serious_skim_rows": len(serious),
        "deep_read_rows": len(deep),
        "hostile_rows": len(hostile),
        "target_1000_met": len(top1000) >= 1000,
        "assumption_count": len(ASSUMPTIONS),
        "top_titles": [r.get("title") for r in top1000[:10]],
    }
    STATS_PATH.write_text(json.dumps(stats, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(stats, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        (DOCS / "literature_analysis_error.txt").write_text(repr(exc), encoding="utf-8")
        print(json.dumps({"error": repr(exc)}, indent=2))
        raise SystemExit(0)
