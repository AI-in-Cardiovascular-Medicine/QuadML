# Regression — Scaling

**Where**: Regression → **Scaling**

**Scaling** rescales imputed feature columns before Feature Selection, Dimensionality Reduction, and the regressor. Each checked method (including **None**) becomes part of the combinatorial search with Imputation × FS × DR × Regressors. Linear models and SVR usually need scaling; many tree models work well with **None**.

![scaling methods](../assets/reg/13.png)

---

## Methods

| Method | Short idea |
|--------|------------|
| **None** | Skip scaling; keep imputed values as-is |
| **Standard Scaler** | Mean 0, variance 1 |
| **Min-Max Scaler** | Scale to a fixed range |
| **Robust Scaler** | Center/scale with robust statistics (median / IQR) |
| **Max Absolute Scaler** | Scale by max absolute value |
| **Power Transformer** | Stabilize variance / reduce skew (search may tune yeo-johnson / box-cox) |
| **Quantile Transformer** | Map to normal or uniform (search may tune distribution) |
| **Normalizer** | Scale each sample to unit norm (search may tune l1 / l2 / max) |

Selecting **None** keeps the imputed feature values unchanged for that pipeline branch.

For a first run, enable **Standard Scaler** and optionally **None**. Avoid checking every scaler on a large search.

![scaling method cards with Select All / Unselect All](../assets/reg/14.png)

---

## What to click

1. Toggle the scaling method cards to include in the search (at least **None** or one scaler).
2. Click **i** on a card for how it works, defaults, pros/cons, and a library link.
3. Use **Select All** / **Unselect All** if you need to manage many cards at once.

There is no user **More Configs** panel for scaling on this page. Where a method has tunable options (Power Transformer, Quantile Transformer, Normalizer), Parameter Tuning explores them during the search.

---

## What is written to disk

The fitted scaler is stored inside the saved pipeline (`.pkl`). Results labels use short codes such as `StdSc` or `No scaling`.

When scaling is on, some Interpretability plots can show original (pre-scale) feature values on axes while the model still uses scaled inputs.

---

## Common mistakes

- Forgetting **None** when you want a no-scale baseline for tree models
- Selecting every scaler on the first run
- Expecting linear / SVR pipelines to work well with **None** only on unscaled features with very different ranges
