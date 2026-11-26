# Survival Analysis — Imputation

Imputation fills in missing values, including those created by Data cleaning, so that every model receives a complete dataset. It is fit on the training data only and then applied to Test (and External) data, so fill values are not taken from the held-out sets. Choose one or more imputers (Simple, KNN, Matrix Completion, Iterative, MissForest); only **Simple Imputation** exposes **More Configs** for the fill strategy (default **median**). Enable only what you need because each extra imputer multiplies the search. Kaplan–Meier and Nelson–Aalen do not use imputation (`N/A` on Results).

![Imputation](../assets/sa/13.png)

--8<-- "_snippets/imputation.md"

## Common mistakes

- Assuming **mean** is the Simple Imputation default while QuadML default is **median**
- Feature-level cleaning without any imputer for the missing values it creates
