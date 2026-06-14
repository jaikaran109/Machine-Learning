# Python Fundamentals - Conditions (if-else)

## What are Conditions?

Conditions allow a program to make decisions based on certain situations.

Think of them as asking a question:

```text
Is age greater than or equal to 18?
```

If the answer is YES, do one thing.

If the answer is NO, do another thing.

---

## Why Do We Need Conditions?

Without conditions, every program would behave the same way regardless of input.

### Real-Life Examples

#### Voting

```text
If age >= 18
    Can Vote
Else
    Cannot Vote
```

#### ATM

```text
If PIN is correct
    Allow transaction
Else
    Show error
```

#### ML Example

```text
If prediction probability > 0.5
    Spam
Else
    Not Spam
```

Conditions are used everywhere.

---

# The if Statement

Used when you want to execute code only if a condition is True.

## Syntax

```python
if condition:
    statement
```

---

## Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

Output:

```text
Eligible to Vote
```

Because:

```text
20 >= 18
```

is True.

---

## Example

```python
age = 15

if age >= 18:
    print("Eligible to Vote")
```

Output:

```text
No Output
```

Because condition is False.

---

# The if-else Statement

Used when there are two possible outcomes.

## Syntax

```python
if condition:
    statement1
else:
    statement2
```

---

## Example

```python
age = 15

if age >= 18:
    print("Can Vote")
else:
    print("Cannot Vote")
```

Output:

```text
Cannot Vote
```

---

## Flow

```text
Condition
   |
   |
 True ---------> if block
   |
 False --------> else block
```

Only one block executes.

---

# The if-elif-else Statement

Used when there are multiple conditions.

## Syntax

```python
if condition1:
    statement1

elif condition2:
    statement2

else:
    statement3
```

---

## Example

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

else:
    print("Grade C")
```

Output:

```text
Grade B
```

---

## Flow

Python checks from top to bottom.

```text
Condition 1
    ↓
Condition 2
    ↓
Condition 3
```

The first True condition executes.

Then Python stops checking.

---

# Multiple elif Statements

```python
marks = 65

if marks >= 90:
    print("A")

elif marks >= 80:
    print("B")

elif marks >= 70:
    print("C")

elif marks >= 60:
    print("D")

else:
    print("F")
```

Output:

```text
D
```

---

# Nested Conditions

An if statement inside another if statement.

## Example

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")
```

Output:

```text
Eligible to Vote
```

---

## Real-Life Example

```text
If age >= 18
    If citizen
        Allow voting
```

Both conditions must be satisfied.

---

# Comparison Operators Used in Conditions

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal To                 |
| !=       | Not Equal To             |
| >        | Greater Than             |
| <        | Less Than                |
| >=       | Greater Than or Equal To |
| <=       | Less Than or Equal To    |

---

## Example

```python
age = 20

if age == 20:
    print("Age is 20")
```

Output:

```text
Age is 20
```

---

# Logical Operators in Conditions

## AND

Both conditions must be True.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

Output:

```text
Eligible
```

---

## OR

At least one condition must be True.

```python
print(10 > 20 or 5 < 10)
```

Output:

```text
True
```

---

## NOT

Reverses the result.

```python
print(not True)
```

Output:

```text
False
```

---

# Truthy and Falsy Values

Python treats some values as False.

## Falsy Values

```python
False
0
0.0
""
[]
{}
set()
None
```

---

## Example

```python
name = ""

if name:
    print("Name Exists")
else:
    print("Empty")
```

Output:

```text
Empty
```

---

# Short-Hand if

Single-line if.

```python
age = 20

if age >= 18: print("Can Vote")
```

---

# Ternary Operator

Compact if-else.

## Syntax

```python
value_if_true if condition else value_if_false
```

---

## Example

```python
age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)
```

Output:

```text
Adult
```

---

# Most Common ML Uses

### Filtering Data

```python
if age > 18:
    ...
```

---

### Data Cleaning

```python
if value is None:
    ...
```

---

### Feature Engineering

```python
if salary > 50000:
    category = "High"
else:
    category = "Low"
```

---

### Prediction Logic

```python
if probability > 0.5:
    prediction = 1
else:
    prediction = 0
```

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

```text
=  Assignment
== Comparison
```

---

## Mistake 2

```python
if age >= 18
    print("Vote")
```

Missing colon.

Correct:

```python
if age >= 18:
    print("Vote")
```

---

## Mistake 3

Incorrect indentation.

Wrong:

```python
if age >= 18:
print("Vote")
```

Correct:

```python
if age >= 18:
    print("Vote")
```

Python relies on indentation.

---

# Practice Questions

### Q1

Take age as input and check whether a person can vote.

---

### Q2

Take a number and check whether it is positive or negative.

---

### Q3

Take marks and print:

```text
90+  → A
75+  → B
60+  → C
Else → F
```

---

### Q4

Check whether a year is a leap year.

---

### Q5

Take username and password and validate login.

---

# Quick Revision

* `if` → One condition
* `if-else` → Two outcomes
* `if-elif-else` → Multiple outcomes
* Nested if → Condition inside condition
* `and` → Both True
* `or` → Any one True
* `not` → Reverse result
* Python uses indentation to define blocks

---

# Summary

Conditions allow programs to make decisions based on data. Python provides `if`, `if-else`, and `if-elif-else` statements to control program flow. Conditions are heavily used in Machine Learning, Data Analysis, Web Development, and almost every real-world software application.
