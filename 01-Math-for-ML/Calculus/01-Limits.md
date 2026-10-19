> The idea of "getting closer and closer", which makes slopes at a single point possible.

---

## 1. The Big Idea

A **limit** answers this question: **as the input gets closer and closer to some number, what value does the output get closer and closer to?**

The key point is that we care about where the output is **heading**, not necessarily where it **is** at that exact input.

**Analogy (walking toward a door):** you walk toward a door, getting closer with every step. At 1 m, 0.5 m, 0.1 m, 0.01 m, you can tell exactly where you are heading, even if you never touch the door. The limit is the **destination** you are heading to.

**Why we need it:** in the last note, we found the slope of `x²` at `x = 3` by using a second point closer and closer to 3. The slope got closer and closer to 6. A limit is the exact mathematical way to say "the value it gets closer to".

---

## 2. Key Terms in Plain Words

| Term | Meaning | Example |
|---|---|---|
| **Function** | A rule that turns an input into an output | `f(x) = x + 1` |
| **x → a** | "x gets closer and closer to `a`" (it may never equal `a`) | `x → 3` |
| **Limit** | The value `f(x)` gets close to as `x → a` | Written `lim (x→a) f(x) = L` |
| **Left-hand limit** | What `f(x)` heads toward when `x` approaches `a` from the **left** (smaller values) | `x → a⁻` |
| **Right-hand limit** | The same, from the **right** (larger values) | `x → a⁺` |
| **Limit exists** | Both sides head toward the **same number** | |
| **Undefined** | The function has no value at that input | `1/0` |
| **Continuous** | The graph has no gaps, jumps or holes | A pencil line drawn without lifting the pencil |
| **Infinity (∞)** | Not a number: it means "grows without end" | `x → ∞` |

**How to read the notation:**

```
lim   f(x) = L      means:  as x gets close to a, f(x) gets close to L
x→a
```

---

## 3. Building the Idea with an Example

Consider the function:

```
f(x) = (x² − 1) / (x − 1)
```

At `x = 1` it gives `0/0`, which has no meaning, so **`f(1)` is undefined**. Does that mean we know nothing about what happens near 1? No. Let's get close.

| x (from the left) | f(x) | | x (from the right) | f(x) |
|---|---|---|---|---|
| 0.9 | 1.9 | | 1.1 | 2.1 |
| 0.99 | 1.99 | | 1.01 | 2.01 |
| 0.999 | 1.999 | | 1.001 | 2.001 |

From **both sides**, the output heads toward **2**. So:

```
lim   (x² − 1) / (x − 1) = 2
x→1
```

**Why it works:** for any `x` other than 1, we can simplify.

```
(x² − 1) / (x − 1) = (x − 1)(x + 1) / (x − 1) = x + 1
```

The graph is the line `y = x + 1` with a **single hole** at `x = 1`. The hole has no value, but the line clearly heads to 2.

> **Main lesson:** a limit does not need the function to be defined at the point. It only needs the **surroundings** to head toward a value.

---

## 4. Left and Right Limits

A limit exists only if the **left-hand limit and right-hand limit are equal**.

**Example where it fails:** `f(x) = |x| / x` near `x = 0`.

| x | −0.1 | −0.01 | 0.01 | 0.1 |
|---|---|---|---|---|
| f(x) | −1 | −1 | 1 | 1 |

- Left-hand limit = **−1**
- Right-hand limit = **+1**

They disagree (the graph jumps), so **the limit does not exist** at 0.

### The three possible outcomes

| Outcome | Example | What it means |
|---|---|---|
| **A number** | `lim (x→1) (x + 1) = 2` | The output settles on a value |
| **Does not exist (jump)** | `lim (x→0) \|x\|/x` | Left and right disagree |
| **Infinite** | `lim (x→0) 1/x²` | The output grows without bound (we write `→ ∞`, and it is not a number) |

---

## 5. Limits at Infinity

We can also ask what happens as `x` becomes **very large** (`x → ∞`) or **very negative** (`x → −∞`).

```
lim   1/x = 0
x→∞
```

