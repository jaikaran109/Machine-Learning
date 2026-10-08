# Python Fundamentals - Operators

## What are Operators?

Operators are special symbols that perform operations on values and variables.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

Here, `+` is an operator.

---

## Why Do We Need Operators?

Imagine you are building an ML model.

You may need to:

* Add values
* Compare values
* Check multiple conditions
* Update counters
* Perform mathematical calculations

Operators make all of this possible.

---

# Types of Operators

Python provides the following types of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Membership Operators
6. Identity Operators

---

# 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning        | Example |
| -------- | -------------- | ------- |
| +        | Addition       | 10 + 5  |
| -        | Subtraction    | 10 - 5  |
| *        | Multiplication | 10 * 5  |
| /        | Division       | 10 / 5  |
| //       | Floor Division | 10 // 3 |
| %        | Modulus        | 10 % 3  |
| **       | Power          | 2 ** 3  |

---

## Addition (+)

```python
a = 10
b = 20

print(a + b)
```

Output:

```text
30
```

---

## Subtraction (-)

```python
print(20 - 5)
```

Output:

```text
15
```

---

## Multiplication (*)

```python
print(10 * 5)
```

Output:

```text
50
```

---

## Division (/)

```python
print(10 / 3)
```

Output:

```text
3.3333333333333335
```

Division always returns a float.

---

## Floor Division (//)

Returns only the integer part.

```python
print(10 // 3)
```

Output:

```text
3
```

---

## Modulus (%)

Returns the remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 = 3 × 3 + 1
```

### Common Uses

Check Even Number:

```python
num = 8

print(num % 2 == 0)
```

Output:

```text
True
```

---

## Exponent (**)

Power operator.

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

# 2. Comparison Operators

Used to compare values.

Result is always:

```text
True
or
False
```

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal To                 |
| !=       | Not Equal To             |
| >        | Greater Than             |
| <        | Less Than                |
| >=       | Greater Than or Equal To |
| <=       | Less Than or Equal To    |

---

## Equal To (==)

```python
print(10 == 10)
```

Output:

```text
True
```

---

```python
print(10 == 5)
```

Output:

```text
False
```

---

## Not Equal To (!=)

```python
print(10 != 5)
```

Output:

```text
True
```

---

## Greater Than (>)

```python
print(20 > 10)
```

Output:

```text
True
```

---

## Less Than (<)

```python
print(20 < 10)
```

Output:

```text
False
```

---

## Greater Than or Equal To (>=)

```python
print(10 >= 10)
```

Output:

```text
True
```

---

## Less Than or Equal To (<=)

```python
print(5 <= 10)
```

Output:

```text
True
```

---

# 3. Logical Operators

Used when combining multiple conditions.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| and      | Both conditions must be True        |
| or       | At least one condition must be True |
| not      | Reverses result                     |

---

## AND Operator

```python
age = 20
citizen = True

print(age >= 18 and citizen)
```

Output:

```text
True
```

Both conditions are True.

---

## OR Operator

```python
print(10 > 20 or 5 < 10)
```

Output:

```text
True
```

At least one condition is True.

---

## NOT Operator

```python
print(not True)
```

Output:

```text
False
```

---

# 4. Assignment Operators

Used to assign values.

---

## Basic Assignment

```python
x = 10
```

---

## Add and Assign

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

Equivalent to:

```python
x = x + 5
```

---

## Subtract and Assign

```python
x -= 3
```

Equivalent to:

```python
x = x - 3
```

---

## Multiply and Assign

```python
x *= 2
```

Equivalent to:

```python
x = x * 2
```

---

## Divide and Assign

```python
x /= 2
```

Equivalent to:

```python
x = x / 2
```

---

# 5. Membership Operators

Used to check whether a value exists inside a collection.

| Operator | Meaning        |
| -------- | -------------- |
| in       | Exists         |
| not in   | Does Not Exist |

---

## in Operator

```python
subjects = ["Math", "Physics", "Chemistry"]

print("Math" in subjects)
```

Output:

```text
True
```

---

## not in Operator

```python
print("Biology" not in subjects)
```

Output:

```text
True
```

---

# 6. Identity Operators

Used to compare memory locations.

| Operator | Meaning          |
| -------- | ---------------- |
| is       | Same Object      |
| is not   | Different Object |

---

## Example

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

Both variables point to the same object.

---

# Operator Precedence

Python follows a specific order.

```text
()
**
*, /, //, %
+, -
Comparison Operators
not
and
or
```

---

## Example

```python
print(2 + 3 * 4)
```

Output:

```text
14
```

Because multiplication happens first.

Equivalent to:

```python
2 + (3 * 4)
```

---

# Operators Used Most in Machine Learning

### Very Frequently Used

```python
+
-
*
/
==
>
<
>=
<=
and
or
=
+=
```

---

### Frequently Used

```python
%
in
not in
```

---

### Rarely Used

```python
is
is not
```

Mostly for advanced Python concepts.

---

# Common Beginner Mistakes

## Mistake 1

```python
if age = 18:
```

Wrong.

Use:

```python
if age == 18:
```

Reason:

* `=` assigns
* `==` compares

---

## Mistake 2

```python
print(10 / 3)
```

Expecting:

```text
3
```

Actual:

```text
3.3333333333333335
```

Use:

```python
10 // 3
```

for integer division.

---

## Mistake 3

```python
print(True and False)
```

Output:

```text
False
```

Because AND requires both conditions to be True.

---

# Practice Questions

### Q1

Take two numbers and print:

* Sum
* Difference
* Product
* Quotient

---

### Q2

Check whether a number is even or odd using `%`.

---

### Q3

Check whether a student is eligible to vote.

Condition:

```text
Age >= 18
```

---

### Q4

Check whether a subject exists inside a list.

---

### Q5

Evaluate:

```python
10 + 5 * 2
```

without running the code.

---

# Quick Revision

* Arithmetic Operators → Mathematical calculations
* Comparison Operators → Compare values
* Logical Operators → Combine conditions
* Assignment Operators → Update variables
* Membership Operators → Check existence
* Identity Operators → Compare objects

---

# Summary

Operators are symbols used to perform calculations, comparisons, assignments, and logical evaluations. They form the foundation of decision-making, data processing, and mathematical computations in Python and are heavily used in Machine Learning, Data Analysis, and Software Development.
