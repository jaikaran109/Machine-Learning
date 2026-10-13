# How to Frame a Machine Learning Problem

> **Phase 4: Machine Learning, ML Foundations**
> How to turn a vague business goal into a clear ML task before writing any code.

---

## 1. The Big Idea

Many beginners open a notebook and start training a model straight away. In real projects, the hardest part comes **before** that: deciding **what exactly the model should predict, and how we will know it works**.

**Analogy (doctor and patient):** A good doctor does not hand out medicine as soon as you walk in. The doctor asks questions, checks what you already tried, runs tests, and only then prescribes. Framing is that first conversation, and a wrong frame means a perfect model for the wrong problem.

### The 7 steps

| # | Step | The question it answers |
|---|---|---|
| 1 | Business problem to ML problem | What does the business want, and what should the model predict? |
| 2 | Type of problem | Is it classification, regression, clustering, or something else? |
| 3 | Current solution | How is this solved today? |
| 4 | Getting data | What data do we need, and do we have it? |
| 5 | Metrics to measure | How will we know it worked? |
| 6 | Online vs batch | How should the model be trained and used? |
| 7 | Check assumptions | What are we taking for granted, and is it true? |

---

## 2. Key Terms in Plain Words

| Term | Meaning |
|---|---|
| **Business problem** | A goal the organization wants to achieve, such as more revenue. It says nothing about ML yet. |
| **ML problem** | The same goal rewritten as a prediction task with clear inputs and an output. |
| **Input (features)** | The information given to the model, such as a user's watch history. |
| **Output (label / target)** | The answer we want the model to predict. |
| **Baseline** | A simple reference solution that a new model must beat. |
| **Churn** | When a customer cancels or stops using a service. |
| **Engagement** | How actively users use a product, such as hours watched. |
| **Offline metric** | A score measured on stored data **before** launching the model. |
| **Online metric** | A score measured **after** launch, on real users. |
| **A/B test** | Showing the new system to one group of users (B) and the old one to another (A), then comparing the results. |
| **Assumption** | Something we treat as true without having proved it. |

---

## 3. Our Example: Netflix

Netflix earns money from subscriptions. We will frame one of its problems through all seven steps.

---

## 4. Step 1: Business Problem to ML Problem

**What to do:** start with the business goal, break it into smaller causes, and find a part that data can help with. Then ask whether ML is really needed.

**Netflix:**

1. **Business goal:** increase revenue.
2. **Break it down:** revenue comes from subscribers paying every month. Raising the price may push people away, so the safer path is to have **more subscribers who stay longer** (fewer cancellations).
3. **Find the cause:** people cancel when they feel they are not getting value, for example when they cannot find anything they want to watch.
4. **Refine the goal:** increase **engagement**, so that every user quickly finds something they enjoy.
5. **Idea:** show each user **personalized recommendations**.

| Business problem | ML problem |
|---|---|
| Increase revenue by keeping subscribers | **Given a user and their history, predict which titles they are most likely to enjoy, and show the best ones first.** |

**Is ML needed?** A rule like "show everyone the most popular titles" is easy but treats millions of users the same. With millions of users and thousands of titles, nobody can write personal rules by hand, which is where ML helps.

---

## 5. Step 2: Type of Problem

**What to do:** decide which family of ML problem this is.

| Family | Idea |
|---|---|
| **Supervised** | Learn from examples that have answers |
| **Unsupervised** | Find structure in data without answers |
| **Reinforcement** | Learn by trial and error from rewards |

Supervised problems split into **regression** (predict a number) and **classification** (predict a category).

**Netflix can be framed in several ways:**

| Framing | What the model predicts | Type |
|---|---|---|
| **Rating prediction** | The rating (1 to 5 stars) a user would give | Supervised, regression |
| **Watch prediction** | Whether the user will watch this title: yes or no (as a probability) | Supervised, classification |
| **Ranking** | The best order of titles for each user | Ranking (a recommendation problem) |
| **Taste groups** | Group users with similar taste | Unsupervised, clustering |

**A sensible choice:** predict the **probability that a user will watch a title** (classification), then **sort titles by that probability** to build the ranked list. The label comes straight from the logs: watched or not watched.

