# Phase 2: Data Visualization

> Turning data into charts that reveal patterns, problems and answers.

---

## Overview

| | |
|---|---|
| **Focus** | Plotting data and using charts for Exploratory Data Analysis (EDA) |
| **Prerequisites** | NumPy, Pandas (`03-Pandas`) |
| **Libraries** | Matplotlib, Seaborn, ydata-profiling |
| **Projects** | 3 |
| **Branch / folder** | `04-Data-Visualization` |
| **Next** | Phase 3: SQL |

**Why visualization matters:** numbers in a table hide patterns that a chart shows in seconds, such as skew, outliers and relationships between columns.

---

## Table of Contents

- [Matplotlib](#matplotlib)
- [Seaborn](#seaborn)
- [Choosing the Right Chart](#choosing-the-right-chart)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Projects](#projects)
- [Code Cheat Sheet](#code-cheat-sheet)
- [Notes in This Branch](#notes-in-this-branch)
- [Progress Checklist](#progress-checklist)
- [Outcome](#outcome)

---

## Matplotlib

The base plotting library in Python. It gives full control over every part of a chart.

| Concept | Meaning |
|---|---|
| **Figure** | The whole canvas |
| **Axes** | One plot inside the figure |
| **Labels, title, legend** | The text that makes a chart readable |
| **Subplots** | Several plots in one figure (`plt.subplots`) |
| **Saving** | Export a chart as an image (`plt.savefig`) |

Common plots: line, bar, scatter, histogram, pie.

---

## Seaborn

A library built on Matplotlib that makes statistical charts with less code and better default styling. It works directly with DataFrames.

| Plot | Function |
|---|---|
| Count of categories | `sns.countplot` |
| Distribution | `sns.histplot` (with `kde=True`) |
| Spread and outliers | `sns.boxplot` |
| Relationship of two numbers | `sns.scatterplot` |
| Correlation table | `sns.heatmap` |
| All pairs of numeric columns | `sns.pairplot` |

---

## Choosing the Right Chart

| Goal | Chart | Typical code |
|---|---|---|
| Trend over time | **Line plot** | `sns.lineplot` |
| Compare categories | **Bar chart** | `sns.barplot`, `sns.countplot` |
| See how a number is spread | **Histogram** | `sns.histplot` |
| See spread and outliers | **Boxplot** | `sns.boxplot` |
| Relationship of two numbers | **Scatter plot** | `sns.scatterplot` |
| Share of a whole (few categories only) | **Pie chart** | `.plot(kind="pie")` |
| Correlations between columns | **Heatmap** | `sns.heatmap(df.corr(numeric_only=True), annot=True)` |
| Overview of many numeric columns | **Pair plot** | `sns.pairplot` |

---

## Exploratory Data Analysis (EDA)

**EDA** means exploring data with statistics and charts **before** modeling, to understand it, spot problems and form ideas. It moves from one column, to two, to many.

### Univariate analysis (one column)

| Data | Tools |
|---|---|
| **Categorical** | Value counts, countplot, pie chart |
| **Numerical** | Histogram, KDE curve, boxplot, `describe()`, skewness |

Look for: dominant categories, class imbalance, skewed shapes, and outliers (the IQR rule).

### Bivariate analysis (two columns)

| Column types | Tools |
|---|---|
| **Number and number** | Scatter plot, correlation |
| **Number and category** | Boxplot, bar plot, violin plot, `groupby` averages |
| **Category and category** | `pd.crosstab`, grouped or stacked bars, heatmap |

### Multivariate analysis (many columns)

| Tool | Use |
|---|---|
| **Correlation heatmap** | Spot related columns at a glance |
| **Pair plot** | See every pair of numeric columns together |
| **Extra dimensions** | Add a third variable with `hue`, `size` or separate panels (`col=`) |

### Automated EDA

A **profiling report** summarizes every column, missing values, correlations and more in one HTML page. The library formerly called *pandas-profiling* is now **`ydata-profiling`**.

```python
from ydata_profiling import ProfileReport
ProfileReport(df).to_file("report.html")
```

Use it to get a quick overview, then still check the important columns yourself.

---

## Projects

| Project | Skills practiced |
|---|---|
| **IPL Data Analysis** | Pandas grouping, bar and line charts, comparing teams and seasons |
| **Netflix Data Analysis** | Cleaning, categorical analysis, trends over time |
| **Sales Data Analysis** | Aggregation, time trends, heatmaps, reporting |

Suggested location: a `projects/` folder in this branch, with one folder per project (notebook plus a short README).

---

## Code Cheat Sheet

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# One column
sns.countplot(x="Sex", data=df)
sns.histplot(df["Age"], kde=True)
sns.boxplot(x=df["Fare"])

# Two columns
sns.scatterplot(x="Age", y="Fare", data=df)
sns.boxplot(x="Pclass", y="Fare", data=df)
pd.crosstab(df["Sex"], df["Survived"])

# Many columns
sns.heatmap(df.corr(numeric_only=True), annot=True)
sns.pairplot(df[["Age", "Fare", "Pclass", "Survived"]], hue="Survived")

plt.show()
```

---

## Notes in This Branch

| Topic | File |
|---|---|
| EDA: Univariate Analysis | [`eda/01-univariate-analysis.md`](eda/01-univariate-analysis.md) |
| EDA: Bivariate and Multivariate Analysis | *planned* (`eda/02-bivariate-multivariate-analysis.md`) |

Update the second row to a link once you add that note.

---

## Progress Checklist

- [ ] Matplotlib
- [ ] Seaborn
- [ ] EDA: Univariate Analysis
- [ ] EDA: Bivariate Analysis
- [ ] EDA: Multivariate Analysis
- [ ] Automated EDA (profiling report)
- [ ] IPL Data Analysis
- [ ] Netflix Data Analysis
- [ ] Sales Data Analysis

---

## Outcome

By the end of this branch, you can:

- Build clear charts with Matplotlib and Seaborn.
- Choose the right chart for the question and the data type.
- Run univariate, bivariate and multivariate EDA on a new dataset.
- Spot skew, outliers, imbalance and relationships from charts.
- Complete three analysis projects and present the findings.
