> All the partial derivatives collected into one vector that points uphill, and the reason gradient descent works.

---

## 1. The Big Idea

In the last note, a function with many inputs had **one slope per input** (one partial derivative each). The **gradient** simply puts all of those slopes together into **one vector**.

That vector has a remarkable property: **it points in the direction where the function rises fastest.** So the opposite direction is where the function falls fastest, which is exactly where a model wants to go to reduce its loss.

**Analogy (a compass for hills):** you stand on a foggy hillside. Your feet can feel the slope in the east direction and in the north direction (the two partial derivatives). Put those two readings together and you get an arrow on the ground: a compass that points **straight uphill**, with a length that tells you how steep it is. Walk the opposite way to go downhill as fast as possible.

| Part of the compass | Gradient |
|---|---|
| Direction of the arrow | The way the function **increases fastest** |
| Length of the arrow | **How steep** the slope is |
| Opposite direction | The way the function **decreases fastest** |

---

## 2. Key Terms in Plain Words

| Term | Meaning | Example |
|---|---|---|
| **Gradient** | The vector of all partial derivatives of a function | `[∂f/∂x, ∂f/∂y]` |
| **∇f** | Notation for the gradient of `f` (the symbol ∇ is called "nabla" or "del") | `∇f = [2x, 2y]` |
| **Vector** | An ordered list of numbers | `[6, 8]` |
| **Magnitude of the gradient** | The length of the vector, `√(sum of squares)`, which measures steepness | `‖[6, 8]‖ = 10` |
| **Steepest ascent** | The direction in which the function rises fastest | The direction of `∇f` |
| **Steepest descent** | The direction in which the function falls fastest | The direction of `−∇f` |
| **Contour lines** | Lines joining points of equal height, like the lines on a hiking map | Circles for `x² + y²` |
| **Stationary point** | A point where the gradient is the zero vector | A minimum, maximum or saddle point |
| **Parameters (θ)** | All of a model's settings collected in a vector | `θ = [w, b]` |
| **Gradient descent** | Repeatedly stepping in the direction of `−∇J` to reduce the loss `J` | `θ := θ − α∇J` |

---

## 3. The Definition

For a function `f(x, y)` of two inputs:

```
∇f = [ ∂f/∂x ,  ∂f/∂y ]
```

For a function of `n` inputs, the gradient has `n` numbers, one partial derivative per input:

```
∇f = [ ∂f/∂x₁ , ∂f/∂x₂ , ... , ∂f/∂xₙ ]
```

**Important:** the gradient has the **same size as the input**. A model with 2 parameters has a gradient with 2 numbers. A neural network with a million parameters has a gradient with a million numbers.

---

## 4. Calculating a Gradient

**Method:** find each partial derivative (treat the other variables as constants), then list them in a vector.

### Example 1: `f(x, y) = x² + y²` (a bowl)

```
∂f/∂x = 2x      ∂f/∂y = 2y
∇f = [2x, 2y]
```

At the point `(3, 4)`:

```
∇f(3, 4) = [6, 8]
Magnitude = √(36 + 64) = 10
```

### Example 2: `f(x, y) = x² + 3xy + y²`

```
∇f = [2x + 3y,  3x + 2y]
At (1, 2):  ∇f = [2 + 6, 3 + 4] = [8, 7]
Magnitude = √(64 + 49) = √113 ≈ 10.63
```

### Example 3: `f(x, y, z) = xyz`

```
∇f = [yz, xz, xy]
At (1, 2, 3):  ∇f = [6, 3, 2]
Magnitude = √(36 + 9 + 4) = √49 = 7
```

---

## 5. Why the Gradient Points Uphill

### Rate of change in any direction

Suppose you walk in a direction given by a **unit vector** `u` (a vector of length 1). The rate at which `f` changes as you walk is:

```
rate of change = ∇f · u        (the dot product)
```

For `f = x² + y²` at `(3, 4)`, where `∇f = [6, 8]`:

| Direction `u` | Calculation | Rate of change | Meaning |
|---|---|---|---|
| `[1, 0]` (east) | `6·1 + 8·0` | **6** | This is just `∂f/∂x` |
| `[0, 1]` (north) | `6·0 + 8·1` | **8** | This is just `∂f/∂y` |
| `[0.6, 0.8]` (along the gradient) | `6·0.6 + 8·0.8 = 3.6 + 6.4` | **10** | The **largest** possible, equal to the magnitude |
| `[−0.6, −0.8]` (opposite) | `−3.6 − 6.4` | **−10** | The **fastest decrease** |
| `[0.8, −0.6]` (sideways) | `4.8 − 4.8` | **0** | No change: walking along a contour |

