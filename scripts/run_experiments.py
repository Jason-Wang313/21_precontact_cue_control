from __future__ import annotations

import csv
import json
import math
import statistics
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
DOCS = ROOT / "docs"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)
DOCS.mkdir(exist_ok=True)

EPISODES_PATH = RESULTS / "episode_results.csv"
SUMMARY_PATH = RESULTS / "summary.csv"
ABLATION_PATH = RESULTS / "ablation_summary.csv"
STATUS_PATH = RESULTS / "experiment_status.json"


CLASSES = ["nominal", "thin_lip", "slippery", "fragile"]
REQUIRED = {
    "nominal": "pinch",
    "thin_lip": "scoop",
    "slippery": "cage",
    "fragile": "soft",
}
PROTOTYPES = np.array(
    [
        [0.38, 0.16, 0.08],
        [1.15, -0.28, 0.18],
        [0.10, 1.05, -0.25],
        [-0.22, 0.18, 1.12],
    ],
    dtype=float,
)
BASE_ONSETS = {
    "nominal": 0.024,
    "thin_lip": 0.052,
    "slippery": 0.043,
    "fragile": 0.047,
}
IMPULSE_THRESHOLDS = {
    "nominal": 0.62,
    "thin_lip": 0.55,
    "slippery": 0.50,
    "fragile": 0.38,
}
POLICIES = ["fixed_nominal", "contact_reactive", "posterior_only", "guard_contract", "oracle_precontact"]


def write_status(stage: str, **extra: Any) -> None:
    STATUS_PATH.write_text(json.dumps({"stage": stage, **extra}, indent=2, sort_keys=True), encoding="utf-8")


def softmax(logp: np.ndarray) -> np.ndarray:
    z = logp - np.max(logp)
    e = np.exp(z)
    return e / np.sum(e)


def cue_amplitude(cls: str, distance: float, condition: str) -> float:
    onset = BASE_ONSETS[cls]
    if condition == "late_cue":
        onset = min(onset, 0.006)
    elif condition == "weak_cue":
        onset *= 0.65
    if distance > onset:
        return 0.0
    x = max(0.0, 1.0 - distance / max(onset, 1e-6))
    if condition == "weak_cue":
        x *= 0.58
    return x


def observe(cls_idx: int, distance: float, condition: str, noise: float, rng: np.random.Generator) -> np.ndarray:
    cls = CLASSES[cls_idx]
    amp = cue_amplitude(cls, distance, condition)
    return PROTOTYPES[cls_idx] * amp + rng.normal(0.0, noise, size=3)


def log_likelihood(obs: np.ndarray, distance: float, condition: str, noise: float) -> np.ndarray:
    sigma2 = max(noise * noise, 1e-6)
    out = np.zeros(len(CLASSES), dtype=float)
    for idx, cls in enumerate(CLASSES):
        pred = PROTOTYPES[idx] * cue_amplitude(cls, distance, condition)
        out[idx] = -0.5 * float(np.sum((obs - pred) ** 2) / sigma2)
    return out


def posterior_threshold(distance: float, start_distance: float, switch_distance: float) -> float:
    if distance < switch_distance:
        return 1.01
    far_fraction = min(1.0, max(0.0, distance / start_distance))
    return 0.68 + 0.24 * far_fraction


def mismatch_impulse(cls: str, active_strategy: str, velocity: float, latency: float, rng: np.random.Generator) -> float:
    required = REQUIRED[cls]
    if active_strategy == required:
        base = 0.12 + 0.35 * velocity + 0.02 * rng.normal()
        return max(0.0, base)
    severity = {
        "nominal": 0.55,
        "thin_lip": 0.82,
        "slippery": 0.74,
        "fragile": 1.05,
    }[cls]
    strategy_penalty = {
        "pinch": 0.18,
        "scoop": 0.12,
        "cage": 0.10,
        "soft": 0.08,
    }.get(active_strategy, 0.15)
    return max(0.0, severity + strategy_penalty + 1.6 * velocity + 1.8 * latency + 0.08 * rng.normal())


