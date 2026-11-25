# Regression — Dimensionality reduction

**Where**: Regression → **Dimensionality Reduction**

Compresses features after Feature Selection. **LDA is not available** (Classification-only).

![Dimensionality Reduction](../assets/reg/19.png)

--8<-- "_snippets/dimensionality-reduction.md"

Choose methods and set options. For example PCA component count or explained variance, and the Kernel PCA kernel:

![Dimensionality Reduction algorithms](../assets/reg/20.png)

## Common mistakes

- Looking for **LDA** outside Classification
- Many DR methods without a **None** baseline
- Pairing Clustering **Laplacian Score** with non-None DR
