# Classification — Overview

**Classification** predicts which **group** a row of the dataset belongs to. It can be **binary** (two classes) or **multi-class** (three or more).

In QuadML you build and compare full pipelines—cleaning, imputation, scaling, feature selection, dimensionality reduction, and classifiers, then review metrics, plots, and explanations. Binary tasks can set a **Decision Threshold** for hard-label metrics. Everything runs locally; no data is uploaded.

### Clinical examples

- Presence of significant coronary artery disease: yes / no  
- Response to cardiac resynchronization therapy: responder / non-responder  
- Heart failure phenotype: HFrEF / HFmrEF / HFpEF  

Use Classification for discrete labels. For a continuous outcome use Regression; for time-to-event use Survival Analysis; for unlabeled grouping use Clustering.

![Classification in the left navigation](../assets/class/Class01.png)

Settings for each step live under **Pipeline**. For a click-through first run, open the [Tutorial](walkthrough.md).

### Suggested first configuration

| Step | Choice |
|------|--------|
| Cleaning | **None** |
| Imputation | **Simple Imputation** |
| Scaling | **Standard Scaler** |
| Feature Selection | **Select K Best** |
| Dimensionality Reduction | **None** |
| Models | Logistic Regression + Random Forest |
| Split | 80/20, Train on all data **off** |
| Search | Random Search, **Fast** or **Balanced** → **Start Procedure** |