def final_success_probability(policy: str, cls: str, active_strategy: str, impulse: float, latency: float) -> float:
    required = REQUIRED[cls]
    if active_strategy == required:
        return max(0.0, min(0.99, 0.96 - 0.18 * max(0.0, impulse - IMPULSE_THRESHOLDS[cls])))
    if policy == "contact_reactive":
        return max(0.02, 0.55 - 1.8 * latency - 0.28 * max(0.0, impulse - IMPULSE_THRESHOLDS[cls]))
    return max(0.01, 0.22 - 0.20 * max(0.0, impulse - IMPULSE_THRESHOLDS[cls]))


def run_episode(
    policy: str,
    cls_idx: int,
    velocity: float,
    switch_latency: float,
    condition: str,
    noise: float,
    rng: np.random.Generator,
) -> dict[str, Any]:
    cls = CLASSES[cls_idx]
    required_strategy = REQUIRED[cls]
    start_distance = 0.060
    step_distance = 0.002
    switch_distance = velocity * switch_latency
    distances = np.arange(start_distance, -1e-9, -step_distance)
    logp = np.zeros(len(CLASSES), dtype=float) - math.log(len(CLASSES))
    switch_started_distance: float | None = None
    switch_target = "pinch"
    predicted_class = "nominal"
    posterior_conf = 0.25
    posterior_margin = 0.0
    early_false_switch = 0
    guard_streak = 0
    guard_last_target = ""

    if policy == "oracle_precontact":
        switch_started_distance = start_distance
        switch_target = required_strategy
        predicted_class = cls
        posterior_conf = 1.0
        posterior_margin = 1.0
    elif policy in {"posterior_only", "guard_contract"}:
        for d in distances:
            obs = observe(cls_idx, float(d), condition, noise, rng)
            logp += log_likelihood(obs, float(d), condition, noise)
            post = softmax(logp)
            order = np.argsort(post)[::-1]
            best = int(order[0])
            second = int(order[1])
            predicted_class = CLASSES[best]
            posterior_conf = float(post[best])
            posterior_margin = float(post[best] - post[second])
            target = REQUIRED[predicted_class]
            if target == "pinch" or switch_started_distance is not None:
                if target == "pinch":
                    guard_streak = 0
                    guard_last_target = ""
                continue
            if policy == "posterior_only":
                if posterior_conf >= 0.92 and posterior_margin >= 0.32:
                    switch_started_distance = float(d)
                    switch_target = target
                    break
            else:
                theta = posterior_threshold(float(d), start_distance, switch_distance)
                deadline_window = max(0.0, float(d) - switch_distance)
                urgency_margin = 0.22 if deadline_window < 0.010 else 0.28
                if posterior_conf >= theta and posterior_margin >= urgency_margin and float(d) >= switch_distance:
                    if target == guard_last_target:
                        guard_streak += 1
                    else:
                        guard_last_target = target
                        guard_streak = 1
                    if guard_streak >= 2:
                        switch_started_distance = float(d)
                        switch_target = target
                        break
                else:
                    guard_streak = 0
                    guard_last_target = ""

    if policy == "contact_reactive":
        predicted_class = cls
        posterior_conf = 1.0
        posterior_margin = 1.0
        if switch_latency <= 1e-9:
            active_strategy = required_strategy
            switch_started_distance = 0.0
            switch_target = required_strategy
        else:
            active_strategy = "pinch"
            switch_target = required_strategy
            switch_started_distance = 0.0
    elif policy == "fixed_nominal":
        active_strategy = "pinch"
        switch_target = "pinch"
    else:
        if switch_started_distance is not None and switch_started_distance + 1e-12 >= switch_distance:
            active_strategy = switch_target
        else:
            active_strategy = "pinch"

    if policy == "oracle_precontact" and switch_latency > 0 and start_distance < switch_distance:
        active_strategy = "pinch"

    if active_strategy != required_strategy and switch_target != "pinch" and switch_target != required_strategy:
        early_false_switch = 1
    if active_strategy != required_strategy and switch_target != "pinch" and switch_started_distance is not None and switch_started_distance >= switch_distance:
        early_false_switch = 1

    impulse = mismatch_impulse(cls, active_strategy, velocity, switch_latency, rng)
    harmful_contact = int(impulse > IMPULSE_THRESHOLDS[cls])
    safe_success = int(active_strategy == required_strategy and not harmful_contact)
    final_prob = final_success_probability(policy, cls, active_strategy, impulse, switch_latency)
    final_success = int(rng.random() < final_prob)
    late_switch = int(active_strategy != required_strategy and required_strategy != "pinch")
    if policy == "posterior_only" and switch_started_distance is not None and switch_started_distance < switch_distance:
        late_switch = 1
    if policy == "guard_contract" and switch_started_distance is None and required_strategy != "pinch":
        late_switch = 1
    regret = max(0.0, impulse - (0.12 + 0.35 * velocity))
    return {
        "policy": policy,
        "class": cls,
        "condition": condition,
        "velocity": velocity,
        "switch_latency": switch_latency,
        "switch_distance": switch_distance,
        "required_strategy": required_strategy,
        "active_strategy_at_contact": active_strategy,
        "predicted_class": predicted_class,
        "switch_started_distance": "" if switch_started_distance is None else round(switch_started_distance, 5),
        "posterior_confidence": round(posterior_conf, 4),
        "posterior_margin": round(posterior_margin, 4),
        "impulse": round(impulse, 5),
        "harmful_contact": harmful_contact,
        "safe_success": safe_success,
        "final_success": final_success,
        "late_switch": late_switch,
        "early_false_switch": early_false_switch,
        "regret": round(regret, 5),
    }


