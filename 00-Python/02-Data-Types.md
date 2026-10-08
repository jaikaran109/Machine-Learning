# Python Fundamentals - Data Types

## What are Data Types?

A data type defines the kind of value a variable can store.

In simple words:

> Data types tell Python what type of information is being stored.

Examples:

* Name → Text
* Age → Number
* Height → Decimal Number
* Student Status → True/False

Different kinds of data require different data types.

---

## Why Do We Need Data Types?

Imagine a college management system.

```python
student_name = "Jai"
age = 20
cgpa = 8.5
is_student = True
```

All values are different.

* `"Jai"` is text
* `20` is a whole number
* `8.5` is a decimal number
* `True` is a boolean value

Python needs to know the type of data to perform operations correctly.

---

# Built-in Data Types in Python

Python provides several built-in data types.

| Data Type | Example         |
| --------- | --------------- |
| int       | 10              |
| float     | 5.8             |
| str       | "Hello"         |
| bool      | True            |
| list      | [1, 2, 3]       |
| tuple     | (1, 2, 3)       |
| set       | {1, 2, 3}       |
| dict      | {"name": "Jai"} |

---

# 1. Integer (int)

Integers are whole numbers.

Examples:

```python
age = 20
marks = 95
temperature = -5
```

Valid integers:

```python
10
0
-100
5000
```

Check type:

```python
age = 20
print(type(age))
```

Output:

```text
<class 'int'>
```

### Real-Life Examples

* Age
* Number of students
* Roll number
* Population

---

# 2. Float (float)

Floats are decimal numbers.

Examples:

```python
cgpa = 8.5
height = 5.9
price = 99.99
```

Check type:

```python
cgpa = 8.5
print(type(cgpa))
```

Output:

```text
<class 'float'>
```

### Real-Life Examples

* Height
* Weight
* CGPA
* Product Price

---

# 3. String (str)

Strings store text.

Strings must be enclosed in quotes.

Examples:

```python
name = "Jai"
city = "Lucknow"
```

Single quotes also work:

```python
name = 'Jai'
```

Check type:

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

---

## Accessing Characters

```python
name = "Jai"

print(name[0])
```

Output:

```text
J
```

Indexing:

```text
J  a  i
0  1  2
```

---

## String Operations

### Length

```python
name = "Jai"

print(len(name))
```

Output:

```text
3
```

---

### Uppercase

```python
print(name.upper())
```

Output:

```text
JAI
```

---

### Lowercase

```python
print(name.lower())
```

Output:

```text
jai
```

---

# 4. Boolean (bool)

Booleans represent only two values.

```python
True
False
```

Examples:

```python
is_student = True
is_logged_in = False
```

Check type:

```python
print(type(is_student))
```

Output:

```text
<class 'bool'>
```

---

## Real-Life Examples

```text
Light ON/OFF
YES/NO
PASS/FAIL
TRUE/FALSE
```

---

## Boolean Comparisons

```python
print(10 > 5)
```

Output:

```text
True
```

---

```python
print(10 < 5)
```

Output:

```text
False
```

---

# 5. List

Lists store multiple values together.

```python
subjects = ["Math", "Physics", "Chemistry"]
```

Check type:

```python
print(type(subjects))
```

Output:

```text
<class 'list'>
```

---

## Features of Lists

* Ordered
* Mutable (can be changed)
* Allow duplicates

Example:

```python
numbers = [10, 20, 30]
```

Access:

```python
print(numbers[0])
```

Output:

```text
10
```

---

## Modifying Lists

```python
numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

---

# 6. Tuple

Tuples are similar to lists.

Difference:

> Tuples cannot be modified.

Example:

```python
data = (10, 20, 30)
```

Check type:

```python
print(type(data))
```

Output:

```text
<class 'tuple'>
```

---

## Invalid Operation

```python
data[0] = 100
```

Output:

```text
TypeError
```

---

## When to Use Tuple?

When data should remain fixed.

Examples:

* Coordinates
* Dates
* Months

---

# 7. Set

Sets store unique values only.

Example:

```python
nums = {1, 2, 3, 3, 4, 4}
print(nums)
```

Output:

```text
{1, 2, 3, 4}
```

Duplicates are automatically removed.

---

## Features

* Unordered
* No duplicates
* Mutable

---

## Real-Life Example

Student IDs:

```python
{101, 102, 103}
```

Each ID must be unique.

---

# 8. Dictionary

Dictionaries store data as key-value pairs.

Example:

```python
student = {
    "name": "Jai",
    "age": 20,
    "cgpa": 8.5
}
```

Check type:

```python
print(type(student))
```

Output:

```text
<class 'dict'>
```

---

## Accessing Values

```python
print(student["name"])
```

Output:

```text
Jai
```

---

## Real-Life Example

```text
Roll Number → Student
Username → Profile
Word → Meaning
```

Everything is stored as Key → Value.

---

# Type Conversion

Sometimes we need to convert one data type into another.

---

## Integer to String

```python
age = 20

age = str(age)

print(type(age))
```

Output:

```text
<class 'str'>
```

---

## String to Integer

```python
num = "100"

num = int(num)

print(type(num))
```

Output:

```text
<class 'int'>
```

---

## Integer to Float

```python
x = 10

x = float(x)

print(x)
```

Output:

```text
10.0
```

---

# Common Beginner Mistakes

## Mistake 1

```python
age = "20"

print(age + 5)
```

Error because `"20"` is a string.

Correct:

```python
age = int(age)

print(age + 5)
```

---

## Mistake 2

```python
name = Jai
```

Strings require quotes.

Correct:

```python
name = "Jai"
```

---

## Mistake 3

```python
data = (10, 20, 30)

data[0] = 100
```

Tuples cannot be modified.

---

# Practice Questions

### Q1

Create variables of type:

* int
* float
* str
* bool

Print their types.

---

### Q2

Create a list of 5 subjects and print the first subject.

---

### Q3

Create a tuple containing 5 numbers.

---

### Q4

Create a set with duplicate values and observe the output.

---

### Q5

Create a dictionary storing:

```text
Name
Age
City
```

Print all values.

---

# Quick Revision

* `int` → Whole Numbers
* `float` → Decimal Numbers
* `str` → Text
* `bool` → True/False
* `list` → Ordered, Mutable
* `tuple` → Ordered, Immutable
* `set` → Unique Values
* `dict` → Key-Value Pairs

---

# Summary

Data types define the kind of value stored in a variable. Python provides several built-in data types such as integers, floats, strings, booleans, lists, tuples, sets, and dictionaries. Choosing the correct data type makes programs efficient, readable, and easier to maintain.
