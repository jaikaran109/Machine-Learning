# Matrix Multiplication for Machine Learning

Matrix multiplication is one of the most important operations in Linear Algebra and Machine Learning.

If you understand matrix multiplication well, you'll understand:

- Linear Regression
- Logistic Regression
- Neural Networks
- Deep Learning
- Transformers
- Embeddings
- Attention Mechanisms

Almost every modern ML model performs millions or billions of matrix multiplications.

---

# Why Do We Need Matrix Multiplication?

Suppose we have:

```text
House:
Area = 1500
Bedrooms = 3
Bathrooms = 2
```

Feature Vector:

\[
x =
\begin{bmatrix}
1500 \\
3 \\
2
\end{bmatrix}
\]

Suppose our model learns:

```text
Area Importance = 0.1
Bedroom Importance = 10
Bathroom Importance = 15
```

Weight Vector:

\[
w =
\begin{bmatrix}
0.1 \\
10 \\
15
\end{bmatrix}
\]

To make a prediction, we combine features and weights.

This is exactly what matrix multiplication does.

---

# What is Matrix Multiplication?

Matrix multiplication combines information from two matrices to produce a new matrix.

Unlike addition:

```text
Addition:
Same shape required
```

Multiplication follows different rules.

---

# Rule for Matrix Multiplication

Suppose:

\[
A = m \times n
\]

\[
B = n \times p
\]

Then:

\[
A \times B
\]

is possible.

Result:

\[
m \times p
\]

---

## The Golden Rule

For multiplication:

```text
Columns of First Matrix
=
Rows of Second Matrix
```

Must be equal.

---

# Example 1

