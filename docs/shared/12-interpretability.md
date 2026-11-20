# Shared — Interpretability

**Where**: Modes that expose it (Classification, Regression, Survival). **Clustering** has no Interpretability left-nav step — use Visualization profiling plots instead.

Explain a **loaded fitted pipeline** (`.pkl` + matching feature CSVs). Availability of methods (SHAP, LIME, PDP/ICE, SurvSHAP, …) depends on mode and model family. Interpretability does **not** replace Test or External metrics for ranking.

Point Results and Interpretability at the same dated run folder under your **Output Directory**.

---

## What to click

1. **Results** — load `Final_Results.csv` from the dated run folder.
2. **Interpretability** — Select Pipeline → **Load files** (model `.pkl`, training features CSV, testing features CSV) from that same run.
3. Choose an explanation method compatible with the detected model.
4. Click **Prepare Explainer** / **Compute** as shown — plot buttons stay disabled until this finishes.
5. Open plots from the grouped buttons; use in-app help for method limits.
6. Save or browse artifacts when offered (for example SurvSHAP `.npz` caches in Survival).

Most methods do **not** retrain the pipeline; they explain the loaded `.pkl`.

---

## Mode notes (summary)

| Mode | Notes |
|------|--------|
| Classification | PDP/ICE for **binary** only among other methods; Class label control for multi-class where shown |
| Regression | SHAP / LIME / Permutation / PDP / ICE on the continuous target (no Class label) |
| Survival | SurvSHAP / SurvivalLIME / Permutation / PDP / ICE / Cox·AFT coefficients; KM / Nelson–Aalen have none |
| Clustering | No Interpretability left-nav step |

---

## Common mistakes

- Running Interpretability without a successful fitted `.pkl` for the chosen combination
- Loading feature CSVs from a different combination than the `.pkl`
- Expecting Clustering to offer the same page
- Treating Train explanations as external validation

---

## Mode manuals

- [Classification — Interpretability](../classification/12-interpretability.md)
- [Regression — Interpretability](../regression/12-interpretability.md)
- [Survival — Interpretability](../survival/13-interpretability.md)
