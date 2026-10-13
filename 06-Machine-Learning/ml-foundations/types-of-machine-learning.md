> The main ways a machine learning system can learn, and how to tell which one a problem needs.

---

## 1. The Big Idea

Machine learning is usually divided into types according to **what kind of feedback the system gets while learning**. Does it get the correct answers, no answers at all, a few answers, or only a reward for good behavior?

**Analogy:** Think of five different teachers.

| Teacher | How they teach | Type of ML |
|---|---|---|
| Gives problems **with the answer key** | You learn to match the answers | Supervised |
| Gives you **no answers**, only a pile of material to organize | You find the patterns yourself | Unsupervised |
| Gives a **few answers**, and a large pile with none | You use the few to understand the rest | Semi-supervised |
| Hides part of the material and asks you to **predict the hidden part** | You create your own exercises | Self-supervised |
| Says nothing, only gives **praise or penalties** after your actions | You learn by trial and error | Reinforcement |

---

## 2. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Feature (input)** | A measurable property used to describe an example (area, age, word count). | The clues. |
| **Label (target, output)** | The correct answer for an example (price, spam or not spam). | The answer. |
| **Labeled data** | Examples that come with their correct label. | Questions with answers. |
| **Unlabeled data** | Examples with no label. | Questions without answers. |
| **Agent** | The learner that takes actions (reinforcement learning). | The player. |
| **Environment** | The world the agent acts in. | The game. |
| **Reward** | A number that tells the agent how good its action was. | Points scored. |

---

## 3. Supervised Learning

### Concept

The model learns from **labeled data**. For each example it sees the input **and** the correct answer, and it learns the mapping from one to the other. Later it predicts the answer for new inputs.

```
Training:   (features, label) pairs  →  model learns the mapping
Prediction: new features             →  predicted label
```

### The two tasks

| Task | Predicts | Examples |
|---|---|---|
| **Regression** | A continuous **number** | House price, temperature, sales |
| **Classification** | A **category** | Spam or not spam, disease or healthy, which digit |

Classification has variants:

| Variant | Meaning | Example |
|---|---|---|
| **Binary** | Two classes | Churn: yes or no |
| **Multiclass** | One of several classes | Handwritten digit 0-9 |
| **Multilabel** | Several labels at once | A photo tagged "beach" and "sunset" |

### Algorithms

| Task | Algorithms |
|---|---|
| **Regression** | Linear, Multiple Linear, Polynomial Regression; Decision Tree, Random Forest, Gradient Boosting, XGBoost (regression versions) |
| **Classification** | Logistic Regression, KNN, Naive Bayes, SVM, Decision Tree, Random Forest, Gradient Boosting, XGBoost |

### Evaluation

Since the true answers are known, we can measure performance directly with metrics such as MSE and R² (regression), or accuracy, precision, recall, F1 and ROC-AUC (classification).

### Strength and limit

It is the most accurate and widely used type, but it needs **labeled data**, which is often expensive because humans must create the labels.

---

## 4. Unsupervised Learning

### Concept

The model learns from **unlabeled data**. No correct answers are provided, so it must discover **hidden structure** on its own, such as groups, patterns or simpler representations.

### The main tasks

| Task | Goal | Algorithms | Example |
|---|---|---|---|
| **Clustering** | Group similar examples | K-Means, Hierarchical Clustering, DBSCAN | Segmenting customers by buying behavior |
| **Dimensionality reduction** | Compress many features into fewer, keeping the important information | PCA, t-SNE | Reducing 100 features to 10 |
| **Association rule learning** | Find items that occur together | Apriori, Eclat | "People who buy bread often buy butter" |
| **Anomaly detection** | Find unusual examples | Isolation Forest, DBSCAN | Spotting fraudulent transactions |

### Evaluation

There is no answer key, so there is no simple accuracy. Results are judged with measures such as the **silhouette score** or by **inspecting whether the groups make sense** to a human.

### Strength and limit

It needs no labels and can reveal patterns nobody anticipated. But the results are harder to evaluate and may not match what you wanted.

---

## 5. Semi-Supervised Learning

### Concept

The model learns from a **small amount of labeled data and a large amount of unlabeled data**. The labeled examples guide the learning, and the unlabeled ones help the model understand the overall shape of the data.

**Common approach (pseudo-labeling):**
1. Train a model on the small labeled set.
2. Use it to guess labels for the unlabeled data.
3. Keep the confident guesses and add them to the training set.
4. Retrain.

**Example:** A hospital has millions of X-rays but only a few thousand diagnosed by doctors. Labeling is costly, so semi-supervised learning uses both.

**Why it matters:** it gets close to supervised accuracy at a fraction of the labeling cost.

---

## 6. Self-Supervised Learning

### Concept

The system **creates its own labels from the data**, by hiding one part of an example and learning to predict it from the rest. No human labeling is needed.

| Data | Hidden part | The model learns to |
|---|---|---|
| Text | The next word, or a masked word | Predict it from the surrounding text |
| Images | A masked patch | Fill in the missing piece |
| Audio | A short segment | Predict it from the neighboring sound |

