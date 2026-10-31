# DataFrames in Pandas

> **Phase 2: Data Analysis, Pandas**
> The table-like structure that holds almost all data you will work with in machine learning.

---

## 1. The Big Idea

A **DataFrame** is a **table in Python**: rows and columns, like an Excel sheet, but one you can filter, clean and calculate with using code.

**Analogy (a class register):**

| Register | DataFrame |
|---|---|
| One student's line | A **row** |
| One heading (Name, Age, Marks) | A **column** |
| The whole register | The **DataFrame** |
| The roll number on each line | The **index** |

**Pandas** is a Python **library** (a ready-made collection of code) for working with tables. It is built on NumPy.

```python
import pandas as pd      # "pd" is the standard short name
```

---

## 2. Key Terms in Plain Words

| Term | Meaning | Example |
|---|---|---|
| **DataFrame** | A 2D table with labeled rows and columns | The whole student table |
| **Series** | **One column** (or one row) of data, with an index | The `Marks` column |
| **Row** | One record | One student |
| **Column** | One property of every record (a feature) | `Marks` |
| **Index** | The labels of the rows. By default `0, 1, 2, ...` | Row `1` |
| **Label** | A name, such as `"Marks"` or a row's index value | `"Riya"` |
| **Position** | A number counting from 0, regardless of the labels | The 2nd row is position `1` |
| **dtype** | The type of data in a column | `int64` (whole numbers), `float64` (decimals), `object` (text) |
| **Attribute** | A stored fact about the object, written **without** brackets | `df.shape` |
| **Method** | An action the object performs, written **with** brackets | `df.head()` |

> In the newest pandas versions, text columns may display as `str` instead of `object`. They mean the same thing for you.

---

## 3. Creating a DataFrame

### Our example table

```python
import pandas as pd

data = {
    "Name":  ["Aman", "Riya", "Sam", "Neha"],
    "Age":   [20, 21, 19, 22],
    "City":  ["Delhi", "Mumbai", "Delhi", "Pune"],
    "Marks": [80, 75, 90, 85],
}
df = pd.DataFrame(data)
print(df)
```

```
   Name  Age    City  Marks
0  Aman   20   Delhi     80
1  Riya   21  Mumbai     75
2   Sam   19   Delhi     90
3  Neha   22    Pune     85
```

The left column `0 1 2 3` is the **index**, added automatically.

### Other ways to create one

| From | Code |
|---|---|
| **A dictionary** (above) | Keys become column names |
| **A list of rows** | `pd.DataFrame([["Aman", 20], ["Riya", 21]], columns=["Name", "Age"])` |
| **A NumPy array** | `pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=["a", "b"])` |
| **A CSV file** (the most common) | `pd.read_csv("file.csv")` |

### A Series on its own

```python
pd.Series([80, 75, 90], index=["Aman", "Riya", "Sam"])
```

```
Aman    80
Riya    75
Sam     90
dtype: int64
```

A DataFrame is a collection of Series (columns) that share the same index.

---

## 4. Looking at a DataFrame

| What | Code | Result for our table |
|---|---|---|
| **Shape** (rows, columns) | `df.shape` | `(4, 4)` |
| **Dimensions** | `df.ndim` | `2` |
| **Size** (total cells) | `df.size` | `16` |
| **Column names** | `df.columns` | `['Name', 'Age', 'City', 'Marks']` |
| **Row labels** | `df.index` | `RangeIndex(start=0, stop=4, step=1)` |
| **Data types** | `df.dtypes` | Name: text, Age: `int64`, City: text, Marks: `int64` |
| **First rows** | `df.head()` | The first 5 rows (default) |
| **Last rows** | `df.tail()` | The last 5 rows |
| **Random rows** | `df.sample(2)` | 2 random rows |
| **Overview** | `df.info()` | Types and non-missing counts |
| **Summary numbers** | `df.describe()` | Mean, std, min, quartiles, max |

