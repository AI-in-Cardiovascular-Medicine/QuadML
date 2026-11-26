## Sample-level methods

Whole samples with unusual values overall are removed.

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **Isolation Forest** | Finds samples that are easy to separate from the rest | Large datasets or many features; scales well |
| **Local Outlier Factor** | Finds samples in sparser regions than their neighbors | Data with groups of different density |
| **DBSCAN** | Finds samples that don't belong to any dense group | Data with clear groups |
| **One-Class SVM** | Learns a boundary around typical samples and removes those outside | Smaller datasets; slower on large ones |
