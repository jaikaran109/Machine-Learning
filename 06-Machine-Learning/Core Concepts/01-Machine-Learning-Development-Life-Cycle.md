> The step-by-step process for taking a machine learning project from an idea to a working model that keeps working.

---

## 1. The Big Idea

Building a model is only one step in a machine learning project. A real project has many stages: understanding the problem, getting data, cleaning it, training, evaluating, deploying and maintaining. Skipping or rushing any stage usually leads to a model that looks good in a notebook but fails in practice.

The process is **iterative**. Results at a later stage often send you back to an earlier one, for example poor evaluation leading to better features.

**Analogy (building a house):** You first decide what the family needs (problem definition), gather materials (data collection), clean and cut them (data preparation), build (training), inspect (evaluation), move in (deployment), and keep repairing it over the years (monitoring). Nobody builds the walls before knowing what house is needed.

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **ML life cycle** | The sequence of stages followed to build, deploy and maintain an ML system. | The recipe for an ML project. |
| **Business problem** | The real-world goal to be solved. | What the organization actually wants. |
| **ML problem** | The business problem restated as a prediction task with inputs and a target. | What exactly the model must predict. |
| **Success metric** | The number used to judge whether the project worked. | The scoreboard. |
| **Baseline** | A simple reference result (a simple model or a rule) that any real model must beat. | The score to beat. |
| **EDA** | Exploratory Data Analysis: studying the data with statistics and plots before modeling. | Getting to know the data. |
| **Feature engineering** | Creating or transforming input variables to make them more useful. | Better clues for the model. |
| **Data leakage** | Information from outside the training data (such as the test set) sneaking into training. | Seeing the exam paper early. |
| **Deployment** | Making the trained model available to produce predictions in the real world. | Putting it to work. |
| **Monitoring** | Tracking the deployed model's performance and the incoming data over time. | Checking it still works. |
| **Concept drift** | The data pattern changes over time, so the model becomes less accurate. | The world changed. |
| **Retraining** | Training the model again on newer data. | Refreshing the model. |

---

## 3. The Stages at a Glance

```
1. Problem Definition
        ↓
2. Data Collection
        ↓
3. Data Preparation (clean, split)
        ↓
4. Exploratory Data Analysis
        ↓
5. Feature Engineering and Selection
        ↓
6. Model Selection and Training
        ↓
7. Evaluation
        ↓
8. Tuning and Improvement ──┐
        ↓                   │ (loop back to
9. Deployment               │  earlier stages)
        ↓                   │
10. Monitoring and Maintenance ──→ retrain when needed
```

| # | Stage | Main question it answers |
|---|---|---|
| 1 | Problem definition | What are we solving, and how will we know it worked? |
| 2 | Data collection | What data do we have or need? |
| 3 | Data preparation | Is the data clean and ready? |
| 4 | EDA | What does the data tell us? |
| 5 | Feature engineering | Which inputs will help most? |
| 6 | Model training | Which algorithm fits best? |
| 7 | Evaluation | How well does it work on unseen data? |
| 8 | Tuning | Can we improve it? |
| 9 | Deployment | How do we put it to use? |
| 10 | Monitoring | Does it keep working? |

---

## 4. Stage 1: Problem Definition

### Concept

Every project starts by turning a business goal into a precise ML task. Poor problem definition is the most common reason projects fail, because a perfect model for the wrong question is useless.

### Steps

1. **State the business goal.** Example: reduce customers leaving.
2. **Decide whether ML is needed.** If a simple rule solves it, use the rule.
3. **Frame it as an ML problem.** Define the input features and the target.
4. **Identify the type.** Regression (a number) or classification (a category), supervised or unsupervised.
5. **Choose the success metric.** For example, recall for churn, RMSE for prices.
6. **Set a baseline.** For example, "predict the average price" or "predict nobody churns."

### Example

| Business goal | ML problem | Type | Metric |
|---|---|---|---|
| Reduce churn | Predict whether a customer will leave next month | Classification | Recall, F1 |
| Price houses fairly | Predict the sale price from house features | Regression | RMSE, R² |
| Find customer groups | Group customers by behavior | Clustering | Silhouette score |

---

## 5. Stage 2: Data Collection

### Concept

A model can only learn from the data it is given, so quantity, quality and relevance of data matter more than the choice of algorithm.

### Sources

Databases, spreadsheets and CSV files, APIs, web scraping (where allowed), sensors and logs, surveys, public datasets (Kaggle, UCI).

### Questions to ask

- Is there **enough** data for the complexity of the problem?
- Is it **representative** of the situations the model will face?
- Does it contain the **target label** (for supervised learning)?
- Is it **legal and ethical** to use (privacy, consent)?
- Is it **biased** toward certain groups or situations?

> **Garbage in, garbage out:** poor data produces a poor model, however advanced the algorithm.

---

## 6. Stage 3: Data Preparation

### Concept

Raw data is rarely ready for modeling. This stage cleans it and converts it into a form the algorithm can use. It usually takes the largest share of project time.

### Tasks

