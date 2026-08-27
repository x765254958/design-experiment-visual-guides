#!/usr/bin/env python3
"""Validate structural and scientific traceability fields in experiment_spec.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ALLOWED_STATUS = {"confirmed", "literature", "provisional", "unknown"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    args = parser.parse_args()
    data = json.loads(args.spec.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []

    for key in ("project", "governance", "materials", "dose_basis", "groups", "assays", "schedule"):
        if key not in data:
            errors.append(f"missing top-level field: {key}")

    project = data.get("project", {})
    for key in ("name", "question", "phase"):
        if not project.get(key):
            errors.append(f"project.{key} is required")

    governance = data.get("governance", {})
    if governance.get("local_sop_required") and not governance.get("training_confirmed"):
        warnings.append("local SOP/training confirmation is still required")

    group_ids: set[str] = set()
    for i, group in enumerate(data.get("groups", [])):
        gid = group.get("id")
        if not gid:
            errors.append(f"groups[{i}].id is required")
        elif gid in group_ids:
            errors.append(f"duplicate group id: {gid}")
        group_ids.add(gid)
        if not group.get("role") or not group.get("treatment"):
            errors.append(f"group {gid or i} requires role and treatment")
        if "concentration" in group and not group.get("unit"):
            errors.append(f"group {gid or i} has concentration without unit")

    dose = data.get("dose_basis", {})
    if dose.get("status") not in ALLOWED_STATUS:
        errors.append("dose_basis.status must be confirmed/literature/provisional/unknown")
    if not dose.get("basis") or not dose.get("unit"):
        errors.append("dose_basis requires basis and unit")

    for i, day in enumerate(data.get("schedule", [])):
        if not day.get("day") or not day.get("objective") or not day.get("tasks"):
            errors.append(f"schedule[{i}] requires day, objective, and tasks")

    for item in data.get("unknowns", []):
        warnings.append(f"unresolved: {item}")

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARNING: {msg}")
    if not errors:
        print(f"OK: {args.spec}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

