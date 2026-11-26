# Classification — Feature selection

Feature selection keeps the most useful original features and drops the rest. Unlike Dimensionality reduction, it doesn't create new features, so the selected ones stay interpretable. Each selected method is combined with each Dimensionality reduction method in the search, so the number of runs grows quickly. Feature selection is fit on the training data only (within each cross-validation fold) and then applied to Test and External data. For most methods, the main parameter can be set in the method's settings, for example the number of features to keep or the percentile.

![Feature Selection](../assets/class/Class24.png)

--8<-- "_snippets/feature-selection-classification.md"

![Feature Selection algorithms](../assets/class/Class25.png)

## Tips

- Keep **None** enabled if you want a full-feature baseline to compare against
- Set *k*, percentile, or max features in each method's settings before you start

## Common mistakes

- Turning off **None** when you still want a full-feature baseline
- Enabling Sequential Forward/Backward with a large feature budget on a first run
- Confusing this step with PCA (that is Dimensionality Reduction)
