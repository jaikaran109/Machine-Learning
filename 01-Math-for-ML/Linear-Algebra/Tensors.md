# Tensors (Beginner Guide)

> **Phase 1: Mathematics for Machine Learning, Linear Algebra**
> How computers store and organize numbers, starting from the very basics.

---

## 1. What Problem Are We Solving?

Machine learning works with numbers: marks, prices, ages, the brightness of the dots in a photo. A computer needs an organized way to store these numbers so it can do math on them quickly.

A **tensor** is that organized way. It is a **container that holds numbers arranged in a neat pattern**.

To understand it, we build up in four small steps.

---

## 2. Building Up Step by Step

### Step 1: One number (scalar)

A single number, such as the temperature today.

```
30
```

A single number is called a **scalar**. To find it, you need **0 directions** (there is nothing to search; it is just one number).

### Step 2: A list of numbers (vector)

A row of numbers in a fixed order, such as one student's marks in 3 subjects.

```
[80, 90, 70]
```

This is called a **vector**. To find one number, you need **1 position**: "the 2nd mark" gives 90.

### Step 3: A table of numbers (matrix)

Rows and columns, like a spreadsheet. Here are the marks of 3 students in 3 subjects.

| | Maths | Science | English |
|---|---|---|---|
| **Aman** | 80 | 90 | 70 |
| **Riya** | 60 | 75 | 85 |
| **Sam** | 90 | 85 | 95 |

Written in Python style:

```
[[80, 90, 70],
 [60, 75, 85],
 [90, 85, 95]]
```

This is called a **matrix**. To find one number, you need **2 positions**: a row and a column. "Riya, Science" gives 75.

### Step 4: A stack of tables (3D tensor)

Now suppose you have these marks for **2 semesters**. That is two tables stacked on top of each other, like two pages in a notebook.

```
Semester 1 table
Semester 2 table
```

To find one number, you now need **3 positions**: semester, student, subject. "Semester 2, Riya, Science" gives one number.

### Going further

You can keep stacking: a shelf of notebooks needs 4 positions, and so on.

### The big idea

| Name | Positions needed to find one number | Example |
|---|---|---|
| **Scalar** | 0 | `30` |
| **Vector** | 1 | `[80, 90, 70]` |
| **Matrix** | 2 | A table of marks |
| **3D tensor** | 3 | Two tables stacked |
| **4D tensor and beyond** | 4 or more | Stacks of stacks |

> **Definition:** a **tensor** is the general name for all of these. A scalar, a vector and a matrix are just tensors with 0, 1 and 2 dimensions.

---

## 3. Key Terms in Plain Words

We use this small table to explain each term.

```
[[1, 2, 3],
 [4, 5, 6]]
```

| Term | Meaning | In our example |
|---|---|---|
| **Element** | One number inside the tensor | `1`, `2`, `3`, `4`, `5`, `6` are the elements |
| **Dimension** | How many positions you need to locate an element. It is also called the number of **axes**. | This table has **2** dimensions (row and column) |
| **Axis** | One direction you can move along. Counting starts at 0. | **Axis 0** goes down the rows. **Axis 1** goes across the columns. |
| **Shape** | How many items there are along each axis, written in brackets | **(2, 3)**, meaning 2 rows and 3 columns |
| **Size** | The total number of elements (multiply the shape numbers) | 2 × 3 = **6** |
| **Index** | The position of an element. **Python starts counting from 0.** | The first row is row 0, the first column is column 0 |
| **Data type (dtype)** | The kind of numbers stored, such as whole numbers (`int`) or decimals (`float`) | Whole numbers here |

**Finding an element by index:** in the table above, `row 1, column 2` (counting from 0) is the number **6**.

> **Note on the word "rank":** you may see "rank of a tensor" in other places. It means the same as the number of dimensions. We will just say "number of dimensions" in this note, to avoid confusion with a different meaning of "rank" used for matrices.

---

## 4. Tensors in Machine Learning

In ML, data is stored as tensors. First, two words:

- A **sample** is one example in your data (one customer, one patient, one photo).
- A **feature** is one measured property of a sample (age, price, height).

### Example 1: a spreadsheet (2D tensor)

A table of 1000 customers, each with 5 features (age, income, and so on):

- Each **row** is one sample (one customer).
- Each **column** is one feature.
- Shape: **(1000, 5)**, so the size is 1000 × 5 = **5,000** numbers.

This is the most common shape you will meet in ML.

### Example 2: a black-and-white photo (2D tensor)

