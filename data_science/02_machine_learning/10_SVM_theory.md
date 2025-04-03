# Support Vector Machines (SVM)

- **Support Vector Machines (SVMs)** are **supervised learning methods** used for both **classification** and **regression** tasks.
- Given a **training dataset**, where each example belongs to a category, **SVM creates a model** that classifies new examples into one of the categories using a **non-probabilistic approach**.

## How SVM Works

- An **SVM model** represents training examples as **points in space**, mapped in such a way that **categories are separated with the largest possible margin**.
- **New data points** are classified based on the **region** they fall into.
- Given the dataset below, an **intuitive** way to classify it is by using a **hyperplane**:

![image.png](../img/Screenshot%20from%202025-04-03%2014-01-46.png)

- However, for **some datasets**, there are **multiple possible hyperplanes**.
- The goal is to **find the hyperplane that maximizes the margin between classes**:

![image.png](../img/Screenshot%20from%202025-04-03%2014-02-46.png)

- The **points that touch the margin lines** are called **support vectors**:

![image.png](../img/Screenshot%20from%202025-04-03%2014-03-46.png)

## Kernel Trick: Handling Non-Linearly Separable Data

- The **kernel trick** allows SVM to handle **non-linearly separable data**.
- It **maps data** into a **higher-dimensional space**, where it **becomes linearly separable**, then **transforms it back**.

![image.png](../img/Screenshot%20from%202025-04-03%2014-04-46.png)

- The **kernel function** transforms the **input space** into a **higher-dimensional feature space**, where a **linear separation** is possible.
- After classification in the **higher dimension**, the results are **mapped back**:

![image.png](../img/Screenshot%20from%202025-04-03%2014-05-46.png)

## Practical Application

- We will first **study SVMs** using a dataset that predicts whether a **tumor is malignant or benign**.
- Then, we will apply **SVM** to the **famous Iris dataset**.
- Additionally, we will **optimize our model** using **GridSearch** to find the best hyperparameters.