\[
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

Shape:

```text
2 × 2
```

\[
B=
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
\]

Shape:

```text
2 × 2
```

Since:

```text
2 = 2
```

Multiplication is possible.

Result shape:

```text
2 × 2
```

---

# How Matrix Multiplication Works

Take:

\[
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

\[
B=
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
\]

The fundamental idea is:

```text
Row × Column
```

Every element in the result is produced by:

```text
One Row from A
×
One Column from B
```

---

# Step-by-Step Calculation

Result matrix:

\[
C=A\times B
\]

First element:

\[
C_{11}
\]

Take:

```text
Row 1 of A
```

\[
[1,2]
\]

and

```text
Column 1 of B
```

\[
\begin{bmatrix}
5\\
7
\end{bmatrix}
\]

Multiply:

\[
1\times5 + 2\times7
\]

\[
=19
\]

---

Second element:

\[
C_{12}
\]

Row 1:

\[
[1,2]
\]

Column 2:

\[
\begin{bmatrix}
6\\
8
\end{bmatrix}
\]

\[
1\times6 + 2\times8
\]

\[
=22
\]

---

Third element:

\[
C_{21}
\]

Row 2:

\[
[3,4]
\]

Column 1:

\[
\begin{bmatrix}
5\\
7
\end{bmatrix}
\]

\[
3\times5 + 4\times7
\]

\[
=43
\]

---

Fourth element:

\[
C_{22}
\]

\[
3\times6 + 4\times8
\]

\[
=50
\]

---

Final Result

\[
C=
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
\]

---

# Shortcut Interpretation

Every element is:

```text
Dot Product
```

between:

```text
Row of First Matrix
and
Column of Second Matrix
```

Matrix multiplication is basically a collection of dot products.

---

# Matrix × Vector Multiplication

This is the most common form in ML.

Suppose:

\[
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

Vector:

\[
x=
\begin{bmatrix}
5 \\
6
\end{bmatrix}
\]

Shapes:

```text
2 × 2

2 × 1
```

Multiplication possible because:

```text
2 = 2
```

---

# Calculation

First Row:

\[
1\times5 + 2\times6
\]

\[
=17
\]

Second Row:

\[
3\times5 + 4\times6
\]

\[
=39
\]

Result:

\[
\begin{bmatrix}
17 \\
39
\end{bmatrix}
\]

---

# ML Interpretation

Matrix:

\[
A
\]

represents learned weights.

Vector:

\[
x
\]

represents input features.

Output:

\[
Ax
\]

represents prediction or transformed features.

---

# Real ML Example

Suppose:

```text
Area = 1500
Bedrooms = 3
Bathrooms = 2
```

Feature Vector:

\[
x=
\begin{bmatrix}
1500 \\
3 \\
2
\end{bmatrix}
\]

Weights:

\[
w=
\begin{bmatrix}
0.1 \\
10 \\
15
\end{bmatrix}
\]

Prediction:

\[
w^T x
\]

Calculation:

\[
1500(0.1)+3(10)+2(15)
\]

\[
150+30+30
\]

\[
210
\]

This prediction comes from matrix/vector multiplication.

---

# Shape Trick

Always remember:

```text
(m × n)

×

(n × p)

=

(m × p)
```

Example:

```text
3 × 4

×

4 × 2

=

3 × 2
```

Possible.

---

Example:

```text
3 × 4

×

5 × 2
```

Not possible.

Because:

```text
4 ≠ 5
```

---

# Why Matrix Multiplication is Used in ML

Because ML models need to:

- Combine features
- Apply learned weights
- Transform data
- Generate predictions

Matrix multiplication does all of these efficiently.

---

# Linear Regression

Prediction:

\[
y=Xw
\]

Where:

\[
X
\]

Feature Matrix.

\[
w
\]

Weight Vector.

---

# Logistic Regression

Prediction:

\[
z=Xw+b
\]

Again:

```text
Matrix Multiplication
```

is the core operation.

---

# Neural Networks

For a layer:

\[
Z=XW+b
\]

Where:

```text
X = Inputs
W = Weights
b = Bias
```

Everything starts with matrix multiplication.

---

# Deep Learning

Every layer performs:

\[
XW
\]

followed by an activation function.

A 100-layer neural network simply performs matrix multiplication repeatedly.

---

# Transformers

Transformers use matrix multiplication to compute:

- Queries (Q)
- Keys (K)
- Values (V)
- Attention Scores

Example:

\[
QK^T
\]

This is matrix multiplication.

Without matrix multiplication, ChatGPT would not exist.

---

# Why GPUs Love Matrix Multiplication

GPUs are designed to perform:

```text
Thousands of matrix multiplications
simultaneously
```

This is why deep learning training is fast on GPUs.

---

# Common Mistakes

## Mistake 1

Thinking multiplication is element-wise.

Wrong:

\[
\begin{bmatrix}
1 & 2
\end{bmatrix}
\times
\begin{bmatrix}
3 & 4
\end{bmatrix}
=
\begin{bmatrix}
3 & 8
\end{bmatrix}
\]

This is element-wise multiplication, not matrix multiplication.

---

## Mistake 2

Ignoring dimensions.

Always check:

```text
Columns of First Matrix
=
Rows of Second Matrix
```

---

## Mistake 3

Memorizing formulas without understanding rows and columns.

Focus on:

```text
Row × Column
```

Everything becomes easier.

---

# Common Interview Questions

## What is matrix multiplication?

An operation where rows of the first matrix are multiplied with columns of the second matrix.

---

## When is matrix multiplication possible?

When:

```text
Columns of First Matrix
=
Rows of Second Matrix
```

---

## What is the shape of the result?

\[
(m\times n)
\times
(n\times p)
=
(m\times p)
\]

---

## Why is matrix multiplication important in ML?

Because almost every ML model computes predictions and transformations using matrix multiplication.

---

# Where Matrix Multiplication Appears in ML

| Topic | Usage |
|---------|---------|
| Linear Regression | Predictions |
| Logistic Regression | Predictions |
| Neural Networks | Forward Pass |
| Deep Learning | Layer Computations |
| CNNs | Feature Transformations |
| RNNs | Hidden State Updates |
| Transformers | Attention Mechanism |
| Embeddings | Feature Projection |
| PCA | Matrix Operations |
| Recommendation Systems | Similarity Calculations |

---

# What You Must Master

Before moving to transpose and inverse matrices, make sure you understand:

- Matrix Multiplication Rules
- Shape Compatibility
- Row × Column Concept
- Dot Product Relationship
- Matrix × Matrix Multiplication
- Matrix × Vector Multiplication
- Result Shape Calculation
- Why ML Models Depend on It

If you understand matrix multiplication deeply, you have already understood one of the most important mathematical operations in all of Machine Learning.
