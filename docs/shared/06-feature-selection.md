# Shared — Feature Selection

**Where**: Any mode → **Feature Selection**

Rank or drop **original** features before optional dimensionality reduction and the model. **None** / no selection keeps all features in that stage of the product. Method lists differ by mode (supervised vs unsupervised vs survival-aware).

---

## What to click

1. Toggle feature-selection method cards (including **None** when offered).
2. Adjust per-method parameters (*k*, thresholds, etc.) via **More Configs**.
3. Prefer **None** on first runs unless you already know a selector helps (or the feature count makes a full-feature search too expensive).

---

## Relation to Dimensionality Reduction

Feature Selection works on original columns. Dimensionality Reduction (where available) compresses whatever remains. Both multiply in the search product when checked (FS × DR). Invalid pairs (for example Clustering **Laplacian Score** + non-None DR) are rejected by the search.

Survival descriptive models (KM / Nelson–Aalen) do not use feature selection.

---

## Common mistakes

- Aggressive selection that removes rare but important predictors before you have baseline metrics
- Combining many FS methods with many models without checking the configuration tree count
- Looking for supervised selectors in Clustering, or generic MI/Variance Threshold on Survival’s allowlist page

---

## Mode manuals

- [Classification — Feature Selection](../classification/05-feature-selection.md)
- [Regression — Feature Selection](../regression/05-feature-selection.md)
- [Survival — Feature Selection](../survival/05-feature-selection.md)
- [Clustering — Feature Selection](../clustering/05-feature-selection.md)