**Two common recommendation ideas:**

- **Collaborative filtering:** "people with similar taste to you liked this."
- **Content-based:** "this title is similar to ones you liked" (same genre, cast and so on).

---

## 6. Step 3: Current Solution

**What to do:** find out how the problem is solved today, even if it is not ML.

**Why it matters:**
- It gives a **baseline** to beat. If ML cannot beat a simple rule, it is not worth the cost.
- It shows what data already exists.
- It reveals what users and the business already accept.

**Netflix:** without ML personalization, the simplest solution is the **same lists for everyone**: "Trending now", "Most popular in your country", "Newly added", and rows by genre.

| | Current (baseline) | Proposed (ML) |
|---|---|---|
| **Who sees what** | Everyone sees similar rows | Each user sees personalized rows |
| **Built by** | Fixed rules and popularity counts | A trained model |

Our model must **clearly beat** the popularity list on the metrics in Step 5.

---

## 7. Step 4: Getting Data

**What to ask:**

1. What data do we need?
2. Do we already have it, and how much?
3. Does it include the **labels** (the answers)?
4. Is the quality good? Is it free of obvious bias?
5. Can we use it legally and respectfully (privacy and consent)?

**Netflix:**

| Data | Example | Role |
|---|---|---|
| **User activity** | Titles watched, when, for how long, whether finished | Features, and the source of the label |
| **Interactions** | Searches, thumbs up or down, ratings, additions to "My List" | Features and labels |
| **Context** | Device, time of day, day of the week | Features |
| **Title information** | Genre, cast, language, release year, description | Features |
| **Label** | "Watched" or "did not watch" | Output |

**Challenges to expect:**

- **Cold start:** a **new user** has no history, and a **new title** has no viewers yet, so the model has little to learn from.
- **Feedback loop:** users can only watch what they are shown, so the data is shaped by past recommendations.
- **Noisy labels:** a user may start a show and quit after five minutes.

---

## 8. Step 5: Metrics to Measure

**What to do:** decide how success will be measured, at three levels.

| Level | Measured | Netflix example |
|---|---|---|
| **Offline metrics** | On stored data before launch | Precision@k, recall, RMSE |
| **Online metrics** | On real users after launch | Play rate, watch hours, click-through rate |
| **Business metrics** | Over the long term | Churn (cancellations), retention, revenue |

**Offline metric in plain words (precision@k):** of the top **k** titles recommended, how many did the user actually watch?

```
Model recommends 5 titles. The user later watches 2 of them.
Precision@5 = 2 / 5 = 0.4
```

**Online testing with an A/B test:**

```
Users are split randomly
Group A → old recommendations (baseline)
Group B → new ML recommendations
Compare watch hours and cancellations between the groups
```

**Important lesson:** a better offline score does not guarantee a better business result. In the well-known **Netflix Prize** contest, teams competed to predict ratings more accurately. Netflix has said it did not put the full winning solution into production, because the engineering cost was too high compared with the gain. So always connect the metric to the real goal: engagement and fewer cancellations.

---

## 9. Step 6: Online vs Batch

**What to do:** decide how the model will learn and be updated. (Recall the earlier note: **batch** trains on a stored dataset and retrains periodically, while **online** updates continuously as data arrives.)

| Question | Netflix situation |
|---|---|
| How fast does data change? | New titles are added and tastes change, but not every second |
| How costly is training? | Models are large, so training constantly is expensive |
| How fresh must predictions be? | Recent viewing should affect what is shown |

**A reasonable design:**

- Retrain the main model in **batches** on a regular schedule (for example daily).
- Add **quick adjustments** based on what the user watched very recently.

Many real systems **mix both**.

**Extra meaning of "online vs batch":** it can also describe **when predictions are made**. Batch predictions are computed ahead of time and stored. Online predictions are computed live when the user opens the app. Systems often combine them.

---

## 10. Step 7: Check Assumptions

**What to do:** list what you are taking for granted, and test the risky ones before building.

