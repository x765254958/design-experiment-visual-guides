# Protocol design rules

## 1. State the claim before the assay

Write one sentence in the form:

> Compared with [control], [intervention] changes [primary endpoint] under [condition] after [time].

If the proposed assay cannot support that sentence, narrow the claim or change the assay.

## 2. Define the experimental unit

Separate:

- technical replicate: repeated wells/measurements from the same preparation;
- biological/independent repeat: new culture, synthesis batch, animal, donor, or experimental day;
- subsample: multiple images or fields from one experimental unit.

Never report technical wells as independent sample size.

## 3. Choose controls by causal question

Common roles:

- blank/background: detects reagent, medium, material, or optical background;
- negative control: establishes untreated or solvent-treated baseline;
- carrier control: separates carrier effects from loaded-material effects;
- positive control: confirms the assay can detect the expected direction;
- process control: detects contamination, handling failure, or batch failure;
- equivalent-dose control: compares active ingredient at matched actual dose.

Do not include all controls automatically. Include the minimum set needed for the stated inference.

## 4. Match the dose basis

Use total-particle mass when screening overall material performance. Use active-drug equivalent only after loading/release is quantified. If actual loading is unknown, do not claim a matched drug-dose comparison.

For composite or coating studies, also consider area dose, mass per area, extract ratio, or released concentration. Record both preparation concentration and final exposure concentration.

## 5. Pair batches correctly

Compare loaded and blank materials only within a defensible synthesis system. Do not cross-pair controls from different precursor ratios, solvent systems, reaction times, or particle-size regimes unless the experiment is explicitly designed to test those factors.

## 6. Separate pilot and formal experiments

Pilot goals:

- confirm feasibility;
- find countable/readable ranges;
- identify safe concentration limits;
- estimate variability;
- freeze the formal protocol.

Formal goals:

- use frozen parameters;
- include planned technical and independent repeats;
- apply predefined exclusion and stop rules;
- retain raw data and metadata.

Do not combine exploratory parameter changes with confirmatory statistics without clearly labeling them.

## 7. Build dependencies

Mark each task as:

- independent/parallel;
- requires material identity;
- requires dose/loading data;
- requires safety screening;
- requires prior endpoint result;
- requires ethics or biosafety approval.

Provide a simple dependency chain and explicitly identify tasks that can run in parallel.

## 8. Write quality controls and stop rules

For every assay define:

- acceptable control behavior;
- contamination/background check;
- instrument/readout range;
- replicate consistency check;
- reasons to repeat or stop;
- how results below detection or above range are recorded.

Never delete an inconvenient result without a predefined and recorded reason.

## 9. Set interpretation boundaries

Examples:

- metabolic activity is not identical to live-cell count;
- CFU reduction is not automatically MIC or MBC;
- morphology alone does not prove loading;
- a carrier-versus-loaded difference does not prove the active ingredient caused it when loading is unknown;
- a pilot animal signal is not a definitive efficacy claim.

