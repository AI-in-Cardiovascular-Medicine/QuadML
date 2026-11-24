# Regression — Models

**Where**: Regression → **Regressors**

Choose regression models to search. Each checked model is crossed with every Imputation × Scaling × FS × DR combination you enabled.

![Regressors](../assets/reg/21.png)

## Models

| Model | How it works | Short code |
|-------|--------------|------------|
| Linear Regression | Fits a linear combination of features to the target | LinReg |
| Ridge Regression | Linear model with L2 shrinkage | Ridge |
| Lasso Regression | Linear model with L1 shrinkage (can zero coefficients) | Lasso |
| Elastic Net | Mix of L1 and L2 penalties | ENet |
| Decision Tree | Yes/no rules on features | DT |
| K-Nearest Neighbors | Predicts from similar training rows | KNN |
| Support Vector Regressor | Margin-based regression in feature space | SVR |
| Random Forest | Averages many decision trees | RF |
| Extra Trees | Like Random Forest with more random splits | ExTr |
| Bagging | Averages models on resampled data | Bag |
| AdaBoost | Sequential models focusing on hard rows | AdaB |
| Gradient Boosting | Sequential trees correcting previous errors | GB |
| XGBoost | Optimized, regularized gradient boosting | XGB |
| Multi-Layer Perceptron | Small neural network | MLP |
| Stacking | Combines several models with a final model | Stk |

**Tip:** For a first run, use **Linear Regression** and **Random Forest**. **Stacking** and **MLP** are much slower. Prefer scaling for linear models and SVR.

## Common mistakes

- Enabling every regressor plus every preprocessor  
- Linear / SVR pipelines with **None** scaling only on mixed-scale features  