A photo is a grid of tiny dots called **pixels**. In a black-and-white photo, each pixel has one number for its brightness, from 0 (black) to 255 (white).

A small 28 by 28 photo has shape **(28, 28)**, so its size is **784** numbers.

### Example 3: a color photo (3D tensor)

A color pixel needs **3 numbers**: how much **red**, **green** and **blue** it has. Each of these three layers is called a **channel**.

| Pixel `[R, G, B]` | Color |
|---|---|
| `[255, 0, 0]` | Red |
| `[0, 255, 0]` | Green |
| `[255, 255, 255]` | White |
| `[0, 0, 0]` | Black |

A color photo that is 224 pixels tall and 224 wide has shape **(224, 224, 3)**.
Size = 224 × 224 × 3 = **150,528** numbers.

> **Channels last:** here the channel number (3) comes last in the shape. Some tools write it first, like (3, 224, 224), which is called "channels first". It is the same data, just arranged differently.

### Example 4: a batch of photos (4D tensor)

A **batch** is a group of samples handled together. Computers work faster on a group than on one photo at a time. A batch of 32 color photos has shape:

```
(32, 224, 224, 3)
 ↑    ↑    ↑   ↑
 |    |    |   └── 3 channels (red, green, blue)
 |    |    └────── 224 pixels wide
 |    └─────────── 224 pixels tall
 └──────────────── 32 photos in the batch
```

Size = 32 × 224 × 224 × 3 = **4,816,896** numbers.

### Summary of shapes

| Data | Shape | Dimensions |
|---|---|---|
| One value | `()` | 0 |
| One sample's features | `(5,)` | 1 |
| Spreadsheet of samples | `(1000, 5)` | 2 |
| Black-and-white photo | `(28, 28)` | 2 |
| Color photo | `(224, 224, 3)` | 3 |
| Batch of color photos | `(32, 224, 224, 3)` | 4 |

---

## 5. Basic Operations in Plain Words

We use these small tensors for the examples.

```
a = [1, 2, 3]
b = [10, 20, 30]

A = [[1, 2, 3],
     [4, 5, 6]]
```

### Adding or multiplying position by position

When two tensors have the **same shape**, you can combine the numbers that sit in the same position.

```
a + b = [1+10, 2+20, 3+30] = [11, 22, 33]
a × b = [1×10, 2×20, 3×30] = [10, 40, 90]
```

### Doing something to every number at once

```
a + 10 = [11, 12, 13]
```

The single number 10 is applied to every element. This is a simple case of what is called **broadcasting**: a smaller tensor is automatically "stretched" to fit a bigger one so the math works. Another example, adding a row to every row of a table:

```
[[1, 2, 3],        [10, 20, 30]        [[11, 22, 33],
 [4, 5, 6]]    +                    =   [14, 25, 36]]
```

The row `[10, 20, 30]` is added to **each** row of the table. Broadcasting works when, comparing shapes from the right, the numbers are equal or one of them is 1.

### Reshaping

**Reshaping** rearranges the **same numbers** into a different shape. Imagine 12 chairs: you can place them as 3 rows of 4, or 2 rows of 6. The chairs do not change, only the arrangement.

```
A has shape (2, 3):   [[1, 2, 3],
                       [4, 5, 6]]

Reshaped to (3, 2):   [[1, 2],
                       [3, 4],
                       [5, 6]]
```

The size must stay the same (6 numbers before and after).

### Transpose

**Transpose** flips rows and columns. The first row becomes the first column.

```
A = [[1, 2, 3],          Transpose of A = [[1, 4],
     [4, 5, 6]]                             [2, 5],
                                            [3, 6]]
```

Shape (2, 3) becomes (3, 2).

### Adding up along an axis

```
A = [[1, 2, 3],
     [4, 5, 6]]

sum along axis 0 (down the rows)    = [1+4, 2+5, 3+6] = [5, 7, 9]
sum along axis 1 (across the columns) = [1+2+3, 4+5+6] = [6, 15]
```

### Dot product

Multiply numbers in matching positions, then **add** the results. You get one number.

```
[1, 2, 3] · [4, 5, 6] = 1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32
```

This is how a model combines inputs with its settings to make a prediction (you will use it in Linear Regression).

### Matrix multiplication

This is a dot product done for every row of the first matrix with every column of the second.

```
A = [[1, 2],       B = [[5, 6],
     [3, 4]]            [7, 8]]

A @ B = [[1×5 + 2×7,  1×6 + 2×8],     = [[19, 22],
         [3×5 + 4×7,  3×6 + 4×8]]        [43, 50]]
```

