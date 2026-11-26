# Regression — Dimensionality reduction

Dimensionality reduction compresses the selected features into a smaller number of new features (components), each a combination of the original ones. It is applied after Feature selection, and each method is combined with each Feature selection method in the search. Because the components replace the original features, Interpretability then shows components instead of the original feature names. Selecting **None** keeps the original features. Dimensionality reduction is fit on the training data only (within each cross-validation fold) and then applied to Test and External data. For most methods, the main parameter can be set in the method's settings, for example the number of components or explained variance. **LDA** is Classification only and does not appear here.

![Dimensionality Reduction](../assets/reg/19.png)

--8<-- "_snippets/dimensionality-reduction.md"

![Dimensionality Reduction algorithms](../assets/reg/20.png)

## Tips

- Keep **None** enabled if you want Interpretability on original feature names
- Set component count, explained variance, or Kernel PCA kernel in each method's settings before you start

## Common mistakes

- Many DR methods without a **None** baseline
- Expecting Interpretability to show original feature names after PCA, ICA, or Kernel PCA
