# Clustering — Visualization

Shows cluster geometry, parameter-choice curves, quality diagnostics, and segment profiling for pipelines you already scored on **Results**. Load `Final_Results.csv` in **Results** first, then open **Visualization** and choose **Single Pipeline** (one configuration), **Pipelines Comparison** (the same plot across combinations), or **Plot Analyzer**. There is **no** Interpretability page in Clustering. Use profiling plots here. Live *k* / eps / density overrides apply on **Single Pipeline** only. Plot buttons depend on the selected clustering model. Use **Plot Explanations** and **Analyze** for in-app help.

![Visualization](../assets/cluster/36.png)

--8<-- "_snippets/visualization-usage.md"

Choose **Single Pipeline**, **Pipelines Comparison**, or **Plot Analyzer**:

![Visualization mode tabs](../assets/cluster/37.png)

**Plot Explanations** covers how to read scatter plots, silhouette views, and profiles:

![Plot Explanations](../assets/cluster/38.png)

**Single Pipeline** — pick a combination, then open a plot group:

![Single Pipeline plot groups](../assets/cluster/39.png)

## Cluster visualization

| Plot | What it shows |
|------|----------------|
| Feature Space | Scatter in clustering feature space |
| Reduced Components | Colours in PCA / ICA / Kernel PCA space |
| t-SNE / UMAP | Exploratory embeddings (UMAP needs `umap-learn`) |

Feature Space scatter (points coloured by cluster):

![Feature Space](../assets/cluster/40.png)

t-SNE scatter (exploratory; clustering was not run in this projection):

![t-SNE Scatter Plot](../assets/cluster/41.png)

UMAP scatter with density-model noise and live parameter sliders:

![UMAP Scatter Plot](../assets/cluster/42.png)

## Parameter selection

| Plot | What it shows |
|------|----------------|
| Elbow / CH / DB vs *k* | Help choose *k* for count-based models |
| GMM BIC / AIC | GMM component choice |
| Dendrogram | Agglomerative hierarchy |
| k-Distance / Density Parameter | DBSCAN / OPTICS / HDBSCAN parameter views |
| OPTICS Reachability / HDBSCAN Condensed Tree | Density structure |

Elbow (inertia vs *k*):

![Elbow Plot](../assets/cluster/43.png)

Calinski–Harabasz vs *k*:

![Calinski-Harabasz Plot](../assets/cluster/44.png)

Davies–Bouldin vs *k*:

![Davies-Bouldin Plot](../assets/cluster/45.png)

Dendrogram (Agglomerative):

![Dendrogram](../assets/cluster/46.png)

Density parameter dependence (for example HDBSCAN `min_cluster_size`):

![Density Parameter Plot](../assets/cluster/47.png)

HDBSCAN Condensed Tree:

![HDBSCAN Condensed Tree](../assets/cluster/48.png)

## Quality and profiling

| Plot | What it shows |
|------|----------------|
| Silhouette histogram / knife | Per-point and per-cluster silhouette |
| Core / Border / Noise | Density roles (density models) |
| Cluster sizes / profile heatmap | Size bars; z-scored feature profiles |
| Sample clustered heatmap | Sample × feature view ordered by cluster |
| Parallel coordinates / box / violin | Feature patterns by cluster |
| Volcano | Cohen’s *d* vs FDR (not log2 fold change) |

Silhouette knife:

![Silhouette Knife Plot](../assets/cluster/49.png)

Silhouette histogram:

![Silhouette Histogram](../assets/cluster/50.png)

Core / Border / Noise:

![Core Border Noise](../assets/cluster/51.png)

Cluster sizes:

![Cluster Sizes](../assets/cluster/52.png)

Feature box plots:

![Feature Box Plot](../assets/cluster/53.png)

Feature violin plots:

![Feature Violin Plot](../assets/cluster/54.png)

Cluster profile heatmap:

![Cluster Profile Heatmap](../assets/cluster/55.png)

Sample clustered heatmap:

![Sample Clustered Heatmap](../assets/cluster/56.png)

## Comparing pipelines

**Pipelines Comparison** — add combinations, then open a plot (buttons depend on the model):

![Pipelines Comparison](../assets/cluster/57.png)

Activated plot buttons after combinations are added:

![Pipelines Comparison plot buttons](../assets/cluster/58.png)

## Plot Analyzer

**Plot Analyzer** adds a plain-language reading next to the chart:

![Plot Analyzer](../assets/cluster/59.png)

Use **Plot Explanations** / **Analyze** for in-app help. Export plot and **Export Cluster Assignments** from plot windows when needed.

## Common mistakes

- Opening Visualization before any successful combination finished
- Mixing plots from an older dated folder after starting a new run
- Treating t-SNE / UMAP layout as the space the algorithm clustered in
- Expecting every plot button for every model (availability is model-dependent)
