# Logistic Regression

- A **classification** method.
- **Examples** of classification models:
  - Email filters (spam or not).
  - Predicting defaulting customers.
  - Disease diagnosis.

## Difference from Linear Regression

- **Linear regression** predicts continuous values.
- Despite its name, **logistic regression** solves classification problems where we predict discrete categories.
- **Binary classification** convention: classes are represented as **0** and **1**.
- **Linear regression is not ideal** for classification since it allows probabilities beyond **100%** or below **0%**.
  ![img](../img/Screenshot%20from%202025-04-01%2016-34-46.png)

## Logistic Function (Sigmoid)

- The **logistic function** (also called the **sigmoid**) restricts outputs between **0 and 1**.
- We apply the **sigmoid function** to linear regression predictions to transform them into probabilities.
  ![img](../img/Screenshot%20from%202025-04-01%2016-36-46.png)

### Interpretation of Sigmoid Outputs

- The **output values** represent the probability of belonging to class **1**.
- After training a logistic regression model, we evaluate it using a **confusion matrix**, instead of metrics used in linear regression.

## Confusion Matrix

- Example: **Disease testing** scenario
  ![img](../img/Screenshot%20from%202025-04-01%2016-41-46.png)

| Actual \ Predicted | No (0) | Yes (1) |
| ------------------ | ------ | ------- |
| **No (0)**         | TN     | FP      |
| **Yes (1)**        | FN     | TP      |

- **Basic Terminology**:
  - **True Positive (TP)**: Correctly predicted as positive.
  - **True Negative (TN)**: Correctly predicted as negative.
  - **False Positive (FP)**: Incorrectly predicted as positive.
  - **False Negative (FN)**: Incorrectly predicted as negative.

### Performance Metrics

![img](../img/Screenshot%20from%202025-04-01%2016-43-46.png)

- **Accuracy**:
  - Measures the proportion of correct predictions.
  - Formula: **(TP + TN) / Total**
  - Example: **150 / 165 = 0.91 (91%)**
- **Misclassification Rate**:
  - Measures the proportion of incorrect predictions.
  - Formula: **(FP + FN) / Total**
  - Example: **15 / 165 = 0.09 (9%)**
