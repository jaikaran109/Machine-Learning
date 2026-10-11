# Tensors

> **Phase 1: Mathematics for Machine Learning, Linear Algebra**
> The data container that every machine learning and deep learning library is built on.

---

## 1. The Big Idea

Machine learning works with numbers arranged in different shapes. A single number, a list of numbers, a table and a stack of images are all different shapes of the same thing. A **tensor** is the general name for this: **a container of numbers arranged along any number of dimensions.**

**Analogy (storage):**

| Container | Tensor |
|---|---|
| A single item | Scalar |
| A row of boxes | Vector |
| A sheet of boxes (rows and columns) | Matrix |
| A stack of sheets | 3D tensor |
| A shelf of stacks | 4D tensor, and so on |

Tensors matter because every dataset, weight and prediction in ML is stored as one, and every operation (addition, multiplication, reshaping) works on them in a uniform way.

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Tensor** | An n-dimensional array of numbers. | A container for numbers of any dimension. |
| **Scalar** | A single number (0 dimensions). | One value. |
| **Vector** | A 1D list of numbers. | One row or column. |
| **Matrix** | A 2D grid of numbers. | A table. |
| **Rank (ndim)** | The number of dimensions (axes) of a tensor. | How many directions it extends in. |
| **Axis** | One dimension of a tensor, counted from 0. | A direction you can move along. |
| **Shape** | The size along each axis, such as `(3, 4)`. | The tensor's dimensions. |
| **Size** | The total number of elements (the product of the shape). | How many numbers it holds. |
| **dtype** | The data type of the elements (`float32`, `int64`). | What kind of numbers it stores. |

> **Note:** "rank" here means the number of dimensions. In linear algebra, the "rank of a matrix" means something different (the number of independent rows or columns). In ML code, `ndim` avoids the confusion.

---

## 3. From Scalar to Tensor

| Name | Rank | Example | Shape |
|---|---|---|---|
| **Scalar** | 0 | `5` | `()` |
| **Vector** | 1 | `[2, 4, 6]` | `(3,)` |
| **Matrix** | 2 | `[[1, 2, 3], [4, 5, 6]]` | `(2, 3)` |
| **3D tensor** | 3 | Two matrices stacked | `(2, 2, 3)` |
| **nD tensor** | n | A stack of stacks | `(...)` |

Vectors, matrices and 3D (or higher) tensors are all tensors. The names scalar, vector and matrix are just the special cases of rank 0, 1 and 2.

---

## 4. Tensors in Machine Learning

The shape of the tensor tells you what kind of data it holds.

| Data | Tensor shape | Meaning of each axis |
|---|---|---|
| **One example** | `(features,)` | A single row of features |
| **Tabular dataset** | `(samples, features)` | 1000 customers with 5 features is `(1000, 5)` |
| **Time series or text** | `(samples, timesteps, features)` | 100 customers, 30 days, 4 measurements is `(100, 30, 4)` |
| **Grayscale image** | `(height, width)` | A 28 by 28 image is `(28, 28)` |
| **Color image** | `(height, width, channels)` | An RGB image is `(224, 224, 3)` |
| **Batch of color images** | `(batch, height, width, channels)` | 32 images is `(32, 224, 224, 3)` |
| **Batch of videos** | `(batch, frames, height, width, channels)` | A 5D tensor |

> The order of axes depends on the library. TensorFlow usually puts channels last, `(batch, H, W, C)`, while PyTorch puts them first, `(batch, C, H, W)`.

### Counting elements

Size is the product of the shape.

```
Batch of 32 RGB images, 224 × 224:
Size = 32 × 224 × 224 × 3 = 4,816,896 numbers

At 4 bytes each (float32): 4,816,896 × 4 ≈ 19.3 MB
```

---

## 5. Essential Tensor Operations

### Element-wise operations

Applied to each position separately, between tensors of the same shape.

```
[1, 2, 3] + [10, 20, 30] = [11, 22, 33]
[1, 2, 3] × [10, 20, 30] = [10, 40, 90]
```

### Reshaping

Changing the shape without changing the data. The total number of elements must stay the same.

```
12 elements can be:   (12,)   (3, 4)   (2, 6)   (2, 2, 3)
```

Flattening turns any tensor into a 1D vector, which is what a fully connected layer expects after convolutions.

### Transpose

Swaps axes. A `(2, 3)` matrix becomes `(3, 2)`.

### Aggregation along an axis

```
A = [[1, 2, 3],
     [4, 5, 6]]

sum(axis=0) = [5, 7, 9]      (collapses the rows, one result per column)
sum(axis=1) = [6, 15]        (collapses the columns, one result per row)
```

### Matrix multiplication and the dot product

For matrices, the inner sizes must match and the outer sizes become the result:

```
(m, n) @ (n, p) = (m, p)
```

This is the heart of a neural network layer:

```
Input X:      (batch, features)   = (32, 10)
Weights W:    (features, units)   = (10, 4)
Output X @ W: (batch, units)      = (32, 4)
```

For vectors, the **dot product** gives a scalar and powers the linear model `ŷ = w·x + b`.

### Broadcasting

Lets tensors of different shapes work together without copying data. Compare the shapes **from the right**. Two dimensions are compatible if they are **equal** or one of them is **1** (or missing).

| Shapes | Compatible? | Result |
|---|---|---|
| `(3, 4)` and `(4,)` | Yes | `(3, 4)` |
| `(3, 4)` and `(3, 1)` | Yes | `(3, 4)` |
| `(3, 4)` and `(3,)` | **No** (4 vs 3) | Error |
| `(2, 3, 4)` and `(3, 1)` | Yes | `(2, 3, 4)` |

