# Vectors for Machine Learning

Vectors are one of the most fundamental concepts in Linear Algebra and Machine Learning.

Before understanding matrices, neural networks, embeddings, or transformers, you must understand vectors.

---

# What is a Vector?

A vector is an ordered collection of numbers.

Example:

\[
[2, 4]
\]

\[
[1, 3, 5]
\]

\[
[170, 65, 21]
\]

Unlike a scalar (single number), a vector contains multiple values.

---

## Real-Life ML Example

Suppose we have a student's data:

```text
Height = 170 cm
Weight = 65 kg
Age = 21 years
```

This can be represented as:

\[
x = [170, 65, 21]
\]

This is called a feature vector.

In Machine Learning, every data point is usually converted into a vector.

---

# Why Vectors Matter in ML

Machines cannot understand:

```text
Jai
Age = 21
Weight = 65
Height = 170
```

But they can understand:

\[
[170,65,21]
\]

Everything in ML eventually becomes vectors.

Examples:

- House Data → Vector
- Customer Data → Vector
- Images → Vector
- Text → Vector
- Audio → Vector

---

# Scalars vs Vectors

## Scalar

A single number.

Examples:

\[
5
\]

\[
10
\]

\[
0.01
\]

Machine Learning Examples:

- Learning Rate
- Accuracy
- Loss Value

---

## Vector

Collection of numbers.

Example:

\[
[1,2,3]
\]

Contains multiple values.

---

# Vector Dimensions

The number of elements inside a vector is called its dimension.

Examples:

### 2D Vector

\[
[3,4]
\]

Dimension = 2

---

### 3D Vector

\[
[2,4,6]
\]

Dimension = 3

---

### 100D Vector

\[
[x_1,x_2,x_3,\ldots,x_{100}]
\]

Dimension = 100

---

## ML Example

House Dataset:

```text
Area
Bedrooms
Bathrooms
Parking
Age
```

Vector:

\[
[1500,3,2,1,5]
\]

Dimension = 5

Because there are 5 features.

---

# Geometric Interpretation

A vector can represent:

- Position
- Direction
- Movement

Example:

\[
[3,4]
\]

Means:

```text
Move 3 units on x-axis
Move 4 units on y-axis
```

Visualize:

```text
      *
     /
    /
   /
  /
 /
*---------
```

The arrow from origin to point is the vector.

---

# Magnitude of a Vector

Magnitude means length of a vector.

Also called:

- Norm
- Length

For vector:

\[
[3,4]
\]

Magnitude:

\[
\sqrt{3^2+4^2}
\]

\[
= \sqrt{25}
\]

\[
= 5
\]

---

## Formula

For vector:

\[
[x_1,x_2,\ldots,x_n]
\]

Magnitude:

\[
||x||=
\sqrt{x_1^2+x_2^2+\cdots+x_n^2}
\]

---

# Why Magnitude Matters in ML

Magnitude tells us:

- How large a vector is
- Importance of a feature vector
- Distance calculations

Used in:

- KNN
- Clustering
- Embeddings
- Recommendation Systems

---

# Direction of a Vector

Magnitude tells:

```text
How far?
```

Direction tells:

```text
Which way?
```

Example:

\[
[3,4]
\]

and

\[
[6,8]
\]

Different magnitudes.

Same direction.

---

## ML Intuition

Two customers may spend:

```text
Customer A = [10,20]
Customer B = [20,40]
```

Customer B spends more.

But behavior pattern is same.

Direction captures this similarity.

---

# Unit Vector

A vector whose magnitude is 1.

Example:

\[
[0.6,0.8]
\]

Magnitude:

\[
1
\]

---

## Why Unit Vectors Matter

They preserve direction.

Remove scale differences.

Used heavily in:

- Similarity Search
- Embeddings
- NLP Models
- Recommendation Systems

---

# Vector Addition

Add corresponding elements.

Example:

\[
[1,2]
+
[3,4]
=
[4,6]
\]

---

## Interpretation

Suppose:

```text
Day 1 Sales = [100,200]
Day 2 Sales = [50,75]
```

Total:

\[
[150,275]
\]

---

## ML Usage

Used in:

- Embedding Updates
- Gradient Updates
- Feature Engineering

---

# Vector Subtraction

Subtract corresponding elements.

Example:

\[
[5,7]
-
[2,3]
=
[3,4]
\]

---

## ML Usage

Used in:

- Error Calculation
- Distance Calculation
- Optimization

---

# Scalar Multiplication

Multiply every element by a scalar.

Example:

\[
3 \times [1,2]
=
[3,6]
\]

