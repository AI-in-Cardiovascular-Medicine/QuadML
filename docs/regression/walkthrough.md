# Regression — end-to-end walkthrough

Follow this once with a small `.csv` or `.xlsx` that has a **numeric outcome** (price, score, lab value, …) and feature columns. Keep every step minimal so the first run finishes quickly. For “why” and edge cases, open the linked step pages.

---

## 1. Start

1. Open QuadML → **Regression** → **File Selection**.
2. **Select File → Browse** — choose your dataset (header row required).
3. **Output Directory → Browse** — choose a **parent** folder. Each run creates a dated subfolder `YYYY-MM-DD_HH-MM-SS`.
4. Set **Label Column** to the numeric outcome (or **Auto-Detect**). In Regression this is the continuous **Target Column** — not classes.
5. Optional: **ID Column**, **Column Removal**, **External Test Data**.

Details: [File Selection](01-file-selection.md).

---

## 2. Preprocess (keep it small)

Use **one** choice per step so the search stays short:

| Step | First-run choice |
|------|------------------|
| [Data Cleaning](02-data-cleaning.md) | **None** (or **IQR** if you already know outliers matter) |
| [Imputation](03-imputation.md) | **Simple Imputation** |
| [Scaling](04-scaling.md) | **Standard Scaler** |
| [Feature Selection](05-feature-selection.md) | **None** |
| [Dimensionality Reduction](06-dimensionality-reduction.md) | **None** |

Leave extra methods unchecked until you need them.

---

## 3. Models and split

1. **Regressors:** check **Linear Regression** and **Random Forest** only ([Regressors](07-regressors.md)).
2. **Data Splitting:** **80 / 20**, leave **Train on all data** unchecked ([Data Splitting](08-data-splitting.md)).

---

## 4. Run

1. Open **Parameter Tuning**.
2. Set **Random Search**, **Balanced** (or **Fast**) budget, CPU/RAM **50 / 50**.
3. Review the selected configuration tree — it should list only the choices above.
4. Click **Start Procedure**.
5. Wait until the progress box finishes. Use **Stop Procedure** only if you need to cancel.

Details: [Parameter Tuning](09-parameter-tuning.md).

---

## 5. Read output

1. **Results:** open **Metric Explanations**. Prefer **Test** MAE / RMSE / R² (lower error is better; R² closer to 1 is better). Select the pipeline combination you want ([Results](10-results.md)).
2. **Visualization:** pick that same combination; open **Residuals vs Predicted** or a metric chart; use **Plot Explanations** / Analyze ([Visualization](11-visualization.md)).
3. **Interpretability:** **Load** files for that pipeline; **Prepare Explainer** for SHAP or Permutation Importance; open one plot ([Interpretability](12-interpretability.md)).

Success: `Final_Results.csv` under `Your Folder\YYYY-MM-DD_HH-MM-SS\`.

---

## Variants (not part of this walkthrough)

Configure these on the listed pages and re-run:

| Variant | Where |
|---------|--------|
| External hold-out file | File Selection |
| Train on all data | Data Splitting (External file required) |
| Bootstrap CIs | Parameter Tuning |
| Extra imputers / scalers / FS / DR / models | Respective steps |

---

## Related pages

- [Introduction](00-introduction.md)
- [Regression documentation index](index.md)
