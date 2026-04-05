#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
SKILLS_DIR = ROOT / "skills"
EVAL_DIR = ROOT / "tests" / "skill-eval"
REPORTS_DIR = EVAL_DIR / "reports"
CASES_DIR = EVAL_DIR / "cases"
TRANSCRIPTS_DIR = EVAL_DIR / "transcripts" / "codex"

SECTION_HEADERS = [
    "## Category",
    "## Works with",
    "## Default workflow",
    "## Output format",
    "## Safety rules",
]

DOC_PATH_PATTERNS = [
    "package/skills/",
    "package/MANIFEST.json",
    "package/adapters/",
]


@dataclass
class SkillReport:
    name: str
    category: str | None
    score: int
    max_score: int
    passed_checks: list[str]
    findings: list[str]
    template_refs: list[str]
    missing_templates: list[str]
    works_with: list[str]
    manifest_composes_with: list[str]


@dataclass
class CaseReport:
    name: str
    score: int
    max_score: int
    findings: list[str]
    transcript_present: bool


def extract_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, Any] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key == "metadata":
            try:
                data[key] = json.loads(value)
            except json.JSONDecodeError:
                data[key] = value
        else:
            data[key] = value
    return data, body


def parse_bullet_block(body: str, header: str) -> list[str]:
    lines = body.splitlines()
    items: list[str] = []
    collecting = False
    for line in lines:
        if line.strip() == header:
            collecting = True
            continue
        if collecting and line.startswith("## "):
            break
        if collecting and line.strip().startswith("- "):
            items.append(line.strip()[2:].strip("`"))
    return items


def parse_template_refs(text: str) -> list[str]:
    return sorted(set(re.findall(r"\{baseDir\}/(templates/[A-Za-z0-9._/-]+)", text)))


def has_all_sections(body: str) -> list[str]:
    return [section for section in SECTION_HEADERS if section in body]


def load_manifest() -> dict[str, Any]:
    return json.loads((ROOT / "MANIFEST.json").read_text())


def skill_manifest_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {skill["name"]: skill for skill in manifest["skills"]}


def evaluate_skill(path: Path, manifest_map: dict[str, dict[str, Any]]) -> SkillReport:
    text = path.read_text()
    frontmatter, body = extract_frontmatter(text)
    name = frontmatter.get("name", path.parent.name)
    metadata = frontmatter.get("metadata", {})
    montana = metadata.get("montana", {}) if isinstance(metadata, dict) else {}
    category = montana.get("category")
    works_with = parse_bullet_block(body, "## Works with")
    template_refs = parse_template_refs(text)
    missing_templates = [
        ref for ref in template_refs if not (path.parent / ref).exists()
    ]
    present_sections = has_all_sections(body)
    manifest_entry = manifest_map.get(name, {})
    manifest_composes_with = manifest_entry.get("composes_with", [])

    findings: list[str] = []
    passed: list[str] = []
    score = 0
    max_score = 10

    if frontmatter.get("name") == name and frontmatter.get("description"):
        score += 2
        passed.append("Frontmatter contains name and description")
    else:
        findings.append("Missing or incomplete frontmatter fields")

    if len(present_sections) == len(SECTION_HEADERS):
        score += 2
        passed.append("Core sections are present")
    else:
        missing = sorted(set(SECTION_HEADERS) - set(present_sections))
        findings.append(f"Missing core sections: {', '.join(missing)}")

    if not missing_templates:
        score += 2
        passed.append("All referenced templates exist")
    else:
        findings.append(
            f"Missing template references: {', '.join(missing_templates)}"
        )

    if category and manifest_entry and manifest_entry.get("category") == category:
        score += 2
        passed.append("Manifest category matches skill metadata")
    else:
        findings.append("Manifest category does not match skill metadata")

    if sorted(works_with) == sorted(manifest_composes_with):
        score += 2
        passed.append("Works with list matches MANIFEST compose rules")
    else:
        findings.append("Works with list differs from MANIFEST compose rules")

    return SkillReport(
        name=name,
        category=category,
        score=score,
        max_score=max_score,
        passed_checks=passed,
        findings=findings,
        template_refs=template_refs,
        missing_templates=missing_templates,
        works_with=works_with,
        manifest_composes_with=manifest_composes_with,
    )


