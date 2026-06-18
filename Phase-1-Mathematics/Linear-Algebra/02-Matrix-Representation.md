# Matrices for Machine Learning

Matrices are one of the most important concepts in Linear Algebra and Machine Learning.

If vectors are the building blocks of data, then matrices are the containers that hold entire datasets.

Almost every Machine Learning algorithm works with matrices.

Examples:

- Datasets → Matrices
- Images → Matrices
- Neural Network Weights → Matrices
- Embeddings → Matrices
- Transformers → Matrices

Understanding matrices properly will make ML significantly easier.

---

# What is a Matrix?

A matrix is a rectangular arrangement of numbers organized into rows and columns.

Example:

\[
A=
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

This is a matrix.

Think of it as a table of numbers.

---

# Matrix Terminology

For:

\[
A=
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

Rows:

```text
[1 2 3]
[4 5 6]
```

Columns:

```text
[1]
[4]

[2]
[5]

[3]
[6]
```

---

# Why Matrices Matter in ML

Suppose we have a dataset:

| Height | Weight | Age |
|----------|----------|----------|
| 170 | 65 | 21 |
| 180 | 75 | 25 |
| 160 | 55 | 20 |

ML sees:

\[
X=
\begin{bmatrix}
170 & 65 & 21 \\
180 & 75 & 25 \\
160 & 55 & 20
\end{bmatrix}
\]

This matrix is called the Feature Matrix.

Rows represent data points.

Columns represent features.

---

# Matrix Dimensions

Dimensions describe the size of a matrix.

Notation:

```text
Rows × Columns
```

Example:

\[
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

Dimensions:

```text
2 × 3
```

Because:

- 2 Rows
- 3 Columns

---

# More Examples

## Example 1

\[
\begin{bmatrix}
1 & 2
\end{bmatrix}
\]

Dimension:

```text
1 × 2
```

---

## Example 2

\[
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
\]

Dimension:

```text
3 × 1
```

---

## Example 3

\[
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\]

Dimension:

```text
3 × 3
```

---

# Rows and Columns in ML

Consider:

| Area | Bedrooms | Bathrooms |
|--------|--------|--------|
| 1500 | 3 | 2 |
| 1800 | 4 | 3 |
| 1200 | 2 | 2 |

Matrix:

\[
X=
\begin{bmatrix}
1500 & 3 & 2 \\
1800 & 4 & 3 \\
1200 & 2 & 2
\end{bmatrix}
\]

---

## Rows = Samples

Each row represents one house.

Example:

\[
[1500,3,2]
\]

One house.

---

## Columns = Features

Column 1:

```text
Area
```

Column 2:

```text
Bedrooms
```

Column 3:

```text
Bathrooms
```

Each column represents one feature.

---

# Shape of a Matrix

Shape means dimensions.

Example:

\[
X=
\begin{bmatrix}
170 & 65 & 21 \\
180 & 75 & 25 \\
160 & 55 & 20
\end{bmatrix}
\]

Shape:

```text
(3,3)
```

Meaning:

```text
3 Rows
3 Columns
```

---

# Why Shape Matters

Neural networks require specific matrix dimensions.

Suppose:

Input Matrix:

```text
100 × 10
```

Weight Matrix:

```text
10 × 5
```

Multiplication works.

But:

```text
100 × 10

5 × 3
```

Will fail.

Dimension mismatch error.

---

# Types of Matrices

---

## Row Matrix

Contains one row.

\[
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
\]

Shape:

```text
1 × 3
```

---

## Column Matrix

Contains one column.

\[
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
\]

Shape:

```text
3 × 1
```

---

## Square Matrix

Rows = Columns

Example:

\[
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

Shape:

```text
2 × 2
```

---

## Rectangular Matrix

Rows ≠ Columns

Example:

\[
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

Shape:

```text
2 × 3
```

---

## Zero Matrix

All elements are zero.

\[
\begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}
\]

Used in initialization.

---

## Identity Matrix

Equivalent of number 1.

\[
I=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\]

Property:

\[
AI=A
\]

Used in:

- Matrix inversion
- Optimization
- Linear algebra operations

---

# Accessing Elements

For:

\[
A=
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\]

Element:

\[
A_{1,2}
\]

Means:

```text
Row 1
Column 2
```

Value:

```text
2
```

---

# Matrix as Dataset

Consider:

| Study Hours | Sleep Hours | Marks |
|------------|------------|------------|
| 4 | 8 | 70 |
| 6 | 7 | 80 |
| 8 | 6 | 90 |

Matrix:

\[
X=
\begin{bmatrix}
4 & 8 & 70 \\
6 & 7 & 80 \\
8 & 6 & 90
\end{bmatrix}
\]

---

## Interpretation

Rows:

Students

Columns:

Features

This is exactly how ML models receive data.

---

# Matrix Storage in NumPy

Python:

```python
import numpy as np

X = np.array([
    [170,65,21],
    [180,75,25],
    [160,55,20]
])
```

Shape:

```python
X.shape
```

Output:

```text
(3,3)
```

---

# Images as Matrices

Suppose:

```text
3 × 3 image
```

Pixel values:

\[
\begin{bmatrix}
255 & 120 & 90 \\
80 & 200 & 50 \\
60 & 40 & 255
\end{bmatrix}
\]

Image = Matrix

---

## Color Images

Actually stored as:

```text
Height × Width × Channels
```

Example:

```text
224 × 224 × 3
```

3 channels:

```text
Red
Green
Blue
```

---

# Neural Networks and Matrices

Input Data:

\[
X
\]

Weights:

\[
W
\]

Bias:

\[
b
\]

Prediction:

\[
XW+b
\]

Everything is matrix-based.

Deep Learning is largely repeated matrix operations.

---

# Common Matrix Mistakes

---

## Mistake 1

Confusing rows and columns.

Remember:

```text
Rows → Samples
Columns → Features
```

---

## Mistake 2

Ignoring dimensions.

Always check:

```python
X.shape
```

---

## Mistake 3

Not understanding shape compatibility.

Before multiplication verify:

```text
Columns of A = Rows of B
```

---

# Real ML Examples

## Linear Regression

Uses matrices for:

- Input features
- Parameters
- Predictions

---

## Logistic Regression

Uses matrices for:

- Feature vectors
- Weight vectors

---

## PCA

Uses matrices for:

- Covariance matrices
- Eigenvector calculations

---

## Neural Networks

Uses matrices for:

- Inputs
- Weights
- Activations

---

## Transformers

Uses matrices for:

- Queries
- Keys
- Values
- Attention Scores

---

# Common Interview Questions

## What is a matrix?

A rectangular arrangement of numbers organized into rows and columns.

---

## What are matrix dimensions?

The number of rows and columns.

Example:

```text
3 × 4
```

Means:

```text
3 rows
4 columns
```

---

## What do rows represent in ML?

Samples or observations.

---

## What do columns represent in ML?

Features or attributes.

---

## Why are matrices important?

Because datasets, images, weights, and neural network computations are represented using matrices.

---

# Where Matrices Appear in ML

| Topic | Usage |
|---------|---------|
| Dataset Storage | Feature Matrix |
| Images | Pixel Matrix |
| Neural Networks | Weight Matrices |
| Linear Regression | Design Matrix |
| PCA | Covariance Matrix |
| Embeddings | Embedding Matrix |
| Transformers | Attention Matrices |
| Deep Learning | Matrix Operations Everywhere |

---

# What You Must Master

Before moving to matrix operations, make sure you understand:

- What is a Matrix
- Rows and Columns
- Matrix Dimensions
- Matrix Shape
- Row Matrix
- Column Matrix
- Square Matrix
- Rectangular Matrix
- Identity Matrix
- Zero Matrix
- Matrix Representation of Datasets

These concepts form the foundation for matrix multiplication, transpose, inverse matrices, PCA, and deep learning.
