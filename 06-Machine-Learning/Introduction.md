# Introduction to Machine Learning

## Contents

- [Part 1: Detailed Introduction](#part-1-detailed-introduction)
- [Part 2: Lesson 1, Machine Learning Explained Slowly](#part-2-lesson-1-machine-learning-explained-slowly)

---

# Part 1: Detailed Introduction

## 1. What is Machine Learning?

Machine learning is the field of study that gives computers the ability to learn from data and improve with experience, without being explicitly programmed for every rule. Tom Mitchell's classic definition states it precisely:

> A program learns from experience **E** with respect to task **T** and performance measure **P**, if its performance at T, as measured by P, improves with E.

**Example:** For a spam filter, the task (T) is classifying emails, the experience (E) is a set of labeled emails, and the performance (P) is the percentage classified correctly.

## 2. Traditional Programming vs. Machine Learning

| | Traditional programming | Machine learning |
|---|---|---|
| **Input** | Data + Rules | Data + Answers |
| **Output** | Answers | Rules (a trained model) |
| **Approach** | Human writes the logic | Algorithm discovers the logic |
| **Best for** | Well-defined, stable problems | Complex patterns too hard to hand-code |

## 3. Why Machine Learning Matters

- **Rules are too complex to write:** recognizing a face or understanding speech
- **Rules change constantly:** fraud patterns evolve, so models can be retrained
- **Scale:** it finds patterns in millions of records no human could inspect
- **Personalization:** recommendations tailored to each user

## 4. How a Model Learns (Intuition)

1. The model starts with random or default parameters.
2. It makes predictions on training data.
3. A **loss function** measures how wrong the predictions are.
4. An **optimizer** (like gradient descent) adjusts the parameters to reduce the loss.
5. This repeats until performance stops improving.
6. The model is tested on unseen data to check it generalizes.

## 5. Applications

- **Healthcare:** disease detection from scans
- **Finance:** fraud detection, credit scoring
- **E-commerce:** product recommendations
- **Transportation:** self-driving systems, route prediction
- **Language:** translation, chatbots, voice assistants
- **Agriculture:** crop disease detection, yield forecasting

## 6. AI vs. ML vs. DL

These three are **nested**: Deep Learning is a subset of Machine Learning, which is a subset of Artificial Intelligence.

**Artificial Intelligence (AI)** is the broadest term: any technique that enables machines to mimic human intelligence, including reasoning, planning, perception, and decision-making. It includes rule-based expert systems, search algorithms (like chess engines), and ML.

**Machine Learning (ML)** is a subset of AI where systems learn patterns from data rather than following hand-coded rules.

**Deep Learning (DL)** is a subset of ML that uses **multi-layered neural networks** to learn hierarchical representations of data automatically. It powers image recognition, speech recognition, and large language models.

### Comparison Table

| Aspect | AI | ML | DL |
|---|---|---|---|
| **Scope** | Broadest | Subset of AI | Subset of ML |
| **Goal** | Mimic human intelligence | Learn patterns from data | Learn complex representations with deep neural networks |
| **Approach** | Rules, logic, search, or learning | Statistical algorithms | Multi-layer neural networks |
| **Data needed** | Varies (rule-based systems need none) | Moderate (hundreds to millions of rows) | Very large (often millions of samples) |
| **Feature engineering** | Manual (in rule-based systems) | Usually manual; humans choose features | Automatic; the network learns features |
| **Hardware** | Standard CPU | CPU is usually enough | GPUs/TPUs strongly preferred |
| **Training time** | Varies | Minutes to hours | Hours to weeks |
| **Interpretability** | High for rule-based | Medium to high | Low ("black box") |
| **Best for** | General intelligent behavior | Structured/tabular data | Images, audio, text, video |
| **Examples** | Chess engine, expert systems | Spam filter, price prediction, churn model | Face recognition, ChatGPT-style LLMs, self-driving vision |

### Same Problem, Three Views: Detecting Cats in Photos

- **AI (rule-based):** A programmer writes rules such as "has pointy ears, whiskers, fur." This is brittle and fails easily.
- **ML:** An engineer hand-extracts features (edges, colors, shapes) and trains a classifier like SVM on them.
- **DL:** A CNN is fed raw pixels and learns edges, then textures, then shapes, then "cat" on its own.

## 7. Types of Machine Learning (Quick Recap)

| Type | Data | Example |
|---|---|---|
| **Supervised** | Labeled | House price prediction |
| **Unsupervised** | Unlabeled | Customer clustering |
| **Semi-supervised** | Few labels, many unlabeled | Medical image labeling |
| **Self-supervised** | Labels generated from the data itself | Next-word prediction in LLMs |
| **Reinforcement** | Rewards from an environment | Game-playing agents |

## 8. When to Use Which?

- **Small or tabular data, need explainability:** classical ML (Phase 4 topics: regression, trees, XGBoost)
- **Images, audio, or text with lots of data:** deep learning
- **Clear fixed rules, no data:** traditional programming or rule-based AI

## 9. Key Takeaway

> **AI** is the goal, **ML** is the method of learning from data, and **DL** is a powerful ML technique using deep neural networks.

For the Phase 4 syllabus, you will focus on **classical ML**, which remains the best choice for most tabular business data and is the foundation for understanding deep learning later.

---

# Part 2: Lesson 1, Machine Learning Explained Slowly

Let's go step by step, like a classroom. Today's lesson covers what ML is, how it learns, and how AI, ML and DL differ. After that, I'll teach each Phase 4 algorithm the same way, one lesson at a time, so nothing feels rushed.

## Topic 1: What is Machine Learning?

Imagine teaching a child to recognize mangoes. You don't hand the child a rulebook saying "if yellow and oval and sweet-smelling, then mango." Instead, you show many mangoes and say "this is a mango" each time. After enough examples, the child recognizes mangoes, even ones they've never seen before.

Machine learning works the same way. Instead of a programmer writing every rule, we show the computer many **examples**, and it **figures out the rules by itself**.

**Traditional programming:** you give the computer *data + rules*, and it gives *answers*.
**Machine learning:** you give the computer *data + answers*, and it gives you the *rules* (called a **model**).

**A real example:** Suppose you want to detect spam emails. Writing rules by hand ("if it contains 'lottery', it's spam") fails, because spammers keep changing their words. With ML, you feed in 100,000 emails already labeled "spam" or "not spam." The algorithm discovers patterns on its own and keeps working even as you retrain it on new emails.

**The formal definition** (by Tom Mitchell) sounds scary but is simple: a program learns if it gets *better at a task* as it gains *more experience*. For the spam filter, the task is sorting emails, the experience is the labeled emails, and "better" means more emails sorted correctly.

### Check your understanding

1. In your own words, how is ML different from traditional programming?
2. Why would hand-written rules fail for recognizing faces?
3. For a model that predicts house prices, what are the task, the experience and the performance measure?

## Topic 2: How Does a Model Actually Learn?

Think of learning to throw darts. Your first throw misses the target. You see *how far off* you were, adjust your arm slightly, and throw again. After many throws, you hit the bullseye consistently.

A model learns in exactly this loop:

1. **Start with a guess.** The model begins with random settings (called *parameters* or *weights*).
2. **Make a prediction.** It predicts an answer for a training example.
3. **Measure the error.** A **loss function** tells us how wrong the prediction was, like measuring how far the dart landed from the bullseye.
4. **Adjust.** An **optimizer** (most famously *gradient descent*) nudges the parameters in the direction that reduces the error.
5. **Repeat** thousands of times until the error stops shrinking.

Finally, we test the model on **new data it has never seen**. This matters a lot. A student who memorizes last year's exam answers scores perfectly on that exam but fails a new one. Memorizing is called **overfitting**, and avoiding it is one of the central skills in ML.

### Check your understanding

1. What does a loss function measure?
2. What is the job of the optimizer?
3. Why do we test on data the model has never seen?
4. Explain overfitting using a student and an exam.

## Topic 3: The Types of Machine Learning

Think of three different kinds of teachers.

**Supervised learning** is like a teacher who gives you problems *with the answer key*. Each training example has a correct label, and you learn to match it. It splits into two kinds:

- **Regression:** predicting a *number* (house price, temperature).
- **Classification:** predicting a *category* (spam or not spam, disease or healthy).

**Unsupervised learning** is like being handed a box of mixed buttons with no instructions. You sort them into piles by similarity, say by color or size. The algorithm finds hidden groups or structure in data that has *no labels*. Example: grouping customers by shopping behavior.

**Reinforcement learning** is like training a dog with treats. The agent tries actions, gets rewards for good ones and penalties for bad ones, and slowly learns the best strategy. Example: a program learning to play chess or a robot learning to walk.

There are two more worth knowing: **semi-supervised** (a few labeled examples plus many unlabeled ones) and **self-supervised** (the data creates its own labels, like predicting the next word in a sentence, which is how large language models are trained).

**Good news:** your entire Phase 4 syllabus is **supervised learning**.

### Check your understanding

1. Is predicting tomorrow's temperature regression or classification? Why?
2. Is "will this customer leave: yes or no?" regression or classification?
3. Which type of learning has no labels?
4. Which type uses rewards and penalties?

## Topic 4: AI vs ML vs DL

These three words are often used as if they mean the same thing. They don't. The easiest way to remember is **Russian nesting dolls**: each one sits inside the bigger one.

> **AI ⊃ ML ⊃ DL**

### Artificial Intelligence (AI), the biggest doll

AI means *any technique that makes a machine behave intelligently*. This includes old-fashioned approaches that involve **no learning at all**. A chess program that follows hand-written rules and searches possible moves is AI. A medical expert system built from a doctor's "if-then" rules is AI.

### Machine Learning (ML), the middle doll

ML is the part of AI where the machine **learns from data** instead of following rules written by a human. Spam filters, price predictors and recommendation systems are ML. Importantly, in classical ML, a *human still decides which features matter*. To predict house prices, an engineer chooses features like area, number of rooms and location.

### Deep Learning (DL), the smallest doll

DL is the part of ML that uses **neural networks with many layers** (hence "deep"). Its special power is that it **discovers the features by itself**. Give a deep network raw pixels of cat photos, and early layers learn to detect edges, middle layers learn shapes like ears and eyes, and later layers learn "this is a cat." This is why DL dominates images, speech and language. The cost is that it needs huge amounts of data and powerful hardware (GPUs).

### Side-by-side comparison

| | AI | ML | DL |
|---|---|---|---|
| **Simple meaning** | Machines acting smart | Machines learning from data | Learning with deep neural networks |
| **Relationship** | Biggest field | Inside AI | Inside ML |
| **Who picks features?** | A human writes the rules | Usually a human | The network itself |
| **Data needed** | Can be none | Small to medium | Very large |
| **Hardware** | Ordinary computer | Ordinary computer | Usually GPUs |
| **Easy to explain?** | Often yes | Often yes | Hard ("black box") |
| **Example** | Rule-based chess engine | Spam filter | Face recognition |

### One problem, three approaches: spotting cats in photos

- **AI (rules):** A programmer writes "pointy ears + whiskers = cat." This breaks the moment a cat is photographed from behind.
- **ML:** An engineer extracts features (edges, colors, textures) and trains a classifier on them. Better, but the human did the hard work of choosing features.
- **DL:** A neural network studies thousands of photos and works out everything itself. Most accurate, but data-hungry.

### Which should you use?

For **tabular data** (rows and columns, like spreadsheets, business records, bank data), classical ML such as XGBoost is usually best, faster and easier to explain. For **images, audio and text**, deep learning usually wins. That's why we master classical ML first: it is the foundation, and it is what most companies use daily on structured data.

### Check your understanding

1. Draw the nesting-doll picture from memory and label the three layers.
2. Give one example of AI that is *not* machine learning.
3. In classical ML, who chooses the features? In DL?
4. You have a 5,000-row spreadsheet of customer data. Would you start with classical ML or deep learning, and why?
5. Why is deep learning called a "black box"?

## Lesson Summary

- ML = learning rules from examples instead of writing them by hand.
- Learning is a loop: predict, measure error, adjust, repeat.
- Always test on unseen data to catch overfitting.
- Supervised learning (regression and classification) is the focus of Phase 4.
- AI ⊃ ML ⊃ DL, like nesting dolls.

**Tip:** Try answering the questions on paper before moving on. If you send me your answers, I'll check them and explain anything you missed.
