# Python Fundamentals - Sets

## What is a Set?

A Set is an unordered collection of unique values.

The most important property of a set is:

```text
No Duplicate Values Allowed
```

Example:

```python
nums = {1, 2, 3, 3, 4, 4}

print(nums)
```

Output:

```text
{1, 2, 3, 4}
```

Duplicate values are automatically removed.

---

# Why Do We Need Sets?

Suppose we have a list of emails:

```python
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com"
]
```

Notice:

```text
a@gmail.com
```

appears twice.

If we only want unique emails:

```python
unique_emails = set(emails)

print(unique_emails)
```

Output:

```text
{
    'a@gmail.com',
    'b@gmail.com',
    'c@gmail.com'
}
```

Sets are commonly used for:

* Removing duplicates
* Fast lookup
* Finding common elements
* Data cleaning

---

# Real-Life Examples

### Unique Student IDs

```python
student_ids = {101, 102, 103}
```

---

### Unique Categories

```python
categories = {
    "Dog",
    "Cat",
    "Bird"
}
```

---

### Unique Email Addresses

```python
emails = {
    "a@gmail.com",
    "b@gmail.com"
}
```

---

# Creating a Set

## Syntax

```python
set_name = {value1, value2, value3}
```

Example:

```python
fruits = {
    "Apple",
    "Banana",
    "Mango"
}
```

---

# Empty Set

Wrong:

```python
s = {}
```

This creates a dictionary.

---

Correct:

```python
s = set()
```

Output:

```text
set()
```

---

# Set Properties

## 1. No Duplicates

```python
nums = {10, 10, 10, 20}

print(nums)
```

Output:

```text
{10, 20}
```

---

## 2. Unordered

```python
nums = {10, 20, 30}
```

Python does not guarantee:

```text
10
20
30
```

Order may vary.

---

## 3. Mutable

You can add or remove elements.

```python
nums = {1, 2, 3}

nums.add(4)
```

Valid.

---

## 4. No Indexing

Wrong:

```python
nums = {10, 20, 30}

print(nums[0])
```

Output:

```text
TypeError
```

Sets do not support indexing.

---

# Why No Indexing?

Lists store elements at positions:

```text
Value : 10 20 30
Index : 0  1  2
```

Sets do not maintain positions.

They are optimized for fast searching.

---

# Adding Elements

## add()

```python
nums = {1, 2, 3}

nums.add(4)

print(nums)
```

Output:

```text
{1, 2, 3, 4}
```

---

Adding a duplicate:

```python
nums.add(4)

print(nums)
```

Output:

```text
{1, 2, 3, 4}
```

Nothing changes.

---

# How Duplicate Checking Works

When an element is inserted:

```python
nums.add(10)
```

Python immediately checks:

```text
Does 10 already exist?
```

If yes:

```text
Ignore
```

If no:

```text
Insert
```

Duplicate checking happens during insertion.

Python does not scan the entire set every time.

Internally, sets use a hash table for fast lookup.

---

# Removing Elements

## remove()

```python
nums = {1, 2, 3}

nums.remove(2)

print(nums)
```

Output:

```text
{1, 3}
```

---

Problem:

```python
nums.remove(10)
```

Output:

```text
KeyError
```

because 10 doesn't exist.

---

## discard()

Safer version.

```python
nums.discard(10)
```

No error.

---

# Iterating Through a Set

Even though sets don't support indexing, they are iterable.

```python
nums = {10, 20, 30}

for num in nums:
    print(num)
```

Output:

```text
10
20
30
```

Order may vary.

---

# Membership Testing

One of the biggest advantages of sets.

```python
nums = {10, 20, 30}

print(20 in nums)
```

Output:

```text
True
```

---

```python
print(50 in nums)
```

Output:

```text
False
```

Membership checking is usually very fast.

---

# Set Length

Use `len()`.

```python
nums = {10, 20, 30}

print(len(nums))
```

Output:

```text
3
```

---

# Set Operations

These are the most powerful features of sets.

Suppose:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

---

## Union

All unique elements.

```python
print(A | B)
```

Output:

```text
{1, 2, 3, 4, 5}
```

---

Equivalent:

```python
print(A.union(B))
```

---

## Intersection

Common elements.

```python
print(A & B)
```

Output:

```text
{3}
```

---

Equivalent:

```python
print(A.intersection(B))
```

---

## Difference

Elements in A but not B.

```python
print(A - B)
```

Output:

```text
{1, 2}
```

---

Equivalent:

```python
print(A.difference(B))
```

---

## Symmetric Difference

Elements present in either set but not both.

```python
print(A ^ B)
```

Output:

```text
{1, 2, 4, 5}
```

---

# Set of Tuples

Sets cannot store lists because lists are mutable.

Wrong:

```python
s = {
    [1, 2],
    [3, 4]
}
```

Output:

```text
TypeError
```

---

Correct:

```python
students = {
    (101, "Jai"),
    (102, "Rahul"),
    (103, "Jai")
}
```

Output:

```text
{
    (101, "Jai"),
    (102, "Rahul"),
    (103, "Jai")
}
```

Notice:

```text
Jai appears twice
```

but data is not lost because the tuples are different.

---

# Common Uses in Machine Learning

## Remove Duplicates

```python
unique_names = set(names)
```

---

## Unique Categories

```python
categories = set(labels)
```

---

## Fast Lookup

```python
if email in email_set:
    ...
```

---

## Find Common Users

```python
common_users = users_a & users_b
```

---

## Data Cleaning

```python
unique_values = set(data)
```

---

# Common Beginner Mistakes

## Mistake 1

Using Indexing

Wrong:

```python
nums[0]
```

Sets don't support indexing.

---

## Mistake 2

Creating Empty Set Incorrectly

Wrong:

```python
s = {}
```

Creates dictionary.

Correct:

```python
s = set()
```

---

## Mistake 3

Expecting Order

Wrong:

```text
Set always prints in insertion order
```

Never rely on set ordering.

---

## Mistake 4

Trying to Store Lists

Wrong:

```python
{
    [1, 2]
}
```

Use tuples instead.

---

# Practice Questions

### Q1

Create a set containing 5 numbers.

---

### Q2

Add a new number.

---

### Q3

Remove a number.

---

### Q4

Check whether a number exists.

---

### Q5

Remove duplicates from a list using a set.

---

### Q6

Find union of two sets.

---

### Q7

Find intersection of two sets.

---

### Q8

Find difference of two sets.

---

# Quick Revision

* Set = Collection of unique values.
* Duplicate values are automatically removed.
* Sets are unordered.
* Sets are mutable.
* Sets do not support indexing.
* `add()` inserts elements.
* `remove()` removes elements.
* `discard()` removes safely.
* `in` performs fast membership testing.
* Union, Intersection, and Difference are core operations.

---

# Importance for Machine Learning

| Concept            | Importance |
| ------------------ | ---------- |
| Duplicate Removal  | ⭐⭐⭐⭐⭐      |
| Membership Testing | ⭐⭐⭐⭐⭐      |
| Union              | ⭐⭐⭐        |
| Intersection       | ⭐⭐⭐⭐       |
| Difference         | ⭐⭐⭐        |
| Set Conversion     | ⭐⭐⭐⭐⭐      |

Sets are widely used in Data Cleaning, Feature Engineering, NLP, Recommendation Systems, and Data Analysis because of their ability to store unique values and perform fast lookups.

---

# Summary

A Set is an unordered collection of unique values. It automatically removes duplicates and provides very fast membership checking through hashing. Sets are commonly used in Machine Learning and Data Analysis for duplicate removal, fast lookup operations, and set-based comparisons such as union and intersection.
