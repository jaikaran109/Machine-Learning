> The slope of a curve at one exact point, and the tool a model uses to learn.

---

## 1. The Big Idea

A **derivative** tells you **how fast a function is changing at one exact point**. In picture form, it is the **slope of the curve at that point**.

**Analogy (the speedometer):** a car travels 100 km in 2 hours, so its *average* speed is 50 km/h. But the speedometer shows how fast it is going **right now**, which could be 30 or 80. The speedometer reads the derivative of distance.

| Idea | Meaning |
|---|---|
| **Average rate of change** | Change over a stretch (between two points) |
| **Instantaneous rate of change** | Change at one exact moment. This is the **derivative**. |

**Example:** the distance of a car is `s(t) = t²` metres after `t` seconds.

- Average speed from 1 s to 3 s: `(9 − 1) / (3 − 1) = 4 m/s`
- Speed at exactly 3 s: **6 m/s** (we will see why in a moment)

---

## 2. Key Terms in Plain Words

| Term | Meaning | Example |
|---|---|---|
| **Derivative** | The slope of a function at a point | The derivative of `x²` at 3 is 6 |
| **f′(x)** | Notation for the derivative of `f` (read "f prime of x") | `f′(x) = 2x` |
| **dy/dx** | Another notation: "the change in `y` for a small change in `x`" | `dy/dx = 2x` |
| **Secant line** | A line through **two** points on a curve | Gives the average slope |
| **Tangent line** | A line that touches the curve at **one** point with the same slope as the curve there | Its slope is the derivative |
| **Increasing / decreasing** | The function goes up / down as `x` grows | |
| **Stationary (critical) point** | A point where the slope is 0 | The bottom of a valley |
| **Minimum / maximum** | The lowest / highest point | |
| **Second derivative f″(x)** | The derivative of the derivative: how the slope itself is changing | |
| **Differentiable** | The derivative exists at that point | `x²` everywhere, but not `\|x\|` at 0 |
| **Differentiation** | The process of finding a derivative | |

---

## 3. From Two Points to One Point

Recall the Limits note. The slope between two points on a curve is:

```
slope = [ f(x + h) − f(x) ] / h
```

Here `h` is the gap between the two points. Now let the gap `h` **shrink toward 0**. The two points merge into one, and the secant line becomes the **tangent line**.

### Definition of the derivative

```
f′(x) = lim   [ f(x + h) − f(x) ] / h
        h→0
```

### Worked example: the derivative of f(x) = x²

```
[ f(x + h) − f(x) ] / h = [ (x + h)² − x² ] / h
                        = [ x² + 2xh + h² − x² ] / h
                        = ( 2xh + h² ) / h
                        = 2x + h

As h → 0:   f′(x) = 2x
```

So the slope of `x²` at any point `x` is `2x`.

| x | Slope `2x` | What the curve is doing |
|---|---|---|
| −2 | −4 | Falling |
| 0 | 0 | Flat (the bottom) |
| 1 | 2 | Rising gently |
| 3 | 6 | Rising steeply |

**The tangent line at `x = 3`:** it passes through `(3, 9)` with slope 6, so `y − 9 = 6(x − 3)`, which is `y = 6x − 9`.

---

## 4. What the Derivative Tells You

| Sign of f′(x) | Meaning | Gradient descent action |
|---|---|---|
| **Positive** | The function is **increasing** (uphill to the right) | Move **left** (decrease `x`) |
| **Negative** | The function is **decreasing** (downhill to the right) | Move **right** (increase `x`) |
| **Zero** | The curve is **flat** here | Possibly a minimum, so stop |

The **size** of the derivative tells you how **steep** the curve is.

> **Warning:** a zero slope does not always mean a minimum. For `f(x) = x³`, the slope `3x²` is 0 at `x = 0`, but the curve keeps rising through that point, so it is neither a
