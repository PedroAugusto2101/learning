# 09. Feature Scaling in Machine Learning

## 09.00 Understanding Feature Ranges and Parameter Values

When building machine learning models, especially with gradient descent, the range of values that each feature (independent variable) takes can significantly affect the learning process.

- **Feature Range vs. Parameter Size:**  
  If a feature has a high range of values (e.g., house size from 300 to 2000 square feet), its associated parameter (weight) tends to be small. Conversely, if a feature has a low range (e.g., number of bedrooms from 0 to 5), its parameter tends to be large. This is because the model compensates for the scale of the feature by adjusting the parameter so that their product contributes appropriately to the prediction.

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

## 09.02 How to Normalize Features

- **What to Do:**  
  To address the issue of features with very different ranges, you should normalize or scale the features so that they all take on comparable ranges of values.

- **Name of the Technique:**  
  This process is called **feature scaling** or **normalization**.

### Common Methods

- **Min-Max Scaling:**  
  Rescales features to a fixed range, usually [0, 1].
- **Standardization (Z-score):**  
  Rescales features so they have mean 0 and standard deviation 1.

After scaling, gradient descent can follow a more direct path to the global minimum, improving both speed and performance of
