# Python Fundamentals - Modules & Packages

## Why Do We Need Modules?

Imagine you write a calculator program.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

Now imagine another project needs the same functions.

Without modules:

```text
Copy Code
Paste Code
Copy Code
Paste Code
```

Again and again.

Not efficient.

---

## Solution: Modules

A module is simply a Python file containing code that can be reused in other programs.

Example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

This file itself is a module.

---

# What is a Module?

A module is a Python file (`.py`) containing:

* Functions
* Variables
* Classes

that can be imported and reused.

Example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b
```

This is a module.

---

# Importing a Module

Suppose:

```text
calculator.py
```

contains:

```python
def add(a, b):
    return a + b
```

Main file:

```python
import calculator

print(calculator.add(10, 20))
```

Output:

```text
30
```

---

# Real-Life Analogy

Imagine a toolbox.

```text
Toolbox
 ├── Hammer
 ├── Screwdriver
 ├── Wrench
```

Instead of building tools every time:

```text
Take tool from toolbox
Use it
```

Modules work exactly like that.

---

# Built-in Modules

Python already provides many modules.

Example:

```python
import math
```

```python
print(math.sqrt(25))
```

Output:

```text
5.0
```

---

Another example:

```python
import random

print(random.randint(1, 10))
```

Output:

```text
7
```

(Random value)

---

# Different Ways to Import

## Method 1

```python
import math

print(math.sqrt(25))
```

---

## Method 2

Import specific function.

```python
from math import sqrt

print(sqrt(25))
```

Output:

```text
5.0
```

---

## Method 3

Import multiple functions.

```python
from math import sqrt, factorial
```

---

## Method 4

Alias

```python
import math as m

print(m.sqrt(25))
```

Output:

```text
5.0
```

Useful when module names are long.

---

# What Happens During Import?

Suppose:

```python
import math
```

Python:

```text
1. Finds module
2. Loads module
3. Makes functions available
```

Then:

```python
math.sqrt(25)
```

works.

---

# Why Modules Are Important

Without modules:

```python
Everything in one file
```

Large projects become messy.

---

With modules:

```text
project/
│
├── main.py
├── database.py
├── auth.py
├── utils.py
```

Code becomes organized.

---

# Creating Your Own Module

File:

```text
calculator.py
```

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

---

Main File:

```python
import calculator

print(calculator.add(5, 10))
```

Output:

```text
15
```

---

# What is a Package?

A package is a collection of modules.

Think:

```text
Module
↓
Single Python File
```

---

```text
Package
↓
Folder containing multiple modules
```

---

# Example Package Structure

```text
school/

├── student.py
├── teacher.py
├── marks.py
```

Here:

```text
school
```

is a package.

---

```text
student.py
teacher.py
marks.py
```

are modules.

---

# Real-Life Analogy

Think of a library.

```text
Library
    ↓
    Bookshelf
        ↓
        Books
```

---

```text
Package
    ↓
    Modules
```

---

# Importing from Package

Structure:

```text
school/

├── student.py
```

Inside:

```python
def show_student():
    print("Student Data")
```

Main file:

```python
from school.student import show_student

show_student()
```

Output:

```text
Student Data
```

---

# Popular Python Packages

You will use these heavily in ML.

## NumPy

```python
import numpy as np
```

Used for:

```text
Arrays
Matrix Operations
Numerical Computing
```

---

## Pandas

```python
import pandas as pd
```

Used for:

```text
Data Analysis
Data Cleaning
```

---

## Matplotlib

```python
import matplotlib.pyplot as plt
```

Used for:

```text
Graphs
Charts
Visualization
```

---

## Scikit-Learn

```python
from sklearn import datasets
```

Used for:

```text
Machine Learning Algorithms
```

---

## TensorFlow

```python
import tensorflow as tf
```

Used for:

```text
Deep Learning
```

---

# Why Packages Matter in ML

Without packages:

```text
Need to write every algorithm manually
```

Impossible.

---

With packages:

```python
import pandas
import numpy
import sklearn
```

Thousands of ready-made functions become available.

---

# Common Beginner Mistakes

## Mistake 1

Forgetting Import

```python
print(sqrt(25))
```

Output:

```text
NameError
```

Need:

```python
from math import sqrt
```

---

## Mistake 2

Wrong Module Name

```python
import Maths
```

Output:

```text
ModuleNotFoundError
```

Correct:

```python
import math
```

---

## Mistake 3

Confusing Module and Package

```text
calculator.py
```

Module

---

```text
school/
```

Package

---

# Practice Questions

### Q1

Import the `math` module and find square root of 49.

---

### Q2

Import `random` and generate a random number.

---

### Q3

Create your own module containing add() and subtract().

---

### Q4

Import your custom module and use its functions.

---

### Q5

Create a package with two modules and import one function.

---

# Quick Revision

* Module = Python file.
* Package = Folder containing modules.
* `import` loads modules.
* `from module import function` imports specific functions.
* `as` creates aliases.
* Modules improve code reuse.
* Packages improve code organization.

---

# Importance for Machine Learning

| Concept              | Importance |
| -------------------- | ---------- |
| import               | ⭐⭐⭐⭐⭐      |
| Built-in Modules     | ⭐⭐⭐⭐       |
| Custom Modules       | ⭐⭐⭐        |
| Packages             | ⭐⭐⭐⭐⭐      |
| Aliases (`np`, `pd`) | ⭐⭐⭐⭐⭐      |

Modules and Packages are the foundation of Machine Learning because every ML project depends heavily on libraries such as NumPy, Pandas, Matplotlib, Scikit-Learn, TensorFlow, and PyTorch.

---

# Summary

A Module is a Python file containing reusable code, while a Package is a collection of related modules organized inside a folder. Modules and packages promote code reuse, improve project structure, and form the foundation of modern Python development. In Machine Learning, nearly all functionality comes from powerful external packages such as NumPy, Pandas, Scikit-Learn, TensorFlow, and PyTorch.
