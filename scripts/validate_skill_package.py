#!/usr/bin/env python3
"""Self-contained validation used by local checks and GitHub Actions."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
    skill_file = root / "SKILL.md"
    if not skill_file.exists():
        fail("SKILL.md is missing")
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is invalid")
    metadata = yaml.safe_load(match.group(1))
    if set(metadata) != {"name", "description"}:
        fail("frontmatter must contain only name and description")
    name = metadata["name"]
    if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
        fail("skill name must be lowercase hyphen-case and under 64 characters")
    if root.name != name:
        fail("folder name and skill name differ")
    if not metadata["description"].strip():
        fail("description is empty")

    agent_file = root / "agents" / "openai.yaml"
    agent = yaml.safe_load(agent_file.read_text(encoding="utf-8"))
    interface = agent.get("interface", {})
    prompt = interface.get("default_prompt", "")
    if f"${name}" not in prompt:
        fail("default_prompt must mention the skill explicitly")

    required_files = (
        "references/intake.md",
        "references/protocol-design.md",
        "references/safety-governance.md",
        "references/visual-guides.md",
        "assets/experiment-spec.example.json",
        "scripts/init_experiment_project.py",
        "scripts/validate_experiment_spec.py",
        "scripts/build_visual_prompt.py",
    )
    for required in required_files:
        if not (root / required).exists():
            fail(f"missing required resource: {required}")
    print(f"OK: {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

