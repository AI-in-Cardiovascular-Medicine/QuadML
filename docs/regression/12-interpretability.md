# Regression — Interpretability

Shows which features drive the predicted continuous value for a loaded fitted regression pipeline (global and local explanations). Use it after you choose a candidate from **Results**. It does **not** replace Test or External metrics for ranking models. Load the matching `.pkl` and feature CSVs, choose a method compatible with the model, set **Explain on**, then **Prepare Explainer**. Prefer **SHAP** when available; **Kernel SHAP** is a model-agnostic alternative that is usually slower. Positive attributions mean a **higher predicted target value**. Prefer **Test** or **External** for **Explain on** when judging which features matter on held-out data. There is no Class label control in Regression.

![Interpretability](../assets/reg/47.png)

--8<-- "_snippets/interpretability-usage.md"

Load the matching `.pkl` and feature CSVs for one pipeline, choose a method and **Explain on** split, then compute / prepare the explainer:

![Load files, method, and Prepare Explainer](../assets/reg/48.png)

SHAP session in progress — sample progress, global and local plot buttons (enabled when ready):

![SHAP session computing](../assets/reg/49.png)

## Methods

| Approach | What it shows | Scope |
|----------|---------------|--------|
| **SHAP** | How each feature pushes the predicted value up or down | All rows and single rows |
| **Kernel SHAP** | Same idea as SHAP, model-agnostic; usually slower | All rows and single rows |
| **LIME** | Local explanation for one row | Single rows (aggregated views available) |
| **Permutation Importance** | Drop in R² / MAE / … when a feature is shuffled | All rows |
| **PDP** | Average prediction as one or two features vary | All rows |
| **ICE** | One curve per row as a feature varies | Single rows |

SHAP summary (global feature impact):

![SHAP Summary Plot](../assets/reg/50.png)

SHAP heatmap across instances:

![SHAP Heatmap](../assets/reg/51.png)

SHAP decision plot:

![SHAP Decision Plot](../assets/reg/52.png)

SHAP dependence scatter of a feature:

![SHAP Dependence Scatter Plot](../assets/reg/53.png)

SHAP waterfall for one instance:

![SHAP Waterfall Plot](../assets/reg/54.png)

Kernel SHAP computing / plot controls:

![Kernel SHAP session](../assets/reg/55.png)

Kernel SHAP summary:

![Kernel SHAP Summary Plot](../assets/reg/56.png)

Kernel SHAP heatmap:

![Kernel SHAP Heatmap](../assets/reg/57.png)

LIME session ready — Feature Importance and Local Explanation:

![LIME method ready](../assets/reg/58.png)

LIME aggregated feature importance:

![LIME Feature Importance](../assets/reg/59.png)

LIME local explanation for one instance:

![LIME Local Explanation](../assets/reg/60.png)

Permutation Importance — choose scoring (R², MAE, RMSE, …):

![Permutation Importance scoring](../assets/reg/61.png)

Permutation Importance plot:

![Permutation Importance Plot](../assets/reg/62.png)

Partial Dependence Plot controls (primary / second feature):

![PDP method configuration](../assets/reg/63.png)

Two-feature PDP example:

![Two Feature PDP](../assets/reg/64.png)

ICE method and primary feature:

![ICE method configuration](../assets/reg/65.png)

ICE plot with average curve:

![ICE Plot](../assets/reg/66.png)

## Common mistakes

- Loading features from a different combination than the `.pkl`
- Treating Train explanations as validation
- Using Interpretability instead of Test metrics to pick a model
- Running Interpretability without a successful fitted `.pkl`
