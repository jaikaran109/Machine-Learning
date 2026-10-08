# Python Fundamentals - Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Think of a function as a machine.

```text
Input
  ↓
┌──────────┐
│ Function │
└──────────┘
  ↓
Output
```

Example:

```text
2, 3
 ↓
ADD MACHINE
 ↓
5
```

The machine takes inputs, performs some work, and produces an output.

---

# Why Do We Need Functions?

Suppose we want to add numbers.

Without functions:

```python
print(2 + 3)
print(10 + 20)
print(50 + 100)
print(200 + 300)
```

This becomes repetitive.

Imagine writing the same logic hundreds of times.

Instead, we can create a reusable function.

```python
def add(a, b):
    return a + b
```

Now:

```python
print(add(2, 3))
print(add(10, 20))
print(add(50, 100))
```

Output:

```text
5
30
150
```

Write once.

Use many times.

This is the biggest advantage of functions.

---

# Real-Life Analogy

Imagine a mixer grinder.

Buying a mixer:

```text
def mixer()
```

Turning it on:

```text
mixer()
```

Giving ingredients:

```text
mixer(mango, milk, sugar)
```

Getting the result:

```text
Mango Shake
```

Functions work exactly like this.

---

# Creating a Function

## Syntax

```python
def function_name():
    statements
```

Example:

```python
def greet():
    print("Hello")
```

---

# Understanding Each Part

```python
def greet():
    print("Hello")
```

### def

Means:

```text
I am creating a function.
```

---

### greet

Function name.

Just like variables have names.

Functions also have names.

---

### ()

Parentheses.

Used to pass inputs.

Currently empty.

---

### :

Mandatory syntax.

---

# Important Concept

After writing:

```python
def greet():
    print("Hello")
```

Nothing happens.

Output:

```text
No Output
```

Why?

Because you only created the function.

You did not execute it.

---

# Calling a Function

To execute a function:

```python
greet()
```

Output:

```text
Hello
```

---

## Easy Trick

```text
def greet()
```

Means:

```text
Build the machine.
```

---

```text
greet()
```

Means:

```text
Start the machine.
```

---

# Parameters

Parameters are inputs accepted by a function.

Example:

```python
def greet(name):
    print("Hello", name)
```

Here:

```text
name
```

is a parameter.

---

# Calling with Arguments

```python
greet("Jai")
```

Output:

```text
Hello Jai
```

---

## Visual Representation

```text
greet("Jai")

name = "Jai"
```

Function receives:

```text
Jai
```

and uses it.

---

# Parameters vs Arguments

This confuses many beginners.

## Function Definition

```python
def add(a, b):
```

These are called:

```text
Parameters
```

---

## Function Call

```python
add(2, 3)
```

These are called:

```text
Arguments
```

---

## Easy Rule

```text
Function Creation → Parameters

Function Call → Arguments
```

---

# Multiple Parameters

Functions can accept multiple inputs.

Example:

```python
def add(a, b):
    print(a + b)
```

Call:

```python
add(10, 20)
```

Output:

```text
30
```

---

Another example:

```python
add(50, 70)
```

Output:

```text
120
```

Same function.

Different inputs.

---

# Return Statement

Most important concept in functions.

Many beginners confuse `print()` and `return`.

---

# Using print()

```python
def add(a, b):
    print(a + b)
```

Call:

```python
add(2, 3)
```

Output:

```text
5
```

Looks fine.

But the value is not stored anywhere.

---

# Using return()

```python
def add(a, b):
    return a + b
```

Now:

```python
result = add(2, 3)

print(result)
```

Output:

```text
5
```

But now:

```python
result
```

contains:

```text
5
```

which can be used later.

---

# Why Return is Important

Example:

```python
def add(a, b):
    return a + b
```

Now:

```python
x = add(2, 3)

print(x * 10)
```

Output:

```text
50
```

Because:

```text
add(2,3)
```

returns:

```text
5
```

Then:

```text
5 × 10
```

becomes:

```text
50
```

---

# Print vs Return

## Print

```python
def add(a, b):
    print(a + b)
```

Used when:

```text
You only want to display the result.
```

---

## Return

```python
def add(a, b):
    return a + b
```

Used when:

```text
You want to use the result later.
```

---

# Default Parameters

Functions can have default values.

Example:

```python
def greet(name="Guest"):
    print("Hello", name)
```

Call:

```python
greet()
```

Output:

```text
Hello Guest
```

---

Call:

```python
greet("Jai")
```

Output:

```text
Hello Jai
```

---

# Functions Returning Multiple Values

Example:

```python
def calculate(a, b):
    return a + b, a - b
```

Call:

```python
sum_value, diff_value = calculate(10, 5)

print(sum_value)
print(diff_value)
```

Output:

```text
15
5
```

---

# Variable Scope

Variables created inside a function exist only inside that function.

Example:

```python
def demo():
    x = 10

demo()

print(x)
```

Output:

```text
Error
```

Because:

```text
x exists only inside demo().
```

---

# Common Uses in Machine Learning

## Data Cleaning

```python
def clean_data(data):
    return cleaned_data
```

---

## Feature Engineering

```python
def categorize_salary(salary):
    if salary > 50000:
        return "High"
    return "Low"
```

---

## Data Normalization

```python
def normalize(x):
    return x / 100
```

---

## Model Evaluation

```python
def accuracy(correct, total):
    return correct / total
```

---

Every ML library uses functions heavily.

---

# Common Beginner Mistakes

## Mistake 1

Creating a function but not calling it.

Wrong:

```python
def greet():
    print("Hello")
```

Output:

```text
Nothing
```

Correct:

```python
greet()
```

---

## Mistake 2

Confusing print and return.

Wrong Understanding:

```text
print and return are same
```

They are not.

---

## Mistake 3

Wrong Number of Arguments

```python
def add(a, b):
```

Wrong:

```python
add(5)
```

Output:

```text
TypeError
```

Because two arguments are required.

---

# Practice Questions

### Q1

Create a function that prints:

```text
Hello World
```

---

### Q2

Create a function that accepts a name and prints:

```text
Hello <name>
```

---

### Q3

Create a function that returns the square of a number.

Example:

```text
Input: 5
Output: 25
```

---

### Q4

Create a function that returns the larger of two numbers.

---

### Q5

Create a function that checks whether a number is even or odd.

---

### Q6

Create a function that calculates the area of a rectangle.

Formula:

```text
Area = Length × Breadth
```

---

# Quick Revision

* Function = Reusable block of code.
* `def` creates a function.
* Function name identifies the function.
* Parameters receive inputs.
* Arguments are values passed during function call.
* `return` sends a value back.
* `print` only displays output.
* Functions reduce repetition and improve code readability.

---

# Importance for Machine Learning

| Concept            | Importance |
| ------------------ | ---------- |
| Function Creation  | ⭐⭐⭐⭐⭐      |
| Parameters         | ⭐⭐⭐⭐⭐      |
| Arguments          | ⭐⭐⭐⭐⭐      |
| Return Statement   | ⭐⭐⭐⭐⭐      |
| Default Parameters | ⭐⭐⭐⭐       |
| Variable Scope     | ⭐⭐⭐⭐       |

Functions are one of the most heavily used concepts in Machine Learning, Data Science, Web Development, and Software Engineering.

---

# Summary

A function is a reusable block of code that performs a specific task. Functions help avoid code repetition, improve readability, and make programs easier to maintain. They can accept inputs through parameters, perform operations, and return results using the `return` statement. Almost every real-world Python application and Machine Learning project is built using functions.