def evaluate_docs() -> list[str]:
    findings: list[str] = []
    docs = ["README.md", "SUPPORT_MATRIX.md", "CATEGORIES.md"]
    for doc in docs:
        text = (ROOT / doc).read_text()
        for pattern in DOC_PATH_PATTERNS:
            if pattern in text:
                candidate = pattern.rstrip("/")
                if not (ROOT / candidate).exists():
                    findings.append(
                        f"{doc} references `{pattern}` but that path does not exist in this repo"
                    )
    return findings


def evaluate_case(path: Path) -> CaseReport:
    text = path.read_text()
    name = path.stem
    required_headers = [
        "# Case:",
        "## Skill under test",
        "## Fixture",
        "## Prompt",
        "## Scoring rubric",
        "## Expected commands",
        "## Expected boundaries",
        "## Red flags",
        "## Transcript",
    ]

    findings: list[str] = []
    score = 0
    max_score = 4

    missing_headers = [header for header in required_headers if header not in text]
    if not missing_headers:
        score += 2
    else:
        findings.append(f"Missing rubric headers: {', '.join(missing_headers)}")

    if re.search(r"- `[^`]+`: [0-9]+ points", text):
        score += 1
    else:
        findings.append("Rubric does not contain point-scored criteria")

    transcript_present = (TRANSCRIPTS_DIR / f"{name}.md").exists()
    if transcript_present:
        score += 1
    else:
        findings.append("Missing Codex transcript for this case")

    return CaseReport(
        name=name,
        score=score,
        max_score=max_score,
        findings=findings,
        transcript_present=transcript_present,
    )


def write_reports(
    skill_reports: list[SkillReport],
    case_reports: list[CaseReport],
    doc_findings: list[str],
) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "repo_root": str(ROOT),
        "skills": [asdict(report) for report in skill_reports],
        "cases": [asdict(report) for report in case_reports],
        "doc_findings": doc_findings,
    }
    (REPORTS_DIR / "skill-evaluation.json").write_text(json.dumps(data, indent=2))

    lines: list[str] = []
    lines.append("# Skill Evaluation Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(
        f"- Evaluated {len(skill_reports)} skills with a static consistency rubric."
    )
    avg = sum(report.score for report in skill_reports) / max(len(skill_reports), 1)
    lines.append(f"- Average score: {avg:.1f}/10")
    case_avg = sum(report.score for report in case_reports) / max(len(case_reports), 1)
    lines.append(f"- Case rubric coverage score: {case_avg:.1f}/4")
    lines.append("")
    lines.append("## Skill Scores")
    lines.append("")
    for report in sorted(skill_reports, key=lambda item: (-item.score, item.name)):
        lines.append(
            f"- `{report.name}`: {report.score}/{report.max_score} ({report.category})"
        )
        for finding in report.findings:
            lines.append(f"  - Finding: {finding}")
    lines.append("")
    lines.append("## Case Coverage")
    lines.append("")
    for report in sorted(case_reports, key=lambda item: item.name):
        transcript = "yes" if report.transcript_present else "no"
        lines.append(
            f"- `{report.name}`: {report.score}/{report.max_score}; transcript present: {transcript}"
        )
        for finding in report.findings:
            lines.append(f"  - Finding: {finding}")
    lines.append("")
    lines.append("## Repo-Level Findings")
    lines.append("")
    if doc_findings:
        for finding in doc_findings:
            lines.append(f"- {finding}")
    else:
        lines.append("- No repo-level documentation path issues were detected.")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(
        "- This report measures internal consistency and reference accuracy, not live model behavior."
    )
    lines.append(
        "- Use the fixture repos, scored case rubrics, and saved transcripts under `tests/skill-eval/` for manual or agent-assisted scenario testing."
    )

    (REPORTS_DIR / "skill-evaluation.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    manifest = load_manifest()
    manifest_map = skill_manifest_map(manifest)
    skill_reports = [
        evaluate_skill(path, manifest_map)
        for path in sorted(SKILLS_DIR.glob("*/SKILL.md"))
    ]
    case_reports = [
        evaluate_case(path)
        for path in sorted(CASES_DIR.glob("*.md"))
    ]
    doc_findings = evaluate_docs()
    write_reports(skill_reports, case_reports, doc_findings)
    print(f"Wrote reports to {REPORTS_DIR}")


if __name__ == "__main__":
    main()
