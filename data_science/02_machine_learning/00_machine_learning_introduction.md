# Machine Learning: Introduction

## **What is Machine Learning?**

- A **data analysis method** that **automates model building**.
- Uses **algorithms that iteratively learn from data**, allowing computers to **discover hidden patterns** without being explicitly programmed.
- Defined by **Arthur Samuel (1959)** as the **field of study that gives computers the ability to learn without being explicitly programmed**.
- Example: In the **checkers experiment**, a machine improved its gameplay by analyzing **thousands of moves and positions**, identifying those that often led to **wins or losses**.
  - If trained with only a few games (e.g., 10), the performance would drop drastically due to **insufficient exploration of possibilities**.

## **Applications of Machine Learning**

- **Fraud detection**
- **Search engine ranking**
- **Automated online advertising**
- **Predicting equipment failures**
- **Financial asset pricing models**
- **Intrusion detection in networks**
- **Recommendation systems**
- **Customer segmentation**
- **Sentiment analysis in texts**
- **Pattern recognition in images**
- **Spam filtering in emails**

## **Lifecycle of a Machine Learning Model**

1. **Data Acquisition** →
2. **Data Cleaning** ↔ **Test Data** ↔ **Model Testing** ↔ **Training Data & Model Building** →
3. **Practical Deployment**

## **Types of Machine Learning Algorithms**

1. **Supervised Learning**
   - Uses **labeled data** to train a model and **predict labels** for new data.
   - **Most commonly used** in real-world applications, with **rapid advancements**.
2. **Unsupervised Learning**
   - Works with **unlabeled data** to **identify patterns and groupings**.
3. **Reinforcement Learning**
   - Agents learn to perform actions based on **trial-and-error experiences**.
4. **Recommendation Systems**
   - Often treated as a **hybrid category**, combining techniques from supervised and unsupervised learning.

### **Supervised Learning**

- Model is trained using **input data with correct labels**.
- Example: Predicting equipment failure using **technical specifications** of components labeled as **"Failed (F)"** or **"Not Failed (NF)"**.
- The model adjusts iteratively based on **training data**.
- Model accuracy is validated using a **test dataset**.

### **Unsupervised Learning**

- No pre-defined labels; the algorithm **identifies hidden structures** in the data.
- The goal is to **group or classify data** based on similarities.
- Common techniques:
  - **Self-organizing maps**
  - **K-means clustering**
  - **Singular Value Decomposition (SVD)**
- Used in:
  - **Topic modeling in text analysis**
  - **Anomaly detection**
  - **Recommendation systems**

### **Reinforcement Learning**

- **Mainly used in robotics, gaming, and navigation**.
- The algorithm learns by **trial and error**, optimizing **long-term rewards**.
- The agent must **select actions** that **maximize expected rewards** over time.
- The final goal is to develop an **optimal decision-making policy** based on the agent’s **current state**.
