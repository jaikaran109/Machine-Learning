> How we check that a model has truly learned, and not just memorized.

---

## 1. The Big Idea

The goal of machine learning is not to do well on data the model has already seen. The goal is to do well on **new, unseen data**. This ability is called **generalization**.

**Analogy:** A teacher gives 100 practice questions, then uses the same 100 in the final exam. Everyone scores high, but did they learn the subject or memorize the answers? You can't tell. A fair teacher **hides** some questions until exam day. The score on those hidden questions shows real understanding.

Train/test split and cross-validation are the two standard ways of "hiding questions" from a model.

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Generalization** | A model's performance on data it has never seen. | Real understanding, not memorizing. |
| **Training set** | The part of the data the model learns from. | The practice questions. |
| **Test set** | The part of the data kept hidden and used only for the final score. | The final exam. |
| **Validation set** | A part of the training data used to compare models and tune settings. | A mock exam. |
| **Hyperparameter** | A setting you choose before training (e.g. learning rate, number of neighbors). | A dial you set, not one the model learns. |
| **Data leakage** | Information from the test set sneaking into training. | Seeing the exam paper in advance. |
| **Fold** | One of the equal parts the data is divided into for cross-validation. | One slice of the data. |
| **Cross-validation** | Repeating training and testing on several different splits and averaging the results. | Several exams instead of one. |

---

## 3. Train/Test Split

### Concept

We divide the dataset into two parts **before** training:

- **Training set (usually 70-80%):** the model learns from this.
- **Test set (usually 20-30%):** locked away until the very end, then used **once** to measure performance.

**Example:** 1,000 rows with an 80/20 split gives 800 training rows and 200 test rows.

### The golden rule

> The model must **never** see the test set during training or tuning.

If it does, the score becomes dishonest, and you will be surprised when the model performs worse in the real world.

### In code

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

| Argument | Meaning |
|---|---|
| `test_size=0.2` | 20% of the data goes to the test set |
| `random_state=42` | Fixes the random shuffle so results are reproducible |
| `stratify=y` | Keeps the class proportions the same in both sets (for classification) |

**Why stratify?** Suppose only 10% of customers churn. A random split could put almost all churners in one set. `stratify=y` makes both sets contain about 10% churners.

### Three-way split: train, validation, test

When you try many models or settings, you need somewhere to compare them. If you compare them on the test set, you are indirectly tuning to it. So we use three sets:

| Set | Typical share | Purpose |
|---|---|---|
| **Training** | 60% | Fit the model |
| **Validation** | 20% | Compare models and tune hyperparameters |
| **Test** | 20% | One final, honest evaluation |

Cross-validation (next section) is the usual way to avoid carving out a separate validation set.

---

## 4. Cross-Validation

### The problem it solves

A single train/test split can be **unlucky**. The test set might happen to contain unusually easy examples, so the score looks too good, or unusually hard ones, so it looks too bad. A single split also leaves out data that the model could have learned from.

### Concept

**Cross-validation (CV)** repeats the train/test process several times on different splits, so that every data point is used for testing exactly once. The final score is the **average**.

### K-Fold cross-validation (steps)

1. Split the training data into **k equal folds** (commonly k = 5 or 10).
2. In round 1, train on folds 2-5 and test on fold 1.
3. In round 2, train on folds 1, 3, 4, 5 and test on fold 2.
4. Continue until each fold has been the test fold once.
5. Average the k scores.

| Round | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|---|---|---|---|---|---|
| 1 | **Test** | Train | Train | Train | Train |
| 2 | Train | **Test** | Train | Train | Train |
| 3 | Train | Train | **Test** | Train | Train |
| 4 | Train | Train | Train | **Test** | Train |
| 5 | Train | Train | Train | Train | **Test** |

```
CV score = (1/k) · (score₁ + score₂ + ... + score_k)
```

**Example:** the five fold scores are `0.88, 0.90, 0.86, 0.92, 0.89`.

```
Mean = (0.88 + 0.90 + 0.86 + 0.92 + 0.89) / 5 = 0.89
Std  = 0.02
```

Report it as **0.89 ± 0.02**. The mean tells you how good the model is, and the standard deviation tells you how **stable** it is. If one fold were far below the others (for example 0.55), that would warn you that the model is sensitive to which data it sees.

### In code

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_train, y_train, cv=5)
print(scores)           # one score per fold
print(scores.mean())    # average
print(scores.std())     # stability
```

### Common variants

| Variant | Idea | Use when |
|---|---|---|
| **K-Fold** | k equal folds | Default for regression |
| **Stratified K-Fold** | Each fold keeps the class proportions | Classification, especially imbalanced data |
| **Leave-One-Out** | k equals the number of rows (each row is a test set once) | Very small datasets (slow otherwise) |

**Choosing k:** 5 or 10 works well in practice. A larger k uses more data for training in each round, but takes longer.

---

## 5. Train/Test Split vs Cross-Validation

| | Train/Test Split | Cross-Validation |
|---|---|---|
| **Number of evaluations** | 1 | k |
| **Speed** | Fast | k times slower |
| **Reliability** | Depends on a lucky or unlucky split | More reliable, shows stability |
| **Data use** | Test data never used for learning | Every point is used for both training and testing (in different rounds) |
| **Best for** | Large datasets, quick checks, final test | Small or medium datasets, model comparison, tuning |

### The standard workflow

1. Split off a **test set** and lock it away.
2. Use **cross-validation on the training set** to compare models and tune hyperparameters.
3. Train the chosen model on the full training set.
4. Evaluate on the test set **once**.

---

## 6. Common Mistakes

| Mistake | Why it is wrong | Fix |
|---|---|---|
| Tuning the model until the test score is best | The test set becomes part of training | Tune with cross-validation or a validation set |
| Scaling or imputing on the whole dataset **before** splitting | Test-set statistics leak into training (data leakage) | Split first, then fit the scaler on the training set only (Pipelines handle this) |
| Not stratifying imbalanced classes | Splits may have very different class mixes | Use `stratify=y` or Stratified K-Fold |
| Shuffling time-ordered data | The model would learn from the future | Split by time, with earlier data for training |
| Forgetting `random_state` | Results change on every run | Set it for reproducibility |

---

## 7. Summary

- The goal is **generalization**: performance on unseen data.
- **Train/test split** hides part of the data to give an honest final score.
- The model must **never** see the test set during training or tuning.
- **Cross-validation** averages scores over k different splits for a more reliable and stable estimate.
- Use `stratify=y` or Stratified K-Fold for classification.
- Typical workflow: split off the test set, tune with cross-validation, then test once.
- Always split **before** preprocessing to avoid data leakage.

---