**Attribute vs method:** `df.shape` has **no** brackets, but `df.head()` **has** brackets. Writing `df.shape()` gives an error.

---

## 5. Selecting Data

### 5.1 Selecting columns

```python
df["Marks"]            # one column → a Series
df[["Name", "Marks"]]  # several columns → a DataFrame (note the DOUBLE brackets)
```

```
0    80
1    75
2    90
3    85
Name: Marks, dtype: int64
```

| Brackets | Gives |
|---|---|
| `df["Marks"]` | A **Series** |
| `df[["Marks"]]` | A **DataFrame** with one column |
| `df[["Name", "Marks"]]` | A **DataFrame** (the inner brackets are a list of names) |

### 5.2 Selecting rows and columns: `loc` and `iloc`

| Tool | Selects by | Example | Result |
|---|---|---|---|
| **`loc`** | **Labels** (names) | `df.loc[1, "Name"]` | `Riya` |
| **`iloc`** | **Positions** (numbers from 0) | `df.iloc[1, 0]` | `Riya` |

The pattern is `[rows, columns]`.

**Slices (ranges):**

```python
df.loc[0:1, ["Name", "Age"]]     # labels 0 to 1, including BOTH ends
df.iloc[0:2, 0:2]                # positions 0 to 1, the end (2) is NOT included
```

Both give:

```
   Name  Age
0  Aman   20
1  Riya   21
```

> **The key difference:** `loc` includes the **end** label, while `iloc` **excludes** the end position (like normal Python slicing).

### 5.3 Using a column as the index

```python
d2 = df.set_index("Name")
d2.loc["Riya", "Marks"]          # 75
```

Now rows are found by name instead of by number.

---

## 6. Filtering Rows

Put a condition inside the brackets. Pandas keeps the rows where the condition is `True`.

```python
df[df["Marks"] > 80]
```

```
   Name  Age   City  Marks
2   Sam   19  Delhi     90
3  Neha   22   Pune     85
```

**What happens inside:** `df["Marks"] > 80` first produces a True/False value for each row (`False, False, True, True`), called a **mask**. The outer `df[...]` keeps the `True` rows.

### Combining conditions

| Word | Symbol | Meaning |
|---|---|---|
| and | `&` | Both must be true |
| or | `\|` | At least one is true |
| not | `~` | The opposite |

```python
df[(df["City"] == "Delhi") & (df["Marks"] > 80)]
```

```
  Name  Age   City  Marks
2  Sam   19  Delhi     90
```

> **Always wrap each condition in brackets**, and use `&` and `|`, **not** the words `and` and `or`.

---

## 7. Adding, Changing and Removing Columns

### Add a new column

```python
df["Result"] = df["Marks"].apply(lambda m: "Pass" if m >= 40 else "Fail")
```

`lambda m: ...` is a **small one-line function**. `apply` runs it on every value of the column. You can also build a column with plain math:

```python
df["Marks_out_of_50"] = df["Marks"] / 2
```

### Remove a column

```python
df.drop(columns=["Result"])
```

### Rename a column

```python
df.rename(columns={"Marks": "Score"})
```

> **Important:** `drop` and `rename` **return a new DataFrame** and leave the original unchanged. To keep the change, assign it back: `df = df.drop(columns=["Result"])`.

---

## 8. Sorting and Quick Statistics

```python
df.sort_values("Marks", ascending=False)
```

```
   Name  Age    City  Marks
2   Sam   19   Delhi     90
3  Neha   22    Pune     85
0  Aman   20   Delhi     80
1  Riya   21  Mumbai     75
```

| Task | Code | Result |
|---|---|---|
| Average | `df["Marks"].mean()` | `82.5` |
| Largest | `df["Marks"].max()` | `90` |
| Count of each value | `df["City"].value_counts()` | Delhi 2, Mumbai 1, Pune 1 |

---

## 9. DataFrame vs List vs NumPy Array

