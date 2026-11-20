# Shared — Imputation

**Where**: Any mode → **Imputation**

Select **one or more** imputation methods. Each checked method enters the combinatorial search product with scalers, feature selectors, models, and (where available) dimensionality reduction.

---

## What to click

1. Toggle individual method cards, or use **Select All** / **Unselect All** when offered.
2. Open a method’s **i** / summary on the card when present.
3. Use **More Configs** when a method exposes parameters (Simple Imputation strategies, etc.).
4. Leave at least one method checked before **Start Procedure** (commonly **Simple Imputation**).

**Simple Imputation** default strategy in QuadML is **median** (not mean).

Click **?** on the step or cards for in-app wording.

---

## Search product

Imputation methods multiply with every other checked stage. Prefer a short list for first runs. Survival descriptive models (KM / Nelson–Aalen) do not use imputation (`N/A` on Results).

---

## Common mistakes

- Checking every imputer on a large model list (product explosion)
- Feature-Level cleaning without any imputer for introduced NaNs
- Assuming **mean** is the Simple Imputation default

---

## Mode manuals

- [Classification — Imputation](../classification/03-imputation.md)
- [Regression — Imputation](../regression/03-imputation.md)
- [Survival — Imputation](../survival/03-imputation.md)
- [Clustering — Imputation](../clustering/03-imputation.md)