**Example:** "The cat sat on the ___". The data itself supplies the answer ("mat"), so a huge amount of text becomes training data.

**Why it matters:** this is how modern large language models are trained. It is technically a form of supervised learning (there are labels), but the labels come from the data itself. It is often grouped with unsupervised learning because humans do not provide them.

---

## 7. Reinforcement Learning

### Concept

An **agent** interacts with an **environment**, takes **actions**, and receives **rewards** or penalties. It learns a strategy (called a **policy**) that maximizes the **total reward over time**.

### The loop

```
Agent observes the state  →  chooses an action  →  environment responds
        ↑                                                   ↓
        └────────── new state + reward ←───────────────────┘
```

| Part | Meaning | Chess example |
|---|---|---|
| **State** | The current situation | The board position |
| **Action** | A choice the agent can make | Moving a piece |
| **Reward** | Feedback on the action | +1 for winning, −1 for losing |
| **Policy** | The agent's strategy | Which move to pick in each position |

### Key ideas

- **Trial and error:** there is no answer key. The agent discovers good actions by trying them.
- **Delayed reward:** a move may only be judged good or bad many steps later, when the game ends.
- **Exploration vs exploitation:** the agent must balance trying new actions (explore) with repeating the best-known ones (exploit).

### Algorithms

Q-Learning, SARSA, Deep Q-Networks (DQN), Policy Gradient methods.

### Examples

Game-playing programs, robots learning to walk, self-driving decisions, ad and recommendation strategies, and resource scheduling.

---

## 8. Comparison

| | Supervised | Unsupervised | Semi-supervised | Self-supervised | Reinforcement |
|---|---|---|---|---|---|
| **Data** | Labeled | Unlabeled | Few labels + many unlabeled | Unlabeled (labels made from the data) | No dataset; interaction with an environment |
| **Feedback** | Correct answers | None | Some correct answers | Hidden part of the data | Rewards and penalties |
| **Goal** | Predict labels | Find structure | Predict with fewer labels | Learn useful representations | Maximize total reward |
| **Typical tasks** | Regression, classification | Clustering, dimensionality reduction | Classification with scarce labels | Language and image pretraining | Games, robotics, control |
| **Example algorithms** | Linear Regression, Random Forest, XGBoost | K-Means, PCA | Pseudo-labeling | Next-word prediction | Q-Learning |
| **Evaluation** | Easy (known answers) | Harder | Like supervised | Via downstream tasks | Total reward earned |

---

## 9. One Business, Three Problems

Take an online store with customer data.

| Question | Type | Why |
|---|---|---|
| "Which customers will leave next month?" (history says who left) | **Supervised (classification)** | The past outcomes are known labels |
| "How much will each customer spend next month?" | **Supervised (regression)** | The target is a number |
| "What natural groups of customers do we have?" | **Unsupervised (clustering)** | No labels, we want hidden groups |
| "Which discount should we show each visitor to maximize sales?" | **Reinforcement** | The system tries offers and learns from the sales that follow |

---

## 10. How to Choose

```
Do you have labeled data?
├── Yes, plenty            → Supervised
│     ├── Predict a number?   → Regression
│     └── Predict a category? → Classification
├── Yes, but very little   → Semi-supervised
├── No labels              → Unsupervised (find groups, reduce features, detect outliers)
├── Can create labels from the data itself → Self-supervised
└── Learning from actions and rewards      → Reinforcement
```

---

## 11. Another Way to Classify: Batch vs Online Learning

Models can also be grouped by **how they receive data**.

| | Batch (offline) | Online (incremental) |
|---|---|---|
| **How it learns** | Trains on all the data at once, then is deployed | Learns continuously from small chunks as data arrives |
| **Updating** | Retrain from scratch with new data | Update on the fly |
| **Suits** | Stable problems, moderate data | Streaming data, changing patterns, huge datasets |
| **Example** | Most scikit-learn models | Stock or news recommendation streams |

Instance-based vs model-based learning (the previous topic) is a third way of classifying.

---

## 12. Phase 4 Map

| Phase 4 topic | Type |
|---|---|
| Linear, Multiple Linear, Polynomial Regression | Supervised (regression) |
| Logistic Regression, KNN, Naive Bayes, SVM | Supervised (classification) |
| Decision Tree, Random Forest | Supervised (both) |
| Gradient Boosting, XGBoost | Supervised (both) |
| K-Means, Hierarchical Clustering, DBSCAN | Unsupervised (clustering) |
| PCA | Unsupervised (dimensionality reduction) |

Most of this phase is supervised learning, with the unsupervised part covering clustering and PCA.

---

## 13. Summary

- ML types differ in **the feedback the learner receives**.
- **Supervised:** learns from labeled data. Regression predicts numbers, classification predicts categories.
- **Unsupervised:** finds structure in unlabeled data (clustering, dimensionality reduction, association, anomaly detection).
- **Semi-supervised:** a few labels plus many unlabeled examples.
- **Self-supervised:** creates its own labels from the data, as in language models.
- **Reinforcement:** an agent learns by trial and error to maximize reward.
- Choose by asking what data you have and what you want to predict or discover.

---
