# Design Experiment Visual Guides

[简体中文](README.md) | [English](README.en.md)

[![Validate skill](https://github.com/x765254958/design-experiment-visual-guides/actions/workflows/validate.yml/badge.svg)](https://github.com/x765254958/design-experiment-visual-guides/actions/workflows/validate.yml)

A Codex Skill for turning an experimental idea into a reviewed design, a beginner-friendly protocol, and day-by-day execution visuals.

The Skill does not immediately draw a workflow from an ambiguous request. It first checks the objective, groups, doses, timing, controls, replicates, and experimental dependencies. The written protocol, plate map, calculation tables, and D0/D1/D2 figures are then derived from the same frozen experiment specification to reduce contradictions between deliverables.

## What it does

- Organizes an experimental design around the research question and available laboratory conditions.
- Separates confirmed, literature-derived, provisional, and unresolved parameters.
- Designs groups, controls, concentration ranges, replicates, and experimental dependencies.
- Produces step-by-step manuals for beginner operators.
- Produces plate maps, grouping diagrams, timelines, and daily operation figures.
- Cross-checks group names, doses, volumes, units, timing, and batch pairing across files.
- Converts an existing SOP, paper method, or laboratory note into an executable experiment package.

The repository currently contains structured L929 CCK-8 and two-strain CFU plate-counting examples. They demonstrate the workflow and are not universal laboratory standards.

## Workflow

```text
Research objective and available conditions
                    ↓
Parameter classification and unresolved items
                    ↓
Groups, controls, doses, replicates, and dependencies
                    ↓
Freeze experiment_spec.json
                    ↓
Protocol / beginner manual / calculation tables
                    ↓
Plate maps and D0, D1, D2 operation figures
                    ↓
Cross-artifact consistency check
```

## Example outputs

The figures below illustrate the two complementary visual formats produced by the Skill: a deterministic plate layout and a day-specific operation guide. Their parameters belong only to the example project. A formal experiment should regenerate them from its approved `experiment_spec.json`.

### D0: plate layout and preparation

<p align="center">
  <img src="assets/style-reference/cck8-D0-layout.png" alt="L929 CCK-8 D0 plate layout" width="49%">
  <img src="assets/style-reference/cck8-D0-operation.png" alt="L929 CCK-8 D0 operation guide" width="49%">
</p>

### D1: material-treatment operation

<p align="center">
  <img src="assets/style-reference/cck8-D1-operation.png" alt="L929 CCK-8 D1 operation guide" width="82%">
</p>

## Output modes

| Mode | Deliverables |
| --- | --- |
| `design-only` | Research logic, groups, endpoints, dependencies, and unresolved questions |
| `protocol` | Experimental design, method, and recording requirements |
| `beginner-manual` | Day-by-day actions, calculations, checks, and raw-data templates |
| `visual-pack` | Plate maps, layouts, timelines, and daily operation figures |
| `full-pack` | Experiment specification, protocol, manual, prompt pack, and final figures |

## Installation

Clone the repository into the Codex skills directory.

### Windows PowerShell

```powershell
git clone https://github.com/x765254958/design-experiment-visual-guides.git `
  "$env:USERPROFILE\.codex\skills\design-experiment-visual-guides"
```

After reopening a Codex task, invoke the Skill explicitly:

```text
Use $design-experiment-visual-guides to design my CCK-8 experiment and
generate a beginner manual, plate map, and D0/D1/D2 operation visuals.
```

## Quick start

### 1. Initialize a project

```bash
python scripts/init_experiment_project.py \
  --name l929-cck8-pilot \
  --out ./work
```

### 2. Edit the experiment specification

Edit the generated file:

```text
work/l929-cck8-pilot/experiment_spec.json
```

See [`assets/experiment-spec.example.json`](assets/experiment-spec.example.json) for an example.

### 3. Validate the specification

```bash
python scripts/validate_experiment_spec.py \
  work/l929-cck8-pilot/experiment_spec.json
```

- `ERROR`: must be resolved before continuing.
- `WARNING`: must remain visible as a pre-run confirmation in the manual.
- Passing validation does not replace ethics, biosafety, or local laboratory approval.

### 4. Build the daily visual prompt pack

```bash
python scripts/build_visual_prompt.py \
  work/l929-cck8-pilot/experiment_spec.json \
  --out work/l929-cck8-pilot/visual-prompts
```

Use deterministic tables or shapes for exact plate positions, numbers, and calculations. After generating an illustrated operation guide, inspect every label, unit, arrow, instrument, and action sequence before use.

## Evidence levels for parameters

| Level | Meaning |
| --- | --- |
| `confirmed` | Supplied by the laboratory, manufacturer, approved SOP, or user |
| `literature` | Reproduced from a citable primary research source |
| `provisional` | Proposed as a pilot starting condition and not yet validated |
| `unknown` | Unresolved and capable of changing the design |

The Skill does not present a pilot condition as a regulation, standard, or established result.

## Repository structure

```text
.
├── SKILL.md                         # Main Skill instructions
├── agents/openai.yaml              # Codex display metadata and default prompt
├── assets/
│   ├── experiment-spec.example.json
│   └── style-reference/             # CCK-8 layout and operation examples
├── references/                      # Design, output, safety, and visual guidance
├── scripts/                         # Initialization, validation, and prompt tools
└── .github/workflows/validate.yml   # Automated GitHub validation
```

## Safety boundary

Work involving live microorganisms, primary human material, genetically modified organisms, hazardous chemicals, or animals must follow the training, SOPs, ethics approval, and biosafety requirements of the responsible institution. This repository helps organize and audit experimental design; it does not replace local approval or invent unconfirmed anesthesia, infection, sterilization, disposal, or waste-handling parameters.

## Development and validation

After installing PyYAML, run:

```bash
python scripts/validate_skill_package.py .
python -m py_compile scripts/*.py
```

GitHub Actions validates the Skill structure and required resources on every push to `main` and on every pull request.

## Interpretation note

The purpose of this project is to keep the experiment design, written procedure, and operation figures synchronized to one parameter source. Expected-result figures may illustrate the planned data format, but they must never be presented as actual experimental results.