| x | 10 | 100 | 1,000 | 1,000,000 |
|---|---|---|---|---|
| 1/x | 0.1 | 0.01 | 0.001 | 0.000001 |

The output shrinks toward 0 but never reaches it, and that is fine for a limit.

**A useful pattern:**

```
lim (2x + 1) / x   =   lim (2 + 1/x)   =   2 + 0   =   2
x→∞                    x→∞
```

---

## 6. How to Calculate a Limit

### Method 1: Direct substitution

If the function is a normal, smooth formula, just **plug in the number**.

```
lim (3x + 1) = 3(2) + 1 = 7
x→2
```

### Method 2: Factor and cancel (when you get 0/0)

Substituting gives `0/0`, which is a **signal to simplify first**, not an answer.

```
lim (x² − 9)/(x − 3):   plugging in 3 gives 0/0

x² − 9 = (x − 3)(x + 3)
(x − 3)(x + 3)/(x − 3) = x + 3

lim (x + 3) = 3 + 3 = 6
x→3
```

### Method 3: Divide by the highest power (limits at infinity)

```
lim (3x² + 2x) / x²  =  lim (3 + 2/x)  =  3
x→∞
```

### The limit rules

If `lim f(x) = A` and `lim g(x) = B`, then:

| Rule | Formula |
|---|---|
| **Sum** | `lim (f + g) = A + B` |
| **Difference** | `lim (f − g) = A − B` |
| **Constant multiple** | `lim (c · f) = c · A` |
| **Product** | `lim (f · g) = A · B` |
| **Quotient** | `lim (f / g) = A / B`, as long as `B ≠ 0` |
| **Power** | `lim (f)ⁿ = Aⁿ` |

**Example:** `lim (x→2) (x² + 3x) = 2² + 3(2) = 4 + 6 = 10`.

---

## 7. Continuity

A function is **continuous at `a`** if you can draw it through `a` without lifting your pencil. Precisely, all three must hold:

1. `f(a)` is defined.
2. The limit as `x → a` exists.
3. The limit **equals** `f(a)`.

```
lim f(x) = f(a)
x→a
```

| Function | At | Continuous? | Why |
|---|---|---|---|
| `x²` | any point | Yes | A smooth curve |
| `(x² − 1)/(x − 1)` | `x = 1` | **No** | `f(1)` is undefined (a hole) |
| `\|x\|/x` | `x = 0` | **No** | A jump |
| `\|x\|` | `x = 0` | **Yes** | The two sides meet at 0 |

**Continuity and slopes:** a function must be continuous to have a slope at a point, but that is **not enough**. `|x|` is continuous at 0, yet it has a **sharp corner** there, so it has **no single slope** at 0. We will meet this again in the Derivatives note.

---

## 8. Why Limits Matter: The Derivative

The derivative is **defined using a limit**:

```
f'(x) = lim   [ f(x + h) − f(x) ] / h
        h→0
```

Here `h` is a tiny step, and the fraction is the slope between two very close points. The limit makes `h` shrink toward 0.

**Example: the slope of `f(x) = x²` at `x = 3`.**

```
[ f(3 + h) − f(3) ] / h = [ (3 + h)² − 9 ] / h
                        = [ 9 + 6h + h² − 9 ] / h
                        = (6h + h²) / h
                        = 6 + h

lim (6 + h) = 6
h→0
```

The slope at `x = 3` is exactly **6**, matching the table from the last note.

---

## 9. Limits in Machine Learning

| Place | Limit idea |
|---|---|
| **Derivatives and gradients** | Defined as limits, so every gradient descent step relies on them |
| **Sigmoid function** (logistic regression) | `σ(x) = 1/(1 + e⁻ˣ)`. As `x → ∞` it approaches **1**, and as `x → −∞` it approaches **0**, so its output stays between 0 and 1 and works as a probability. |
| **Convergence of training** | The loss approaches a limit (a minimum value) as training continues |
| **Probability** | A CDF approaches 0 at the far left and 1 at the far right |
| **Corners** | ReLU and MAE have sharp corners where the slope is not defined, so libraries use a convention for that single point |

---

## 10. In Code

### Approaching a limit with numbers