def aggregate(rows: list[dict[str, Any]], keys: list[str]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in rows:
        key = tuple(row[k] for k in keys)
        groups.setdefault(key, []).append(row)
    out: list[dict[str, Any]] = []
    for key, group in sorted(groups.items()):
        impulses = [float(r["impulse"]) for r in group]
        out.append(
            {
                **{keys[i]: key[i] for i in range(len(keys))},
                "episodes": len(group),
                "safe_success_rate": round(statistics.mean(int(r["safe_success"]) for r in group), 5),
                "final_success_rate": round(statistics.mean(int(r["final_success"]) for r in group), 5),
                "harmful_contact_rate": round(statistics.mean(int(r["harmful_contact"]) for r in group), 5),
                "late_switch_rate": round(statistics.mean(int(r["late_switch"]) for r in group), 5),
                "early_false_switch_rate": round(statistics.mean(int(r["early_false_switch"]) for r in group), 5),
                "mean_impulse": round(statistics.mean(impulses), 5),
                "p90_impulse": round(float(np.quantile(np.array(impulses), 0.9)), 5),
                "mean_regret": round(statistics.mean(float(r["regret"]) for r in group), 5),
            }
        )
    return out


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_figures(summary: list[dict[str, Any]], ablation: list[dict[str, Any]]) -> dict[str, str]:
    outputs: dict[str, str] = {}
    try:
        import matplotlib.pyplot as plt

        normal = [r for r in summary if r["condition"] == "normal"]
        policies = ["fixed_nominal", "contact_reactive", "posterior_only", "guard_contract", "oracle_precontact"]
        latencies = sorted({float(r["switch_latency"]) for r in normal})

        plt.figure(figsize=(6.2, 3.7))
        for policy in policies:
            ys = []
            for lat in latencies:
                vals = [float(r["safe_success_rate"]) for r in normal if r["policy"] == policy and abs(float(r["switch_latency"]) - lat) < 1e-9]
                ys.append(statistics.mean(vals) if vals else float("nan"))
            plt.plot(latencies, ys, marker="o", linewidth=2, label=policy.replace("_", " "))
        plt.xlabel("strategy switching latency (s)")
        plt.ylabel("safe success rate")
        plt.ylim(0, 1.02)
        plt.grid(True, alpha=0.25)
        plt.legend(fontsize=7, ncol=2)
        plt.tight_layout()
        path = FIGURES / "safe_success_by_latency.pdf"
        plt.savefig(path)
        outputs["safe_success_by_latency"] = str(path)
        plt.close()

        plt.figure(figsize=(6.2, 3.7))
        for policy in policies:
            ys = []
            for lat in latencies:
                vals = [float(r["p90_impulse"]) for r in normal if r["policy"] == policy and abs(float(r["switch_latency"]) - lat) < 1e-9]
                ys.append(statistics.mean(vals) if vals else float("nan"))
            plt.plot(latencies, ys, marker="s", linewidth=2, label=policy.replace("_", " "))
        plt.xlabel("strategy switching latency (s)")
        plt.ylabel("90th percentile first-contact impulse")
        plt.grid(True, alpha=0.25)
        plt.legend(fontsize=7, ncol=2)
        plt.tight_layout()
        path = FIGURES / "impulse_by_latency.pdf"
        plt.savefig(path)
        outputs["impulse_by_latency"] = str(path)
        plt.close()

        conditions = ["normal", "weak_cue", "late_cue"]
        x = np.arange(len(conditions))
        width = 0.18
        plt.figure(figsize=(6.2, 3.7))
        for pi, policy in enumerate(["contact_reactive", "posterior_only", "guard_contract", "oracle_precontact"]):
            ys = []
            for cond in conditions:
                vals = [float(r["safe_success_rate"]) for r in ablation if r["policy"] == policy and r["condition"] == cond]
                ys.append(statistics.mean(vals) if vals else 0.0)
            plt.bar(x + (pi - 1.5) * width, ys, width=width, label=policy.replace("_", " "))
        plt.xticks(x, [c.replace("_", " ") for c in conditions])
        plt.ylabel("safe success rate")
        plt.ylim(0, 1.02)
        plt.legend(fontsize=7, ncol=2)
        plt.tight_layout()
        path = FIGURES / "cue_ablation.pdf"
        plt.savefig(path)
        outputs["cue_ablation"] = str(path)
        plt.close()
    except Exception as exc:
        (FIGURES / "figure_error.txt").write_text(repr(exc), encoding="utf-8")
    return outputs


def main() -> int:
    rng = np.random.default_rng(21)
    rows: list[dict[str, Any]] = []
    velocities = [0.10, 0.18, 0.26]
    latencies = [0.00, 0.03, 0.06, 0.09, 0.12]
    conditions = ["normal", "weak_cue", "late_cue"]
    episodes_per_cell = 120
    total_cells = len(POLICIES) * len(velocities) * len(latencies) * len(conditions)
    done = 0
    for condition in conditions:
        noise = {"normal": 0.20, "weak_cue": 0.25, "late_cue": 0.20}[condition]
        for velocity in velocities:
            for latency in latencies:
                for policy in POLICIES:
                    done += 1
                    write_status("running", cell=done, total_cells=total_cells, policy=policy, velocity=velocity, latency=latency, condition=condition)
                    for _ in range(episodes_per_cell):
                        cls_idx = int(rng.integers(0, len(CLASSES)))
                        rows.append(run_episode(policy, cls_idx, velocity, latency, condition, noise, rng))
    write_csv(EPISODES_PATH, rows)
    summary = aggregate(rows, ["condition", "policy", "switch_latency"])
    write_csv(SUMMARY_PATH, summary)
    ablation = aggregate(rows, ["condition", "policy"])
    write_csv(ABLATION_PATH, ablation)
    figures = make_figures(summary, ablation)
    normal_guard = [r for r in ablation if r["condition"] == "normal" and r["policy"] == "guard_contract"][0]
    normal_contact = [r for r in ablation if r["condition"] == "normal" and r["policy"] == "contact_reactive"][0]
    normal_post = [r for r in ablation if r["condition"] == "normal" and r["policy"] == "posterior_only"][0]
    result = {
        "episodes": len(rows),
        "summary_path": str(SUMMARY_PATH),
        "ablation_path": str(ABLATION_PATH),
        "figures": figures,
        "normal_guard_safe_success": normal_guard["safe_success_rate"],
        "normal_contact_safe_success": normal_contact["safe_success_rate"],
        "normal_posterior_safe_success": normal_post["safe_success_rate"],
        "normal_guard_harmful_rate": normal_guard["harmful_contact_rate"],
        "normal_contact_harmful_rate": normal_contact["harmful_contact_rate"],
    }
    (RESULTS / "experiment_summary.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    write_status("done", **result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        write_status("fatal_caught", error=repr(exc))
        print(json.dumps({"error": repr(exc)}, indent=2))
        raise SystemExit(0)
