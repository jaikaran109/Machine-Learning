> Studying one column at a time to understand its values, spread and problems.

---

## 1. The Big Idea

**EDA (Exploratory Data Analysis)** means exploring data with statistics and charts before modeling. **Univariate** means "one variable". Univariate analysis looks at **each column on its own**, like checking each ingredient separately before combining them.

| Type | Looks at |
|---|---|
| **Univariate** | One column at a time |
| **Bivariate** | The relationship between two columns |
| **Multivariate** | Many columns together |

We use the Titanic dataset again.

**Why do it:**
- See how values are spread
- Spot missing values, odd values and outliers
- Decide what cleaning or transformation is needed

---

## 2. Key Terms

| Term | Meaning |
|---|---|
| **Categorical data** | Values that are groups (Sex, Embarked). *Nominal* groups have no order. *Ordinal* groups do (class 1, 2, 3). |
| **Numerical data** | Values that are quantities. *Discrete* are counts (number of siblings). *Continuous* can take any value (Age, Fare). |
| **Distribution** | How the values are spread across their range |
| **Bin** | A range of values grouped together in a histogram |
| **Quartile** | Values that split sorted data into four equal parts (Q1, median, Q3) |
| **IQR** | Interquartile range: Q3 − Q1 |
| **Outlier** | A value far from the rest |
| **Skewness** | How lopsided a distribution is |

Titanic columns by type:

| Column | Type |
|---|---|
| Survived | Categorical (yes or no) |
| Pclass | Categorical, ordinal |
| Sex, Embarked | Categorical, nominal |
| Age, Fare | Numerical, continuous |
| SibSp, Parch | Numerical, discrete (counts) |
| Name, Ticket | Identifiers (almost unique per row) |

---

## 3. Which Chart for Which Data

| Data | Question | Tools |
|---|---|---|
| **Categorical** | How many in each group? | `value_counts()`, countplot, pie chart |
| **Numerical** | How are values spread? | Histogram, KDE curve, boxplot, `describe()`, skewness |

---

## 4. Univariate Analysis of Categorical Data

```python
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
df = pd.read_csv("titanic.csv")

print(df["Sex"].value_counts())                 # counts
print(df["Sex"].value_counts(normalize=True))   # proportions
sns.countplot(x="Sex", data=df); plt.show()     # bar chart of counts
df["Embarked"].value_counts().plot(kind="pie", autopct="%.1f%%"); plt.show()
```

| Chart | Use |
|---|---|
| **Countplot** | Bars show how many rows are in each category |
| **Pie chart** | Shows each category's share. Use only with **few** categories. |

**Titanic results:**

| Column | Counts | Reading |
|---|---|---|
| **Survived** | 0: 549 (61.6%), 1: 342 (38.4%) | More passengers died than survived |
| **Pclass** | 3rd: 491 (55.1%), 1st: 216 (24.2%), 2nd: 184 (20.7%) | More than half were in 3rd class |
| **Sex** | Male: 577 (64.8%), Female: 314 (35.2%) | Almost two thirds were male |
| **Embarked** | S: 644 (72.4%), C: 168 (18.9%), Q: 77 (8.7%), 2 missing | Most boarded at S |

**What to look for:** a dominant category, class imbalance in the target (Survived is moderately imbalanced), rare categories, and missing values.

---

## 5. Univariate Analysis of Numerical Data

### The five-number summary and the boxplot

The five numbers are **min, Q1, median, Q3, max**. A **boxplot** draws them:

- The **box** runs from Q1 to Q3, with a line at the median.
- The **whiskers** extend to the last values inside the fences below.
- **Dots** beyond the whiskers are outliers.

**The IQR rule for outliers:**

```
IQR        = Q3 − Q1
Lower fence = Q1 − 1.5 × IQR
Upper fence = Q3 + 1.5 × IQR
Values outside the fences are flagged as outliers.
```

### Histogram and KDE

