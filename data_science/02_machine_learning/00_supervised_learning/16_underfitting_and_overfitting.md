# 16. UNDERFITTING AND OVERFITTING IN MACHINE LEARNING

## 16.00 Introduction

- Understanding the challenges of underfitting and overfitting in machine learning models.

### What are Underfitting and Overfitting?

- **Underfitting** occurs when a model is too simple to capture the underlying patterns in the data, resulting in poor performance even on the training set. This is also known as **high bias**.
- **Overfitting** happens when a model is too complex and fits the training data too closely, including noise and outliers, leading to poor generalization on new, unseen data. This is referred to as **high variance**.

## 16.01 Examples in Regression

### Linear Regression Example

- **Scenario:** Predicting housing prices based on house size.
- **Underfitting:** Using a simple linear model (straight line) fails to capture the true relationship if the data is more complex. The model cannot fit the training data well, indicating high bias.
- **Just Right:** Introducing a quadratic model (using features like x and x²) allows the model to fit the data better and generalize well to new examples.
- **Overfitting:** Using a fourth-order polynomial (features x, x², x³, x⁴) can fit the training data perfectly, but the resulting curve is overly complex and does not generalize well to new data, indicating high variance.

## 16.02 Generalization and Model Selection

### Generalization

- The goal in machine learning is to build models that perform well not only on the training data but also on new, unseen examples. This property is called **generalization**.

### Bias-Variance Tradeoff

- **High Bias (Underfitting):** Model is too simple, ignores relevant patterns.
- **High Variance (Overfitting):** Model is too complex, captures noise as if it were a pattern.
- The ideal model achieves a balance, fitting the data well without being too rigid or too flexible.

## 16.03 Analogy: Goldilocks Principle

- The process of finding the right model is similar to the Goldilocks story: one model is too simple (underfitting), another is too complex (overfitting), and the best model is "just right," balancing bias and variance.

## 16.04 Examples in Classification

### Logistic Regression Example

- **Scenario:** Classifying tumors as malignant or benign using features like tumor size and patient age.
- **Underfitting:** A simple logistic regression model with a linear decision boundary may not separate the classes well (high bias).
- **Just Right:** Adding quadratic features allows for a more flexible decision boundary (e.g., an ellipse), improving classification and generalization.
- **Overfitting:** Using many high-order polynomial features creates a highly complex decision boundary that fits the training data perfectly but fails to generalize (high variance).

## 16.05 Addressing Underfitting and Overfitting

- To achieve a model that is "just right," it is important to select the appropriate model complexity and features.
- In upcoming lessons, techniques such as **regularization** will be introduced to help control overfitting and improve model generalization.

## 16.06 Summary

- **Underfitting (High Bias):** Model too simple, poor fit to training data.
- **Overfitting (High Variance):** Model too complex, fits training data too closely, poor generalization.
-
