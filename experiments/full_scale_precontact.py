from __future__ import annotations

import csv
import json
import math
import platform
import statistics
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGURES = ROOT / "figures" / "full_scale"
TEX = RESULTS / "tex"
DOCS = ROOT / "docs"
SEED = 21021


@dataclass(frozen=True)
class Mode:
    name: str
    strategy: str
    prototype: tuple[float, float, float, float]
    onset: float
    impulse_threshold: float
    mismatch_severity: float
    harm_cost: float


@dataclass(frozen=True)
class Case:
    case_id: int
    mode_idx: int
    velocity: float
    latency: float
    condition: str
    model_condition: str
    calibrated_condition: str
    false_cost: float = 1.0
    harm_scale: float = 1.0
    special: str = "none"


MODES = [
    Mode("nominal", "pinch", (0.28, 0.10, 0.04, 0.02), 0.026, 0.64, 0.52, 0.40),
    Mode("thin_lip", "scoop", (1.15, -0.24, 0.18, 0.06), 0.056, 0.52, 0.92, 2.40),
    Mode("slippery", "cage", (0.10, 1.05, -0.25, 0.20), 0.047, 0.48, 0.84, 2.05),
    Mode("fragile", "soft", (-0.22, 0.16, 1.12, 0.23), 0.052, 0.36, 1.22, 3.45),
    Mode("occluded_rim", "tilt", (0.83, -0.10, 0.34, 0.82), 0.044, 0.45, 0.98, 2.65),
    Mode("compliant_skin", "soft", (-0.08, 0.30, 0.82, 1.05), 0.050, 0.39, 1.05, 3.05),
]
PROTOTYPES = np.asarray([m.prototype for m in MODES], dtype=float)
STRATEGIES = sorted({m.strategy for m in MODES})
POLICY_OFFSETS = {
    "fixed_nominal": 11,
    "contact_reactive": 23,
    "posterior_fixed": 37,
    "posterior_tuned": 41,
    "posterior_cost_tuned": 43,
    "source_tuned_posterior": 47,
    "calibrated_posterior": 53,
    "v2_guard": 59,
    "deadline_threshold": 61,
    "risk_guard": 67,
    "calibrated_deadline_guard": 71,
    "risk_no_deadline": 73,
    "risk_no_cost": 79,
    "risk_no_margin": 83,
    "distance_only": 89,
    "oracle_precontact": 97,
}
ROW_FIELDS = [
    "family",
    "case_id",
    "policy",
    "mode",
    "condition",
    "velocity",
    "switch_latency",
    "switch_distance",
    "false_cost",
    "harm_scale",
    "special",
    "required_strategy",
    "active_strategy_at_contact",
    "predicted_mode",
    "switch_target",
    "switch_started_distance",
    "deadline_margin",
    "posterior_confidence",
    "posterior_margin",
    "safe_success",
    "final_success",
    "harmful_contact",
    "late_switch",
    "early_false_switch",
    "deadline_violation",
    "avoidable_lateness",
    "impulse",
    "expected_cost",
    "switch_reason",
]
METRICS = [
    "safe_success",
    "final_success",
    "harmful_contact",
    "late_switch",
    "early_false_switch",
    "deadline_violation",
    "avoidable_lateness",
    "impulse",
    "expected_cost",
]


def ensure_dirs() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    TEX.mkdir(parents=True, exist_ok=True)


def stable_seed(case_id: int, policy: str, salt: int = 0) -> int:
    return int(SEED + 1009 * case_id + 9176 * POLICY_OFFSETS.get(policy, 101) + salt)