Typical use: adding a bias vector `(units,)` to every row of an output `(batch, units)`.

---

## 6. In Code

### NumPy

```python
import numpy as np

scalar = np.array(5)
vector = np.array([2, 4, 6])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
tensor3d = np.zeros((2, 2, 3))

print(scalar.ndim, vector.ndim, matrix.ndim, tensor3d.ndim)   # 0 1 2 3
print(matrix.shape, matrix.size, matrix.dtype)                # (2, 3) 6 int64

print(matrix.reshape(3, 2))       # reshape to (3, 2)
print(matrix.T)                   # transpose, shape (3, 2)
print(matrix.sum(axis=0))         # [5 7 9]
print(matrix.sum(axis=1))         # [ 6 15]

X = np.random.rand(32, 10)
W = np.random.rand(10, 4)
print((X @ W).shape)              # (32, 4)
```

### PyTorch and TensorFlow

Deep learning libraries use tensors that behave like NumPy arrays but add GPU support and automatic gradients.

```python
import torch
t = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)

import tensorflow as tf
c = tf.constant([[1.0, 2.0], [3.0, 4.0]])
```

`requires_grad=True` tells PyTorch to track operations, so it can compute the gradients needed for backpropagation automatically (Phase 5).

---

## 7. Why Tensors Matter

| Reason | Explanation |
|---|---|
| **One structure for all data** | Tables, images, text and audio all become tensors |
| **Speed** | Operations on whole tensors run in parallel on CPU and GPU, far faster than Python loops (vectorization) |
| **Automatic gradients** | Frameworks track tensor operations to compute gradients for learning |
| **Batching** | A batch is just one extra axis, so many examples are processed at once |

---

## 8. Common Mistakes

| Mistake | Fix |
|---|---|
| Mixing up shape and rank | Rank is the number of axes. Shape lists the size of each. |
| Shape mismatch in matrix multiplication | Check that the inner sizes match: `(m, n) @ (n, p)` |
| Wrong axis in `sum` or `mean` | Remember axis 0 collapses rows, and axis 1 collapses columns |
| Forgetting the batch axis | A single image is `(H, W, C)`, but models expect `(1, H, W, C)` |
| Confusing `(n,)` with `(n, 1)` | A 1D vector and a column matrix are different shapes and broadcast differently |
| Mixing dtypes | Convert integers to `float32` before feeding a neural network |

---

## 9. Summary

- A **tensor** is an n-dimensional array of numbers. Scalars, vectors and matrices are tensors of rank 0, 1 and 2.
- **Rank** is the number of axes, **shape** is the size along each axis, and **size** is the total number of elements.
- ML data is stored as tensors, such as `(samples, features)` for tables and `(batch, H, W, C)` for images.
- Key operations are element-wise math, reshape, transpose, aggregation along an axis, matrix multiplication and broadcasting.
- Matrix multiplication follows `(m, n) @ (n, p) = (m, p)`.
- Tensors give speed through vectorization, GPU support and automatic gradients.

---

## 10. Practice Questions

1. In your own words, what is a tensor? Give the rank of a scalar, a vector and a matrix.
2. What is the difference between the rank and the shape of a tensor?
3. A tensor has shape `(32, 28, 28, 1)`. What does each axis likely represent, and how many elements does it hold?
4. A dataset has 500 patients, 12 months and 6 measurements per month. What shape would the tensor have, and how many elements?
5. What is the shape of `(64, 10) @ (10, 5)`? Is `(64, 10) @ (5, 10)` valid?
6. Which of these broadcasts successfully? Give the result shape where valid.
   - a) `(3, 4)` and `(4,)`
   - b) `(3, 4)` and `(3,)`
   - c) `(2, 3, 4)` and `(3, 1)`
7. A tensor has 24 elements. If you reshape it to `(4, ?, 2)`, what is the missing value?
8. For `A = [[1, 2], [3, 4]]`, calculate `A.sum(axis=0)` and `A.sum(axis=1)`.
9. Why is operating on whole tensors faster than looping over numbers in Python?
10. Why does PyTorch need `requires_grad=True`, and which topic from Phase 1 does it relate to?

### Answers

- **Q1:** A tensor is an n-dimensional array of numbers. Scalar rank 0, vector rank 1, matrix rank 2.
- **Q2:** Rank counts the axes (for example 4). Shape lists each axis's size (for example `(32, 28, 28, 1)`).
- **Q3:** Batch of 32, height 28, width 28, 1 channel (a batch of grayscale images). Elements = `32 × 28 × 28 × 1 = 25,088`.
- **Q4:** Shape `(500, 12, 6)`, with `500 × 12 × 6 = 36,000` elements.
- **Q5:** `(64, 5)`. The second one is **not valid**, since the inner sizes are 10 and 5.
- **Q6:** a) valid, `(3, 4)`. b) not valid (4 vs 3). c) valid, `(2, 3, 4)`.
- **Q7:** `24 / (4 × 2) = 3`.
- **Q8:** `axis=0` gives `[4, 6]`, and `axis=1` gives `[3, 7]`.
- **Q9:** Tensor operations run in optimized compiled code and in parallel (vectorization), while Python loops handle one number at a time.
- **Q10:** It tells PyTorch to record operations so it can compute **gradients** automatically. This links to the gradients in the Calculus section (partial derivatives and gradient descent).
