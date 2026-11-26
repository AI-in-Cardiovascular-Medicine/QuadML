# Clustering — Scaling

Scaling puts features on comparable ranges, so that features with large values (e.g. cholesterol in mg/dL) don't outweigh features with small ones (e.g. creatinine in mg/dL). Distance-based algorithms (**K-Means**, **DBSCAN**, **OPTICS**, **Spectral Clustering**, and similar) usually need it; **None** leaves values unchanged. It is fit on the prepared clustering data (there is no Train/Test split). Clustering omits **Quantile Transformer** and **Normalizer**. Enable only what you need because each extra scaler multiplies the search.

![Scaling](../assets/cluster/12.png)

## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | No scaling is applied: leaves all values unchanged | Features are on the same scale |
| **Standard Scaler** | Subtracts the mean and divides by the standard deviation (mean 0, variance 1) | Default choice for distance-based clustering |
| **Min-Max Scaler** | Rescales each feature to a fixed range (0 to 1 by default) | Features with known bounds |
| **Robust Scaler** | Subtracts the median and divides by the interquartile range | Features with outliers |
| **Max Absolute Scaler** | Divides each feature by its maximum absolute value (range −1 to 1), keeping zeros at zero | Data with many zeros (sparse data) |
| **Power Transformer** | Applies a power transformation (Yeo-Johnson by default) to make each feature more Gaussian | Skewed features |

## Common mistakes

- Distance-based clustering with only **None** on mixed-scale features
- Selecting every scaler on the first run
- Expecting Quantile Transformer or Normalizer on this page (hidden in Clustering)
