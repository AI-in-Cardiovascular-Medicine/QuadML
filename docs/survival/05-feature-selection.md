# Survival Analysis — Feature selection

**Where**: Survival Analysis → **Feature Selection**

**Task note:** Survival uses a **restricted allowlist** (Cox-based scoring, Cox-LASSO, Boruta, …). KM / Nelson–Aalen skip this step.

![Feature Selection](../assets/sa/19.png)

--8<-- "_snippets/feature-selection.md"

## Common mistakes

- Turning off **None** when you still want a full-feature baseline
- Enabling SFS/SBS with a large feature budget on a smoke run
- Confusing this step with PCA (that is Dimensionality Reduction)
