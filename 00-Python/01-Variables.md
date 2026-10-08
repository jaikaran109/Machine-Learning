# Python Fundamentals - Variables

## What is a Variable?

A variable is a named storage location used to store data in memory.

Think of a variable as a labeled box.

```python
name = "Jai"
age = 20
```

Here:

* `name` stores `"Jai"`
* `age` stores `20`

Whenever we need these values, we can use the variable name instead of writing the actual value repeatedly.

```python
print(name)
print(age)
```

### Output

```text
Jai
20
```

---

## Why Do We Need Variables?

Without variables:

```python
print("Jai")
print("Jai")
print("Jai")
```

If the name changes, we must modify every occurrence.

With variables:

```python
name = "Jai"

print(name)
print(name)
print(name)
```

Now we only need to change the value once.

```python
name = "Rahul"
```

All references automatically use the new value.

---

## Variable Assignment

The `=` operator assigns a value to a variable.

```python
x = 10
```

Read it as:

> Store 10 inside variable x.

**NOT**

> x equals 10 (mathematical equality)

---

## Rules for Naming Variables

### Rule 1: Must Start with a Letter or Underscore

✅ Valid

```python
name = "Jai"
_age = 20
student1 = "Aman"
```

❌ Invalid

```python
1name = "Jai"
```

Variables cannot start with a number.

---

### Rule 2: Cannot Contain Spaces

❌ Invalid

```python
first name = "Jai"
```

✅ Valid

```python
first_name = "Jai"
```

---

### Rule 3: Only Letters, Numbers, and Underscores Allowed

✅ Valid

```python
student_name = "Jai"
student1 = "Jai"
```

❌ Invalid

```python
student-name = "Jai"
student@name = "Jai"
```

---

### Rule 4: Variable Names are Case Sensitive

```python
name = "Jai"
Name = "Rahul"
```

These are different variables.

```python
print(name)
print(Name)
```

### Output

```text
Jai
Rahul
```

---

### Rule 5: Reserved Keywords Cannot Be Used

❌ Invalid

```python
if = 10
for = 20
class = 30
```

These words already have special meanings in Python.

---

## Best Practices

### Use Meaningful Names

❌ Poor

```python
x = "Jai"
```

✅ Better

```python
student_name = "Jai"
```

---

### Use Snake Case

Python convention:

```python
student_name = "Jai"
total_marks = 500
```

Avoid:

```python
studentName
StudentName
```

for beginner Python projects.

---

## Reassigning Variables

Variables can store new values.

```python
age = 20
age = 21

print(age)
```

### Output

```text
21
```

The old value is replaced.

---

## Multiple Assignments

### Assign Multiple Variables

```python
name = "Jai"
age = 20
city = "Kanpur"
```

---

### Assign in One Line

```python
name, age, city = "Jai", 20, "Kanpur"
```

---

### Same Value to Multiple Variables

```python
a = b = c = 10
```

```python
print(a)
print(b)
print(c)
```

### Output

```text
10
10
10
```

---

## Dynamic Typing

Python automatically determines the data type.

```python
x = 10
print(type(x))
```

### Output

```text
<class 'int'>
```

---

```python
x = "Jai"
print(type(x))
```

### Output

```text
<class 'str'>
```

The same variable can store different types at different times.

---

## Real Life Example

Imagine a college management system.

```python
student_name = "Jai"
roll_number = 101
cgpa = 8.5
```

Instead of remembering these values everywhere, we store them in variables.

```python
print(student_name)
print(roll_number)
print(cgpa)
```

---

## Common Beginner Mistakes

### Mistake 1

```python
print(Name)
```

when variable is

```python
name = "Jai"
```

Python sees them as different variables.

---

### Mistake 2

```python
student name = "Jai"
```

Spaces are not allowed.

---

### Mistake 3

```python
1student = "Jai"
```

Variable names cannot start with numbers.

---

## Practice Questions

### Q1

Create variables:

```text
Name = Jai
Age = 20
City = Kanpur
```

Print all values.

---

### Q2

Store your CGPA in a variable and print it.

---

### Q3

Create a variable called `college_name` and assign your college name.

---

### Q4

Create three variables in one line and print them.

---

## Quick Revision

* Variables store data.
* `=` is used for assignment.
* Variable names cannot start with numbers.
* Spaces are not allowed.
* Python is case-sensitive.
* Use meaningful names.
* Python automatically determines data types.
* Variables can be reassigned.

---

## Summary

A variable is a named container that stores data in memory. Variables make programs flexible, reusable, and easier to maintain by allowing values to be stored and accessed through meaningful names rather than hardcoded values.
