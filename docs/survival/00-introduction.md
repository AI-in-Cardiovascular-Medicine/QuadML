# Survival Analysis — Overview

**Survival Analysis** estimates **time-to-event** outcomes: each row has a **duration** (follow-up time) and an **event / censor** indicator (event observed vs still event-free at last contact).

In QuadML you configure and compare complete pipelines by cleaning, imputation, scaling, feature selection, dimensionality reduction, descriptive curves (Kaplan–Meier / Nelson–Aalen), and survival models (Cox, AFT, RSF, and related methods) and then evaluate them with discrimination and calibration metrics (C-index, td-AUC, IBS, Mean Cal, Slope, ICI), survival plots, and model explanations. Unlike Classification or Regression, you map **Duration** and **Event / Censor** columns and set evaluation horizons. All computation runs locally; no data is uploaded.

### Clinical examples

- Time to death or transplant after diagnosis  
- Time to restenosis after stenting  
- Time to device failure with right censoring  

**Attention**: Use Survival for duration and event. For discrete labels use Classification; for a continuous outcome use Regression; for unlabeled grouping use Clustering.

![Survival Analysis in the left navigation](../assets/sa/0.png)

Settings for each step live under **Pipeline**. For a click-through first run, open the [Tutorial](walkthrough.md).

