> A technique that stops a model from overfitting by discouraging it from becoming too complex.

---

## 1. The Big Idea

An overfit model usually has **very large weights**. To match every wiggle and every bit of noise in the training data, it has to twist itself, and twisting requires large coefficients.

**Regularization** adds a **penalty for large weights** to the cost function. The model now has two goals: fit the data well, and keep the weights small. The result is a simpler, smoother model that generalizes better.

**Analogy (the budget):** A manager who can hire unlimited specialists builds a team that fits today's problem perfectly but collapses when anything changes. A manager with a **budget** must hire only the people who really matter. Regularization is the budget for a model.

In bias-variance terms: regularization accepts a **small increase in bias** in return for a **large decrease in variance**, which lowers the total error.

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Regularization** | Adding a penalty on the size of the weights to the cost function to reduce overfitting. | A budget on model complexity. |
| **Penalty term** | The extra amount added to the cost, based on the weights. | The price of large weights. |
| **Alpha (α)** | The strength of the penalty. Also written λ (lambda). | How strict the budget is. |
| **L2 penalty** | The sum of the **squared** weights. | Punishes big weights heavily. |
| **L1 penalty** | The sum of the **absolute** weights. | Punishes all weights equally. |
| **Ridge regression** | Linear regression with an L2 penalty. | Shrinks all weights. |
| **Lasso regression** | Linear regression with an L1 penalty. | Shrinks weights and can remove features. |
| **Shrinkage** | Pulling weights closer to zero. | Making the model more modest. |
| **Sparse model** | A model in which many weights are exactly zero. | Uses only a few features. |
| **Feature selection** | Choosing which features to keep. | Dropping useless clues. |
| **Hyperparameter** | A setting you choose, not one the model learns (alpha is one). | A dial you set yourself. |

---

## 3. The Idea in Formulas

Start from the usual cost (MSE) for linear regression:

```
J = MSE = (1/n) · Σ (ŷ − y)²
```

### Ridge (L2)

```
J_ridge = MSE + α · (w₁² + w₂² + ... + wₘ²)
```

### Lasso (L1)

```
J_lasso = MSE + α · (|w₁| + |w₂| + ... + |wₘ|)
```

**Points to remember:**
- The **bias term `b` is not penalized**. Only the weights are.
- `α = 0` means no penalty (ordinary linear regression).
- A larger `α` means stronger shrinkage.
- Libraries scale the cost slightly differently (scikit-learn divides the MSE part by 2 in Lasso, for example), so the same `α` can give slightly different results across tools. The idea is identical.

### The effect on alpha

| Alpha | Effect | Risk |
|---|---|---|
| **0** | No penalty, plain model | Overfitting |
| **Small** | Gentle shrinkage | Slight reduction in variance |
| **Large** | Strong shrinkage, weights near zero | **Underfitting** |

---

## 4. Ridge Regression (L2)

### Concept

Ridge shrinks **all weights toward zero**, with the largest weights shrunk the most (because the penalty uses squares). It almost never makes a weight **exactly** zero.

### Why it is also called "weight decay"

Add the penalty's gradient (`2αw`) to the usual gradient descent update:

```
w_new = w · (1 − 2ηα) − η · (gradient of MSE)
```

(Here η is the learning rate.) The first part multiplies the weight by a number slightly below 1 at every step, so the weight **decays** toward zero unless the data pushes back.

### Strengths

- Handles **correlated features** gracefully by sharing the weight among them.
- Stable and smooth, with a clean closed-form solution.
- A good default when most features carry some information.

### Limit

It keeps **all** features, so it does not simplify the model by removing any.

---

## 5. Lasso Regression (L1)

### Concept

Lasso also shrinks weights, but it subtracts a **constant amount** from each, so weak weights hit **exactly zero** and drop out of the model. That makes Lasso a built-in **feature selector**.

### Why exact zeros happen

- The L2 penalty's pull weakens as a weight gets small (the gradient `2αw` shrinks with `w`), so it never quite reaches zero.
- The L1 penalty's pull stays **the same size** (`α`) no matter how small the weight is, so it can push a small weight all the way to zero.

**Geometric picture:** the L1 constraint region is a diamond with corners on the axes, and the best solution tends to land on a corner, where some weights are zero. The L2 region is a circle with no corners.

### Strengths

- Produces **sparse, simpler, more interpretable** models.
- Useful when you suspect many features are irrelevant.

### Limits

- Among **correlated features**, it tends to keep one and drop the others somewhat arbitrarily.
- With more features than rows, it can keep at most as many features as there are rows.

---

## 6. Worked Example: One Weight

To see the difference clearly, use a one-weight model with the cost `(w − 3)²`. Without a penalty, the best weight is `w = 3`.

**Ridge:** `J = (w − 3)² + α·w²`. Setting the derivative to zero gives `w = 3 / (1 + α)`.

**Lasso:** `J = (w − 3)² + α·|w|`. For `w > 0`, setting the derivative to zero gives `w = 3 − α/2`. The optimum is exactly `0` once `α ≥ 6`.

| Alpha | Ridge weight `3/(1+α)` | Lasso weight `max(0, 3 − α/2)` |
|---|---|---|
| 0 | 3.00 | 3.00 |
| 1 | 1.50 | 2.50 |
| 2 | 1.00 | 2.00 |
| 4 | 0.60 | 1.00 |
| 6 | 0.43 | **0.00** |
| 10 | 0.27 | **0.00** |

**What this shows:**
- **Ridge** shrinks the weight smoothly and proportionally. It gets small but **never exactly zero**.
- **Lasso** subtracts a fixed amount, and once `α` is large enough the weight becomes **exactly zero** (the feature is removed).

