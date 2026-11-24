# Survival Analysis — Metrics

**Where**: Survival Analysis → **Results**

Compare searched pipelines using Train / Test (or External) metrics. Prefer **Test** or **External**.

![Results](../assets/sa/34.png)

--8<-- "_snippets/results-usage.md"

## Discrimination (higher is better)

| Metric | What it means | Better |
|--------|---------------|--------|
| C-index | Concordance of predicted risk with observed order | Higher |
| td-AUC | Time-dependent AUC at evaluation horizons | Higher |
| Integrated AUC | Summary of td-AUC over time (when reported) | Higher |

## Calibration / error (context-dependent)

| Metric | What it means | Better |
|--------|---------------|--------|
| IBS | Integrated Brier score of predicted survival | Lower |
| Mean Calibration | Average predicted vs observed event rate | Near **1** |
| Calibration Slope | Slope of predicted vs observed risk | Near **1** |
| ICI | Integrated calibration index | Lower |

## Cohort / descriptive rows

| Metric / flag | What it means |
|---------------|----------------|
| N/A preprocess | KM / Nelson–Aalen skip imputation, scaling, FS, DR |
| Cohort comparison p-values | Train vs Test balance checks (when shown) |

When absolute risk matters: prefer calibration (**Mean Cal**, **Slope**, **ICI**) first, then Test C-index / td-AUC among well-calibrated rows. Do not rank by C-index alone. Open **Metric Explanations** in the app for full definitions.

## Common mistakes

- Comparing runs from different Output Directory dated folders without noting File Selection changes
- Expecting Bootstrap CI columns when Bootstrap was off for that run
- Opening a `Final_Results.csv` from a different mode
- Picking by Train metrics while held-out scores are poor
