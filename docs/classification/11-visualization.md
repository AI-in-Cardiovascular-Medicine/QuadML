# Classification — Visualization

**Where**: Classification → **Visualization**

Charts for comparing pipelines and inspecting one selected pipeline. Load `Final_Results.csv` in **Results** first.

![Visualization](../assets/class/Class46.png)

--8<-- "_snippets/visualization-usage.md"

Choose **Single Pipeline** or **Pipelines Comparison**, pick a pipeline, and set **Results to display** (prefer **Test** or **External**):

![Single Pipeline and Results to display](../assets/class/Class47.png)

## Comparing pipelines

| Plot | What it shows |
|------|----------------|
| Single-metric plots | One metric across pipelines |
| Metrics comparison | Several metrics together |
| Heatmap | A metric for each combination of model and preprocessing |
| Performance distribution | How scores are spread across the search |
| Class distribution | How many rows are in each class |
| Calibration curve | Whether predicted probabilities match observed frequencies |
| Decision curve | Net benefit of using the model at different thresholds |

**Pipelines Comparison** offers Combined Plot / Side by Side, All Combinations actions, and Selected Pipelines:

![Pipelines Comparison controls](../assets/class/Class49.png)

Single-metric comparison (for example Accuracy across pipelines):

![Accuracy comparison chart](../assets/class/Class50.png)

Metrics comparison across selected pipelines:

![All metrics comparison](../assets/class/Class52.png)

Heatmap of one metric (model × dimensionality reduction):

![F1-score performance heatmap](../assets/class/Class51.png)

All-metrics heatmap:

![All metrics performance heatmap](../assets/class/Class55.png)

Combined ROC curves across pipelines:

![Combined ROC-AUC curves](../assets/class/Class54.png)

**Side by Side** confusion matrices:

![Side by Side confusion matrix](../assets/class/Class56.png)

## One pipeline

| Plot | What it shows |
|------|----------------|
| Confusion matrix | Correct and wrong predictions per class |
| ROC curve | Ranking quality at every threshold (binary) |
| Precision–recall curve | Performance when the positive class is rare |
| Probability distribution | How predicted probabilities are spread |
| Cumulative gains and lift | How much better than random the top-ranked rows are |
| Decision curve | Net benefit across thresholds |

ROC curve for a selected pipeline:

![ROC curve for one pipeline](../assets/class/Class53.png)

Calibration curves for a selected pipeline:

![Classification calibration curves](../assets/class/Class48.png)


## Common mistakes

- Opening Visualization before any successful combination finished
- Mixing plots from an older dated folder after starting a new run
- Reading Train-only plots as trustworthy absolute performance
