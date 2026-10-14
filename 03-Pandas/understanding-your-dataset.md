> The seven quick checks to run on any new dataset before doing anything else.

---

## 1. The Big Idea

Before cooking, you look at the ingredients: how many there are, what they are, and whether any are spoiled. A dataset needs the same first look. These checks take a few minutes and prevent mistakes later.

We use the **Titanic dataset**: one row per passenger, with details and whether they survived.

```python
import pandas as pd
df = pd.read_csv("titanic.csv")
```

| Step | Question | Code |
|---|---|---|
| 1 | How big is the data? | `df.shape` |
| 2 | What does it look like? | `df.head()`, `df.sample(5)` |
| 3 | What is the data type of each column? | `df.info()` |
| 4 | Are there missing values? | `df.isnull().sum()` |
| 5 | What does it look like mathematically? | `df.describe()` |
| 6 | Are there duplicate rows? | `df.duplicated().sum()` |
| 7 | How are the columns correlated? | `df.corr(numeric_only=True)` |

---

## 2. Key Terms

| Term | Meaning |
|---|---|
| **Row (sample)** | One record, here one passenger |
| **Column (feature)** | One property of every record, such as Age |
| **Missing value** | A cell with no data, shown as `NaN` ("not a number") |
| **Duplicate** | A row that is repeated exactly |
| **Correlation** | How strongly two numeric columns move together |

---

## 3. Step 1: How Big Is the Data?

```python
df.shape        # (891, 12)
```

**891 rows** (passengers) and **12 columns** (features). Size tells you how heavy the analysis will be and whether the data is enough for ML.

---

## 4. Step 2: What Does the Data Look Like?

```python
df.head(3)      # first 3 rows
```

| PassengerId | Survived | Pclass | Sex | Age | Fare | Cabin |
|---|---|---|---|---|---|---|
| 1 | 0 | 3 | male | 22.0 | 7.2500 | NaN |
| 2 | 1 | 1 | female | 38.0 | 71.2833 | C85 |
| 3 | 1 | 3 | female | 26.0 | 7.9250 | NaN |

Use `df.sample(5)` as well, because the first rows may not represent the whole file. You can already spot a `NaN` in the Cabin column.

---

## 5. Step 3: Data Type of Each Column

```python
df.info()
```

| Type | Meaning | Titanic columns |
|---|---|---|
| **int64** | Whole numbers | PassengerId, Survived, Pclass, SibSp, Parch |
| **float64** | Decimal numbers | Age, Fare |
| **object (text)** | Text | Name, Sex, Ticket, Cabin, Embarked |

**Look closer:** `Survived` (0 or 1) and `Pclass` (1, 2, 3) are stored as numbers, but they are really **categories**, so averaging them as numbers is not meaningful in the usual way. Always ask what a column *means*, not just how it is stored.

`info()` also shows the **non-null count** per column, which leads to the next step.

---

## 6. Step 4: Missing Values

```python
df.isnull().sum()
```

| Column | Missing | Percent |
|---|---|---|
| Age | 177 | 19.9% |
| Cabin | 687 | 77.1% |
| Embarked | 2 | 0.2% |
| All others | 0 | 0% |

**What it suggests (decided later, in Data Cleaning):**
- **Cabin:** more than three quarters missing, so it may be dropped.
- **Age:** about a fifth missing, so it should be filled in (imputed).
- **Embarked:** only 2 missing, so fill with the most common value.

---

## 7. Step 5: The Data Mathematically

```python
df.describe()
```

| | Survived | Age | Fare |
|---|---|---|---|
| **count** | 891 | 714 | 891 |
| **mean** | 0.38 | 29.70 | 32.20 |
| **std** | 0.49 | 14.53 | 49.69 |
| **min** | 0 | 0.42 | 0.00 |
| **25%** | 0 | 20.12 | 7.91 |
| **50%** | 0 | 28.00 | 14.45 |
| **75%** | 1 | 38.00 | 31.00 |
| **max** | 1 | 80.00 | 512.33 |

**Reading each row:**

| Row | Meaning |
|---|---|
| **count** | How many values are **not missing** |
| **mean** | The average |
| **std** | Standard deviation: how spread out the values are |
| **min / max** | Smallest and largest value |
| **25% / 50% / 75%** | Quartiles: 25% of values lie below the first number. The 50% value is the **median** (the middle value). |

**What we learn:**
- Age `count` is 714, not 891, which matches the 177 missing.
- `Survived` mean is 0.38, so about **38% survived** (because the values are 0 and 1).
- Age mean (29.7) and median (28) are close, so ages are fairly balanced.
- Fare mean (32.2) is **much higher** than the median (14.45), and the max is 512.33. A **few very expensive tickets** pull the average up.
- The minimum Fare is 0, which is worth checking.

---

## 8. Step 6: Duplicate Values

```python
df.duplicated().sum()     # 0
```

No duplicate rows here. If there were, remove them with `df.drop_duplicates()`, because repeated rows can make a model overconfident (and leak across the train/test split).

---

## 9. Step 7: Correlation Between Columns

```python
df.corr(numeric_only=True)
```

**Correlation** is a number from **−1 to +1**:

| Value | Meaning |
|---|---|
| Near **+1** | Both rise together |
| Near **−1** | One rises as the other falls |
| Near **0** | No straight-line relationship |

Some Titanic values:

| Pair | Correlation | Reading |
|---|---|---|
| Survived and Pclass | **−0.34** | Lower class number (1st class) went with higher survival |
| Survived and Fare | **0.26** | Higher fares went with higher survival |
| Pclass and Fare | **−0.55** | 1st class tickets cost more |
| Pclass and Age | −0.37 | Older passengers tended to be in higher classes |
| SibSp and Parch | 0.42 | Family sizes go together |

**Warnings:**
- **Correlation is not causation.** A link does not prove one thing caused the other.
- It only captures **straight-line** relationships.
- Only **numeric** columns are included, so text columns such as Sex are left out until they are encoded.

---

## 10. Checklist and Findings

| Check | Titanic finding | Next action |
|---|---|---|
| Size | 891 rows, 12 columns | Small, so fine for quick models |
| Look | Cabin has NaN | Investigate |
| Types | `Survived`, `Pclass` are really categories | Treat as categories |
| Missing | Age 19.9%, Cabin 77.1%, Embarked 0.2% | Impute Age and Embarked, consider dropping Cabin |
| Math | Fare is heavily skewed | Look at it with univariate analysis |
| Duplicates | 0 | Nothing to do |
| Correlation | Class and Fare relate to survival | Explore further |

---

## 11. Practice Questions

1. What do the two numbers in `(891, 12)` mean?
2. Age has 177 missing out of 891. What percentage is that?
3. Why are `Survived` and `Pclass` stored as numbers but treated as categories?
4. What does the 50% row in `describe()` tell you?
5. Fare has mean 32.2 and median 14.45. What does that suggest?
6. What does a correlation of −0.34 mean? Does it prove 1st class caused survival?
7. Why can duplicate rows hurt a model?
8. List the seven steps in order.

### Answers

1. 891 rows (samples) and 12 columns (features).
2. `177 / 891 = 19.9%`.
3. The values are labels for groups (0 or 1, class 1/2/3), not quantities, so ordinary math on them is not meaningful.
4. The **median**, the middle value: half the values lie below it.
5. A few very high values pull the mean up, so the data is skewed to the right.
6. A moderate tendency for one value to fall as the other rises. No, correlation is not causation.
7. The model may over-trust repeated examples, and the same row can end up in both train and test sets.
8. Size, look, data types, missing values, mathematical summary, duplicates, correlation.
