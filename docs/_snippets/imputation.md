## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **Simple Imputation** | Replaces missing values with one value per feature (the median by default) | Basic, fast |
| **K-Nearest Neighbors Imputation** | Uses the values of the most similar samples | When missing values can be inferred from similar samples |
| **Matrix Completion** | Estimates missing values from patterns shared across all features | Many missing values spread over many features; can be slow |
| **Iterative Imputation** | Predicts each feature from the others, repeating until the estimates stabilize | Features that are related to each other; slower |
| **MissForest Imputation** | Like Iterative Imputation, but uses Random Forests, so it also captures nonlinear relations | Nonlinear relations between features; slowest |

Categorical features are converted to numbers before Imputation. Missing values in those columns are then filled like other numeric features. **Simple Imputation** defaults to **median**; choose **most_frequent** in More Configs if you want the most common value instead.