| | List | NumPy array | DataFrame |
|---|---|---|---|
| **Dimensions** | Any | Any | Always 2D |
| **Types** | Mixed | One type for everything | **A different type per column** |
| **Labels** | No | No | **Yes** (row and column names) |
| **Missing values** | Awkward | Awkward | Built-in (`NaN`) |
| **Best for** | General data | Fast numerical math | **Real-world tables** |

---

## 10. Common Mistakes

| Mistake | Fix |
|---|---|
| `df.shape()` | `shape` is an attribute, so write `df.shape` |
| `df["Name", "Age"]` | Use a list inside: `df[["Name", "Age"]]` |
| Using `and` / `or` in filters | Use `&` / `\|` with each condition in brackets |
| Forgetting to assign after `drop` or `rename` | Write `df = df.drop(...)` |
| Confusing `loc` and `iloc` slices | `loc` includes the end label, `iloc` excludes the end position |
| Counting positions from 1 | Positions start at **0** |

---

## 11. Summary

- A **DataFrame** is a 2D table with labeled rows (the **index**) and named columns. A **Series** is one column.
- Create one from a dictionary, a list of rows, a NumPy array or a CSV (`pd.read_csv`).
- Inspect it with `shape`, `columns`, `dtypes`, `head()`, `info()` and `describe()`.
- Select a column with `df["col"]` (Series) or `df[["col"]]` (DataFrame).
- Use **`loc`** for labels and **`iloc`** for positions.
- Filter rows with a condition: `df[df["Marks"] > 80]`, combining conditions with `&` and `|`.
- Add columns by assigning, and remove or rename them with `drop` and `rename` (assign the result back).
- Each column can have its own data type, which makes DataFrames ideal for real data.

---

## 12. Practice Questions

Use the student table from Section 3.

1. In your own words, what is a DataFrame? How is it different from a Series?
2. What are `df.shape` and `df.size` for our table?
3. What does `df["Marks"]` return, and what does `df[["Marks"]]` return?
4. What do `df.loc[1, "Name"]` and `df.iloc[1, 0]` return? When would the two differ?
5. How many rows does `df.loc[0:1]` return? How many does `df.iloc[0:1]` return?
6. Which students does `df[df["Marks"] > 80]` return?
7. Write the filter for students from Delhi **or** with marks below 80. Which students match?
8. Why do we need brackets around each condition when using `&`?
9. What is the sorted order of names by Marks, highest first?
10. After `df.drop(columns=["Age"])`, does `df` still have an `Age` column? Why?
11. What is the average of `Marks`, and what does `df["City"].value_counts()` show?
12. Write code to add a column `Grade` that is `"A"` when `Marks >= 85` and `"B"` otherwise.

### Answers

1. A DataFrame is a 2D table with labeled rows and columns. A Series is one column (or row) of it.
2. `df.shape` is `(4, 4)` and `df.size` is `16`.
3. `df["Marks"]` returns a **Series**. `df[["Marks"]]` returns a one-column **DataFrame**.
4. Both return `Riya`. They differ when the index is not `0, 1, 2, ...` (for example if you set `Name` as the index), because `loc` uses labels and `iloc` uses positions.
5. `df.loc[0:1]` returns **2** rows (it includes the end label), and `df.iloc[0:1]` returns **1** row (it excludes the end position).
6. Sam (90) and Neha (85).
7. `df[(df["City"] == "Delhi") | (df["Marks"] < 80)]`. Aman and Sam (Delhi), and Riya (marks 75).
8. Because `&` binds more tightly than comparison operators, so without brackets Python reads the expression in the wrong order and raises an error.
9. Sam, Neha, Aman, Riya.
10. Yes, it still has `Age`, because `drop` returns a new DataFrame. You must write `df = df.drop(columns=["Age"])` to keep the change.
11. The average is `82.5`. `value_counts()` shows how many rows each city has: Delhi 2, Mumbai 1, Pune 1.
12. `df["Grade"] = df["Marks"].apply(lambda m: "A" if m >= 85 else "B")`