| Assumption | Why it may be wrong | How to check |
|---|---|---|
| **Watching means liking** | A user may watch out of boredom or let autoplay run | Use how much was watched, thumbs up or down, and rewatching |
| **Past behavior predicts future taste** | Tastes change, and one account may be shared by several people | Compare older and newer behavior, and use separate profiles |
| **Better recommendations reduce cancellations** | Users may cancel for price or other reasons | Run an A/B test and track churn |
| **Our data represents all users** | Users only choose from what they were shown | Look at new users and rarely shown titles |
| **Model output is usable** | The app needs a ranked list, not a single score | Confirm the format with the product team |

If an assumption is wrong, the whole frame can fail, so it is much cheaper to find out now than after building the system.

---

## 11. The Framing Sheet (Netflix)

| Step | Answer |
|---|---|
| **1. Business to ML** | Keep subscribers by increasing engagement. Predict which titles each user will enjoy, then rank them. |
| **2. Type** | Supervised classification (watch or not), then rank by probability. |
| **3. Current solution** | Same popular lists for everyone. This is the baseline. |
| **4. Data** | Watch history, interactions, context, title details. Label: watched or not. Watch for cold start. |
| **5. Metrics** | Offline: precision@k. Online: watch hours, play rate. Business: churn. Confirm with an A/B test. |
| **6. Online vs batch** | Regular batch training plus quick recent-activity updates. |
| **7. Assumptions** | Watching means liking, past predicts future, better recommendations reduce churn. Test each one. |

---

## 12. Summary

- Framing means turning a business goal into a precise ML task **before** modeling.
- The seven steps: business problem to ML problem, type of problem, current solution, getting data, metrics, online vs batch, check assumptions.
- Always find the **baseline** (current solution) and measure against it.
- Use offline metrics before launch, online metrics (with A/B tests) after launch, and business metrics for the real goal.
- Expect data problems such as cold start and feedback loops.
- Write down your assumptions and test the risky ones early.

---

## 13. Practice Questions

1. Why should you frame the problem before choosing an algorithm?
2. What is the difference between a business problem and an ML problem? Use Netflix as the example.
3. Name three different ways Netflix could frame its recommendation problem, with the ML type of each.
4. Why is knowing the current solution useful even when it is not ML?
5. Give two data sources Netflix could use, and say which one provides the label.
6. What is the cold start problem?
7. A model recommends 5 titles, and the user watches 3 of them. What is precision@5?
8. What is the difference between an offline metric and an online metric? Give an example of each.
9. What is an A/B test, and why is it used?
10. Why can a model with a better offline score still fail to help the business?
11. Give two assumptions Netflix makes, and how you could check each.
12. Frame your **placement prediction** project in the seven steps.

### Answers

1. Otherwise you may build a perfect model for the wrong question, wasting time and money.
2. Business problem: keep subscribers and grow revenue. ML problem: predict which titles each user will enjoy and rank them.
3. Rating prediction (regression), watch prediction (classification), ranking, or user clustering (unsupervised).
4. It gives a baseline to beat and shows what data and processes already exist.
5. Watch history and device or time of day, for example. The label comes from the watch history: watched or not watched.
6. A new user or title has no data, so the model has little to learn from.
7. `3 / 5 = 0.6`.
8. Offline is measured on stored data before launch (precision@k). Online is measured on real users after launch (watch hours).
9. Split users randomly into an old-system group and a new-system group, then compare results. It shows whether the change really caused an improvement.
10. Offline accuracy may not reflect real engagement, and the model may be too costly or slow to run (as with the Netflix Prize).
11. For example, "watching means liking" (check completion and thumbs ratings), and "better recommendations reduce churn" (check with an A/B test).
12. Sample answer:

| Step | Placement prediction |
|---|---|
| Business to ML | A college wants to know which students may struggle to get placed. Predict whether a student gets placed. |
| Type | Supervised, binary classification |
| Current solution | A placement officer's judgment or a simple cutoff on marks |
| Data | The Kaggle student dataset: academic details as features, placed or not as the label |
| Metrics | Accuracy, precision, recall |
| Online vs batch | Batch, retrained when a new batch of students arrives |
| Assumptions | Past batches resemble future ones, and the small dataset is representative |