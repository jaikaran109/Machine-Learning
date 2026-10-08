# Python Fundamentals - Dictionaries

## What is a Dictionary?

A dictionary is a collection of data stored as **Key-Value Pairs**.

Think of it as:

```text
Key  → Value
```

Example:

```python
student = {
    "name": "Jai",
    "age": 20,
    "cgpa": 8.5
}
```

Here:

```text
"name" → "Jai"
"age"  → 20
"cgpa" → 8.5
```

---

## Why Do We Need Dictionaries?

Suppose we want to store information about a student.

Using a list:

```python
student = ["Jai", 20, 8.5]
```

Problem:

```text
What does 20 represent?
Age?
Marks?
Roll Number?
```

Not clear.

Using a dictionary:

```python
student = {
    "name": "Jai",
    "age": 20,
    "cgpa": 8.5
}
```

Now everything is meaningful.

---

# Real-Life Examples

### Student Record

```python
student = {
    "name": "Jai",
    "age": 20
}
```

---

### Employee Data

```python
employee = {
    "id": 101,
    "salary": 50000
}
```

---

### User Profile

```python
user = {
    "username": "jai123",
    "followers": 500
}
```

---

### ML Dataset Row

```python
person = {
    "age": 25,
    "salary": 45000,
    "purchased": 1
}
```

---

# Creating a Dictionary

## Syntax

```python
dictionary_name = {
    key1: value1,
    key2: value2
}
```

Example:

```python
student = {
    "name": "Jai",
    "age": 20
}
```

---

# Dictionary Visualization

```python
student = {
    "name": "Jai",
    "age": 20
}
```

Representation:

```text
"name" → "Jai"
"age"  → 20
```

Unlike lists, dictionaries do NOT use numeric indexes.

They use keys.

---

# Accessing Values

Use the key.

```python
student = {
    "name": "Jai",
    "age": 20
}

print(student["name"])
```

Output:

```text
Jai
```

---

```python
print(student["age"])
```

Output:

```text
20
```

---

# Why Not Use Indexes?

Lists:

```python
student = ["Jai", 20]
```

Access:

```python
student[0]
```

Not meaningful.

---

Dictionaries:

```python
student["name"]
```

Very readable.

---

# Modifying Values

```python
student = {
    "name": "Jai",
    "age": 20
}

student["age"] = 21

print(student)
```

Output:

```text
{'name': 'Jai', 'age': 21}
```

---

# Adding New Key-Value Pairs

```python
student = {
    "name": "Jai"
}

student["cgpa"] = 8.5

print(student)
```

Output:

```text
{'name': 'Jai', 'cgpa': 8.5}
```

---

# Removing Elements

## pop()

```python
student = {
    "name": "Jai",
    "age": 20
}

student.pop("age")

print(student)
```

Output:

```text
{'name': 'Jai'}
```

---

## del

```python
del student["name"]
```

Deletes the key-value pair.

---

# Dictionary Length

Use `len()`.

```python
student = {
    "name": "Jai",
    "age": 20
}

print(len(student))
```

Output:

```text
2
```

---

# Checking Keys

```python
student = {
    "name": "Jai",
    "age": 20
}

print("name" in student)
```

Output:

```text
True
```

---

```python
print("cgpa" in student)
```

Output:

```text
False
```

---

# get() Method

Safer way to access values.

Example:

```python
student = {
    "name": "Jai"
}

print(student.get("name"))
```

Output:

```text
Jai
```

---

Problem:

```python
print(student["age"])
```

Output:

```text
KeyError
```

---

Better:

```python
print(student.get("age"))
```

Output:

```text
None
```

No error.

---

# Traversing Dictionaries

## Loop Through Keys

```python
student = {
    "name": "Jai",
    "age": 20
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

---

# Loop Through Values

```python
for value in student.values():
    print(value)
```

Output:

```text
Jai
20
```

---

# Loop Through Both

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Jai
age 20
```

---

# Useful Dictionary Methods

## keys()

```python
print(student.keys())
```

Output:

```text
dict_keys(['name', 'age'])
```

---

## values()

```python
print(student.values())
```

Output:

```text
dict_values(['Jai', 20])
```

---

## items()

```python
print(student.items())
```

Output:

```text
dict_items([('name', 'Jai'), ('age', 20)])
```

---

# Nested Dictionaries

Dictionary inside dictionary.

```python
students = {
    "student1": {
        "name": "Jai",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}
```

Access:

```python
print(students["student1"]["name"])
```

Output:

```text
Jai
```

---

# Why Dictionaries are Important in Machine Learning

Most ML projects store data like:

```python
config = {
    "learning_rate": 0.01,
    "epochs": 100,
    "batch_size": 32
}
```

---

Model Metrics:

```python
metrics = {
    "accuracy": 95,
    "precision": 92
}
```

---

Dataset Records:

```python
person = {
    "age": 25,
    "salary": 50000
}
```

Dictionaries are everywhere in ML.

---

# Common Beginner Mistakes

## Mistake 1

Accessing Missing Key

```python
student["cgpa"]
```

Output:

```text
KeyError
```

Use:

```python
student.get("cgpa")
```

---

## Mistake 2

Duplicate Keys

```python
student = {
    "name": "Jai",
    "name": "Rahul"
}
```

Output:

```text
{'name': 'Rahul'}
```

Latest value replaces old value.

---

## Mistake 3

Confusing Keys and Values

Wrong:

```python
student["Jai"]
```

Correct:

```python
student["name"]
```

---

# Practice Questions

### Q1

Create a dictionary storing:

```text
Name
Age
City
```

Print all values.

---

### Q2

Add a new key called `cgpa`.

---

### Q3

Update age.

---

### Q4

Remove city.

---

### Q5

Print all keys.

---

### Q6

Print all values.

---

### Q7

Count how many key-value pairs exist.

---

# Quick Revision

* Dictionary = Key-Value pairs.
* Keys are unique.
* Values can repeat.
* Access using keys.
* Dictionaries are mutable.
* `get()` is safer than direct access.
* `keys()`, `values()`, `items()` are commonly used.
* Dictionaries are heavily used in ML projects.

---

# Importance for Machine Learning

| Concept             | Importance |
| ------------------- | ---------- |
| Accessing Values    | ⭐⭐⭐⭐⭐      |
| get()               | ⭐⭐⭐⭐⭐      |
| items()             | ⭐⭐⭐⭐⭐      |
| keys()              | ⭐⭐⭐⭐       |
| values()            | ⭐⭐⭐⭐       |
| Nested Dictionaries | ⭐⭐⭐⭐       |

Dictionaries are one of the most important Python data structures and are used extensively in Machine Learning, Data Analysis, APIs, and Backend Development.

---

# Summary

A dictionary is a mutable collection of key-value pairs. Unlike lists, dictionaries use meaningful keys instead of numeric indexes, making data easier to organize and access. They are heavily used in real-world applications and Machine Learning projects for storing configurations, datasets, model parameters, and results.
