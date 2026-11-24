# Clustering — Search settings

**Where**: Clustering → **Search Settings**

Sets search budget and starts the run. Replaces Parameter Tuning in other modes. No Train/Test split, Bootstrap CI, or imbalance panel.

![Search Settings](../assets/cluster/27.png)

--8<-- "_snippets/search-run.md"

--8<-- "_snippets/start-stop-resources.md"

## How winners are chosen

| Model family | Hyperparameter selection |
|--------------|--------------------------|
| Centroid / hierarchical / Spectral / Birch | Average rank of Silhouette ↑, CH ↑, Davies–Bouldin ↓ |
| Gaussian Mixture Model | BIC (lower better) |
| DBSCAN / OPTICS / HDBSCAN | Validity filters → **DISCO** (higher better); DBCV reported only |

There is **no** automatic best model across paradigms — compare sizes, noise, DISCO / BIC, and domain knowledge.

**Tip:** Check the configuration tree before Start. Use **Fast** for a first run.

## Common mistakes

- Starting with every method checked — combination count is a product
- Ignoring Resource Usage on large searches
- Changing File Selection roles after configuring without re-checking the tree
- Closing the app instead of **Stop**
- Setting CPU/RAM to 100% on a machine you still need for other work
- Starting again without noticing a new dated folder was created
