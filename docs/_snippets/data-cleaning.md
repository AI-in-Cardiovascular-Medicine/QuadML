Cleaning runs when you click **Start Procedure**, not when you change a card. If no method card is selected, that means **None** (baseline hygiene still runs).

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

Feature-level methods turn outlier **cells** into missing values (filled later by Imputation). Sample-level methods drop whole **rows**.

Optional on this page: **Exact Duplicate Rows**, **Missing / Outlier Threshold**, **Correlation Analysis** (supervised; Clustering uses FS → Correlation Thresholding instead).
