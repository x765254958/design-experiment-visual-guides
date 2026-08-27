#!/usr/bin/env python3
"""Create a minimal experiment-design workspace from the bundled example spec."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    root = args.out.resolve() / args.name
    if root.exists() and any(root.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty directory: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for child in ("visual-prompts", "figures", "raw-records"):
        (root / child).mkdir(exist_ok=True)

    example = Path(__file__).resolve().parent.parent / "assets" / "experiment-spec.example.json"
    spec = json.loads(example.read_text(encoding="utf-8"))
    spec["project"]["name"] = args.name
    (root / "experiment_spec.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (root / "source-matrix.md").write_text(
        "# Source matrix\n\n| Parameter | Value | Status | Source | Notes |\n"
        "|---|---|---|---|---|\n", encoding="utf-8"
    )
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

