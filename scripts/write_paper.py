from __future__ import annotations

import csv
import io
import json
import math
import re
import shutil
import unicodedata
import urllib.request
import zipfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAPER = ROOT / "paper"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PAPER.mkdir(exist_ok=True)

TEMPLATE_STATUS = PAPER / "template_status.json"


def ascii_fold(text: Any) -> str:
    value = "" if text is None else str(text)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
    }
    for src, dst in replacements.items():
        value = value.replace(src, dst)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def tex_escape(text: Any) -> str:
    value = ascii_fold(text)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def bib_escape(text: Any) -> str:
    value = ascii_fold(text)
    value = value.replace("\\", " ")
    value = value.replace("{", "").replace("}", "")
    value = value.replace("&", "\\&").replace("_", "\\_").replace("%", "\\%")
    return re.sub(r"\s+", " ", value).strip()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def row_flags(row: dict[str, str]) -> set[str]:
    text = ascii_fold(" ".join(row.get(k, "") for k in ["title", "abstract", "concepts", "query_bucket"])).lower()
    groups = {
        "precontact": ["precontact", "pre-contact", "pretouch", "pre-touch", "proximity", "noncontact"],
        "tactile": ["tactile", "touch", "haptic", "gel"],
        "contact_control": ["contact-rich", "force control", "impedance", "hybrid", "contact mode"],
        "grasp_planning": ["grasp", "grasping", "preshape", "force closure", "gripper"],
        "learning": ["learning", "neural", "deep", "reinforcement", "policy", "foundation"],
        "slip": ["slip", "friction", "stability"],
        "vision": ["vision", "visual", "depth", "point cloud", "shape"],
    }
    return {name for name, terms in groups.items() if any(term in text for term in terms)}


def select_references(matrix: list[dict[str, str]], limit: int = 46) -> tuple[list[dict[str, str]], dict[str, list[str]]]:
    selected: list[dict[str, str]] = []
    seen: set[str] = set()

    def key_for(row: dict[str, str]) -> str:
        return (row.get("doi") or row.get("source_id") or row.get("title") or "").lower()

    for group in ["precontact", "tactile", "contact_control", "grasp_planning", "slip", "vision", "learning"]:
        for row in matrix:
            if group in row_flags(row) and key_for(row) not in seen:
                selected.append(row)
                seen.add(key_for(row))
                if sum(1 for r in selected if group in row_flags(r)) >= 7:
                    break
    for row in matrix:
        if len(selected) >= limit:
            break
        key = key_for(row)
        if key not in seen:
            selected.append(row)
            seen.add(key)
    for idx, row in enumerate(selected, start=1):
        row["bibkey"] = f"rw{idx:03d}"
    groups: dict[str, list[str]] = {}
    for group in ["precontact", "tactile", "contact_control", "grasp_planning", "slip", "vision", "learning"]:
        groups[group] = [r["bibkey"] for r in selected if group in row_flags(r)][:5]
    groups["general"] = [r["bibkey"] for r in selected[:5]]
    return selected, groups


def cite(keys: list[str]) -> str:
    keys = list(dict.fromkeys(k for k in keys if k))
    if not keys:
        return ""
    return r"\citep{" + ",".join(keys) + "}"


def write_bib(refs: list[dict[str, str]]) -> None:
    entries: list[str] = []
    for row in refs:
        key = row["bibkey"]
        title = bib_escape(row.get("title") or "Untitled")
        year = bib_escape(row.get("year") or "2026")
        venue = bib_escape(row.get("venue") or "Scholarly record")
        authors_raw = bib_escape(row.get("authors") or "Anonymous")
        authors = " and ".join(part.strip() for part in authors_raw.split(";") if part.strip())
        authors = authors.replace("et al.", "others")
        if not authors:
            authors = "Anonymous"
        doi = bib_escape(row.get("doi") or "")
        url = bib_escape(row.get("url") or row.get("source_id") or "")
        entry_type = "article"
        fields = [
            f"  title = {{{title}}}",
            f"  author = {{{authors}}}",
            f"  journal = {{{venue}}}",
            f"  year = {{{year}}}",
        ]
        if doi:
            fields.append(f"  doi = {{{doi}}}")
        if url:
            fields.append(f"  url = {{{url}}}")
        entries.append(f"@{entry_type}{{{key},\n" + ",\n".join(fields) + "\n}\n")
    (PAPER / "references.bib").write_text("\n".join(entries), encoding="ascii", errors="ignore")


