
## Typical methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | Keeps every eligible feature | Small/medium feature counts; baseline |
| **Select K Best** | Top *k* by univariate score | Fast filter; first cut on wide data |
| **Select Percentile** | Top percentage by score | Relative budgets instead of fixed *k* |
| **Recursive Feature Elimination** | Iteratively drops weakest features | When you want model-aware pruning |
| **Select from Model** | Keeps features important to a model | Embedded importance |
| **Boruta** | All-relevant selection vs shadow features | Exploratory “which features matter” |
| **Mutual Information** | Ranks by MI with the outcome | Nonlinear dependence (supervised modes) |
| **Lasso / Cox-LASSO** | Shrinkage-based selection | Sparse linear / survival models |
| **Variance Threshold** | Drops near-constant features | Unsupervised / clustering |
| **Sequential Forward/Backward** | Greedy add/remove | Small *k* only can be very slow |

**Point:** Prefer **None** if the number of features are few or a fast filter on first runs. SFS/SBS can dominate runtime.
