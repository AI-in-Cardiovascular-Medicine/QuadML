## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | Leaves imputed values unchanged | Tree ensembles; no-scale baseline |
| **Standard Scaler** | Mean 0, variance 1 | Default first choice for linear / SVM-style models |
| **Min-Max Scaler** | Scales to a fixed range | Bounded features; neural nets |
| **Robust Scaler** | Centers/scales with median and IQR | Outliers that survive cleaning |
| **Max Absolute Scaler** | Scales by max absolute value | Sparse data; preserve zeros |
| **Power Transformer** | Reduces skew / stabilizes variance | Skewed numeric features |
| **Quantile Transformer** | Maps to normal or uniform | Heavy tails; rank like scaling |
| **Normalizer** | Unit-norm per row | Row-wise magnitude matters |
