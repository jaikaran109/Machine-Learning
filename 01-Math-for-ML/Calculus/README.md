> The math of change, and the reason a model can learn.

---

## 1. The Big Idea

**Calculus is the math of change.** It answers questions such as:

- How fast is something changing right now?
- If I change this input a little, how much does the output change?
- At what input is the output smallest or largest?

**Analogy (a car):**

| Instrument | What it tells you | Calculus idea |
|---|---|---|
| **Speedometer** | How fast the distance is changing **right now** | **Derivative** (rate of change) |
| **Odometer** | The total distance added up over the trip | **Integral** (accumulation) |

Calculus has two halves:

| Half | Studies | Used in ML |
|---|---|---|
| **Differential calculus** | Rates of change and slopes (derivatives) | **A lot.** It is how models learn. |
| **Integral calculus** | Totals and areas under curves | Mostly in probability (area under a distribution curve) |

Our four topics (Limits, Derivatives, Partial Derivatives, Gradients) belong to **differential calculus**.

---

## 2. Why Machine Learning Needs Calculus

Recall from the Loss Functions and Gradient Descent note: a model learns by repeatedly **reducing its error (loss)**.

To reduce the loss, the model must know:

1. **Which direction** should I change each setting (parameter)?
2. **By how much** should I change it?

The answer to both comes from the **slope** of the loss. Calculus is the tool that finds slopes.

**The hiker analogy:** a hiker in fog wants the lowest point of a valley. The only information is the slope under their feet. If the ground slopes down to the right, step right. Calculus gives the model that sense of slope.

```
Loss measures the error
        ↓
Slope of the loss tells which way is downhill
        ↓
Step downhill (gradient descent)
        ↓
Repeat until the loss is small
```

---

## 3. Key Terms in Plain Words

| Term | Meaning | Example |
|---|---|---|
| **Function** | A rule that turns an input into an output | `f(x) = x²` turns 3 into 9 |
| **Variable** | A quantity that can change | `x` |
| **Slope** | How steep a line is: rise divided by run | A road that climbs 2 m for every 10 m forward |
| **Rate of change** | How fast the output changes when the input changes | Speed is the rate of change of distance |
| **Curve** | A graph that bends, so its slope keeps changing | The graph of `x²` |
| **Minimum / maximum** | The lowest / highest point of a function | The bottom of a valley |
| **Optimization** | Finding the input that gives the best (smallest or largest) output | Training a model |

### Slope of a straight line (recap)

```
slope = rise / run = (y₂ − y₁) / (x₂ − x₁)
```

**Example:** the line through `(1, 3)` and `(3, 7)` has slope `(7 − 3) / (3 − 1) = 2`.

For a straight line, the slope is the **same everywhere**. For a **curve**, the slope **keeps changing**, and that is exactly the case calculus handles.

---

## 4. The Four Topics at a Glance

| Topic | The question it answers | Plain meaning | ML use |
|---|---|---|---|
| **Limits** | What value does a function get closer and closer to? | The idea of "getting infinitely close" | The foundation that makes derivatives possible |
| **Derivatives** | How steep is the curve at **one exact point**? | The slope at a single point | Slope of the loss for one parameter |
| **Partial Derivatives** | If the function has **many inputs**, how does it change when I move **only one** of them? | A slope in one direction, others held still | The slope for each parameter separately |
| **Gradients** | What are **all** the partial slopes together? | A vector of partial derivatives that points uphill | Gradient descent walks in the opposite direction |

### How they connect

```
Limits
  ↓  (give a precise meaning to "slope at one point")
Derivatives
  ↓  (extend to functions with many inputs)
Partial Derivatives
  ↓  (collect them all into one vector)
Gradients
  ↓  (step in the opposite direction)
Gradient Descent  →  a trained model
```

Each topic builds on the one before, so we learn them in this order.

---

## 5. A Preview: From Slope Between Two Points to Slope at One Point

For a curve, we can measure the slope **between two points**. Take `f(x) = x²` and start at `x = 3`, where `f(3) = 9`.

| Second point | `f` at that point | Slope between the points |
|---|---|---|
| `x = 4` | 16 | `(16 − 9) / (4 − 3) = 7` |
| `x = 3.1` | 9.61 | `(9.61 − 9) / 0.1 = 6.1` |
| `x = 3.01` | 9.0601 | `(9.0601 − 9) / 0.01 = 6.01` |

As the second point moves **closer and closer** to `x = 3`, the slope gets closer and closer to **6**. That value is the slope **at** `x = 3`, and it is called the **derivative** of `x²` at 3. The idea of "getting closer and closer" is exactly what a **limit** describes.