A **histogram** splits the range into bins and counts values in each bin. A **KDE** is a smooth curve drawn over it.

```python
sns.histplot(df["Age"], kde=True); plt.show()
sns.boxplot(x=df["Fare"]); plt.show()
print(df["Age"].skew(), df["Fare"].skew())
```

> Older tutorials use `sns.distplot`, which is deprecated. Use `histplot` or `displot` instead.

### Skewness

| Skewness | Shape |
|---|---|
| About **0** | Symmetric |
| **Positive** | Long tail on the **right** (a few very large values) |
| **Negative** | Long tail on the **left** |

Rule of thumb: between −0.5 and 0.5 is roughly symmetric, and beyond ±1 is strongly skewed.

### Titanic results

| | Age | Fare |
|---|---|---|
| Count | 714 | 891 |
| Mean / Median | 29.7 / 28.0 | 32.2 / 14.45 |
| Q1 / Q3 | 20.1 / 38.0 | 7.91 / 31.0 |
| IQR | 17.9 | 23.1 |
| Fences | −6.7 to 64.8 | −26.7 to 65.6 |
| Outliers | 11 (all above 64.8) | 116 (all above 65.6) |
| Skewness | 0.39 | 4.79 |
| Shape | Fairly symmetric | Strongly right-skewed |

```python
q1, q3 = df["Fare"].quantile([0.25, 0.75])
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(len(df[(df["Fare"] < low) | (df["Fare"] > high)]))   # 116
```

**Age:** most passengers are between about 20 and 38, with a few older ones flagged as outliers. 177 values are missing.
**Fare:** most tickets are cheap, but a few cost hundreds, so the mean (32.2) is far above the median (14.45).

**Important:** an outlier is not always an error. The expensive fares are real first-class tickets, so deleting them would remove real information. Check first, then decide.

---

## 6. What to Do With What You Find

| Finding | Possible action (later phases) |
|---|---|
| Missing values in Age | Impute |
| Fare strongly right-skewed | Apply a log or power transform |
| Outliers in Fare | Keep, cap or transform, depending on the model |
| Target imbalance (62% / 38%) | Use stratified split and suitable metrics |
| Rare categories | Group them or handle them in encoding |

---

## 7. Summary

- **Univariate analysis** studies one column at a time.
- **Categorical:** use value counts, countplot and pie chart.
- **Numerical:** use histogram, KDE, boxplot, `describe()` and skewness.
- The **IQR rule** flags outliers: below Q1 − 1.5×IQR or above Q3 + 1.5×IQR.
- **Positive skew** means a long right tail, where mean is greater than median.
- Outliers are not automatically errors, so investigate before removing.

---

## 8. Practice Questions

1. What does "univariate" mean? How is it different from bivariate?
2. Which chart would you use for `Sex`? For `Age`? Why?
3. 314 of 891 passengers are female. What percentage is that?
4. A column has Q1 = 10 and Q3 = 30. Calculate the IQR and both fences.
5. A value of 75 appears in that column. Is it an outlier?
6. Fare has skewness 4.79 and mean greater than median. What shape is it?
7. A skewness of −1.2 means which tail is long?
8. Why is a pie chart a poor choice for a column with 20 categories?
9. Why should you not delete every outlier automatically?
10. Name two things you could do about the skewed `Fare` column.

### Answers

1. One variable at a time. Bivariate studies the relationship between two.
2. Countplot (or pie chart) for Sex, because it is categorical. Histogram or boxplot for Age, because it is numerical.
3. `314 / 891 = 35.2%`.
4. IQR = 20. Lower fence = 10 − 30 = **−20**. Upper fence = 30 + 30 = **60**.
5. Yes, 75 is above 60.
6. Strongly right-skewed, with a long tail of large values.
7. The **left** tail.
8. Too many slices to compare, so a bar chart reads more clearly.
9. Some outliers are real, valuable data (like first-class fares), and removing them loses information.
10. Apply a log or power transform, or cap extreme values.
