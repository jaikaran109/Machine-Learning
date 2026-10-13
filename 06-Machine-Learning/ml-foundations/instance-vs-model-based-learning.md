> Two different ways a machine learning system can turn training data into predictions on new data.

---

## 1. The Big Idea

After training, a system must predict for **new** data it has never seen. There are two basic strategies:

- **Instance-based:** keep the examples and compare each new case with them.
- **Model-based:** study the examples, build a general rule (a model), and then use that rule.

**Analogy:** Two students prepare for an exam.

- **Student A** keeps every past exam paper. For a new question, she finds the *most similar* old question and copies its answer. (Instance-based)
- **Student B** studies the papers, understands the underlying formula, and then throws the papers away. For a new question, she applies the formula. (Model-based)

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Instance-based learning** | The system stores the training examples and predicts by measuring how **similar** a new example is to the stored ones. | Memorize, then compare. |
| **Model-based learning** | The system uses the training data to **learn parameters** that form a model, then predicts with the model alone. | Learn a rule, then apply it. |
| **Lazy learner** | Does almost no work during training and defers the work until a prediction is requested. | Studies only when asked. |
| **Eager learner** | Does the heavy work during training so that predictions are fast. | Studies in advance. |
| **Similarity measure** | A way to decide how close two examples are, such as Euclidean distance. | "How alike are these two?" |
| **Non-parametric** | The model has no fixed number of parameters. It can grow with the data. | Flexible size. |
| **Parametric** | The model has a fixed number of parameters, such as `w` and `b`, no matter how much data you have. | Fixed size. |

---

## 3. Instance-Based Learning

### Concept

The "model" is the **training data itself**. Nothing is summarized or compressed. When a new example arrives, the system looks up the closest stored examples and bases its answer on them.

### How it works (steps)

1. **Training:** simply store all the examples.
2. **Prediction:** for a new example, measure its similarity (distance) to every stored example.
3. Pick the most similar ones.
4. Combine their answers: majority vote for classification, average for regression.

### Characteristics

- **Lazy:** training is instant, but prediction is slow because it must search the stored data.
- **Memory-heavy:** all the training data must be kept.
- **Flexible:** it can fit very complex patterns without assuming a shape.
- **Sensitive to feature scale and irrelevant features,** because distance depends on them.

### Algorithms

| Algorithm | Idea |
|---|---|
| **KNN (k-Nearest Neighbors)** | Predicts from the k closest training examples. The standard example, and the only one in your Phase 4 list. |
| **Locally Weighted Regression** | Fits a small regression around each new point, giving nearby examples more weight. |
| **Case-Based Reasoning** | Solves a new problem by adapting the solution of the most similar stored case. |
| **Learning Vector Quantization (LVQ)** | Stores a small set of representative examples (prototypes) and classifies by the nearest one. |
| **Self-Organizing Maps (SOM)** | Arranges stored prototypes on a grid according to similarity. |

---

## 4. Model-Based Learning

### Concept

The system studies the training data and **builds a model**: a compact mathematical or logical rule with parameters. After training, the original data is no longer needed to make predictions.

### How it works (steps)

1. **Choose a model form**, such as a line `ŷ = w·x + b`.
2. **Train:** find the parameter values that minimize the cost (for example, with gradient descent).
3. **Predict:** plug the new example into the trained model.

### Characteristics

- **Eager:** training takes the effort, but prediction is very fast.
- **Compact:** only the learned parameters (or tree, or rules) are stored.
- **Often interpretable:** you can inspect the weights or the tree.
- **Can underfit** if the chosen model form is too simple for the data.

### Algorithms

| Algorithm | What the "model" is |
|---|---|
| **Linear / Multiple / Polynomial Regression** | Weights `w` and bias `b` |
| **Logistic Regression** | Weights and bias passed through a sigmoid |
| **Naive Bayes** | Learned class and feature probabilities |
| **Decision Tree** | A tree of learned splitting rules |
| **Random Forest** | A collection of trees |
| **Gradient Boosting, XGBoost, LightGBM, CatBoost** | A sequence of trees added together |
| **SVM** | A decision boundary defined by support vectors and weights |
| **Neural Networks** | Layers of learned weights |
| **K-Means** | The learned cluster centers |
| **PCA** | The learned principal component directions |

