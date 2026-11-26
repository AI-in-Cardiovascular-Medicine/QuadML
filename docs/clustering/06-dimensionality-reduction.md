# Clustering — Dimensionality reduction

Dimensionality reduction compresses the selected features into a smaller number of new features (components), each a combination of the original ones. It is applied after Feature selection, and each method is combined with each Feature selection method in the search. Selecting **None** keeps the original features. Dimensionality reduction is fit on the prepared clustering data (there is no Train/Test split). For most methods, the main parameter can be set in the method's settings, for example the number of components or explained variance. **LDA** is Classification only and does not appear here. If Feature Selection is **Laplacian Score**, DR is forced to **None** for that combination. Clustering has no Interpretability step.

![Dimensionality Reduction](../assets/cluster/18.png)

## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | Leaves the original features unchanged | Keep original features; required with Laplacian Score |
| **PCA** | Builds new features that capture as much shared variation as possible | Compress correlated numeric features |
| **ICA** | Builds new features that are as independent from each other as possible | Separating mixed signals |
| **Kernel PCA** | Like PCA, but can capture curved / nonlinear patterns | Nonlinear structure |

![Dimensionality Reduction algorithms](../assets/cluster/19.png)

## Tips

- Keep **None** enabled if you want original features (and when using Laplacian Score)
- Set component count, explained variance, or Kernel PCA kernel in each method's settings before you start

## Common mistakes

- Many DR methods without a **None** baseline
- Pairing **Laplacian Score** with PCA, ICA, or Kernel PCA