def softmax(logp: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    z = logp / max(temperature, 1e-6)
    z = z - np.max(z)
    e = np.exp(z)
    return e / np.sum(e)


def condition_noise(condition: str) -> float:
    return {
        "normal": 0.205,
        "early_cue": 0.200,
        "weak_cue": 0.275,
        "late_cue": 0.215,
        "high_noise": 0.365,
        "uninformative_until_contact": 0.225,
        "random_cue": 0.330,
        "onset_late_shift": 0.250,
        "onset_early_shift": 0.225,
        "prototype_drift": 0.260,
        "noise_shift": 0.365,
        "mixed_velocity_shift": 0.240,
    }.get(condition, 0.220)


def condition_onset(mode: Mode, condition: str) -> float:
    onset = mode.onset
    if condition == "early_cue":
        onset *= 1.38
    elif condition == "weak_cue":
        onset *= 0.70
    elif condition == "late_cue":
        onset = min(onset * 0.45, 0.018)
    elif condition == "uninformative_until_contact":
        onset = 0.0015
    elif condition == "onset_late_shift":
        onset *= 0.62
    elif condition == "onset_early_shift":
        onset *= 1.30
    return onset


def condition_amp_scale(condition: str) -> float:
    if condition == "weak_cue":
        return 0.56
    if condition == "high_noise":
        return 0.90
    if condition == "noise_shift":
        return 0.92
    return 1.0


def prototype_for(idx: int, condition: str, actual: bool) -> np.ndarray:
    proto = PROTOTYPES[idx].copy()
    if actual and condition == "prototype_drift":
        drift = np.array([0.12, -0.10, 0.08, -0.06], dtype=float)
        proto = 0.84 * proto + 0.16 * PROTOTYPES[(idx + 2) % len(MODES)] + ((idx % 3) - 1) * 0.05 * drift
    return proto


def cue_amplitude(idx: int, distance: float, condition: str) -> float:
    onset = condition_onset(MODES[idx], condition)
    if condition == "random_cue":
        return 0.0
    if distance > onset:
        return 0.0
    x = max(0.0, 1.0 - distance / max(onset, 1e-6))
    return condition_amp_scale(condition) * (x ** 1.25)


def observe(mode_idx: int, distance: float, condition: str, rng: np.random.Generator) -> np.ndarray:
    noise = condition_noise(condition)
    if condition == "random_cue":
        return rng.normal(0.0, noise, size=4)
    mean = prototype_for(mode_idx, condition, actual=True) * cue_amplitude(mode_idx, distance, condition)
    return mean + rng.normal(0.0, noise, size=4)


def log_likelihood(obs: np.ndarray, distance: float, condition: str) -> np.ndarray:
    noise = condition_noise(condition)
    sigma2 = max(noise * noise, 1e-6)
    out = np.zeros(len(MODES), dtype=float)
    for idx in range(len(MODES)):
        pred = prototype_for(idx, condition, actual=False) * cue_amplitude(idx, distance, condition)
        out[idx] = -0.5 * float(np.sum((obs - pred) ** 2) / sigma2)
    return out


def posterior_by_strategy(post: np.ndarray) -> dict[str, float]:
    out = {s: 0.0 for s in STRATEGIES}
    for idx, mode in enumerate(MODES):
        out[mode.strategy] += float(post[idx])
    return out


def posterior_threshold(distance: float, start_distance: float, switch_distance: float) -> float:
    if distance < switch_distance:
        return 1.02
    far_fraction = min(1.0, max(0.0, distance / start_distance))
    return 0.68 + 0.24 * far_fraction


def cost_tuned_thresholds(case: Case) -> tuple[float, float]:
    pressure = case.harm_scale / max(case.harm_scale + case.false_cost, 1e-9)
    conf = 0.93 - 0.34 * pressure
    margin = 0.34 - 0.22 * pressure
    return float(np.clip(conf, 0.50, 0.95)), float(np.clip(margin, 0.04, 0.38))


def select_risk_action(post: np.ndarray, case: Case) -> tuple[str, float, float, float]:
    p_strategy = posterior_by_strategy(post)
    candidates = [(s, p) for s, p in p_strategy.items() if s != "pinch"]
    target, p_target = max(candidates, key=lambda item: item[1])
    avoidable_target_harm = 0.0
    switch_wrong = 0.0
    for idx, mode in enumerate(MODES):
        p = float(post[idx])
        if mode.strategy == target:
            avoidable_target_harm += p * mode.harm_cost * case.harm_scale
        if mode.strategy != target:
            switch_wrong += p * (case.false_cost + 0.35 * mode.harm_cost * case.harm_scale)
    return target, p_target, avoidable_target_harm, switch_wrong


def impulse_for(mode: Mode, active_strategy: str, velocity: float, latency: float, case: Case, rng: np.random.Generator) -> float:
    if case.special == "equal_impulse":
        base = 0.27 + 0.34 * velocity + 0.015 * rng.normal()
        return max(0.0, base)
    if active_strategy == mode.strategy:
        return max(0.0, 0.10 + 0.42 * velocity + 0.025 * rng.normal())
    if active_strategy == "pinch":
        return max(0.0, mode.mismatch_severity + 1.55 * velocity + 1.25 * latency + 0.070 * rng.normal())
    strategy_penalty = {
        "scoop": 0.12,
        "cage": 0.10,
        "soft": 0.08,
        "tilt": 0.14,
        "pinch": 0.18,
    }.get(active_strategy, 0.15)
    false_pressure = 0.035 * min(case.false_cost, 10.0)
    return max(0.0, 0.72 * mode.mismatch_severity + strategy_penalty + false_pressure + 1.18 * velocity + 0.80 * latency + 0.075 * rng.normal())


def final_success_probability(policy: str, mode: Mode, active_strategy: str, impulse: float, harmful: int) -> float:
    if active_strategy == mode.strategy and not harmful:
        return 0.965
    if active_strategy == mode.strategy:
        return 0.70
    if policy == "contact_reactive":
        return max(0.02, 0.56 - 0.24 * harmful - 0.18 * max(0.0, impulse - mode.impulse_threshold))
    return max(0.01, 0.22 - 0.15 * harmful - 0.10 * max(0.0, impulse - mode.impulse_threshold))


def run_policy(case: Case, policy: str, params: dict[str, Any] | None = None, family: str = "") -> dict[str, Any]:
    params = params or {}
    mode = MODES[case.mode_idx]
    start_distance = 0.078
    step_distance = 0.003
    distances = np.arange(start_distance, -1e-9, -step_distance)
    switch_distance = case.velocity * case.latency
    cue_rng = np.random.default_rng(stable_seed(case.case_id, "posterior_fixed", 101))
    out_rng = np.random.default_rng(stable_seed(case.case_id, policy, 313))
    model_condition = case.model_condition
    temperature = 1.0
    if policy in {"calibrated_deadline_guard", "calibrated_posterior"}:
        model_condition = case.calibrated_condition
        temperature = 1.28
    if policy == "source_tuned_posterior":
        model_condition = "normal"
    if policy == "calibrated_posterior":
        model_condition = case.calibrated_condition

    logp = np.zeros(len(MODES), dtype=float) - math.log(len(MODES))
    switch_started_distance: float | None = None
    switch_target = "pinch"
    switch_reason = "none"
    predicted_idx = 0
    posterior_conf = 1.0 / len(MODES)
    posterior_margin = 0.0
    guard_streak = 0
    guard_target = ""
    first_required_confident_distance: float | None = None

    if policy == "oracle_precontact":
        switch_started_distance = start_distance
        switch_target = mode.strategy
        switch_reason = "oracle"
        predicted_idx = case.mode_idx
        posterior_conf = 1.0
        posterior_margin = 1.0
    elif policy == "contact_reactive":
        predicted_idx = case.mode_idx
        posterior_conf = 1.0
        posterior_margin = 1.0
        switch_target = mode.strategy
        switch_reason = "contact"
        switch_started_distance = 0.0
    elif policy != "fixed_nominal":
        for d0 in distances:
            d = float(d0)
            obs = observe(case.mode_idx, d, case.condition, cue_rng)
            logp += log_likelihood(obs, d, model_condition)
            post = softmax(logp, temperature=temperature)
            order = np.argsort(post)[::-1]
            predicted_idx = int(order[0])
            second = int(order[1])
            predicted_mode = MODES[predicted_idx]
            posterior_conf = float(post[predicted_idx])
            posterior_margin = float(post[predicted_idx] - post[second])
            required_prob = sum(float(post[i]) for i, m in enumerate(MODES) if m.strategy == mode.strategy)
            if mode.strategy != "pinch" and required_prob >= 0.60 and first_required_confident_distance is None:
                first_required_confident_distance = d
            target = predicted_mode.strategy
            if target == "pinch":
                guard_streak = 0
                guard_target = ""
                continue

            if policy in {"posterior_fixed", "posterior_tuned", "source_tuned_posterior", "calibrated_posterior"}:
                chosen = params.get("by_condition", {}).get(case.condition, params)
                conf = float(chosen.get("conf", 0.90))
                margin = float(chosen.get("margin", 0.24))
                if posterior_conf >= conf and posterior_margin >= margin:
                    switch_started_distance = d
                    switch_target = target
                    switch_reason = f"posterior_{conf:.2f}_{margin:.2f}"
                    break
            elif policy == "posterior_cost_tuned":
                conf, margin = cost_tuned_thresholds(case)
                if posterior_conf >= conf and posterior_margin >= margin:
                    switch_started_distance = d
                    switch_target = target
                    switch_reason = f"cost_posterior_{conf:.2f}_{margin:.2f}"
                    break
            elif policy == "v2_guard":
                theta = posterior_threshold(d, start_distance, switch_distance)
                slack = d - switch_distance
                urgency_margin = 0.22 if slack < 0.010 else 0.28
                if d >= switch_distance and posterior_conf >= theta and posterior_margin >= urgency_margin:
                    if target == guard_target:
                        guard_streak += 1
                    else:
                        guard_target = target
                        guard_streak = 1
                    if guard_streak >= 2:
                        switch_started_distance = d
                        switch_target = target
                        switch_reason = "v2_guard"
                        break
                else:
                    guard_streak = 0
                    guard_target = ""
            elif policy in {"deadline_threshold", "calibrated_deadline_guard"}:
                slack = d - switch_distance
                if d >= switch_distance:
                    p_strategy = posterior_by_strategy(post)
                    ranked_strategies = sorted(p_strategy.items(), key=lambda item: item[1], reverse=True)
                    strategy_target, strategy_conf = ranked_strategies[0]
                    if strategy_target == "pinch":
                        continue
                    strategy_margin = strategy_conf - ranked_strategies[1][1]
                    denom = max(start_distance - switch_distance, 1e-6)
                    urgency = 1.0 - min(1.0, max(0.0, slack / denom))
                    conf = 0.94 - 0.16 * urgency
                    margin = 0.24 - 0.08 * urgency
                    if policy == "calibrated_deadline_guard":
                        conf -= 0.02
                        margin -= 0.01
                    if strategy_conf >= conf and strategy_margin >= margin:
                        switch_started_distance = d
                        switch_target = strategy_target
                        posterior_conf = float(strategy_conf)
                        posterior_margin = float(strategy_margin)
                        switch_reason = policy
                        break
            elif policy in {"risk_guard", "risk_no_deadline", "risk_no_cost", "risk_no_margin"}:
                risk_target, p_target, wait_harm, switch_wrong = select_risk_action(post, case)
                slack = d - switch_distance
                feasible = d >= switch_distance
                if policy == "risk_no_deadline":
                    feasible = True
                if policy == "risk_no_cost":
                    wait_harm = sum(float(post[i]) for i, m in enumerate(MODES) if m.strategy != "pinch")
                    switch_wrong = 1.0 - p_target
                urgency = 1.0 + 1.70 * math.exp(-max(slack, 0.0) / 0.014)
                if 0.0 <= slack < 0.006:
                    urgency += 0.60
                margin_ok = posterior_margin >= 0.035 or policy == "risk_no_margin"
                cost_ratio = case.false_cost / max(case.false_cost + case.harm_scale, 1e-9)
                p_floor = 0.54 + 0.14 * cost_ratio
                if feasible and p_target >= p_floor and margin_ok and wait_harm * urgency > switch_wrong + 0.10:
                    switch_started_distance = d
                    switch_target = risk_target
                    switch_reason = f"risk_{wait_harm * urgency:.2f}_{switch_wrong:.2f}"
                    break
            elif policy == "distance_only":
                if d >= switch_distance and d <= switch_distance + 0.014:
                    switch_started_distance = d
                    switch_target = target
                    switch_reason = "distance_only"
                    break

    if policy == "fixed_nominal":
        active_strategy = "pinch"
        switch_target = "pinch"
    elif policy == "contact_reactive":
        active_strategy = mode.strategy if case.latency <= 1e-12 else "pinch"
    else:
        if switch_started_distance is not None and switch_started_distance + 1e-12 >= switch_distance:
            active_strategy = switch_target
        else:
            active_strategy = "pinch"

    if policy == "oracle_precontact" and switch_distance > start_distance:
        active_strategy = "pinch"

    impulse = impulse_for(mode, active_strategy, case.velocity, case.latency, case, out_rng)
    threshold = 999.0 if case.special == "equal_impulse" else mode.impulse_threshold
    harmful_contact = int(impulse > threshold)
    early_false = int(active_strategy != "pinch" and active_strategy != mode.strategy)
    late_switch = int(mode.strategy != "pinch" and active_strategy != mode.strategy)
    deadline_violation = 0
    if switch_started_distance is not None and switch_started_distance < switch_distance and switch_target != "pinch":
        deadline_violation = 1
    if (
        late_switch
        and mode.strategy != "pinch"
        and switch_distance > 1e-12
        and active_strategy == "pinch"
    ):
        deadline_violation = 1
    avoidable_lateness = int(
        late_switch
        and switch_distance > 1e-12
        and first_required_confident_distance is not None
        and first_required_confident_distance >= switch_distance
    )
    safe_success = int(active_strategy == mode.strategy and not harmful_contact)
    final_prob = final_success_probability(policy, mode, active_strategy, impulse, harmful_contact)
    final_success = int(out_rng.random() < final_prob)
    expected_cost = (
        case.harm_scale * mode.harm_cost * harmful_contact
        + case.false_cost * early_false
        + 0.18 * impulse
        + 0.35 * late_switch
    )
    deadline_margin = "" if switch_started_distance is None else round(switch_started_distance - switch_distance, 5)
    return {
        "family": family,
        "case_id": case.case_id,
        "policy": policy,
        "mode": mode.name,
        "condition": case.condition,
        "velocity": round(case.velocity, 4),
        "switch_latency": round(case.latency, 4),
        "switch_distance": round(switch_distance, 5),
        "false_cost": round(case.false_cost, 4),
        "harm_scale": round(case.harm_scale, 4),
        "special": case.special,
        "required_strategy": mode.strategy,
        "active_strategy_at_contact": active_strategy,
        "predicted_mode": MODES[predicted_idx].name,
        "switch_target": switch_target,
        "switch_started_distance": "" if switch_started_distance is None else round(switch_started_distance, 5),
        "deadline_margin": deadline_margin,
        "posterior_confidence": round(posterior_conf, 5),
        "posterior_margin": round(posterior_margin, 5),
        "safe_success": safe_success,
        "final_success": final_success,
        "harmful_contact": harmful_contact,
        "late_switch": late_switch,
        "early_false_switch": early_false,
        "deadline_violation": deadline_violation,
        "avoidable_lateness": avoidable_lateness,
        "impulse": round(float(impulse), 5),
        "expected_cost": round(float(expected_cost), 5),
        "switch_reason": switch_reason,
    }


class GroupAgg:
    def __init__(self, keys: list[str]) -> None:
        self.keys = keys
        self.groups: dict[tuple[Any, ...], dict[str, Any]] = {}

    def add(self, row: dict[str, Any]) -> None:
        key = tuple(row[k] for k in self.keys)
        if key not in self.groups:
            self.groups[key] = {"n": 0, "sums": {m: 0.0 for m in METRICS}, "impulses": [], "costs": []}
        g = self.groups[key]
        g["n"] += 1
        for metric in METRICS:
            g["sums"][metric] += float(row[metric])
        g["impulses"].append(float(row["impulse"]))
        g["costs"].append(float(row["expected_cost"]))

    def rows(self) -> list[dict[str, Any]]:
        out = []
        for key, g in sorted(self.groups.items()):
            n = int(g["n"])
            row = {self.keys[i]: key[i] for i in range(len(self.keys))}
            row["n"] = n
            for metric in METRICS:
                mean = g["sums"][metric] / max(n, 1)
                row[f"{metric}_mean"] = round(mean, 6)
                if metric in {"safe_success", "harmful_contact", "late_switch", "early_false_switch", "deadline_violation"}:
                    row[f"{metric}_ci95"] = round(1.96 * math.sqrt(max(mean * (1.0 - mean), 0.0) / max(n, 1)), 6)
            row["impulse_p90"] = round(float(np.quantile(np.asarray(g["impulses"]), 0.90)), 6)
            row["expected_cost_p90"] = round(float(np.quantile(np.asarray(g["costs"]), 0.90)), 6)
            out.append(row)
        return out


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if not rows:
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def append_row(writer: csv.DictWriter, aggs: list[GroupAgg], row: dict[str, Any]) -> None:
    writer.writerow(row)
    for agg in aggs:
        agg.add(row)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def sf(value: Any, default: float = 0.0) -> float:
    try:
        x = float(value)
        if math.isfinite(x):
            return x
    except Exception:
        pass
    return default


def latex_escape(text: Any) -> str:
    return str(text).replace("_", r"\_").replace("%", r"\%")


def fmt(value: Any, digits: int = 3) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return latex_escape(value)


def write_table(path: Path, caption: str, label: str, columns: list[tuple[str, str]], rows: list[dict[str, Any]], digits: int = 3) -> None:
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\small",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\begin{tabular}{" + "l" + "c" * (len(columns) - 1) + "}",
        r"\toprule",
        " & ".join(latex_escape(c[1]) for c in columns) + r" \\",
        r"\midrule",
    ]
    for row in rows:
        lines.append(" & ".join(fmt(row.get(key, ""), digits) for key, _ in columns) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_progress(stage: str, family_status: dict[str, str], total_rows: int, total_cases: int, plot_failures: int = 0) -> None:
    payload = {
        "stage": stage,
        "family_status": family_status,
        "total_rows": total_rows,
        "total_cases": total_cases,
        "plot_failures": plot_failures,
        "updated_unix": time.time(),
    }
    (RESULTS / "progress.json").write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def tune_posterior_thresholds(condition: str, objective: str = "safe", false_cost: float = 1.0, harm_scale: float = 1.0) -> dict[str, float]:
    confs = [0.54, 0.64, 0.74, 0.84, 0.94]
    margins = [0.04, 0.12, 0.22, 0.34]
    velocities = [0.08, 0.18, 0.30]
    latencies = [0.0, 0.08, 0.16, 0.20]
    cases = []
    case_id = 100000
    for rep in range(2):
        for v in velocities:
            for lat in latencies:
                for mode_idx in range(len(MODES)):
                    cases.append(
                        Case(
                            case_id=case_id,
                            mode_idx=mode_idx,
                            velocity=v,
                            latency=lat,
                            condition=condition,
                            model_condition=condition,
                            calibrated_condition=condition,
                            false_cost=false_cost,
                            harm_scale=harm_scale,
                        )
                    )
                    case_id += 1 + rep
    best: dict[str, float] | None = None
    tune_rows = []
    for conf in confs:
        for margin in margins:
            safe = harmful = late = cost = 0.0
            for case in cases:
                row = run_policy(case, "posterior_tuned", {"conf": conf, "margin": margin}, family="tune")
                safe += float(row["safe_success"])
                harmful += float(row["harmful_contact"])
                late += float(row["late_switch"])
                cost += float(row["expected_cost"])
            n = len(cases)
            rec = {
                "condition": condition,
                "objective": objective,
                "conf": conf,
                "margin": margin,
                "safe_success_rate": safe / n,
                "harmful_contact_rate": harmful / n,
                "late_switch_rate": late / n,
                "expected_cost_mean": cost / n,
            }
            tune_rows.append(rec)
            score = rec["safe_success_rate"] - 0.10 * rec["harmful_contact_rate"] - 0.04 * rec["late_switch_rate"]
            if objective == "cost":
                score = -rec["expected_cost_mean"]
            if best is None or score > best["score"]:
                best = {**rec, "score": score}
    assert best is not None
    write_csv(RESULTS / f"tuning_{condition}_{objective}.csv", tune_rows)
    return {"conf": float(best["conf"]), "margin": float(best["margin"]), "score": float(best["score"])}


def stream_family(
    family: str,
    rows_path: Path,
    cases: list[Case],
    policies: list[str],
    params_by_policy: dict[str, dict[str, Any]] | None,
    group_specs: list[tuple[str, list[str]]],
) -> dict[str, Any]:
    params_by_policy = params_by_policy or {}
    aggs = [GroupAgg(keys) for _, keys in group_specs]
    row_count = 0
    t0 = time.perf_counter()
    with rows_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ROW_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for case in cases:
            for policy in policies:
                row = run_policy(case, policy, params_by_policy.get(policy), family=family)
                append_row(writer, aggs, row)
                row_count += 1
    summary_paths = {}
    for (name, _), agg in zip(group_specs, aggs):
        path = RESULTS / f"{family}_{name}.csv"
        write_csv(path, agg.rows())
        summary_paths[name] = str(path.relative_to(ROOT))
    return {
        "family": family,
        "rows": row_count,
        "cases": len(cases),
        "seconds": time.perf_counter() - t0,
        "rows_path": str(rows_path.relative_to(ROOT)),
        "summaries": summary_paths,
    }


def family_a_main() -> dict[str, Any]:
    conditions = ["normal", "early_cue", "weak_cue", "late_cue", "high_noise", "uninformative_until_contact"]
    velocities = [0.06, 0.10, 0.16, 0.22, 0.30]
    latencies = [0.0, 0.03, 0.06, 0.09, 0.12, 0.16, 0.20]
    thresholds = {cond: tune_posterior_thresholds(cond, "safe") for cond in conditions}
    write_csv(RESULTS / "family_a_tuned_thresholds.csv", [{"condition": k, **v} for k, v in thresholds.items()])
    cases = []
    case_id = 1
    reps = 8
    for condition in conditions:
        for v in velocities:
            for lat in latencies:
                for rep in range(reps):
                    for mode_idx in range(len(MODES)):
                        cases.append(Case(case_id, mode_idx, v, lat, condition, condition, condition))
                        case_id += 1
    policies = [
        "fixed_nominal",
        "contact_reactive",
        "posterior_fixed",
        "posterior_tuned",
        "v2_guard",
        "deadline_threshold",
        "risk_guard",
        "calibrated_deadline_guard",
        "oracle_precontact",
    ]
    params = {"posterior_tuned": {"by_condition": thresholds}}
    result = stream_family(
        "family_a",
        RESULTS / "family_a_rows.csv",
        cases,
        policies,
        params,
        [
            ("summary_by_condition_policy", ["condition", "policy"]),
            ("summary_by_latency", ["condition", "policy", "switch_latency"]),
            ("summary_by_mode", ["condition", "policy", "mode"]),
        ],
    )
    result["tuned_thresholds"] = thresholds
    return result


def family_b_cost() -> dict[str, Any]:
    cases = []
    case_id = 300000
    harm_scales = [0.5, 1.0, 2.0, 4.0, 8.0]
    false_costs = [0.25, 0.75, 1.5, 3.0, 6.0]
    velocities = [0.10, 0.18, 0.26]
    latencies = [0.06, 0.10, 0.14]
    for harm in harm_scales:
        for false in false_costs:
            for v in velocities:
                for lat in latencies:
                    for rep in range(4):
                        for mode_idx in range(len(MODES)):
                            cases.append(Case(case_id, mode_idx, v, lat, "normal", "normal", "normal", false, harm))
                            case_id += 1
    policies = ["posterior_fixed", "posterior_cost_tuned", "v2_guard", "risk_guard", "calibrated_deadline_guard", "oracle_precontact"]
    return stream_family(
        "family_b",
        RESULTS / "family_b_rows.csv",
        cases,
        policies,
        {},
        [
            ("summary_by_cost", ["harm_scale", "false_cost", "policy"]),
            ("summary_by_policy", ["policy"]),
        ],
    )


def family_c_shift() -> dict[str, Any]:
    shift_conditions = ["normal", "onset_late_shift", "onset_early_shift", "prototype_drift", "noise_shift", "mixed_velocity_shift"]
    velocities_by_condition = {
        "mixed_velocity_shift": [0.05, 0.12, 0.28, 0.34],
    }
    cases = []
    case_id = 500000
    for condition in shift_conditions:
        velocities = velocities_by_condition.get(condition, [0.08, 0.16, 0.24, 0.30])
        for v in velocities:
            for lat in [0.04, 0.08, 0.12, 0.18]:
                for rep in range(8):
                    for mode_idx in range(len(MODES)):
                        cases.append(Case(case_id, mode_idx, v, lat, condition, "normal", condition))
                        case_id += 1
    policies = ["source_tuned_posterior", "calibrated_posterior", "risk_guard", "calibrated_deadline_guard", "oracle_precontact"]
    params = {
        "source_tuned_posterior": {"conf": 0.76, "margin": 0.12},
        "calibrated_posterior": {"conf": 0.70, "margin": 0.08},
    }
    return stream_family(
        "family_c",
        RESULTS / "family_c_rows.csv",
        cases,
        policies,
        params,
        [
            ("summary_by_shift", ["condition", "policy"]),
            ("summary_by_shift_latency", ["condition", "policy", "switch_latency"]),
        ],
    )


def family_d_negative() -> dict[str, Any]:
    scenario_defs = [
        ("zero_latency", "normal", 0.0, 1.0, 1.0, "none"),
        ("evidence_at_contact", "uninformative_until_contact", 0.10, 1.0, 1.0, "none"),
        ("random_cue", "random_cue", 0.10, 1.0, 1.0, "none"),
        ("no_hidden_mode", "normal", 0.10, 1.0, 1.0, "nominal_only"),
        ("equal_impulse", "normal", 0.10, 1.0, 1.0, "equal_impulse"),
        ("early_switch_cost_high", "normal", 0.10, 8.0, 1.0, "none"),
        ("switch_too_slow", "normal", 0.34, 1.0, 1.0, "none"),
    ]
    cases = []
    case_id = 700000
    for scenario, condition, latency, false_cost, harm, special in scenario_defs:
        mode_indices = [0] if special == "nominal_only" else list(range(len(MODES)))
        for v in [0.08, 0.16, 0.24, 0.30]:
            for rep in range(14):
                for mode_idx in mode_indices:
                    cases.append(Case(case_id, mode_idx, v, latency, condition, condition, condition, false_cost, harm, scenario))
                    case_id += 1
    policies = ["posterior_fixed", "posterior_cost_tuned", "v2_guard", "deadline_threshold", "risk_guard", "calibrated_deadline_guard", "oracle_precontact"]
    return stream_family(
        "family_d",
        RESULTS / "family_d_rows.csv",
        cases,
        policies,
        {},
        [
            ("summary_by_scenario", ["special", "policy"]),
            ("summary_by_scenario_mode", ["special", "policy", "mode"]),
        ],
    )


def family_e_ablations() -> dict[str, Any]:
    cases = []
    case_id = 900000
    conditions = ["normal", "weak_cue", "late_cue", "high_noise"]
    for condition in conditions:
        for v in [0.08, 0.16, 0.24, 0.30]:
            for lat in [0.04, 0.08, 0.12, 0.16, 0.20]:
                for rep in range(8):
                    for mode_idx in range(len(MODES)):
                        cases.append(Case(case_id, mode_idx, v, lat, condition, condition, condition, 1.0, 2.0))
                        case_id += 1
    policies = [
        "posterior_fixed",
        "deadline_threshold",
        "risk_guard",
        "calibrated_deadline_guard",
        "risk_no_deadline",
        "risk_no_cost",
        "risk_no_margin",
        "distance_only",
    ]
    return stream_family(
        "family_e",
        RESULTS / "family_e_rows.csv",
        cases,
        policies,
        {},
        [
            ("summary_by_ablation", ["condition", "policy"]),
            ("summary_by_ablation_latency", ["condition", "policy", "switch_latency"]),
        ],
    )


def make_tables() -> None:
    a = read_csv(RESULTS / "family_a_summary_by_condition_policy.csv")
    normal = [r for r in a if r["condition"] == "normal"]
    order = ["fixed_nominal", "contact_reactive", "posterior_fixed", "posterior_tuned", "v2_guard", "deadline_threshold", "risk_guard", "calibrated_deadline_guard", "oracle_precontact"]
    normal_rows = sorted(normal, key=lambda r: order.index(r["policy"]) if r["policy"] in order else 99)
    write_table(
        TEX / "table_main_normal.tex",
        "Family A normal-cue aggregate. Safe success requires the correct strategy to be active by first contact and no harmful impulse.",
        "tab:main-normal",
        [
            ("policy", "Policy"),
            ("safe_success_mean", "Safe success"),
            ("harmful_contact_mean", "Harmful"),
            ("late_switch_mean", "Late"),
            ("early_false_switch_mean", "Early false"),
            ("expected_cost_mean", "Cost"),
        ],
        normal_rows,
    )
    high_latency = [r for r in read_csv(RESULTS / "family_a_summary_by_latency.csv") if r["condition"] == "normal" and abs(sf(r["switch_latency"]) - 0.20) < 1e-9]
    high_latency = sorted(high_latency, key=lambda r: order.index(r["policy"]) if r["policy"] in order else 99)
    write_table(
        TEX / "table_high_latency.tex",
        "Family A high-latency normal-cue slice at 0.20 s switch latency.",
        "tab:high-latency",
        [
            ("policy", "Policy"),
            ("safe_success_mean", "Safe success"),
            ("harmful_contact_mean", "Harmful"),
            ("deadline_violation_mean", "Deadline viol."),
            ("impulse_p90", "p90 impulse"),
        ],
        high_latency,
    )
    b = read_csv(RESULTS / "family_b_summary_by_policy.csv")
    write_table(
        TEX / "table_cost_policy.tex",
        "Family B cost-asymmetry aggregate. The risk guard optimizes expected first-contact cost rather than only posterior confidence.",
        "tab:cost-policy",
        [
            ("policy", "Policy"),
            ("expected_cost_mean", "Mean cost"),
            ("safe_success_mean", "Safe success"),
            ("harmful_contact_mean", "Harmful"),
            ("early_false_switch_mean", "Early false"),
        ],
        sorted(b, key=lambda r: sf(r["expected_cost_mean"])),
    )
    c = read_csv(RESULTS / "family_c_summary_by_shift.csv")
    write_table(
        TEX / "table_shift.tex",
        "Family C distribution shift. Source-tuned posterior thresholds use the normal-cue source model; calibrated policies receive the shifted cue model.",
        "tab:shift",
        [
            ("condition", "Shift"),
            ("policy", "Policy"),
            ("safe_success_mean", "Safe success"),
            ("harmful_contact_mean", "Harmful"),
            ("deadline_violation_mean", "Deadline viol."),
            ("expected_cost_mean", "Cost"),
        ],
        sorted(c, key=lambda r: (r["condition"], sf(r["expected_cost_mean"]))),
    )
    d = read_csv(RESULTS / "family_d_summary_by_scenario.csv")
    keep = [r for r in d if r["policy"] in {"posterior_fixed", "risk_guard", "calibrated_deadline_guard", "oracle_precontact"}]
    write_table(
        TEX / "table_negative_controls.tex",
        "Family D negative controls. Benefits should disappear when latency, precontact information, or first-contact harm is removed.",
        "tab:negative-controls",
        [
            ("special", "Scenario"),
            ("policy", "Policy"),
            ("safe_success_mean", "Safe success"),
            ("harmful_contact_mean", "Harmful"),
            ("deadline_violation_mean", "Deadline viol."),
            ("expected_cost_mean", "Cost"),
        ],
        sorted(keep, key=lambda r: (r["special"], r["policy"])),
    )
    e = read_csv(RESULTS / "family_e_summary_by_ablation.csv")
    write_table(
        TEX / "table_ablations.tex",
        "Family E ablations of the deadline-aware guard family.",
        "tab:ablations",
        [
            ("condition", "Condition"),
            ("policy", "Policy"),
            ("safe_success_mean", "Safe success"),
            ("harmful_contact_mean", "Harmful"),
            ("late_switch_mean", "Late"),
            ("expected_cost_mean", "Cost"),
        ],
        sorted(e, key=lambda r: (r["condition"], sf(r["expected_cost_mean"]))),
    )


def make_plots() -> int:
    failures = 0
    try:
        rows = [r for r in read_csv(RESULTS / "family_a_summary_by_latency.csv") if r["condition"] == "normal"]
        policies = ["contact_reactive", "posterior_tuned", "v2_guard", "deadline_threshold", "risk_guard", "calibrated_deadline_guard", "oracle_precontact"]
        plt.figure(figsize=(7.1, 4.1))
        for policy in policies:
            sub = sorted([r for r in rows if r["policy"] == policy], key=lambda r: sf(r["switch_latency"]))
            plt.plot([sf(r["switch_latency"]) for r in sub], [sf(r["safe_success_mean"]) for r in sub], marker="o", linewidth=2, label=policy.replace("_", " "))
        plt.xlabel("strategy switching latency (s)")
        plt.ylabel("safe success rate")
        plt.ylim(0, 1.04)
        plt.grid(True, alpha=0.25)
        plt.legend(fontsize=7, ncol=2)
        plt.tight_layout()
        plt.savefig(FIGURES / "safe_success_vs_latency.pdf")
        plt.savefig(FIGURES / "safe_success_vs_latency.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_a.txt").write_text(repr(exc), encoding="utf-8")
    try:
        rows = [r for r in read_csv(RESULTS / "family_a_summary_by_latency.csv") if r["condition"] == "normal"]
        policies = ["contact_reactive", "posterior_tuned", "deadline_threshold", "risk_guard", "calibrated_deadline_guard"]
        plt.figure(figsize=(7.1, 4.1))
        for policy in policies:
            sub = sorted([r for r in rows if r["policy"] == policy], key=lambda r: sf(r["switch_latency"]))
            plt.plot([sf(r["switch_latency"]) for r in sub], [sf(r["impulse_p90"]) for r in sub], marker="s", linewidth=2, label=policy.replace("_", " "))
        plt.xlabel("strategy switching latency (s)")
        plt.ylabel("p90 first-contact impulse")
        plt.grid(True, alpha=0.25)
        plt.legend(fontsize=7, ncol=2)
        plt.tight_layout()
        plt.savefig(FIGURES / "p90_impulse_vs_latency.pdf")
        plt.savefig(FIGURES / "p90_impulse_vs_latency.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_b.txt").write_text(repr(exc), encoding="utf-8")
    try:
        rows = [r for r in read_csv(RESULTS / "family_b_summary_by_policy.csv") if r["policy"] != "oracle_precontact"]
        names = [r["policy"].replace("_", " ") for r in sorted(rows, key=lambda r: sf(r["expected_cost_mean"]))]
        vals = [sf(r["expected_cost_mean"]) for r in sorted(rows, key=lambda r: sf(r["expected_cost_mean"]))]
        plt.figure(figsize=(7.1, 4.0))
        plt.bar(np.arange(len(vals)), vals, color="#4c78a8")
        plt.xticks(np.arange(len(vals)), names, rotation=20, ha="right")
        plt.ylabel("mean expected first-contact cost")
        plt.tight_layout()
        plt.savefig(FIGURES / "cost_asymmetry_policy_cost.pdf")
        plt.savefig(FIGURES / "cost_asymmetry_policy_cost.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_c.txt").write_text(repr(exc), encoding="utf-8")
    try:
        rows = read_csv(RESULTS / "family_c_summary_by_shift.csv")
        shifts = sorted({r["condition"] for r in rows})
        policies = ["source_tuned_posterior", "calibrated_posterior", "risk_guard", "calibrated_deadline_guard"]
        x = np.arange(len(shifts))
        width = 0.18
        plt.figure(figsize=(8.4, 4.2))
        for i, policy in enumerate(policies):
            vals = []
            for shift in shifts:
                match = [r for r in rows if r["condition"] == shift and r["policy"] == policy]
                vals.append(sf(match[0]["safe_success_mean"]) if match else 0.0)
            plt.bar(x + (i - 1.5) * width, vals, width=width, label=policy.replace("_", " "))
        plt.xticks(x, [s.replace("_", " ") for s in shifts], rotation=15, ha="right")
        plt.ylabel("safe success rate")
        plt.ylim(0, 1.04)
        plt.legend(fontsize=7, ncol=2)
        plt.tight_layout()
        plt.savefig(FIGURES / "shift_robustness.pdf")
        plt.savefig(FIGURES / "shift_robustness.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_d.txt").write_text(repr(exc), encoding="utf-8")
    try:
        rows = read_csv(RESULTS / "family_e_summary_by_ablation.csv")
        normal = [r for r in rows if r["condition"] == "normal"]
        normal = sorted(normal, key=lambda r: sf(r["expected_cost_mean"]))
        plt.figure(figsize=(8.0, 4.1))
        plt.bar(np.arange(len(normal)), [sf(r["expected_cost_mean"]) for r in normal], color="#6f8f4e")
        plt.xticks(np.arange(len(normal)), [r["policy"].replace("_", " ") for r in normal], rotation=20, ha="right")
        plt.ylabel("mean expected first-contact cost")
        plt.tight_layout()
        plt.savefig(FIGURES / "ablation_cost_normal.pdf")
        plt.savefig(FIGURES / "ablation_cost_normal.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_e.txt").write_text(repr(exc), encoding="utf-8")
    try:
        rows = [r for r in read_csv(RESULTS / "family_a_summary_by_condition_policy.csv") if r["policy"] not in {"fixed_nominal", "oracle_precontact"}]
        plt.figure(figsize=(6.2, 4.6))
        for r in rows:
            plt.scatter(sf(r["early_false_switch_mean"]), sf(r["harmful_contact_mean"]), s=26)
        plt.xlabel("early false-switch rate")
        plt.ylabel("harmful first-contact rate")
        plt.grid(True, alpha=0.25)
        plt.tight_layout()
        plt.savefig(FIGURES / "frontier_harmful_vs_early_false.pdf")
        plt.savefig(FIGURES / "frontier_harmful_vs_early_false.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_f.txt").write_text(repr(exc), encoding="utf-8")
    return failures


def write_claim_evidence_table() -> None:
    a = read_csv(RESULTS / "family_a_summary_by_condition_policy.csv")
    normal = {r["policy"]: r for r in a if r["condition"] == "normal"}
    b = {r["policy"]: r for r in read_csv(RESULTS / "family_b_summary_by_policy.csv")}
    c = read_csv(RESULTS / "family_c_summary_by_shift.csv")
    d = read_csv(RESULTS / "family_d_summary_by_scenario.csv")
    e = read_csv(RESULTS / "family_e_summary_by_ablation.csv")
    uninformative_cal = next(r for r in a if r["condition"] == "uninformative_until_contact" and r["policy"] == "calibrated_deadline_guard")
    zero_cal = next(r for r in d if r["special"] == "zero_latency" and r["policy"] == "calibrated_deadline_guard")
    normal_risk_e = next(r for r in e if r["condition"] == "normal" and r["policy"] == "risk_guard")
    normal_cal_e = next(r for r in e if r["condition"] == "normal" and r["policy"] == "calibrated_deadline_guard")
    no_deadline_e = next(r for r in e if r["condition"] == "normal" and r["policy"] == "risk_no_deadline")
    shift_source = next(r for r in c if r["condition"] == "onset_late_shift" and r["policy"] == "source_tuned_posterior")
    shift_cal = next(r for r in c if r["condition"] == "onset_late_shift" and r["policy"] == "calibrated_deadline_guard")
    rows = [
        {
            "claim": "Contact-reactive switching is too late under nonzero latency",
            "evidence": f"Normal contact-reactive safe success {sf(normal['contact_reactive']['safe_success_mean']):.3f} versus calibrated deadline guard {sf(normal['calibrated_deadline_guard']['safe_success_mean']):.3f}.",
            "status": "supported synthetic",
        },
        {
            "claim": "A tuned posterior baseline is strong and must be reported",
            "evidence": f"Normal tuned posterior safe success {sf(normal['posterior_tuned']['safe_success_mean']):.3f}; v2 guard {sf(normal['v2_guard']['safe_success_mean']):.3f}.",
            "status": "reported boundary",
        },
        {
            "claim": "Calibrated deadline guards improve cost-sensitive operation",
            "evidence": f"Family B calibrated deadline guard mean cost {sf(b['calibrated_deadline_guard']['expected_cost_mean']):.3f} versus fixed posterior {sf(b['posterior_fixed']['expected_cost_mean']):.3f}; risk guard is worse at {sf(b['risk_guard']['expected_cost_mean']):.3f}.",
            "status": "supported synthetic",
        },
        {
            "claim": "Calibration/shift matters separately from deadline feasibility",
            "evidence": f"Onset-late shift source posterior safe success {sf(shift_source['safe_success_mean']):.3f}; calibrated deadline guard {sf(shift_cal['safe_success_mean']):.3f}.",
            "status": "supported synthetic",
        },
        {
            "claim": "Benefit disappears when precontact evidence is absent",
            "evidence": f"Uninformative-until-contact calibrated deadline guard safe success {sf(uninformative_cal['safe_success_mean']):.3f}.",
            "status": "negative control",
        },
        {
            "claim": "Naive risk extension underperforms",
            "evidence": f"Normal risk guard cost {sf(normal_risk_e['expected_cost_mean']):.3f}; no-deadline ablation {sf(no_deadline_e['expected_cost_mean']):.3f}; calibrated deadline guard {sf(normal_cal_e['expected_cost_mean']):.3f}.",
            "status": "negative method result",
        },
        {
            "claim": "Zero latency removes the physical lateness mechanism",
            "evidence": f"Zero-latency calibrated deadline guard deadline violation {sf(zero_cal['deadline_violation_mean']):.3f}.",
            "status": "sanity check",
        },
    ]
    write_csv(RESULTS / "claim_evidence.csv", rows)
    write_table(
        TEX / "table_claim_evidence.tex",
        "Claim-to-evidence map for the full-scale v3 synthetic suite.",
        "tab:claim-evidence",
        [("claim", "Claim"), ("evidence", "Evidence"), ("status", "Status")],
        rows,
    )


def write_runtime_table(family_results: list[dict[str, Any]], plot_failures: int) -> None:
    rows = [
        {
            "family": r["family"],
            "rows": int(r["rows"]),
            "cases": int(r["cases"]),
            "seconds": round(float(r["seconds"]), 3),
        }
        for r in family_results
    ]
    rows.append({"family": "plots", "rows": 0, "cases": 0, "seconds": plot_failures})
    write_csv(RESULTS / "runtime_summary.csv", rows)
    write_table(
        TEX / "table_runtime_memory.tex",
        "Runtime and artifact scale for the RAM-light full-scale runner. Rows are streamed family by family to CSV while summaries are aggregated by compact groups.",
        "tab:runtime-memory",
        [("family", "Family"), ("rows", "Rows"), ("cases", "Cases"), ("seconds", "Seconds")],
        rows,
        digits=2,
    )


def write_evidence_summary(metadata: dict[str, Any]) -> None:
    a = {r["policy"]: r for r in read_csv(RESULTS / "family_a_summary_by_condition_policy.csv") if r["condition"] == "normal"}
    b = {r["policy"]: r for r in read_csv(RESULTS / "family_b_summary_by_policy.csv")}
    c_late = {r["policy"]: r for r in read_csv(RESULTS / "family_c_summary_by_shift.csv") if r["condition"] == "onset_late_shift"}
    d = read_csv(RESULTS / "family_d_summary_by_scenario.csv")
    zero = next(r for r in d if r["special"] == "zero_latency" and r["policy"] == "calibrated_deadline_guard")
    uninf = next(r for r in read_csv(RESULTS / "family_a_summary_by_condition_policy.csv") if r["condition"] == "uninformative_until_contact" and r["policy"] == "calibrated_deadline_guard")
    e = {r["policy"]: r for r in read_csv(RESULTS / "family_e_summary_by_ablation.csv") if r["condition"] == "normal"}
    lines = [
        "# Full-Scale Evidence Summary",
        "",
        f"- Stage: {metadata['stage']}",
        f"- Seed: {metadata['seed']}",
        f"- Total rows: {metadata['total_rows']}",
        f"- Total cases: {metadata['total_cases']}",
        f"- Plot failures: {metadata['plot_failures']}",
        "",
        "## Headline Numbers",
        "",
        f"- Family A normal contact-reactive safe success: {sf(a['contact_reactive']['safe_success_mean']):.3f}.",
        f"- Family A normal tuned-posterior safe success: {sf(a['posterior_tuned']['safe_success_mean']):.3f}.",
        f"- Family A normal v2-guard safe success: {sf(a['v2_guard']['safe_success_mean']):.3f}.",
        f"- Family A normal risk-guard safe success: {sf(a['risk_guard']['safe_success_mean']):.3f}.",
        f"- Family A normal calibrated deadline-guard safe success: {sf(a['calibrated_deadline_guard']['safe_success_mean']):.3f}.",
        f"- Family B cost-asymmetry calibrated deadline-guard mean expected cost: {sf(b['calibrated_deadline_guard']['expected_cost_mean']):.3f}; fixed posterior mean cost: {sf(b['posterior_fixed']['expected_cost_mean']):.3f}; risk guard mean cost: {sf(b['risk_guard']['expected_cost_mean']):.3f}.",
        f"- Family C onset-late-shift source-tuned posterior safe success: {sf(c_late['source_tuned_posterior']['safe_success_mean']):.3f}; calibrated deadline guard: {sf(c_late['calibrated_deadline_guard']['safe_success_mean']):.3f}.",
        f"- Family D zero-latency calibrated deadline-guard deadline violation: {sf(zero['deadline_violation_mean']):.3f}.",
        f"- Family A uninformative-until-contact calibrated deadline-guard safe success: {sf(uninf['safe_success_mean']):.3f}.",
        f"- Family E normal risk-guard cost: {sf(e['risk_guard']['expected_cost_mean']):.3f}; no-deadline ablation cost: {sf(e['risk_no_deadline']['expected_cost_mean']):.3f}.",
        "",
        "## Scope",
        "",
        "These results support a synthetic mechanism claim about activation deadlines, first-contact safety accounting, and cost-sensitive precontact switching. They do not establish real-robot performance or universal dominance over all learned/tuned policies.",
    ]
    (DOCS / "evidence_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    family_status: dict[str, str] = {}
    family_results: list[dict[str, Any]] = []
    total_rows = 0
    total_cases = 0
    start = time.perf_counter()
    write_progress("running", family_status, total_rows, total_cases)
    for name, fn in [
        ("A", family_a_main),
        ("B", family_b_cost),
        ("C", family_c_shift),
        ("D", family_d_negative),
        ("E", family_e_ablations),
    ]:
        result = fn()
        family_results.append(result)
        family_status[name] = "complete"
        total_rows += int(result["rows"])
        total_cases += int(result["cases"])
        write_progress("running", family_status, total_rows, total_cases)
        print(json.dumps(result, sort_keys=True), flush=True)
    make_tables()
    plot_failures = make_plots()
    write_claim_evidence_table()
    write_runtime_table(family_results, plot_failures)
    metadata = {
        "stage": "complete",
        "seed": SEED,
        "total_rows": total_rows,
        "total_cases": total_cases,
        "plot_failures": plot_failures,
        "families": family_results,
        "elapsed_seconds": time.perf_counter() - start,
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "matplotlib": getattr(plt.matplotlib, "__version__", "unknown"),
        "outputs": sorted(str(p.relative_to(ROOT)) for p in RESULTS.rglob("*") if p.is_file()),
    }
    (RESULTS / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8")
    write_progress("complete", family_status, total_rows, total_cases, plot_failures)
    write_evidence_summary(metadata)
    print(json.dumps(metadata, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        ensure_dirs()
        payload = {"stage": "fatal", "error": repr(exc)}
        (RESULTS / "progress.json").write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        print(json.dumps(payload, indent=2, sort_keys=True))
        raise
