# What is Machine Learning?

## 🔍 Definition

- Subfield of **Artificial Intelligence (AI)** that enables systems to **learn and improve** from experience **without explicit programming**.
- Uses algorithms trained on data to **detect patterns** — ML does **not create** patterns, it finds them.
- Algorithms analyze data, identify trends, and make **predictions or decisions** based on it.
- **Data is key**: the quality and quantity of data are essential to the model’s success.
- ML has existed for decades, but recent advances in **big data** and **computational power (e.g., GPUs)** have made it more powerful and precise.

## 🧠 What is Learning?

- Learning = the ability to **adapt, modify, and improve** behavior and responses — a fundamental human trait.
- ML aims to replicate human learning in machines.
- This is achieved through **math + programming**, the languages we use to communicate with computers.
- Strong foundations in **math** and **coding** are crucial to mastering ML.
- ML is a method of **data analysis** that automates building **analytical models** to find hidden patterns without being explicitly programmed for a specific task.

---

# Data Science vs. Machine Learning

## 🔗 Relationship

- **Closely related fields**, but not the same.
- **Data Science** is a broad field focused on **collecting, processing, analyzing, and interpreting** large volumes of data to extract insights and knowledge.
- **Machine Learning (ML)** is a subfield of AI that focuses on **developing algorithms and models** that learn from data to make predictions or decisions.
- ML provides the **tools and techniques** for **predictive analysis** and **pattern discovery** within Data Science.
- 👉 Every ML project is a **Data Science** project, but **not every** Data Science project involves ML.

---

# Types of Machine Learning

## ✅ Supervised Learning

- Algorithm is trained on **labeled data** (inputs and outputs are known).
- Goal: **learn a function** to map inputs to outputs and predict new data.
- All models make errors — the goal is to minimize the error.
- **Examples**: Linear Regression, Decision Tree Classifiers.
  ![img](../img/Screenshot%20from%202025-04-08%2021-43-46.png)

## 🔍 Unsupervised Learning

- Algorithm is trained on **unlabeled data** (no predefined output).
- Goal: identify **hidden patterns or structures** (e.g., clusters or dimensionality reduction).
- Can be used to label data first, then apply supervised models.
- **Examples**: Clustering (e.g., K-Means), Principal Component Analysis (PCA).
  ![img](../img/Screenshot%20from%202025-04-08%2021-44-46.png)

## 🎮 Reinforcement Learning

- Agent learns by interacting with an environment, receiving **rewards or punishments**.
- Goal: **maximize cumulative reward** over time.
- **Examples**: Board games, robotic control, process optimization, trading bots.
  ![img](../img/Screenshot%20from%202025-04-08%2021-45-46.png)

---

# Supervised Learning

## 🔢 Regression

- Supervised learning technique used to **predict continuous values**.
- Goal: model the relationship between a **dependent variable (y)** and one or more **independent variables (x)**.
- When predicting multiple targets → **multi-target regression**.
- **Examples**: Predicting house prices (based on size, location, etc.), forecasting temperature from historical data.
  ![img](../img/Screenshot%20from%202025-04-09%2007-36-46.png)

## 🏷️ Classification

- Also supervised learning, but used to **predict categories or classes**.
- Goal: map inputs to one or more **discrete categories**.
- Summary: if you want to predict a **number**, use **regression**; if you want to predict a **class**, use **classification**.
- **Examples**: Spam detection, medical diagnosis (e.g., disease prediction).
  ![img](../img/Screenshot%20from%202025-04-09%2007-37-46.png)

---

# Unsupervised Learning

## 🔗 Clustering

- Unsupervised learning technique that **groups similar data points** together.
- Goal: discover hidden **patterns or structures** in the data.
- Common algorithm: **K-Means**, which assigns data points to clusters based on proximity to centroids.
- **Examples**: Market segmentation, customer behavior analysis, anomaly detection.

![img](../img/Screenshot%20from%202025-04-09%2007-38-46.png)

> Uses computational processing to perform clustering (e.g., customer segmentation).

![img](../img/Screenshot%20from%202025-04-09%2007-39-46.png)

---

# Feature Engineering

- Process of using **domain knowledge** to create new features that **enhance model performance**.
- Involves **transforming**, **combining**, and **creating new features** from existing ones to provide more relevant information to the model.

## 🔧 Common activities:

