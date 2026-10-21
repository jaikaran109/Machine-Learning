> The slope of a function that has many inputs, measured one input at a time.

---

## 1. The Big Idea

In the last note, the function had **one** input, `f(x)`, so there was only one slope. But real ML models have **many** settings (parameters). Even simple linear regression has two: `w` and `b`. The loss depends on **both**, so we need a way to ask how it changes with each one.

A **partial derivative** is the slope of a function with respect to **one input**, while every other input is **held still**.

**Analogy (a hillside):** you stand on a hill. If you walk **east**, the ground might rise steeply. If you walk **north**, it might be nearly flat. The slope depends on the direction. A partial derivative is the slope when you walk in **one chosen direction** (say east) without moving in the other.

| Walking | Slope |
|---|---|
| East only | Partial derivative with respect to the east position |
| North only | Partial derivative with respect to the north position |

**Why we need it in ML:** each parameter has its own slope. The model uses one partial derivative per parameter to decide how to change that parameter.

---

## 2. Key Terms in Plain Words

| Term | Meaning | Example |
|---|---|---|
| **Function of several variables** | A function with more than one input | `f(x, y) = x² + y²` |
| **Partial derivative** | The derivative with respect to **one** variable, treating the others as constants | `∂f/∂x` |
| **∂ (curly d)** | The symbol for a partial derivative, read "partial" or "del" | `∂f/∂x` reads "partial f partial x" |
| **Held constant** | Treated like an ordinary fixed number | In `∂f/∂x`, `y` is a fixed number |
| **Surface** | The graph of a two-input function (height over the `x`-`y` plane) | A bowl for `x² + y²` |
| **Slice** | A cut through the surface that keeps one input fixed | The slice `y = 2` |
| **Parameter** | A setting the model learns | `w`, `b` |
| **Gradient** | The vector that collects **all** partial derivatives (next topic) | `[∂f/∂x, ∂f/∂y]` |

**Notation:** `∂f/∂x` is also written `fₓ`, and `∂f/∂y` is written `f_y`. For a single-input function we use the ordinary `d` (`df/dx`). The curly `∂` signals that other variables exist.

---

## 3. The Definition

For `f(x, y)`, the partial derivative with respect to `x` is:

```
∂f/∂x = lim   [ f(x + h, y) − f(x, y) ] / h
        h→0
```

**Reading it:** nudge only `x` by a tiny `h`, keep `y` fixed, and see how `f` changes. Likewise:

```
∂f/∂y = lim   [ f(x, y + h) − f(x, y) ] / h
        h→0
```

### The slice picture

Take the bowl `f(x, y) = x² + y²`. To find `∂f/∂x` at `y = 2`:

1. **Fix** `y = 2`. The function becomes `f(x) = x² + 4`, a curve in one variable.
2. Take the ordinary derivative: `2x`.

So `∂f/∂x = 2x`. We took a slice of the surface and found its slope, which is all a partial derivative is.

---

## 4. How to Calculate a Partial Derivative

**The one rule:** to find `∂f/∂x`, treat **every other variable as a constant**, then differentiate normally. All the rules from the Derivatives note (power, sum, product, chain) still apply.

### Example 1: `f(x, y) = x² + y²`

| Partial | Steps | Result |
|---|---|---|
| `∂f/∂x` | `x²` becomes `2x`. `y²` is a constant, so it becomes `0`. | `2x` |
| `∂f/∂y` | `x²` is a constant, so it becomes `0`. `y²` becomes `2y`. | `2y` |

### Example 2: `f(x, y) = x² + 3xy + y²`

| Partial | Steps | Result |
|---|---|---|
| `∂f/∂x` | `x²` gives `2x`. In `3xy`, `3y` is a constant multiplier of `x`, so it gives `3y`. `y²` gives `0`. | `2x + 3y` |
| `∂f/∂y` | `x²` gives `0`. In `3xy`, `3x` is the constant multiplier, so it gives `3x`. `y²` gives `2y`. | `3x + 2y` |

**Evaluate at the point `(1, 2)`:**

```
∂f/∂x = 2(1) + 3(2) = 8
∂f/∂y = 3(1) + 2(2) = 7
```

**Sanity check with a tiny nudge.** `f(1, 2) = 1 + 6 + 4 = 11`.

```
Nudge x by 0.01:  f(1.01, 2) = 11.0801   →  (11.0801 − 11) / 0.01 = 8.01  ≈ 8 ✓
Nudge y by 0.01:  f(1, 2.01) = 11.0701   →  (11.0701 − 11) / 0.01 = 7.01  ≈ 7 ✓
```

### Example 3: `f(x, y) = x²y`

```
∂f/∂x = 2xy      (y is a constant multiplier)
∂f/∂y = x²       (x² is a constant multiplier)
```

### Example 4: three inputs, `f(x, y, z) = xyz`

```
∂f/∂x = yz
∂f/∂y = xz
∂f/∂z = xy
```

