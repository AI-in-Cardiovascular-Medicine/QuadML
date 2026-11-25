# Survival Analysis — Feature selection

Chooses which **original** feature columns to keep for searched **covariate** pipelines by ranking, filtering, or model-based pruning against the survival outcome or keeps all of them (**None**). Unlike Dimensionality Reduction, it does not create new components; each selected method is crossed with DR in the search (FS × DR). Survival uses a **restricted allowlist** of methods suited to time-to-event data (for example Cox-based scoring, Cox-LASSO, Boruta). Prefer **None** when the feature count is small; enable only what you need because each extra method multiplies the search. Kaplan–Meier and Nelson–Aalen do not use Feature Selection (`N/A` on Results).

![Feature Selection](../assets/sa/19.png)

--8<-- "_snippets/feature-selection.md"

Method cards and per-method settings (for example *k* or max features):

![Feature Selection algorithms](../assets/sa/20.png)

## Common mistakes

- Turning off **None** when you still want a full-feature baseline
- Enabling SFS/SBS with a large feature budget on a smoke run
- Confusing this step with PCA (that is Dimensionality Reduction)