### Illustrative multi-feature picture

Coefficients for five features of the same dataset (made-up numbers to illustrate the pattern):

| Feature | No penalty | Ridge | Lasso |
|---|---|---|---|
| x₁ | 8.2 | 5.4 | 6.0 |
| x₂ | −6.5 | −4.1 | −4.5 |
| x₃ | 3.1 | 2.6 | 2.2 |
| x₄ | 0.9 | 0.7 | **0** |
| x₅ | −0.7 | −0.5 | **0** |

Ridge pulls every coefficient in. Lasso removes the two weakest features entirely.

---

## 7. Ridge vs Lasso

| | Ridge (L2) | Lasso (L1) |
|---|---|---|
| **Penalty** | Sum of squared weights | Sum of absolute weights |
| **Effect on weights** | Shrinks all, rarely to exactly zero | Shrinks some to **exactly zero** |
| **Feature selection** | No | **Yes** |
| **Correlated features** | Shares weight among them (handles well) | Picks one, drops others |
| **Model** | Dense (uses all features) | Sparse (uses few features) |
| **Best when** | Most features are useful | Many features are likely useless |
| **scikit-learn** | `Ridge`, `RidgeCV` | `Lasso`, `LassoCV` |

### Elastic Net (the blend)

**Elastic Net** combines both penalties, so you get some feature selection from L1 and the stability with correlated features from L2. It has two settings: `alpha` (overall strength) and `l1_ratio` (the mix of L1 vs L2). It is a good choice when features are correlated **and** you suspect many are useless.

---

## 8. Practical Rules

### 1. Scale your features first

The penalty depends on the **size** of the weights, and the size of a weight depends on the **scale** of its feature. Without scaling, a feature measured in thousands gets a tiny weight and is barely penalized, while a feature measured in fractions gets a large weight and is penalized heavily, which is unfair. Always apply `StandardScaler` before Ridge or Lasso.

### 2. Choose alpha with cross-validation

Alpha is a hyperparameter. Try a range of values (for example `0.001, 0.01, 0.1, 1, 10, 100`) and pick the one with the best cross-validation score. scikit-learn's `RidgeCV` and `LassoCV` do this for you.

### 3. Do not penalize the intercept

Libraries handle this automatically.

### 4. Use a pipeline

Putting the scaler and the model in a `Pipeline` keeps the scaler fitted only on training data, which avoids data leakage during cross-validation.

---

## 9. In Code

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Ridge: scale, then choose alpha by 5-fold cross-validation
ridge = make_pipeline(
    StandardScaler(),
    RidgeCV(alphas=[0.01, 0.1, 1, 10, 100], cv=5)
)
ridge.fit(X_train, y_train)

# Lasso: scale, then choose alpha by 5-fold cross-validation
lasso = make_pipeline(
    StandardScaler(),
    LassoCV(cv=5, random_state=42)
)
lasso.fit(X_train, y_train)

print("Ridge R² (test):", ridge.score(X_test, y_test))
print("Lasso R² (test):", lasso.score(X_test, y_test))

# Inspect what was learned
ridge_model = ridge.named_steps["ridgecv"]
lasso_model = lasso.named_steps["lassocv"]

print("Best Ridge alpha:", ridge_model.alpha_)
print("Best Lasso alpha:", lasso_model.alpha_)
print("Features removed by Lasso:", np.sum(lasso_model.coef_ == 0))
```

**Experiment:** compare these scores with plain `LinearRegression`. On data with many features and little training data, the regularized models usually score better on the test set.

---

## 10. Regularization Beyond Linear Models

The same idea (restrain the model's flexibility) appears throughout machine learning:

| Model | How it is regularized |
|---|---|
| **Logistic Regression** | L2 penalty by default. In scikit-learn, `C` is the **inverse** of the strength (smaller `C` means stronger regularization). |
| **SVM** | `C` controls the tradeoff between a wide margin and training errors. |
| **Decision Tree** | Limit `max_depth`, `min_samples_leaf`, or prune. |
| **Random Forest / XGBoost** | Limit depth, learning rate, number of trees. XGBoost also has explicit L1 and L2 penalty settings (`reg_alpha`, `reg_lambda`). |
| **Neural Networks** | Weight decay, dropout, early stopping. |

---

## 11. Common Mistakes

| Mistake | Why it hurts | Fix |
|---|---|---|
| Not scaling features | Penalty is applied unfairly across features | Use `StandardScaler` in a pipeline |
| Picking alpha by guessing or on the test set | Poor or dishonest result | Use cross-validation (`RidgeCV`, `LassoCV`) |
| Setting alpha too high | Weights shrink too much, **underfitting** | Lower alpha |
| Expecting Ridge to remove features | It rarely makes weights exactly zero | Use Lasso or Elastic Net |
| Trusting Lasso's choice among correlated features | It may drop a useful one arbitrarily | Use Elastic Net, or check stability |
| Treating regularization as a replacement for more data | It helps, but cannot replace information | Collect more data if possible |

---

## 12. Summary

- **Regularization** adds a penalty on the weights' size to the cost, which discourages overly complex models and reduces overfitting.
- **Ridge (L2)** adds `α · Σ w²`. It shrinks all weights and rarely makes them exactly zero.
- **Lasso (L1)** adds `α · Σ |w|`. It can make weights exactly zero, so it performs **feature selection**.
- **Elastic Net** mixes the two.
- **Alpha** sets the strength: 0 means no penalty, and very large means underfitting.
- Always **scale features** first, and choose alpha with **cross-validation**.
- Regularization trades a **small rise in bias** for a **large drop in variance**.
- The bias term is not penalized.

---