- **Feature Selection** – choosing the most relevant variables.
- **Feature Transformation** – modifying features (e.g., normalization, log-transform).
- **Feature Creation** – deriving new features (e.g., ratios, interactions).
- **Categorical Feature Encoding** – converting categories into numerical format (e.g., one-hot, label encoding).

---

# Machine Learning Pipeline

![img](../img/Screenshot%20from%202025-04-19%2020-18-02.png)

1. **Problem Definition** – Clearly understand what needs to be solved.
2. **Data Collection & Exploration** – Gather and explore available data.
3. **Preprocessing** – Clean, transform, and prepare data.
4. **Model Training** – Apply ML algorithms to learn patterns from the data.
5. **Hyperparameter Tuning** – Adjust model parameters to improve performance.
6. **Model Evaluation** – Assess performance using suitable metrics.
7. **Model Selection** – Choose the best-performing model.
8. **Testing & Versioning** – Validate with unseen data and track versions.
9. **Deployment** – Deploy the model to production for real-world usage.

---

# MLOps – Operationalizing Machine Learning

As organizations mature in their machine learning (ML) practices, they begin to automate and streamline the ML lifecycle — this is the foundation of **MLOps**.

Inspired by **DevOps** in software development, MLOps aims to manage the end-to-end ML workflow efficiently and at scale.

![MLOps Lifecycle](../img/Screenshot%20from%202025-04-19%2020-08-31.png)

## What is MLOps?

MLOps (Machine Learning Operations) is a set of practices that combines ML and DevOps to **automate, monitor, and manage** the lifecycle of ML models.

It spans from **model development** to **deployment and continuous monitoring** in production.

## Core Components of MLOps:

- **Model Development & Training** – Data preparation, feature engineering, and model building.
- **Continuous Integration (CI)** – Automated testing and validation of code and models.
- **Continuous Deployment (CD)** – Automating deployment to staging/production environments.
- **Model Monitoring & Management** – Track performance and detect model drift.
- **Data Management** – Versioning, lineage, and quality checks.
- **ML Pipeline Automation** – End-to-end automation of the ML workflow.
- **Governance & Compliance** – Ensuring auditability, fairness, and accountability.
- **Collaboration & Reproducibility** – Enabling teamwork and repeatable experiments.

---

# Model Monitoring and Maintenance

Monitoring and maintaining ML models in production is essential to ensure they remain **accurate**, **reliable**, and **efficient** over time.

## Why is it Important?

- Models may experience **performance degradation** due to:
  - Changes in data distribution (data drift)
  - New patterns not seen during training (concept drift)
  - External changes (seasonality, behavior shifts, etc.)

## Key Activities

- **Continuous Performance Tracking**:
  - Monitor metrics like **accuracy**, **precision**, **recall**, and **F1-score**
  - Detect **anomalies**, **data drift**, and **concept drift**
- **Model Updating**:

  - **Re-training** models on new data
  - **Updating training datasets**
  - **Hyperparameter tuning** to adapt to new patterns

- **Version Control and Documentation**:
  - Keep detailed records of model versions, configurations, and performance over time
  - Ensure **reproducibility** and **auditability** for all model updates

## Goal

Adapt the model to changing data and maintain high performance in real-world scenarios.

---

# MLOps Tools and Frameworks

MLOps relies on a set of tools and frameworks to streamline the **development**, **deployment**, and **management** of ML models.

## Key Tools

1. **MLflow**

   - Open-source platform to manage the ML lifecycle.
   - Tracks experiments, manages models, and facilitates deployment.
   - Components: Tracking, Projects, Models, Registry.

2. **Kubeflow**

   - ML toolkit for Kubernetes.
   - Enables scalable ML pipelines, experiment tracking, and model serving.

3. **TensorFlow Extended (TFX)**

   - End-to-end platform for deploying production ML pipelines using TensorFlow.
   - Includes components like data validation, transformation, and model analysis.

4. **Apache Airflow**

   - Workflow orchestration tool.
   - Schedules and manages data pipelines and ML workflows.

5. **Data Version Control (DVC)**
   - Version control system for machine learning projects.
   - Tracks data, models, and experiments—integrates with Git.

## Purpose

These tools support **automation**, **scalability**, **versioning**, and **collaboration**, making it easier to manage ML systems in production environments.
