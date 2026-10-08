> The main careers that work with data, what each one does, and the skills each one needs.

---

## 1. The Big Idea

Data does not turn into business value on its own. It has to be collected, stored, cleaned, analyzed, modeled, deployed and maintained, and different people specialize in different parts of that journey.

**Analogy (a restaurant chain):**

| Restaurant | Data world | Role |
|---|---|---|
| Supplier network and kitchen storage that keep ingredients flowing | Pipelines and storage that keep data flowing | **Data Engineer** |
| Manager reporting which dishes sold best last month | Reports and dashboards on past performance | **Data Analyst** |
| Chef inventing a new dish predicted to be popular | Models that predict or discover something new | **Data Scientist** |
| Team making that dish reliably in every outlet, every day | Putting a model into production | **ML Engineer** |

Job titles overlap and differ between companies, so treat this as a guide to the **type of work** and **skills**, not strict boundaries.

---

## 2. Types of Skills

Every role mixes four kinds of skills. Each role section below lists its skills under these headings.

| Skill type | Meaning | Examples |
|---|---|---|
| **Technical skills** | Knowing how to do the work | SQL, Python, building pipelines, training models |
| **Tools** | The software and platforms used | Excel, Power BI, Spark, Docker, scikit-learn |
| **Analytical / math skills** | Reasoning with numbers and logic | Statistics, probability, linear algebra, problem solving |
| **Soft skills** | Working with people and ideas | Communication, storytelling, teamwork, curiosity, business sense |

> **Key point:** tools change every few years, but **fundamentals** (SQL, statistics, problem solving, communication) stay valuable in almost every role.

---

## 3. Key Definitions

| Term | Definition | In simple words |
|---|---|---|
| **Data pipeline** | An automated sequence that moves data from sources to where it is used. | A conveyor belt for data. |
| **ETL / ELT** | Extract, Transform, Load: pulling data from sources, cleaning it, and storing it. | Collect, clean, store. |
| **Data warehouse** | A central database organized for analysis and reporting. | A tidy library of company data. |
| **Data lake** | Storage for large amounts of raw data in any format. | A big storeroom of raw data. |
| **Dashboard** | An interactive page of charts and key numbers. | A control panel for the business. |
| **KPI** | Key Performance Indicator: a number that tracks success. | The score the business watches. |
| **Model** | A system trained on data to predict or discover something. | The learned rule. |
| **Deployment** | Making a model available for real use. | Putting it to work. |
| **MLOps** | Practices for deploying, monitoring and maintaining ML models. | Keeping models healthy in production. |

---

## 4. Data Analyst

### Definition

A **Data Analyst** examines data to **describe what happened and why**, and presents findings that help people make decisions.

### Type of work

Looks at **past and current** data. Mostly descriptive and diagnostic analysis.

### Typical tasks

- Write SQL queries to pull data from databases
- Clean and organize data
- Calculate statistics, trends and comparisons
- Build dashboards and reports
- Explain findings to non-technical teams

### Key question

*"What happened, and why?"*

### Example

Sales dropped 12% last month. The analyst finds the drop is concentrated in one region and one product category, and reports it with charts.

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | SQL (joins, aggregations), data cleaning, data visualization, basic Python or R, A/B test basics |
| **Tools** | Excel, Power BI or Tableau, SQL databases, Google Sheets, Jupyter |
| **Analytical / math** | Descriptive statistics, hypothesis testing basics, trend and root-cause analysis, attention to detail |
| **Soft** | Data storytelling, clear presentation, business curiosity, stakeholder communication |

### Output

Reports, dashboards, insights and recommendations.

---

## 5. Business Analyst

### Definition

A **Business Analyst** connects business needs with data and technology. They define **what problem should be solved** and what a solution must do.

### Type of work

Less about deep data work and more about **requirements, processes and decisions**. Uses data as one input.

### Typical tasks

- Gather requirements from stakeholders
- Analyze business processes and find inefficiencies
- Define KPIs and success measures
- Work with technical teams to deliver solutions
- Present recommendations to management

