# Survival Analysis — Models

**Where**: Survival Analysis → **Survival Models**

Covariate (predictive) models that use features plus duration/event. Kaplan–Meier and Nelson–Aalen are on **Descriptive Analysis**, not here.

Each checked model is crossed with every Imputation × Scaling × FS × DR combination you enabled.

![Survival Models](../assets/sa/26.png)

## Models

| Model | How it works | Short code |
|-------|--------------|------------|
| Cox Proportional Hazards | Semi-parametric hazard model with covariates | CoxPH |
| Weibull AFT | Parametric accelerated failure time (Weibull) | WbAFT |
| Log-Normal AFT | Parametric AFT with log-normal errors | LNAFT |
| Log-Logistic AFT | Parametric AFT with log-logistic errors | LLAFT |
| Random Survival Forest | Forest of survival trees | RSF |
| Extra Survival Trees | Extremely randomized survival trees | EST |
| Survival Gradient Boosting | Boosted trees for survival | SGBM |
| Survival Support Vector Machine | Ranking-oriented SVM (no \(S(t)\)) | SSVM |
| DeepSurv | Neural Cox-style model | DeepSurv |

**Tip:** First run: **Cox Proportional Hazards** (+ **Kaplan-Meier** on Descriptive). **RSF / EST / SGBM / SSVM** can write very large `.pkl` files. **DeepSurv** is slower.

## Common mistakes

- Enabling every ML model on a large cohort for a first run  
- Looking for KM on this page (it is on Descriptive Analysis)  
- Ignoring disk space for RSF / SSVM / SGBM  
