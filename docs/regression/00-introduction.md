# Regression — Overview

**Regression** estimates a **continuous** outcome for each row, for example a lab value, clinical score, dose, or other numeric endpoint.

In QuadML you configure and compare complete pipelines, cleaning, imputation, scaling, feature selection, dimensionality reduction, and regressors and then evaluate them with error and fit metrics (MAE, RMSE, R², and related scores), residual diagnostics, and model explanations. Unlike Classification, there is no class label, Task Type, or Decision Threshold. All computation runs locally; no data is uploaded.

### Clinical examples

- Estimated glomerular filtration rate (eGFR)  
- Peak VO₂ or another continuous exercise metric  
- Length of hospital stay (days)  

**Attention**: Use Regression for continuous outcomes. For discrete labels use Classification; for time-to-event use Survival Analysis; for unlabeled grouping use Clustering.

![Regression in the left navigation](../assets/reg/0.png)

Settings for each step live under **Pipeline**.

### Suggested first configuration

| Step | Choice |
|------|--------|
| Cleaning | **None** |
| Imputation | **Simple Imputation** |
| Scaling | **Standard Scaler** |
| Feature Selection | **None** if the number of features are few |
| Dimensionality Reduction | **None** |
| Models | Linear Regression + Random Forest |
| Split | 80/20, Train on all data **off** |
| Search | Random Search, **Fast** or **Balanced** → **Start Procedure** |
