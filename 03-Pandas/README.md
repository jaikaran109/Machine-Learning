# Phase 2: Pandas

> The main Python library for loading, exploring, cleaning and reshaping tabular data.

---

## Overview

| | |
|---|---|
| **Focus** | Getting data into Python and getting it ready for analysis |
| **Prerequisites** | Phase 0 (Python), NumPy |
| **Libraries** | pandas, plus requests and BeautifulSoup for gathering data |
| **Branch / folder** | `03-Pandas` |
| **Next** | `04-Data-Visualization` |

**Why Pandas matters:** real data arrives as messy tables. Pandas is where you load it, inspect it and clean it before any chart or model.

---

## Table of Contents

- [DataFrames](#dataframes)
- [Data Gathering](#data-gathering)
- [Understanding Your Data](#understanding-your-data)
- [Data Manipulation](#data-manipulation)
- [Data Cleaning](#data-cleaning)
- [Handling Missing Data](#handling-missing-data)
- [Outlier Detection and Removal](#outlier-detection-and-removal)
- [Command Cheat Sheet](#command-cheat-sheet)
- [Notes in This Branch](#notes-in-this-branch)
- [Progress Checklist](#progress-checklist)
- [Outcome](#outcome)

---

## DataFrames

| Term | Meaning |
|---|---|
| **Series** | One labeled column of data |
| **DataFrame** | A table of rows and columns, like a spreadsheet in Python |
| **Index** | The labels for the rows |
| **Columns** | The labels for the columns |
| **dtype** | The data type of a column (`int64`, `float64`, `object` for text) |

---

## Data Gathering

| Source | How | Code idea |
|---|---|---|
| **CSV files** | Read a comma-separated file | `pd.read_csv("file.csv")` |
| **JSON** | Read nested data | `pd.read_json("file.json")` |
| **SQL databases** | Run a query and load the result | `pd.read_sql(query, connection)` |
| **APIs** | Request data from a web service, then convert | `requests.get(url).json()` then `pd.DataFrame(...)` |
| **Web scraping** | Download a page and pick out the data | `requests` + BeautifulSoup (or `pd.read_html` for simple tables) |

> Always check the website's terms and `robots.txt` before scraping.

---

## Understanding Your Data

Run these seven checks on every new dataset (full explanation in the note below).

| Step | Question | Command |
|---|---|---|
| 1 | How big is the data? | `df.shape` |
| 2 | What does it look like? | `df.head()`, `df.sample(5)` |
| 3 | What is the type of each column? | `df.info()` |
| 4 | Are there missing values? | `df.isnull().sum()` |
| 5 | What does it look like mathematically? | `df.describe()` |
| 6 | Are there duplicate rows? | `df.duplicated().sum()` |
| 7 | How are the columns correlated? | `df.corr(numeric_only=True)` |

---

## Data Manipulation

| Task | Meaning | Code idea |
|---|---|---|
| **Select columns** | Pick one or more columns | `df["Age"]`, `df[["Age", "Fare"]]` |
| **Select rows by label** | Use row and column labels | `df.loc[0, "Age"]` |
| **Select rows by position** | Use integer positions | `df.iloc[0, 3]` |
| **Filter** | Keep rows matching a condition | `df[df["Age"] > 30]` |
| **Combine conditions** | `&` for and, `\|` for or (use brackets) | `df[(df["Age"] > 30) & (df["Sex"] == "female")]` |
| **Sort** | Order the rows | `df.sort_values("Fare", ascending=False)` |
| **Group and summarize** | Split into groups, then compute a summary | `df.groupby("Sex")["Survived"].mean()` |
| **Merge (join)** | Combine tables on a shared column | `pd.merge(df1, df2, on="id")` |
| **Concatenate** | Stack tables together | `pd.concat([df1, df2])` |
| **New columns** | Create a column from others | `df["family"] = df["SibSp"] + df["Parch"]` |
| **Apply a function** | Run a function on each value | `df["Age"].apply(func)` |

---

## Data Cleaning

| Task | Meaning | Code idea |
|---|---|---|
| **Fix data types** | Convert a column to the right type | `df["col"].astype("int")` |
| **Remove duplicates** | Drop repeated rows | `df.drop_duplicates()` |
| **Fix inconsistent values** | Standardize spelling and case | `df["col"].str.lower()` |
| **Rename columns** | Make labels clear | `df.rename(columns={"old": "new"})` |
| **Drop columns or rows** | Remove what is not needed | `df.drop(columns=["Cabin"])` |
| **Handle missing values** | See the next section | |

---

## Handling Missing Data

A **missing value** is an empty cell, shown as `NaN`. First count them with `df.isnull().sum()`, then pick a method.

| Method | Idea | Code idea |
|---|---|---|
| **Complete case analysis** | Delete rows with missing values | `df.dropna()` |
| **Numerical imputation** | Fill with the mean or median | `df["Age"].fillna(df["Age"].median())` |
| **Categorical imputation** | Fill with the most common value, or a "Missing" label | `df["Embarked"].fillna(df["Embarked"].mode()[0])` |
| **Missing indicator** | Add a column that flags which values were missing | `df["Age_missing"] = df["Age"].isnull()` |
| **KNN imputer** | Fill using the values of similar rows | scikit-learn `KNNImputer` |
| **Iterative imputer** | Predict each missing column from the others | scikit-learn `IterativeImputer` |

**How to choose:**
- Very few missing (around 5% or less) and random: deleting rows is acceptable.
- A column mostly empty (like Cabin, 77% missing): consider dropping the column.
- Skewed numeric columns: prefer the **median** over the mean.

---

## Outlier Detection and Removal

An **outlier** is a value far from the rest. Investigate before removing, since some outliers are real data.

| Method | Rule |
|---|---|
| **Z-score** | Flag values more than about 3 standard deviations from the mean: `z = (x − mean) / std` |
| **IQR** | Flag values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR |
| **Percentile / winsorization** | Cap values at chosen percentiles (for example the 1st and 99th) instead of deleting them |

```python
q1, q3 = df["Fare"].quantile([0.25, 0.75])
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = df[(df["Fare"] < low) | (df["Fare"] > high)]
```

---

## Command Cheat Sheet

```python
import pandas as pd

df = pd.read_csv("titanic.csv")

# Look
df.shape; df.head(); df.info(); df.describe()

# Select and filter
df["Age"]; df[["Age", "Fare"]]; df[df["Age"] > 30]

# Group and sort
df.groupby("Pclass")["Survived"].mean()
df.sort_values("Fare", ascending=False)

# Clean
df.isnull().sum()
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df.drop_duplicates()
```

---

## Notes in This Branch

| Topic | File |
|---|---|
| Understanding Your Dataset | [`understanding-your-dataset.md`](understanding-your-dataset.md) |

Add a row here for each new note.

---

## Progress Checklist

- [ ] DataFrames
- [ ] Data Gathering (CSV, JSON and SQL, APIs, web scraping)
- [ ] Understanding Your Data
- [ ] Data Manipulation
- [ ] Data Cleaning
- [ ] Missing Values (complete case, numerical, categorical, indicator, KNN and iterative imputer)
- [ ] Outlier Detection and Removal (z-score, IQR, winsorization)

---

## Outcome

By the end of this branch, you can:

- Load data from files, databases, APIs and web pages into a DataFrame.
- Run a quick health check on any new dataset.
- Select, filter, sort, group and merge data.
- Clean data by fixing types, removing duplicates, and handling missing values and outliers.
