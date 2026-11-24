# Survival Analysis — Scaling

**Where**: Survival Analysis → **Scaling**

Rescales features for covariate models. Cox / AFT often need scaling; some tree ensembles can use **None**.

**Task note:** KM / Nelson–Aalen do not use scaling (`N/A`).

![Scaling](../assets/sa/16.png)

--8<-- "_snippets/scaling.md"

## Common mistakes

- Linear / SVM-style models with only **None** on mixed-scale features
- Selecting every scaler on the first run
- Forgetting **None** when you want a tree-model baseline
