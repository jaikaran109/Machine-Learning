# Python Fundamentals - List Comprehension

## What is List Comprehension?

List Comprehension is a concise way to create lists using a single line of code instead of writing a complete loop with `append()`.

Think of it as:

```text
Create List
+
Apply Logic
+
Store Result
```

all in one line.

---

# Why Do We Need List Comprehension?

Suppose we want squares of numbers from 1 to 5.

Traditional Approach:

```python
squares = []

for i in range(1, 6):
    squares.append(i * i)

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Works perfectly.

But Python provides a shorter and cleaner way.

---

# List Comprehension Version

```python
squares = [i * i for i in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Same result.

Less code.

More readable.

---

# General Syntax

```python
[new_value for item in iterable]
```

Read it as:

```text
For every item in iterable,
create new_value,
store it in a list.
```

---

# Understanding Each Part

Example:

```python
[i for i in range(5)]
```

### Expression

```python
i
```

What should be stored in the list?

---

### Loop Variable

```python
for i
```

Current value being processed.

---

### Iterable

```python
in range(5)
```

Source of values.

---

Python internally does:

```python
result = []

for i in range(5):
    result.append(i)
```

Output:

```text
[0, 1, 2, 3, 4]
```

---

# Example 1: Squares

Traditional:

```python
squares = []

for i in range(1, 6):
    squares.append(i * i)
```

---

List Comprehension:

```python
squares = [i * i for i in range(1, 6)]
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# Example 2: Cubes

```python
cubes = [i ** 3 for i in range(1, 6)]

print(cubes)
```

Output:

```text
[1, 8, 27, 64, 125]
```

---

# Example 3: Copy a List

```python
nums = [10, 20, 30]

copy_nums = [x for x in nums]

print(copy_nums)
```

Output:

```text
[10, 20, 30]
```

---

# Example 4: Convert Strings to Uppercase

```python
names = ["jai", "rahul", "aman"]

upper_names = [name.upper() for name in names]

print(upper_names)
```

Output:

```text
['JAI', 'RAHUL', 'AMAN']
```

---

# List Comprehension with Conditions

Sometimes we want only specific values.

Example:

Only even numbers.

Traditional:

```python
evens = []

for i in range(10):

    if i % 2 == 0:
        evens.append(i)
```

---

List Comprehension:

```python
evens = [i for i in range(10) if i % 2 == 0]

print(evens)
```

Output:

```text
[0, 2, 4, 6, 8]
```

---

# Syntax with Condition

```python
[new_value for item in iterable if condition]
```

---

# Example 5: Odd Numbers

```python
odds = [i for i in range(10) if i % 2 != 0]

print(odds)
```

Output:

```text
[1, 3, 5, 7, 9]
```

---

# Example 6: Filter Names

```python
names = ["Jai", "Rahul", "Aman", "Rohit"]

result = [name for name in names if len(name) > 4]

print(result)
```

Output:

```text
['Rahul', 'Rohit']
```

---

# Transform + Filter Together

Example:

Take only even numbers and square them.

```python
nums = [1, 2, 3, 4, 5, 6]

result = [x * x for x in nums if x % 2 == 0]

print(result)
```

Output:

```text
[4, 16, 36]
```

---

# Visual Understanding

```python
[x * x for x in range(5)]
```

Think:

```text
Take x
↓
Square x
↓
Store in list
↓
Repeat
```

---

# Common ML Examples

## Data Normalization

```python
marks = [50, 60, 70]

normalized = [x / 100 for x in marks]

print(normalized)
```

Output:

```text
[0.5, 0.6, 0.7]
```

---

## Feature Transformation

```python
ages = [18, 20, 22]

features = [age * 2 for age in ages]
```

---

## Data Filtering

```python
ages = [12, 18, 25, 15, 30]

adults = [age for age in ages if age >= 18]

print(adults)
```

Output:

```text
[18, 25, 30]
```

---

# Nested List Comprehension

Example:

```python
matrix = [[1, 2], [3, 4]]

flat = [num for row in matrix for num in row]

print(flat)
```

Output:

```text
[1, 2, 3, 4]
```

---

# When Should You Use List Comprehension?

Good:

```python
squares = [x * x for x in nums]
```

Simple and readable.

---

Bad:

```python
[x*y+z for x in a for y in b if condition1 and condition2]
```

Too complex.

Use normal loops if readability suffers.

---

# Common Beginner Mistakes

## Mistake 1

Wrong Order

Wrong:

```python
[i in range(5) for i]
```

Correct:

```python
[i for i in range(5)]
```

---

## Mistake 2

Forgetting Expression

Wrong:

```python
[for i in range(5)]
```

Correct:

```python
[i for i in range(5)]
```

---

## Mistake 3

Using It Everywhere

List comprehension is useful.

But if logic becomes complicated:

```python
Use a normal loop.
```

---

# Traditional Loop vs List Comprehension

### Traditional

```python
result = []

for x in nums:
    result.append(x * 2)
```

---

### List Comprehension

```python
result = [x * 2 for x in nums]
```

Both are correct.

List comprehension is shorter.

---

# Practice Questions

### Q1

Create a list of squares from 1 to 10.

---

### Q2

Create a list of cubes from 1 to 10.

---

### Q3

Create a list containing only even numbers from 1 to 20.

---

### Q4

Convert all names to uppercase using list comprehension.

---

### Q5

Create a list containing lengths of words.

Example:

```python
words = ["apple", "banana", "cat"]
```

Output:

```text
[5, 6, 3]
```

---

### Q6

Create a list containing squares of only even numbers.

---

# Quick Revision

* List Comprehension creates lists in a concise way.
* General syntax:

```python
[new_value for item in iterable]
```

* With condition:

```python
[new_value for item in iterable if condition]
```

* Can transform data.
* Can filter data.
* Can do both together.
* Frequently used in Python projects.

---

# Importance for Machine Learning

| Concept                     | Importance |
| --------------------------- | ---------- |
| Basic List Comprehension    | ⭐⭐⭐⭐⭐      |
| Filtering Data              | ⭐⭐⭐⭐⭐      |
| Transforming Data           | ⭐⭐⭐⭐⭐      |
| Combined Filter + Transform | ⭐⭐⭐⭐⭐      |
| Nested Comprehension        | ⭐⭐⭐        |

List Comprehension is heavily used in Data Cleaning, Feature Engineering, Data Transformation, and Machine Learning pipelines because it provides a concise and readable way to process collections of data.

---

# Summary

List Comprehension is a compact syntax for creating and transforming lists in Python. It combines looping, filtering, and value transformation into a single expression, making code shorter and often more readable. It is one of the most commonly used Python features in Data Science and Machine Learning.