---

## Why It Matters

Used in:

- Learning Rate Updates
- Gradient Descent
- Feature Scaling

Example:

\[
0.01 \times Gradient
\]

Very common in ML.

---

# Dot Product

One of the most important vector operations.

Given:

\[
[1,2,3]
\]

and

\[
[4,5,6]
\]

Dot Product:

\[
1\times4+2\times5+3\times6
\]

\[
=32
\]

---

## Formula

\[
a \cdot b
=
\sum_{i=1}^{n} a_i b_i
\]

---

# Why Dot Product Matters

The dot product measures similarity.

Large Dot Product:

```text
More Similar
```

Small Dot Product:

```text
Less Similar
```

---

# Real ML Example

Netflix Recommendation

User Preferences:

\[
[5,4,5]
\]

Movie Features:

\[
[5,4,5]
\]

Dot Product:

High

Recommendation:

Strong

---

# Cosine Similarity

One of the most common similarity metrics in ML.

Formula:

\[
\cos(\theta)
=
\frac{a\cdot b}
{||a||\,||b||}
\]

---

## Interpretation

### Similar Direction

\[
\cos(\theta) \approx 1
\]

Very Similar

---

### Perpendicular

\[
\cos(\theta)=0
\]

Unrelated

---

### Opposite Direction

\[
\cos(\theta)\approx -1
\]

Very Different

---

## Used In

- Search Engines
- NLP
- Recommendation Systems
- Embeddings
- LLMs

---

# Distance Between Vectors

Suppose:

\[
A=[1,2]
\]

\[
B=[4,6]
\]

Distance:

\[
\sqrt{(4-1)^2+(6-2)^2}
\]

\[
=5
\]

---

## Why Distance Matters

Used in:

- KNN
- Clustering
- Anomaly Detection

Smaller Distance:

```text
More Similar
```

Larger Distance:

```text
Less Similar
```

---

# Orthogonal Vectors

Orthogonal means perpendicular.

Condition:

\[
a \cdot b = 0
\]

Example:

\[
[1,0]
\]

\[
[0,1]
\]

Dot Product:

\[
0
\]

Therefore orthogonal.

---

## Why Orthogonality Matters

Used in:

- PCA
- SVD
- Deep Learning
- Embeddings

Orthogonal vectors carry independent information.

---

# Feature Vectors

In ML, vectors often represent features.

Example:

```text
House:
Area = 1500
Bedrooms = 3
Bathrooms = 2
Age = 5
```

Vector:

\[
[1500,3,2,5]
\]

This is called a feature vector.

---

# Word Embeddings

Words can also become vectors.

Example:

```text
King
```

\[
[0.1,0.9,0.4,\ldots]
\]

```text
Queen
```

\[
[0.2,0.8,0.5,\ldots]
\]

Modern NLP models represent words as vectors.

---

# Images as Vectors

Image:

```text
28 × 28
```

Contains:

\[
784
\]

pixels.

Can be flattened into:

\[
[x_1,x_2,\ldots,x_{784}]
\]

A vector.

---

# Neural Networks and Vectors

Input Layer:

\[
x
\]

Weight Vector:

\[
w
\]

Prediction:

\[
x \cdot w
\]

This is a dot product.

Neural networks perform millions of vector operations every second.

---

# Common Interview Questions

## What is a vector?

An ordered collection of numbers representing data, direction, or features.

---

## What is magnitude?

The length of a vector.

---

## What is direction?

The orientation of a vector in space.

---

## What is a unit vector?

A vector with magnitude 1.

---

## What is a dot product?

An operation that measures similarity between vectors.

---

## Why are vectors important in ML?

Because every piece of data is ultimately represented as vectors.

---

# Where Vectors Appear in ML

| Topic | Usage |
|---------|---------|
| Feature Vectors | Dataset Representation |
| Dot Product | Neural Networks |
| Cosine Similarity | NLP |
| Distance Metrics | KNN |
| Embeddings | LLMs |
| Recommendation Systems | Similarity Search |
| Clustering | Grouping Data |
| PCA | Dimensionality Reduction |
| Gradient Descent | Optimization |
| Deep Learning | Every Layer |

---

# What You Must Master

Before moving to matrices, make sure you understand:

- What is a Vector
- Dimensions
- Magnitude
- Direction
- Unit Vectors
- Vector Addition
- Vector Subtraction
- Scalar Multiplication
- Dot Product
- Distance
- Cosine Similarity
- Orthogonality

These concepts alone will explain a huge portion of how data is represented and compared inside Machine Learning systems.
