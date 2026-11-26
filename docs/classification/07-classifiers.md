# Classification — Classifiers

This step picks the **classification algorithms** that map features to class labels. Each checked classifier is trained and evaluated as part of the search; hyperparameters for those models are explored later on **Parameter Tuning**, not typed by hand here.

Every selected classifier is crossed with every Imputation × Scaling × Feature Selection × Dimensionality Reduction combination you enabled earlier, so the total number of pipelines is a product of those choices.

![Classifiers](../assets/class/Class29.png)

## Classifiers

| Classifier | How it works | Short code |
|------------|--------------|------------|
| **Logistic Regression** | Linear model of the probability of the outcome | LR |
| **Lasso Regression** | Logistic regression that shrinks some coefficients to zero | LASSO LR |
| **Elastic Net** | Logistic regression with a mix of Lasso and Ridge penalties | ENet |
| **Decision Tree** | A series of yes/no rules on the features | DT |
| **K-Nearest Neighbors** | Predicts from the most similar rows in the training data | KNN |
| **Support Vector Classifier** | Finds the boundary that best separates the classes | SVC |
| **Random Forest** | Averages many decision trees on random subsets | RF |
| **Extra Trees** | Like Random Forest, with more randomly chosen splits | ExTr |
| **Bagging** | Averages many copies of a model on resampled data | Bag |
| **AdaBoost** | Builds models one after another, focusing on mistakes | AdaB |
| **Gradient Boosting** | Builds trees sequentially, each correcting previous errors | GB |
| **XGBoost** | Optimized, regularized gradient boosting | XGB |
| **Naive Bayes** | Uses probabilities, assuming features are independent | NB |
| **Multi-Layer Perceptron** | A small neural network | MLP |
| **Stacking** | Combines several models with a final model | Stk |

**Tip:** Runtime grows with every option selected. **Stacking** and **Multi-Layer Perceptron** are much slower.

## Common mistakes

- Enabling every classifier plus every imputer / scaler / FS / DR method
- Expecting Stacking or MLP to finish as fast as Logistic Regression