> **Note:** Decision Trees and Random Forests are *non-parametric* in the sense that their size can grow with the data, but they are still model-based because they learn a rule and then discard the data. Likewise, SVM keeps the support vectors, but it is classed as model-based because it learns a boundary.

---

## 5. Worked Example: Predicting a House Price

Training data (area in sq ft, price in ₹ lakh):

| Area | Price |
|---|---|
| 1000 | 40 |
| 1200 | 48 |
| 1500 | 60 |
| 2000 | 80 |

**New house: 1300 sq ft. What is the price?**

**Instance-based (KNN, k = 2):**
1. Distances from 1300: to 1200 is 100, to 1500 is 200, to 1000 is 300, to 2000 is 700.
2. The two nearest are 1200 (₹48) and 1500 (₹60).
3. Prediction = average = `(48 + 60) / 2 = ₹54 lakh`.

**Model-based (Linear Regression):**
1. Learn from the data: `price = 0.04 × area` (this data is exactly linear).
2. The data can now be discarded.
3. Prediction = `0.04 × 1300 = ₹52 lakh`.

**What this shows:** KNN answered from nearby examples and was slightly off, because it only averaged neighbors. The linear model captured the overall trend. KNN, however, would have handled a curved or irregular pattern without any change, while a straight line would not.

---

## 6. Comparison

| Aspect | Instance-Based | Model-Based |
|---|---|---|
| **What is learned** | Nothing; data is stored | Parameters or rules |
| **Training time** | Very fast | Can be slow |
| **Prediction time** | Slow (searches all data) | Fast |
| **Memory** | Stores all training data | Stores only the model |
| **Learner type** | Lazy | Eager |
| **Interpretability** | Low to medium (the neighbors explain a prediction) | Often high (weights, trees) |
| **Complex patterns** | Handles them naturally | Depends on the model chosen |
| **Large datasets** | Struggles | Scales well |
| **Many features** | Suffers (curse of dimensionality) | Generally better |
| **Feature scaling** | Essential | Depends on the algorithm |
| **Adding new data** | Easy: just store it | Usually needs retraining |
| **Example** | KNN | Linear Regression |

### When to use which

- **Instance-based:** small to medium data, complex boundaries, no clear model form, or when new data arrives constantly.
- **Model-based:** large data, fast predictions needed, explainability needed, or the relationship has a recognizable form.

### Where Phase 4 algorithms fall

| Instance-based | Model-based |
|---|---|
| KNN | Linear, Logistic Regression, Naive Bayes, Decision Trees, Random Forest, Gradient Boosting, XGBoost, SVM, K-Means, PCA |

Hierarchical Clustering doesn't fit neatly into either group, since it compares examples with each other but builds no predictive model.

---

## 7. Summary

- **Instance-based learning** memorizes the examples and predicts by similarity. It is lazy.
- **Model-based learning** learns parameters or rules and predicts from the model alone. It is eager.
- The main algorithm for instance-based learning is **KNN**. Almost every other Phase 4 algorithm is model-based.
- Instance-based means fast training and slow prediction. Model-based means slower training and fast prediction.
- Neither is always better. The choice depends on data size, speed needs, explainability and the shape of the pattern.

---

## 8. Practice Questions

1. In your own words, how does an instance-based learner differ from a model-based learner?
2. What does "lazy learner" mean? Which type of learning is lazy?
3. Name three instance-based algorithms and five model-based algorithms.
4. Why is KNN fast to train but slow to predict?
5. After training a linear regression model, do you still need the training data to make predictions? What about KNN?
6. Why does KNN need feature scaling?
7. Using the house data above, predict the price of a **1100 sq ft** house with KNN (k = 2) and with the linear model `price = 0.04 × area`.
8. A dataset has millions of rows and predictions must be returned in milliseconds. Which type would you lean toward, and why?
9. New data arrives every hour. Which type adapts more easily without retraining?

### Answers to the numerical question

- **Q7:** Distances from 1100: to 1000 is 100, to 1200 is 100, to 1500 is 400. The two nearest are 1000 (₹40) and 1200 (₹48), so KNN gives `(40 + 48) / 2 = ₹44 lakh`. The linear model gives `0.04 × 1100 = ₹44 lakh`. Both agree here because the data is evenly spaced around 1100.