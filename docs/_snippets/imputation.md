## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **Simple Imputation** | Fills each column with a constant strategy (default **median**) | First runs; mostly numeric data |
| **K-Nearest Neighbors Imputation** | Fills from similar rows | Missingness that depends on other features |
| **Matrix Completion** | Recovers a low-rank matrix (SoftImpute-style) | Wider missing patterns; can be slow |
| **Iterative Imputation** | Models each feature from the others in turn | Complex missingness; more compute |
| **MissForest Imputation** | Iterative fill with a lightweight Random Forest | Nonlinear relations; more compute |

