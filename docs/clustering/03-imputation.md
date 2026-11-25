# Clustering — Imputation

Fills missing feature values including cells cleared by feature-level cleaning, so every searched pipeline has complete inputs for scaling, feature selection, dimensionality reduction, and clustering. Choose one or more imputers (Simple, KNN, Matrix Completion, Iterative, MissForest); only **Simple Imputation** exposes **More Configs** for the fill strategy (default **median**). Imputation is applied at **Start Procedure**. Enable only what you need because each extra imputer multiplies the search.

![Imputation](../assets/cluster/9.png)

--8<-- "_snippets/imputation.md"

**More Configs…** on Simple Imputation opens the strategy options (mean, median, most_frequent, constant):

![Simple Imputation More Configs](../assets/cluster/10.png)


## Common mistakes

- Checking every imputer with every scaler and model (product explosion)
- Assuming **mean** is the Simple Imputation default, QuadML default is **median**
- Feature-level cleaning without any imputer for the NaNs it creates
