# Python Fundamentals - Input and Output

## What is Input and Output?

Every program interacts with users in two ways:

1. **Input** → Taking data from the user.
2. **Output** → Displaying data to the user.

Think of it like a conversation.

```text
User → Input → Program → Output → User
```

### Real-Life Example

ATM Machine:

```text
Enter PIN      → Input
Check Balance  → Output
```

Instagram:

```text
Enter Username → Input
Show Profile   → Output
```

Calculator:

```text
Enter Numbers  → Input
Show Result    → Output
```

---

# Output in Python

Output means displaying information on the screen.

Python uses the `print()` function for output.

## Basic Syntax

```python
print(value)
```

Example:

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

## Printing Numbers

```python
print(10)
print(100)
```

Output:

```text
10
100
```

---

## Printing Variables

```python
name = "Jai"

print(name)
```

Output:

```text
Jai
```

---

## Printing Multiple Values

```python
name = "Jai"
age = 20

print(name, age)
```

Output:

```text
Jai 20
```

Python automatically adds a space between values.

---

## Printing Text and Variables Together

```python
name = "Jai"

print("My name is", name)
```

Output:

```text
My name is Jai
```

---

## Using f-Strings (Recommended)

Modern Python uses f-strings.

Syntax:

```python
f"Text {variable}"
```

Example:

```python
name = "Jai"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Jai and I am 20 years old.
```

### Why Use f-Strings?

* Cleaner
* More readable
* Most commonly used in real projects

---

# Special Characters in Output

## New Line (`\n`)

Moves output to the next line.

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

## Tab (`\t`)

Adds horizontal space.

```python
print("Name\tAge")
```

Output:

```text
Name    Age
```

---

## Printing Quotes

```python
print("My name is \"Jai\"")
```

Output:

```text
My name is "Jai"
```

---

# Input in Python

Input means taking data from the user.

Python uses the `input()` function.

## Basic Syntax

```python
input("Message")
```

Example:

```python
name = input("Enter your name: ")
```

Program:

```text
Enter your name:
```

If user enters:

```text
Jai
```

Then:

```python
name = "Jai"
```

---

## Displaying User Input

```python
name = input("Enter your name: ")

print(name)
```

Input:

```text
Jai
```

Output:

```text
Jai
```

---

## Example: Greeting Program

```python
name = input("Enter your name: ")

print(f"Welcome {name}")
```

Input:

```text
Jai
```

Output:

```text
Welcome Jai
```

---

# Important Rule About input()

Everything received from `input()` is stored as a string.

Example:

```python
age = input("Enter age: ")

print(type(age))
```

Input:

```text
20
```

Output:

```text
<class 'str'>
```

Even though the user entered a number, Python stores it as a string.

---

# Converting Input to Integer

Suppose:

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
```

Input:

```text
10
20
```

Output:

```text
1020
```

Why?

Because both values are strings.

```python
"10" + "20"
```

becomes:

```text
1020
```

This is called string concatenation.

---

## Correct Method

Use `int()`.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Input:

```text
10
20
```

Output:

```text
30
```

---

# Converting Input to Float

```python
cgpa = float(input("Enter CGPA: "))

print(cgpa)
```

Input:

```text
8.5
```

Output:

```text
8.5
```

---

# Multiple Inputs in One Line

Suppose user enters:

```text
10 20
```

Use:

```python
a, b = map(int, input().split())

print(a)
print(b)
```

Output:

```text
10
20
```

---

## Understanding the Code

### Step 1

Input:

```text
10 20
```

---

### Step 2

```python
input().split()
```

Result:

```python
["10", "20"]
```

---

### Step 3

```python
map(int, ...)
```

Result:

```python
[10, 20]
```

---

### Step 4

```python
a, b = ...
```

Assignment:

```python
a = 10
b = 20
```

---

# Common Input Patterns

## Taking Integer Input

```python
age = int(input("Enter age: "))
```

---

## Taking Float Input

```python
cgpa = float(input("Enter CGPA: "))
```

---

## Taking String Input

```python
name = input("Enter name: ")
```

---

## Taking Two Integers

```python
a, b = map(int, input().split())
```

---

## Taking List of Integers

Input:

```text
1 2 3 4 5
```

Code:

```python
numbers = list(map(int, input().split()))

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

# Real-Life Example: Student Registration

```python
name = input("Enter Name: ")
age = int(input("Enter Age: "))
cgpa = float(input("Enter CGPA: "))

print("\nStudent Details")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"CGPA : {cgpa}")
```

Input:

```text
Jai
20
8.5
```

Output:

```text
Student Details
Name : Jai
Age  : 20
CGPA : 8.5
```

<!-- If You want upto 2 decimal places--> 
cgpa = 8.56789

print(f"{cgpa:.2f}")


---

# Common Beginner Mistakes

## Mistake 1

```python
num = input()

print(num + 5)
```

Error because `num` is a string.

Correct:

```python
num = int(input())

print(num + 5)
```

---

## Mistake 2

```python
print("Age is " + 20)
```

Error because string and integer cannot be concatenated.

Correct:

```python
print("Age is", 20)
```

or

```python
print(f"Age is {20}")
```

---

## Mistake 3

```python
a, b = input().split()
```

Then using:

```python
print(a + b)
```

Input:

```text
10 20
```

Output:

```text
1020
```

Because both values are strings.

Use:

```python
a, b = map(int, input().split())
```

---

# Practice Questions

### Q1

Take a user's name and print:

```text
Welcome <name>
```

---

### Q2

Take two integers and print their sum.

---

### Q3

Take age as input and print:

```text
You are <age> years old.
```

---

### Q4

Take three integers and print their average.

---

### Q5

Take five integers in a single line and store them in a list.

---

# Quick Revision

* `print()` → Output
* `input()` → Input
* Input always returns a string.
* Use `int()` for integers.
* Use `float()` for decimals.
* Use f-strings for formatted output.
* Use `split()` to separate values.
* Use `map()` for multiple numeric inputs.

---

# Summary

Input and Output are the primary ways through which a program communicates with users. Python uses `input()` to receive data and `print()` to display data. Since `input()` always returns a string, type conversion functions such as `int()` and `float()` are often required to perform mathematical operations.
