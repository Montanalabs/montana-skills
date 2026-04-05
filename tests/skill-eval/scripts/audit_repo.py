#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EVAL_SCRIPT = ROOT / "tests" / "skill-eval" / "scripts" / "evaluate_skills.py"
REPORT_PATH = ROOT / "tests" / "skill-eval" / "reports" / "skill-evaluation.json"


def main() -> int:
    subprocess.run([sys.executable, str(EVAL_SCRIPT)], cwd=ROOT, check=True)

    report = json.loads(REPORT_PATH.read_text())
    failures: list[str] = []

    for skill in report["skills"]:
        if skill["score"] != skill["max_score"]:
            failures.append(
                f"Skill {skill['name']} scored {skill['score']}/{skill['max_score']}: "
                + "; ".join(skill["findings"])
            )

    for case in report["cases"]:
        if case["score"] != case["max_score"]:
            failures.append(
                f"Case {case['name']} scored {case['score']}/{case['max_score']}: "
                + "; ".join(case["findings"])
            )

    if report["doc_findings"]:
        failures.extend(report["doc_findings"])

    if failures:
        print("Montana skill repo audit failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Montana skill repo audit passed: "
        f"{len(report['skills'])} skills, {len(report['cases'])} cases, "
        "no report findings."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
