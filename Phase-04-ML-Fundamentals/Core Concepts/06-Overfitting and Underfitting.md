> Why a model can fail on new data, how to recognize it, and how to fix it.

---

## 1. The Big Idea

A model is useful only if it works on **new, unseen data**. Two opposite problems can stop that from happening:

- **Underfitting:** the model is too simple and never learns the real pattern.
- **Overfitting:** the model is too complex and learns the training data, including its random noise, instead of the real pattern.

**Analogy:** Three students prepare for an exam.

| Student | What they did | Practice questions | Real exam |
|---|---|---|---|
| **A** | Barely studied, knows only the basics | Fails | Fails |
| **B** | Memorized every practice question word for word | Scores 100% | Fails when the wording changes |
| **C** | Understood the underlying concepts | Does well | Does well |

Student A is **underfitting**, Student B is **overfitting**, and Student C has a **good fit**.

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Pattern (signal)** | The true, repeatable relationship in the data. | What we want to learn. |
| **Noise** | Random variation in the data that has no real meaning (measurement errors, chance). | What we should ignore. |
| **Underfitting** | The model is too simple to capture the pattern, so it performs poorly on **both** training and test data. | Hasn't learned enough. |
| **Overfitting** | The model fits the training data, noise included, so it performs very well on training data but poorly on new data. | Memorized instead of learned. |
| **Good fit** | The model captures the pattern and ignores the noise, so it performs well on both. | Learned the concept. |
| **Generalization** | How well a model performs on unseen data. | Real understanding. |
| **Model complexity** | How flexible a model is (e.g. polynomial degree, tree depth). | How wiggly it can get. |
| **Generalization gap** | Training score minus test score. | How much the model flatters itself. |

---

## 3. Underfitting

### Concept

The model is **too simple** for the data. It cannot represent the real relationship, so it misses the pattern.

**Example:** fitting a straight line to data that clearly curves. The line is wrong in the same way everywhere, so errors are large on both the training and the test set.

### Signs

- Training score is **low**.
- Test score is **low**, and close to the training score.
- The model's predictions look too rigid and too "average".

### Common causes

- A model that is too simple (e.g. a linear model for non-linear data)
- Too few or uninformative features
- Too much regularization
- Training stopped too early

### Fixes

| Fix | Example |
|---|---|
| Use a more powerful model | Polynomial regression, deeper trees, Random Forest, boosting |
| Add useful features | Create new features, polynomial terms |
| Reduce regularization | Lower `alpha` in Ridge or Lasso |
| Train longer | More epochs or iterations |

---

## 4. Overfitting

### Concept

The model is **too complex** for the amount of data. It has enough flexibility to twist itself around every training point, including the random noise. The result looks perfect on the training data but fails on anything new.

**Example:** a wiggly curve that passes through every single training point. It "explains" the noise, so a new point lands far from the curve.

### Signs

- Training score is **very high**.
- Test (or cross-validation) score is **much lower**.
- A large generalization gap.

### Common causes

