# Python Fundamentals - File Handling

## What is File Handling?

File Handling is the process of reading data from files and writing data to files.

Without file handling, data exists only while the program is running.

Example:

```python
name = "Jai"
```

When the program stops:

```text
Data is lost
```

---

## Why Do We Need File Handling?

Imagine you are building:

* WhatsApp
* Instagram
* Banking System
* Student Management System

You need to save data permanently.

Examples:

```text
Messages
Photos
User Profiles
Marks
Reports
Logs
```

This data is stored in files or databases.

File Handling is the first step toward learning how data is stored permanently.

---

# Real-Life Example

Suppose a teacher wants to save marks.

Without files:

```python
marks = [90, 85, 78]
```

When the program closes:

```text
Marks disappear
```

---

With files:

```text
marks.txt
```

```text
90
85
78
```

Even after closing the program:

```text
Data remains saved
```

---

# Opening a File

Before reading or writing, Python must open the file.

## Syntax

```python
file = open("filename", "mode")
```

Example:

```python
file = open("students.txt", "r")
```

---

# File Modes

| Mode | Meaning      |
| ---- | ------------ |
| r    | Read         |
| w    | Write        |
| a    | Append       |
| x    | Create       |
| rb   | Read Binary  |
| wb   | Write Binary |

---

# Read Mode (r)

Used when we want to read existing data.

Suppose:

```text
students.txt
```

contains:

```text
Jai
Rahul
Aman
```

Code:

```python
file = open("students.txt", "r")

data = file.read()

print(data)

file.close()
```

Output:

```text
Jai
Rahul
Aman
```

---

# What is `read()`?

Reads the entire file.

```python
content = file.read()
```

Example:

```text
Hello World
```

becomes:

```python
"Hello World"
```

---

# Reading One Line

Use:

```python
file.readline()
```

Example:

```python
file = open("students.txt", "r")

print(file.readline())
```

Output:

```text
Jai
```

Only first line is read.

---

# Reading All Lines

Use:

```python
file.readlines()
```

Example:

```python
file = open("students.txt", "r")

print(file.readlines())
```

Output:

```python
['Jai\n', 'Rahul\n', 'Aman\n']
```

Returns a list.

---

# Write Mode (w)

Used to write data into a file.

Example:

```python
file = open("notes.txt", "w")

file.write("Hello Python")

file.close()
```

File Content:

```text
Hello Python
```

---

# Important Warning

Write mode deletes old data.

Suppose:

```text
notes.txt
```

contains:

```text
Old Data
```

Now:

```python
file = open("notes.txt", "w")

file.write("New Data")
```

File becomes:

```text
New Data
```

Old data is gone.

---

# Append Mode (a)

Used to add data without deleting existing data.

Example:

```python
file = open("notes.txt", "a")

file.write("\nNew Line")

file.close()
```

File:

```text
Old Data
New Line
```

Existing content remains.

---

# Create Mode (x)

Creates a new file.

```python
file = open("newfile.txt", "x")
```

If file already exists:

```text
FileExistsError
```

---

# Closing Files

Always close files after use.

```python
file.close()
```

Why?

Because:

```text
Operating System resources are released.
```

---

# Better Way: with Statement

Instead of:

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

Use:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Python automatically closes the file.

Recommended approach.

---

# Writing Multiple Lines

```python
with open("students.txt", "w") as file:

    file.write("Jai\n")
    file.write("Rahul\n")
    file.write("Aman\n")
```

Output File:

```text
Jai
Rahul
Aman
```

---

# Loop Through a File

```python
with open("students.txt", "r") as file:

    for line in file:
        print(line)
```

Output:

```text
Jai
Rahul
Aman
```

Very useful for large files.

---

# Common Uses in Machine Learning

## Reading CSV Files

Before Pandas:

```python
with open("data.csv", "r") as file:
    data = file.read()
```

---

## Saving Results

```python
with open("results.txt", "w") as file:
    file.write("Accuracy = 95%")
```

---

## Logging

```python
with open("log.txt", "a") as file:
    file.write("Model Trained\n")
```

---

## Storing Predictions

```python
with open("predictions.txt", "w") as file:
    file.write(str(predictions))
```

---

# Common Beginner Mistakes

## Mistake 1

Forgetting to Close File

Wrong:

```python
file = open("data.txt", "r")
```

Better:

```python
with open("data.txt", "r") as file:
```

---

## Mistake 2

Using Write Mode Accidentally

```python
open("notes.txt", "w")
```

Existing data gets deleted.

---

## Mistake 3

Reading Non-Existing File

```python
open("abc.txt", "r")
```

Output:

```text
FileNotFoundError
```

---

## Mistake 4

Forgetting Newline Character

```python
file.write("Jai")
file.write("Rahul")
```

Output:

```text
JaiRahul
```

Need:

```python
file.write("Jai\n")
file.write("Rahul\n")
```

---

# Practice Questions

### Q1

Create a file and write your name into it.

---

### Q2

Read data from a file and print it.

---

### Q3

Append a new line into a file.

---

### Q4

Count how many lines exist in a file.

---

### Q5

Count how many words exist in a file.

---

### Q6

Read a file and print each line separately.

---

### Q7

Store student names in a file and display them.

---

# Quick Revision

* `open()` opens a file.
* `r` → Read mode.
* `w` → Write mode.
* `a` → Append mode.
* `x` → Create mode.
* `read()` reads entire file.
* `readline()` reads one line.
* `readlines()` returns all lines.
* `close()` closes the file.
* `with open()` automatically closes files.

---

# Importance for Machine Learning

| Concept       | Importance |
| ------------- | ---------- |
| Reading Files | ⭐⭐⭐⭐⭐      |
| Writing Files | ⭐⭐⭐⭐       |
| Append Mode   | ⭐⭐⭐        |
| read()        | ⭐⭐⭐⭐⭐      |
| readline()    | ⭐⭐⭐        |
| with open()   | ⭐⭐⭐⭐⭐      |

File Handling is heavily used in Data Analysis, Machine Learning, Automation, Logging, and Software Development because data often comes from files and results frequently need to be stored.

---

# Summary

File Handling allows programs to store and retrieve data permanently using files. Python provides different modes such as read, write, append, and create for interacting with files. File handling is essential in Machine Learning for reading datasets, saving predictions, logging results, and processing large amounts of data.
