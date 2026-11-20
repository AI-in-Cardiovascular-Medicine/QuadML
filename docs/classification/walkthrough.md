# Classification — end-to-end walkthrough

## 1. Start

Open QuadML → Classification → File Selection.

Select File → Browse.

Output Directory → Browse (parent folder).

Set Label Column (or Auto-Detect).

Leave Task Type on auto. For binary, leave Decision Threshold on Youden (Train) unless you have a reason to change it.

Optional: ID Column, Column Removal, External file.

## 2. Preprocess (keep it small)

| Step | Choice |
| --- | --- |
| Data Cleaning | None |
| Imputation | Simple Imputation |
| Scaling | Standard Scaler |
| Feature Selection | None |
| Dimensionality Reduction | None |

## 3. Models and split

Classifiers: Logistic Regression and Random Forest

Data Splitting: 80/20, Train on all data unchecked

## 4. Run

Parameter Tuning: Random Search, Balanced budget, CPU/RAM 50/50.

Review the selected configuration tree.

Click Start Procedure.

Wait until the progress box finishes. Use Stop Procedure only if you need to cancel.

## 5. Read output

Results: open Metric Explanations. Compare Test metrics. Select the combination you want.

Visualization: pick that combination; open ROC or a metric chart; use Plot Explanations / Analyze.

Interpretability: Load files for that pipeline; Prepare Explainer for SHAP or Permutation Importance; open one plot.

You should find Final_Results.csv under Your Folder\YYYY-MM-DD_HH-MM-SS\.