**The conclusion:** the rate of change is biggest when `u` points the same way as `∇f`. So:

- **`∇f` points toward the fastest increase**, and its length is that fastest rate.
- **`−∇f` points toward the fastest decrease.**

### Check with real numbers

At `(3, 4)`, `f = 25`. Take a small step of length 0.1 in each direction:

```
Along the gradient:  (3.06, 4.08) → f = 26.01   (rose by about 1.0, so 10 per unit)
Opposite:            (2.94, 3.92) → f = 24.01   (fell by about 1.0, so −10 per unit)
```

### The contour picture

For `f = x² + y²`, the contour lines are circles around the origin. At any point, the gradient points **straight outward**, crossing the circle at a right angle. In general, **the gradient is always perpendicular to the contour line.**

---

## 6. Gradient Descent in Vector Form

**Gradient descent** takes a step in the direction of the **negative** gradient:

```
θ_new = θ_old − α · ∇J(θ_old)
```

| Symbol | Meaning |
|---|---|
| `θ` | The vector of all parameters, such as `[w, b]` |
| `J` | The loss (cost) |
| `∇J` | The gradient of the loss: the slope for every parameter |
| `α` | The learning rate: the size of the step |

This single line updates **every parameter at once**, each by its own partial derivative:

```
[w_new, b_new] = [w, b] − α · [∂J/∂w, ∂J/∂b]
```

### Worked example: `f(x, y) = x² + y²`, start at `(3, 4)`, `α = 0.1`

Here `∇f = [2x, 2y]`, so each step gives `θ_new = θ − 0.1·2θ = 0.8·θ`.

| Step | Position | Gradient | Loss `f` |
|---|---|---|---|
| Start | (3, 4) | [6, 8] | 25 |
| 1 | (2.4, 3.2) | [4.8, 6.4] | 16 |
| 2 | (1.92, 2.56) | [3.84, 5.12] | 10.24 |
| 3 | (1.536, 2.048) | [3.07, 4.10] | 6.55 |

Each step moves toward `(0, 0)`, the minimum, and the steps shrink because the gradient shrinks as the slope flattens.

### The learning rate matters

For the same bowl, each step multiplies the position by `(1 − 2α)`:

| α | Factor | What happens |
|---|---|---|
| 0.1 | 0.8 | Smooth descent toward `(0, 0)` |
| 1.0 | −1 | Bounces forever between `(3, 4)` and `(−3, −4)`, never improving |
| 1.1 | −1.2 | **Diverges**: from `(3, 4)` the next point is `(−3.6, −4.8)` with loss 36, which is worse than 25 |

---

## 7. The Gradient of a Real Loss

### Linear regression

For `J(w, b) = (1/n) Σ (w·xᵢ + b − yᵢ)²`:

```
∇J = [ (2/n) Σ (ŷᵢ − yᵢ)·xᵢ ,   (2/n) Σ (ŷᵢ − yᵢ) ]
```

**Numeric example:** `x = [1, 2, 3]`, `y = [3, 5, 7]`, start with `w = 0`, `b = 0`.

```
Errors (ŷ − y) = [−3, −5, −7]

∂J/∂w = (2/3)(1·(−3) + 2·(−5) + 3·(−7)) = −22.67
∂J/∂b = (2/3)(−3 − 5 − 7)                 = −10

∇J = [−22.67, −10]        magnitude ≈ 24.78
```

Update with `α = 0.1`:

```
[w, b] = [0, 0] − 0.1·[−22.67, −10] = [2.27, 1.00]
```

The cost drops from 27.67 to about 0.33 in a single step.

### Compact matrix form

If `X` is the data matrix with a column of ones for the bias, and `θ = [w, b]`:

```
∇J = (2/n) · Xᵀ (Xθ − y)
```

For the example above, `X = [[1,1],[2,1],[3,1]]`, `Xθ − y = [−3, −5, −7]`, and `Xᵀ(Xθ − y) = [−34, −15]`, so `∇J = (2/3)·[−34, −15] = [−22.67, −10]`. ✓

