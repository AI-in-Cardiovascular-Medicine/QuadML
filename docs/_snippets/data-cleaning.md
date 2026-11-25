
## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | No outlier detector; baseline hygiene only | Clean data; first baseline |
| **Interquartile Range** | Flags extreme cells with IQR fences | Classic univariate outliers |
| **Z-Score** | Flags cells far from the mean | Roughly Gaussian features |
| **Modified Z-Score** | Robust median-based fences | Skewed features / outliers |
| **Isolation Forest** | Drops outlier **rows** (multivariate) | Row-level anomalies |
| **Local Outlier Factor** | Drops outlier rows by local density | Local density anomalies |
| **DBSCAN** (cleaning) | Drops outlier rows | Density-based row outliers |
| **One-Class SVM** | Drops outlier rows | One-class boundary outliers |
