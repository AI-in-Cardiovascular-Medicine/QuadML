# Survival Analysis — Descriptive Analysis

**Where**: Survival Analysis → **Descriptive Analysis**

This page is **not** a data-summary screen. It selects **non-parametric** models that describe the cohort **without covariates**:

- **Kaplan–Meier (KM)** — survival curve for censored data
- **Nelson–Aalen (NeA)** — cumulative hazard

![Descriptive Analysis method cards](../assets/sa/25.png)

---

## What they do

| Model | Role |
|-------|------|
| **Kaplan-Meier** | Cohort \(S(t)\); median survival when defined |
| **Nelson-Aalen** | Cohort cumulative hazard \(H(t)\) |

You must select **at least one** model on this page **or** on **Survival Models** before **Start Procedure**. You can run KM / Nelson–Aalen alone, covariate models alone, or both.

Click **i** on a card for the in-app description.

---

## What they do not use

Kaplan–Meier and Nelson–Aalen do **not** use imputation, scaling, feature selection, or dimensionality reduction. On `Final_Results.csv` those steps show as `N/A (not used)`.

They also **cannot** be explained with SurvSHAP / SurvivalLIME / PDP — Interpretability will say methods are not available for descriptive models. Use **Visualization** for KM / Nelson–Aalen curves.

---

## What to click

1. Toggle **Kaplan-Meier** and/or **Nelson-Aalen**.
2. Continue to **Survival Models** if you also want covariate (predictive) models.

For a first run, enable **Kaplan-Meier** here plus **Cox Proportional Hazards** on Survival Models.
