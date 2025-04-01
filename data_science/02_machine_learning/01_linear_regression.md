# **Linear Regression Theory**

## **Introduction**

- Developed from **Francis Galton’s** research in the **19th century**, studying the relationship between **parents' and children's heights**.
- He found that:
  - A **child’s height** tends to be **similar to the parents’ height**.
  - However, the child's height will likely **regress toward the population average**.
- **Example:**
  - If a **basketball player** is **2.2 meters** tall, his child is likely to be **tall** but probably **not as tall**, around **2.0 meters**.

## **Understanding Linear Regression**

- The simplest example of **linear regression** is **finding the regression curve** for **two data points**.
- The goal is to **draw a line that best fits the points**.
- Linear regression is a method to find the best-fit straight line through a set of data points to predict values.
  - Example: Predicting someone's height based on their age using a straight line.

## **Least Squares Method**

- The **classical method** for linear regression is the **least squares method**.
- It finds the line that **minimizes the sum of squared distances** from all points to the line.
- This technique can be extended to **datasets with multiple points**.

## **Objective of Linear Regression**

- **Minimize the vertical distance** from each point to the line.
- ![img](../img/Screenshot%20from%202025-03-31%2013-35-46.png)
- Different methods can be used, such as:
  - **Minimizing the sum of squared distances (Least Squares Method).**
  - **Minimizing the sum of absolute errors.**
- - ![img](../img/Screenshot%20from%202025-03-31%2013-37-46.png)
- Despite different approaches, the **underlying principle remains the same**: finding the best fit line to model relationships in data.
