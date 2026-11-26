# Clustering — Search settings

Sets how QuadML searches the combinations you selected, then starts the run with **Start Procedure**. **Search Settings** replaces Parameter Tuning in other modes. There is no Train/Test split, Bootstrap CI panel, imbalance panel, or CV fold control here, Clustering evaluates unsupervised metrics on the prepared data.

![Search Settings](../assets/cluster/27.png)

## Settings

| Setting | What it does |
|---------|--------------|
| **Search Budget** | **Fast** / **Balanced** / **Thorough** — how rich the search is (does not uncheck methods) |
| **CPU % / RAM %** | Resource limits (defaults often **50 / 50**) |

![Search Budget and resources](../assets/cluster/28.png)

## Running the search

**Start Procedure** checks that a run is not already active and that the input and Output Directory are set, then creates a new dated folder and launches the search. **Stop Procedure** cancels the run; partial results may remain, and **Rebuild Results** can rebuild `Final_Results.csv` from finished combo files when possible. Only one search can run at a time across modes.

![Start, Stop, and Rebuild](../assets/cluster/29.png)

## How winners are chosen

| Model family | Hyperparameter selection |
|--------------|--------------------------|
| Centroid / hierarchical / Spectral / Birch | Average rank of Silhouette ↑, CH ↑, Davies–Bouldin ↓ |
| Gaussian Mixture Model | BIC (lower better) |
| DBSCAN / OPTICS / HDBSCAN | Validity filters → **DISCO** (higher better); DBCV reported only |

There is **no** automatic best model across paradigms, compare sizes, noise, DISCO / BIC, and domain knowledge.

## Tips

- Check the configuration tree before Start 
- Combination count is the product of every checked option
- Prefer **Fast** for a first run
- Prefer **Stop Procedure** over closing the app

## Common mistakes

- Starting with every method checked
- Ignoring Resource Usage on large searches
- Setting CPU/RAM to 100% on a machine you still need for other work
- Starting again without noticing a new dated folder was created