| Task | Example |
|---|---|
| **Handle missing values** | Fill with the median, or drop the column |
| **Remove duplicates** | Delete repeated rows |
| **Fix errors and inconsistent formats** | "M" and "Male", impossible ages |
| **Handle outliers** | Investigate extreme values, then cap, fix or keep |
| **Encode categories** | One-hot encoding, label encoding |
| **Scale features** | Standardization (important for KNN, SVM, linear models) |
| **Split the data** | Train, (validation), and test sets |

### Golden rule: split first

> Split off the **test set before** any step that learns from the data (imputing, scaling, encoding, feature selection). Fit these steps on the **training set only**, then apply them to the test set. Otherwise test information leaks into training and the final score is dishonest.

Using a scikit-learn **Pipeline** enforces this automatically.

---

## 7. Stage 4: Exploratory Data Analysis (EDA)

### Concept

EDA means looking at the data before modeling, to understand its structure, spot problems and form ideas about which features matter.

### Typical checks

| Check | Tool | What you learn |
|---|---|---|
| Size and types | `df.shape`, `df.info()` | Rows, columns, data types |
| Summary statistics | `df.describe()` | Ranges, means, suspicious values |
| Missing values | `df.isna().sum()` | Which columns need cleaning |
| Distributions | Histograms, box plots | Skew and outliers |
| Target balance | `y.value_counts()` | Whether classes are imbalanced |
| Relationships | Correlation matrix, scatter plots | Which features relate to the target |
| Category effects | Group-by averages, bar charts | How categories differ |

### Why it matters

EDA can reveal imbalanced classes, data errors, features that duplicate each other, or a pattern that suggests a useful new feature. It guides the next stages.

---

## 8. Stage 5: Feature Engineering and Selection

### Concept

The **features** are the clues the model uses, and better clues often help more than a fancier algorithm.

### Feature engineering

Creating or transforming features to expose the pattern more clearly.

| Technique | Example |
|---|---|
| Combine features | `price_per_sqft = price / area` |
| Extract parts | Month and weekday from a date |
| Polynomial features | `x²`, `x·y` |
| Transform skewed values | Log of income |
| Bin values | Age groups |
| Aggregate | Number of purchases in the last 30 days |

### Feature selection

Removing features that add noise or duplicate others, which reduces overfitting and speeds up training. Methods include dropping highly correlated features, using Lasso, and looking at feature importance from tree models.

---

## 9. Stage 6: Model Selection and Training

### Concept

Choose an algorithm that suits the problem and train it, meaning find the parameters that minimize the cost (as in the gradient descent topic).

### Steps

1. **Start with a simple baseline model** (for example Linear or Logistic Regression).
2. **Try several candidate algorithms** (KNN, Decision Tree, Random Forest, XGBoost).
3. **Train each** on the training set.
4. **Compare them with cross-validation**, not on the test set.

### Choosing the algorithm

| Consideration | Guidance |
|---|---|
| **Problem type** | Regression, classification, clustering |
| **Data size** | Small data suits simpler models. Instance-based methods like KNN struggle on very large data. |
| **Tabular data** | Gradient boosting (XGBoost) and Random Forest are usually strong |
| **Explainability needed** | Linear models and decision trees are easier to explain |
| **Training and prediction speed** | Model-based methods predict faster than instance-based ones |

> Start simple. A simple model that is nearly as accurate is easier to explain, cheaper to run and less likely to overfit.

---

## 10. Stage 7: Evaluation

### Concept

Measure how well the model works on **data it has never seen**, using a metric that matches the business goal.

### Choosing the metric

| Problem | Metrics |
|---|---|
| Regression | MAE, RMSE, R² |
| Balanced classification | Accuracy, F1 |
| Imbalanced classification | Precision, Recall, F1, ROC-AUC |

**Accuracy can mislead.** If only 5% of customers churn, a model that always predicts "no churn" is 95% accurate but catches **zero** churners. Recall, precision and F1 reveal this.

### The evaluation routine

1. Use **cross-validation** on the training set to compare models.
2. Check **training vs validation score** to spot overfitting or underfitting.
3. Compare against the **baseline**.
4. Inspect the **errors** (confusion matrix, worst predictions).
5. Evaluate the final chosen model on the **test set once**.

---

## 11. Stage 8: Tuning and Improvement

### Concept

If the results fall short of the goal, improve the model. Improvement is a **loop**, so you may return to any earlier stage.

| Approach | Example |
|---|---|
| **Hyperparameter tuning** | GridSearchCV, RandomizedSearchCV |
| **Better features** | New engineered features |
| **More or better data** | Collect more, fix errors, fix labels |
| **Handle imbalance** | Class weights, resampling |
| **Reduce overfitting** | Regularization, pruning, simpler model |
| **Reduce underfitting** | More flexible model, more features |
| **Ensembling** | Random Forest, boosting, combining models |

Diagnose first (bias or variance?) and then act. Randomly trying things wastes time.

---

## 12. Stage 9: Deployment

### Concept

A model only creates value when it is **used**. Deployment makes the trained model available to produce predictions on new data in the real world.

### Common ways

