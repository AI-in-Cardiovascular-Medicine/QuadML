# Regression — Scaling

Scaling puts features on comparable ranges, so that features with large values (e.g. cholesterol in mg/dL) don't outweigh features with small ones (e.g. creatinine in mg/dL). Models based on distances or coefficients (Linear Regression, Ridge, Lasso, Support Vector Regressor, K-Nearest Neighbors, Multi-Layer Perceptron) usually need it; tree-based models (Random Forest, XGBoost, etc.) work fine without it. It is fit on the training data only and then applied to Test (and External) data, so scale factors are not taken from the held-out sets. Enable only what you need because each extra scaler multiplies the search.

![Scaling](../assets/reg/13.png)

--8<-- "_snippets/scaling.md"

## Common mistakes

- Linear / SVM-style models with only **None** on mixed-scale features
- Selecting every scaler on the first run
- Forgetting **None** when you want a tree-model baseline
