# Regression — Interpretability

**Where**: Regression → **Interpretability**

Explains a loaded fitted pipeline for the continuous target. Does **not** replace Test metrics.

![Interpretability](../assets/reg/47.png)

--8<-- "_snippets/interpretability-usage.md"

## Methods

| Approach | What it shows | Scope |
|----------|---------------|--------|
| **SHAP** | How each feature pushes the predicted value up or down | All rows and single rows |
| **Kernel SHAP** | Same idea for any model; usually slower | All rows and single rows |
| **LIME** | Local explanation for one row | Single rows |
| **Permutation Importance** | Drop in R² / MAE / … when a feature is shuffled | All rows |
| **PDP** | Average prediction as one or two features vary | All rows |
| **ICE** | One curve per row as a feature varies | Single rows |

**Task note:** No Class label control. PDP/ICE are available (not limited to binary tasks).

## Common mistakes

- Loading features from a different combination than the `.pkl`
- Treating Train explanations as external validation
- Using Interpretability instead of Test metrics to pick a model
- Running Interpretability without a successful fitted `.pkl`
