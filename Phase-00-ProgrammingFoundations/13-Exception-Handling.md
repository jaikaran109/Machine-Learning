# Python Fundamentals - Exception Handling

## What is an Exception?

An Exception is a runtime error that occurs while a program is executing.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError: division by zero
```

The program crashes because an exception occurred.

---

# Why Do We Need Exception Handling?

Imagine you're building:

* ATM Software
* Banking System
* Instagram
* WhatsApp
* Machine Learning Pipeline

Users can make mistakes.

Examples:

```text
Enter invalid input
Open missing file
Divide by zero
Access invalid index
```

Without exception handling:

```text
Program crashes
```

With exception handling:

```text
Program continues safely
```

---

# Real-Life Analogy

Imagine driving a car.

Without brakes:

```text
Problem occurs
↓
Crash
```

With brakes:

```text
Problem occurs
↓
Handle problem safely
↓
Continue journey
```

Exception Handling acts like brakes for your program.

---

# Common Exceptions

## ZeroDivisionError

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

---

## ValueError

```python
age = int("abc")
```

Output:

```text
ValueError
```

---

## IndexError

```python
nums = [10, 20]

print(nums[5])
```

Output:

```text
IndexError
```

---

## KeyError

```python
student = {
    "name": "Jai"
}

print(student["age"])
```

Output:

```text
KeyError
```

---

## FileNotFoundError

```python
open("data.txt")
```

Output:

```text
FileNotFoundError
```

---

# The Problem

Suppose:

```python
num = int(input("Enter Number: "))

print(100 / num)

print("Program Finished")
```

Input:

```text
0
```

Output:

```text
ZeroDivisionError
```

Program stops immediately.

---

# try and except

Used to handle exceptions.

## Syntax

```python
try:
    risky_code

except:
    handle_error
```

---

## Example

```python
try:
    print(10 / 0)

except:
    print("Something went wrong")
```

Output:

```text
Something went wrong
```

Program does not crash.

---

# How try-except Works

```text
try block
    ↓
No Error?
    ↓
Continue Normally
```

---

```text
try block
    ↓
Error Occurs?
    ↓
Jump to except block
```

---

# Handling Specific Exceptions

Better than using a generic except.

Example:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

# Multiple Exceptions

Example:

```python
try:

    num = int(input())

    print(10 / num)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot Divide By Zero")
```

Possible Outputs:

```text
Invalid Input
```

or

```text
Cannot Divide By Zero
```

---

# Capturing Error Message

Use:

```python
except Exception as e
```

Example:

```python
try:
    print(10 / 0)

except Exception as e:
    print(e)
```

Output:

```text
division by zero
```

---

# else Block

Runs only when no exception occurs.

Example:

```python
try:

    num = int(input())

    print(10 / num)

except ZeroDivisionError:

    print("Cannot Divide By Zero")

else:

    print("Operation Successful")
```

Input:

```text
2
```

Output:

```text
5.0
Operation Successful
```

---

# finally Block

Runs no matter what happens.

Example:

```python
try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Program Ended")
```

Output:

```text
Error
Program Ended
```

---

# Why finally is Useful

Suppose:

```python
file = open("data.txt")
```

Even if an error occurs:

```text
File must be closed
```

Example:

```python
try:

    file = open("data.txt")

except:

    print("Error")

finally:

    print("Cleaning Resources")
```

---

# Complete Flow

```text
try
 ↓
No Error?
 ↓
else
 ↓
finally
```

---

```text
try
 ↓
Error?
 ↓
except
 ↓
finally
```

---

# Raising Exceptions

You can create exceptions manually.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age Cannot Be Negative")
```

Output:

```text
ValueError: Age Cannot Be Negative
```

---

# Custom Validation Example

```python
salary = -1000

if salary < 0:
    raise ValueError("Invalid Salary")
```

---

# Common Uses in Machine Learning

## Reading Dataset

```python
try:
    file = open("data.csv")

except FileNotFoundError:
    print("Dataset Not Found")
```

---

## Handling User Input

```python
try:
    age = int(input())

except ValueError:
    print("Enter Valid Number")
```

---

## Model Loading

```python
try:
    load_model()

except:
    print("Model Load Failed")
```

---

## Data Conversion

```python
try:
    value = float(data)

except ValueError:
    value = 0
```

Very common in data cleaning.

---

# Common Beginner Mistakes

## Mistake 1

Using Bare except

Bad:

```python
except:
    print("Error")
```

Better:

```python
except ValueError:
    print("Invalid Value")
```

---

## Mistake 2

Putting Everything Inside try

Bad:

```python
try:
    entire_program()
```

Only place risky code inside try.

---

## Mistake 3

Ignoring Error Details

Bad:

```python
except:
    pass
```

This hides important bugs.

---

## Mistake 4

Confusing Errors and Exceptions

```text
Syntax Error
```

cannot be handled using try-except.

Example:

```python
if True
    print("Hello")
```

This fails before execution starts.

---

# Practice Questions

### Q1

Take two numbers and handle division by zero.

---

### Q2

Take integer input and handle invalid values.

---

### Q3

Open a file safely using try-except.

---

### Q4

Access a list index and handle IndexError.

---

### Q5

Access a dictionary key and handle KeyError.

---

### Q6

Use try-except-else.

---

### Q7

Use try-except-finally.

---

# Quick Revision

* Exception = Runtime error.
* `try` contains risky code.
* `except` handles errors.
* `else` runs when no error occurs.
* `finally` always runs.
* `raise` creates exceptions manually.
* Handle specific exceptions whenever possible.

---

# Importance for Machine Learning

| Concept             | Importance |
| ------------------- | ---------- |
| try-except          | ⭐⭐⭐⭐⭐      |
| Specific Exceptions | ⭐⭐⭐⭐⭐      |
| Exception as e      | ⭐⭐⭐⭐       |
| finally             | ⭐⭐⭐        |
| raise               | ⭐⭐⭐        |
| else                | ⭐⭐         |

Exception Handling is heavily used in Data Cleaning, Dataset Loading, Model Training, APIs, Automation, and Production ML Systems because real-world data is often messy and unpredictable.

---

# Summary

Exception Handling allows programs to deal with runtime errors gracefully instead of crashing. Python provides `try`, `except`, `else`, `finally`, and `raise` to manage exceptions effectively. Proper exception handling improves program reliability and is essential in Machine Learning, Data Analysis, and Software Development.
