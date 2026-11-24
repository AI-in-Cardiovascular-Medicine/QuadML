# Classification — Scaling

**Where**: Classification → **Scaling**

Rescales features before Feature Selection, Dimensionality Reduction, and the classifier. Linear models and SVC usually need scaling; many trees work with **None**.

![Scaling](../assets/class/Class21.png)

--8<-- "_snippets/scaling.md"

A common first-run pair is **None** + **Standard Scaler**:

![None and Standard Scaler selected](../assets/class/Class22.png)

**Unselect All** clears every scaler before you pick a smaller set:

![Scaling method toggles](../assets/class/Class23.png)

## Common mistakes

- Linear / SVM-style models with only **None** on mixed-scale features
- Selecting every scaler on the first run
- Forgetting **None** when you want a tree-model baseline
