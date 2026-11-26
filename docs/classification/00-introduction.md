# Classification — Overview

**Classification** predicts which **group** a row belongs to. It can be **binary** (two classes) or **multi-class** (three or more). Typical examples are disease present/absent, treatment responder/non-responder, or heart-failure phenotypes.

In QuadML you configure and compare complete pipelines of cleaning, imputation, scaling, feature selection, dimensionality reduction, and classifiers and then evaluate them with Train / Test (or External) metrics, plots, and model explanations. All computation runs locally; no data is uploaded.

### Clinical examples

- Presence of significant coronary artery disease: yes / no  
- Response to cardiac resynchronization therapy: responder / non-responder  
- Heart failure phenotype: HFrEF / HFmrEF / HFpEF  

**Attention**: Use Classification for discrete labels. For a continuous outcome use Regression; for time-to-event use Survival Analysis; for unlabeled grouping use Clustering.

![Classification in the left navigation](../assets/class/Class01.png)

Settings for each step live under **Pipeline**.