### Key question

*"What does the business need, and how do we get it?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Requirements gathering, process modeling (flowcharts, BPMN), basic SQL, cost-benefit analysis, documentation |
| **Tools** | Excel, Jira, Visio or Lucidchart, a BI tool, PowerPoint |
| **Analytical / math** | Problem solving, root-cause analysis, basic statistics, KPI design |
| **Soft** | Communication, negotiation, stakeholder management, facilitation, domain knowledge |

### Output

Requirement documents, process maps, KPI definitions, recommendations.

---

## 6. BI Developer / BI Analyst

### Definition

A **Business Intelligence (BI) Developer** builds and maintains the **reporting systems** that let the organization monitor performance continuously.

### Type of work

Focuses on **repeatable, automated reporting** rather than one-off analysis.

### Typical tasks

- Design data models for reporting
- Build and refresh dashboards
- Write complex SQL and calculated measures
- Ensure reports are accurate and fast
- Manage access to reports

### Key question

*"How do we let everyone see the key numbers, always up to date?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Advanced SQL, data modeling (star schema), dashboard design, report performance tuning, basic data warehousing |
| **Tools** | Power BI (DAX), Tableau, SSRS, a data warehouse, Excel |
| **Analytical / math** | KPI definition, basic statistics, accuracy checking and validation |
| **Soft** | Visual design sense, understanding user needs, attention to detail, communication |

### Output

Dashboards and automated reports.

---

## 7. Data Engineer

### Definition

A **Data Engineer** designs, builds and maintains the **systems that collect, store and move data**, so that clean, reliable data is available to everyone else.

### Type of work

**Infrastructure and software engineering for data.** Without this work, analysts and scientists have nothing dependable to work with.

### Typical tasks

- Build data pipelines (ETL/ELT)
- Design and manage data warehouses and data lakes
- Process large datasets (batch and streaming)
- Ensure data quality, security and reliability
- Optimize performance and cost

### Key question

*"How do we get clean, reliable data to the people who need it?"*

### Example

Collect data from the website, app and payment system every hour, clean it, and load it into the warehouse for analysts.

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Strong SQL, Python (or Scala or Java), ETL/ELT design, data modeling, batch and streaming processing, databases (SQL and NoSQL), data quality testing, Linux |
| **Tools** | Apache Spark, Airflow, Kafka, dbt, Docker, Git, cloud platforms (AWS, Azure, GCP), warehouses (Snowflake, BigQuery, Redshift) |
| **Analytical / math** | Algorithms and data structures, systems thinking, performance optimization, debugging |
| **Soft** | Reliability and ownership, documentation, collaboration with analysts and scientists |

### Output

Pipelines, databases, warehouses and clean datasets.

---

## 8. Analytics Engineer

### Definition

An **Analytics Engineer** sits between data engineering and analysis. They transform raw warehouse data into **clean, well-documented, trustworthy tables** that analysts can use directly.

### Typical tasks

- Write SQL transformations and tests
- Build reusable data models
- Document data definitions
- Apply software practices (version control, testing) to analytics

### Key question

*"How do we make the data easy and safe for analysts to use?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Advanced SQL, data modeling, data testing, documentation, version control workflows, basic Python |
| **Tools** | dbt, Git, a cloud warehouse (Snowflake, BigQuery), a BI tool |
| **Analytical / math** | Business logic translation, data quality reasoning |
| **Soft** | Working with both engineers and analysts, clear definitions and documentation |

### Output

Tested, documented data models.

---

## 9. Data Scientist

### Definition

A **Data Scientist** uses statistics and machine learning to **predict what will happen, or to discover patterns**, and turns these into actionable insight.

### Type of work

Goes beyond describing the past. Builds **predictive and exploratory models** and runs experiments.

### Typical tasks

- Frame business problems as ML problems
- Explore and prepare data, and engineer features
- Train, evaluate and tune models (regression, classification, clustering)
- Run statistical tests and A/B tests
- Explain results and trade-offs to stakeholders

### Key question

*"What will happen next, and what should we do about it?"*

