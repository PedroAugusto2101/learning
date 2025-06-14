# 11. Polynomial Regression and Feature Engineering

## 11.00 Introduction to Polynomial Regression

Polynomial regression extends linear regression by allowing the model to fit curves, not just straight lines, to the data. This is achieved by creating new features from the original input feature(s) by raising them to higher powers.

### Example: Housing Price Prediction

Suppose you have a dataset where the feature $x$ is the size of a house in square feet. If a straight line does not fit the data well, you can use polynomial regression to fit a curve:

- **Quadratic Model:**  
  Includes $x$ and $x^2$ (size and size squared) as features.

  $$
  f(x) = w_1 x + w_2 x^2 + b
  $$

  However, a quadratic model may not always make sense for all data, as it can eventually decrease, which may not align with real-world expectations (e.g., house prices should not decrease as size increases).

- **Cubic Model:**  
  Adds $x^3$ (size cubed) as a feature.
  $$
  f(x) = w_1 x + w_2 x^2 + w_3 x^3 + b
  $$
  This allows the model to fit more complex curves, potentially providing a better fit for the data.

## 11.01 Feature Engineering with Polynomial and Nonlinear Features

- **Polynomial Features:**  
  By raising the original feature to different powers (e.g., $x^2$, $x^3$), you create new features that enable the model to capture non-linear relationships.

- **Alternative Transformations:**  
  You are not limited to powers. For example, you can use the square root of $x$ as a feature:
  $$
  f(x) = w_1 x + w_2 \sqrt{x} + b
  $$
  The square root function increases less steeply as $x$ grows and never decreases, which may be more appropriate for some datasets.

## 11.02 Importance of Feature Scaling in Polynomial Regression

When using polynomial or nonlinear features, feature scaling becomes even more important:

- **Range Differences:**  
  If $x$ ranges from 1 to 1,000, then $x^2$ ranges from 1 to 1,000,000, and $x^3$ from 1 to 1,000,000,000. These large differences can cause optimization algorithms like gradient descent to perform poorly unless features are scaled to similar ranges.

- **Best Practice:**  
  Always apply feature scaling when using polynomial or nonlinear features to ensure efficient and stable training.

## 11.03 Choosing Features for Your Model

- **Flexibility:**  
  You have many choices in how to engineer features—using powers, roots, or other transformations. The best choice depends on the data and the problem context.

- **Model Selection:**  
  In practice, you can compare different models with different sets of features and use performance metrics to decide which features to include.

## 11.04 Summary

Polynomial regression and feature engineering allow you to fit more flexible, non-linear models to your data by creating new features from existing ones. Proper feature scaling is essential when using polynomial features to ensure effective optimization. The choice of features is a key part of building successful machine learning models, and experimenting with different transformations can lead to better
