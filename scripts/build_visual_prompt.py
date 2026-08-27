#!/usr/bin/env python3
"""Build one layout prompt and one operation prompt for each scheduled day."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def lines(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values) or "- none specified"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.spec.read_text(encoding="utf-8"))
    args.out.mkdir(parents=True, exist_ok=True)

    groups = [
        f"{g['id']}: {g.get('treatment', '')}; role={g.get('role', '')}; "
        f"dose={g.get('concentration', '')} {g.get('unit', '')}".strip()
        for g in data.get("groups", [])
    ]

    for day in data.get("schedule", []):
        label = day["day"]
        common = (
            f"Project: {data['project']['name']}\n"
            f"Day: {label}\nObjective: {day['objective']}\n"
            f"Groups:\n{lines(groups)}\n"
            f"Key parameters:\n{lines(day.get('key_parameters', []))}\n"
            f"Warnings:\n{lines(day.get('warnings', []))}\n"
            "Constraint: label provisional conditions as reference/pilot; laboratory SOP prevails.\n"
        )
        layout = (
            "Create a precise scientific layout figure. Use deterministic labels, consistent group colors, "
            "and show only positions or timing specified in the experiment specification.\n" + common
        )
        operation = (
            "Create a 3:2 landscape beginner laboratory operation infographic with a title, numbered steps, "
            "central illustrated sequence, key-parameter panel, calculation/preparation panel, and warnings.\n"
            f"Actions:\n{lines(day.get('tasks', []))}\n" + common
        )
        (args.out / f"{label}-layout.txt").write_text(layout, encoding="utf-8")
        (args.out / f"{label}-operation.txt").write_text(operation, encoding="utf-8")
    print(f"Wrote prompts to {args.out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

