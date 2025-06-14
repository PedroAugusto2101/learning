# 09. Feature Engineering in Machine Learning

## 09.00 Understanding Feature Ranges and Parameter Values

When building machine learning models, especially those using gradient descent, the range of values that each feature (independent variable) takes can significantly affect the learning process.

- **Feature Range vs. Parameter Size:**  
  If a feature has a high range of values (e.g., house size from 300 to 2000 square feet), its associated parameter (weight) tends to be small. Conversely, if a feature has a low range (e.g., number of bedrooms from 0 to 5), its parameter tends to be large. The model compensates for the scale of the feature by adjusting the parameter so that their product contributes appropriately to the prediction.

### Example

Suppose we want to predict house prices using two features:

- x1: Size of the house (300–2000 sq ft)
- x2: Number of bedrooms (0–5)

If we set parameters as w1 = 50, w2 = 0.1, and b = 50, the predicted price is unrealistically high. Swapping the parameter values (w1 = 0.1, w2 = 50, b = 50) gives a much more reasonable prediction, matching the true price.

## 09.01 Why Analyze Feature Ranges?

- **Importance of Analysis:**  
  It is crucial to analyze the ranges of independent variables before training a machine learning model. Features with very different ranges can cause the optimization process (like gradient descent) to behave inefficiently, leading to slow convergence or suboptimal solutions.

### Impact on Gradient Descent

- When features have different scales, the cost function contours become elongated ellipses. Gradient descent may "bounce" back and forth, taking a long time to reach the minimum.
- If features are scaled to similar ranges, the contours become more circular, allowing gradient descent to converge more quickly and efficiently.

- **Which models are sensitive to feature scaling?**  
  Models that rely on distance calculations or gradient-based optimization are especially sensitive to feature scaling. These include:

  - Linear regression (with gradient descent)
  - Logistic regression
  - Neural networks
  - k-Nearest Neighbors (k-NN)
  - Support Vector Machines (SVM)
  - Principal Component Analysis (PCA)
  - Clustering algorithms (e.g., k-means)

  Tree-based models (like decision trees and random forests) are generally less sensitive to feature scaling.

## 09.02 How to Normalize Features

- **What to Do:**  
  To address the issue of features with very different ranges, you should normalize or scale the features so that they all take on comparable ranges of values.

- **Name of the Technique:**  
  This process is called **feature scaling** or **normalization**.

### Common Methods

#### Min-Max Scaling

- **How it works:**  
  Divide each feature value by the maximum value of that feature.
  - Example: If x1 ranges from 300 to 2000, scaled x1 = x1 / 2000 (now ranges from 0.15 to 1).
  - For x2 ranging from 0 to 5, scaled x2 = x2 / 5 (now ranges from 0 to 1).

#### Mean Normalization

- **How it works:**  
  Subtract the mean and divide by the range (max - min).
  - Example: For x1, mean μ1 = 600, range = 2000 - 300 = 1700.
    - Normalized x1 = (x1 - μ1) / (2000 - 300)
    - Resulting values typically range from negative to positive (e.g., -0.18 to 0.82).

#### Z-score Normalization (Standardization)

- **How it works:**  
  Subtract the mean and divide by the standard deviation.
  - Example: For x1, mean μ1 = 600, standard deviation σ1 = 450.
    - Z-score normalized x1 = (x1 - μ1) / σ1
    - Values typically range around -1 to +1, but can extend further.

### Choosing a Normalization Method

- **How to choose:**

  - Use **min-max scaling** when you want features in a specific range (e.g., [0, 1]).
  - Use **mean normalization** or **z-score normalization** when you want features centered around zero, especially if your data contains outliers or you want to preserve the distribution's shape.
  - For most machine learning algorithms sensitive to feature scale, **z-score normalization** is a safe default.

- **Rule of thumb:**  
  Aim for features to range roughly from -1 to +1, but small deviations are acceptable. If a feature has a much larger or smaller range than others, it's usually best to rescale it.

- **When in doubt:**  
  There is almost never harm in applying feature scaling. If unsure, it is recommended to scale your features.

## 09.03 Feature Engineering: Creating New Features

The choice and creation of features can have a huge impact on your model's performance. Feature engineering involves using domain knowledge or intuition to design new features, often by transforming or combining existing ones, to make it easier for the learning algorithm to make accurate predictions.

### Example: House Price Prediction

Suppose you have two features for each house:

- x1: Width (frontage) of the lot
- x2: Depth of the lot

A basic model might use both features separately:

$$
f(x) = w_1 x_1 + w_2 x_2 + b
$$

However, you might notice that the area of the land (width × depth) could be more predictive of price. You can create a new feature:

- x3 = x1 × x2 (area of the plot)

Now, your model can be:

$$
f(x) = w_1 x_1 + w_2 x_2 + w_3 x_3 + b
$$

This allows the model to learn whether frontage, depth, or area is most important for predicting price. Creating such new features is a core part of feature engineering and can significantly improve model performance.

Feature engineering can also enable your model to fit not just straight lines, but curves and more complex, non-linear relationships in your data.

## 09.04 Summary

Feature scaling and feature engineering are essential steps in building effective machine learning models. Scaling ensures all features contribute equally to the optimization process, while engineering new features can unlock better predictive power by leveraging domain knowledge and intuition. Both steps help your algorithms learn more efficiently and make more
