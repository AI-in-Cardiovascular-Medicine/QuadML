# Clustering — Feature selection

**Where**: Clustering → **Feature Selection**

**Task note:** Unsupervised selectors only (Variance Threshold, Correlation Thresholding, Feature Agglomeration, Laplacian Score, …). If **Laplacian Score** is selected, Dimensionality Reduction must be **None**.

![Feature Selection](../assets/cluster/15.png)

--8<-- "_snippets/feature-selection.md"

## Common mistakes

- Turning off **None** when you still want a full-feature baseline
- Enabling SFS/SBS with a large feature budget on a smoke run
- Confusing this step with PCA (that is Dimensionality Reduction)
