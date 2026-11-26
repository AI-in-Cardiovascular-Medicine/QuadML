# Regression — Imputation

Imputation fills in missing values, including those created by Data cleaning, so that every model receives a complete dataset. It is fit on the training data only and then applied to Test (and External) data, so fill values are not taken from the held-out sets. Enable only what you need because each extra imputer multiplies the search.

![Imputation](../assets/reg/10.png)

--8<-- "_snippets/imputation.md"

**More Configs…** on Simple Imputation opens the strategy options (for example constant fill):

![Simple Imputation More Configs](../assets/reg/11.png)

## Common mistakes

- Assuming **mean** is the Simple Imputation default while QuadML default is **median**
- Feature-level cleaning without any imputer for the missing values it creates
