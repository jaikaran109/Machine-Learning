# Linear Algebra for Machine Learning

Linear Algebra is one of the most important mathematical foundations of Machine Learning.

Think of it this way:

- Statistics tells us how to analyze data.
- Calculus tells us how models learn.
- Linear Algebra tells us how data is represented.

Almost every ML algorithm, neural network, image, dataset, embedding, and transformer is built on linear algebra.

---

# What is Linear Algebra?

Linear Algebra is the study of:

1. Vectors
2. Matrices
3. Transformations
4. Systems of Equations

In ML, almost everything is stored as vectors and matrices.

Example Dataset:

| Height | Weight | Age |
|----------|----------|-----|
| 170 | 65 | 21 |
| 180 | 75 | 25 |
| 160 | 55 | 20 |

ML sees it as:

\[
X =
\begin{bmatrix}
170 & 65 & 21 \\
180 & 75 & 25 \\
160 & 55 & 20
\end{bmatrix}
\]

This table is actually a matrix.

---

# 1. Scalars

A scalar is a single number.

Examples:

```text
5
10
-3
0.25
```

In ML:

- Learning Rate = 0.01
- Accuracy = 95%

These are scalars.

---

# 2. Vectors

A vector is a collection of numbers.

Example:

\[
[170, 65, 21]
\]

This could represent:

```text
Height = 170
Weight = 65
Age = 21
```

This entire row is one vector.

In ML:

Every data point is usually represented as a vector.

---

## Real Example

Suppose we have a house dataset:

```text
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

ML models take vectors as input.

---

# Why Vectors Matter

A neural network never sees:

```text
House:
Area = 1500
Bedrooms = 3
Bathrooms = 2
```

It sees:

\[
[1500,3,2]
\]

Everything becomes numbers.

---

# 3. Vector Operations

## Addition

\[
[1,2,3] + [4,5,6]
=
[5,7,9]
\]

Used in:

- Embeddings
- Feature Engineering

---

## Scalar Multiplication

\[
2 \times [1,2,3]
=
[2,4,6]
\]

Used for:

- Scaling Data
- Normalization

---

# 4. Dot Product

One of the most important concepts in ML.

Two vectors:

\[
[1,2,3]
\]

\[
[4,5,6]
\]

Dot Product:

\[
1 \times 4 + 2 \times 5 + 3 \times 6 = 32
\]

General Formula:

\[
a \cdot b = \sum_{i=1}^{n} a_i b_i
\]

---

## ML Intuition

Dot product measures similarity.

Example:

Netflix Recommendation System

User Likes:

```text
Action
Sci-Fi
Adventure
```

Movie Contains:

```text
Action
Sci-Fi
Adventure
```

Dot Product → High

Recommendation Score → High

---

# 5. Matrices

A matrix is a collection of vectors.

Example:

\[
\begin{bmatrix}
170 & 65 & 21 \\
180 & 75 & 25 \\
160 & 55 & 20
\end{bmatrix}
\]

Rows:
- Samples

Columns:
- Features

In ML:

Almost every dataset becomes a matrix.

---

# Shape of Matrix

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

- 2 Rows
- 3 Columns

---

# Why Shape Matters

Neural networks crash if dimensions don't match.

You'll constantly hear:

```text
Dimension Mismatch
Shape Mismatch
```

This is linear algebra.

---

# 6. Matrix Multiplication

Heart of Machine Learning.

Suppose:

\[
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

\[
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
\]

Matrix multiplication works by multiplying rows and columns.

---

## Why Matrix Multiplication Matters

Every neural network layer performs:

\[
Output = Input \times Weights
\]

This operation is matrix multiplication.

---

# Neural Network = Matrix Multiplication

Input:

\[
x
\]

Weights:

\[
W
\]

Output:

\[
y = xW
\]

A deep neural network is basically:

```text
Matrix Multiplication
+
Activation Function
Repeated Many Times
```

---

# 7. Transpose

Rows become columns.

Example:

\[
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
\]

becomes

\[
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
\]

Notation:

\[
A^T
\]

Used heavily in:

- Linear Regression
- PCA
- Deep Learning

---

# 8. Identity Matrix

Equivalent of number 1.

Example:

\[
I =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\]

Property:

\[
AI = A
\]

Used in:

- Matrix Inversion
- Optimization

---

# 9. Inverse Matrix

Equivalent of division.

For numbers:

```text
5 × (1/5) = 1
```

For matrices:

\[
AA^{-1} = I
\]

Used in:

- Linear Regression Closed Form Solution

---

# 10. Linear Transformations

A matrix can:

- Rotate Vectors
- Stretch Vectors
- Compress Vectors
- Reflect Vectors

ML often transforms data into better representations.

---

# 11. Eigenvalues & Eigenvectors

Most beginners fear this topic.

For ML, you only need intuition.

A transformation changes most vectors.

Some special vectors only get stretched.

Those are Eigenvectors.

Stretch factor = Eigenvalue.

---

## Example

Imagine rotating a sheet of paper.

Most arrows move.

Some special directions remain aligned.

Those are Eigenvectors.

---

# Why Eigenvalues Matter in ML

Used in:

## PCA (Principal Component Analysis)

Dimensionality Reduction

Example:

```text
100 Features
↓
10 Important Features
```

PCA finds important directions using eigenvectors.

---

# 12. Rank

Rank tells us how much information exists in a matrix.

Example:

If columns are duplicates:

```text
Height
2 × Height
```

Second column adds no new information.

Low Rank Matrix.

---

## ML Usage

Used in:

- Data Compression
- Recommendation Systems
- PCA

---

# 13. Distance

ML constantly measures distance.

Example:

\[
[1,2]
\]

and

\[
[4,6]
\]

Distance tells how different they are.

Used in:

- KNN
- Clustering
- Embeddings

---

# 14. Orthogonality

Orthogonal means perpendicular.

Dot Product:

\[
a \cdot b = 0
\]

Used in:

- PCA
- SVD
- Embeddings

---

# 15. Basis

A basis is a set of vectors that can represent all other vectors in a space.

Think:

```text
English:
26 Letters

All Words Are Formed From Them
```

Similarly:

Basis vectors create all vectors in a space.

---

# Where Each Topic Appears in ML

| Topic | Used In |
|---------|---------|
| Vectors | Features, Embeddings |
| Matrices | Datasets |
| Dot Product | Similarity, Neural Networks |
| Matrix Multiplication | Deep Learning |
| Transpose | Regression, PCA |
| Inverse | Linear Regression |
| Eigenvalues | PCA |
| Eigenvectors | PCA |
| Distance | KNN, Clustering |
| Orthogonality | PCA, SVD |
| Rank | Compression |
| Transformations | Neural Networks |

---