---

## 5. What a Partial Derivative Tells You

At a point, each partial derivative gives the slope **in that variable's own direction**.

| At `(1, 2)` for `f = x² + 3xy + y²` | Value | Meaning |
|---|---|---|
| `∂f/∂x` | 8 | Increasing `x` slightly **raises** `f` quickly (about 8 per unit) |
| `∂f/∂y` | 7 | Increasing `y` slightly raises `f` (about 7 per unit) |

The **sign** and **size** work as in ordinary derivatives:

| Partial derivative | Meaning for that variable |
|---|---|
| **Positive** | `f` rises as the variable increases, so to lower `f`, **decrease** the variable |
| **Negative** | `f` falls as the variable increases, so to lower `f`, **increase** the variable |
| **Zero** | `f` is flat in that direction |

**A minimum of a surface** occurs where **all** partial derivatives are zero at once. For `x² + y²`, `2x = 0` and `2y = 0` give `(0, 0)`, the bottom of the bowl.

---

## 6. Partial Derivatives in Machine Learning

### 6.1 A loss with two parameters

For linear regression, the cost depends on `w` and `b`:

```
J(w, b) = (1/n) · Σ (w·xᵢ + b − yᵢ)²
```

So we need **two** partial derivatives, `∂J/∂w` and `∂J/∂b`.

### 6.2 Deriving them with the chain rule

For **one** example, let the error be `u = w·x + b − y`, so the loss is `L = u²`.

```
∂L/∂w = (dL/du) · (∂u/∂w) = 2u · x
∂L/∂b = (dL/du) · (∂u/∂b) = 2u · 1 = 2u
```

Here `∂u/∂w = x` because `b` and `y` are constants when we focus on `w`, and `∂u/∂b = 1` because `w·x` and `y` are constants when we focus on `b`.

Averaging over all `n` examples gives the formulas you saw earlier:

```
∂J/∂w = (2/n) · Σ (ŷᵢ − yᵢ) · xᵢ
∂J/∂b = (2/n) · Σ (ŷᵢ − yᵢ)
```

### 6.3 A complete numeric example

Data: `x = [1, 2, 3]`, `y = [3, 5, 7]`. Start with `w = 0`, `b = 0`.

```
Predictions ŷ        = [0, 0, 0]
Errors (ŷ − y)       = [−3, −5, −7]

∂J/∂w = (2/3)·(1·(−3) + 2·(−5) + 3·(−7)) = (2/3)(−34) = −22.67
∂J/∂b = (2/3)·(−3 − 5 − 7)                 = (2/3)(−15) = −10
```

Both are **negative**, so increasing `w` and `b` lowers the loss. Each parameter is updated with **its own** partial derivative (learning rate `α = 0.1`):

```
w = 0 − 0.1·(−22.67) = 2.27
b = 0 − 0.1·(−10)    = 1.00
```

### 6.4 A picture with a simple bowl

Let the loss be `J(w, b) = w² + b²`, so `∂J/∂w = 2w` and `∂J/∂b = 2b`. Start at `(w, b) = (3, 4)`, where `J = 9 + 16 = 25`.

```
∂J/∂w = 2(3) = 6
∂J/∂b = 2(4) = 8

With α = 0.1:   w = 3 − 0.1·6 = 2.4
                b = 4 − 0.1·8 = 3.2
New loss: 2.4² + 3.2² = 5.76 + 10.24 = 16
```

The loss dropped from 25 to 16 in one step. Notice that `b` moved **more** than `w`, because the surface is steeper in the `b` direction.

### 6.5 Where else partial derivatives appear

| Place | Role |
|---|---|
| **Linear and logistic regression** | One partial derivative per weight, plus one for the bias |
| **Neural networks** | Thousands or millions of weights, each with its own partial derivative (found by backpropagation) |
| **Finding the minimum** | All partial derivatives equal zero |

---

## 7. Ordinary vs Partial Derivatives

| | Ordinary derivative | Partial derivative |
|---|---|---|
| **Function** | One input, `f(x)` | Several inputs, `f(x, y, ...)` |
| **Symbol** | `df/dx` | `∂f/∂x` |
| **Other variables** | None | Held constant |
| **Result** | One slope | One slope per input |

---

## 8. In Code

### Numerical partial derivatives

```python
def f(x, y):
    return x**2 + 3*x*y + y**2

h = 1e-5
dfdx = (f(1 + h, 2) - f(1, 2)) / h     # about 8
dfdy = (f(1, 2 + h) - f(1, 2)) / h     # about 7
print(dfdx, dfdy)
```

### Exact partial derivatives with SymPy

```python
import sympy as sp

x, y = sp.symbols("x y")
f = x**2 + 3*x*y + y**2

print(sp.diff(f, x))                       # 2*x + 3*y
print(sp.diff(f, y))                       # 3*x + 2*y
print(sp.diff(f, x).subs({x: 1, y: 2}))    # 8
print(sp.diff(f, y).subs({x: 1, y: 2}))    # 7
```

