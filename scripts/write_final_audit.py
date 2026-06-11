from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"
PAPER = ROOT / "paper"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/21.pdf")
DESKTOP_PDF = Path("C:/Users/wangz/OneDrive/Desktop/21.pdf")


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}


def git_url() -> str:
    env_url = os.environ.get("GITHUB_URL", "").strip()
    if env_url:
        return env_url
    try:
        proc = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            url = proc.stdout.strip()
            if url.startswith("git@github.com:"):
                url = "https://github.com/" + url.split(":", 1)[1]
            if url.endswith(".git"):
                url = url[:-4]
            return url
    except Exception:
        pass
    return "GitHub push failed or remote URL unavailable"


def main() -> int:
    stats = read_json(DOCS / "literature_stats.json")
    exp = read_json(RESULTS / "experiment_summary.json")
    build = read_json(PAPER / "build_status.json")
    template = read_json(PAPER / "template_status.json")
    gh = git_url()
    desktop_status = "pending orchestrator copy"
    if os.environ.get("ORCHESTRATOR_COPIED_DESKTOP", "").strip().lower() in {"1", "true", "yes"}:
        desktop_status = "orchestrator copy reported complete"
    lines = [
        "# Final Audit",
        "",
        "1. Chosen thesis: Precontact cues should be used as latency-aware hybrid-control guards for switching grasp strategy before first contact, not merely as perception features.",
        "2. Field assumption broken: first contact is an acceptable decision boundary and post-contact tactile correction can arrive early enough to change the safe strategy.",
        "3. New central mechanism: a precontact guard contract whose threshold depends on cue posterior, posterior margin, remaining distance, approach speed, switch latency, and asymmetric early/late switching costs.",
        "4. Genuine novelty: pre-touch/proximity sensing, tactile feedback, and contact control are not claimed as new; the novelty boundary is placing the discrete strategy guard before first contact and making physical activation deadline part of the decision rule.",
        "5. Closest hostile prior work: the 100-paper hostile set in `docs/hostile_prior_work.md`, especially pre-touch/proximity sensing, tactile reactive grasping, and hybrid contact-control papers that already cover the ingredients but not the latency-aware guard contract.",
        f"6. Literature coverage: {stats.get('matrix_rows', 'unknown')} matrix entries, {stats.get('serious_skim_rows', 'unknown')} serious-skim entries, {stats.get('deep_read_rows', 'unknown')} deep-read entries, {stats.get('hostile_rows', 'unknown')} hostile entries; target 1000 met: {stats.get('target_1000_met', 'unknown')}.",
        "7. Proof/formal-claim status: one activation-deadline proposition is proved under constant approach speed and fixed switch latency; it is a timing lemma, not a general optimal-control theorem.",
        f"8. Strongest evidence: runnable simulation with {exp.get('episodes', 'unknown')} episodes; normal-cue guard safe success {exp.get('normal_guard_safe_success', 'unknown')} versus contact-reactive {exp.get('normal_contact_safe_success', 'unknown')} and posterior-only {exp.get('normal_posterior_safe_success', 'unknown')}; harmful contact guard {exp.get('normal_guard_harmful_rate', 'unknown')} versus contact-reactive {exp.get('normal_contact_harmful_rate', 'unknown')}.",
        "9. Biggest weaknesses: no real robot experiment, synthetic cue/contact model, metadata/abstract-based literature extraction for many papers, and a deliberately simple formal result.",
        "10. Paper-readiness judgment: workshop. The mechanism is crisp and runnable, but real hardware evidence is needed before a strong ICLR submission.",
        f"11. Exact Downloads PDF path: {DOWNLOADS_PDF}; exists: {DOWNLOADS_PDF.exists()}; build stage: {build.get('stage', 'unknown')}; template status: {template.get('status', 'unknown')}.",
        f"12. GitHub URL: {gh}.",
        f"13. Desktop copy status: {desktop_status}; current Desktop path exists: {DESKTOP_PDF.exists()}.",
        "",
        "## Build Notes",
        "",
        f"- Build copied to Downloads: {build.get('copied_to_downloads', 'unknown')}.",
        f"- Intermediate paper PDF removed: {build.get('removed_intermediate_pdf', 'unknown')}.",
        f"- ICLR template source status: {template.get('status', 'unknown')}.",
    ]
    (DOCS / "final_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"final_audit": str(DOCS / "final_audit.md"), "github_url": gh}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        (DOCS / "final_audit_error.txt").write_text(repr(exc), encoding="utf-8")
        print(json.dumps({"error": repr(exc)}, indent=2))
        raise SystemExit(0)
