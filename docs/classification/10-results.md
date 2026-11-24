# Classification — Metrics

**Where**: Classification → **Results**

Compare searched pipelines using Train / Test (or External) metrics. Prefer **Test** or **External** when choosing a model.

![Results](../assets/class/Class41.png)

--8<-- "_snippets/results-usage.md"

Browse or confirm `Final_Results.csv` for the output run folder, then filter pipelines and open details:

![Results file and pipeline filters](../assets/class/Class42.png)

## Metrics that use the decision threshold

These compare predicted classes with the true classes (binary threshold or multi-class argmax).

| Metric | What it means | Better |
|--------|---------------|--------|
| Accuracy | Share of rows classified correctly | Higher |
| Balanced Accuracy | Average of sensitivity and specificity; fairer when classes are imbalanced | Higher |
| Sensitivity (Recall) | Share of positive cases that are detected | Higher |
| Specificity | Share of negative cases correctly ruled out | Higher |
| Precision (PPV) | When the model predicts positive, how often it is right | Higher |
| NPV | When the model predicts negative, how often it is right | Higher |
| F1-score | Balance between precision and sensitivity | Higher |
| MCC | Correlation between predicted and true classes; robust to imbalance | Higher |
| Cohen's kappa | Agreement with the true classes beyond chance | Higher |

## Metrics that use predicted probabilities

These do not depend on the decision threshold.

| Metric | What it means | Better |
|--------|---------------|--------|
| ROC-AUC | How well the model ranks positives above negatives (0.5 = random, 1 = perfect) | Higher |
| PR-AUC | Like ROC-AUC, focused on the positive class; useful when it is rare | Higher |
| Brier score | Average error of the predicted probabilities | Lower |
| Log loss | Penalizes confident wrong predictions | Lower |
| ECE | Calibration error: predicted probabilities vs observed frequencies | Lower |

Open **Metric Explanations** in the app for full definitions. Large Train vs Test gaps often mean overfitting.

## Common mistakes

- Comparing runs from different Output Directory dated folders without noting File Selection changes
- Expecting Bootstrap CI columns when Bootstrap was off for that run
- Opening a `Final_Results.csv` from a different mode
- Picking by Train metrics while held-out scores are poor
