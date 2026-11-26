## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | No scaling is applied: leaves all values unchanged | Features are on the same scale; tree-based models |
| **Standard Scaler** | Subtracts the mean and divides by the standard deviation (mean 0, variance 1) | Default choice for distance- or coefficient-based models |
| **Min-Max Scaler** | Rescales each feature to a fixed range (0 to 1 by default) | Features with known bounds; neural networks (MLP) |
| **Robust Scaler** | Subtracts the median and divides by the interquartile range | Features with outliers |
| **Max Absolute Scaler** | Divides each feature by its maximum absolute value (range −1 to 1), keeping zeros at zero | Data with many zeros (sparse data) |
| **Power Transformer** | Applies a power transformation (Yeo-Johnson by default) to make each feature more Gaussian | Skewed features |
| **Quantile Transformer** | Maps values to a uniform or normal distribution based on their ranks | Heavy-tailed features or strong outliers; note that it changes the shape of the distribution |
| **Normalizer** | Rescales each sample (row), not each feature, to unit norm | Rarely suitable for tabular clinical data; only when the overall magnitude of a sample matters |
