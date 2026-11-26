# Classification — Metrics

Shows Train / Test (or External) scores for every searched pipeline after **Start Procedure** (or **Rebuild Results**). Load `Final_Results.csv` from the output run folder, then filter by cleaning, imputation, scaling, feature selection, dimensionality reduction, and classifier. You see metrics that use the predicted class (**Accuracy**, **Balanced Accuracy**, **Sensitivity**, **Specificity**, **Precision**, **NPV**, **F1**, **MCC**, **Cohen's kappa**) and metrics that use predicted probabilities (**ROC-AUC**, **PR-AUC**, **Brier**, **Log loss**, **ECE**). For two-class problems, the Decision Threshold from Parameter Tuning turns probabilities into a class before those first metrics are scored; multi-class picks the class with the highest probability. Prefer held-out **Test** or **External** scores when choosing a model; check ranking quality (ROC-AUC / PR-AUC) together with how the model behaves at your threshold—do not pick by Accuracy alone when classes are imbalanced. Open **Metric Explanations** in the app for full definitions.

![Results](../assets/class/Class41.png)

--8<-- "_snippets/results-usage.md"

Browse or confirm `Final_Results.csv` for the output run folder, then filter pipelines and open Train / Test / External metrics:

![Results file and pipeline filters](../assets/class/Class42.png)

**Compare All Pipelines (table)** ranks configurations by CV score (Test metrics are for reference):

![Compare All Pipelines table](../assets/class/Class44.png)

**Detailed Report** opens the full CSV-style metric view for a pipeline:

![Detailed Report](../assets/class/Class45.png)

## Metrics that use the predicted class

These compare the class the model predicts with the true class. For two-class problems they use the Decision Threshold; for multi-class they use the class with the highest probability.

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

These do not depend on the Decision Threshold.

| Metric | What it means | Better |
|--------|---------------|--------|
| ROC-AUC | How well the model ranks positives above negatives (0.5 = random, 1 = perfect) | Higher |
| PR-AUC | Like ROC-AUC, focused on the positive class; useful when it is rare | Higher |
| Brier score | Average error of the predicted probabilities | Lower |
| Log loss | Penalizes confident wrong predictions | Lower |
| ECE | Calibration error: predicted probabilities vs observed frequencies | Lower |

Prefer held-out **Test** / **External** scores; large Train vs Test gaps often mean overfitting. On imbalanced data, prefer Balanced Accuracy / MCC / PR-AUC over Accuracy alone. Open **Metric Explanations** in the app for full definitions.

## Common mistakes

- Comparing runs from different Output Directory dated folders without noting File Selection changes
- Expecting Bootstrap CI columns when Bootstrap was off for that run
- Opening a `Final_Results.csv` from a different mode
- Picking by Train metrics while held-out scores are poor
