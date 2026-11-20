# Shared — Data Cleaning

**Where**: Any mode → **Data Cleaning**

Choose one cleaning policy and optional **Correlation Analysis** (where shown). Cleaning runs on **Start Procedure**; correlation filtering (when enabled) runs later on the **training** set after the train/test split (supervised modes).

---

## What to click

### Cleaning method (choose one)

1. Expand Feature-Level and/or Sample-Level sections as shown (Clustering hides sample-level methods).
2. Select **exactly one** method (if you do not choose any cleaning method, that means **None**):
   - **None** — leave every method card unselected; baseline hygiene only (outlier cleaning off).
   - A **Feature-Level** detector — outlier cells become NaN and are filled later by Imputation.
   - A **Sample-Level** detector — whole outlier rows are dropped (not available in Clustering).
3. Optional **More Configs…** for advanced parameters of the selected method.

### Correlation Analysis (optional)

4. Enable **Correlation Analysis** if you want high-correlation feature filtering after the split.
5. Set method and **threshold** (default often near **0.99**) when controls are enabled.
6. Clustering **hides** Correlation Analysis on this page — use Feature Selection → **Correlation Thresholding** instead.

Status text reminds you: cleaning is off under **None**, but baseline hygiene still runs on **Start Procedure**. **Exact Duplicate Rows** and **Missing / Outlier Threshold** remain available in modes that show them (including Clustering).

---

## Workflow note

Data cleaning runs when you click **Start Procedure**.  
Optional Correlation Analysis is chosen here, but runs later on the training set after the train/test split (supervised modes).

---

## Common mistakes

- Selecting a Feature-Level detector and forgetting to include an Imputation method for the NaNs it creates
- Expecting correlation or cleaning to rewrite the preview before **Start Procedure**
- Combining many expensive cleaners — only **one** cleaning method is active
- Looking for Isolation Forest / Correlation Analysis in Clustering on this page

---

## Mode manuals

- [Classification — Data Cleaning](../classification/02-data-cleaning.md)
- [Regression — Data Cleaning](../regression/02-data-cleaning.md)
- [Survival — Data Cleaning](../survival/02-data-cleaning.md)
- [Clustering — Data Cleaning](../clustering/02-data-cleaning.md)