### Example

Build a churn model that scores every customer's chance of leaving, so the retention team can contact the riskiest ones.

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Python, SQL, data cleaning, feature engineering, supervised and unsupervised ML, model evaluation and tuning, experiment design, basic deployment knowledge |
| **Tools** | pandas, NumPy, scikit-learn, XGBoost, Matplotlib or Seaborn, Jupyter, Git, a deep learning library (later) |
| **Analytical / math** | Statistics and probability, linear algebra, calculus basics (gradients), hypothesis testing, critical thinking |
| **Soft** | Problem framing, explaining models simply, storytelling, curiosity, business understanding |

### Output

Models, experiments, forecasts and recommendations.

> **This Phase 4 is mainly Data Scientist territory**, and the four projects (house price, student performance, churn, credit risk) are typical data science tasks.

---

## 10. Machine Learning Engineer

### Definition

A **Machine Learning Engineer** takes models and turns them into **reliable, scalable software** that runs in the real world.

### Type of work

Closer to **software engineering** than data science. A model in a notebook is not a product, and the ML engineer bridges that gap.

### Typical tasks

- Convert notebook code into production-quality code
- Build training and prediction pipelines
- Deploy models as APIs or batch jobs
- Optimize speed, memory and cost
- Test, version and monitor models

### Key question

*"How do we make this model work reliably for millions of users?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Strong Python, software engineering (testing, clean code, design), ML algorithms, deep learning, API development, model optimization, system design |
| **Tools** | scikit-learn, PyTorch or TensorFlow, FastAPI or Flask, Docker, Kubernetes, Git, CI/CD, cloud platforms |
| **Analytical / math** | Linear algebra, statistics, optimization, performance profiling |
| **Soft** | Collaboration with data scientists and software teams, ownership of production systems, documentation |

### Output

Production ML systems and services.

---

## 11. MLOps Engineer

### Definition

An **MLOps Engineer** builds the tooling and processes for the **full life of an ML model**: automated training, deployment, monitoring and retraining.

### Typical tasks

- Automate training and deployment pipelines
- Track experiments and model versions
- Monitor models for drift and failures
- Manage infrastructure for ML workloads
- Trigger retraining when performance drops

### Key question

*"How do we keep models running, accurate and up to date?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | DevOps practices, CI/CD, infrastructure as code, containerization, Python scripting, monitoring and logging, understanding of the ML life cycle |
| **Tools** | MLflow, Docker, Kubernetes, Terraform, Airflow or Kubeflow, Git, Prometheus or Grafana, cloud platforms |
| **Analytical / math** | Basic ML and statistics (to interpret drift and metrics), troubleshooting, systems thinking |
| **Soft** | Reliability mindset, cross-team collaboration, incident handling, documentation |

### Output

Automated ML pipelines and monitoring systems.

---

## 12. AI Engineer

### Definition

An **AI Engineer** builds **applications on top of AI models**, especially large language models and other pre-trained models, rather than training models from scratch.

### Typical tasks

- Integrate LLMs and other AI APIs into products
- Build chatbots, assistants and search systems
- Design prompts and retrieval pipelines
- Evaluate and improve AI feature quality and safety

### Key question

*"How do we turn powerful pre-trained AI into a useful product?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Python, API integration, prompt design, retrieval and embeddings, evaluation of AI outputs, backend development, basic ML and NLP concepts |
| **Tools** | LLM provider APIs, vector databases, LLM frameworks, FastAPI, Docker, cloud platforms |
| **Analytical / math** | Evaluation design, debugging non-deterministic systems, basic statistics |
| **Soft** | Product thinking, responsible and safe AI judgment, fast learning, user empathy |

### Output

AI-powered applications and features.

---

## 13. Research Scientist (ML / AI)

### Definition

A **Research Scientist** develops **new algorithms and methods** and advances the state of the art, often publishing papers.

### Typical tasks

- Study the literature and propose new ideas
- Design and run experiments
- Develop new model architectures and training methods
- Publish results

### Key question

*"Can we build a fundamentally better method?"*

