# Survival Analysis — Imputation

**Where**: Survival Analysis → **Imputation**

Fills missing features for **covariate** pipelines.

**Task note:** Kaplan–Meier and Nelson–Aalen do not use imputation (`N/A` on Results).

![Imputation](../assets/sa/13.png)

--8<-- "_snippets/imputation.md"

## Common mistakes

- Checking every imputer with every scaler and model (product explosion)
- Assuming **mean** is the Simple Imputation default — QuadML default is **median**
- Feature-level cleaning without any imputer for the NaNs it creates
