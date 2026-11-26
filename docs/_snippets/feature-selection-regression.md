## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | Keeps every feature as-is | Small feature counts; full-feature baseline |
| **Select K Best** | Keeps the *k* features that score highest against the numeric target | Fast first cut on wide data |
| **Select Percentile** | Keeps a percentage of the highest-scoring features | Relative budgets instead of a fixed *k* |
| **Recursive Feature Elimination** | Repeatedly drops the weakest features using a model | Model-aware pruning |
| **Select from Model** | Keeps features that a chosen model finds important | When you trust that model's importance scores |
| **Tree Based Feature Selection** | Keeps features important to a tree model | Tree-based importance |
| **Boruta** | Keeps features that matter more than random comparison copies | Exploratory “which features matter” |
| **Mutual Information** | Ranks features by how much information they share with the target, including nonlinear links | Nonlinear dependence |
| **Lasso** | Uses Lasso shrinkage so some feature weights become zero | Sparse linear selection |
| **Variance Threshold** | Drops features that barely change across samples | Near-constant columns |
| **Sequential Forward Selection** | Adds features one by one when they improve the model | Small feature counts only; can be very slow |
| **Sequential Backward Selection** | Removes features one by one when they hurt least | Small feature counts only; can be very slow |
