> Two ways of training and updating a machine learning model.

---

## 1. The Big Idea

The main question is:

> Do we train the model on a large collection of data **at once**, or do we **keep updating it** as new data arrives?

| Approach | In one line |
|---|---|
| **Batch Learning** | Train on a fixed, complete dataset, then deploy. |
| **Online Learning** | Learn step by step as each new piece of data arrives. |

**Analogy (studying for an exam):**
- **Batch:** collect all your notes first, study everything, then take the exam. You don't change your plan after every new piece of information.
- **Online:** learn Topic 1, spot a mistake, adjust, learn Topic 2, adjust again. Your knowledge keeps adapting as information comes in.

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Batch learning** | The model is trained on a fixed, complete dataset in one go. It does not learn from new data automatically afterwards. | Study everything, then stop. |
| **Retraining** | Training the model again on the old data plus the new data. | Study again from the updated notes. |
| **Online learning** | The model learns incrementally, updating itself as new data arrives. | Keep learning continuously. |
| **Data stream** | Data that arrives continuously, one record or small chunk at a time. | A never-ending flow of data. |
| **Concept drift** | The relationship or pattern in the data changes over time. | The world changes, the old rules stop working. |
| **Incremental update** | A small adjustment to the model using only the newest data. | A quick correction, not a full re-study. |

---

## 3. Batch Learning

### Concept

The model is trained once on a **fixed, complete dataset**. After training, it does not learn from new data on its own. If new data arrives, you generally have to **retrain** using the updated dataset.

```
Historical Data
      ↓
   Training
      ↓
    Model
      ↓
 Predictions
```

### Retraining example

You trained a churn model on 100,000 customer records. Tomorrow you receive 5,000 new customers. The existing model does not learn from them automatically.

```
Old Data:       100,000
New Data:         5,000
                ───────
Total Data:     105,000
      ↓
  Retraining
      ↓
 Updated Model
```

### When to use it

Batch learning suits problems where:
- Data doesn't change very rapidly.
- Data can be collected in advance.
- Real-time adaptation isn't necessary.

**Why it helps:** you can train periodically, test the model, evaluate performance and deploy a stable version. This makes the system easier to manage, because continuously updating gives little benefit when the problem isn't changing quickly.

### Use cases

**1. House price prediction.** A real-estate company has 500,000 historical records (area, bedrooms, location, age, bathrooms, price). The model doesn't need to learn every time one house is sold.

```
New data collected → Every month → Retrain model → Deploy updated model
```

House prices don't need second-by-second updates, so periodic retraining is enough.

**2. Student pass/fail prediction.** Using attendance, previous marks, assignments, internal marks and study hours from earlier semesters, you can retrain once per semester.

**3. Movie recommendation.** A streaming platform has 100 million user interactions. It trains on the large dataset and retrains every day, every few hours or every week, depending on its needs. Processing a large amount of data together makes training more controlled and easier to optimize.

---

## 4. Online Learning

### Concept

The model learns **incrementally** from new data as it arrives, instead of waiting for a huge dataset.

```
Batch:    Data → Train → Stop

Online:   Data 1 → Update Model
          Data 2 → Update Model
          Data 3 → Update Model
          ...
```

### Example: email spam detector

```
New Email
   ↓
 Model
   ↓
Prediction
   ↓
Actual feedback (spam or not)
   ↓
Model gets updated
```

The model gradually adapts. This matters because spammers keep changing their techniques. Today the message might be "Congratulations! You won $1,000", and tomorrow "Your account requires verification...". A model that learns only once a year becomes outdated.

### When to use it

Online learning suits problems where:
- Data keeps arriving continuously.
- Patterns can change.
- Fast adaptation is useful.

### Use cases

**1. Fraud detection.** A bank processes millions of transactions, and fraud patterns keep changing. When a new transaction is labeled fraud or legitimate, that feedback updates the model, so it adapts to new behavior instead of relying only on old training data.

```
New transaction → Prediction → Fraud / Legitimate → Feedback → Model update
```

**2. Market data.** New data arrives every minute, and the market can change (normal market, then economic news, then a crash, then different patterns). An online system can adapt to newer patterns instead of relying entirely on old ones.

> **Important:** this does not mean online learning can reliably predict stock prices. It only describes a training strategy that can adapt to changing data.

**3. IoT sensor monitoring.** A factory machine produces readings every second (temperature, pressure, vibration, voltage). Waiting to collect 10 years of data before updating the model would not help detect a problem happening now.

```
Sensor → New data → Model → Prediction → Update model
```

---

## 5. Data Stream

Online learning is especially useful when the data is a **continuous stream**.

```
IoT Sensor
    ↓
Data every second
    ↓
10:00:01
10:00:02
10:00:03
10:00:04
...
```

Each new reading can be used to update the model straight away, so the system adapts to changing machine behavior.

---

## 6. Concept Drift

**Concept drift** means the relationship or pattern in your data changes over time.

**Example:** customers once liked Product A, but after some time they prefer Product B. A model trained on the old behavior starts performing badly.

```
Changing data
      ↓
Concept Drift
      ↓
Old model may become less accurate
      ↓
Online Learning
      ↓
Continuous adaptation
```

Concept drift is one of the main reasons online learning is useful in real-world ML systems. (Batch systems handle it too, by retraining often enough.)

---

## 7. Comparison

| Feature | Batch Learning | Online Learning |
|---|---|---|
| **Training** | Large dataset at once | Incrementally |
| **New data** | Usually requires retraining | Can update the model |
| **Data arrival** | Periodic or static | Continuous or streaming |
| **Adaptation** | Slower | Faster |
| **Suitable for** | Stable problems | Changing environments |
| **Computation** | Can require large training jobs | Smaller incremental updates |
| **Model updates** | Periodic | Frequent or continuous |
| **Example** | House price model | Fraud detection |
| **Another example** | Student prediction | Spam detection |

---

## 8. Which One Should You Use?

Don't think "batch = good, online = better". **It depends on the problem.**

**Use Batch Learning when:**

```
Data is relatively stable
        +
Data can be collected
        +
Real-time adaptation isn't necessary
        ↓
Batch Learning
```

Examples: house price prediction, student performance prediction, periodic demand forecasting, many recommendation systems, customer segmentation.

**Use Online Learning when:**

```
Data keeps arriving
        +
Patterns can change
        +
Fast adaptation is useful
        ↓
Online Learning
```

Examples: spam detection, fraud detection, IoT monitoring, real-time recommendation adaptation, some advertising systems, streaming data applications.

---

## 9. Summary

- **Batch learning** trains on a fixed, complete dataset. New data usually means **retraining**.
- **Online learning** updates the model **incrementally** as data arrives.
- Batch suits **stable** problems and gives a controlled, easy-to-manage system.
- Online suits **streaming, changing** data and adapts faster.
- **Concept drift** (patterns changing over time) is a main reason for online learning.
- Neither is better in general. Choose based on how fast the data and patterns change.

---
