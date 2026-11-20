# Survival Analysis — end-to-end walkthrough

Follow this once with a small `.csv` or `.xlsx` that has a **Duration Column**, an **Event / Censor Column**, and feature columns. Keep every step minimal so the first run finishes quickly. For “why” and edge cases, open the linked step pages.

---

## 1. Start

1. Open QuadML → **Survival Analysis** → **File Selection**.
2. **Select File → Browse** — choose your dataset (header row required).
3. **Output Directory → Browse** — choose a **parent** folder. Each run creates a dated subfolder `YYYY-MM-DD_HH-MM-SS`.
4. Set **Duration Column** and **Event / Censor Column** (or **Auto-Detect**).
5. Set **Event Coding** so **1 = event observed** unless your file is coded the other way.
6. Leave **Eval. Horizons** on **Auto from follow-up**.
7. Optional: **ID Column**, **Column Removal**, **External Test Data** (External must also have duration + event).

Details: [File Selection](01-file-selection.md).

---

## 2. Preprocess (keep it small)

Use **one** choice per step so the search stays short:

| Step | First-run choice |
|------|------------------|
| [Data Cleaning](02-data-cleaning.md) | **None** (or one feature-level method if needed) |
| [Imputation](03-imputation.md) | **Simple Imputation** |
| [Scaling](04-scaling.md) | **Standard Scaler** |
| [Feature Selection](05-feature-selection.md) | **None** |
| [Dimensionality Reduction](06-dimensionality-reduction.md) | **None** |

Leave extra methods unchecked until you need them. KM / Nelson–Aalen ignore these steps (`N/A` on Results).

---

## 3. Models

1. **Descriptive Analysis:** check **Kaplan-Meier** ([Descriptive Analysis](07-descriptive-analysis.md)).
2. **Survival Models:** check **Cox Proportional Hazards** only ([Survival Models](08-survival-models.md)).

You can run descriptive only, covariate only, or both. **Start Procedure** needs at least one model on either page.

---

## 4. Split and run

1. **Data Splitting:** **80 / 20**, leave **Train on all data** unchecked ([Data Splitting](09-data-splitting.md)).
2. Open **Parameter Tuning**.
3. Set **Random Search** (or Grid Search), **Fast** budget, CPU/RAM **50 / 50**.
4. Review the selected configuration tree — it should list only the choices above.
5. Click **Start Procedure**.
6. Wait until the progress box finishes. Use **Stop Procedure** only if you need to cancel.

Details: [Parameter Tuning](10-parameter-tuning.md).

---

## 5. Read output

1. **Results:** open **Metric Explanations**. Do **not** pick by C-index alone if absolute risk matters — check **Mean Calibration**, **Slope**, and **ICI**, then Test C-index among well-calibrated rows ([Results](11-results.md)).
2. **Visualization:** Risk Group KM and Calibration Plot for the Cox pipeline; KM curve for Kaplan–Meier ([Visualization](12-visualization.md)).
3. **Interpretability:** **Load** the Cox `.pkl` + matching CSVs (with duration/event); try Cox Coefficients and/or SurvSHAP ([Interpretability](13-interpretability.md)).

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
| Custom / long-term horizons | File Selection → Eval. Horizons |

---

## Related pages

- [Introduction](00-introduction.md)
- [Survival Analysis documentation index](index.md)
