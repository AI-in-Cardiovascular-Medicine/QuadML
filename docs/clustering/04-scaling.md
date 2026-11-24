# Clustering — Scaling

**Where**: Clustering → **Scaling**

Rescales features before FS, DR, and clustering. Distance-based methods (**K-Means**, **DBSCAN**, …) usually need scaling.

![Scaling](../assets/cluster/12.png)

--8<-- "_snippets/scaling.md"

**Task note:** Clustering omits **Quantile Transformer** and **Normalizer**. **None** (no scaling) is available.

## Common mistakes

- Linear / SVM-style models with only **None** on mixed-scale features
- Selecting every scaler on the first run
- Forgetting **None** when you want a tree-model baseline
