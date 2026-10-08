# Python Fundamentals - Strings

## What is a String?

A string is a sequence of characters used to store text.

Examples:

```python
name = "Jai"
city = "Kanpur"
message = "Hello World"
```

Everything inside quotes is a string.

---

# Why Do We Need Strings?

Imagine building:

* WhatsApp
* Instagram
* Gmail
* ChatGPT

All of these applications deal with text.

Examples:

```text
User Name
Email Address
Password
Message
Comment
Review
```

All of these are strings.

---

# Creating Strings

## Double Quotes

```python
name = "Jai"
```

---

## Single Quotes

```python
name = 'Jai'
```

Both are valid.

---

# String Visualization

```python
name = "Jai"
```

Memory Representation:

```text
J   a   i
0   1   2
```

Every character has an index.

---

# Accessing Characters

## Positive Indexing

```python
name = "Jai"

print(name[0])
```

Output:

```text
J
```

---

```python
print(name[1])
```

Output:

```text
a
```

---

```python
print(name[2])
```

Output:

```text
i
```

---

# Negative Indexing

Python can count from the end.

```text
J   a   i
-3 -2 -1
```

Example:

```python
name = "Jai"

print(name[-1])
```

Output:

```text
i
```

---

# String Length

Use `len()`.

```python
name = "Jai"

print(len(name))
```

Output:

```text
3
```

---

# String Traversal

Loop through every character.

```python
name = "Jai"

for ch in name:
    print(ch)
```

Output:

```text
J
a
i
```

---

# String Concatenation

Joining strings together.

```python
first = "Jai"
last = "Karan"

print(first + " " + last)
```

Output:

```text
Jai Karan
```

---

# String Repetition

```python
print("Hi" * 3)
```

Output:

```text
HiHiHi
```

---

# String Slicing

One of the most important concepts.

## Syntax

```python
string[start:end]
```

Python takes:

```text
start → included
end   → excluded
```

---

Example:

```python
name = "JaiKaran"

print(name[0:3])
```

Output:

```text
Jai
```

---

Visualization:

```text
J a i K a r a n
0 1 2 3 4 5 6 7
```

Python takes:

```text
0
1
2
```

Not 3.

---

## Slice From Beginning

```python
name[:3]
```

Output:

```text
Jai
```

---

## Slice Till End

```python
name[3:]
```

Output:

```text
Karan
```

---

## Entire String

```python
name[:]
```

Output:

```text
JaiKaran
```

---

# String Immutability

Strings cannot be modified.

Example:

```python
name = "Jai"

name[0] = "R"
```

Output:

```text
TypeError
```

---

Why?

Strings are immutable.

---

Correct Method:

```python
name = "Rai"
```

Create a new string instead.

---

# Important String Methods

---

## upper()

Converts to uppercase.

```python
name = "jai"

print(name.upper())
```

Output:

```text
JAI
```

---

## lower()

Converts to lowercase.

```python
name = "JAI"

print(name.lower())
```

Output:

```text
jai
```

---

## capitalize()

```python
name = "jai"

print(name.capitalize())
```

Output:

```text
Jai
```

---

## strip()

Removes spaces from both ends.

```python
name = "   Jai   "

print(name.strip())
```

Output:

```text
Jai
```

---

## replace()

Replace text.

```python
message = "Hello World"

print(message.replace("World", "Python"))
```

Output:

```text
Hello Python
```

---

## count()

Counts occurrences.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## find()

Returns first position.

```python
text = "banana"

print(text.find("n"))
```

Output:

```text
2
```

---

# Membership Operators

Check whether a substring exists.

```python
name = "JaiKaran"

print("Jai" in name)
```

Output:

```text
True
```

---

```python
print("Rahul" in name)
```

Output:

```text
False
```

---

# Splitting Strings

Very important.

```python
text = "Python Java C++"

words = text.split()

print(words)
```

Output:

```text
['Python', 'Java', 'C++']
```

---

# Joining Strings

```python
words = ["Python", "Java", "C++"]

print("-".join(words))
```

Output:

```text
Python-Java-C++
```

---

# f-Strings

Modern way of formatting strings.

```python
name = "Jai"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Jai and I am 20 years old.
```

---

# Common Uses in Machine Learning

## Cleaning Text

```python
review = review.lower()
```

---

## Removing Spaces

```python
review = review.strip()
```

---

## Replacing Characters

```python
text = text.replace(",", "")
```

---

## Tokenization

```python
words = sentence.split()
```

---

## Filtering Data

```python
if "spam" in email:
    ...
```

---

# Common Beginner Mistakes

## Mistake 1

Forgetting Quotes

Wrong:

```python
name = Jai
```

Correct:

```python
name = "Jai"
```

---

## Mistake 2

Invalid Index

```python
name = "Jai"

print(name[10])
```

Output:

```text
IndexError
```

---

## Mistake 3

Trying to Modify String

Wrong:

```python
name[0] = "R"
```

Strings are immutable.

---

# Practice Questions

### Q1

Take a name and print its length.

---

### Q2

Print first and last character of a string.

---

### Q3

Convert a string to uppercase.

---

### Q4

Count vowels in a string.

---

### Q5

Reverse a string.

Example:

```text
Jai → iaJ
```

---

### Q6

Check whether a string is a palindrome.

Example:

```text
madam → True
level → True
hello → False
```

---

### Q7

Count how many times a character appears in a string.

---

# Quick Revision

* String = Sequence of characters.
* Indexing starts from 0.
* Negative indexing starts from the end.
* `len()` gives length.
* Strings are immutable.
* Slicing extracts parts of a string.
* `upper()`, `lower()`, `replace()`, `split()` are commonly used.
* f-strings are the preferred formatting method.

---

# Importance for Machine Learning

| Concept   | Importance |
| --------- | ---------- |
| Indexing  | ⭐⭐⭐⭐⭐      |
| Slicing   | ⭐⭐⭐⭐⭐      |
| Traversal | ⭐⭐⭐⭐⭐      |
| split()   | ⭐⭐⭐⭐⭐      |
| replace() | ⭐⭐⭐⭐⭐      |
| lower()   | ⭐⭐⭐⭐⭐      |
| strip()   | ⭐⭐⭐⭐⭐      |
| f-Strings | ⭐⭐⭐⭐       |

Strings are heavily used in NLP, Data Cleaning, Data Preprocessing, Chatbots, Search Engines, and Text Analytics.

---

# Summary

A string is a sequence of characters used to store text. Strings support indexing, slicing, traversal, and many built-in methods for text processing. They are one of the most important data types in Python and are extensively used in Machine Learning, especially in text preprocessing and Natural Language Processing (NLP).