**The result to remember:** for `f(x) = x²`, the slope at any point is `2x`.

| `x` | Slope `2x` | Meaning |
|---|---|---|
| 0 | 0 | Flat: the **bottom** of the curve |
| 1 | 2 | Rising gently |
| 3 | 6 | Rising steeply |
| −2 | −4 | Falling (going downhill as `x` increases) |

**A key observation:** where the slope is **0**, the curve is flat. For a valley shape, that is the **lowest point**. This is why finding where the slope is zero helps us **minimize the loss**.

---

## 6. Where Calculus Appears in Machine Learning

| Place in ML | Calculus idea |
|---|---|
| **Gradient descent** | Gradients show the downhill direction |
| **Training linear and logistic regression** | Derivatives of the loss for `w` and `b` |
| **Backpropagation (deep learning)** | Chain rule applied through many layers |
| **Finding the best model settings** | Slope equal to zero at the minimum |
| **Probability** | Areas under curves (integrals) for PDF and CDF |

---

## 7. How Much Calculus Do You Really Need?

You do **not** need to be a calculus expert. For ML you need to:

1. **Understand the ideas:** slope, rate of change, and why a zero slope means a flat spot.
2. **Know a few rules:** the power rule and the chain rule (in the Derivatives note).
3. **Read gradient formulas**, such as the ones for linear regression.

Libraries such as scikit-learn, PyTorch and TensorFlow **calculate derivatives and gradients automatically**, but understanding them tells you *what the computer is doing* and *why training works*.

---

## 8. Common Worries

| Worry | Reality |
|---|---|
| "Calculus is only for advanced math people." | The ML version is mostly one idea: the slope. |
| "I must solve long derivative problems by hand." | You only need the basic rules and the intuition. |
| "The slope of a curve doesn't make sense." | It is the slope of a tiny straight piece of the curve at one point. |

---

## 9. Summary

- **Calculus is the math of change.** ML uses mainly **differential calculus** (slopes).
- A model learns by reducing its loss, and calculus tells it **which direction** to move and **how much**.
- A straight line has one slope. A **curve's slope changes**, and the **derivative** gives the slope at one exact point.
- **Limits** give the precise meaning of "slope at a point". **Partial derivatives** handle many inputs. The **gradient** collects them into one vector.
- Where the slope is **zero**, the curve is flat, which is where minimums (and maximums) occur.
- For `f(x) = x²`, the slope at any point is `2x`.
- Order of study: **Limits, Derivatives, Partial Derivatives, Gradients**.

---

## 10. Practice Questions

1. In one line, what is calculus?
2. Which half of calculus does ML mainly use?
3. In the car analogy, which instrument matches the derivative?
4. Why does a model need to know the slope of its loss?
5. Find the slope of the line through `(1, 3)` and `(3, 7)`.
6. What is the slope of the line `y = 5x − 2`?
7. Why is the slope of a straight line easy, but the slope of a curve harder?
8. For `f(x) = x²`, the slope at `x = 0` is `0`. What does a zero slope tell you about that point?
9. Calculate the slope of `f(x) = x²` between `x = 2` and `x = 3`, then between `x = 2` and `x = 2.1`. What value is it getting close to?
10. Match each topic to its meaning:
    - Limits, Derivatives, Partial Derivatives, Gradients
    - (a) The slope at one point  (b) A vector of all partial slopes  (c) The idea of getting infinitely close  (d) The slope with respect to one input among many
11. Which of the four topics does gradient descent directly use to choose its direction?

### Answers

1. The math of change: how fast things change, and where they are smallest or largest.
2. Differential calculus (derivatives and slopes).
3. The speedometer (how fast distance is changing right now).
4. The slope shows which direction reduces the loss, and how steeply, so the model knows how to adjust its parameters.
5. `(7 − 3) / (3 − 1) = 2`.
6. `5`.
7. A line has the same slope everywhere. A curve's slope changes from point to point, so we need the slope at one exact point.
8. The curve is flat there, so it could be a minimum or maximum (here it is the bottom of the curve).
9. Between 2 and 3: `(9 − 4) / 1 = 5`. Between 2 and 2.1: `(4.41 − 4) / 0.1 = 4.1`. It is getting close to **4**, which equals `2x` at `x = 2`.
10. Limits = (c), Derivatives = (a), Partial Derivatives = (d), Gradients = (b).
11. The **gradient**. It points uphill, so gradient descent steps in the opposite direction.