**Shape rule:** the **inner numbers must match**, and the **outer numbers** give the result.

```
(2, 3) @ (3, 4) → (2, 4)
```

Here the inner numbers are both 3, so it works. `(2, 3) @ (2, 4)` would **not** work.

---

## 6. In Code (NumPy)

**NumPy** is a Python **library**, a ready-made collection of code, for working with tensors (it calls them arrays). Later phases use the same ideas in deep learning libraries.

```python
import numpy as np                      # load the NumPy library

A = np.array([[1, 2, 3],
              [4, 5, 6]])               # make a 2D tensor

print(A.ndim)    # number of dimensions -> 2
print(A.shape)   # shape                -> (2, 3)
print(A.size)    # total elements       -> 6

print(A[1, 2])           # row 1, column 2 (counting from 0) -> 6
print(A.reshape(3, 2))   # reshape to (3, 2)
print(A.T)               # transpose
print(A.sum(axis=0))     # [5 7 9]
print(A.sum(axis=1))     # [ 6 15]
```

---

## 7. Why Do We Use Tensors?

| Reason | Meaning |
|---|---|
| **One format for everything** | Spreadsheets, photos, text and sound can all be stored as tensors |
| **Speed** | Doing math on a whole tensor at once is far faster than looping through numbers one by one |
| **Batches** | Adding one extra dimension lets us process many samples at the same time |

---

## 8. Common Mistakes

| Mistake | Fix |
|---|---|
| Counting positions from 1 | Python counts from **0** |
| Mixing up dimensions and shape | Dimensions is how many axes (for example 2). Shape lists the size of each axis (for example (2, 3)). |
| Wrong axis when summing | Axis 0 goes down the rows, axis 1 goes across the columns |
| Reshaping to a size that doesn't fit | The total number of elements must stay the same |
| Multiplying matrices whose inner numbers differ | Check the shape rule: (2, 3) @ (3, 4) works |

---

## 9. Summary

- A **tensor** is a container that holds numbers arranged in a pattern.
- A **scalar** (0 dimensions), **vector** (1), and **matrix** (2) are all tensors.
- **Dimensions** = how many positions you need to find a number. **Shape** = the size along each axis. **Size** = total numbers.
- In ML, a spreadsheet has shape (samples, features), a color photo has (height, width, channels), and a batch of photos adds one more dimension.
- Useful operations: add or multiply position by position, reshape, transpose, sum along an axis, dot product and matrix multiplication.
- Python counts positions from 0.

---

## 10. Practice Questions

1. In your own words, what is a tensor? How many dimensions do a scalar, a vector and a matrix have?
2. What is the shape and size of `[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]`?
3. How many positions do you need to find one number in a table? In a stack of tables?
4. A dataset has 200 patients, each with 8 measurements. What is its shape and size?
5. What is the shape and size of a color photo that is 100 pixels tall and 100 wide? What if it is black and white?
6. A batch has 16 color photos, each 64 by 64 pixels, with channels last. Write its shape and size.
7. For `A = [[1, 2], [3, 4]]`, calculate the sum along axis 0 and along axis 1.
8. You have 12 numbers. Can you reshape them to (3, 4)? To (2, 6)? To (5, 3)?
9. Calculate `[1, 2, 3] + 10`.
10. Calculate the dot product of `[2, 3]` and `[4, 5]`.
11. Does `(4, 2) @ (2, 5)` work? What is the result shape? What about `(4, 2) @ (3, 5)`?

### Answers

1. A tensor is a container for numbers arranged in a pattern. A scalar has 0 dimensions, a vector 1, and a matrix 2.
2. Shape (3, 4), size 12.
3. 2 positions in a table (row, column), and 3 in a stack of tables.
4. Shape (200, 8), size 1,600.
5. Color: shape (100, 100, 3), size 30,000. Black and white: shape (100, 100), size 10,000.
6. Shape (16, 64, 64, 3), size 16 × 64 × 64 × 3 = 196,608.
7. Axis 0: [4, 6]. Axis 1: [3, 7].
8. (3, 4) yes. (2, 6) yes. (5, 3) no, because 5 × 3 = 15, not 12.
9. [11, 12, 13].
10. 2×4 + 3×5 = 8 + 15 = 23.
11. Yes, the inner numbers are both 2, and the result shape is (4, 5). `(4, 2) @ (3, 5)` does not work, because the inner numbers are 2 and 3.
