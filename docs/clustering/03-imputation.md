# Clustering — Imputation

**Where**: Clustering → **Imputation**

Fills missing features so every searched pipeline has complete inputs for scaling and clustering.

![Imputation](../assets/cluster/9.png)

--8<-- "_snippets/imputation.md"

## Common mistakes

- Checking every imputer with every scaler and model (product explosion)
- Assuming **mean** is the Simple Imputation default — QuadML default is **median**
- Feature-level cleaning without any imputer for the NaNs it creates