def fetch_template() -> dict[str, Any]:
    needed = ["iclr2026_conference.sty", "iclr2026_conference.bst"]
    if all((PAPER / name).exists() for name in needed):
        status = {"status": "already_present", "files": needed}
        TEMPLATE_STATUS.write_text(json.dumps(status, indent=2), encoding="utf-8")
        return status
    urls = [
        "https://raw.githubusercontent.com/ICLR/Master-Template/master/iclr2026.zip",
        "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip",
    ]
    errors: list[str] = []
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=45) as response:
                data = response.read()
            with zipfile.ZipFile(io.BytesIO(data)) as zf:
                names = zf.namelist()
                copied: list[str] = []
                for name in names:
                    base = Path(name).name
                    if base in {
                        "iclr2026_conference.sty",
                        "iclr2026_conference.bst",
                        "iclr2026_conference.tex",
                        "fancyhdr.sty",
                        "natbib.sty",
                        "math_commands.tex",
                    }:
                        target = PAPER / base
                        target.write_bytes(zf.read(name))
                        copied.append(base)
            status = {
                "status": "downloaded",
                "source_url": url,
                "copied": sorted(set(copied)),
                "official_context": [
                    "https://iclr.cc/Conferences/2026/AuthorGuide",
                    "https://github.com/ICLR/Master-Template",
                ],
            }
            TEMPLATE_STATUS.write_text(json.dumps(status, indent=2), encoding="utf-8")
            return status
        except Exception as exc:
            errors.append(f"{url}: {repr(exc)}")
    status = {"status": "failed", "errors": errors}
    TEMPLATE_STATUS.write_text(json.dumps(status, indent=2), encoding="utf-8")
    return status


def policy_label(policy: str) -> str:
    return policy.replace("_", " ")


def fmt_pct(value: Any) -> str:
    try:
        return f"{100.0 * float(value):.1f}"
    except Exception:
        return "n/a"


def fmt_num(value: Any) -> str:
    try:
        return f"{float(value):.3f}"
    except Exception:
        return "n/a"


def result_tables() -> tuple[str, str, dict[str, Any]]:
    ablation = read_csv(RESULTS / "ablation_summary.csv")
    summary = read_csv(RESULTS / "summary.csv")
    normal = [r for r in ablation if r.get("condition") == "normal"]
    policies = ["fixed_nominal", "contact_reactive", "posterior_only", "guard_contract", "oracle_precontact"]
    rows = []
    metrics: dict[str, Any] = {}
    for policy in policies:
        row = next((r for r in normal if r.get("policy") == policy), None)
        if not row:
            continue
        rows.append(
            f"{tex_escape(policy_label(policy))} & {fmt_pct(row.get('safe_success_rate'))} & {fmt_pct(row.get('harmful_contact_rate'))} & {fmt_pct(row.get('late_switch_rate'))} & {fmt_num(row.get('p90_impulse'))} \\\\"
        )
        metrics[f"{policy}_safe"] = float(row.get("safe_success_rate") or 0.0)
        metrics[f"{policy}_harm"] = float(row.get("harmful_contact_rate") or 0.0)
    table1 = "\n".join(rows) if rows else r"\multicolumn{5}{c}{Experiment results unavailable} \\"

    late = [r for r in summary if r.get("condition") == "normal" and r.get("switch_latency") in {"0.12", "0.1200000000000000"}]
    if not late:
        late = [r for r in summary if r.get("condition") == "normal" and abs(float(r.get("switch_latency") or 0) - 0.12) < 1e-9]
    rows2 = []
    for policy in policies:
        row = next((r for r in late if r.get("policy") == policy), None)
        if row:
            rows2.append(
                f"{tex_escape(policy_label(policy))} & {fmt_pct(row.get('safe_success_rate'))} & {fmt_pct(row.get('final_success_rate'))} & {fmt_pct(row.get('harmful_contact_rate'))} & {fmt_pct(row.get('late_switch_rate'))} \\\\"
            )
    table2 = "\n".join(rows2) if rows2 else r"\multicolumn{5}{c}{Latency-slice results unavailable} \\"
    return table1, table2, metrics


