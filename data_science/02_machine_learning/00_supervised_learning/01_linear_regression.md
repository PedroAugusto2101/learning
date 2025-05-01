# **Linear Regression**

---

## **Introduction**

- Regression has its roots in **Francis Galton’s 19th-century studies**, where he noticed that children's heights **regress toward the population mean**.
  - **Example**: A basketball player of **2.2m** may have a child around **2.0m**—tall, but closer to average.

## **Supervised Learning: Regression Context**

- Regression is a **supervised learning** task, where models learn from **labeled training data** to predict **continuous numeric outputs**.
- It differs from **classification**, which predicts **categories** with a limited number of outcomes.
- Regression problems have **infinitely many possible outputs**.

| Input (X)         | Output (Y)              | Example Task           |
| ----------------- | ----------------------- | ---------------------- |
| email             | spam? (0/1)             | spam filter            |
| audio             | transcribed text        | speech recognition     |
| English           | Spanish                 | machine translation    |
| ad, user info     | clicked? (0/1)          | ad click prediction    |
| image, radar data | positions of other cars | autonomous vehicles    |
| smartphone image  | defect? (0/1)           | visual inspection      |
| house features    | price (in $)            | house price prediction |

![img](../../img/Screenshot%20from%202025-05-01%2014-39-16.png)

- **Training data** consists of:

  - **X (features)**: independent variables (e.g., house size)
  - **Y (target)**: dependent variable (e.g., house price)
  - Each data point is represented as a pair **(x, y)**

- The model learns a **function f(x) = ŷ**, where **ŷ** is the prediction for **y**.
  - **f** is called the **model**.
  - The goal is to find **f** that generalizes well to new, unseen data.

## **Understanding Regression Models**

- Regression models aim to capture the **relationship between inputs and outputs** by fitting a function that approximates the data distribution.
- There are many types of regression models suited for different problems and data complexities.

![img](../../img/Screenshot%20from%202025-04-29%2007-06-20.png)

### **Linear Regression**

- The **simplest and most widely used** regression algorithm.
- It fits a **straight line** to the data:  
  **f(x) = w·x + b**

  - **w** = weight/slope
  - **b** = bias/intercept

- The model **predicts numeric values** (e.g., predicting house price based on size).
- When using only **one input feature**, it's called **simple linear regression** or **univariate linear regression**.
- Despite its simplicity, linear regression often serves as a **foundation** for more complex models.

### **Least Squares Method**

- A classical method used to estimate **w** and **b** by **minimizing the sum of squared errors** between predictions and actual values.
- This approach can also be extended to **multiple features** (multivariate linear regression).

### **Regression Flow**

1. **Input**: Training data (features and targets)
2. **Model training**: The algorithm fits the best line (function f)
3. **Prediction**: For new input x, compute **ŷ = f(x)**
4. **Evaluation**: Compare **ŷ** with actual **y** using error metrics

### **Common Terminology**

- **X**: input feature(s), independent variable(s)
- **Y**: target/output, dependent variable
- **m**: number of training examples
- **ŷ (y-hat)**: model’s predicted value for y

## **Other Regression Techniques**

- **Polynomial Regression**: Fits curves; used when the relationship is nonlinear.
- **Ridge & Lasso Regression**: Add regularization to avoid overfitting in linear models.
- **Logistic Regression**: Despite its name, used for **classification**.
- **Support Vector Regression (SVR)**: Finds a margin around the best fit line using support vectors.
- **Decision Trees & Random Forests**: Model complex nonlinear relationships with tree structures.
- **K-Nearest Neighbors (KNN) Regression**: Predicts by averaging the target values of the closest neighbors.
- **Neural Networks**: Capable of modeling highly complex nonlinear patterns; computationally intensive.

## **Regression Objective**

- The core objective is to **minimize prediction error**.
- Common error metrics:

  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **Mean Absolute Error (MAE)**

- Methods differ in how they fit the model:
  - **Least Squares**: minimizes squared differences
  - **MAE-based methods**: more robust to outliers

![img](../../img/Screenshot%20from%202025-03-31%2013-35-46.png)
![img](../../img/Screenshot%20from%202025-03-31%2013-37-46.png)

## **Final Notes**

- Choose the regression algorithm based on:

  - **Data structure and size**
  - **Relationship complexity**
  - **Overfitting/underfitting concerns**

- Linear regression is not only a **simple yet powerful tool**, but also a **starting point** for understanding and developing more advanced models.
- Regression is essential whenever the goal is to **predict numeric values** from input features.
