# Shared — Scaling

**Where**: Any mode → **Scaling**

Select **one or more** scalers (including **None** / no scaling where offered). Checked scalers enter the search product with imputation, feature selection, DR, and models.

---

## What to click

1. Toggle scaler cards (for example **Standard Scaler**, **Min-Max Scaler**, **None**).
2. Use **Select All** / **Unselect All** if present.
3. Open advanced parameters via **More Configs** only when a method supports them on this page (many scalers are tuned later during search).
4. For a first run, **Standard Scaler** plus optional **None** is a common pair.

**Clustering** omits Quantile Transformer and Normalizer. Survival descriptive models (KM / Nelson–Aalen) do not use scaling.

---

## Common mistakes

- Scaling-sensitive models (linear / SVM-style) with only **None** when features are on very different scales
- Selecting every scaler unnecessarily
- Looking for Quantile Transformer / Normalizer in Clustering

---

## Mode manuals

- [Classification — Scaling](../classification/04-scaling.md)
- [Regression — Scaling](../regression/04-scaling.md)
- [Survival — Scaling](../survival/04-scaling.md)
- [Clustering — Scaling](../clustering/04-scaling.md)