| Method | Description |
|---|---|
| **Batch predictions** | Run the model on a schedule and store the results (for example, nightly churn scores) |
| **Real-time API** | Wrap the model in a web service that returns a prediction per request |
| **Embedded** | Run inside an app or device |
| **Dashboard or app** | A simple interface such as Streamlit |

### Practical points

- **Save the whole pipeline** (preprocessing plus model), not just the model, so new data is treated exactly like the training data:

```python
import joblib
joblib.dump(model, "model.joblib")
model = joblib.load("model.joblib")
```

- Keep the **versions** of libraries and data used.
- Test the deployed system on realistic inputs.

---

## 13. Stage 10: Monitoring and Maintenance

### Concept

After deployment, the world keeps changing. Customer behavior, fraud patterns and prices shift, so a model that was accurate at launch can slowly get worse. This is **concept drift**, and it connects to the batch vs online topic.

### What to monitor

| What | Why |
|---|---|
| **Prediction quality** (when true outcomes become known) | Detect falling accuracy |
| **Input data distribution** | Detect changes in the incoming data (data drift) |
| **Errors and failures** | Catch bugs and bad inputs |
| **Speed and cost** | Make sure it stays practical |

### What to do when performance drops

- **Retrain** on fresher data, either periodically (batch learning) or continuously (online learning).
- Review features and the problem definition, since the situation may have changed.
- Keep a record of model versions so you can roll back.

---

## 14. Worked Example: Customer Churn Project

This project is on your Phase 4 list, so here is how each stage applies.

| Stage | What you would do |
|---|---|
| **1. Problem definition** | Goal: reduce customers leaving. Task: classify whether a customer will churn next month. Metric: recall and F1. Baseline: predict "no churn" for everyone. |
| **2. Data collection** | Customer records: tenure, plan, monthly charges, support calls, and a churn label. |
| **3. Data preparation** | Fix missing values, remove duplicates, encode categories, scale numbers. **Split first**, using `stratify=y` because churners are rare. |
| **4. EDA** | Check the churn rate (for example 5%, so imbalanced). Check which features relate to churn. |
| **5. Feature engineering** | Create "average charge per month of tenure", "calls in last 30 days". |
| **6. Model training** | Logistic Regression as the baseline, then Random Forest and XGBoost. |
| **7. Evaluation** | Compare with stratified 5-fold cross-validation using F1. Accuracy alone would be misleading. Final check on the test set once. |
| **8. Tuning** | Tune `max_depth`, `n_estimators`, class weights. |
| **9. Deployment** | Save the pipeline and score all customers each night. |
| **10. Monitoring** | Compare predictions with real churn each month. Retrain every quarter, or sooner if recall drops. |

### Code skeleton (Stages 3 to 9)

```python
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load data (assumes the "churn" column is 0 or 1)
df = pd.read_csv("churn.csv")
X = df.drop(columns="churn")
y = df["churn"]

# Split FIRST (stratified because classes are imbalanced)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

num_cols = X.select_dtypes(include="number").columns
cat_cols = X.select_dtypes(exclude="number").columns

# Preprocessing (fitted on training data only, inside the pipeline)
preprocess = ColumnTransformer([
    ("num", Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ]), num_cols),
    ("cat", Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder(handle_unknown="ignore")),
    ]), cat_cols),
])

model = Pipeline([
    ("prep", preprocess),
    ("clf", RandomForestClassifier(class_weight="balanced", random_state=42)),
])

# Compare with cross-validation on the training set
print("CV F1:", cross_val_score(model, X_train, y_train, cv=5, scoring="f1").mean())

# Train, then evaluate on the test set ONCE
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))

# Save the whole pipeline for deployment
joblib.dump(model, "churn_model.joblib")
```

---

## 15. Common Mistakes

| Mistake | Why it hurts | Fix |
|---|---|---|
| Jumping straight to modeling | You may solve the wrong problem | Define the problem and metric first |
| Preprocessing before splitting | Data leakage, dishonest score | Split first, use a Pipeline |
| Tuning on the test set | The test set stops being unseen | Tune with cross-validation |
| Judging only by accuracy on imbalanced data | Hides a useless model | Use precision, recall, F1, ROC-AUC |
| Skipping the baseline | You can't tell if the model is any good | Always compare to a simple baseline |
| Starting with the most complex model | Overfitting, hard to explain | Start simple and add complexity if needed |
| Ignoring the data (no EDA) | Missed errors and imbalance | Explore before modeling |
| Treating deployment as the end | Models degrade over time | Monitor and retrain |

---

## 16. Summary

- The ML life cycle has ten stages: problem definition, data collection, data preparation, EDA, feature engineering, model training, evaluation, tuning, deployment and monitoring.
- It is **iterative**. Later results send you back to earlier stages.
- **Define the problem and metric first**, and always set a **baseline**.
- **Data quality matters more than algorithm choice.** Data preparation usually takes the most time.
- **Split before preprocessing** to avoid data leakage, and use a Pipeline.
- Compare models with **cross-validation**, and touch the **test set only once**.
- Pick metrics that match the goal. Accuracy misleads on imbalanced data.
- Deployment is not the end. **Monitor for concept drift and retrain** when needed.

---