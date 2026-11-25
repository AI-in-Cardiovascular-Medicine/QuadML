# Clustering — Scaling

Rescales imputed feature values so every searched pipeline has comparable numeric inputs for feature selection, dimensionality reduction, and clustering. Distance-based algorithms (**K-Means**, **DBSCAN**, and similar) usually need scaling; **None** keeps values unchanged when you want an unscaled baseline. Scaling is applied at **Start Procedure**. Enable only what you need because each extra scaler multiplies the search.

![Scaling](../assets/cluster/12.png)

## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | Leaves imputed values unchanged | Unscaled baseline |
| **Standard Scaler** | Mean 0, variance 1 | Default first choice for distance-based clustering |
| **Min-Max Scaler** | Scales to a fixed range | Bounded features |
| **Robust Scaler** | Centers/scales with median and IQR | Outliers that survive cleaning |
| **Max Absolute Scaler** | Scales by max absolute value | Sparse data; preserve zeros |
| **Power Transformer** | Reduces skew / stabilizes variance | Skewed numeric features |

![None and Standard Scaler selected](../assets/cluster/13.png)

## Common mistakes

- Distance-based clustering with only **None** on mixed-scale features
- Selecting every scaler on the first run
- Expecting Quantile Transformer or Normalizer on this page (hidden in Clustering)
