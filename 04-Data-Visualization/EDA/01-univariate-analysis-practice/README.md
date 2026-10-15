# EDA: Univariate Analysis (Notebook)

> **Phase 2: Data Visualization, EDA**
> A hands-on notebook that studies the Titanic dataset **one column at a time**, using charts and summary statistics.

---

## Overview

| | |
|---|---|
| **Notebook** | [`01-univariate-analysis.ipynb`](01-univariate-analysis.ipynb) |
| **Topic** | Univariate analysis (one variable at a time) |
| **Dataset** | Titanic passenger data (891 rows, 12 columns) |
| **Libraries** | pandas, seaborn, matplotlib |
| **Companion note** | [`01-univariate-analysis.md`](01-univariate-analysis.md) |

**Goal:** understand how the values of each column are spread, using the right chart for each data type.

---

## Dataset

The notebook uses the Titanic passenger dataset from Kaggle: **Titanic - Machine Learning from Disaster**. Each row is one passenger, and the columns used here are:

| Column | Type | Meaning |
|---|---|---|
| `Survived` | Categorical | 0 = did not survive, 1 = survived |
| `Pclass` | Categorical (ordinal) | Ticket class: 1, 2 or 3 |
| `Sex` | Categorical | Male or female |
| `Age` | Numerical | Age in years |
| `Fare` | Numerical | Ticket price |

> The data file is **not included** in this repository. Download it from the Kaggle page above and place it where the notebook can read it (see [How to Run](#how-to-run)).

---

## What the Notebook Covers

### 1. Categorical data

| Step | Code idea | What it shows |
|---|---|---|
| **Countplot** | `sns.countplot(x='Survived', data=df)` and `value_counts()` | How many rows fall in each category |
| **Pie chart** | `df['col'].value_counts().plot(kind='pie', autopct='%.2f')` | Each category's percentage share (done for `Survived`, `Pclass` and `Sex`) |

### 2. Numerical data

| Step | Code idea | What it shows |
|---|---|---|
| **Histogram** | `plt.hist(df['Age'])` | The range of ages, grouped into bins |
| **Distribution plot** | `sns.distplot(df['Age'])` | A histogram with a smooth curve over it |
| **Boxplot** | `sns.boxplot(df['Fare'])` | Median, quartiles and outliers of the fares |
| **Summary values** | `min()`, `max()`, `mean()` on `Age` | The basic numbers behind the plot |

**Which chart for which data:**

| Data type | Charts used |
|---|---|
| Categorical | Countplot, pie chart |
| Numerical | Histogram, distplot, boxplot |

---

## Key Findings

Using the standard 891-row Titanic file:

| Column | Finding |
|---|---|
| **Survived** | 549 passengers (61.6%) did not survive and 342 (38.4%) did |
| **Pclass** | More than half (55.1%) were in 3rd class |
| **Sex** | About two thirds (64.8%) were male |
| **Age** | Ranges from 0.42 to 80, with a mean of about 29.7. Most passengers are between about 20 and 38. |
| **Fare** | Strongly right-skewed. A few very high fares appear as outliers on the boxplot. |

---

## How to Run

### Option 1: Google Colab

1. Open the notebook in Colab.
2. Upload `Titanic-Dataset.csv` using the Files panel on the left.
3. Run all cells.

The notebook reads the file from `/content/Titanic-Dataset.csv`, which is the Colab upload location.

### Option 2: Locally (Jupyter)

```bash
pip install pandas seaborn matplotlib jupyter
jupyter notebook
```

Then change the path in the data-loading cell to where you saved the file:

```python
df = pd.read_csv('Titanic-Dataset.csv')
```

---

## Notes

- `sns.distplot` is **deprecated** in recent seaborn versions and may show a warning. The modern replacement is:

```python
sns.histplot(df['Age'], kde=True)
```

- Missing values are not handled in this notebook. `Age` has 177 missing values, which the plots simply ignore.
- Pie charts work well here because each column has only a few categories.

---

## Next Steps

| Topic | Status |
|---|---|
| Univariate analysis | Done (this notebook) |
| Bivariate analysis (two columns) | Planned |
| Multivariate analysis (many columns) | Planned |
| Handling missing values and outliers found here | Phase 2, Data Cleaning |
