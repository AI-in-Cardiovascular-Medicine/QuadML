# Shared — Results

**Where**: Any mode → **Results** (after a search)

Browse pipeline combinations from `Final_Results.csv` (or rebuilt from `combo_results`). Labels use shared abbreviations. Metric sets differ by mode — open **Metric Explanations** in the app for definitions.

---

## What to click

1. Open **Results** after **Start Procedure** finishes (or after **Rebuild Results**). Confirm `Final_Results.csv` in the dated run folder, or **Browse** another folder that contains that CSV or combo JSON.
2. Read pipeline cards / rows (Train vs Test, or External, or unsupervised metrics — depending on mode).
3. Click **Metric Explanations** for the full in-app metric text.
4. Use Compare / Detailed Report / Show Selected (and filters) as labeled.

---

## Display conventions

Pipeline labels follow Shared abbreviation order, for example:

`IQR | SimpImp(med) | StdSc | SKB | LR`

Keep-all stages show as `No cleaning`, `No scaling`, `No selection`, `No DR` rather than being omitted. See [Outputs, abbreviations, and reports](14-outputs-abbreviations-reports.md).

Prefer held-out metrics (**Test** / **External**) in supervised modes. Clustering has no Train/Test — compare internal indices carefully and do not force one “winner” across paradigms.

---

## Common mistakes

- Comparing runs from different Output Directory dated folders without noting File Selection changes
- Expecting Bootstrap CI columns when Bootstrap was off for that run
- Opening a `Final_Results.csv` from a different mode
- Treating Train scores as generalization

---

## Mode manuals

- [Classification — Results](../classification/10-results.md)
- [Regression — Results](../regression/10-results.md)
- [Survival — Results](../survival/11-results.md)
- [Clustering — Results](../clustering/09-results.md)