- A model that is too complex (very deep trees, very high polynomial degree, too many neighbors' worth of flexibility)
- Too little training data
- Too many features, especially irrelevant ones
- Noisy data
- Training for too long

### Fixes

| Fix | How it helps |
|---|---|
| **Get more data** | Harder to memorize, and noise averages out |
| **Simplify the model** | Lower polynomial degree, shallower tree, fewer features |
| **Regularization (Ridge, Lasso)** | Penalizes large weights, forcing smoother models |
| **Cross-validation** | Detects overfitting early and guides tuning |
| **Early stopping** | Stop training when validation error starts rising |
| **Pruning (trees)** | Cut back branches that fit noise |
| **Ensembles (Random Forest)** | Averaging many models cancels out individual noise |
| **Feature selection** | Remove irrelevant features |

---

## 5. How to Diagnose It

Compare the **training score** with the **test or cross-validation score**.

| Training score | Test score | Diagnosis |
|---|---|---|
| Low | Low (close to training) | **Underfitting** |
| High | High (close to training) | **Good fit** |
| Very high | Much lower | **Overfitting** |

**Illustrative numbers (accuracy):**

| Model | Train | Test | Verdict |
|---|---|---|---|
| A | 55% | 52% | Underfitting |
| B | 99% | 65% | Overfitting |
| C | 91% | 88% | Good fit |

```
Generalization gap = training score − test score
```

A small gap with good scores is what we want. A large gap signals overfitting. Low scores on both signal underfitting.

### Learning curves

A **learning curve** plots training and validation scores as the amount of training data grows.

| Pattern | Meaning |
|---|---|
| Both curves low and close together | Underfitting. More data will not help, a better model will. |
| Training high, validation much lower, a wide gap | Overfitting. More data will probably help. |
| Both high and converging | Good fit |

### Validation curves

A **validation curve** plots training and validation scores against a **complexity setting**, such as polynomial degree. Underfitting appears on the left (simple), overfitting on the right (complex), and the best setting is where the validation score peaks.

---

## 6. Worked Example: Polynomial Degree

Data follows a smooth curve with a little noise. We fit polynomial regression with different degrees.

| Degree | Model shape | Training error | Test error | Verdict |
|---|---|---|---|---|
| 1 | Straight line | High | High | **Underfit** |
| 4 | Smooth curve | Low | Low | **Good fit** |
| 15 | Wild wiggles through every point | Almost zero | High | **Overfit** |

As complexity rises, **training error keeps falling**, but **test error falls and then rises again**. That turn is the point where the model stops learning the pattern and starts learning the noise.

### In code

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

rng = np.random.RandomState(42)
X = np.sort(rng.uniform(0, 6, 40)).reshape(-1, 1)
y = np.sin(X).ravel() + rng.normal(0, 0.2, 40)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

for degree in [1, 4, 15]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    print(f"Degree {degree:2d} | train R² = {model.score(X_train, y_train):.3f} "
          f"| test R² = {model.score(X_test, y_test):.3f}")
```

**What to expect:** degree 1 scores low on both, degree 4 scores high on both, and degree 15 scores very high on training but noticeably lower (possibly very poor) on test. Exact numbers depend on the random data.

---

## 7. Complexity Settings by Algorithm

Every algorithm has dials that control complexity. Use them to move between underfitting and overfitting.

| Algorithm | Setting | Increasing it |
|---|---|---|
| Polynomial Regression | Degree | More complex (overfit risk) |
| Ridge / Lasso | `alpha` | **Simpler** (underfit risk) |
| KNN | `k` | **Simpler** (small k overfits, large k underfits) |
| Decision Tree | `max_depth` | More complex (overfit risk) |
| Random Forest | `max_depth`, `n_estimators` | Depth adds complexity, more trees add stability |
| SVM | `C`, `gamma` | More complex (overfit risk) |
| Gradient Boosting / XGBoost | `n_estimators`, `learning_rate`, `max_depth` | More rounds and depth add complexity |

---

## 8. Link to Bias and Variance (preview)

| | Underfitting | Overfitting |
|---|---|---|
| **Bias** | High (consistently wrong in the same way) | Low |
| **Variance** | Low (stable) | High (changes a lot with the training data) |

Total prediction error can be thought of as:

```
Error = Bias² + Variance + Irreducible noise
```

Making a model more complex lowers bias but raises variance. The goal is the sweet spot in between. This is the **bias-variance tradeoff**, covered in detail in the next topic.

---

## 9. Common Misconceptions

| Myth | Reality |
|---|---|
| "High training accuracy means a good model." | It may only mean memorization. Check the test score. |
| "More complex is always better." | Beyond a point, extra complexity fits noise. |
| "More data always fixes it." | It helps overfitting, but not underfitting. |
| "100% training accuracy is the goal." | It is usually a warning sign of overfitting. |

---

## 10. Summary

- **Underfitting:** too simple, so both training and test scores are low.
- **Overfitting:** too complex, so training score is high but test score is much lower.
- **Good fit:** the model captures the pattern, ignores the noise, and scores well on both.
- Diagnose by comparing training and test (or cross-validation) scores.
- Fix underfitting with a stronger model, better features and less regularization.
- Fix overfitting with more data, a simpler model, regularization, early stopping, pruning or ensembles.
- Training error always falls as complexity rises, but test error falls and then rises again.

---
