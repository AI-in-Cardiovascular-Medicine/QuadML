# Classification — Feature selection

**Where**: Classification → **Feature Selection**

Chooses which **original** feature columns to keep for modeling—by ranking, filtering, or model-based pruning against the label—or keeps all of them (**None**). Unlike Dimensionality Reduction, it does not create new components; each selected method is crossed with DR in the search (FS × DR).

![Feature Selection](../assets/class/Class24.png)

--8<-- "_snippets/feature-selection.md"

**Classification note:** Supervised selectors (Select K Best, RFE, Boruta, Mutual Information, …) appear on this page.

Method cards and per-method settings (for example *k* or max features):

![Feature Selection algorithms](../assets/class/Class25.png)

**Unselect All** and the in-app warning about slow Sequential Forward/Backward search:

![Feature Selection Unselect All and SFS/SBS note](../assets/class/Class26.png)

## Common mistakes

- Turning off **None** when you still want a full-feature baseline
- Enabling SFS/SBS with a large feature budget on a smoke run
- Confusing this step with PCA (that is Dimensionality Reduction)
