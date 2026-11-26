# Clustering — Overview

**Clustering** groups similar rows into cohorts **without** a required target label. Typical examples are patient subtypes, sample cohorts, or any unsupervised segmentation.

In QuadML you configure and compare complete pipelines—cleaning, imputation, scaling, unsupervised feature selection, dimensionality reduction, and clustering models—then evaluate them with internal validation metrics (Silhouette, Calinski–Harabasz, Davies–Bouldin, DISCO, BIC, and related scores), assignment CSVs, and cluster plots. Unlike Classification, Regression, or Survival Analysis, there is no required outcome column, no External file, no Data Splitting, and no Interpretability step. **Search Settings** replaces Parameter Tuning. All computation runs locally; no data is uploaded.

### Clinical examples

- Molecular or clinical patient subtypes  
- Device / sample cohorts without a gold-standard label  
- Exploratory grouping before a supervised task  

**Attention**: Use Clustering for unlabeled grouping. For discrete labels use Classification; for a continuous outcome use Regression; for time-to-event use Survival Analysis.

![Clustering in the left navigation](../assets/cluster/0.png)

Settings for each step live under **Pipeline**.

### What is different

- No required target; optional **Benchmark Label** for ARI / NMI / FMI only (not used for ranking)
- No External file, no Data Splitting, no Interpretability
- **Search Settings** replaces Parameter Tuning
- Feature Selection is unsupervised; no LDA; sample-level cleaning methods are hidden

