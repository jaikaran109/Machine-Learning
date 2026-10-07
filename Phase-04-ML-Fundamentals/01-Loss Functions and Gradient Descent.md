# Core Concepts 

> **Phase 4: Machine Learning Fundamentals**
> This note explains how a model measures its own mistakes (loss functions) and how it uses those mistakes to improve (gradient descent). Almost every algorithm later in this phase, and in deep learning, relies on these two ideas.

---

## Table of Contents

1. [Why Do We Need This?](#1-why-do-we-need-this)
2. [Notation Used in This Note](#2-notation-used-in-this-note)
3. [Recap: What a Model and Its Parameters Are](#3-recap-what-a-model-and-its-parameters-are)
4. [Loss Function vs Cost Function](#4-loss-function-vs-cost-function)
5. [Loss Functions for Regression](#5-loss-functions-for-regression)
6. [Loss Functions for Classification](#6-loss-functions-for-classification)
7. [The Loss Surface](#7-the-loss-surface)
8. [What is a Gradient?](#8-what-is-a-gradient)
9. [Calculating the Gradient for Linear Regression](#9-calculating-the-gradient-for-linear-regression)
10. [The Weight Update Rule](#10-the-weight-update-rule)
11. [The Learning Rate](#11-the-learning-rate)
12. [Full Worked Example](#12-full-worked-example)
13. [Variants of Gradient Descent](#13-variants-of-gradient-descent)
14. [When Do We Stop Training?](#14-when-do-we-stop-training)
15. [Gradient Descent From Scratch in Python](#15-gradient-descent-from-scratch-in-python)
16. [Common Problems and Fixes](#16-common-problems-and-fixes)
17. [Formula Cheat Sheet](#17-formula-cheat-sheet)
18. [Summary](#18-summary)
19. [Answers to Numerical Questions](#19-answers-to-numerical-questions)

---

## 1. Why Do We Need This?

A machine learning model starts out knowing nothing. Its settings (parameters) are random, so its first predictions are poor. To improve, the model needs to answer two questions:

1. **How wrong am I?** This is answered by the **loss function**.
2. **How should I change my parameters to be less wrong?** This is answered by **gradient descent**.

### The mountain story

Imagine standing on a mountain in thick fog. You cannot see the valley, but you want to reach the lowest point. You feel the slope under your feet, take a small step downhill, and repeat.

| In the story | In machine learning |
|---|---|
| Your height on the mountain | The model's error (loss) |
| Your position (where you stand) | The model's current parameter values |
| The lowest point in the valley | The best parameters (smallest loss) |
| Feeling the slope | Calculating the gradient |
| Taking a step | Updating the parameters |
| Length of your step | The learning rate |

### Check your understanding

1. What two questions must a model answer in order to improve?
2. In the mountain story, what does "feeling the slope" correspond to?

---

## 2. Notation Used in This Note

| Symbol | Meaning |
|---|---|
| `n` | Number of training examples |
| `x_i` | Input (feature) of the i-th example |
| `y_i` | True (actual) value of the i-th example |
| `ŷ_i` (y-hat) | Value predicted by the model for the i-th example |
| `w` | Weight (slope) parameter |
| `b` | Bias (intercept) parameter |
| `e_i` | Error of the i-th example, defined here as `ŷ_i − y_i` |
| `L` | Loss for a single example |
| `J` | Cost: the average loss over all examples |
| `α` (alpha) | Learning rate |
| `∂J/∂w` | Partial derivative of J with respect to w (the gradient component for w) |
| `Σ` | Sum over all examples (from i = 1 to n) |

---

## 3. Recap: What a Model and Its Parameters Are

The simplest model is a straight line (simple linear regression):

```
ŷ = w · x + b
```

- `x` is the input, for example the area of a house.
- `ŷ` is the predicted output, for example the predicted price.
- `w` and `b` are the **parameters**. Training means finding the values of `w` and `b` that make predictions as accurate as possible.

With many features (multiple linear regression):

```
ŷ = w₁·x₁ + w₂·x₂ + ... + wₘ·xₘ + b
```

Whatever the model, the logic is the same: **parameters are the dials that training adjusts.**

### Check your understanding

1. In `ŷ = w·x + b`, which symbols are parameters and which are data?
2. If `w = 3` and `b = 2`, what is the prediction for `x = 4`?

---

## 4. Loss Function vs Cost Function

These terms are often used loosely, but they have a precise meaning:

| Term | Definition |
|---|---|
| **Loss function** `L` | The error for a **single** training example |
| **Cost function** `J` | The **average** loss over the **whole** training set |

```
J = (1/n) · Σ L(ŷ_i, y_i)
```

Gradient descent minimizes the **cost** `J`. Many books and libraries use "loss" for both, so always check the context.

### Check your understanding

1. What is the difference between a loss function and a cost function?
2. Which of the two does gradient descent try to minimize?

---

## 5. Loss Functions for Regression

Regression predicts a number, so the loss measures the distance between the predicted and the actual number.

### 5.1 Mean Squared Error (MSE)

```
MSE = (1/n) · Σ (y_i − ŷ_i)²
```

**Steps to calculate:**
1. For each example, find the error `y_i − ŷ_i`.
2. Square each error.
3. Average all the squared errors.

**Why square the error?**
- Squaring makes every error positive, so over-predictions and under-predictions cannot cancel out.
- Large errors are punished much more heavily (10² = 100, while 2² = 4).
- The squared function is smooth, so its derivative is easy to calculate. This is what makes gradient descent work well.

**Drawback:** it is sensitive to outliers, because one huge error gets squared into an enormous number. Its units are also squared (for example, rupees²).

**Worked example:**

| Example | Actual y | Predicted ŷ | Error (y − ŷ) | Squared error |
|---|---|---|---|---|
| 1 | 10 | 12 | −2 | 4 |
| 2 | 20 | 18 | 2 | 4 |
| 3 | 30 | 33 | −3 | 9 |

```
MSE = (4 + 4 + 9) / 3 = 17 / 3 = 5.67
```

### 5.2 Root Mean Squared Error (RMSE)

```
RMSE = √MSE
```

Taking the square root brings the units back to the original scale. For the example above, `RMSE = √5.67 ≈ 2.38`, which reads as "the predictions are typically off by about 2.38 units."

### 5.3 Mean Absolute Error (MAE)

```
MAE = (1/n) · Σ |y_i − ŷ_i|
```

For the example above: `MAE = (2 + 2 + 3) / 3 = 2.33`.

- Treats all errors in proportion to their size, so it is **robust to outliers**.
- Has a sharp corner at zero error, so the derivative is undefined exactly there. Gradient descent can still use it, but it is less smooth than MSE.

### 5.4 Huber Loss (a blend of the two)

```
L = ½ · e²                    if |e| ≤ δ
L = δ · (|e| − ½ · δ)         if |e| > δ
```

It behaves like MSE for small errors (smooth) and like MAE for large errors (robust). `δ` is a threshold you choose.

### 5.5 Comparison

| Loss | Formula | Outlier sensitivity | Smooth? | Typical use |
|---|---|---|---|---|
| **MSE** | `mean((y − ŷ)²)` | High | Yes | Default for linear regression |
| **RMSE** | `√MSE` | High | Yes | Reporting error in original units |
| **MAE** | `mean(\|y − ŷ\|)` | Low | No (corner at 0) | Data with outliers |
| **Huber** | MSE for small, MAE for large errors | Medium | Yes | Compromise between the two |

### Check your understanding

1. Why do we square errors in MSE? Give two reasons.
2. Calculate MSE, MAE and RMSE for actual values `[5, 8, 12]` and predictions `[6, 7, 15]`.
3. Which loss would you prefer if your data has a few extreme outliers, and why?
4. How is RMSE related to MSE, and why is it easier to interpret?

---

## 6. Loss Functions for Classification

In classification the model outputs a **probability**, so measuring the distance between two numbers is not the best approach. We need a loss that heavily punishes confident wrong answers. You will need this when we study Logistic Regression.

### 6.1 The sigmoid function (recap)

Logistic regression converts a raw score `z = w·x + b` into a probability between 0 and 1:

```
p = σ(z) = 1 / (1 + e^(−z))
```

### 6.2 Binary Cross-Entropy (Log Loss)

For a single example with true label `y ∈ {0, 1}` and predicted probability `p`:

```
L = −[ y · ln(p) + (1 − y) · ln(1 − p) ]
```

Over the whole dataset:

```
J = −(1/n) · Σ [ y_i · ln(p_i) + (1 − y_i) · ln(1 − p_i) ]
```

**How to read it:**
- If the true label is `y = 1`, the loss reduces to `−ln(p)`. A high `p` gives a small loss.
- If the true label is `y = 0`, the loss reduces to `−ln(1 − p)`. A low `p` gives a small loss.

**Worked examples:**

| True y | Predicted p | Loss | Meaning |
|---|---|---|---|
| 1 | 0.90 | −ln(0.90) = 0.105 | Confident and correct, tiny loss |
| 1 | 0.50 | −ln(0.50) = 0.693 | Unsure, moderate loss |
| 1 | 0.10 | −ln(0.10) = 2.303 | Confident and wrong, large loss |
| 0 | 0.90 | −ln(1 − 0.90) = 2.303 | Confident and wrong, large loss |

As `p` approaches the wrong extreme, the loss grows without bound. This strongly discourages confident mistakes.

**Why not use MSE for classification?** Combined with the sigmoid, MSE produces a bumpy loss surface with flat regions where learning stalls. Cross-entropy gives a clean, convex surface for logistic regression.

### 6.3 Categorical Cross-Entropy (more than two classes)

With `K` classes, a one-hot true label `y`, and predicted probabilities `p`:

```
L = −Σ (k = 1..K) y_k · ln(p_k)
```

Only the term for the true class survives, so the loss is simply `−ln(probability given to the correct class)`.

### 6.4 Hinge Loss (used by SVM)

With labels `y ∈ {−1, +1}` and model score `f(x)`:

```
L = max(0, 1 − y · f(x))
```

The loss is zero when the example is correctly classified with enough margin, and grows linearly otherwise. We will meet this again if you study SVM.

### 6.5 Summary

| Task | Typical loss |
|---|---|
| Regression | MSE (or MAE, Huber) |
| Binary classification | Binary cross-entropy |
| Multi-class classification | Categorical cross-entropy |
| SVM | Hinge loss |

### Check your understanding

1. Why is a confident wrong prediction punished so heavily by cross-entropy?
2. Calculate the binary cross-entropy for `y = 1`, `p = 0.5`.
3. Calculate the loss for `y = 0`, `p = 0.2`. Is it larger or smaller than for `y = 0`, `p = 0.9`?
4. Which loss would you use for predicting whether an email is spam?

---

## 7. The Loss Surface

If we plot the cost `J` against the parameters, we get a **loss surface**.

- With **one** parameter, it is a curve.
- With **two** parameters (`w` and `b`), it is a 3D surface, like a landscape.
- With thousands of parameters, we cannot draw it, but the idea is the same.

Training means finding the **lowest point** of this landscape.

### Convex vs non-convex

| | Convex | Non-convex |
|---|---|---|
| **Shape** | A single smooth bowl | Hills, valleys and flat plateaus |
| **Minima** | Exactly one (the global minimum) | Many local minima and saddle points |
| **Gradient descent** | Guaranteed to reach the best solution (with a suitable learning rate) | May settle in a local minimum or stall on a plateau |
| **Examples** | Linear regression with MSE, logistic regression | Neural networks |

Good news for this phase: the models you will train with gradient descent here (linear and logistic regression) have **convex** loss surfaces, so there is one best answer to find.

### Check your understanding

1. What is a loss surface?
2. What does "convex" mean, and why is it good news for gradient descent?
3. Why is training a neural network harder than training a linear regression?

---

## 8. What is a Gradient?

### 8.1 The derivative (one parameter)

The **derivative** of a function tells us its **slope** at a point: how fast the output changes when the input changes slightly.

| Slope | Meaning |
|---|---|
| Positive | Loss goes **up** as the parameter increases |
| Negative | Loss goes **down** as the parameter increases |
| Zero | Flat ground, possibly a minimum |

**Example:** for `J(w) = (w − 3)²`, the derivative is `dJ/dw = 2(w − 3)`.

- At `w = 0` the slope is `2(0 − 3) = −6` (negative, so increasing `w` lowers the loss).
- At `w = 5` the slope is `2(5 − 3) = +4` (positive, so decreasing `w` lowers the loss).
- At `w = 3` the slope is `0`. This is the minimum.

### 8.2 Partial derivatives (many parameters)

When the cost depends on several parameters, we take the slope with respect to **one parameter at a time**, treating the others as fixed numbers. This is a **partial derivative**, written `∂J/∂w` and `∂J/∂b`.

### 8.3 The gradient vector

The **gradient** collects all the partial derivatives into one vector:

```
∇J = [ ∂J/∂w , ∂J/∂b ]
```

**Key fact:** the gradient points in the direction of **steepest increase** of the cost. Therefore, **the negative gradient points in the direction of steepest decrease.** Gradient descent simply walks along the negative gradient.

### 8.4 Derivative rules you need

| Rule | Formula |
|---|---|
| Power rule | `d/dx (xⁿ) = n · xⁿ⁻¹` |
| Constant multiple | `d/dx (c · f) = c · f'` |
| Sum rule | `d/dx (f + g) = f' + g'` |
| Chain rule | `d/dx f(g(x)) = f'(g(x)) · g'(x)` |

### Check your understanding

1. What does a negative slope tell you about which way to move the parameter?
2. Find the derivative of `J(w) = (w − 5)²` and evaluate it at `w = 1`.
3. What is a partial derivative, and why do we need them?
4. Why do we move in the direction of the **negative** gradient?

---

## 9. Calculating the Gradient for Linear Regression

This is the derivation that makes gradient descent concrete. Follow it line by line.

### 9.1 Setup

```
Model:    ŷ_i = w · x_i + b
Error:    e_i = ŷ_i − y_i
Cost:     J(w, b) = (1/n) · Σ (ŷ_i − y_i)²  =  (1/n) · Σ e_i²
```

### 9.2 Gradient with respect to w

Apply the chain rule to each squared term `e_i²`:

```
∂(e_i²)/∂w = 2 · e_i · ∂e_i/∂w
```

Since `e_i = w·x_i + b − y_i`, the derivative of `e_i` with respect to `w` is simply `x_i`. So:

```
∂J/∂w = (1/n) · Σ 2 · e_i · x_i

∂J/∂w = (2/n) · Σ (ŷ_i − y_i) · x_i
```

### 9.3 Gradient with respect to b

The derivative of `e_i` with respect to `b` is `1`. So:

```
∂J/∂b = (2/n) · Σ (ŷ_i − y_i)
```

### 9.4 Final formulas

```
∂J/∂w = (2/n) · Σ (ŷ_i − y_i) · x_i

∂J/∂b = (2/n) · Σ (ŷ_i − y_i)
```

**In words:**
- The gradient for `b` is just twice the **average error**.
- The gradient for `w` is twice the **average of (error × input)**, so inputs with larger values have more influence on `w`.

### 9.5 Convention note

Many textbooks define the cost with an extra half: `J = (1/2n) · Σ e_i²`. The 2 then cancels and the gradients become `(1/n) · Σ e_i · x_i` and `(1/n) · Σ e_i`. Both versions are valid. They differ only by a constant factor, which is absorbed into the learning rate. This note uses the version **without** the half.

### 9.6 Many features (vector form)

For multiple linear regression with weights `w₁ ... wₘ`:

```
∂J/∂w_j = (2/n) · Σ (ŷ_i − y_i) · x_ij        for each feature j
```

In compact matrix form, with feature matrix `X` (n rows, with a column of ones to carry the bias) and parameter vector `θ`:

```
∇J(θ) = (2/n) · Xᵀ · (X·θ − y)
```

### 9.7 Gradient for logistic regression (preview)

For binary cross-entropy with a sigmoid output `p_i = σ(w·x_i + b)`, the derivation (via the chain rule) gives a remarkably similar result:

```
∂J/∂w = (1/n) · Σ (p_i − y_i) · x_i

∂J/∂b = (1/n) · Σ (p_i − y_i)
```

The structure is the same: `(prediction − actual) × input`, averaged. This is why one training loop can serve many models.

### Check your understanding

1. Starting from `J = (1/n) Σ e_i²`, explain in your own words why `∂J/∂w` contains the input `x_i`.
2. Why does `∂J/∂b` not contain `x_i`?
3. For data `x = [1, 2]`, `y = [2, 4]` with `w = 0`, `b = 0`, calculate `∂J/∂w` and `∂J/∂b`.
4. If we use the `(1/2n)` convention, what do the gradient formulas become?

---

## 10. The Weight Update Rule

### 10.1 The formula

```
w_new = w_old − α · ∂J/∂w

b_new = b_old − α · ∂J/∂b
```

In general, for all parameters `θ` together:

```
θ := θ − α · ∇J(θ)
```

(The symbol `:=` means "is replaced by.")

### 10.2 Why the minus sign?

The gradient points **uphill**. We want to go **downhill**, so we subtract it.

| Slope at current position | `α · slope` | Effect on `w` | Result |
|---|---|---|---|
| Negative (e.g. −6) | Negative | `w` increases | Moves right, toward the valley |
| Positive (e.g. +4) | Positive | `w` decreases | Moves left, toward the valley |
| Zero | Zero | `w` unchanged | Already at the bottom, so we stop |

### 10.3 Why steps shrink automatically

The step size is `α × slope`. Near the bottom of the valley the slope flattens, so the steps naturally get smaller even though `α` stays fixed. This lets gradient descent settle smoothly instead of bouncing around.

### 10.4 Simultaneous update (important)

Compute **both** gradients using the **old** values, and only then update both parameters:

```
dw = ∂J/∂w   (using w_old, b_old)
db = ∂J/∂b   (using w_old, b_old)

w = w − α · dw
b = b − α · db
```

A common bug is updating `w` first and then calculating `db` with the already-updated `w`. That mixes old and new values and gives the wrong direction.

### 10.5 The algorithm

```
1. Initialize w and b (zeros or small random numbers)
2. Repeat until stopping:
     a. Compute predictions:   ŷ = w·x + b
     b. Compute the cost:      J
     c. Compute gradients:     dw, db
     d. Update parameters:     w = w − α·dw,  b = b − α·db
3. Return the final w and b
```

### Check your understanding

1. Why do we subtract the gradient rather than add it?
2. If the slope is `+8` and `α = 0.25`, by how much and in which direction does `w` move?
3. Why do the steps get smaller as we near the minimum, even with a constant learning rate?
4. What goes wrong if you update `w` before calculating the gradient for `b`?

---

## 11. The Learning Rate

The learning rate `α` controls the **size of each step**. It is a **hyperparameter**: you choose it, the model does not learn it.

| Learning rate | What happens | How it looks on the loss curve |
|---|---|---|
| **Too small** | Very slow progress, may need huge numbers of iterations | Loss decreases, but painfully slowly |
| **Just right** | Steady descent to the minimum | Loss falls quickly, then flattens |
| **Too large** | Overshoots the minimum, bounces from side to side | Loss zig-zags or stays high |
| **Far too large** | Diverges: each step lands further away | Loss grows, may become `inf` or `NaN` |

### Practical advice

- Common starting values: `0.1`, `0.01`, `0.001`. Try several and plot the loss curve.
- **Always plot loss against iteration.** A healthy curve decreases and flattens.
- If the loss **increases** or becomes `NaN`, the learning rate is too large.
- **Feature scaling** (covered in the Data Preparation lesson) lets you use a larger learning rate and converge much faster, because features with very different ranges create a stretched, narrow valley that is hard to descend.
- **Learning rate schedules** (reducing `α` over time) and advanced optimizers (Momentum, RMSProp, Adam) improve on plain gradient descent. They matter most for deep learning and are not required in this phase.

### Check your understanding

1. What is a hyperparameter? Is the learning rate one?
2. Describe what the loss curve looks like when the learning rate is too large.
3. Your loss becomes `NaN` after a few iterations. What is the most likely cause and fix?
4. Why does feature scaling help gradient descent?

---

## 12. Full Worked Example

We will fit a line to a tiny dataset by hand, using every formula from above.

### Data

| i | x | y |
|---|---|---|
| 1 | 1 | 3 |
| 2 | 2 | 5 |
| 3 | 3 | 7 |

The data follows `y = 2x + 1` exactly, so the ideal answer is `w = 2`, `b = 1`. Let us see if gradient descent finds it.

**Settings:** start with `w = 0`, `b = 0`, learning rate `α = 0.1`, `n = 3`.

### Iteration 1

**Predictions:** `ŷ = 0·x + 0 = [0, 0, 0]`

**Errors** `ŷ − y`: `[−3, −5, −7]`

**Cost:**
```
J = (9 + 25 + 49) / 3 = 27.667
```

**Gradients:**
```
∂J/∂w = (2/3) · (1·(−3) + 2·(−5) + 3·(−7))
      = (2/3) · (−34)
      = −22.667

∂J/∂b = (2/3) · (−3 − 5 − 7)
      = (2/3) · (−15)
      = −10.000
```

**Update:**
```
w = 0 − 0.1 · (−22.667) = 2.267
b = 0 − 0.1 · (−10.000) = 1.000
```

### Iteration 2

**Predictions:** `ŷ = 2.267·x + 1 = [3.267, 5.533, 7.800]`

**Errors:** `[0.267, 0.533, 0.800]`

**Cost:**
```
J = (0.071 + 0.284 + 0.640) / 3 = 0.332
```

**Gradients:**
```
∂J/∂w = (2/3) · (1·0.267 + 2·0.533 + 3·0.800) = (2/3) · 3.733 = 2.489
∂J/∂b = (2/3) · (0.267 + 0.533 + 0.800)       = (2/3) · 1.600 = 1.067
```

**Update:**
```
w = 2.267 − 0.1 · 2.489 = 2.018
b = 1.000 − 0.1 · 1.067 = 0.893
```

### Iteration 3

**Predictions:** `ŷ = 2.018·x + 0.893 = [2.911, 4.929, 6.947]`

**Errors:** `[−0.089, −0.071, −0.053]`

**Cost:** `J ≈ 0.0053`

**Gradients:**
```
∂J/∂w = (2/3) · (−0.391) = −0.261
∂J/∂b = (2/3) · (−0.213) = −0.142
```

**Update:**
```
w = 2.018 + 0.026 = 2.044
b = 0.893 + 0.014 = 0.908
```

### Results table

| Iteration | w (start) | b (start) | Cost J | ∂J/∂w | ∂J/∂b | w (new) | b (new) |
|---|---|---|---|---|---|---|---|
| 1 | 0.000 | 0.000 | 27.667 | −22.667 | −10.000 | 2.267 | 1.000 |
| 2 | 2.267 | 1.000 | 0.332 | 2.489 | 1.067 | 2.018 | 0.893 |
| 3 | 2.018 | 0.893 | 0.0053 | −0.261 | −0.142 | 2.044 | 0.908 |

### What to notice

1. **The cost collapses:** 27.667, then 0.332, then 0.0053. Most of the learning happens in the first steps.
2. **Overshoot:** in iteration 1, `w` jumped past its target of 2 (to 2.267). The gradient then turned positive and pulled it back. This gentle back-and-forth is normal.
3. **Gradient signs matter:** a negative gradient increased the parameter, a positive gradient decreased it.
4. **Convergence:** with more iterations, `w` approaches 2 and `b` approaches 1, and the gradients shrink toward zero.

### Check your understanding

1. In iteration 1, why were both gradients negative?
2. Why did `w` move down in iteration 2?
3. Redo iteration 1 using `α = 0.05`. What are the new `w` and `b`? Is the cost after one step higher or lower than with `α = 0.1`?
4. Using `x = [1, 2]`, `y = [2, 4]`, `w = 0`, `b = 0`, `α = 0.1`, compute one full update of `w` and `b`.

---

## 13. Variants of Gradient Descent

The versions differ only in **how much data is used to compute each gradient**.

| Variant | Data per update | Updates per epoch | Pros | Cons |
|---|---|---|---|---|
| **Batch GD** | The entire dataset | 1 | Smooth, stable path | Slow and memory-heavy for large data |
| **Stochastic GD (SGD)** | 1 example | `n` | Fast updates, can escape shallow local minima | Noisy, zig-zag path |
| **Mini-batch GD** | A small batch (e.g. 32 or 64) | `n / batch size` | Good balance of speed and stability | Needs a batch size choice |

**Epoch:** one complete pass through the entire training set.

**Mini-batch gradient descent** is the standard choice in practice, especially in deep learning.

The update rule is identical in all three. Only the examples used to compute `∂J/∂w` change. For SGD with a single example `i`:

```
∂J/∂w ≈ 2 · (ŷ_i − y_i) · x_i
∂J/∂b ≈ 2 · (ŷ_i − y_i)
```

### Check your understanding

1. What is an epoch?
2. Why is SGD's path noisy compared with batch gradient descent?
3. A dataset has 1,000 examples and you use mini-batches of 50. How many updates happen per epoch?
4. Why is mini-batch gradient descent usually preferred in practice?

---

## 14. When Do We Stop Training?

| Criterion | Idea |
|---|---|
| **Fixed number of epochs** | Run a set number of iterations (for example 1,000) |
| **Tolerance** | Stop when the cost improvement is tiny: `\|J_old − J_new\| < ε` |
| **Small gradient** | Stop when the gradient magnitude is near zero |
| **Early stopping** | Stop when the loss on validation data stops improving (guards against overfitting, which links to the previous lesson) |

### Check your understanding

1. Why is a near-zero gradient a sensible stopping signal?
2. How does early stopping help prevent overfitting?

---

## 15. Gradient Descent From Scratch in Python

```python
import numpy as np
import matplotlib.pyplot as plt

# Data: y = 2x + 1
X = np.array([1, 2, 3], dtype=float)
y = np.array([3, 5, 7], dtype=float)

# Initialize parameters and hyperparameters
w, b = 0.0, 0.0
alpha = 0.1
epochs = 1000
n = len(X)

loss_history = []

for epoch in range(epochs):
    # 1. Forward pass: predictions
    y_pred = w * X + b

    # 2. Error and cost (MSE)
    error = y_pred - y
    cost = np.mean(error ** 2)
    loss_history.append(cost)

    # 3. Gradients (using the old w and b)
    dw = (2 / n) * np.sum(error * X)
    db = (2 / n) * np.sum(error)

    # 4. Update parameters
    w = w - alpha * dw
    b = b - alpha * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch:4d} | cost = {cost:.6f} | w = {w:.4f} | b = {b:.4f}")

print(f"\nFinal parameters: w = {w:.4f}, b = {b:.4f}")

# Plot the loss curve
plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Cost (MSE)")
plt.title("Loss curve")
plt.show()
```

**What to expect:** the cost drops sharply and then flattens close to zero, while `w` approaches 2 and `b` approaches 1.

**Experiments to try:**
- Change `alpha` to `0.01`, `0.05`, `0.2`, `0.5` and compare the loss curves. Note when it diverges.
- Replace the data with noisy values and see the cost settle above zero.
- Verify your hand calculations from Section 12 against the printed output.

### Using scikit-learn

```python
from sklearn.linear_model import SGDRegressor

model = SGDRegressor(learning_rate="constant", eta0=0.01, max_iter=1000)
model.fit(X.reshape(-1, 1), y)
print(model.coef_, model.intercept_)
```

(For small linear regression problems, scikit-learn's `LinearRegression` solves for the best parameters directly using the **normal equation** instead of iterating, which you will see in the Linear Regression lesson.)

### Check your understanding

1. In the code, which line computes the cost and which lines compute the gradients?
2. Why do we store `loss_history`?
3. What would you expect to see if you set `alpha = 0.5`?

---

## 16. Common Problems and Fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Loss increases or becomes `NaN` | Learning rate too large | Reduce `α` (try dividing by 10) |
| Loss decreases extremely slowly | Learning rate too small, or unscaled features | Increase `α`, scale features |
| Loss stuck at a high value | Underfitting or poor initialization | More expressive model, check data |
| Results differ from hand calculation | Updated `w` before computing `db` | Compute both gradients first |
| Training loss low, validation loss high | Overfitting | Regularization, more data, early stopping |
| Loss zig-zags heavily | Learning rate slightly too large, or SGD noise | Lower `α` or use mini-batches |

---

## 17. Formula Cheat Sheet

| Concept | Formula |
|---|---|
| Linear model | `ŷ = w·x + b` |
| Error | `e_i = ŷ_i − y_i` |
| MSE | `(1/n) · Σ (y_i − ŷ_i)²` |
| RMSE | `√MSE` |
| MAE | `(1/n) · Σ \|y_i − ŷ_i\|` |
| Sigmoid | `σ(z) = 1 / (1 + e^(−z))` |
| Binary cross-entropy | `−(1/n) · Σ [ y·ln(p) + (1 − y)·ln(1 − p) ]` |
| Gradient of MSE w.r.t. `w` | `(2/n) · Σ (ŷ_i − y_i) · x_i` |
| Gradient of MSE w.r.t. `b` | `(2/n) · Σ (ŷ_i − y_i)` |
| Gradient of log loss w.r.t. `w` | `(1/n) · Σ (p_i − y_i) · x_i` |
| Matrix form (MSE) | `∇J = (2/n) · Xᵀ(Xθ − y)` |
| Update rule | `θ := θ − α · ∇J(θ)` |
| Updates per epoch (mini-batch) | `n / batch size` |

---

## 18. Summary

- A model improves by repeatedly measuring its error and adjusting its parameters.
- The **loss** is the error on one example, and the **cost** is the average over all examples.
- **MSE** is the standard regression loss. **Cross-entropy** is the standard classification loss.
- The **gradient** is the vector of partial derivatives and points toward steepest increase of the cost.
- For linear regression with MSE: `∂J/∂w = (2/n) Σ (ŷ − y)·x` and `∂J/∂b = (2/n) Σ (ŷ − y)`.
- The **update rule** is `θ := θ − α · ∇J`. We subtract because the gradient points uphill.
- The **learning rate** controls step size: too small is slow, too large diverges.
- Update all parameters **simultaneously** using the old values.
- Batch, stochastic and mini-batch gradient descent differ only in how much data is used per update.
- Always **plot the loss curve** to confirm training is healthy.

---

## 19. Answers to Numerical Questions

| Section | Question | Answer |
|---|---|---|
| 3 | Prediction for `w=3, b=2, x=4` | `3·4 + 2 = 14` |
| 5 | Actual `[5,8,12]`, predicted `[6,7,15]` | Errors `[−1, 1, −3]`. MSE = `(1+1+9)/3 = 3.67`, MAE = `(1+1+3)/3 = 1.67`, RMSE = `√3.67 = 1.91` |
| 6 | BCE for `y=1, p=0.5` | `−ln(0.5) = 0.693` |
| 6 | Loss for `y=0, p=0.2` | `−ln(0.8) = 0.223`, which is **smaller** than `−ln(0.1) = 2.303` for `p=0.9` |
| 8 | Derivative of `(w−5)²` at `w=1` | `2(w−5) = 2(1−5) = −8` |
| 9 | `x=[1,2]`, `y=[2,4]`, `w=0`, `b=0` | Errors `[−2, −4]`. `∂J/∂w = (2/2)(−2 − 8) = −10`, `∂J/∂b = (2/2)(−6) = −6` |
| 10 | Slope `+8`, `α = 0.25` | `w` moves by `0.25 × 8 = 2` **downward** (decreases by 2) |
| 12 | Iteration 1 with `α = 0.05` | `w = 0 − 0.05(−22.667) = 1.133`, `b = 0.5`. Cost is higher than with `α = 0.1` after one step, because the step is smaller |
| 12 | `x=[1,2]`, `y=[2,4]`, `α=0.1` | Gradients `−10` and `−6`, so `w = 1.0`, `b = 0.6` |
| 13 | 1,000 examples, batch 50 | `1000 / 50 = 20` updates per epoch |
| Lesson 2 | Predictions `[70, 90]` vs actual `[80, 85]` | Errors `[−10, 5]`. MSE = `(100 + 25)/2 = 62.5` |

---

