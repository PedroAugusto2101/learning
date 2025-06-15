# 03. Classification and Logistic Regression

## 03.00 Introduction to Classification

- **Classification** is a type of supervised learning where the output variable, \( y \), can only take on one of a small set of possible values (categories), rather than any number in an infinite range.
- **Examples of classification problems:**
  - Determining if an email is spam (yes/no)
  - Detecting if a financial transaction is fraudulent (fraud/not fraud)
  - Classifying a tumor as malignant or benign

### Binary Classification

- **Binary classification**: Only two possible output classes (e.g., yes/no, true/false, 0/1).
- Common conventions:
  - 0 = negative class (e.g., not spam, not fraudulent, benign)
  - 1 = positive class (e.g., spam, fraudulent, malignant)
- The terms _class_ and _category_ are used interchangeably.
- The choice of which class is 0 or 1 is arbitrary and can be swapped depending on the context.

## 03.01 Linear Regression for Classification: Why It Fails

- **Linear regression** predicts continuous values, not categories.
- Attempting to use linear regression for classification:
  - Fit a straight line to the data.
  - Use a threshold (e.g., 0.5): if output < 0.5, predict 0; if output ≥ 0.5, predict 1.
- **Problem:** Linear regression can output values less than 0 or greater than 1, which do not make sense for classification.
- **Sensitivity to outliers:** Adding a single outlier can shift the decision boundary (threshold) significantly, leading to poor classification.

### Example Visualization

- Suppose we plot tumor size (x-axis) vs. label (y-axis: 0 for benign, 1 for malignant).
- Linear regression fits a line, and a threshold (e.g., 0.5) is used to separate classes.

```python
# Visualizing linear regression for classification
import matplotlib.pyplot as plt
import numpy as np

# Example data
X = np.array([1, 2, 3, 4, 5, 6, 7, 20])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Fit linear regression
coeffs = np.polyfit(X, y, 1)
y_pred = np.polyval(coeffs, X)

plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, y_pred, color='red', label='Linear Regression')
plt.axhline(0.5, color='green', linestyle='--', label='Threshold 0.5')
plt.xlabel('Tumor Size')
plt.ylabel('Label (0=Benign, 1=Malignant)')
plt.legend()
plt.title('Linear Regression for Classification')
plt.show()
```

- Adding an outlier (e.g., a data point far to the right) can shift the regression line and the threshold, leading to incorrect classifications.

## 03.02 Logistic Regression: A Better Approach

- **Logistic regression** is designed for classification, not regression, despite its name.
- The output of logistic regression is always between 0 and 1, representing the probability that \( y = 1 \).
- Logistic regression avoids the problems of linear regression for classification:
  - Outputs are always valid probabilities.
  - Less sensitive to outliers in the input space.
- The decision boundary (threshold, e.g., 0.5) is more stable and meaningful.

### Key Points

- Logistic regression is widely used for binary classification problems.
- The name "regression" is historical; logistic regression is fundamentally a classification algorithm.

```python
# Visualizing logistic regression curve
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import expit

X = np.linspace(0, 10, 100)
# Example logistic regression parameters
beta_0 = -5
beta_1 = 1
y_prob = expit(beta_0 + beta_1 * X)

plt.plot(X, y_prob, color='red', label='Logistic Regression')
plt.axhline(0.5, color='green', linestyle='--', label='Decision Boundary (0.5)')
plt.xlabel('Tumor Size')
plt.ylabel('Probability (Malignant)')
plt.title('Logistic Regression Output')
plt.legend()
plt.show()
```

## 03.03 Terminology Recap

- **Negative class (0):** Absence of the property (e.g., not spam, benign).
- **Positive class (1):** Presence of the property (e.g., spam, malignant).
- The assignment of 0 and 1 is arbitrary and can be reversed depending on the
