> Why models make mistakes, and why fixing one kind of mistake tends to create the other.

---

## 1. The Big Idea

A model's errors on new data come from two opposite problems:

- **Bias:** the model is **too simple**, so it is wrong in the same way every time.
- **Variance:** the model is **too sensitive**, so its answers change a lot with the training data.

Making a model more complex lowers bias but raises variance. Making it simpler does the reverse. We look for the **sweet spot** in between.

**Analogy (exam preparation):**

| Student | Behavior | Problem |
|---|---|---|
| **A** | Learns one fixed shortcut and applies it to every question | **High bias.** Wrong the same way every time. |
| **B** | Memorizes last year's papers, and changes answers with every new paper seen | **High variance.** Unreliable. |
| **C** | Understands the concepts | **Balanced.** |

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Bias** | The gap between the model's **average prediction** (over many training sets) and the true value. | Consistently off target. |
| **Variance** | How much the model's predictions **change** when trained on different samples. | Unstable. |
| **Irreducible error** | Randomness in the data that no model can remove. | The unavoidable part. |
| **Underfitting** | High bias, low variance. | Too simple. |
| **Overfitting** | Low bias, high variance. | Too complex. |

---

## 3. The Formula

```
Expected Error = Bias² + Variance + Irreducible Error
```

We cannot reduce the last term, so the goal is to **minimize Bias² + Variance**.

---

## 4. The Tradeoff

| | Simple model | Complex model |
|---|---|---|
| **Bias** | High | Low |
| **Variance** | Low | High |
| **Fit** | Underfitting | Overfitting |

As complexity grows, bias falls and variance rises. Total test error forms a **U-shape**, and the best model sits at the bottom of the U.

---

## 5. Worked Example

The true price of a house is **100** (₹ lakh). Each model is trained on 4 different samples of data, and we record its prediction for this house.

| Model | Predictions | Average | Bias | Bias² | Variance | Bias² + Variance |
|---|---|---|---|---|---|---|
| **A (too simple)** | 80, 82, 78, 80 | 80 | −20 | 400 | 2 | **402** |
| **B (too complex)** | 90, 110, 95, 105 | 100 | 0 | 0 | 62.5 | **62.5** |
| **C (balanced)** | 97, 101, 98, 100 | 99 | −1 | 1 | 2.5 | **3.5** |

**How to calculate (Model B):**
1. Average = `(90 + 110 + 95 + 105) / 4 = 100`
2. Bias = average − true = `100 − 100 = 0`
3. Deviations from the average: `−10, +10, −5, +5`
4. Variance = average of squared deviations = `(100 + 100 + 25 + 25) / 4 = 62.5`

**Reading the table:**
- **A** is stable but far from 100 (high bias).
- **B** is correct on average but jumps around (high variance).
- **C** has a little of each and the lowest total.

---

## 6. Diagnose and Fix

| Training error | Test error | Problem | Fix |
|---|---|---|---|
| High | High (close to training) | **High bias** | More flexible model, more features, less regularization |
| Low | Much higher | **High variance** | More data, simpler model, regularization, pruning, bagging |

---

## 7. Summary

- **Bias:** error from being too simple. **Variance:** error from being too sensitive.
- `Error = Bias² + Variance + Irreducible Error`.
- High bias is **underfitting**, and high variance is **overfitting**.
- More complexity means lower bias and higher variance, so test error is **U-shaped**.
- More data helps variance, but not bias.
- Random Forest mainly reduces variance, and boosting mainly reduces bias.

---