### Other models

| Model | Gradient idea |
|---|---|
| **Logistic regression** | `∇J = (1/n) Σ (pᵢ − yᵢ)·xᵢ`: the same "(prediction − actual) × input" pattern |
| **Neural networks** | The gradient has one entry per weight, computed efficiently by **backpropagation** (the chain rule) |

---

## 8. When the Gradient Is Zero

If `∇f = [0, 0, ...]`, the point is **stationary**: the function is flat in every direction. There are three possibilities:

| Type | Shape | Gradient descent |
|---|---|---|
| **Minimum** | Bottom of a bowl | What we want |
| **Maximum** | Top of a hill | Rarely reached when descending |
| **Saddle point** | A mountain pass: up in one direction, down in another | Can slow training down |

For `f = x² + y²`, `∇f = [2x, 2y] = [0, 0]` only at `(0, 0)`, the minimum.

**Convex losses:** linear regression with MSE has a bowl-shaped loss with **one** minimum, so gradient descent reaches the best answer. Neural network losses are bumpy, with many local minima and saddle points.

---

## 9. A Caution: Steepest Is Not Always Straight to the Minimum

The negative gradient is the **steepest** way down from where you stand, which is not always the **direct** way to the minimum.

**Example:** `f(x, y) = x² + 10y²` (a long, narrow valley). At `(1, 1)`:

```
∇f = [2x, 20y] = [2, 20]
```

The steepest way down is almost entirely in the `y` direction, while the minimum at `(0, 0)` lies diagonally. So gradient descent **zig-zags** across the narrow valley.

**Fix:** **scale your features** so that the valley is rounder. This is why feature scaling makes gradient descent faster.

---

## 10. In Code

### Numerical gradient

```python
import numpy as np

def numerical_gradient(f, point, h=1e-5):
    point = np.array(point, dtype=float)
    grad = np.zeros_like(point)
    for i in range(len(point)):
        step = np.zeros_like(point)
        step[i] = h
        grad[i] = (f(point + step) - f(point)) / h
    return grad

f = lambda p: p[0]**2 + 3*p[0]*p[1] + p[1]**2
print(numerical_gradient(f, [1, 2]))      # about [8. 7.]
```

### Exact gradient with SymPy

```python
import sympy as sp

x, y = sp.symbols("x y")
f = x**2 + 3*x*y + y**2
gradient = [sp.diff(f, v) for v in (x, y)]
print(gradient)                                            # [2*x + 3*y, 3*x + 2*y]
print([g.subs({x: 1, y: 2}) for g in gradient])            # [8, 7]
```

### Gradient descent on a bowl

```python
import numpy as np

theta = np.array([3.0, 4.0])
alpha = 0.1

for step in range(1, 4):
    gradient = 2 * theta                  # ∇f for f = x² + y²
    theta = theta - alpha * gradient
    print(step, theta, (theta ** 2).sum())
# 1 [2.4 3.2]       about 16
# 2 [1.92 2.56]     about 10.24
# 3 [1.536 2.048]   about 6.55
```

### Linear regression gradient

```python
X = np.array([[1, 1], [2, 1], [3, 1]], dtype=float)   # x column and a column of ones
y = np.array([3, 5, 7], dtype=float)
theta = np.zeros(2)                                    # [w, b]

gradient = (2 / len(y)) * X.T @ (X @ theta - y)
print(gradient)                                        # about [-22.67 -10.]
```

---

## 11. Common Mistakes

| Mistake | Fix |
|---|---|
| Thinking the gradient points downhill | It points **uphill**, and gradient descent uses `−∇f` |
| Forgetting the minus sign in the update | `θ = θ − α∇J`, not `+` |
| Updating parameters one by one with new values | Compute the **whole** gradient first, then update all parameters together |
| Mixing up gradient and slope | A slope is one number (one variable). A gradient is a vector (many variables). |
| Assuming a zero gradient means a minimum | It could be a maximum or saddle point |
| Using a learning rate that is too large | The loss can bounce around or grow, so reduce `α` |

---

## 12. Summary

