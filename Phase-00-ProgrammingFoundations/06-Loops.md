# Python Fundamentals - Loops

## What are Loops?

Loops are used to execute a block of code repeatedly.

Instead of writing the same code multiple times, we can place it inside a loop and let Python execute it automatically.

---

## Why Do We Need Loops?

Suppose we want to print:

```text
Hello
Hello
Hello
Hello
Hello
```

Without loops:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

This approach is repetitive and inefficient.

Using a loop:

```python
for i in range(5):
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
Hello
Hello
```

---

## Real-Life Examples

### Attendance System

```text
Check attendance of every student.
```

### Processing a Dataset

```text
Process every row in a CSV file.
```

### Machine Learning

```text
Train a model for multiple epochs.
```

### Gaming

```text
Keep running until the player exits.
```

---

# Types of Loops in Python

Python provides two main loops:

1. `for` Loop
2. `while` Loop

---

# The for Loop

Used when the number of iterations is known.

## Syntax

```python
for variable in sequence:
    statement
```

---

## Example

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## Understanding range()

```python
range(5)
```

Generates:

```text
0, 1, 2, 3, 4
```

---

### range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

### range(start, stop, step)

```python
for i in range(0, 11, 2):
    print(i)
```

Output:

```text
0
2
4
6
8
10
```

---

# Looping Through a List

```python
subjects = ["Math", "Physics", "Chemistry"]

for subject in subjects:
    print(subject)
```

Output:

```text
Math
Physics
Chemistry
```

---

# Looping Through a String

```python
name = "Jai"

for ch in name:
    print(ch)
```

Output:

```text
J
a
i
```

---

# The while Loop

Used when the number of iterations is unknown.

The loop continues until the condition becomes False.

## Syntax

```python
while condition:
    statement
```

---

## Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

## How It Works

### Iteration 1

```text
count = 1
1 <= 5 → True
```

Prints:

```text
1
```

---

### Iteration 2

```text
count = 2
2 <= 5 → True
```

Prints:

```text
2
```

And so on.

---

# Infinite Loop

A loop that never stops.

Example:

```python
while True:
    print("Hello")
```

This runs forever.

Use carefully.

---

# break Statement

Used to immediately stop a loop.

## Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

Loop stops when `i` becomes 5.

---

# continue Statement

Used to skip the current iteration.

## Example

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

The value 2 is skipped.

---

# pass Statement

Placeholder for future code.

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

Output:

```text
0
1
2
3
4
```

`pass` does nothing.

---

# Nested Loops

A loop inside another loop.

## Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

---

## Real-Life Example

Think of a classroom.

```text
For every row
    For every student
        Mark attendance
```

---

# enumerate()

Used when we need both index and value.

Example:

```python
subjects = ["Math", "Physics", "Chemistry"]

for index, subject in enumerate(subjects):
    print(index, subject)
```

Output:

```text
0 Math
1 Physics
2 Chemistry
```

---

# zip()

Used to iterate through multiple collections together.

Example:

```python
names = ["Jai", "Rahul"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```text
Jai 90
Rahul 85
```

---

# Common Uses in Machine Learning

## Data Processing

```python
for row in dataset:
    process(row)
```

---

## Data Cleaning

```python
for value in data:

    if value is None:
        value = 0
```

---

## Training Loop

```python
for epoch in range(100):
    train_model()
```

---

## Evaluating Predictions

```python
correct = 0

for i in range(len(actual)):

    if actual[i] == predicted[i]:
        correct += 1
```

---

# Common Beginner Mistakes

## Mistake 1

Forgetting Colon

Wrong:

```python
for i in range(5)
    print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

## Mistake 2

Infinite While Loop

Wrong:

```python
count = 1

while count <= 5:
    print(count)
```

`count` never changes.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Mistake 3

Wrong Range Expectation

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

Not:

```text
1 2 3 4 5
```

---

# Practice Questions

### Q1

Print numbers from 1 to 100.

---

### Q2

Print all even numbers from 1 to 100.

---

### Q3

Find the sum of first N natural numbers.

---

### Q4

Print the multiplication table of a number.

---

### Q5

Count the number of digits in a number.

---

### Q6

Reverse a number.

Example:

```text
1234 → 4321
```

---

### Q7

Check whether a number is a palindrome.

Example:

```text
121 → Palindrome
123 → Not Palindrome
```

---

### Q8

Find the largest element in a list.

---

# Quick Revision

* `for` loop → Used when iterations are known.
* `while` loop → Used when iterations are unknown.
* `range()` → Generates numbers.
* `break` → Stops the loop.
* `continue` → Skips current iteration.
* `pass` → Placeholder statement.
* Nested loops → Loop inside another loop.
* `enumerate()` → Index + Value.
* `zip()` → Multiple collections together.

---

# Importance for Machine Learning

| Concept      | Importance |
| ------------ | ---------- |
| for Loop     | ⭐⭐⭐⭐⭐      |
| while Loop   | ⭐⭐⭐⭐       |
| break        | ⭐⭐⭐⭐       |
| continue     | ⭐⭐⭐⭐       |
| range()      | ⭐⭐⭐⭐⭐      |
| Nested Loops | ⭐⭐⭐⭐⭐      |
| enumerate()  | ⭐⭐⭐⭐       |
| zip()        | ⭐⭐⭐⭐       |

---

# Summary

Loops allow a program to execute a block of code repeatedly. Python provides `for` and `while` loops for iteration. Loops are heavily used in Machine Learning, Data Analysis, Data Processing, Automation, and Software Development because they make it possible to work with large amounts of data efficiently.
