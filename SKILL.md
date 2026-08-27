---
name: design-experiment-visual-guides
description: Design auditable laboratory experiments and turn the approved design into beginner-friendly protocols, plate maps, calculation tables, day-by-day checklists, and illustrated operation guides. Use when a user asks to formulate or simplify an experimental plan, choose groups or concentrations, arrange experimental order, write an SOP/Word manual, produce D0/D1/D2 workflow figures, or convert an existing protocol, paper, or lab conditions into visual execution guidance for cell, material, microbiology, biochemical, or animal studies.
---

# Design Experiment Visual Guides

Build the experiment in two passes: first freeze an auditable design, then create execution artifacts from that same frozen specification. Never draw the workflow before resolving contradictions that would change the experiment.

## Core workflow

### 1. Collect the minimum experiment brief

Read `references/intake.md`. Extract facts from user files before asking questions. Ask only for missing information that changes groups, doses, timing, safety, statistics, or feasibility.

Classify every parameter as one of:

- `confirmed`: supplied by the laboratory, manufacturer, approved SOP, or user.
- `literature`: reproduced from a cited primary source.
- `provisional`: a proposed starting condition requiring a pilot.
- `unknown`: unresolved and capable of changing the design.

Never relabel a provisional parameter as a standard or regulation.

### 2. Apply the safety and governance gate

Read `references/safety-governance.md` before giving operational detail for live microorganisms, primary human material, genetically modified organisms, hazardous chemicals, or animals.

- Continue only within the user's approved laboratory scope and training.
- Require institutional SOP/ethics/biosafety confirmation where applicable.
- Do not invent sterilization, dosing, disposal, anesthesia, infection, or containment procedures.
- When a safe protocol depends on local approval, output the decision point and required confirmation instead of guessing.

### 3. Build the experimental logic

Read `references/protocol-design.md`. Define in order:

1. Research question and primary endpoint.
2. Experimental unit and comparison logic.
3. Controls, groups, dose basis, and batch pairing.
4. Pilot versus formal experiment.
5. Technical replicates versus independent biological repeats.
6. Dependency graph: what can run in parallel and what must wait.
7. Quality controls, stop conditions, raw records, and interpretation limits.

Use current primary literature when parameters are uncertain, time-sensitive, or source attribution matters. Keep literature-derived conditions separate from the final user-specific choice.

### 4. Freeze the experiment specification

Create `experiment_spec.json` using `assets/experiment-spec.example.json` as the schema example. Initialize a project with:

```bash
python scripts/init_experiment_project.py --name <project-name> --out <directory>
```

Validate the edited specification:

```bash
python scripts/validate_experiment_spec.py <directory>/experiment_spec.json
```

Resolve every `ERROR`. Preserve `WARNING` items in the manual as pre-run confirmations.

### 5. Produce the written protocol

Follow `references/output-contract.md`. Create a concise experiment plan first, then a separate beginner manual if requested.

For Word output, use the document-creation capability and render the final DOCX for visual QA. The beginner manual must make the purpose and the method correspond one-to-one and must include:

- group table;
- preparation list;
- exact calculation basis;
- labeled day-by-day operations;
- plate map where relevant;
- quality controls and stop conditions;
- raw-data table;
- interpretation boundary.

Do not add assays merely because they are common. Include only assays needed to answer the stated question or required by a confirmed protocol.

### 6. Generate execution visuals

Read `references/visual-guides.md`. Derive every visual from `experiment_spec.json`, not from memory.

Generate the daily visual prompt pack:

```bash
python scripts/build_visual_prompt.py <directory>/experiment_spec.json --out <directory>/visual-prompts
```

Create two complementary visual types:

- layout visual: plate map, grouping, sample position, or timeline;
- operation visual: instruments, preparation, action sequence, key parameters, and warnings for one day.

Use deterministic tables/shapes for exact plate maps and calculations. Use image generation for illustrated laboratory actions and style matching. After generation, inspect every label, number, unit, arrow, and instrument. Correct text or units before delivery.

### 7. Cross-check all artifacts

Verify that the specification, protocol, plate map, calculation table, and figures use identical:

- group names;
- concentrations and units;
- volumes and final concentrations;
- sample/batch pairing;
- day labels and treatment duration;
- control definitions;
- endpoint names.

Do not deliver a figure if it conflicts with the written method.

## Output modes

Select the smallest mode that satisfies the request:

- `design-only`: research logic, groups, endpoints, dependencies, unresolved questions.
- `protocol`: design plus method and records.
- `beginner-manual`: protocol expanded into executable steps and checks.
- `visual-pack`: approved manual converted into daily layout and operation figures.
- `full-pack`: specification, protocol, manual, prompt pack, and final figures.

## Domain examples

- For L929 CCK-8 planning, read `references/example-cck8.md`.
- For two-strain CFU plate counting, read `references/example-cfu.md`.

These are examples of structure, not universal experimental standards. Replace their provisional parameters with the user's confirmed laboratory conditions.

