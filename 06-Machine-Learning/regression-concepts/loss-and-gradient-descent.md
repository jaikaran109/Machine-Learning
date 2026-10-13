## 1. The Big Idea

A model starts with random settings, so its first predictions are bad. To get better it must do two things:

1. **Measure how wrong it is.** This is the job of the **loss function**.
2. **Change its settings to be less wrong.** This is the job of **gradient descent**.

**Analogy:** You are on a foggy mountain and want to reach the valley. You can't see it, but you can feel the slope under your feet. So you step downhill, feel the slope again, and repeat.

| Mountain | Machine learning |
|---|---|
| Your height | The error (loss) |
| The valley | The best model (lowest loss) |
| Feeling the slope | Calculating the gradient |
| Taking a step | Updating the parameters |
| Step size | Learning rate |

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Parameters** | The values inside a model that training adjusts (e.g. `w` and `b` in `ŷ = w·x + b`). | The model's dials. |
| **Prediction (ŷ)** | The model's output for an input. | The model's guess. |
| **Error** | The difference between the prediction and the real value: `ŷ − y`. | How far off one guess was. |
| **Loss function** | A formula that turns the error of **one example** into a single number. | Score for one mistake. |
| **Cost function (J)** | The **average loss over all training examples**. | Score for the whole model. |
| **Gradient** | The slope of the cost with respect to a parameter. It shows which way, and how steeply, the cost rises. | The direction of "uphill". |
| **Gradient descent** | An algorithm that repeatedly moves the parameters in the direction that lowers the cost. | Walking downhill step by step. |
| **Learning rate (α)** | A number that sets how big each step is. | Step size. |
| **Epoch** | One full pass through the training data. | One round of study. |

---

## 3. Loss Function

### Concept

A loss function answers: **"How bad was this prediction?"** A small value means a good prediction, and a large value means a bad one. Training is simply the search for parameters that make the cost as small as possible.

### Mean Squared Error (MSE): for regression

```
MSE = (1/n) · Σ (y − ŷ)²
```

**Steps:** find each error, square it, then average.

**Why square the errors?**
- Squaring makes all errors positive, so over- and under-predictions can't cancel out.
- Big mistakes are punished much more than small ones (10² = 100, 2² = 4).

**Example:** actual `[10, 20, 30]`, predicted `[12, 18, 33]`. Errors are `2, −2, 3`.
`MSE = (4 + 4 + 9) / 3 = 5.67`

### Other losses (know the names)

| Loss | Used for | Idea |
|---|---|---|
| **MAE** `mean(\|y − ŷ\|)` | Regression with outliers | Average size of the error, less sensitive to extreme values |
| **Binary cross-entropy (log loss)** | Classification (e.g. Logistic Regression) | Heavily punishes confident wrong probabilities |

For classification, the model outputs a probability `p`. If the true label is 1 and the model says `p = 0.9`, the loss is small (0.105). If it says `p = 0.1`, the loss is large (2.303). Confident and wrong is punished the most.

---

## 4. Gradient

### Concept

The **gradient is the slope of the cost curve** at your current position. It tells you two things:

| Slope | What it means | What to do |
|---|---|---|
| **Negative** | Cost falls as the parameter increases | Increase the parameter |
| **Positive** | Cost rises as the parameter increases | Decrease the parameter |
| **Zero** | Flat ground, you are at the bottom | Stop |

For a model with several parameters, we find the slope for each one separately (a **partial derivative**, written `∂J/∂w`).

### Gradient for linear regression (the formulas to remember)

With `ŷ = w·x + b` and `J = (1/n) · Σ (ŷ − y)²`:

```
∂J/∂w = (2/n) · Σ (ŷ − y) · x

∂J/∂b = (2/n) · Σ (ŷ − y)
```

**How to read them:**
- `∂J/∂b` is twice the **average error**.
- `∂J/∂w` is twice the **average of (error × input)**. It contains `x` because `w` multiplies `x`, so the input decides how strongly `w` affects each error.

**Where they come from (the idea):** differentiate the squared error using the chain rule. The square brings down a 2, and the derivative of the error with respect to `w` is `x`, and with respect to `b` is `1`.

---

## 5. Gradient Descent

### Concept

Gradient descent moves the parameters **opposite to the gradient**, because the gradient points uphill and we want to go downhill.

### The update rule

```
w = w − α · ∂J/∂w

b = b − α · ∂J/∂b
```

**Why the minus sign?**
- Slope negative: `w − α·(negative)` makes `w` **bigger**, moving toward the valley.
- Slope positive: `w − α·(positive)` makes `w` **smaller**, moving toward the valley.

**Steps shrink automatically:** near the bottom the slope flattens, so `α × slope` becomes small and the model settles smoothly.

**Important:** calculate both gradients first using the old values, then update both `w` and `b` together.

### The algorithm

```
1. Start with w and b (zeros or small random numbers)
2. Repeat:
     a. Predict:    ŷ = w·x + b
     b. Measure:    compute the cost J
     c. Gradient:   compute ∂J/∂w and ∂J/∂b
     d. Update:     w = w − α·∂J/∂w,   b = b − α·∂J/∂b
3. Stop when the cost stops improving
```

### Learning rate

| Learning rate | Result |
|---|---|
| **Too small** | Learns, but extremely slowly |
| **Just right** | Steady descent to the minimum |
| **Too large** | Overshoots and bounces around, or the cost explodes (`NaN`) |

Common starting values are `0.1`, `0.01` and `0.001`. Always plot the cost against the epoch number: a healthy curve falls and then flattens.

### Variants (just the idea)

| Type | Uses per update |
|---|---|
| **Batch** | All the data (stable but slow) |
| **Stochastic (SGD)** | One example (fast but noisy) |
| **Mini-batch** | A small group, such as 32 (the usual choice) |

---

## 6. Worked Example (one step)

Data: `x = [1, 2, 3]`, `y = [3, 5, 7]` (the true line is `y = 2x + 1`).
Start: `w = 0`, `b = 0`, `α = 0.1`.

| Step | Calculation | Result |
|---|---|---|
| Predict | `ŷ = 0·x + 0` | `[0, 0, 0]` |
| Errors `ŷ − y` | | `[−3, −5, −7]` |
| Cost | `(9 + 25 + 49) / 3` | `27.67` |
| `∂J/∂w` | `(2/3)·(1·(−3) + 2·(−5) + 3·(−7))` | `−22.67` |
| `∂J/∂b` | `(2/3)·(−3 − 5 − 7)` | `−10` |
| New `w` | `0 − 0.1·(−22.67)` | `2.27` |
| New `b` | `0 − 0.1·(−10)` | `1.0` |

After one step the parameters jump from `(0, 0)` to `(2.27, 1.0)`, already close to the true `(2, 1)`. Repeating the loop makes `w` approach 2 and `b` approach 1, and the cost approaches 0.

---

## 7. Summary

- **Loss function:** measures how wrong a prediction is. **Cost** is its average over all data.
- **MSE** is the standard loss for regression. **Cross-entropy** is the standard for classification.
- **Gradient:** the slope of the cost. It shows which direction is uphill.
- **Gradient descent:** repeatedly step opposite to the gradient to lower the cost.
- **Update rule:** `parameter = parameter − learning rate × gradient`.
- **Learning rate:** too small is slow, too large diverges.

---