### Skills Required

| Skill type | Skills |
|---|---|
| **Technical** | Deep learning and ML theory, experiment design, strong programming, reproducible research, reading and implementing papers |
| **Tools** | PyTorch or JAX, GPUs and clusters, experiment trackers, LaTeX |
| **Analytical / math** | Advanced linear algebra, calculus, probability, optimization, rigorous statistics |
| **Soft** | Creativity, persistence, scientific writing, presenting research, openness to being wrong |

### Output

New methods, papers and prototypes. Often requires a master's or PhD.

---

## 14. Other Data Roles

| Role | Definition and work | Key skills |
|---|---|---|
| **Statistician** | Designs studies and experiments and applies rigorous statistical methods to draw reliable conclusions. Common in healthcare, research and government. | Advanced statistics, experimental design, R or Python, clear reporting |
| **Data Architect** | Designs the overall blueprint of how an organization stores, integrates and governs data. A senior, planning-focused role. | Data modeling, database and cloud architecture, security, big-picture thinking |
| **Database Administrator (DBA)** | Keeps databases running, secure, fast and backed up. | SQL, database tuning, backup and recovery, security, monitoring |
| **Data Governance / Data Steward** | Defines and enforces rules on data quality, ownership, privacy and compliance. | Data quality management, privacy and compliance knowledge, policy writing, communication |
| **Data Product Manager** | Decides what data and ML products to build, prioritizes them and links them to business value. | Product management, data literacy, prioritization, stakeholder management, communication |
| **Quantitative Analyst (Quant)** | Applies mathematics and statistics to financial markets and risk. | Advanced math and probability, Python or C++, finance knowledge, modeling |
| **Computer Vision / NLP Engineer** | Specializes in images and video, or in language and text. | Deep learning, PyTorch or TensorFlow, image or text processing, model optimization |

---

## 15. Comparison

| Role | Main question | Looks at | Main output | Core tools | ML depth | Coding depth |
|---|---|---|---|---|---|---|
| **Data Analyst** | What happened and why? | Past and present | Reports, dashboards | SQL, Excel, BI tools | Low | Low to medium |
| **Business Analyst** | What does the business need? | Processes, requirements | Requirements, recommendations | Excel, SQL | Low | Low |
| **BI Developer** | How do we monitor performance continuously? | Reporting needs | Automated dashboards | SQL, Power BI, Tableau | Low | Medium |
| **Data Engineer** | How do we deliver reliable data? | Data systems | Pipelines, warehouses | Python, SQL, Spark, Airflow | Low | High |
| **Analytics Engineer** | How do we make data analysis-ready? | Warehouse data | Clean data models | SQL, dbt | Low | Medium |
| **Data Scientist** | What will happen, and what should we do? | Patterns, future | Models, insights | Python, scikit-learn, statistics | High | Medium to high |
| **ML Engineer** | How do we run models at scale? | Production systems | Deployed ML services | Python, Docker, cloud | High | High |
| **MLOps Engineer** | How do we keep models healthy? | ML lifecycle | Automated pipelines | MLflow, Kubernetes | Medium | High |
| **AI Engineer** | How do we build products with AI models? | AI applications | AI features | LLM APIs, Python | Medium | High |
| **Research Scientist** | Can we create a better method? | New algorithms | Papers, prototypes | PyTorch, advanced math | Very high | Medium to high |

---

## 16. How the Roles Work Together

```
Data Sources (app, website, sensors, sales)
        ↓
Data Engineer         → collects, cleans and stores data (pipelines, warehouse)
        ↓
Analytics Engineer    → turns raw tables into clean, documented data models
        ↓
   ┌────┴─────────────────────────┐
   ↓                              ↓
Data Analyst / BI Developer   Data Scientist
(reports, dashboards)         (builds predictive models)
   ↓                              ↓
Business decisions            ML Engineer → MLOps Engineer
                              (deploys and maintains the model)
                                  ↓
                              Business application (e.g. churn alerts)
```

### Example: the customer churn project