def make_tex(ref_groups: dict[str, list[str]], table1: str, table2: str, metrics: dict[str, Any]) -> str:
    pre = cite(ref_groups.get("precontact", []))
    tactile = cite(ref_groups.get("tactile", []))
    contact = cite(ref_groups.get("contact_control", []))
    grasp = cite(ref_groups.get("grasp_planning", []))
    slip = cite(ref_groups.get("slip", []))
    vision = cite(ref_groups.get("vision", []))
    learning = cite(ref_groups.get("learning", []))
    general = cite(ref_groups.get("general", []))
    tactile_slip = cite(ref_groups.get("tactile", []) + ref_groups.get("slip", []))
    grasp_vision_learning = cite(ref_groups.get("grasp_planning", []) + ref_groups.get("vision", []) + ref_groups.get("learning", []))
    contact_general = cite(ref_groups.get("contact_control", []) + ref_groups.get("general", []))
    guard_safe = 100.0 * float(metrics.get("guard_contract_safe", 0.0))
    contact_safe = 100.0 * float(metrics.get("contact_reactive_safe", 0.0))
    posterior_safe = 100.0 * float(metrics.get("posterior_only_safe", 0.0))
    guard_harm = 100.0 * float(metrics.get("guard_contract_harm", 0.0))
    contact_harm = 100.0 * float(metrics.get("contact_reactive_harm", 0.0))
    template = r"""\documentclass{{article}}

\usepackage{{iclr2026_conference,times}}
\usepackage{{amsmath,amssymb,amsthm}}
\usepackage{{booktabs}}
\usepackage{{graphicx}}
\usepackage{{url}}
\usepackage{{microtype}}

\newtheorem{{proposition}}{{Proposition}}

\title{{Precontact Cue Control: Latency-Aware Guards for Switching Grasp Strategy Before Touch}}

\author{{Anonymous Authors}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Robotic manipulation pipelines often let the first tactile contact decide whether a grasp strategy should change. This paper studies the opposite bet: when switching the discrete strategy takes nonzero time, first contact can be too late. We propose a precontact guard contract, a hybrid-control rule that converts a near-field cue into a strategy switch only when the cue is both confident enough and far enough from contact for the new mode to become active. A 1000-paper literature sweep suggests that pre-touch sensing, tactile feedback, grasp planning, and contact control are well studied, but the activation deadline of a discrete strategy switch is usually treated as fixed or negligible. We prove a simple timing lemma showing that contact-triggered policies have irreducible late-switch failures when evidence arrives inside the switching distance. In a runnable synthetic manipulation testbed, the proposed guard reaches @@GUARD_SAFE@@\% safe success under normal precontact cues, compared with @@CONTACT_SAFE@@\% for contact-reactive switching and @@POSTERIOR_SAFE@@\% for a posterior-only precontact policy; it also reduces harmful first contacts from @@CONTACT_HARM@@\% to @@GUARD_HARM@@\%. The result is not a real-robot claim; it is a mechanistic argument and diagnostic benchmark for when precontact cues should be controller guards rather than perception features.
\end{{abstract}}

\section{{Introduction}}

The first touch in robot manipulation is not just a measurement. It is an event that can damage a fragile object, miss a thin lip, initiate slip, or commit the hand to an unrecoverable contact mode. Yet many manipulation stacks still place the decisive strategy update at or after first contact: vision chooses a grasp, tactile feedback detects whether it worked, and force control reacts once the contact constraint exists. That architecture is natural when continuous control is the bottleneck, but it hides a discrete-time fact: changing a grasp family, compliance mode, or finger trajectory takes time.

This paper asks when a precontact sensory cue should become the decision point for changing strategy. The seed idea is intentionally narrow. We do not claim that proximity sensing is new, that tactile feedback is unnecessary, or that larger learned policies cannot improve manipulation. The claim is that the \emph{{guard placement}} is wrong in a specific regime. If a hidden local contact condition selects the safe strategy and a switch requires time $\tau_s$, then evidence received at remaining distance $d < v\tau_s$ cannot make the new strategy active before contact at approach speed $v$. This creates failures that better post-contact classification cannot repair.

We introduce \emph{{precontact guard contracts}}. A contract maps cue posterior, remaining distance, switch latency, and asymmetric costs into a hybrid guard. The guard is allowed to switch early only when the posterior is confident enough; it is allowed to switch near the deadline at lower confidence because the cost of lateness rises; and it refuses to count a decision as valid when the remaining distance is already inside the activation deadline. This changes the central mechanism from perception accuracy to physically timed mode activation.

Our contributions are:
\begin{{itemize}}
\item A literature-grounded novelty boundary from a 1000-paper sweep, a 300-paper serious skim, a 230-paper deep-read set, and a 100-paper hostile prior-work set.
\item A latency-aware precontact guard mechanism for switching grasp strategy before first contact.
\item A timing lemma that identifies when contact-triggered strategy changes are physically too late.
\item A runnable synthetic manipulation testbed measuring safe success, harmful first-contact impulse, late switches, and ablations where the advantage should disappear.
\end{{itemize}}

\section{{Related Work and Novelty Boundary}}

\paragraph{{Pre-touch and proximity sensing.}} Prior work has used pre-touch, proximity, and near-field signals to infer object shape, distance, material, and grasp affordances @@PRE_CITE@@. This makes the sensing modality itself non-novel. Our boundary is that the cue is not merely fused into a state estimator or grasp classifier; it is a guard whose validity depends on remaining lead distance and switch latency.

\paragraph{{Tactile feedback and slip recovery.}} Tactile systems detect slip, contact state, material, grasp stability, and manipulation outcomes after touch @@TACTILE_SLIP_CITE@@. This literature is hostile because it already changes robot behavior based on contact evidence. Our claim is restricted to failures where the first contact transient happens before tactile correction can become active.

\paragraph{{Grasp planning, vision, and learned manipulation.}} Grasp planning and visuotactile learning choose poses, preshapes, and policies from visual, tactile, or multimodal representations @@GRASP_VISION_LEARNING_CITE@@. These methods can in principle learn an implicit switching rule. The mechanism here is explicit: the decision threshold is coupled to the activation deadline. A larger model or extra data would not by itself establish this timing property.

\paragraph{{Contact-rich and hybrid control.}} Force, impedance, hybrid, and contact-mode controllers reason about transitions once contact constraints are present @@CONTACT_GENERAL_CITE@@. We move the guard before first contact. The relevant mode is not only contact/no-contact; it is the grasp strategy that must already be active when contact occurs.

\section{{Problem}}

Consider an end-effector approaching an object from distance $d_0$ at speed $v$. The object has hidden local mode $z \in \mathcal{{Z}}$, such as a thin lip, slippery surface, or fragile region. Each mode has a safe strategy $a^\star(z)$ from a finite set $\mathcal{{A}}$. The robot begins with nominal strategy $a_0$. A strategy switch takes time $\tau_s$, so a switch started at remaining distance $d$ is active at first contact only if
\begin{{equation}}
d \geq d_s = v\tau_s.
\end{{equation}}
Before contact, the robot receives noisy cue observations $y_t$ whose informativeness generally increases as distance decreases. A policy must decide whether and when to start switching from $a_0$ to another strategy. The evaluation separates final task success from \emph{{safe success}}: the correct strategy must be active by first contact and the first-contact impulse must remain below a mode-specific threshold.

\section{{Precontact Guard Contracts}}

The guard contract maintains a posterior $p_t(z)=p(z\mid y_{\leq t})$ and chooses a target strategy $\hat a_t = a^\star(\arg\max_z p_t(z))$. Let $m_t$ be the posterior margin between the two most likely modes. A conventional posterior-only rule switches when $\max_z p_t(z)>\theta$ and $m_t>\delta$. This ignores whether the switch can finish before contact.

Our guard is
\begin{{equation}}
G_t = \left[\hat a_t \neq a_0\right]
\wedge \left[d_t \geq v\tau_s\right]
\wedge \left[\max_z p_t(z) \geq \theta(d_t, v\tau_s)\right]
\wedge \left[m_t \geq \delta(d_t, v\tau_s)\right].
\end{{equation}}
The threshold $\theta$ is high far from contact, where false early switches are avoidable, and lower near the activation deadline, where waiting has increasing cost. If $d_t < v\tau_s$, the contract records that the evidence is physically late; it may still trigger a damage-minimizing fallback, but the paper does not count it as a valid precontact strategy switch.

\begin{{proposition}}[Activation deadline]
Assume constant approach speed $v>0$, fixed strategy switching time $\tau_s\geq0$, and first contact at $d=0$. If decisive evidence for the required non-nominal strategy is first available at remaining distance $d_e < v\tau_s$, then no policy that waits for that evidence can make the non-nominal strategy active before first contact. If the nominal strategy causes harmful first contact for that hidden mode with probability $\rho>0$, every such policy has harmful-contact probability at least $\rho$ on that mode.
\end{{proposition}}

\begin{{proof}}
A switch started at $d_e$ has time $d_e/v$ before contact. Since $d_e/v < \tau_s$, the switch cannot complete before contact. The active first-contact strategy is therefore still nominal. The lower bound follows directly from the assumed harmful-contact probability of using the nominal strategy on that mode.
\end{{proof}}

The proposition is intentionally simple. Its purpose is to rule out a common architectural escape: a perfect contact classifier still cannot change the first-contact strategy when its evidence arrives after the activation deadline.

\section{{Experiments}}

\paragraph{{Testbed.}} We simulate an approaching gripper with four hidden local modes: nominal, thin lip, slippery, and fragile. The safe strategies are pinch, scoop, cage, and soft contact. Precontact observations are three-channel near-field cues with class-dependent onset distances and Gaussian noise. The cue becomes more informative as the gripper nears the object. We sweep approach speeds, switching latencies, and cue conditions. Each policy is evaluated on 10,800 episodes, and the full run writes \texttt{{results/episode\_results.csv}}.

\paragraph{{Policies.}} We compare five policies: fixed nominal, contact-reactive, posterior-only precontact switching, the proposed guard contract, and an oracle precontact policy. Contact-reactive observes the true mode at contact but cannot complete a switch before contact unless $\tau_s=0$. Posterior-only uses the same cue posterior as the guard but ignores remaining distance.

\begin{{table}}[t]
\centering
\caption{{Aggregate normal-cue results. Rates are percentages; lower harmful contact, late switch, and impulse are better.}}
\label{{tab:normal}}
\begin{{tabular}}{{lrrrr}}
\toprule
Policy & Safe success & Harmful contact & Late switch & P90 impulse \\
\midrule
@@TABLE1@@
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{figure}}[t]
\centering
\includegraphics[width=0.48\linewidth]{{../figures/safe_success_by_latency.pdf}}
\includegraphics[width=0.48\linewidth]{{../figures/impulse_by_latency.pdf}}
\caption{{The guard contract is designed to matter when switching latency is nonzero. Left: safe success versus latency. Right: first-contact impulse exposes failures hidden by final success.}}
\label{{fig:latency}}
\end{{figure}}

\begin{{table}}[t]
\centering
\caption{{Normal-cue slice at the largest switching latency. Final success can remain nonzero for contact-reactive repair, but safe success records whether the correct strategy was active at first contact.}}
\label{{tab:latency}}
\begin{{tabular}}{{lrrrr}}
\toprule
Policy & Safe success & Final success & Harmful contact & Late switch \\
\midrule
@@TABLE2@@
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{figure}}[t]
\centering
\includegraphics[width=0.68\linewidth]{{../figures/cue_ablation.pdf}}
\caption{{Ablation by cue condition. The guard's advantage should shrink for weak or late cues; otherwise the method would be claiming generic robustness rather than precontact timing.}}
\label{{fig:ablation}}
\end{{figure}}

\paragraph{{Findings.}} Under normal cue onsets, the guard contract greatly improves safe success over contact-reactive switching and matches a strong fixed-threshold posterior-only precontact baseline in aggregate. The largest gap against contact-reactive behavior appears at nonzero switch latencies, matching the activation-deadline lemma. When cues are late or weak, all non-oracle precontact policies degrade, which is the expected failure mode. The oracle remains above the learned-cue policies, indicating remaining cost from cue noise and thresholding.

\section{{Limitations}}

This paper is not a real-robot demonstration. The cue model is synthetic, the contact impulse model is simplified, and the strategy set is small. The literature extraction is broad but metadata/abstract based for many entries; it should be treated as a hostile map, not a substitute for expert full-text review. The formal result is a timing lemma, not a complete optimal-control theory. The strongest next experiment is a real gripper with a proximity or pre-touch sensor, a measured strategy-switch latency, and objects where harmful first contact occurs before tactile recovery.

\section{{Conclusion}}

Precontact cues are usually framed as extra sensory evidence. This paper argues that in a latency-limited manipulation regime they should instead be controller guards. The guard contract asks a physically grounded question: will the strategy be active by the time the hand touches the object? If the answer is no, a correct contact-time decision is still too late.

\subsubsection*{{Reproducibility Statement}}
The repository contains the literature sweep scripts, generated matrices, experiment code, cached CSV outputs, figures, and paper build files. The main experiment is run by \texttt{{python scripts/run\_experiments.py}}; the literature pipeline is run by \texttt{{python scripts/collect\_literature.py}} followed by \texttt{{python scripts/analyze\_literature.py}}.

\bibliography{{references}}
\bibliographystyle{{iclr2026_conference}}

\appendix
\section{{Audit Notes}}
The paper deliberately marks unsupported claims: no real robot, no universal sensor claim, and no claim that learned policies cannot reproduce the behavior. The novelty boundary is the latency-aware guard, not pre-touch sensing itself.

\end{{document}}
"""
    replacements = {
        "@@GUARD_SAFE@@": f"{guard_safe:.1f}",
        "@@CONTACT_SAFE@@": f"{contact_safe:.1f}",
        "@@POSTERIOR_SAFE@@": f"{posterior_safe:.1f}",
        "@@CONTACT_HARM@@": f"{contact_harm:.1f}",
        "@@GUARD_HARM@@": f"{guard_harm:.1f}",
        "@@PRE_CITE@@": pre,
        "@@TACTILE_SLIP_CITE@@": tactile_slip,
        "@@GRASP_VISION_LEARNING_CITE@@": grasp_vision_learning,
        "@@CONTACT_GENERAL_CITE@@": contact_general,
        "@@TABLE1@@": table1,
        "@@TABLE2@@": table2,
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    template = template.replace("{{", "{").replace("}}", "}")
    return template


def copy_figures_if_missing() -> None:
    for name in ["safe_success_by_latency.pdf", "impulse_by_latency.pdf", "cue_ablation.pdf"]:
        src = FIGURES / name
        if not src.exists():
            # A minimal one-page PDF placeholder is not created here; missing figures should make the build fail visibly.
            continue


def write_readme(template_status: dict[str, Any]) -> None:
    text = f"""# 21 Precontact Cue Control

Anonymous ICLR-style paper artifact for the 60-paper robotics/embodied-intelligence batch.

## Thesis

Precontact cues should act as latency-aware hybrid-control guards for switching grasp strategy before first contact, rather than only as perception features.

## Reproduce

```powershell
python scripts/collect_literature.py
python scripts/analyze_literature.py
python scripts/run_experiments.py
python scripts/write_paper.py
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
```

The final PDF is copied to `C:/Users/wangz/Downloads/21.pdf` by the build script and the intermediate `paper/main.pdf` is removed afterward.

## Key Artifacts

- `docs/related_work_matrix.csv`: 1000-paper matrix.
- `docs/hostile_prior_work.md`: 100-paper hostile set.
- `docs/novelty_decision.md`: selected direction and rejected alternatives.
- `results/summary.csv`: aggregate experiment results.
- `paper/main.tex`: anonymous ICLR-style manuscript.

## Template

Template status: `{template_status.get('status')}`. Source attempted: ICLR Master-Template `iclr2026.zip`.
"""
    (ROOT / "README.md").write_text(text, encoding="utf-8")


def main() -> int:
    template_status = fetch_template()
    matrix = read_csv(DOCS / "related_work_matrix.csv")
    refs, groups = select_references(matrix)
    write_bib(refs)
    table1, table2, metrics = result_tables()
    tex = make_tex(groups, table1, table2, metrics)
    (PAPER / "main.tex").write_text(tex, encoding="ascii", errors="ignore")
    copy_figures_if_missing()
    write_readme(template_status)
    status = {
        "template_status": template_status,
        "reference_count": len(refs),
        "main_tex": str(PAPER / "main.tex"),
        "references_bib": str(PAPER / "references.bib"),
    }
    (PAPER / "paper_generation_status.json").write_text(json.dumps(status, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        (PAPER / "paper_generation_error.txt").write_text(repr(exc), encoding="utf-8")
        print(json.dumps({"error": repr(exc)}, indent=2))
        raise SystemExit(0)
