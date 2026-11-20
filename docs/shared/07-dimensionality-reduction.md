# Shared — Dimensionality Reduction

**Where**: Classification, Regression, Clustering, and Survival Analysis

Compress features **after** Feature Selection. **None** / no DR keeps the current feature space for that branch of the product. Every checked FS method is crossed with every checked DR method (FS × DR), except mode-specific invalid pairs.

---

## What to click

1. Toggle DR method cards (PCA and others as listed; Classification may include **LDA**).
2. Set components / parameters in on-card controls when shown.
3. Include **None** if you want an unreduced baseline in the same search.

---

## Mode differences (summary)

| Mode | Notes |
|------|--------|
| Classification | Includes **LDA** among DR options |
| Regression | PCA / ICA / Kernel PCA / None (no LDA) |
| Clustering | PCA / ICA / Kernel PCA / None (no LDA); Laplacian Score forces DR = None |
| Survival | None / PCA / ICA / Kernel PCA (no LDA). KM / Nelson–Aalen skip DR |

---

## Common mistakes

- Setting components higher than usable sample/feature size
- Omitting **None** when you still want a non-reduced comparison
- Looking for **LDA** outside Classification
- Confusing Feature Selection (rank/drop original columns) with DR (project into components)

---

## Mode manuals

- [Classification — Dimensionality Reduction](../classification/06-dimensionality-reduction.md)
- [Regression — Dimensionality Reduction](../regression/06-dimensionality-reduction.md)
- [Survival — Dimensionality Reduction](../survival/06-dimensionality-reduction.md)
- [Clustering — Dimensionality Reduction](../clustering/06-dimensionality-reduction.md)
