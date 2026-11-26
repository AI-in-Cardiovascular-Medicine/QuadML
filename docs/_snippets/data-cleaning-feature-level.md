## Feature-level methods

Outlier values are filled in later by Imputation.

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **Interquartile Range** | Sets values far outside the middle 50% of the data to missing | Any feature; no assumption about the distribution |
| **Z-Score** | Sets values many standard deviations from the mean to missing | Features with a roughly bell-shaped distribution |
| **Modified Z-Score** | Like Z-Score, but based on the median, so less affected by the outliers themselves | Skewed features, or when outliers are extreme |
