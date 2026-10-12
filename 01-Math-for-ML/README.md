# Phase 1: Mathematics for Machine Learning

> The math behind how models represent data, learn from it and make predictions.

---

## Overview

| | |
|---|---|
| **Focus** | Linear algebra, calculus, probability and statistics |
| **Prerequisites** | Phase 0 (Python basics) |
| **Branch / folder** | `01-Math-for-ML` |
| **Next phase** | Phase 2: Data Analysis |

**Why this phase matters:** every ML algorithm is built from four ideas.

| Idea | Math area | Example |
|---|---|---|
| Data is stored as numbers in arrays | Linear algebra | A dataset is a matrix |
| Models improve by following a slope | Calculus | Gradient descent |
| Predictions are uncertain | Probability | Naive Bayes, classification probabilities |
| Data must be summarized and compared | Statistics | Mean, variance, correlation |

---

## Table of Contents

- [Linear Algebra](#linear-algebra)
- [Calculus](#calculus)
- [Probability](#probability)
- [Statistics](#statistics)
- [Formula Cheat Sheet](#formula-cheat-sheet)
- [Where This Math Is Used Later](#where-this-math-is-used-later)
- [Suggested Order](#suggested-order)
- [Progress Checklist](#progress-checklist)
- [Notes in This Branch](#notes-in-this-branch)
- [Outcome](#outcome)

---

## Linear Algebra

Linear algebra is the language of data. It describes how numbers are arranged and combined.

| Topic | Meaning | Used in ML for |
|---|---|---|
| **Scalars** | A single number | Learning rate, a bias value |
| **Vectors** | An ordered list of numbers | One data point, or a list of weights |
| **Matrices** | A 2D grid of numbers | A full dataset (rows are examples, columns are features) |
| **Tensors** | Numbers arranged in any number of dimensions | Batches of images and text in deep learning |
| **Matrix Operations** | Addition, multiplication, transpose | Computing predictions for all rows at once |
| **Dot Product** | Multiply matching entries and add them up | Weighted sums such as `ŷ = w·x + b` |
| **Eigenvalues & Eigenvectors** | Directions a matrix only stretches, and the stretch factors | Finding directions of maximum variance (PCA) |

---

## Calculus

Calculus describes how things change, which is how a model finds out which way to improve.

| Topic | Meaning | Used in ML for |
|---|---|---|
| **Limits** | The value a function approaches | The foundation of derivatives |
| **Derivatives** | The slope of a function at a point | How the loss changes as a parameter changes |
| **Partial Derivatives** | The slope with respect to one variable, others held fixed | The slope for each parameter separately |
| **Gradients** | The vector of all partial derivatives | The direction gradient descent follows to reduce the loss |

---

## Probability

Probability measures uncertainty, which is present in all real data.

| Topic | Meaning | Used in ML for |
|---|---|---|
| **Random Variables** | A variable whose value depends on chance | Modeling uncertain outcomes |
| **Conditional Probability** | The chance of an event given another | Reasoning with evidence |
| **Bayes Theorem** | Updating a probability when new evidence arrives | Naive Bayes classifiers |
| **Probability Distributions** | How likely each value is | Describing how data is spread |
| **PDF and CDF** | Density and cumulative probability of a continuous variable | Understanding a feature's distribution |
| **Gaussian (Normal) Distribution** | The symmetric bell curve | A common assumption in models and in feature transformations |
| **Non-Gaussian Distributions** | Skewed or non-bell-shaped data | Recognizing data that needs transformation |

---

## Statistics

Statistics summarizes data and measures relationships between variables.

| Topic | Meaning | Used in ML for |
|---|---|---|
| **Mean, Median, Mode** | Measures of the center | Summaries, filling missing values |
| **Variance, Standard Deviation** | Measures of spread | Feature scaling, outlier detection |
| **Correlation** | How strongly two variables move together | Finding related features |
| **Descriptive Statistics** | A compact summary of a dataset | The first step of EDA |

---

## Formula Cheat Sheet

### Linear algebra

```
Dot product:           a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ
Matrix multiplication: (m × n) @ (n × p) = (m × p)
Eigenvector:           A v = λ v
```

### Calculus

```
Derivative:       f'(x) = lim (h→0) [ f(x + h) − f(x) ] / h
Power rule:       d/dx (xⁿ) = n · xⁿ⁻¹
Chain rule:       d/dx f(g(x)) = f'(g(x)) · g'(x)
Gradient:         ∇f = [ ∂f/∂x₁ , ∂f/∂x₂ , ... , ∂f/∂xₙ ]
Gradient descent: w := w − α · ∂J/∂w
```

### Probability

```
Conditional probability: P(A | B) = P(A and B) / P(B)
Bayes theorem:           P(A | B) = P(B | A) · P(A) / P(B)
CDF:                     F(x) = P(X ≤ x)
Gaussian PDF:            f(x) = 1 / (σ√(2π)) · exp( −(x − μ)² / (2σ²) )
```

### Statistics

```
Mean:                μ = (1/n) Σ xᵢ
Variance:            σ² = (1/n) Σ (xᵢ − μ)²      (sample variance divides by n − 1)
Standard deviation:  σ = √variance
Correlation:         r = Cov(X, Y) / (σₓ · σᵧ)    (always between −1 and +1)
```

**Rule of thumb for a Gaussian:** about 68% of values lie within 1σ of the mean, 95% within 2σ, and 99.7% within 3σ.

---

## Where This Math Is Used Later

| Math topic | Where it appears |
|---|---|
| Vectors, matrices, dot product | Linear and logistic regression (`ŷ = w·x + b`), neural network layers |
| Tensors | Deep learning data and PyTorch / TensorFlow |
| Eigenvalues and eigenvectors | PCA (Phase 4) |
| Derivatives, partial derivatives, gradients | Gradient descent, backpropagation (Phases 4 and 5) |
| Bayes theorem | Naive Bayes (Phase 4) |
| Distributions and the Gaussian | Feature transformations, assumptions in models, outlier detection (Phases 2 and 4) |
| Mean, variance, standard deviation | Standardization, regularization, bias-variance (Phase 4) |
| Correlation | EDA and feature selection (Phase 2) |

---

## Suggested Order

```
Linear Algebra  →  Calculus  →  Probability  →  Statistics
```

Calculus builds on the idea of functions, and probability and statistics build on each other, so this order lets each topic prepare the next.

---

## Progress Checklist

**Linear Algebra**
- [ ] Scalars
- [ ] Vectors
- [ ] Matrices
- [ ] Tensors
- [ ] Matrix Operations
- [ ] Dot Product
- [ ] Eigenvalues & Eigenvectors

**Calculus**
- [ ] Limits
- [ ] Derivatives
- [ ] Partial Derivatives
- [ ] Gradients

**Probability**
- [ ] Random Variables
- [ ] Conditional Probability
- [ ] Bayes Theorem
- [ ] Probability Distributions
- [ ] PDF and CDF
- [ ] Gaussian Distribution
- [ ] Non-Gaussian Distributions

**Statistics**
- [ ] Mean, Median, Mode
- [ ] Variance, Standard Deviation
- [ ] Correlation
- [ ] Descriptive Statistics

---

## Notes in This Branch

| Topic | File |
|---|---|
| Tensors | [`tensors.md`](tensors.md) |

Add a row here for each note you write.

---

## Outcome

By the end of this phase, you can:

- Represent data as vectors, matrices and tensors, and combine them with matrix operations.
- Explain what a gradient is and why it points the way to a lower loss.
- Use probability rules, Bayes theorem and distributions to reason about uncertainty.
- Summarize a dataset with descriptive statistics and measure relationships with correlation.
- Connect each math topic to the ML algorithm that uses it.