### The regression partial derivatives in NumPy

```python
import numpy as np

X = np.array([1.0, 2.0, 3.0])
y = np.array([3.0, 5.0, 7.0])
w, b = 0.0, 0.0
n = len(X)

error = (w * X + b) - y
dJ_dw = (2 / n) * np.sum(error * X)    # -22.67
dJ_db = (2 / n) * np.sum(error)        # -10.0
print(dJ_dw, dJ_db)
```

---

## 9. Common Mistakes

| Mistake | Fix |
|---|---|
| Differentiating the "other" variable too | Treat it as a **constant**: its own derivative term becomes 0 |
| Using `d` instead of `∂` | Use `∂` for functions with several inputs |
| Forgetting the constant multiplier | In `3xy`, `∂/∂x` gives `3y`, not just `3` |
| Updating `w` before computing the partial for `b` | Compute **all** partials with the old values, then update together |
| Thinking a zero partial means a minimum | The surface may still slope in another direction. All partials must be zero (and the shape checked). |

---

## 10. Summary

- A **partial derivative** is the slope of a many-input function with respect to **one** input, holding the others **constant**.
- Notation: `∂f/∂x`. Procedure: treat the other variables as constants and differentiate normally.
- Geometrically, it is the slope of a **slice** of the surface.
- Each parameter has its **own** partial derivative, so a model with `w` and `b` has `∂J/∂w` and `∂J/∂b`.
- For linear regression: `∂J/∂w = (2/n) Σ (ŷ − y)·x` and `∂J/∂b = (2/n) Σ (ŷ − y)`.
- A positive partial means decrease that parameter to lower the loss, and a negative partial means increase it.
- All partial derivatives collected together form the **gradient** (next topic).

---

## 11. Practice Questions

1. In your own words, what is a partial derivative, and how is it different from an ordinary derivative?
2. Find `∂f/∂x` and `∂f/∂y` for `f(x, y) = x² + y²`.
3. Find both partial derivatives of `f(x, y) = 3x²y + 2y`.
4. For `f(x, y) = x² + 3xy + y²`, calculate `∂f/∂x` and `∂f/∂y` at the point `(2, 1)`.
5. Find all three partial derivatives of `f(x, y, z) = xyz + z²`.
6. What is `∂f/∂x` for `f(x, y) = 5y + 7`? Why?
7. For `J(w, b) = w² + b²`, take one gradient descent step from `(3, 4)` with `α = 0.1`. What is the new `J`?
8. A single-example loss is `L = (w·x + b − y)²`. With `x = 2`, `y = 5`, `w = 1`, `b = 1`, find `∂L/∂w` and `∂L/∂b`.
9. Why does `∂L/∂b` not contain `x`, while `∂L/∂w` does?
10. Data `x = [1, 2]`, `y = [3, 5]`, with `w = 1`, `b = 0`. Calculate `∂J/∂w` and `∂J/∂b` for the average squared-error cost.
11. At some point, `∂f/∂x` is positive and `∂f/∂y` is negative. To reduce `f`, should you increase or decrease `x`? And `y`?
12. Where are `∂f/∂x` and `∂f/∂y` for `f = x² + y²` both zero? What is that point?

### Answers

1. A partial derivative is the slope of a many-input function in one variable's direction, with the other variables held fixed. An ordinary derivative is for a function of a single input.
2. `∂f/∂x = 2x` and `∂f/∂y = 2y`.
3. `∂f/∂x = 6xy` and `∂f/∂y = 3x² + 2`.
4. `∂f/∂x = 2x + 3y = 4 + 3 = 7` and `∂f/∂y = 3x + 2y = 6 + 2 = 8`.
5. `∂f/∂x = yz`, `∂f/∂y = xz`, `∂f/∂z = xy + 2z`.
6. `0`, because `x` does not appear in the function, so `f` does not change when `x` changes.
7. `∂J/∂w = 6`, `∂J/∂b = 8`. New point `(2.4, 3.2)`, new `J = 5.76 + 10.24 = 16`.
8. `ŷ = 1·2 + 1 = 3`, `u = 3 − 5 = −2`. `∂L/∂w = 2(−2)(2) = −8` and `∂L/∂b = 2(−2) = −4`.
9. `∂u/∂b = 1` because `b` is simply added, while `∂u/∂w = x` because `w` is multiplied by `x`.
10. `ŷ = [1, 2]`, errors `ŷ − y = [−2, −3]`. `∂J/∂w = (2/2)(1·(−2) + 2·(−3)) = −8` and `∂J/∂b = (2/2)(−2 − 3) = −5`.
11. **Decrease** `x` (positive slope means `f` rises as `x` rises) and **increase** `y` (negative slope means `f` falls as `y` rises).
12. `2x = 0` and `2y = 0` give `(0, 0)`, the bottom of the bowl, where `f = 0` is the minimum.
