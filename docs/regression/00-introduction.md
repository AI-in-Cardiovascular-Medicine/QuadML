# Regression — Overview

**Regression** predicts a **numeric** value for each row. Typical examples are a lab measurement, score, dose, price, or any continuous clinical or research outcome.

In QuadML you build and compare full pipelines—cleaning, imputation, scaling, feature selection, dimensionality reduction, and regressors—then review error/fit metrics (MAE, RMSE, R², …), residual plots, and explanations. There is no class label, Task Type, or Decision Threshold. Everything runs locally; no data is uploaded.

### Clinical examples

- Estimated glomerular filtration rate (eGFR)  
- Peak VO₂ or another continuous exercise metric  
- Length of hospital stay (days)  

Use Regression for continuous outcomes. For discrete labels use Classification; for time-to-event use Survival Analysis; for unlabeled grouping use Clustering.

![Regression in the left navigation](../assets/reg/0.png)

Settings for each step live under **Pipeline**. For a click-through first run, open the [Tutorial](walkthrough.md).

### Suggested first configuration

| Step | Choice |
|------|--------|
| Cleaning | **None** |
| Imputation | **Simple Imputation** |
| Scaling | **Standard Scaler** |
| Feature Selection | **None** |
| Dimensionality Reduction | **None** |
| Models | Linear Regression + Random Forest |
| Split | 80/20, Train on all data **off** |
| Search | Random Search, **Fast** or **Balanced** → **Start Procedure** |
