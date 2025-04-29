# **Regression Algorithms**

## **Introduction**

- Regression originated from **Francis Galton’s** studies in the **19th century**, analyzing the relationship between **parents' and children's heights**.
  - He observed that children's height **regresses toward the population average**.
  - **Example:** A basketball player with **2.2m** height may have a child around **2.0m**—still tall, but not as extreme.

## **Supervised Learning: Regression Context**

- Regression is a type of **supervised learning**, where the model learns to map **inputs (X)** to **continuous outputs (Y)** based on labeled data.
- It requires **training data with correct answers** to learn patterns.

| Input (X)         | Output (Y)              | Example Task           |
| ----------------- | ----------------------- | ---------------------- |
| email             | spam? (0/1)             | spam filter            |
| audio             | transcribed text        | speech recognition     |
| English           | Spanish                 | machine translation    |
| ad, user info     | clicked? (0/1)          | ad click prediction    |
| image, radar data | positions of other cars | autonomous vehicles    |
| smartphone image  | defect? (0/1)           | visual inspection      |
| house features    | price (in $)            | house price prediction |

- After training on input-output pairs, the model is tested with **new inputs** to predict **unseen outputs**.
- In regression specifically, the **output is a number** (continuous value), not a category.

## **Understanding Regression Models**

- The goal of regression is to find a function that best describes the relationship between input variables and a continuous target variable.
- There are various regression algorithms, each suitable for different patterns and data characteristics.
  ![img](../../img/Screenshot%20from%202025-04-29%2007-06-20.png)

### **Linear Regression**

- The most basic form; fits a **straight line** to the data.
- Example: Predicting a person’s height based on age using a straight line.
- Works best when the relationship between X and Y is approximately linear.

### **Least Squares Method**

- A **classical technique** for linear regression.
- Finds the line that **minimizes the sum of squared errors** between predicted and actual values.
- Can be applied to datasets with **multiple features**.

### **Other Regression Techniques**

- **Polynomial Regression:** Fits **curves** instead of straight lines; useful when data has nonlinear patterns.
- **Ridge and Lasso Regression:** Include **regularization** to prevent overfitting in linear models.
- **Logistic Regression:** Used for **classification**, despite the name; predicts the probability of class membership.
- **Support Vector Regression (SVR):** Uses support vectors to find the optimal margin in regression tasks.
- **Decision Trees & Random Forests:** Model complex nonlinear relationships using **tree structures**.
- **K-Nearest Neighbors Regression:** Predicts by **averaging the target values** of the nearest neighbors.
- **Neural Networks:** Can approximate complex nonlinear functions; more powerful but computationally intensive.

## **Regression Objective**

- All regression models aim to **minimize the prediction error**.
- Common error metrics include:

  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **Mean Absolute Error (MAE)**

- Methods differ in how they fit the model:
  - **Least Squares:** Minimizes the sum of squared differences.
  - **Absolute Error Minimization:** More robust to outliers.

![img](../../img/Screenshot%20from%202025-03-31%2013-35-46.png)
![img](../../img/Screenshot%20from%202025-03-31%2013-37-46.png)

## **Final Notes**

- Choosing the right regression algorithm depends on:
  - Data structure
  - Complexity of relationships
  - Overfitting/underfitting trade-off
- Regression is essential for problems where we want to **predict numeric values** from input features.
