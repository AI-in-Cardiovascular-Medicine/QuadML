# Survival Analysis — Descriptive analysis

**Where**: Survival Analysis → **Descriptive Analysis**

Non-parametric **cohort** models **without covariates**. Not a data-summary screen.

![Descriptive Analysis](../assets/sa/25.png)

## Methods

| Model | What it does | When to use it |
|-------|--------------|----------------|
| **Kaplan-Meier** | Cohort survival \(S(t)\); median survival when defined | Baseline survival curve |
| **Nelson-Aalen** | Cohort cumulative hazard \(H(t)\) | Cumulative hazard view |

You must select at least one model here **or** on Survival Models before Start. You can run descriptive only, covariate only, or both.

**They do not use** imputation, scaling, FS, or DR (`N/A` on Results). They have **no** Interpretability — use Visualization for curves.

## Common mistakes

- Looking for KM on the Survival Models page  
- Expecting SurvSHAP for descriptive models  