- The **gradient** `∇f` is the vector of **all partial derivatives**: `[∂f/∂x₁, ..., ∂f/∂xₙ]`.
- It has the **same number of entries as the inputs**, one slope per parameter.
- It points in the direction of **steepest increase**, and its **length** is how steep that is.
- The **negative gradient** points toward the **steepest decrease**.
- The gradient is **perpendicular to contour lines**, and the rate of change in direction `u` is `∇f · u`.
- **Gradient descent:** `θ_new = θ_old − α·∇J(θ_old)`.
- A **zero gradient** marks a minimum, a maximum or a saddle point.
- For linear regression: `∇J = [(2/n) Σ (ŷ − y)·x, (2/n) Σ (ŷ − y)]`, or `(2/n) Xᵀ(Xθ − y)`.
- Scale your features, because steepest is not always the straight path to the minimum.

---

## 13. Practice Questions

1. In your own words, what is a gradient, and how is it different from a partial derivative?
2. Find `∇f` for `f(x, y) = x² + y²`. Calculate it at `(3, 4)` and find its magnitude.
3. Find `∇f` for `f(x, y) = 3x²y + 2y`, then evaluate it at `(1, 2)`.
4. Find `∇f` for `f(x, y) = x² + 3xy + y²` at `(2, 1)`.
5. Find `∇f` for `f(x, y, z) = xyz` at `(1, 2, 3)`, and its magnitude.
6. Which direction does the gradient point? In which direction should gradient descent move?
7. At a point the gradient is `[4, −3]`. What is its magnitude, and what is the unit vector of steepest **descent**?
8. For `f = x² + y²`, take one gradient descent step from `(1, 2)` with `α = 0.25`. Compare the loss before and after.
9. For linear regression with `x = [1, 2]`, `y = [3, 5]`, start with `w = 1`, `b = 0`. Find `∇J`, take one step with `α = 0.1`, and compare the cost before and after.
10. At `(3, 4)` on `f = x² + y²`, the gradient is `[6, 8]`. What is the rate of change when walking in the direction `[0.8, −0.6]`? What does this mean?
11. For `f = x² + y²` starting at `(3, 4)`, what happens with `α = 1.0`?
12. A model has 500 parameters. How many numbers are in its gradient?
13. What does it mean if the gradient is the zero vector? Name three possibilities.

### Answers

1. A partial derivative is the slope in one variable's direction (one number). The gradient collects **all** of them into one vector that points uphill.
2. `∇f = [2x, 2y]`. At `(3, 4)` it is `[6, 8]`, with magnitude `√(36 + 64) = 10`.
3. `∇f = [6xy, 3x² + 2]`. At `(1, 2)` it is `[12, 5]`.
4. `∇f = [2x + 3y, 3x + 2y]`. At `(2, 1)` it is `[7, 8]`.
5. `∇f = [yz, xz, xy]`. At `(1, 2, 3)` it is `[6, 3, 2]`, with magnitude `√49 = 7`.
6. The gradient points toward the **steepest increase**. Gradient descent moves in the **opposite** direction, `−∇f`.
7. Magnitude `√(16 + 9) = 5`. Steepest descent is `−[4, −3] / 5 = [−0.8, 0.6]`.
8. `∇f = [2, 4]`, so the new point is `(1 − 0.25·2, 2 − 0.25·4) = (0.5, 1.0)`. The loss falls from `1 + 4 = 5` to `0.25 + 1 = 1.25`.
9. `ŷ = [1, 2]`, errors `[−2, −3]`. `∂J/∂w = (2/2)(1·(−2) + 2·(−3)) = −8` and `∂J/∂b = (2/2)(−2 − 3) = −5`, so `∇J = [−8, −5]`. New values: `w = 1 − 0.1(−8) = 1.8` and `b = 0 − 0.1(−5) = 0.5`. The cost falls from `(4 + 9)/2 = 6.5` to `(0.49 + 0.81)/2 = 0.65` (new errors are `[−0.7, −0.9]`).
10. `6·0.8 + 8·(−0.6) = 4.8 − 4.8 = 0`. The function does not change in that direction: it is **along the contour line**, at a right angle to the gradient.
11. The factor is `1 − 2α = −1`, so the position bounces between `(3, 4)` and `(−3, −4)` forever and the loss stays at 25. The learning rate is too large.
12. 500 numbers: one partial derivative per parameter.
13. It means the function is flat in every direction. It could be a **minimum**, a **maximum** or a **saddle point**.
