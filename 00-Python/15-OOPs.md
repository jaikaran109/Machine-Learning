# Python Fundamentals - Object-Oriented Programming (OOP)

## Why Was OOP Invented?

Imagine you're building a Student Management System.

Without OOP:

```python
name1 = "Jai"
age1 = 20
cgpa1 = 8.5

name2 = "Rahul"
age2 = 21
cgpa2 = 8.0
```

Now imagine:

```text
100 Students
1000 Students
10000 Students
```

Managing separate variables becomes impossible.

---

## The Real Problem

Notice:

```text
Student 1
    Name
    Age
    CGPA

Student 2
    Name
    Age
    CGPA
```

The structure repeats.

Programmers thought:

> Can we create a blueprint for students?

This blueprint is called a **Class**.

---

# Real-Life Analogy

Think of a blueprint for a house.

```text
Blueprint
    ↓
House 1

Blueprint
    ↓
House 2

Blueprint
    ↓
House 3
```

The blueprint is the same.

The houses are different.

---

In OOP:

```text
Class
    ↓
Object 1

Class
    ↓
Object 2

Class
    ↓
Object 3
```

---

# What is a Class?

A Class is a blueprint used to create objects.

Example:

```python
class Student:
    pass
```

This class currently does nothing.

It only defines a new type called:

```text
Student
```

---

# What is an Object?

An Object is an instance of a class.

Example:

```python
class Student:
    pass

s1 = Student()
s2 = Student()
```

Here:

```text
Student → Class

s1 → Object

s2 → Object
```

---

# Visual Representation

```text
Class Student
       ↓
 ┌──────────┐
 │ Blueprint│
 └──────────┘

      ↓

s1 = Student()
s2 = Student()
s3 = Student()
```

---

# Attributes

Attributes are variables belonging to an object.

Example:

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

---

Create Objects:

```python
s1 = Student("Jai", 20)
s2 = Student("Rahul", 21)
```

Access:

```python
print(s1.name)
print(s1.age)
```

Output:

```text
Jai
20
```

---

# Understanding **init**()

This is the most important OOP concept.

```python
def __init__(...)
```

is called a constructor.

It runs automatically whenever an object is created.

---

Example:

```python
class Student:

    def __init__(self):
        print("Object Created")
```

Now:

```python
s1 = Student()
```

Output:

```text
Object Created
```

---

# What is self?

This confuses almost everyone.

Suppose:

```python
s1 = Student("Jai", 20)
```

Python internally does:

```python
Student.__init__(s1, "Jai", 20)
```

So:

```python
self
```

refers to the current object.

---

For:

```python
s1 = Student(...)
```

```text
self = s1
```

---

For:

```python
s2 = Student(...)
```

```text
self = s2
```

---

# Methods

Functions inside a class are called methods.

Example:

```python
class Student:

    def greet(self):
        print("Hello")
```

---

Usage:

```python
s1 = Student()

s1.greet()
```

Output:

```text
Hello
```

---

# Complete Example

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print(self.name)
        print(self.age)
```

---

Create Object:

```python
s1 = Student("Jai", 20)

s1.display()
```

Output:

```text
Jai
20
```

---

# Why OOP is Useful

Without OOP:

```python
name1
age1

name2
age2

name3
age3
```

Messy.

---

With OOP:

```python
student1.name
student1.age

student2.name
student2.age
```

Clean and organized.

---

# Encapsulation

Encapsulation means:

```text
Data + Methods
Together
```

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Both data and behavior belong to the object.

---

# Inheritance

Inheritance allows one class to reuse another class.

---

Example:

```python
class Person:

    def greet(self):
        print("Hello")
```

---

```python
class Student(Person):
    pass
```

Now:

```python
s = Student()

s.greet()
```

Output:

```text
Hello
```

Student inherited from Person.

---

# Real-Life Analogy

```text
Animal
   ↓

Dog
Cat
Lion
```

All animals can:

```text
Eat
Sleep
Move
```

Inheritance avoids rewriting code.

---

# Polymorphism

Same method.

Different behavior.

---

Example:

```python
class Dog:

    def sound(self):
        print("Bark")
```

---

```python
class Cat:

    def sound(self):
        print("Meow")
```

---

Usage:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

Same method name.

Different behavior.

---

# Abstraction

Hide unnecessary details.

Example:

```python
car.start()
```

You don't know:

```text
Fuel Injection
Engine Process
Battery Logic
```

You only know:

```python
car.start()
```

This is abstraction.

---

# Four Pillars of OOP

```text
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
```

Memorize these.

Interviewers love asking them.

---

# OOP in Machine Learning

Almost every ML library uses OOP.

Example:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

Notice:

```python
LinearRegression()
```

creates an object.

---

Training:

```python
model.fit(X, y)
```

---

Prediction:

```python
model.predict(X)
```

---

Everything revolves around objects.

---

# Common Beginner Mistakes

## Mistake 1

Forgetting self

Wrong:

```python
class Student:

    def display():
        pass
```

Correct:

```python
class Student:

    def display(self):
        pass
```

---

## Mistake 2

Using Attribute Without self

Wrong:

```python
name = name
```

Correct:

```python
self.name = name
```

---

## Mistake 3

Confusing Class and Object

```text
Student
```

Class

---

```text
s1 = Student()
```

Object

---

# Practice Questions

### Q1

Create a Student class with name and age.

---

### Q2

Create a Car class with brand and model.

---

### Q3

Create a BankAccount class with deposit method.

---

### Q4

Create a Person class and Student class using inheritance.

---

### Q5

Create Dog and Cat classes demonstrating polymorphism.

---

# Quick Revision

* Class = Blueprint.
* Object = Instance of a class.
* Attribute = Variable inside object.
* Method = Function inside class.
* self = Current object.
* **init**() = Constructor.
* Inheritance = Reuse code.
* Polymorphism = Same method, different behavior.
* Abstraction = Hide complexity.
* Encapsulation = Data + Methods together.

---

# Importance for Machine Learning

| Concept       | Importance |
| ------------- | ---------- |
| Class         | ⭐⭐⭐⭐⭐      |
| Object        | ⭐⭐⭐⭐⭐      |
| self          | ⭐⭐⭐⭐⭐      |
| **init**()    | ⭐⭐⭐⭐⭐      |
| Methods       | ⭐⭐⭐⭐⭐      |
| Inheritance   | ⭐⭐⭐⭐       |
| Polymorphism  | ⭐⭐⭐        |
| Abstraction   | ⭐⭐⭐        |
| Encapsulation | ⭐⭐⭐⭐       |

Every major ML library such as NumPy, Pandas, Scikit-Learn, TensorFlow, and PyTorch is heavily based on OOP concepts.

---

# Summary

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using classes and objects. A class acts as a blueprint, while objects represent real-world entities created from that blueprint. OOP improves code organization, reusability, and maintainability through concepts such as encapsulation, inheritance, polymorphism, and abstraction. It is one of the most important concepts in Python and forms the foundation of modern Machine Learning libraries.
