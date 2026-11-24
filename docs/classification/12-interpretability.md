# Classification — Interpretability

**Where**: Classification → **Interpretability**

Explains a loaded fitted pipeline. It does **not** replace Test or External metrics for ranking.

![Interpretability](../assets/class/Class57.png)

--8<-- "_snippets/interpretability-usage.md"

Load the matching `.pkl` and feature CSVs for one pipeline, then **Prepare Explainer**:

![Load pipeline files](../assets/class/Class58.png)

Choose a method, set **Explain on** (for example Test), run **Prepare Explainer**, then open plot buttons when the session is ready:

![SHAP method and Prepare Explainer](../assets/class/Class59.png)

## Methods

| Approach | What it shows | Scope |
|----------|---------------|--------|
| **SHAP** | How much each feature pushes the predicted probability up or down | All rows and single rows |
| **Kernel SHAP** | ow much each feature pushes the predicted probability up or down | All rows and single rows |
| **LIME** | Which features drove one prediction, via a simple local model | Single rows (aggregated views available) |
| **Permutation Importance** | How much performance drops when a feature is shuffled | All rows |
| **Partial Dependence Plot (PDP)** | How the average prediction changes as one or two features vary | All rows (binary for PDP/ICE in Classification) |
| **ICE** | One curve per row as a feature varies | Single rows (binary for PDP/ICE in Classification) |

**Task note:** PDP/ICE are limited to **binary** classification in this mode. Multi-class may show a Class label control where needed.

SHAP summary (global feature impact):

![SHAP Summary Plot](../assets/class/Class60.png)

SHAP heatmap across instances:

![SHAP Heatmap](../assets/class/Class62.png)

SHAP decision plot for a selected instance:

![SHAP Decision Plot (local)](../assets/class/Class63.png)

Kernel SHAP summary:

![Kernel SHAP Summary Plot](../assets/class/Class64.png)

LIME aggregated feature importance:

![LIME Feature Importance (aggregated)](../assets/class/Class65.png)

LIME local explanation for one instance:

![LIME Local Explanation](../assets/class/Class66.png)

Permutation Importance on Test:

![Permutation Importance](../assets/class/Class67.png)

Partial Dependence Plot controls (primary / second feature, Two Feature PDP):

![PDP method configuration](../assets/class/Class68.png)

Two-feature PDP example:

![Two Feature PDP](../assets/class/Class69.png)

ICE method and primary feature:

![ICE method configuration](../assets/class/Class70.png)

ICE plot with average curve:

![ICE Plot](../assets/class/Class71.png)

Multi-class runs can expose a **Class label** control before preparing the explainer:

![Class label for multi-class SHAP](../assets/class/Class72.png)

## Common mistakes

- Loading CSVs from a different combination than the `.pkl`  
- Treating Train explanations as validation  
- Using Interpretability instead of Test metrics to pick a model  
- Running Interpretability without a successful fitted `.pkl`