```python
def f(x):
    return (x**2 - 1) / (x - 1)

for h in [0.1, 0.01, 0.001, 0.0001]:
    print(f(1 - h), f(1 + h))
# values approach 2 from both sides (1.9, 1.99, ... and 2.1, 2.01, ...)
```

### Exact limits with SymPy

```python
import sympy as sp

x = sp.symbols("x")
print(sp.limit((x**2 - 1) / (x - 1), x, 1))     # 2
print(sp.limit(1 / x, x, sp.oo))                # 0
print(sp.limit(sp.Abs(x) / x, x, 0, "+"))       # 1  (right-hand limit)
print(sp.limit(sp.Abs(x) / x, x, 0, "-"))       # -1 (left-hand limit)
```

---

## 11. Common Mistakes

| Mistake | Fix |
|---|---|
| Thinking the limit must equal `f(a)` | The limit is about **nearby** values and the function may not even be defined at `a` |
| Treating `0/0` as the answer | It is a signal to **simplify** (factor and cancel) |
| Checking only one side | Check **both** sides. They must agree. |
| Treating ∞ as a number | It means "grows without end", so do not do ordinary arithmetic with it |
| Cancelling terms that are not factors | Only cancel **common factors**, as in `(x−1)(x+1)/(x−1)` |

---

## 12. Summary

- A **limit** is the value a function **approaches** as the input gets close to a point. It can exist even where the function itself is undefined.
- Notation: `lim (x→a) f(x) = L`.
- A limit exists only if the **left and right limits agree**.
- Outcomes: a **number**, **does not exist** (a jump), or **infinite** (grows without bound).
- To calculate: **substitute**; if `0/0`, **factor and cancel**; for `x → ∞`, divide by the highest power.
- **Continuous** means `lim f(x) = f(a)`: no gaps or jumps.
- The **derivative** is defined as a limit: `f'(x) = lim (h→0) [f(x+h) − f(x)] / h`.

---

## 13. Practice Questions

1. In your own words, what is a limit?
2. Can a limit exist at a point where the function is undefined? Explain using `(x² − 1)/(x − 1)` at `x = 1`.
3. Evaluate `lim (x→2) (3x + 1)`.
4. Evaluate `lim (x→3) (x² − 9)/(x − 3)`.
5. Evaluate `lim (x→0) (x² + 5x)/x`.
6. Evaluate `lim (x→2) (x² + 3x)` using the limit rules.
7. Evaluate `lim (x→∞) 1/x` and `lim (x→∞) (2x + 1)/x`.
8. For `|x|/x`, find the left and right limits at 0. Does the limit exist?
9. What does it mean for a function to be continuous at a point? Is `|x|` continuous at 0?
10. Use the limit definition to find the slope of `f(x) = x²` at `x = 2`.
11. What does the sigmoid function approach as `x → ∞` and as `x → −∞`? Why is this useful in classification?
12. What happens to `1/x²` as `x → 0`?

### Answers

1. The value a function gets closer and closer to as the input approaches a point.
2. Yes. At `x = 1` the function is undefined (0/0), but the values from both sides head toward 2, so the limit is 2.
3. `3(2) + 1 = 7`.
4. Substitution gives `0/0`. Factor `x² − 9 = (x − 3)(x + 3)` and cancel to get `x + 3`, so the limit is `6`.
5. Cancel `x` to get `x + 5`, so the limit is `5`.
6. `2² + 3(2) = 10`.
7. `1/x → 0`. And `(2x + 1)/x = 2 + 1/x → 2`.
8. Left limit `−1`, right limit `+1`. They differ, so the limit does **not** exist.
9. `lim f(x) = f(a)`: no gap or jump at that point. Yes, `|x|` is continuous at 0 (the limit 0 equals `f(0)`), even though it has a corner there.
10. `[ (2 + h)² − 4 ] / h = (4h + h²) / h = 4 + h`, and as `h → 0` this becomes **4**.
11. It approaches **1** as `x → ∞` and **0** as `x → −∞`. Its output always stays between 0 and 1, so it can be read as a probability.
12. It grows without bound, so we say it goes to **∞** (there is no finite limit).
