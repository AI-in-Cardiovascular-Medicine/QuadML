# Regression — Tutorial

End-to-end click path for a first Regression run. Keep the search small.

---

## 1. Start

1. Open QuadML → **Regression** → **File Selection**.
2. **Select File → Browse** — `.csv` / `.xlsx` with a numeric outcome.
3. **Output Directory → Browse** — writable parent folder.
4. Set **Label Column** to the numeric target (or **Auto-Detect**).
5. Optional: ID Column, Column Removal, External file.

![File Selection](../assets/reg/2.png)

---

## 2. Preprocess

| Step | Choice |
|------|--------|
| Data Cleaning | **None** |
| Imputation | **Simple Imputation** |
| Scaling | **Standard Scaler** |
| Feature Selection | **None** |
| Dimensionality Reduction | **None** |

---

## 3. Models and split

1. **Regressors:** **Linear Regression** + **Random Forest** only.
2. **Data Splitting:** 80/20, Train on all data **off**.

---

## 4. Run

1. **Parameter Tuning:** Random Search, Balanced (or Fast), CPU/RAM 50/50.
2. Review the tree → **Start Procedure** → wait (or **Stop** to cancel).

---

## 5. Read output

1. **Metrics:** prefer **Test** MAE / RMSE / R².
2. **Visualization:** Residuals vs Predicted or a metric chart.
3. **Interpretability:** Load the pipeline; Prepare Explainer for SHAP or Permutation Importance.

Success: `Final_Results.csv` under `Your Folder\YYYY-MM-DD_HH-MM-SS\`.
