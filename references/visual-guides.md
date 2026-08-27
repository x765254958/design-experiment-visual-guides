# Daily operation visual guides

## Purpose

Convert an approved written protocol into a visual execution aid. A figure does not replace training or an SOP.

## Visual set

For each relevant day create:

1. **Layout figure** — plate map, sample positions, group colors, data wells, and background wells.
2. **Operation figure** — actions, instruments, sequence arrows, key parameters, calculations, and warnings.

Use day labels consistently: D0, D1, D2, or descriptive phases when calendar days are inappropriate.

## Operation figure structure

Use a landscape 3:2 layout with:

- title and one-line day objective;
- left panel: numbered operations;
- center panel: illustrated action sequence;
- right panel: key parameters;
- bottom-left: calculation or preparation table;
- bottom-right: warnings and stop conditions.

Keep one figure focused on one day's executable work. Move analysis and interpretation to a separate figure if crowded.

## Content rules

- Derive labels and numbers from `experiment_spec.json`.
- Show preparation concentration and final exposure concentration separately.
- Show where mixing, timing, labeling, background controls, and photos are required.
- Use exact units and Unicode symbols consistently.
- Use the same group codes and colors across all days.
- Label provisional conditions as “reference” or “pilot”.
- Include “laboratory SOP prevails” where local handling matters.

## Image-generation workflow

1. Generate the prompt pack with `scripts/build_visual_prompt.py`.
2. Use the image-generation capability with the project's approved style reference.
3. Generate one asset per day and per visual type.
4. Inspect the image at original resolution.
5. Check every character, number, unit, arrow direction, container, instrument, and day label.
6. If exact text fails, regenerate or overlay the labels deterministically in PowerPoint/SVG/HTML before delivery.

Do not rely on image generation alone for dense plate maps, formulas, or exact tables; create those deterministically.

## Style reference assets

The `assets/style-reference/` folder contains a CCK-8 example set. Use it to learn layout and visual hierarchy, not as a universal scientific protocol.