| Step | Who | Work |
|---|---|---|
| 1 | **Business Analyst** | Defines the goal: reduce churn, and what success means |
| 2 | **Data Engineer** | Builds the pipeline bringing customer, billing and support data into the warehouse |
| 3 | **Data Analyst** | Studies who churned and reports the main patterns |
| 4 | **Data Scientist** | Trains and evaluates the churn prediction model |
| 5 | **ML Engineer** | Deploys the model to score customers nightly |
| 6 | **MLOps Engineer** | Monitors performance and triggers retraining when it drops |
| 7 | **BI Developer** | Builds the dashboard where the retention team sees risky customers |

In small companies, one person often does several of these jobs.

---

## 17. Skills Matrix Across Roles

**Core** = essential, **Useful** = helpful, **Basic** = light working knowledge, **-** = rarely needed.

| Skill | Data Analyst | Business Analyst | BI Developer | Data Engineer | Analytics Engineer | Data Scientist | ML Engineer | MLOps Engineer | AI Engineer | Research Scientist |
|---|---|---|---|---|---|---|---|---|---|---|
| **SQL** | Core | Basic | Core | Core | Core | Core | Useful | Basic | Basic | Basic |
| **Python** | Useful | Basic | Basic | Core | Basic | Core | Core | Core | Core | Core |
| **Statistics** | Core | Basic | Basic | Basic | Basic | Core | Useful | Basic | Basic | Core |
| **Machine learning** | Basic | - | - | Basic | - | Core | Core | Useful | Useful | Core |
| **Data visualization** | Core | Useful | Core | Basic | Basic | Useful | Basic | Basic | Basic | Useful |
| **Cloud and DevOps** | Basic | - | Basic | Core | Basic | Useful | Core | Core | Useful | Basic |
| **Software engineering** | Basic | - | Basic | Core | Useful | Useful | Core | Core | Core | Useful |
| **Communication and business sense** | Core | Core | Useful | Useful | Useful | Core | Useful | Useful | Useful | Useful |

### Skills almost every data role needs

1. **SQL**, to get data out of databases
2. **A programming language** (usually Python)
3. **Basic statistics**, to avoid wrong conclusions
4. **Clear communication**, because results only matter if people understand them
5. **Problem solving**, to turn vague questions into precise tasks

---

## 18. Choosing a Role and Building Skills

| If you enjoy... | Consider | Skills to build first |
|---|---|---|
| Finding stories in numbers and presenting them | Data Analyst, BI Developer | SQL, Excel, Power BI or Tableau, statistics basics |
| Understanding business problems and people | Business Analyst, Data Product Manager | Requirements gathering, SQL basics, communication |
| Building systems and solving engineering problems | Data Engineer, ML Engineer, MLOps | Python, SQL, Git, cloud basics, Docker |
| Statistics, experiments and prediction | Data Scientist | Python, statistics, scikit-learn (this Phase 4) |
| Building products with AI | AI Engineer | Python, APIs, ML basics |
| Mathematics and inventing new methods | Research Scientist | Linear algebra, probability, deep learning theory |

A common path: start as a **Data Analyst**, then move toward **Data Scientist** or **Data Engineer** as skills grow. Phase 4 builds the foundation for the Data Scientist and ML Engineer paths.

---

## 19. Summary

- Data work is a chain: **collect, store, clean, analyze, model, deploy, maintain**.
- **Data Analyst:** explains what happened. **Business Analyst:** defines what the business needs. **BI Developer:** builds reporting systems.
- **Data Engineer:** builds the pipelines and storage. **Analytics Engineer:** prepares analysis-ready data.
- **Data Scientist:** predicts and discovers using ML. **ML Engineer:** puts models into production. **MLOps Engineer:** keeps them running.
- **AI Engineer:** builds products on pre-trained models. **Research Scientist:** invents new methods.
- Skills fall into four types: **technical, tools, analytical/math and soft.**
- Tools change, but SQL, Python, statistics, problem solving and communication stay valuable everywhere.
- Titles overlap and vary by company, so check the actual responsibilities in a job description.

---
