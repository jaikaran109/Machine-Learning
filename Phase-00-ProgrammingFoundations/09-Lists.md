# Python Fundamentals - Lists

## What is a List?

A list is a collection of multiple values stored in a single variable.

Instead of creating many variables:

```python
subject1 = "Math"
subject2 = "Physics"
subject3 = "Chemistry"
```

We can store everything together:

```python
subjects = ["Math", "Physics", "Chemistry"]
```

A list helps us manage related data efficiently.

---

## Why Do We Need Lists?

Imagine storing marks of 100 students.

Without lists:

```python
mark1 = 90
mark2 = 85
mark3 = 78
...
```

Very difficult to manage.

With lists:

```python
marks = [90, 85, 78]
```

Everything is stored in a single variable.

---

# Real-Life Examples

### Student Marks

```python
marks = [90, 85, 78, 92]
```

---

### Subjects

```python
subjects = ["Math", "Physics", "Chemistry"]
```

---

### Shopping Cart

```python
cart = ["Milk", "Bread", "Butter"]
```

---

### ML Dataset Row

```python
features = [23, 45000, 1]
```

---

# Creating a List

## Syntax

```python
list_name = [value1, value2, value3]
```

Example:

```python
numbers = [10, 20, 30, 40]
```

---

# List Visualization

```python
numbers = [10, 20, 30, 40]
```

Memory Representation:

```text
Value : 10  20  30  40
Index : 0   1   2   3
```

Each element has an index.

---

# Accessing Elements

## Positive Indexing

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
```

Output:

```text
10
```

---

```python
print(numbers[2])
```

Output:

```text
30
```

---

# Negative Indexing

Python can count from the end.

```text
10  20  30  40
-4 -3 -2 -1
```

Example:

```python
print(numbers[-1])
```

Output:

```text
40
```

---

# List Length

Use `len()`.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

---

# Traversing a List

## Using for Loop

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

Output:

```text
10
20
30
```

---

# Modifying Elements

Lists are mutable.

Meaning:

```text
Lists can be changed after creation.
```

Example:

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

---

# Adding Elements

## append()

Adds an element at the end.

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

## insert()

Adds at a specific position.

```python
numbers = [10, 30]

numbers.insert(1, 20)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

# Removing Elements

## remove()

Removes by value.

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30]
```

---

## pop()

Removes by index.

```python
numbers = [10, 20, 30]

numbers.pop(1)

print(numbers)
```

Output:

```text
[10, 30]
```

---

# List Slicing

## Syntax

```python
list[start:end]
```

Start is included.

End is excluded.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

---

# Membership Operator

Check if an element exists.

```python
subjects = ["Math", "Physics", "Chemistry"]

print("Math" in subjects)
```

Output:

```text
True
```

---

```python
print("Biology" in subjects)
```

Output:

```text
False
```

---

# Useful List Methods

## sort()

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 5, 8]
```

---

## reverse()

```python
numbers = [1, 2, 3]

numbers.reverse()

print(numbers)
```

Output:

```text
[3, 2, 1]
```

---

## count()

```python
nums = [1, 2, 2, 2, 3]

print(nums.count(2))
```

Output:

```text
3
```

---

## index()

```python
nums = [10, 20, 30]

print(nums.index(20))
```

Output:

```text
1
```

---

# List Comprehension

A shorter way to create lists.

Traditional:

```python
squares = []

for i in range(5):
    squares.append(i * i)
```

---

List Comprehension:

```python
squares = [i * i for i in range(5)]
```

Output:

```text
[0, 1, 4, 9, 16]
```

---

# Why Lists are Important in Machine Learning

Before learning NumPy, almost everything starts with lists.

Example:

```python
ages = [18, 20, 22, 19]
```

---

Data Processing:

```python
for age in ages:
    print(age)
```

---

Feature Storage:

```python
features = [23, 45000, 1]
```

---

Model Predictions:

```python
predictions = [1, 0, 1, 1, 0]
```

Lists are everywhere in ML.

---

# Common Beginner Mistakes

## Mistake 1

Invalid Index

```python
numbers = [10, 20]

print(numbers[5])
```

Output:

```text
IndexError
```

---

## Mistake 2

Using Parentheses Instead of Brackets

Wrong:

```python
numbers = (10, 20, 30)
```

This creates a tuple.

Correct:

```python
numbers = [10, 20, 30]
```

---

## Mistake 3

Confusing append() and insert()

```python
append(value)
```

Adds at end.

```python
insert(index, value)
```

Adds at specific position.

---

# Practice Questions

### Q1

Create a list of 5 subjects and print all elements.

---

### Q2

Find the largest element in a list.

---

### Q3

Find the sum of all elements.

---

### Q4

Count even numbers in a list.

---

### Q5

Reverse a list.

---

### Q6

Check whether a given number exists in a list.

---

### Q7

Create a list of squares from 1 to 10 using list comprehension.

---

# Quick Revision

* List = Collection of multiple values.
* Lists are ordered.
* Lists are mutable.
* Indexing starts from 0.
* Negative indexing starts from the end.
* `append()` adds at the end.
* `insert()` adds at a specific position.
* `remove()` removes by value.
* `pop()` removes by index.
* Slicing extracts part of a list.
* List comprehensions create lists efficiently.

---

# Importance for Machine Learning

| Concept            | Importance |
| ------------------ | ---------- |
| Indexing           | ⭐⭐⭐⭐⭐      |
| Traversal          | ⭐⭐⭐⭐⭐      |
| append()           | ⭐⭐⭐⭐⭐      |
| Slicing            | ⭐⭐⭐⭐⭐      |
| Membership Testing | ⭐⭐⭐⭐       |
| List Comprehension | ⭐⭐⭐⭐⭐      |

Lists are one of the most frequently used data structures in Python and form the foundation for learning NumPy, Pandas, and Machine Learning.

---

# Summary

A list is an ordered and mutable collection of values. Lists allow us to store, access, modify, and process multiple pieces of data efficiently. They are one of the most important data structures in Python and are heavily used in Machine Learning, Data Analysis, and Software Development.
